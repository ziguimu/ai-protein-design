# Codex TfR1 design execution review

> **Publication note / 发布说明:** This is a redacted review note derived from a local case-review document. It is not a complete source conversation or a byte-for-byte transcript. Source coverage and unresolved checks stated below remain in force. Local paths, host identifiers, network addresses, contact details and full conversation UUIDs were redacted or shortened; scientific claims were not changed by this sanitization. The unmodified source is retained locally.
>
> 本文件是从本地案例审阅文档整理的脱敏审阅记录，不是完整原始对话，也不是逐字聊天导出。来源覆盖范围和未决核查状态仍以正文为准。已脱敏本地路径、主机标识、网络地址、联系方式并缩短完整会话 UUID；本次脱敏不修改科学结论。未修改的来源文件留存本地。


## Source scope

Primary source: local Codex rollout `CODEX_TFR1_MAIN_1`, event 7–19 (2026-10-28T07:53:31Z–07:53:41Z). Prepared segment `reviews/prepared/codex_chunks/CODEX_TFR1_MAIN_1_visible_C001.txt`; checkpoint recorded separately. This is the start of the task only.

## User objective and constraints

- Produce 3–5 TfR1 design sequences.
- Prioritize human affinity; mouse affinity is desirable.
- pH response is not a required design objective or validation; a few His or other potentially responsive residues may remain.
- First agree on design direction and key uncertainties, then execute autonomously.
- User points to a prior ChatGPT conversation, but the Codex input contains only a bounded preview of that thread.

## Evidence status

This segment establishes the user request and the assistant's plan to inspect prior work, challenge requirements, local WSL, and the specified skill. It contains no target structure review or design output. Later segments must establish what was actually inspected, which direction was agreed, and what was executed.

## Initial access/tool reconnaissance (events 19–26)

- The captured session's tool inventory showed no `read_thread` or Skill invocation endpoint. The local `grill-me` file only instructed calling a Skill tool; successful use is not evidenced here.
- Early reconnaissance inspected the local WSL/drive state and visible project files. This segment contains no target-structure evidence or design execution. The absence of an API is specific to the captured session/tool inventory and should not be generalized to all Codex sessions.

## WSL and existing project inventory (event 30)

- The first WSL inventory call returned a Windows-side access error in corrupted/Unicode-misdecoded terminal text; the exact message cannot be recovered from this transcript representation. It is not evidence WSL was usable. A second attempt follows in event 34.
- `<LOCAL_PRP>` contained several unrelated protein-design projects (EGFR, GLP1R, GPD, pMHC, TNF). This inventory did not establish a TfR1 design directory or biological suitability.

## WSL status and available assets (event 39)

- The follow-up `wsl --list --verbose` completed successfully and reported Ubuntu as **Stopped**, WSL version 2. This resolves the earlier ambiguous output: the distribution existed but was not running at that moment.
- The local pMHC folder had candidate structures and analysis scripts from the prior G12D workflow. These establish available local precedent, not TfR1 design assets or transferable quality thresholds.
- The Codex `grill-me` file was found, but no successful `grilling` skill invocation is present in this segment.

## WSL capacity, prior pMHC assets, and challenge requirements (event 50)

- **Verified WSL execution:** command ran under Ubuntu as `ziguimu`; installed paths included RFdiffusion, ProteinMPNN, Boltz, ColabFold, Rosetta, USalign, PyMOL and several conda environments. At capture, GPU was RTX 5070 Laptop, 8151 MiB total/6879 MiB free; `/` had 896 GB available and `/mnt/d` 284 GB. These are point-in-time observations.
- The only task-specific local artifacts displayed were for KRAS G12D–HLA-A*11:01: a geometry review queue for 20 structures. Its own notes say it is not an affinity ranking; binder D is backbone-only; C6 minimum may not be an Asp OD distance; only 5 candidates had OD1/OD2 measurements; broad HLA contact does not establish mutation specificity. It is precedent for auditing caveats, not evidence for TfR1.
- Search output from the official Challenge 4 page states human TfR1 binding at pH 7.4 and no detectable binding at pH 6.0 as a required property. This conflicts with the user's initial request to skip pH design/validation. Preserve both: user may intentionally deprioritize the competition requirement, but any result then cannot be called challenge-compliant. Later turns must establish the agreed scope.
- Boltz affinity documentation surfaced in the same search distinguishes small-molecule affinity support from protein-protein structure confidence. Do not infer that an available affinity head provides validated binder-target affinity scores.
- The tool output also included generic FAQs and small-molecule sources; these do not establish performance of TfR1 protein-protein predictions.

## Official Challenge 4 requirements and local Boltz audit (events 54 and 58)

The live challenge page was opened and its requirements were read from the captured result. It defines three objectives: human TfR1 measurable KD; pH 7.4 binding with no detectable binding at pH 6.0; and mouse TfR1 cross-reactivity. Ranking prioritizes pH selectivity, then the mouse:human KD ratio among designs with human KD below 1 µM, then lowest human KD. This directly conflicts with the user's initial “affinity first / no pH validation” preference. A later scope decision must identify whether the goal is a competition-compliant entry or a deliberately non-compliant affinity-focused research design. Do not silently satisfy one while claiming the other.

The assay target is a soluble human ectodomain (residues 121–760) homodimer; mouse ectodomain is 123–763. The page recommends the apical domain while preserving transferrin binding. It notes 78% human–mouse identity and 6/9 differences in the apical patch. 11QC/11RN match modeled UniProt residues; older structures can have S142 where the construct has G142; the C-terminal Twin-Strep tag must not be part of the interface. Track-specific design counts, formats, length limits, submission fields and public disclosure terms also appear in the page and need task-specific handling.

The user’s local Boltz is 2.2.1 and both confidence and affinity checkpoints exist. However, the local prediction docs explicitly say the affinity property is for a ligand chain (small molecule) and only supports small-molecule/protein affinity. It cannot be called a protein-protein binder-affinity prediction. Model/checkpoint presence is not method applicability.

