# Evidence and claim boundaries

Use the strongest wording justified by the evidence actually available. Report evidence by layer; do not compress it into one “confidence” or “affinity” score.

| Evidence layer | Supports | Does not establish by itself |
|---|---|---|
| Sequence validity / developability heuristic | Sequence parses, follows design constraints, has a stated liability profile | Correct fold or binding |
| Monomer structure prediction | A plausible fold under a specified model/input | Complex pose, binding, affinity, or function |
| Complex pose prediction | A plausible relative arrangement under a specified model | Experimental binding, affinity, specificity, or biological activity |
| Interface geometry/chemistry | Contact pattern, shape, clashes, polar satisfaction, and selected interface descriptors | Binding free energy or measured affinity |
| Physical/energy calculation | Model-dependent energetic comparison under named assumptions | Calibrated affinity unless independently validated for the target domain |
| Affinity predictor | Its defined score/estimate within documented applicability and calibration | Assay outcome outside that domain; function or specificity |
| Dynamics/robustness analysis | Stability or sensitivity within modeled conditions and sampling | Binding in vivo or functional effect |
| Binding experiment | Binding under the stated construct, assay, and conditions | Functional effect or cross-species activity unless tested |
| Functional experiment | The measured functional endpoint under the stated conditions | Unmeasured mechanisms, contexts, or species |

## Reporting rules

- Name the model, version, input, score definition, units, and direction before interpreting a score.
- Explain whether metrics are comparable across constructs, models, or runs; do not assume they are.
- Distinguish measured values from predictions, structural descriptors, literature statements, and user-provided labels.
- For affinity language, state whether evidence is experimental or a predictor estimate. A high pose score alone supports a structural-priority hypothesis, not “high affinity”.
- For cross-species claims, compare verified ortholog constructs and test both species in an appropriate assay; a plausible model on one species is not cross-reactivity evidence.
- For functional designs, binding and function are separate endpoints. A binder is not automatically an agonist, antagonist, enzyme, or delivery molecule.
- If no candidate meets frozen gates, report zero passing candidates. If a small set is requested, label them as provisional candidates and state the evidence gap instead of relaxing gates after seeing results.
