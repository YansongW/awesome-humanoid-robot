---
$id: ent_robot_system_odri_bolt
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: ODRI Bolt (Open Dynamic Robot Initiative)
  zh: ODRI Bolt 开源双足机器人
  ko: ODRI Bolt (Open Dynamic Robot Initiative)
summary:
  en: The open-source point-foot biped from the Open Dynamic Robot Initiative, an international academic consortium of NYU, MPI-IS and LAAS-CNRS, featuring 6 degrees of freedom driven by proprioceptive force-controlled BLMC brushless actuators with dual encoders and a custom MicroDriver card, released under BSD licenses with full mechanical, electrical, firmware and control designs.
  zh: Bolt 是 Open Dynamic Robot Initiative（ODRI，开放动态机器人计划）的开源双足平台，由 NYU、马克斯·普朗克智能系统研究所、LAAS-CNRS 等国际学术联盟开发，6 自由度点足构型，核心为自研 BLMC 无刷力控执行器（现成无框电机 + 双编码器 + 自研 MicroDriver 驱动卡），机械、电气、固件、控制全链路以 BSD 许可开源。
  ko: The open-source point-foot biped from the Open Dynamic Robot Initiative, an international academic consortium of NYU, MPI-IS and LAAS-CNRS, featuring 6 degrees of freedom driven by proprioceptive force-controlled BLMC brushless actuators with dual encoders and a custom MicroDriver card, released under BSD licenses with full mechanical, electrical, firmware and control designs.
domains:
- 02_components
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- system
- knowledge
tags:
- open_source
- biped_robot
- odri
- bolt
- force_control
- quasi_direct_drive
- bldc_actuator
- research_platform
- bsd_license
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: '内容整理自调研档案 data/roadmap/research/open-dynamic-robot-initiative.md（访问日期 2026-07-01）。官方未公布统一 BOM 总价与整机身高/重量，标注为未知。'
sources:
- id: src_001
  type: website
  title: open_robot_actuator_hardware GitHub Repository
  url: https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Open Dynamic Robot Initiative GitHub Organization
  url: https://github.com/open-dynamic-robot-initiative
  accessed_at: '2026-07-01'
---

## 概述

Bolt 是 Open Dynamic Robot Initiative（ODRI，开放动态机器人计划）旗下的开源双足平台。ODRI 是国际学术联盟，成员包括 New York University（Ludovic Righetti 团队）、Max Planck Institute for Intelligent Systems（Felix Grimminger 等）、LAAS-CNRS 等；其平台家族还包括 Solo 8/12（四足，8 或 12 自由度）与 TriFinger（三指操作平台）。Bolt 为 6 自由度点足双足（来源：调研档案 open-dynamic-robot-initiative.md，下同）。

许可证：执行器硬件与多数软件 BSD-3-Clause，Master Board 为 BSD-2-Clause。硬件成本未知——官方未公布统一 BOM 总价，论文强调"低成本、可复现"，执行器物料以现成无框电机 + 自研驱动卡构成；统一官方身高/重量数值亦未在检索中获得。核心仓库 `open_robot_actuator_hardware` 1,428 stars（2022-09 后停更，设计已固化），`master-board` 135 stars（2026-06-30 仍活跃）。Solo/Bolt 被多所欧美高校复制用于力控与 RL 研究，被 Upkie 等第三方开源项目官方列为同类推荐。

## 核心内容

### 关键参数

| 项目 | 数值 | 来源 |
|---|---|---|
| 平台形态 | Bolt（双足，6 自由度点足）；姊妹平台 Solo 8/12、TriFinger | 调研档案 |
| 硬件成本（BOM） | 未知（官方未公布统一总价，论文强调低成本可复现） | 调研档案 |
| 身高 / 重量 | 未知（统一官方数值未获得） | 调研档案 |
| 通信中枢 | 自研 Master Board（与执行器驱动卡高速同步通信） | 调研档案 |
| 上位机 | 实时 Linux 控制栈 | 调研档案 |
| 新手友好度 | 2 / 5（调研档案评估） | 调研档案 |

### 执行器方案（核心贡献）

- 自研 BLMC 无刷力控执行器：现成无框电机 + 双编码器（电机端/输出端）+ 自研 MicroDriver 驱动卡，低减速比、高扭矩透明度，支持本体感知（proprioceptive）力控——这是 ODRI 的核心贡献，是理解"准直驱 + 力控"技术路线的必研项目。
- `open_robot_actuator_hardware` 仓库提供全部机械/电气设计文件（含 Bolt 双足 6 自由度版本 biped_6dof_v1）。
- 传感器以执行器内置双编码器 + IMU 为主；强调"本体感知即可控"，视觉非标配。

### 软件栈与文档

- C++ 实时控制 + Python 接口；提供仿真支持（Gazebo/PyBullet 生态，trifinger_simulation 等仓库持续更新至 2025-12）。
- 官网（open-dynamic-robot-initiative.github.io）+ 各仓库 README + 执行器硬件论文（Grimminger et al.）；文档偏科研工程风格，面向有嵌入式/控制背景的用户，非 step-by-step 新手教程。
- 学术使用方式以论文 + workshop 形式推广。

### 适合人群

- 适合：有运控/嵌入式基础的研究者与工程师——想理解"力控执行器怎么造"，这是全网最完整的开源参考（机械、电气、固件、控制全链路 BSD 许可）。
- 门槛：需要电机控制、电力电子、实时系统功底；自研驱动卡打样与调试门槛高；无保姆级教程；不适合零基础新手直接上手。

## 参考

- [open_robot_actuator_hardware 仓库（含 Bolt 双足 6 DoF 设计）](https://github.com/open-dynamic-robot-initiative/open_robot_actuator_hardware)
- [open-dynamic-robot-initiative GitHub 组织](https://github.com/open-dynamic-robot-initiative)
- [awesome-open-source-robots 清单条目](https://github.com/stephane-caron/awesome-open-source-robots)
