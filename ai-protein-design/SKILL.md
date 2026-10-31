---
name: ai-protein-design
description: Use when planning, generating, evaluating, or handing off AI-assisted protein designs, including binders, peptides, interfaces, or functional proteins; especially when target structure, affinity claims, candidate ranking, or compute provenance matters.
---

# AI protein design

Help the user reach a defensible design decision or candidate set. Choose the workflow for the design objective and available evidence; do not equate a plausible structure with a validated molecule.

## Workflow

1. **Set the actual endpoint.** Capture the user's primary objective, target species and construct, desired function, affinity/selectivity priorities, cross-species requirements, design constraints, available compute/assays, deliverable, and stopping condition. If the user asks to agree on direction first, settle that before running design. Mark any user-requested review checkpoint and stop at that explicit hold point. If the user authorizes autonomous execution through an agreed plan, continue through routine phases without asking for each step. A proposed plan or authorization from an earlier task is not approval to start a new compute run.
2. **Audit target and inputs before expensive work.** Read actual sequences and structures. Confirm chain/entity identity, numbering, construct boundaries, species, biological assembly, oligomeric state, missing regions, modifications, conformations, and relevant binding partners/known binders. Record mappings and unresolved assumptions. Reuse traceable prior audits when inputs and versions are unchanged; verify the invariants relevant to this task without repeating costly work by default. Use current authoritative sources when biological or tool facts may have changed.
3. **Choose methods for the endpoint.** State each method's input, output, applicability, dependencies, and evidence level. Run a low-cost input/smoke check before a large batch. Do not select a method just because it is installed or emits an affinity-like field.
4. **Freeze task-specific acceptance criteria before ranking.** Record required metrics, definitions, units, thresholds, missing-data handling, controls, and changes. Never borrow numeric cutoffs from another target or model without task-specific calibration. Keep failed and excluded samples in the ledger.
5. **Track sample identity and diversity.** Preserve candidate, sequence, scaffold/family, seed, model, run, and prediction identifiers. Report the number of independent scaffolds/families separately from sequences and repeated predictions.
6. **Evaluate in evidence layers.** Separate sequence validity and fold, complex pose, interface chemistry/geometry, energy or calibrated affinity estimate, dynamics, function, and experiment. Select only the levels relevant to the user endpoint; report what remains untested.
7. **Verify execution and outputs.** Record environment, inputs and hashes, config, command, timestamps, exit status, logs, expected and observed files, and data joins. Label each step as proposed, prepared, submitted, running, process-complete, output-verified, or scientifically interpreted, and name the evidence source for each status. A suggested command is not an executed action; a submitted job is not a running job; process completion is not output verification; a passed computational gate is not experimental binding.
8. **Deliver the decision with limits.** Present candidates and ranking basis, controls, diversity, generated/eligible/retained counts, rejected/failed counts, evidence by layer, unresolved risks, and the next decision-changing test. Before delivery, map each quantitative or decision-changing report claim to its source data, calculation, and frozen criterion; check field names against their actual formulas and reread the complete report after edits for stale contradictions. Use “predicted structural candidate” unless stronger evidence supports stronger language.
9. **Update the case library at a task milestone.** When a design task ends or reveals a useful correction, add a source-linked case and a proposed experience change. Preserve old judgments and versions. Promote a general rule only when evidence and scope support it; keep conflicting observations and task-specific thresholds conditional.

## References

Read [workflow.md](references/workflow.md) for stage gates, [evidence.md](references/evidence.md) for claim boundaries, [report-claim-audit.md](references/report-claim-audit.md) for final report reconciliation, and [task-branches.md](references/task-branches.md) when the design type changes the objective or validation. Consult the local case library at `D:\Codex\AI_protein_design_skill\experience\experience_log.md` and relevant `reviews/cases/` entries when available; treat each as evidence with its stated scope, not as universal thresholds.

For project coverage and result checks, use `scripts/audit_records.py` with a task-specific config. See its CLI help and `references/workflow.md`; it embeds no universal scientific cutoff.