## User choices and local feasibility/target evidence (events 63–76)

The user answered the direction questions: small single-chain de novo binder (roughly 60–100 aa as proposed), avoid the natural transferrin interface, allow up to 72 hours of local compute. This is a research/selection preference and still conflicts with the official challenge’s mandatory pH and mouse objectives unless later scope changed.

Local feasibility was confirmed: RFdiffusion checkpoint files exist; the RFdiffusion environment reports PyTorch 2.7.1+cu128, CUDA available, RTX 5070 Laptop, with `sm_120` listed. The previous result table and threshold CSV are for KRAS G12D pMHC. That source explicitly labels geometry as non-affinity ranking and notes backbone-only binder limitations. Its ipTM/BSA/etc cutoffs are task-local records and must not become TfR1/general defaults. One Boltz log prints RTX A6000, inconsistent with current local inventory; provenance must be checked before using this as hardware evidence. A targeted search found no run scripts in one GLP1R directory; absence is bounded to that path and is not proof no prior script exists anywhere.

RCSB’s 11QC page identifies an author-assigned C2 human TfR1 ectodomain homodimer, two chains, 639 modeled residues, cryo-EM 2.40 Å, with three glycosylation sites reported. Challenge numbering is 121–760; chain/construct numbering and glycan handling must be explicitly mapped. Proteinbase’s selection prompt says tracks 2/3 selection weighs novelty, diversity and a small confidence set; submitters’ selected methods/metrics are visible and can become public. Selection and competition winning are separate.

## Tool smoke test, old analysis scripts, and structure references (events 81–93)

User clarified the sequence/pH trade-off: keep His optional and subordinate to binder quality; if fewer than three candidates meet the task criteria, deliver only those that pass rather than filling a quota. This is a strong acceptance rule. It remains in tension with the challenge's published pH objective, so “pass” must name the chosen scope.

RFdiffusion import and CUDA tensor test passed despite nonfatal PyTorch deprecation warnings. Review of local analysis code exposed assumptions worth testing before reuse: some code defines the first chain as receptor and all later chains as binder, and one script converts coordinate residue IDs by subtracting one. Those assumptions are unsafe for homodimer-plus-binder complexes unless chain and residue mappings are explicit. A fixed `/tmp` receptor/binder filename also needs care in parallel runs. These are audit leads, not confirmed bugs.

A Boltz log says pynvml is unsupported and fallback/default device information is used for the RTX 5070 Laptop, then prints a fixed A6000-style information line. This is a telemetry/default-value issue; it does not establish that the work ran on A6000. Prior pMHC mutant/WT rows are structural descriptors only; Gly sidechain minima are NaN by definition.

RCSB 3S9L is a TfR1–transferrin complex with iron in transferrin's N-lobe; the viewer sequence includes an artificial N-terminal tag. It can inform ligand-site context, but chain identity, construct and residue numbering must be verified before modeling. Literature/OVO search results provide examples of large-scale RFdiffusion pipelines, multiple filters and sequence/structure clustering, but their cutoffs are target- and campaign-specific; no threshold should be copied wholesale.

## Finalized historical plan and approval boundary (events 98–173)

Additional local tool findings: Boltz CLI help was available; PyRosetta was not, while USalign/TM-align were available. The old ipSAE code maps contact residues by chain-local sequence IDs and indexes the global PAE matrix directly, without chain offsets. For a concatenated multichain matrix this can read the wrong residue pairs. Assistant explicitly rejected direct reuse.

The user accepted the main design choices: 60–100 aa de novo single-chain binder, avoid the transferrin site, max 72 h, binding quality over forced histidines, and deliver only candidates passing criteria even if fewer than three. The user approved a plan that deliberately omitted pH optimization/validation and treated mouse binding as a bonus, despite the formal competition objectives. Any competition-facing claim must expose this divergence.

The approved plan proposed 64 initial backbones and 8 sequences per backbone; later caps of 192 backbones and 96 human first-pass predictions; up to 10 candidates for three Boltz seeds plus two ColabFold models; mouse follow-up on up to 8 designs at two seeds; a 72 h budget with design/prediction stop times; and candidate filters including pLDDT 85, ipTM 0.70, PAE 10 Å, binder RMSD 2.5 Å, severe clash 2.0 Å, and ΔSASA/2 500 Å². These were project-level proposed gates, not benchmark-calibrated affinity criteria or universal standards. The plan also included whole-dimer, glycan, transferrin, sequence/numbering, and reproducibility checks. Proposed means executed results only after later tool evidence.

The user approved the plan before execution. The session remained in plan mode, so the assistant requested a mode switch; the user then repeated execution. Record these as separate gates: plan approval did not itself start computation. The initial proposed output path was D:\GPTwork; subsequent user-directed moves supersede it.

## Initial implementation instructions and working directory (event 176)

The recorded assistant read `executing-plans` and Biopython skill files, then inspected `D:\GPTwork`; no AGENTS.md was found there. The plan execution skill required a durable ledger and continuous execution after approval, which matches the user's autonomous-execution preference. This read-only call did not start a design run or create outputs. The initial workspace listing is historical and later path corrections take precedence.

## Workspace setup and target-input audit: critical species error (events 184–208)

The user explicitly required all task files under `<LOCAL_PRP>\TfR1_challenge4_20261028`; the directory was created. The first progress script records the approved budget, gates, stop conditions, and output contents. It also says no sequences had yet been generated.

**Confirmed input bug:** the fetch script labels `https://rest.uniprot.org/uniprotkb/P12346.fasta` as `mouse.fasta`. The subsequent Biopython output identifies it as `sp|P12346|TRFE_RAT Serotransferrin protein 1 OS=Rattus norvegicus`, 698 aa. It is rat transferrin, not mouse TfR1. This cannot be used to infer or predict mouse TfR1 cross-reactivity. The fetch script checked only that downloaded bytes exceeded 100 and stored a hash; it did not validate accession identity, organism, target name, or expected sequence length. Preserve the later correction, if any, as a separate causal step.

