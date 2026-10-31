# TfR1 第三轮名单与逐样本筛选的原始文件复核

> **Publication note / 发布说明:** This is a redacted review note derived from a local case-review document. It is not a complete source conversation or a byte-for-byte transcript. Source coverage and unresolved checks stated below remain in force. Local paths, host identifiers, network addresses, contact details and full conversation UUIDs were redacted or shortened; scientific claims were not changed by this sanitization. The unmodified source is retained locally.
>
> 本文件是从本地案例审阅文档整理的脱敏审阅记录，不是完整原始对话，也不是逐字聊天导出。来源覆盖范围和未决核查状态仍以正文为准。已脱敏本地路径、主机标识、网络地址、联系方式并缩短完整会话 UUID；本次脱敏不修改科学结论。未修改的来源文件留存本地。


复核日期：2026-10-30。此为对本地原始文件的定向复核；不运行新预测，不评价实验亲和力。

## 核对文件

- `<LOCAL_PRP>\TfR1_challenge4_20261028\final_round3\final_candidates.csv`
- `final_candidates.fasta`、`final_report_pre_review.md`、`final_report.md`
- `round3_beta\work\beta5_refine2_metrics.csv`（12条变体，各3个扩散样本）
- `round3_beta\work\beta5_variant_metrics.csv`（8条变体，各3个扩散样本）
- `round3_beta\work\beta5_refine2_summary.csv`、`beta5_variant_summary.csv`
- `round3_beta\scripts\score_beta5_variants.py`、`finalize_round3.py`
- 原复盘：`final_round3\review_20261029.md`

## 独立重算结果

将每个CSV中的逐样本 `binder_pose_rmsd_A` 与原方案的2.5 Å姿势门槛比较；另按 `score_beta5_variants.py` 的票数表达式重算宽松票数。五条最终名单的原始行均存在，每条3个样本均无解析错误。

| 候选 | 宽松综合票数 | binder pose RMSD ≤2.5 Å | 原复盘给出的姿势范围 Å | 原始表 ipTM范围 |
|---|---:|---:|---:|---:|
| B5X_001 | 3/3 | 1/3 | 2.39–3.08 | 0.829–0.846 |
| B5X_002 | 3/3 | 0/3 | 3.24–5.14 | 0.827–0.827 |
| B5V_004 | 3/3 | 2/3 | 1.56–3.03 | 0.795–0.803 |
| B5X_003 | 3/3 | 0/3 | 2.84–3.32 | 0.767–0.772 |
| B5X_010 | 3/3 | 2/3 | 2.05–2.51 | 0.719–0.724 |

### 3/3的真实含义

`score_beta5_variants.py` 中的 `votes` 表达式检查 ipTM、界面PAE、热点距离、半界面面积和外部结构冲突；**没有检查 `binder_pose_rmsd_A`**。`finalize_round3.py` 把这个宽松 `bound_pose_votes` 字段拼成字符串输出。最终报告正文却写成五条都“在3个结合态扩散样本中重现设计姿势”，并把名单里的3/3解释成姿势重复支持。该说法不受计票代码支持。

`final_report.md` 开头新增了复核警示，指出旧报告的3/3并非姿势复现；但警示下方仍原样保留“都重现设计姿势”和将3/3解释为姿势的旧正文。因此文件整体仍有自相矛盾，不能作为已完全更正的最终报告引用。原始文件未改动；此复核记录与原复盘共同界定其状态。

## 名单复现性与多样性

`finalize_round3.py` 使用固定列表 `['B5X_001','B5X_002','B5V_004','B5X_003','B5X_010']`，不是从可复算的全量排序/预先声明规则自动导出。最终CSV/FASTA确有5条、长度均为90 aa；5个ID均来自beta_5路线，原复盘记载全部来自同一beta_5骨架家族。选择理由不能仅由代码完整复现。

## 可迁移的问题与技能缺口

- 指标列名（`bound_pose_votes`）和报告语义（“pose复现”）不一致；字段本身不能验证其含义。
- 预设验收条件存在，但投票表达式漏掉姿势RMSD；运行无错误和产生5条交付物没有触发这一逻辑审查。
- 复核警示与保留的报告正文互相冲突；只在开头加免责声明不能修正后文错误主张。
- 实际技能已要求按配置复算通过数、独立抽样检查并交付局限，但轻量审计器不能读懂报告中的自然语言。因此这一环仍需显式人工逐项映射“每条结论→计算/表格→验收条件”，并检查报告内部矛盾。是否将其自动化，须基于其他案例评估误报和可行范围。

## 证据边界

这些文件证明该批模型指标和筛选脚本的具体不一致；不证明候选不结合，也不给出真实KD。原复盘中其他数量和方法结论需要各自的数据源支撑；本次只直接重算了最终名单相关两张逐样本CSV及所查看的代码/报告。所有候选结构都来自同一设计骨架家族，是结构多样性缺口，不是五个独立结构验证。

## 生成与筛选规模的原始表复核

| 阶段 | 从本地文件核对的数量 | 含义及限制 |
|---|---|---|
| 第一轮结构/序列池 | `work/candidate_pool.csv`：1024条唯一序列、64个唯一backbone标签；498行`eligible`、526行`rejected`。`work/human_shortlist.csv`与`human_boltz_metrics.csv`各96行 | 1024是ProteinMPNN序列数，不是RFdiffusion骨架数；表中eligible/rejected是序列启发式状态，不是结合命中/亲和力结论。骨架目录有65个PDB文件，可能包含试点结构；因此以候选表64个唯一backbone标签表述批量设计规模。 |
| 第二轮 | `round2/work/backbones`有32个PDB；`candidate_pool.csv`有60条唯一序列/30个backbone；human shortlist 12条；`boltz_ensemble_metrics.csv`有72行。后续refine shortlist 9条，Boltz metrics 54行 | 32个结构并不都出现在序列池；记录数量不把PDB、序列和预测样本混算。 |
| 第三轮beta骨架批次 | backbone audit 16行、几何通过15行；序列池30条唯一序列/15个backbone；human shortlist 8条，Boltz metrics 48行 | 30条序列是15个通过骨架各2条，不是30个结构设计。 |
| beta_5聚焦变体与定稿 | 第一批8条×3样本=24行；refine2 12条×3样本=36行；最终手工挑5条 | 五条都来自同一beta_5骨架家族；从候选池到名单的选择理由不能仅由最终列表复现。 |

数量来源是各阶段CSV的行数/唯一值，以及本地结构文件清点；分别代表生成序列、几何合格序列、入选预测序列、模型样本和最终名单。RFdiffusion目录总PDB数未直接当成功骨架数。