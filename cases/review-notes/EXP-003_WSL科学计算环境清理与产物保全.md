# EXP-003 — WSL 科学计算环境清理：缓存分类与可恢复性

> **Publication note / 发布说明:** This is a redacted review note derived from a local case-review document. It is not a complete source conversation or a byte-for-byte transcript. Source coverage and unresolved checks stated below remain in force. Local paths, host identifiers, network addresses, contact details and full conversation UUIDs were redacted or shortened; scientific claims were not changed by this sanitization. The unmodified source is retained locally.
>
> 本文件是从本地案例审阅文档整理的脱敏审阅记录，不是完整原始对话，也不是逐字聊天导出。来源覆盖范围和未决核查状态仍以正文为准。已脱敏本地路径、主机标识、网络地址、联系方式并缩短完整会话 UUID；本次脱敏不修改科学结论。未修改的来源文件留存本地。


## 来源与范围

- 会话 `6acdb536…`（10月13日）、`6aca0579…`（10月10日）和 `6ad5e44d…`（10月19日）；全文位于项目 `AI蛋白质设计任务聊天记录/2026-10-31_ChatGPT导出补充审阅/`。
- 与设计方法无直接关系，但清理对象含 RFdiffusion、ProteinMPNN、ColabFold、Boltz 的模型权重/参数、环境、日志和缓存，属于计算运行的环境与数据保全支持案例。

## 观察到的因果链

- 第一轮助手早期给出宽泛的 `rm -rf ~/.cache/huggingface`、`rm -rf ~/.boltz` 等删除建议，只依据目录类别推断“可以重新下载”，未先确定缓存内容、离线/恢复依赖和具体任务状态。之后在用户贴出占用统计后，建议转向只读盘点和缓存分类；早期建议仍属于需要保留的错误记录。
- 另一条部署位置对话（`6ac457ff…`）中，助手依据“`D:\WSL\Ubuntu\ext4.vhdx` 加 `Ubuntu.tar`”的描述，推测 tar 是迁移备份并建议在 WSL/项目验证后删除。虽然先列出了一些验证项，结尾仍过早给出“可以直接删”的判断；导出没有证明归档包是否唯一、导入状态或其他备份是否存在。备份删除前应核实注册实例、实际VHDX路径、系统和关键环境可启动、tar完整性/替代备份，以及用户是否接受失去回滚点。
- 归档聊天查找对话（`6ae2f0ee…`）先正确区分 ChatGPT 云端记录与 Codex 本地会话文件；随后助手声称“通过授权的电脑连接”检查了路径并找到了会话索引、标题和文件。该导出含7个可见用户/助手节点及24个隐藏内部节点，但不含工具事件，故这些本地检查主张只能标为聊天中的状态报告，不能由该导出独立证实。类似任务要把“查找计划”“助手声称已查”“工具实际返回”和“已读取并确认正文”分开记录，尤其不要将Codex本地会话当作ChatGPT账号归档聊天。
- 另一个C盘占用对话先把 `pagefile.sys` 增大归因于近期 RFdiffusion/ProteinMPNN/ColabFold/Boltz 内存压力，并按猜测的32 GB RAM建议调整为4–8 GB；在用户问 Boltz 运行中能否清理后，助手改为明确建议运行期间不要调小 pagefile。两次回答的风险判断不一致，且机器 RAM 容量和 `swap.vhdx` 来源并未确认。
- 用户机器实际包含多套 Conda 科学环境、ColabFold 参数和 Boltz 数据；目录名称不能证明内容可再生。第一轮对话还涉及删除较详细 CSV / PRP 内容的历史后果，但当前导出本身无法完成文件级因果核验。
- 第二轮通过 `du`、`conda env list` 与 dry-run 定位到 `~/.cache/pip` 6.5 GB、ColabFold 参数约 3.5 GB、Boltz 约 5.9 GB。用户运行 `pip cache purge` 后，pip 缓存降至 12 KB、WSL 使用量从约 65 GB 降至59 GB；ColabFold 参数保留。
- 后续 VHDX 操作出现粘贴顺序混乱、0 GB读数、DiskPart多命令粘在一行等问题；用户/助手核验实际目录后确认 VHDX仍为73,195,847,680字节。对话最后并未执行 `compact vdisk`，不能声称 Windows 侧虚拟磁盘已经缩小。

## 可迁移经验候选

- 清理前只读盘点目标绝对路径、子目录和实际大小，区分可再生成缓存、模型权重/参数、环境、项目输入输出、日志和唯一证据材料。
- 目录名和可重新下载的理论可能性不足以授权删除；要确认模型恢复方式、网络/离线需求、运行进程、来源、备份及下游依赖。
- 优先使用工具自带的 dry-run/清理命令并核对真实缓存位置；小范围单项清理后检查文件和目标软件能否继续使用，再扩展操作。
- Windows 压缩 VHDX 与 Linux 内部释放空间是不同步骤；状态读数不合理时停下并用独立来源核验实际文件字节数。用户未确认 `compact vdisk` 执行成功，不记录为完成。
- 科学结果、日志与唯一的详细表需有可恢复副本及来源版本；压缩磁盘不能替代科研文件备份。
- 对分页文件/交换文件等活动内存机制，不能仅按文件大小直接清理或用 GPU 显存推断系统 RAM；先确认操作系统、虚拟机/WSL状态和任务阶段，运行高内存任务期间避免降低虚拟内存配置。

## 核验状态

上述容量与操作结果来自聊天粘贴的终端输出；本轮未连接 WSL 复测。真实磁盘回收效果未确认。WSL部署位置、tar身份与归档聊天本地检索主张均未从聊天导出以外的工具记录独立核验。该案例加强现有 PD-012（高风险文件操作前盘点与保留原件）及执行状态证据边界，不改变技能中的蛋白设计算法建议。