The human P02786 FASTA is full-length 760 aa. Parsed 11QC chains A/B each have 639 standard residues beginning at 122, while the competition construct is 121–760; explicit mapping/coverage checks are required before designing. 3S9L has four parsed chains and hetero components, so chain IDs and receptor/transferrin roles need explicit validation.

This is a general input-validation failure mode: plausible filenames and successful downloads do not prove target identity. Validate accession, species, protein name, sequence, construct, chain, residue numbering and organism before consuming the sequence/structure.

## Wrong mouse input detected and test failure (events 212–228)

The error was investigated before candidate generation. UniProt and mouse references identify **Q62351**, TFR1_MOUSE, 763 aa, as mouse transferrin receptor 1. The historical fetch script was changed/expected to use Q62351, and new tests asserted human P02786/760 aa, mouse Q62351/763 aa, and every standard 11QC residue against the human sequence at its PDB residue number.

The test run failed exactly on the bad `mouse.fasta`: it contained `sp|P12346|TRFE_RAT`, so expected `Q62351` was absent. Human 11QC residue mapping passed. The assistant then told the user the incorrect sequence was caught and replacement was underway. Completion of the replacement and a passing rerun are not in this segment; next events must confirm them.

This is a useful positive pattern: define identity checks, run them before generation, preserve the expected failure, repair source input, then rerun. The test emits `ResourceWarning` because FASTA files are parsed from inline open handles without context managers; this does not explain the identity failure but should be fixed.

## Corrected mouse input and first RFdiffusion smoke run (events 229–246)

The bad `P12346` rat transferrin file was quarantined as `rejected_P12346_not_mouse_TfR1.fasta`; the sequence source was changed to mouse TfR1 `Q62351`. The recorded rerun reports the human accession/length, mouse accession/length and 11QC-to-human residue checks passing. This closes the input identity correction in the conversation; the original wrong download and its detection remain part of the causal record.

The subsequent target preparation reports an apical crop from human 11QC and mouse sequence mapping, alignment of transferrin from 3S9L, patch hotspots 247/244 and 303/327, and an alignment RMSD of 0.68975 Å. These are historical outputs, not independently reproduced facts. The 3S9L chain identity, numbering correspondence, glycan representation and crop boundaries still need raw-file validation before treating them as sound target geometry.

An RFdiffusion smoke run for one 60–80 aa design was launched. The captured log ends while sampling (timestep 32); it does not establish successful completion or a valid binder. The nearby high-confidence prediction artifact is named `PMHC_candidate_03` and belongs to the earlier KRAS G12D pMHC work, not TfR1. No final TfR1 sequence, affinity prediction or experimental validation appears here.

**Causal summary:** wrong species input → identity test fails before design → correct Q62351 substituted and tests pass → target crops and patch inputs prepared → RFdiffusion smoke run starts but completion is not evidenced. Keep these as distinct states in any future progress report.

## Restart request and second-run state inspection (MAIN_2 events 10–51)

The user directed the project into `<LOCAL_PRP>\TfR1_challenge4_20261028` and asked to begin execution. The folder was created and a WSL access check returned `WSL_ACCESS_OK` after a garbled WSL diagnostic. The assistant found existing task files, input-preparation scripts, and a smoke log, then inspected them rather than blindly repeating the run. RFdiffusion checkpoints and ProteinMPNN weights were present. The assistant read plan-execution and scientific-critical-thinking guidance.

The output paired with that inspection includes the approved scope, a status file at `rfdiffusion_smoke`, human P02786 and mouse Q62351 crop metadata, a residue map, scripts, and log tail. The RFdiffusion trace is still stepping through the denoising run (captured through timestep 28); no output structure, completed smoke test, sequence generation, or candidate ranking is established. Files and weights existing on disk are not evidence that the next pipeline stages ran.

The human-to-mouse map is not a trivial same-numbering map: the captured object shows offsets/indels. Confirm mapping from sequence alignment and structure residue IDs before interpreting mouse modeling. The project acceptance values in the status record are per-campaign screening gates, not measured affinity and not general defaults.

## Target preparation checks and completed RFdiffusion smoke (MAIN_2 events 55–114)

At first, the process check found no matching process, no listed work products, and a stale `status.json` still set to `rfdiffusion_smoke`; those observations alone were ambiguous. The assistant reviewed `prepare_targets.py`, input tests and the smoke launcher, then relaunched one RFdiffusion design using patch 1, its metadata hotspots and a 60–80 aa contig. The recorded session later returned `RFdiffusion smoke exit 0` and “Finished design in 1.76 minutes.” This confirms a successful smoke command; the output PDB and structural plausibility await MAIN_2 C004.

Preparation code builds a human crop, aligns a transferrin complex, and scores exposed patch residues after filters for dimer partner, resolved glycan atoms, transferrin, sequon proximity, conservation and aromaticity. It takes chain A from both 11QC and 3S9L and uses common numeric residue IDs for superposition. Chain identity, construct mapping and numbering need validation before trusting the alignment. The tests validate FASTA accession/length and 11QC residue identity at PDB numbering, but do not validate 3S9L mapping, glycan extraction, or full-context binding geometry. Patch score is a heuristic, not epitope evidence.

The user asked whether the run could be unattended. The assistant accurately said the session would not wake itself after it ended, then proposed a WSL background runner and completion status/notification. No recurring Codex monitor is established in this event range.

## Smoke artifact and user correction about monitoring (MAIN_2 events 118–161)

