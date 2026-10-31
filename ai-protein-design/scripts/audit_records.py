#!/usr/bin/env python3
"""Audit semantic-review coverage and task-configured screening records.

No universal scientific thresholds are embedded. Pass a JSON task config.
"""
from __future__ import annotations

import argparse
import csv
import json
from pathlib import Path
from typing import Any


def read_csv(path: Path) -> tuple[list[dict[str, str]], list[str]]:
    with path.open(encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return list(reader), reader.fieldnames or []


def audit_coverage(path: Path) -> dict[str, Any]:
    rows, fields = read_csv(path)
    required = {"source_id", "conversation_id", "role", "import_status", "semantic_review_status", "source_locator"}
    errors: list[str] = []
    if not rows:
        errors.append("Coverage ledger is empty; no source messages are accounted for")
    if not required.issubset(fields):
        errors.append(f"Missing columns: {', '.join(sorted(required - set(fields)))}")
    id_column = "message_id" if "message_id" in fields else "message_id_or_ordinal"
    if id_column not in fields:
        errors.append("Missing columns: message_id or message_id_or_ordinal")
    seen: set[tuple[str, str, str]] = set()
    duplicates: list[str] = []
    for i, row in enumerate(rows, start=2):
        key = (row.get("source_id", ""), row.get("conversation_id", ""), row.get(id_column, ""))
        if key in seen:
            duplicates.append(f"line {i}: {key}")
        seen.add(key)
        if row.get("import_status") == "imported" and not row.get("source_locator"):
            errors.append(f"line {i}: imported row has no source locator")
        if row.get("semantic_review_status") == "reviewed" and row.get("import_status") != "imported":
            errors.append(f"line {i}: reviewed row is not marked imported")
        if row.get("semantic_review_status") == "reviewed" and not row.get("reviewer_note", "").strip():
            errors.append(f"line {i}: reviewed row has no review note")
        if row.get("semantic_review_status") == "excluded_with_reason" and not row.get("reviewer_note", "").strip():
            errors.append(f"line {i}: excluded row has no exclusion reason")
    pending = sum(r.get("semantic_review_status") not in ("reviewed", "excluded_with_reason") for r in rows)
    return {"rows": len(rows), "pending_semantic_review": pending, "duplicate_keys": duplicates,
            "errors": errors, "pass": not errors and not duplicates and pending == 0}


def audit_chunk_coverage(index_path: Path, checkpoints_path: Path) -> dict[str, Any]:
    index = json.loads(index_path.read_text(encoding="utf-8"))
    checkpoints: list[dict[str, Any]] = []
    errors: list[str] = []
    for line_no, line in enumerate(checkpoints_path.read_text(encoding="utf-8-sig").splitlines(), start=1):
        if not line.strip():
            continue
        try:
            checkpoints.append(json.loads(line))
        except json.JSONDecodeError as exc:
            errors.append(f"checkpoint line {line_no} is invalid JSON: {exc}")
    index_ids = [str(row.get("chunk_id", "")) for row in index]
    checkpoint_ids = [str(row.get("chunk_id", "")) for row in checkpoints]
    duplicate_index_ids = sorted({x for x in index_ids if x and index_ids.count(x) > 1})
    duplicate_checkpoint_ids = sorted({x for x in checkpoint_ids if x and checkpoint_ids.count(x) > 1})
    index_set, checkpoint_set = set(index_ids), set(checkpoint_ids)
    missing_checkpoints = sorted(index_set - checkpoint_set)
    extra_checkpoints = sorted(checkpoint_set - index_set)
    pending_chunks = sorted(str(row.get("chunk_id", "<missing-id>")) for row in index
                            if row.get("semantic_review_status", row.get("status", row.get("review_status")))
                            != "semantic_reviewed")
    status_by_id = {str(row.get("chunk_id", "")): row.get(
        "status", row.get("review_status", row.get("semantic_review_status"))) for row in checkpoints}
    checkpoint_status_mismatch = sorted(cid for cid in index_set & checkpoint_set
                                        if status_by_id.get(cid) != "semantic_reviewed")
    declared_gaps = [{"chunk_id": row.get("chunk_id"), "gaps": row.get("gaps", [])}
                     for row in checkpoints if row.get("gaps")]
    if duplicate_index_ids:
        errors.append("Chunk index contains duplicate IDs")
    if duplicate_checkpoint_ids:
        errors.append("Checkpoints contain duplicate IDs")
    if missing_checkpoints:
        errors.append("Some indexed chunks have no checkpoint")
    if extra_checkpoints:
        errors.append("Some checkpoints are absent from the index")
    if pending_chunks:
        errors.append("Some indexed chunks are not semantically reviewed")
    if checkpoint_status_mismatch:
        errors.append("Some checkpoint statuses are not semantic_reviewed")
    return {"indexed_chunks": len(index), "checkpoints": len(checkpoints),
            "duplicate_index_ids": duplicate_index_ids,
            "duplicate_checkpoint_ids": duplicate_checkpoint_ids,
            "missing_checkpoints": missing_checkpoints, "extra_checkpoints": extra_checkpoints,
            "pending_chunks": pending_chunks,
            "checkpoint_status_mismatch": checkpoint_status_mismatch,
            "declared_gaps": declared_gaps, "errors": errors, "pass": not errors}


def audit_results(results_path: Path, config_path: Path) -> dict[str, Any]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    rows, fields = read_csv(results_path)
    required_metrics = list(config.get("required_metrics", []))
    required_columns = list(config.get("required_columns", []))
    id_col = config.get("candidate_id_column", "candidate_id")
    missing_columns = [m for m in [id_col, *required_metrics, *required_columns] if m not in fields]
    errors: list[str] = []
    if missing_columns:
        errors.append(f"Missing configured columns: {', '.join(missing_columns)}")
    ids = [r.get(id_col, "").strip() for r in rows] if id_col in fields else []
    duplicates = sorted({x for x in ids if x and ids.count(x) > 1})
    if duplicates:
        errors.append(f"Duplicate candidate IDs: {', '.join(duplicates)}")
    sample_col = config.get("sample_id_column")
    duplicate_samples: list[str] = []
    if sample_col and sample_col in fields:
        sample_ids = [r.get(sample_col, "").strip() for r in rows]
        duplicate_samples = sorted({x for x in sample_ids if x and sample_ids.count(x) > 1})
        if duplicate_samples:
            errors.append(f"Duplicate sample IDs: {', '.join(duplicate_samples)}")
    missing_values: dict[str, list[str]] = {}
    for metric in required_metrics:
        if metric in fields:
            absent = [r.get(id_col, f"row-{i}") for i, r in enumerate(rows, start=1) if not r.get(metric, "").strip()]
            if absent:
                missing_values[metric] = absent
    if missing_values:
        errors.append("Required metric values are missing")

    criteria = list(config.get("criteria", []))
    criterion_errors: list[str] = []
    passing_ids: list[str] = []
    operators = {
        "<": lambda a, b: a < b, "<=": lambda a, b: a <= b,
        ">": lambda a, b: a > b, ">=": lambda a, b: a >= b,
        "==": lambda a, b: a == b, "!=": lambda a, b: a != b,
    }
    for criterion in criteria:
        metric, op = criterion.get("metric"), criterion.get("op")
        if metric not in fields or metric not in required_metrics:
            criterion_errors.append(f"Criterion metric {metric!r} must be present and listed as required_metrics")
        if op not in operators:
            criterion_errors.append(f"Unsupported criterion operator: {op!r}")
    if criteria and not criterion_errors:
        for i, row in enumerate(rows, start=1):
            passed = True
            for criterion in criteria:
                try:
                    actual = float(row[criterion["metric"]])
                    threshold = float(criterion["value"])
                    passed = passed and operators[criterion["op"]](actual, threshold)
                except (KeyError, ValueError, TypeError):
                    passed = False
            if passed:
                passing_ids.append(row.get(id_col, f"row-{i}"))
    if criterion_errors:
        errors.extend(criterion_errors)
    reported_count = config.get("reported_pass_count")
    calculated_count = len(passing_ids) if criteria and not criterion_errors else None
    if reported_count is not None and calculated_count is None:
        errors.append("reported_pass_count is configured but no valid task criteria are available")
    elif reported_count is not None and int(reported_count) != calculated_count:
        errors.append(f"Reported pass count {reported_count} does not match configured-criteria count {calculated_count}")
    configured_gates = config.get("gates", {})
    observed_gates = config.get("reported_gates", {})
    gate_drift = {k: {"configured": configured_gates.get(k), "reported": observed_gates.get(k)}
                  for k in set(configured_gates) | set(observed_gates)
                  if configured_gates.get(k) != observed_gates.get(k)}
    if gate_drift:
        errors.append("Reported gates differ from the frozen task configuration")
    claim_requirements = config.get("claim_requirements", {})
    unsupported_claims: dict[str, dict[str, list[str]]] = {}
    for item in config.get("reported_claims", []):
        claim = item.get("claim", "")
        supplied = set(item.get("evidence", []))
        required = claim_requirements.get(claim)
        if not claim:
            errors.append("A reported claim has no claim name")
        elif required is None:
            unsupported_claims[claim] = {"required": [], "reported": sorted(supplied)}
        elif not set(required).issubset(supplied):
            unsupported_claims[claim] = {"required": list(required), "reported": sorted(supplied)}
    if unsupported_claims:
        errors.append("Reported claims exceed or lack configured evidence support")
    return {"rows": len(rows), "missing_columns": missing_columns, "missing_values": missing_values,
            "duplicate_candidate_ids": duplicates, "sample_id_column": sample_col,
            "duplicate_sample_ids": duplicate_samples, "calculated_passing_ids": passing_ids,
            "calculated_pass_count": calculated_count, "reported_pass_count": reported_count,
            "gate_drift": gate_drift, "unsupported_claims": unsupported_claims, "errors": errors,
            "pass": not errors}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    sub = ap.add_subparsers(dest="mode", required=True)
    c = sub.add_parser("coverage"); c.add_argument("ledger", type=Path)
    cc = sub.add_parser("chunk-coverage"); cc.add_argument("index", type=Path); cc.add_argument("checkpoints", type=Path)
    r = sub.add_parser("results"); r.add_argument("results", type=Path); r.add_argument("config", type=Path)
    args = ap.parse_args()
    if args.mode == "coverage":
        result = audit_coverage(args.ledger)
    elif args.mode == "chunk-coverage":
        result = audit_chunk_coverage(args.index, args.checkpoints)
    else:
        result = audit_results(args.results, args.config)
    print(json.dumps(result, ensure_ascii=False, indent=2))
    return 0 if result["pass"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
