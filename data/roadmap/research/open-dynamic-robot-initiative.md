# Open Dynamic Robot Initiative（ODRI，开放动态机器人计划）调研档案【补充项目】

> 调研访问日期：2026-07-01。所有事实均附来源 URL（见文末）；未查到的信息标注"未知"。GitHub 星标等为检索时点快照。
> 入选理由：全球最重要的开源**力控/本体感知执行器**生态之一，其 Bolt 为开源双足平台，Solo 四足与 TriFinger 同样知名；是理解"准直驱 + 力控"技术路线的必研项目。

## 基本信息

| 项目 | 内容 |
|---|---|
| 项目名 | Open Dynamic Robot Initiative（开放动态机器人计划，简称 ODRI） |
| 发起机构 | 国际学术联盟：New York University（Ludovic Righetti 团队）、Max Planck Institute for Intelligent Systems（Felix Grimminger 等）、LAAS-CNRS 等 |
| 开源许可证 | BSD-3-Clause（执行器硬件与多数软件）；Master Board 为 BSD-2-Clause |
| 硬件成本（BOM） | **未知**（官方未公布统一 BOM 总价；论文强调"低成本、可复现"，执行器物料以现成无框电机 + 自研驱动卡构成） |
| 平台形态 | Solo 8/12（四足，8 或 12 自由度）、**Bolt（双足，6 自由度点足）**、TriFinger（三指操作平台） |
| 身高 / 重量 | 因平台而异（Solo 为桌面级四足；Bolt 为小型双足）；统一官方数值未在检索中获得，**未知** |

## 执行器方案

- 自研 **BLMC 无刷力控执行器**：现成无框电机 + 双编码器（电机端/输出端）+ 自研 MicroDriver 驱动卡，低减速比、高扭矩透明度，支持本体感知力控——这是 ODRI 的核心贡献。
- `open_robot_actuator_hardware` 仓库提供全部机械/电气设计文件（含 Bolt 双足 6 自由度版本 biped_6dof_v1）。

## 计算平台与传感器

- 通信中枢为自研 **Master Board**（与执行器驱动卡高速同步通信）；上位机跑实时 Linux 控制栈。
- 传感器以执行器内置双编码器 + IMU 为主；强调"本体感知即可控"，视觉非标配。

## 软件栈

- C++ 实时控制 + Python 接口；提供仿真支持（Gazebo/PyBullet 生态，trifinger_simulation 等仓库持续更新至 2025-12）。
- 学术使用方式以论文 + workshop 形式推广（Solo/Bolt 被多所欧美高校复制用于力控与 RL 研究）。

## 文档与教程质量

- 官网（open-dynamic-robot-initiative.github.io）+ 各仓库 README + 执行器硬件论文（Grimminger et al.）；文档偏科研工程风格，面向有嵌入式/控制背景的用户，非 step-by-step 新手教程。

## 社区活跃度

- GitHub 组织快照：`open_robot_actuator_hardware` **1,428 stars**（核心仓库，2022-09 后停更，设计已固化）；`master-board` 135 stars（2026-06-30 仍活跃）；`open-motor-driver-initiative` 115 stars（2025-09）；`trifinger_simulation` 42 stars（2025-12）；`solo` 41 stars。
- 被 Upkie 等第三方开源项目官方列为同类推荐，生态影响力大于星标表面值。

## 新手友好度评估：2 / 5

- 优点：想理解"力控执行器怎么造"，这是全网最完整的开源参考（机械、电气、固件、控制全链路 BSD 许可）。
- 门槛：需要电机控制、电力电子、实时系统功底；自研驱动卡打样与调试门槛高；无保姆级教程。
- 适合：有运控/嵌入式基础的研究者与工程师；不适合零基础新手直接上手。

## 来源 URL（访问日期 2026-07-01）

- https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware （执行器硬件开源仓库，含 Bolt 双足 6 DoF 设计；星标与停更时间经 GitHub API 检索）
- https://github.com/open-dynamic-robot-initiative （组织仓库列表：master-board、solo、trifinger_simulation 等活跃度快照）
- https://github.com/stephane-caron/awesome-open-source-robots （ODRI Solo/Bolt 在开源机器人清单中的条目与 Bolt 双足图示）
- https://pypi.org/project/upkie/ （Upkie 官方将 ODRI 列为同类"开源力控模块化腿足架构"）