RFdiffusion produced `patch1_short_0.pdb` (71,556 bytes) and its `.trb` metadata (75,434 bytes). This confirms a smoke structure was written, not that it is a viable binder. The ProteinMPNN help lookup used an incorrect helper-script path and failed; the repository listing shows `protein_mpnn_run.py` at the repository root. ColabFold CLI help and Boltz checkpoints were available, but neither is evidence of a TfR1 prediction run.

The user clearly distinguished an unattended WSL job from Codex returning to inspect and continue. The assistant acknowledged it could not stay active or promise to wake up after a conversation ended. The user's requirement for periodic agent checks is carried into the separate monitor/automation sources and must not be misrepresented as implemented merely because a Windows or WSL background job was discussed.

## 10054 connection interruption and automation clarification (MAIN_3 events 7–93)

The user reiterates the desired behavior: Codex should return on a timer, inspect WSL and continue. The conversation separately investigates a `stream disconnected` / Windows 10054 message. A process and Codex-file inventory was attempted; one CIM query failed. SQLite inspection failed because the WindowsApps Python alias could not launch, and the `netsh` command was malformed. The status page showed service health at that time, while official network guidance identified WebSocket/proxy/firewall closure as a possible cause. The assistant properly did not claim this proved a local or WSL root cause. The logs do not establish a network repair.

The important correction: the user was right that Codex has Automations. Search results included official OpenAI documentation distinguishing ChatGPT scheduled tasks from Codex Automations and describing scheduled Codex work that can reuse existing threads and wake to continue long tasks. ChatGPT scheduled tasks in a project have different file-access limits; they should not be confused with local Codex automation. In that historical conversation, the current session tool list had no automation-management interface. That limitation was specific to the live session, not proof that users must rely only on Windows Task Scheduler. The record does not prove an automation was actually created for the TfR1 task.

## 64-backbone sequence campaign and Boltz input preparation (MAIN_3 events 223–375)

The RFdiffusion batch completed four strata of 16 backbones (patch 1/2 × 60–80/80–100 aa), 64 total. The ProteinMPNN startup initially failed because its input glob also counted the standalone smoke PDB (65 instead of 64). The first repair wrote literal `\n` into Python and caused a syntax error; an explicit four-glob repair launched successfully. A sample structure has target chain A (195 residues) and binder chain B (72 residues).

ProteinMPNN completed 64 backbones × 16 sequences = 1,024 sequences. The screening script removed exact duplicates and applied sequence-only filters: 60–100 aa length, max homopolymer ≤5, hydrophobic fraction ≤0.65, alanine fraction ≤0.45 and at least 12 distinct amino acids. Ranking combines the ProteinMPNN score with 0.1×global score, then keeps at most two per backbone. It retained 96 sequences across 56 backbone designs after 498 sequences met these basic filters. This is computational sequence plausibility and diversity filtering; none of these values establish target binding or affinity.

The Boltz input-preparation script wrote 96 human complex YAMLs using only the 195-aa apical crop plus each binder. They omit full-length ectodomain context, the homodimer, glycans and transferrin. Boltz CLI availability and YAML generation are verified; a successful TfR1 prediction is not yet shown. This is a material gap against the earlier plan to assess full-context compatibility.

## Offline Boltz pilot and external MSA boundary (MAIN_3 events 379–450)

The initial Boltz command requested `--use_msa_server`; automatic review rejected it because candidate sequences would be sent to an unspecified external MSA service. The assistant respected the rejection and tried offline mode. Its first edit did not actually add MSA fields, and the Boltz log correctly reported missing MSA. A later explicit line-based edit added `msa: empty` to both target and binder YAML entries. The Boltz2 pilot then completed with zero failed examples and wrote a CIF plus confidence, PAE, PDE and pLDDT files for TFR1_001.

This is one complex-structure prediction, not a KD or experimental-affinity estimate. The run log identifies an RTX 5070 through runtime output while also printing a fixed “NVIDIA RTX A6000” information line; treat the latter as unreliable telemetry. The 96-input batch was discussed but is not yet shown launched here.

## 96-candidate Boltz run and zero-pass structure triage (MAIN_3 events 451–626)

The offline Boltz2 controller completed 96/96 candidate predictions with no failures. One candidate confidence file had directed pair ipTM values of 0.306 (target→binder) and 0.395 (binder→target), chain A/B lengths 195/98, and a 293×293 PAE matrix. These are prediction-structure fields, not affinity outputs.

A common metrics script scored 96 structures and reported **zero** passing its proposed combined gates. Several high-ipTM structures had 30–50 Å binder pose RMSD after aligning the target to the RFdiffusion design, so the untemplated cropped target complex did not preserve the designed interface. The script takes only directional A→B ipTM while the model exposes both directions; this asymmetric choice should be surfaced. Its PAE/BSA/pLDDT/RMSD filters are task-defined geometry gates and do not supply affinity evidence. The crop also omits full dimer/glycan/transferrin context, and the script does not check these or clashes.

A local target-template probe was attempted after the pose-drift diagnosis. Boltz failed to parse the template due to sequence/numbering mismatch. A chain-renumbering attempt proceeded; then a naive SEQRES script printed `SEQRES 2`, exposing a bad two-residue extraction. Template path remains unresolved at this source boundary; don't count the probe as a successful independent confirmation.

## Template-conditioned Boltz probe repair (MAIN_3 events 630–712)

The target template was rebuilt from the full 195-aa metadata sequence and renumbered. The initial SEQRES helper had extracted only two residues; the corrected script used the JSON field and reported `sequence 195 seqres 195`. Boltz then rejected the declared template mapping. Inspection of the local Boltz parser led to changing the protein/template internal ID mapping (`template_id: A1`); the next run completed with zero failed examples and wrote the candidate’s structure and confidence/PAE files.

This probe is template-conditioned using the same target crop used in design. It tests whether a target template can stabilize the modeled fold, but does not independently validate binding. Candidate-level template ipTM, PAE and pose metrics had not yet been extracted at the end of this segment. The first metric command returned WSL access denied; its tool-discovery follow-up is pending in MAIN_3 C014.

