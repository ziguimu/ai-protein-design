# Final report claim audit

Use this check before delivering any ranked list or scientific report. It is especially important when scripts, summaries, tables, and prose are generated in separate steps.

## Claim-to-evidence review

Read the complete deliverable, including headings, captions, tables, footnotes, warnings, and copied older text. For every quantitative or decision-changing statement, record:

| Report location and claim | Source file/table/field | Recalculation or query | Frozen criterion / field meaning | Scope and caveat | Status |
|---|---|---|---|---|---|
| ... | ... | ... | ... | ... | verified / qualified / unsupported |

At minimum, reconcile reported counts and rates with the underlying rows; distinguish sequences, unique sequences, backbones, scaffold families, samples, predictions, and experiments. For a gate or “vote”, compare the named meaning with the exact Boolean expression in the scoring code and the frozen task configuration. Verify numerator, denominator, failed/missing rows, and any aggregation rule. Do not infer that a field named `pose_votes`, `affinity`, or `pass` actually measures that property without checking its computation.

For selection/ranking claims, confirm that the final IDs are produced by a reproducible rule or document the human selection rationale and deviations. Verify the selected sequences/structures match the final FASTA/CSV and their provenance.

## Corrections and version consistency

When correcting a report, update or clearly supersede every affected claim. Then reread the entire final file and its derived summaries to find stale or contradictory text. A warning or correction note at the top does not neutralize a conflicting assertion later in the document. Keep the original report and version history, but make the active report unambiguous.

## Limits of automation

The bundled results auditor can recalculate configured criteria, compare configured and reported gates/counts, and check declared claim-evidence requirements. It does not extract every natural-language claim from a report or determine that a human-provided evidence mapping is scientifically valid. A person must enumerate and review the full report claims; mark unsupported statements for removal or qualification. Do not describe the config check as semantic report verification.
