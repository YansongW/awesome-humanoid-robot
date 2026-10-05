---
$id: ent_paper_pour_toward_humanoid_robots_in_cons_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Toward Humanoid Robots in Construction: A Teleoperation Feasibility Study'
  zh: 'Toward Humanoid Robots in Construction: A Teleoperation Feasibility Study'
  ko: 'Toward Humanoid Robots in Construction: A Teleoperation Feasibility Study'
summary:
  en: We present a teleoperation system that enables a single operator to perform construction tasks on a Unitree G1 humanoid,
    combining extended reality (XR) based upper body control with pedal-based locomotion to enable simultaneous manipulation
    and locomotion. Motivated by persistent labor shortages, hazardous working conditions, and challenges in humanoid autonomy,
    we investigate teleoperation as a ...
  zh: 本文提出一套面向 Unitree G1 人形机器人的遥操作系统，由单一操作者通过扩展现实（XR）控制上半身并结合踏板控制行走，从而同时完成操作与移动。研究动机来自建筑行业长期存在的劳动力短缺、危险作业环境以及人形机器人自主性不足，作者将遥操作视为近期可行的过渡方案。系统在两项取自
    O*NET 职业数据库的建筑任务上评估，工具搬运成功率为 100%，表面喷漆成功率为 80%，但耗时明显高于人工基线。
  ko: We present a teleoperation system that enables a single operator to perform construction tasks on a Unitree G1 humanoid,
    combining extended reality (XR) based upper body control with pedal-based locomotion to enable simultaneous manipulation
    and locomotion. Motivated by persistent labor shortages, hazardous working conditions, and challenges in humanoid autonomy,
    we investigate teleoperation as a ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_robots
- teleoperation
- extended_reality
- construction_robotics
- unitree_g1
- task_success_rate
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2610.00718);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.00718 Toward Humanoid Robots in Construction: A Teleoperation Feasibility Study'
  url: https://arxiv.org/abs/2610.00718
  date: '2026-09-30'
  accessed_at: '2026-10-05'
---

## 概述

该工作由 Parastoo Ali Pour、David R. Martin、Chang Min Hur、Bo Zhang、Tommy Zhou、Brandon Thomas Lichter、Shane Stanfield、Pramod Khargonekar 等人完成，聚焦于将人形机器人引入建筑场景的可行性。作者构建了一套遥操作系统，让单个操作者借助扩展现实（XR）界面控制 Unitree G1 的上半身，并通过踏板实现行走，使操作与移动能够同步进行。研究以劳动力短缺、作业危险和人形机器人自主能力有限为背景，把遥操作定位为近期可落地的方案，既能减轻工人身体负担，也能采集高质量示范数据。评估选取 O*NET 职业数据库中的两项代表性建筑任务，报告任务成功率与完成时间，并与人工基线对比。结果显示工具搬运成功率为 100%、表面喷漆成功率为 80%，但遥操作所需时间显著多于人工执行。

## 核心内容

### 问题背景
建筑行业面临持续的劳动力短缺与危险的作业条件，而人形机器人的自主能力尚不足以直接胜任此类任务。作者因此将遥操作视为一种近期可行的替代路径：既能减少工人的身体负担，又能在执行过程中产生高质量的示范数据。

### 方法
- 硬件平台：Unitree G1 人形机器人。
- 控制方式：单一操作者使用扩展现实（XR）界面控制机器人上半身，同时通过踏板控制行走，实现操作与移动的并行。
- 系统目标：让一名操作者即可完成建筑作业，而非依赖多人与复杂的自主策略。

### 实验设置
- 任务来源：从 O*NET 职业数据库中选取两项具有代表性的建筑任务。
- 评估指标：任务成功率与完成时间。
- 对照条件：人工执行基线（manual baseline）。

### 关键结果
- 工具搬运（tool transport）：成功率 100%。
- 表面喷漆（surface painting）：成功率 80%。
- 完成时间：与人工执行相比，遥操作所需时间显著更长。

### 结论
该可行性研究说明，基于 XR 上半身控制与踏板行走的遥操作方案，可以让单名操作者在 Unitree G1 上完成部分建筑任务，并在工具搬运上达到完全成功；但喷漆任务仍有失败，且效率明显低于人工，表明遥操作在建筑场景中具备近期应用潜力，同时仍需在成功率与作业速度上继续改进。

## Overview

We present a teleoperation system that enables a single operator to perform construction tasks on a Unitree G1 humanoid, combining extended reality (XR) based upper body control with pedal-based locomotion to enable simultaneous manipulation and locomotion. Motivated by persistent labor shortages, hazardous working conditions, and challenges in humanoid autonomy, we investigate teleoperation as a practical near-term approach for reducing physical strain on workers while generating high quality demonstration data. We evaluate the system on two representative construction tasks drawn from O*NET occupational database, and report task success and completion time relative to a manual baseline. The system achieved 100% success on tool transport and 80% success on surface painting, with teleoperation requiring substantially more time compared to manual execution.

## 参考
- https://arxiv.org/abs/2610.00718