## Template score contradiction and provisional shortlist drift (MAIN_3 events 718–801)

The historical tool inventory confirmed that Remote Desktop Commander could query a device and run/read terminal processes, but it was not a Codex Automation scheduler. A first template-metric command failed because `python` was not available in the Ubuntu environment; using the Boltz environment Python succeeded.

For TFR1_041_template, the result was target A 195 aa (mean pLDDT 91.4), binder B 61 aa (mean pLDDT 76.0), directional pair ipTM 0.183/0.194, 67 CA pairs under 10 Å and median symmetric interface PAE 18.12 Å. This sharply contradicts the untemplated ipTM 0.813, PAE 2.89 and pLDDT 86. The full 96-candidate untemplated table had zero passing the combined geometry gates, with top-score pose RMSDs about 29.7–50.3 Å.

Despite the previously approved “deliver fewer or none if nothing passes” rule, the assistant began packaging five high-ipTM sequences as provisional follow-up candidates. That is a decision drift, not a pass. A remote-desktop write attempt failed with a PowerShell quoting/parser error; at this boundary no package files had been written. C017 must confirm what, if anything, was ultimately saved and how it was labelled.

## MAIN_3 C017–C020补充（2026-10-30）

- **候选打包的验收漂移：** 五条高ipTM FASTA及指标表写入成功，文件回执确认存在；每条`pass_core=False`。这是在明确“零条通过、只交达标者”后继续打包，虽标为provisional，仍不得写成合格交付。后续应把用途和失败门槛放在文件名/元数据层，避免暂存项被误认。来源`CODEX_TFR1_MAIN_3` C016–C017，事件758–855。更正C016边界记录：当时只知写入失败，C017确认后续直接文件写入成功。
- **运行环境先核精确路径：** ColabFold CLI和缓存存在，但运行参数把`--data`给到`params`子目录，引发3.82GB下载；只留下29MB部分权重。停止后核实并仅删除这次生成的部分文件，再把路径改为缓存根目录。来源C018–C020，事件894–1024。
- **预测状态多证据判断：** 重启后日志进入GPU流程，却报出数十GB统一内存申请；GPU监视显示低占用/无进程，CPU进程高，随后WSL状态查询AccessDenied。状态冲突时不能单凭一个遥测判断失败或完成，需用退出码、预测文件和逐条日志交叉确认。C020末尾仍无输出，C021续查。
- **证据边界：** 此ColabFold轮次即使完成，也只是结构交叉预测；目标为195-aa裁剪单体，没有天然二聚体、糖链或转铁蛋白背景，不能推出Kd/亲和力或全靶点适配。

## MAIN_3 C021–C023补充：选点与扩量复盘（2026-10-30）

- **分清数量与独立性：** RFdiffusion做64个骨架（2个patch×2个长度层×16）；MPNN每骨架16条，共1024序列。后续只选96条进入Boltz，覆盖56骨架；不是1024个独立结合姿势。96个模型中0个通过项目组合结构门槛。来源MAIN_3 C006–C012及C023，事件1169–1217。
- **选点证据不足，但错误未被证明：** 可访问性脚本过滤表面面积、二聚体、已见糖链、sequon、转铁蛋白并加入保守性/芳香性；没有证据支持所选面是高亲和力功能表位。patch1为Y247/E244，Y247不保守；patch2为L303/S327，S327与二聚体/观察糖链最近距离约13.7/13.9Å。结论应是位点策略需结合已知配体/抗体/功能表位和全结构证据复核；仅凭0/96或结构可及性，不能断言选错。
- **先验证少数姿势再扩增：** 这轮在少数/单骨架姿势是否可独立复现尚未验证前，就扩到64骨架、1024序列。建议先用少量设计验证姿势、界面化学、完整构建体/寡聚体/修饰兼容性和多模型稳定性，再按规则扩量。每骨架多条序列属于相关样本，统计时按骨架家族聚类汇报。
- **结构门槛边界：** 本项目pass_core门槛为iptm≥0.70、界面PAE≤10、binder pLDDT≥85、半埋藏面积≥500、设计姿势RMSD≤2.5；应报告0/96及所有门槛来源。它们是未校准的计算验收规则，不是亲和力/实验成功概率。
- **来源限制：** 用户要找以前归档TfR1 ChatGPT聊天；历史会话当时的工具清单未显示读取普通ChatGPT归档的接口，后续回传待C024，不能称已搜档案。

## MAIN_3 C024–C025：归档访问与挑战推荐表位（2026-10-30）

- 当前历史会话没有普通ChatGPT归档读取工具；用户随后明确让助手依靠公开资料继续，无需等待旧聊天。
- Proteinbase Challenge 04可见搜索结果推荐人TfR1 ectodomain homodimer的apical功能表位。列出的结合区域包括人Tyr211附近202–215、348与371；已知病毒/VP1u ligand结构11RN/3KAS及设计binder结构6WRV；transferrin结合于helical区619–670，并掠过另一亚基的apical区域。该区域人鼠差异显著，鼠源需在对应同源表位上逐位点映射。
- 与此相比，本轮patch热点Y247/E244、L303/S327源自表面几何启发式，并未引用病毒/抗体复合物或已知功能表位来定点；两者并非等价替代证据。挑战页面推荐是一条设计依据，不自动证明对用户目标的最佳表位。
- 页面明确比赛目标还包括pH7.4结合、pH6释放、mouse结合；用户的自定义目标未要求专门设计/验证pH响应。保持任务范围透明，不能以比赛规则覆写用户要求，也不能说完成比赛目标。
- Challenge页面指出目标为human P02786 ectodomain 121–760 homodimer，结构11QC chains A/B；旧结构3S9L/6WRV可能在142位用Ser，而UniProt/当前构建体为Gly。建模前应核对序列构建体和关键位点。
- C025搜索结果有截断，以上只按可见主页面内容记录；下一段看助手如何查现成binder并修正路线。

