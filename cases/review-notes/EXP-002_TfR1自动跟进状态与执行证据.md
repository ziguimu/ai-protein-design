# EXP-002 — TfR1 自动跟进：执行接续必须有状态证据

> **Publication note / 发布说明:** This is a redacted review note derived from a local case-review document. It is not a complete source conversation or a byte-for-byte transcript. Source coverage and unresolved checks stated below remain in force. Local paths, host identifiers, network addresses, contact details and full conversation UUIDs were redacted or shortened; scientific claims were not changed by this sanitization. The unmodified source is retained locally.
>
> 本文件是从本地案例审阅文档整理的脱敏审阅记录，不是完整原始对话，也不是逐字聊天导出。来源覆盖范围和未决核查状态仍以正文为准。已脱敏本地路径、主机标识、网络地址、联系方式并缩短完整会话 UUID；本次脱敏不修改科学结论。未修改的来源文件留存本地。


## 来源与限制

- ChatGPT 会话：`6ae1b865…`，“设置论文筛选任务”。
- 全文副本：[导出聊天记录](../../AI蛋白质设计任务聊天记录/2026-10-31_ChatGPT导出补充审阅/6ae1b865-08ac-83ea-a7a1-250dce4e9bb3_设置论文筛选任务.md)。
- 会话有 7 个用户节点、34 个可见助手节点、20 个隐藏内部节点、1 个空节点和 1 处分支；按父子关系阅读。该导出没有工具事件节点，进程与文件状态均是助手在聊天中的报告，不是可独立审计的底层日志。
- 聊天先包含每周论文筛选任务，随后转为 TfR1 项目定时检查和接续计算。两个目标需分开记录。

## 对话中的流程报告及矛盾

- 初始轮次：称 RFdiffusion 四批共 64 个骨架完成，ProteinMPNN 第一轮启动/完成，预测阶段推进到 human Boltz 96/96。一个助手节点报告 `pass_core=0` 并称流程结束；随后另一个分支/更新进入第二轮，故不能把早期停止报告当成全项目结束。
- 后续轮次：第二轮产生 32 个骨架，31 个几何审计通过；ProteinMPNN 首次输出为 0 字节且退出码/日志状态不一致，最初未盲目重跑。后续又报告恢复到 Boltz shortlist 24 项、4/24。
- 一处后续助手报告最终 5 条全部为探索性；另一条报告补充每条都是 0/6 次 Boltz 通过阈值。再往后又有 `round3_beta` 精修任务处于运行的报告。它们属于不同阶段/时间点，需按状态文件版本和时间线分开，不能压成“筛选完成并得到5个通过候选”。
- 线程里的自动化意图包含每小时检查并在当前步骤结束后继续下一步。对“接续”的理解先过于保守，只读状态；用户指出应继续启动已定义的下一阶段后，才按现存脚本与约定执行。自主执行授权和明确验收/停止条件应写入任务契约。

## 经验候选

- 每个阶段状态需有不可混淆的 run/round/attempt ID、输入与配置版本、启动/完成时间、进程、退出码、预期产物和审计摘要；`status.json` 被不同脚本覆盖时要保留历史状态，避免将新阶段误判成旧阶段已结束。
- 对缺失、0 字节、异常完成或日志缺失的输出，先查进程、脚本、日志和文件大小；只有确认重跑安全、不会覆盖有效结果或造成重复计算后再继续。
- 监控器应区分“报告进度”“允许继续”“阶段完成”和“达到目标”。达成流程停止条件后不再继续发起计算；空候选/0通过应如实写为失败筛选，不改阈值凑出候选。
- 定时提醒、无人化监控、本地脚本和对话助手持续可见性是不同能力。不得声称已创建自动任务或已完成本地检查，除非对应接口/日志证实。
- 对用户明确授权的 autonomous continuation，要按已有方案完成可运行阶段，同时不越过明确的禁止事项（如不提交、不合成），并在缺少脚本/关键参数时记录具体阻塞。

## 核验状态

本案例复述的是会话报告，未将该会话中的每一个进程状态与本地 TfR1 原始文件逐项映射。可信候选数量、模型阈值通过率和终选结论仍以 `<LOCAL_PRP>\TfR1_challenge4_20261028` 中有版本号的实际报告/日志和后续本地复核为准。该会话支持现有 PD-005/PD-006 的运行溯源原则，不单独证明自动监控提升设计质量。
