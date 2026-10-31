# Workflow and decision gates

## 1. Task contract

Before choosing tools, translate the request into a short contract:

- target: species, construct, sequence/structure source, relevant state;
- design type and primary endpoint: binding, selectivity, cross-reactivity, agonism/antagonism, catalysis, stability, or another function;
- constraints: length, scaffold, mutations, chemistry, expression, delivery, pH, budget, compute, and experimental availability;
- outputs: candidate count, sequence/structure files, metrics, report, and handoff format;
- acceptance: predeclared gates, controls, missing-data policy, stop/continue conditions.

Resolve conflicting requirements using the user's current priorities. A contest brief, paper protocol, and user objective can differ; preserve each and identify which controls the current run.
- **Review cadence:** Record which stages the user wants reviewed before proceeding. Stop at an explicit hold point. If the current task explicitly authorizes autonomous execution, carry out the agreed routine stages without seeking routine approval; do not infer new expensive work from a draft plan or old authorization.

## 2. Target/input gate

Do not launch expensive generation until target inputs can be traced. Compare the actual observed chain sequence with the intended sequence and construct. Record chain/entity mapping and author-vs-canonical numbering. Check biological assembly, oligomer state, partner composition, crystallization truncations, mutations, unresolved residues, glycans/other modifications, disulfides, membrane orientation, conformational state, and whether separate chains came from compatible complexes. For cross-species work, align the actual constructs and map interface residues; names alone are not evidence.

If a prior audit has clear provenance and the relevant inputs/version are unchanged, reuse it. Recheck changed or decision-critical invariants; do not repeat expensive predictions solely to recreate an existing verified artifact.

Use known binders, ligands, substrates, or competitors as contextual controls only after verifying their source, species, construct, assay, epitope/site, and evidence type. A structure model can support a geometric hypothesis; it does not establish a biological label.

## 3. Method and run gate

For every method, record intended output, input assumptions, model/version, training/template dependence where known, and applicability to the requested endpoint. Distinguish installed, smoke-tested, run-complete, output-audited, and scientifically interpreted. When ranking depends on predicted complex poses, test the full input/model/scoring path on positive controls matched to the target construct and state. Check pose/interface recovery, not just a confidence score. If a control fails, diagnose construct, template, assembly, chain mapping, and method applicability before using those scores to rank candidates or set cutoffs.

For network-dependent tools, verify the actual endpoint and artifact the program requests (DNS, TLS, URL/path, download size/hash, and load), not just generic connectivity or a mirror homepage. Track model weights, affinity weights, CCD/data files, MSA services, template search, compilation, inference, and output validation as separate stages; stop the success claim at the last stage supported by evidence.

Use an evidence-linked run state for each consequential action: `proposed` (recommendation only), `prepared` (inputs/config created), `submitted` (accepted by a scheduler or service), `running` (active process/allocation observed), `process-complete` (terminal state or exit code observed), `output-verified` (expected artifacts and schema/count/content checks passed), and `scientifically-interpreted` (task criteria and evidence limits assessed). Record whether the evidence was observed in the current environment, pasted by the user, or reported in an earlier conversation. Never advance a state from a suggestion, a progress fragment, a directory-size change, or an assistant's narrative alone. For a completed batch, reconcile expected and observed candidate/model counts and list failures before calling the batch output-verified.

Keep a run manifest with immutable run ID; target/sequence/structure hashes; configuration and criteria version; tool versions; seeds; generated scaffold/family IDs; command; host/environment; start/end; exit code; logs; expected outputs; actual outputs; and failure reason. Check a small representative input and output schema before scaling.

## 4. Sampling and ranking gate

Keep separate counts for design backbones, sequences per backbone, scaffold families, random seeds, model/rank repeats, and experimental replicates. Deduplicate sequences and structures at a stated method/threshold. Repeated scoring of related candidates is not independent validation.

Preserve every generated candidate and its status. Use explicit states such as `generated`, `prediction_failed`, `missing_metric`, `failed_gate`, `retained_for_review`, and `experimentally_tested`; do not encode missing data as zero or a failing score. Check that ranking code evaluates every frozen gate; compare its pass/fail expression with the written criteria and independently recompute sample rows before publishing counts.

Before deleting or overwriting source data, logs, intermediate structures, or detailed tables, inventory exact paths and downstream dependencies, preserve hashes/manifests, and make a recoverable copy or archive. Prefer reversible moves until the replacement is checked and no analysis depends on the original.

## 5. Validation gate

Use staged checks appropriate to the design:

- sequence/schema and construct validity;
- monomer fold or local geometry;
- complex pose and chain mapping;
- interface chemistry, shape, buried area, clashes, and unsatisfied polar groups;
- energy or affinity models only when endpoint, units, and applicability are clear;
- robustness across seeds/models/target states and relevant homologs;
- functional or binding assay, when available.

Do not impose a universal ipTM, pLDDT, interface-area, contact, or energy cutoff. Configure the task's cutoffs before looking at the ranking; if criteria change, version them and report which candidates changed status.

## 6. Report-claim audit

Before handing off ranked candidates or scientific conclusions, enumerate every quantitative or decision-changing statement in the complete report and map it to its source row/field, calculation, and frozen acceptance criterion. Compare the gate's name and plain-language interpretation with the actual scoring expression; recalculate counts and denominators from per-sample records, including errors and missing rows. Reconcile the report, CSV/FASTA, task configuration, and final candidate IDs. After editing a correction, reread the entire final report and derivative files for stale contradictions. A disclaimer does not repair a contradictory claim elsewhere. Use [report-claim-audit.md](report-claim-audit.md); the automated results check verifies declared configuration and evidence mappings but cannot discover all prose claims.

## 7. Handoff gate

The report should make the following questions answerable:

- What was the requested endpoint and which criteria were frozen?
- Which inputs, constructs, assemblies, and residue maps were used?
- How many unique sequences, scaffolds/families, predictions, failures, and retained candidates exist?
- What evidence supports each claim, and what evidence is missing?
- What changed from the prior run and why?
- What is the next experiment or analysis most likely to change the decision?

Use `templates/design_task_handoff.md` and `templates/design_run_config.json` from the project archive when available.

## 8. Lightweight audit tool

The bundled `scripts/audit_records.py` has three checks:

- `python scripts/audit_records.py chunk-coverage INDEX.json CHECKPOINTS.jsonl` compares indexed chunks, semantic-review states, checkpoint identities, and declared gaps. A passing check means the two ledgers agree; it does not prove the source archive is complete or that every attachment was inspected.
- `python scripts/audit_records.py coverage MESSAGE_LEDGER.csv` checks per-message source locators, import/review status, duplicate source-message keys, and reviewer notes.
- `python scripts/audit_records.py results CANDIDATES.csv TASK_CONFIG.json` checks required task metrics/columns, duplicates, configured gates, pass counts recomputed from configured criteria, and whether claims include the evidence required by that task.

The task config owns its required fields, gates, and criteria. The utility supplies no general scientific cutoff. Keep `claim_requirements` specific to the endpoint and evidence requested; for example, a structural score alone must not satisfy a configured experimental-binding claim. The script checks declared evidence tokens and data consistency; it cannot decide whether an assay, model, or biological interpretation is scientifically sufficient.