## MAIN_3 C027：已有TfR1 binder先例（2026-10-30）

- **de novo设计实测：** 原始sheet-extension研究报告一轮48个设计，24个SEC可溶、7个BLI显示结合；后续3个表征KD约400–700nM，3DS18实验晶体复合物与设计姿势相近。后续轮次按目标构象调整、放宽芳香侧链chi2约束。经验：报告每级筛选分母、可溶性和实验结合率；把设计模型与实验结构对齐；从实测结构检验界面，不只依赖预测分数。来源CODEX_TFR1_MAIN_3 C027，turn10search4。
- **跨物种先例：** TXB2 VNAR相关测定在人/鼠TfR1显示亚nM级结合（约0.65/0.25nM），但它是特定抗体样支架与融合构型，不作为新设计小蛋白的普遍期望，也不是Kd越低越利于BBB转运的证据。来源C027，turn10search1/6。
- **epitope多样性：** 公开摘要还提到TB14.2包绕Y211疏水口袋、界面His可能响应内体pH；C5/B8 VHH结合保守二聚体界面腔体。两种策略目标与分子尺寸不同，必须验证天然同源二聚体可达性、功能效果及实验亲和力，不能复制成通用结论。来源C027，turn10search7/8。
- 搜索中引用的审阅文章和交互式设计站点只作为找线索；当前RCSB页只取到页面头部，未做6WRV/11RN原子级叠合。

## MAIN_3 C026–C030：挑战位点、先例与原过滤矛盾（2026-10-30）

- Challenge 04将apical功能表位指向Tyr211邻近区域（202–215、348、371）；原流程选的Y247/E244与L303/S327不是同一热点。Challenge还定义pH7.4、pH6.0、mouse、人源KD的多目标排序；用户当时的定制要求未包括pH专门工程/验证，需分开报告。
- surface_audit.csv显示由于transferrin_min≥12Å硬过滤，Tyr211及202–215周围多残基被排除。Y211最近距离3.88Å、R208为3.69Å，205K是202–215里唯一个合格位置；N348的SASA 23.75和Tf距离9.98Å均触发排除；K371过筛但人鼠不保守。该结果表明旧过滤标准与challenge推荐面存在显著冲突。下一步需审视3S9L的Tf链C/D是否分别贴近TfR不同亚基、目标同源二聚体构象、链对应和坐标叠合。潜在根因是把全复合物最小距离套成全局一票否决；现阶段是强线索，仍未完成链级验证。
- ProteinMPNN执行为每骨架两个温度各8序列，共16；64×16=1,024。序列筛选只看长度、同聚物、疏水、丙氨酸、氨基酸种类和MPNN/global score，并每骨架最多2条抽样至96；未筛靶点亲和力、人鼠/鼠源和pH。不能把它写成1024个结合假设或验证样本。
- 公开实验先例有价值但有边界：sheet-extension de novo设计文献摘要报道20nM hTfR binder与BBB芯片；另轮设计曾有实验晶体与预测pose接近。2025 TB14研究从Y211疏水口袋出发，进化S4-4的YSD KD约305±55nM；其界面His仅为可能pH敏感的机理假设，未见该对话中pH release测定。TXB2是VNAR而非新设计mini-protein，跨物种KD不能当作本项目通用目标线。

### MAIN_3-C031：复合物链与表位距离复核

3S9L PDB头信息标注TfR1为链A/B、transferrin为链C/D。原位点脚本汇总使用C/D所有原子距离；当前回传只确认实体身份，没有分链最近距离，故不能判断哪一条transferrin链构成近距离或是否因另一受体亚基空间位置而误杀apical表位。所选热点E244/Y247/L303/S327到Y211的CA距离为32.29/28.20/33.62/36.54 Å，表明其和Y211邻域是不同空间面。CA距离仅提供粗定位，不能证明表位优劣。公开来源片段称de novo sheet-extension靶向远离transferrin结合区域的apical边缘β链；RCSB列出3DS18实验晶体复合物（2.47 Å）。网页返回有截断，且本段没有独立重算原子界面。
 - Evidence: local prepared chunk CODEX_TFR1_MAIN_3_visible_C031.txt, event 1305; 3S9L header and CA-distance output. 
 - Status: entity/header and CA positions directly inspected; chain-specific clash interpretation unresolved.
### MAIN_3-C033：跨二聚体界面的VHH先例

2025 C5/B8研究通过突变扫描将表位定位在TfR1同源二聚体界面附近，涉及E634/G636/E728/R732，横跨两个受体亚基；其与holo-Tf位点相邻但不重叠，未见Tf竞争。研究报告该区域的人鼠序列一致性75%、相似性83.3%，但关键E634在人为Glu、鼠为Asp，且VHH物种结合表现并不完全相同。该案例说明跨物种设计须针对局部残基、电荷、构象和实际结合测试，单看整体或局部同源率不够。该凹槽宽约32.6Å，可容纳约25Å VHH而不适配约48Å Fab；约796Å²界面面积是此VHH体系的数据，不是通用合格线。当前回传是功能突变映射；未提供高分辨率复合物原子坐标。2026预印本搜索片段提到C5VHH+hTfR1+holo-Tf cryo-EM及糖链接触，证据状态需与同行评审论文分开。
- Source: `CODEX_TFR1_MAIN_3_visible_C033.txt`, event 1314, retrieved ScienceDirect/PubMed/PMC snippets.
- Application caveat: BBB转运可能偏好中等亲和/快解离；这与此任务亲和力优先的用户目标不同。
### MAIN_3-C035（事件1354；2026-10-30）

