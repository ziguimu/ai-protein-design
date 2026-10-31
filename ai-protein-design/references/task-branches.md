# Task branches

Use the shared workflow, then add branch-specific checks. These branches are a routing aid, not a claim that every branch has equal evidence in the local case archive.

## Protein binders and interface design

Define epitope/site, target state, accessibility, competitors, species/constructs, and whether the endpoint is binding, selectivity, cross-reactivity, or function. Inspect target assembly and interface residues before generation. Track scaffold-family diversity separately from sequence count. Validate both monomer fold and complex pose, then interface chemistry and appropriate affinity evidence. Do not let docking confidence substitute for affinity.

## Peptide ligands and functional designs

Identify whether the intended endpoint is receptor binding, agonism, antagonism, biased signaling, stability, or another functional effect. Verify peptide processing, termini, disulfides/PTMs, receptor construct/state, membrane context, endogenous ligands, and assay readout. Structural similarity or docking does not establish agonism. Compare against relevant ligand/control structures only after confirming numbering and construct compatibility.

## MHC-I peptide targets and pMHC binders

Define the HLA allele, presented peptide sequence and length, mutation position, and whether the goal is peptide-dependent binding, mutant-versus-WT selectivity, or another endpoint. Keep HLA heavy chain, peptide, and β2-microglobulin chain identities and residue/token maps explicit. Include β2m in the modeled context when required by the biological construct; inspect binder contacts with peptide, HLA, and β2m separately. For mutation-specific recognition, compare matched mutant and WT pMHC and include no-peptide or irrelevant-peptide controls when the construct and assay support them. Do not treat binding to HLA/β2m or a predicted peptide pose as evidence of mutant-peptide specificity. Confirm the intended specificity with an appropriate binding or functional assay.

## pH-conditional binding

Use this branch only when pH-dependent binding or release is part of the current objective. Specify the pH values or range, desired direction of binding change, target construct/state, and assay endpoint. Keep constructs and other assay conditions matched across pH comparisons. Treat histidine or other titratable-residue placement as a design hypothesis; residue count and predicted structure scores do not demonstrate pH response. Validate binding or release across the specified pH conditions with relevant controls. If pH response is not requested, do not add pH optimization or validation as an automatic gate.

## Enzyme or catalytic designs

Define substrate, reaction, catalytic residues, cofactors, protonation/metal states, and measurable kinetic endpoint before choosing a design method. Verify geometry and chemical plausibility, then evaluate substrate binding separately from catalytic activity. A folded enzyme-like structure or favorable docking pose does not establish turnover. Use this branch as a planning checklist; consult current domain methods and literature for specific catalytic models.

## Other protein design tasks

For stability, expression, solubility, immunogenicity, delivery, or assembly objectives, define the property and assay first. Select predictors with a relevant validation domain and state uncertainty. Do not reuse binder-interface metrics as substitutes for a different endpoint.