- C035已逐片审阅并登记；累计35/41，下一段C036。五段归并完成。
- RFdiffusion官方README确认支持binder design，同时说明推理实际配置由checkpoint决定。WSL本地可见7个约462MB权重，总约3.2GB；没有Complex_beta权重。文件存在不等同该环境/设计条件已运行验证。
- Proteinbase FAQ给出比赛硬要求：挑战获胜设计须满足全部目标；该跨物种/pH目标包括人源结合pH下可测KD、释放pH无可检测结合、鼠源结合，之后按pH开关、鼠/人KD比、亲和力排序。这是比赛标准，和用户自定义“不专门做pH响应/验证”分开。
- FAQ将de novo zero-shot定义为不以已有binder为起始且需与已知蛋白有足够序列和结构多样性；允许用已知binder校准指标/模型，不允许直接改造已有binder。若目标为参赛，设计及模板/初始化流程要做新颖性合规审查。
- Track 1只筛选排名前20条通过过滤的设计，要求提交排序和方法来源；竞赛计划公开结果与失败。需先确认参与track，不能自动把FAQ规则变成用户任务硬验收。
- 整体因果链：先前启发式表位筛选的transferrin硬距离条件可能排除推荐apical面，但链级原因未核实；原始少数热点远离Y211。已有VHH二聚体界面结合剂提供另一种不同尺寸的表位先例。用户已要求先优化新方案再启动计算，历史此时尚未进入新一轮生成。
### MAIN_3-C038：Tf链配对错误导致Y211误筛

3S9L的生物组装注释显示assembly 1包含A/C并通过二重对称生成第二组，assembly 2包含B/D；RCSB页面亦标注A2B2。旧脚本把TfR1链A对齐到11QC后，将同一原始不对称单元的转铁蛋白链C与D合并计算最近距离，但D链属于受体链B的另一组复合物，不在A链坐标系的配体位置。故Y211与D链的约3.9Å是错误链配对造成的伪冲突，12Å阈值遂淘汰官方推荐apical表位。按A/C生物配对和对称副本重建后，对齐RMSD 0.68975Å，Y211到两份Tf最近原子距离54.503/54.285Å；叠合3DS18的Tf距离为52.315/33.953Å，无2Å内原子对。

- Causal status: directly confirmed for this structure alignment by PDB assembly annotations and coordinate audit.
- Limitation: static distance only; does not establish allostery, competition kinetics, conformational ensemble compatibility, or lack of steric effects in other states.
- Prevention: verify author biological assembly; pair receptor and ligand chains; preserve chain mappings through transformations; report per-chain distances and inspect known complex controls before hard exclusion.
- Source: `CODEX_TFR1_MAIN_3_visible_C038.txt`, events 1377–1395; historical audit files `corrected_assembly_audit.json`, `audit_assembly.py` under old PRP project route.
### MAIN_3-C036–C040阶段归并：从错误热点到小批量校准

#### 因果链
原先以SASA、保守性和距离门槛挑热点；3S9L预处理错误把受体A与另一组装的Tf链D混算，Y211被记为约3.9Å并淘汰；已知3DS18/2DS25.5实验结构对齐显示旧热点离其界面22–28Å，旧方案真正缺的是结构上下文与位姿控制。生物组装校正后Y211至正确Tf配体约54Å，3DS18叠合无原子重叠。对96个首轮复合物复核序列一致性和自折叠表现后，不能将“自身可折叠”误当作“正确结合”。
#### 已确认经验及边界
- 对称受体复合物需按PDB biological assembly保持配体—受体链配对；不对齐一条受体后把非对称单元所有配体链一起做距离过滤。
- 先用实验结构做表位映射、姿势重现及对照校准；受体构象、二聚体、糖链和已知配体状态都要留在相关坐标框架内。
- 目标是暴露β边缘时，局部链构象和芳香侧链χ2可影响结果；多个构象、独立姿势、序列变化应分开覆盖。
- RFdiffusion官方的样本量、hotspot数量、ipTM/PAE/BSA建议均依其模型/数据，不是跨靶点保证线；官方论文的Rosetta筛线也不直接转成Boltz的合格线。
- 对照资源：3DS18/6WRV、2DS25.5/6WRW；依次保留其独立设计身份与各自实验数值。比赛允许已知binder校准，但禁止作为新参赛序列的突变母本。
#### 证据缺口/风险
旧五条pose RMSD 30–50Å在当前C039展示脚本里没有计算实现；追查此前指标脚本或作为来源不明的助手汇总保留。链对静态距离不代表竞争实验。当前没有新的候选序列或计算验证。用户自定义不要求专项pH设计，与比赛完整规则分开报告。
#### 下一步
审阅C041；之后核对全来源记录数、最后检查点/manifest一致性及输出归档，以阶段摘要为继续工作依据。
### C041只读产物复核（2026-10-30）

- 已读取round2的apo/bound/control/assembly PDB。控制复合物链A为195aa受体crop，链B分别为93aa的3DS18和88aa的2DS25.5坐标序列；SE­QRES全序列长度为94/88，差异来自3DS18末端未建模残基。生物组装文件有受体A/B各638aa、Tf C/D各515aa。
- 原生成日志的Biopython重命名警告没有造成当前输出的链配对错乱：A-C和B-D各有277个4.5Å内重原子对；交叉A-D和B-C均为0，最近交叉距离6.302Å。输出映射与组装接触符合预期。代码仍宜先将副本从旧Model脱离后再重命名，避免父索引脆弱。
- 台账检查发现MAIN_3/C004有一条早期output_pending记录和一条后续semantic_reviewed完成记录。已保留完整审阅项、去掉过时重复项；现在每个MAIN_3分段对应唯一一条检查点。

## MAIN_4 C001–C002：第二轮复盘与β边缘设计（事件1775–6985）

### 第二轮失败

- 用户要求重启并继续到得到满意结果；助手先用2DS25.5/3DS18正对照校准。聊天报告无模板与apo条件不能恢复对照姿势；2DS25.5结合态模板5/5恢复，而3DS18取向仍偏约18–19 Å。对话显示ipTM较高不必然代表正确姿势。
- 32个RFdiffusion骨架完成后，30个通过初筛几何；ProteinMPNN因批量参数组合产生空FASTA，修正后继续。后续72个Boltz结构先被评分脚本全标解析失败；定位到骨架与预测结构残基对应实现错误，修正后按当时冻结标准无一通过。围绕唯一较好的TFR2_011骨架又生成9条序列变体，没有得到可信命中。
- 这一段反映的流程经验是：生成前校准对照姿势；扩批前完整跑通一例序列输出和指标映射；解析失败先修代码而非淘汰候选；同一骨架增序列不等于解决界面/姿势问题。所有上述数字/状态在该段主要来自助手进度陈述，部分由round2日志复盘支持，未在本段对每个输出逐一复现。

### 第三轮结构候选与报告纠正

- 助手改为β边缘链配对拓扑，并以公开2DS25.5结合模式作结构先验。条件pilot先遇到contig命令解析问题和目标/设计链长度映射错误；改正后pilot进入采样，但界面弱。随后16个骨架中15个过几何初筛，15个骨架生成序列并多轮Boltz筛选，最终报告5条候选B5X_001、B5X_002、B5V_004、B5X_003、B5X_010。
- 同一项目的独立复核文件 `<LOCAL_PRP>\TfR1_challenge4_20261028\final_round3\review_20261029.md` 对原始CSV、代码和预测样本复查后纠正了较强的原始报告：5条均来自同一beta_5骨架；原先方案要求至少两个骨架家族未达到；报告称3/3设计姿势复现，但计票代码没有使用已计算的binder pose RMSD，也没有将官方接触条件纳入计票。按原2.5 Å姿势门槛，B5X_001为1/3、B5X_002为0/3、B5V_004为2/3、B5X_003为0/3、B5X_010为2/3；所以没有一条达到3/3，也没有一条达到原2/3门槛。
- 筛选阈值从最初阶段到beta5变体阶段发生变化；最终名单由手写ID列表导出，B5X_010入选而更好的X004未入选，未找到充分可复现的选择/多样性依据。三个扩散样本是单一模型与条件下的计算重复，非独立实验。
- 任务范围限制：Boltz输入仅为空MSA并使用195 aa受体片段；未完成第二预测器、独立binder折叠、完整640 aa受体/糖链构象集合、能量分析、鼠源复合物预测或KD实验。0.54–0.57是界面邻近区域序列保守程度，不证明mouse binding；His数量也不证明pH响应。

### 因果链与证据定位

- 用户目标：最后给出3–5条优先人源亲和力、鼠源加分的TfR1序列；不要求专门工程化或验证pH响应。
- 路线变化：首轮热点/组装错误 → 第二轮修正位点但几何/脚本和界面失败 → 阳性姿势校准 → β边缘配对路线 → 结构候选报告 → 独立复核发现姿势门槛、骨架多样性和report计票不一致。
- 原始用户/助手可见消息：`CODEX_TFR1_MAIN_4_visible_C001`（事件1775–3562）与`C002`（事件3571–6985）；准确消息ID和源事件范围见 `reviews/prepared/codex_chunks/CODEX_TFR1_MAIN_4_manifest.json`。原始工具调用和日志仍在本机JSONL对应事件；这些工具事件尚未逐项全部语义审阅。
- 独立文件证据：`final_round3/review_20261029.md`、`final_candidates.csv`、`final_candidates.fasta`及代表性CIF；详尽逐样本RMSD与原始字段以该复核文档为主。此复核支持结构/报告问题，不提供实验亲和力证据。

### 可迁移经验候选

1. 对预测姿势筛选，先在匹配构建体/构象条件下验证正对照能否恢复已知界面；对照失败时不据该条件的分数淘汰候选或制定筛选线。
2. 将书面门槛逐项对应到计分代码；为边界样本写小测试或独立重算，尤其是pose RMSD、官方接触、链映射和缺失值。
3. 任何门槛更新都记录时点/理由，并保留同一 frozen rule 的复算结果；不能用后续筛选阈值替代原先验收。
4. 报候选时分开序列数、结构家族数、模型/seed重复数和实验数；多次预测一致只能说明该模型条件下重现，不能叫独立结合验证。
5. “拿到3–5条序列”与“3–5个独立骨架”不同；有多样性要求时自动按序列与骨架家族检查。若用户只要求序列，仍如实列明亲缘/同骨架关系。
6. 阳性对照姿势重现与候选亲和力是不同证据；此轮没有实验KD，不能宣称真实高亲和力。

## MAIN_4末段确认与完整可访问来源边界（2026-10-30）

MAIN_4最后两段复述并串联了TfR1筛选的关键链条：起始阶段曾使用错误物种输入（大鼠转铁蛋白）；RFdiffusion/ProteinMPNN共生成或报告1,024条序列，经过基础序列规则和骨架数量限制后保留96条预测准备；离线Boltz及姿势/几何复核未得到达到既定组合标准的候选，后续打包5条临时候选与原“不达标不凑数”验收目标冲突。上述数量来自历史日志汇总，仍需逐项回到原始文件确认，不能当作现有亲和力结果。

另一个会改变靶点分析方向的错误已在后续结构复核中定位：3S9L具有两组不同的受体-转铁蛋白链组，旧分析混用不同组，造成Y211约3.9Å的错误距离；正确组装关系约54Å。故不能以旧混配结果判定挑战推荐Y211表位与转铁蛋白冲突。2DS25与3DS18是不同结合剂，各自证据不能合并成同一结合模式。

MAIN_1/2/3、AUTOMATION/MONITOR与清洗后MAIN_4共115段可访问Codex材料现已语义审阅完成。此状态不覆盖未发现的其他Codex会话，也不表示普通ChatGPT账号归档/隐藏分支/全部附件完整。MAIN_4原始rollout工具事件没有全量逐项审阅；本案例具体数值与模型产物仍以独立原始文件复核状态为准。
