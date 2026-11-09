---
$id: ent_paper_kumar_pact_pose_robust_actuation_co_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PACT: Pose-Robust Actuation Co-Design for Tendon-Driven Robotic Hands'
  zh: 'PACT: Pose-Robust Actuation Co-Design for Tendon-Driven Robotic Hands'
  ko: 'PACT: Pose-Robust Actuation Co-Design for Tendon-Driven Robotic Hands'
summary:
  en: Humanoid robotic hands must provide sufficient force, speed, and backdrivability within a human-scale envelope. Tendon-driven
    transmissions address this challenge by relocating actuators to the palm and forearm, but routing paths, moment arms,
    and capstan dimensions jointly determine both force capability and joint speed, so selecting them sequentially satisfies
    one requirement at the expense of ...
  zh: PACT 是一个面向腱驱动机器人手的姿态鲁棒驱动协同设计框架，由 Prashant Kumar、Rachael Granberry、Taylor Niehues、Andrew A. Stanley 与 Gabe Pirie 提出。该框架在依赖姿态的力需求与传动带宽约束下，联合优化腱走线、力臂与绞盘尺寸，并以最大最小目标提升最弱姿态下的任务力覆盖。应用于四自由度手指时，得到采用准直驱执行器的非对称
    N+1 腱拓扑，在八个姿态下任务力覆盖达 0.88–1.00，并预测在人类尺寸包络内最小孤立关节屈伸带宽为 5 Hz。
  ko: Humanoid robotic hands must provide sufficient force, speed, and backdrivability within a human-scale envelope. Tendon-driven
    transmissions address this challenge by relocating actuators to the palm and forearm, but routing paths, moment arms,
    and capstan dimensions jointly determine both force capability and joint speed, so selecting them sequentially satisfies
    one requirement at the expense of ...
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
- tendon_driven_hands
- actuation_co_design
- pose_robust_optimization
- humanoid_robotic_hands
- drivetrain_bandwidth
- max_min_optimization
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.05302);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.05302 PACT: Pose-Robust Actuation Co-Design for Tendon-Driven Robotic Hands'
  url: https://arxiv.org/abs/2611.05302
  date: '2026-11-03'
  accessed_at: '2026-11-09'
---

## 概述

人形机器人手需要在人类尺度包络内同时满足力、速度与可反驱性，腱驱动传动通过把执行器移至手掌与前臂来应对这一矛盾，但走线路径、力臂与绞盘尺寸共同决定出力能力与关节速度，顺序设计往往顾此失彼。PACT 框架将腱走线、力臂与绞盘尺寸放在统一优化中处理，约束条件包括随姿态变化的力需求与传动带宽限制。方法上采用可行力 formulation 在所有关节上施加执行器边界与平衡约束，并以最大最小目标最大化最弱姿态下的任务力覆盖。该框架应用于四自由度手指，产生使用准直驱执行器的非对称 N+1 腱拓扑；在八个姿态下任务力覆盖为 0.88–1.00，预测在第七十百分位人类尺寸包络内最小孤立关节屈伸带宽为 5 Hz。原型实测与预测偏差最高达 24.5%，主要归因于未建模的传动损耗。

## 核心内容

### 问题背景
人形机器人手受限于人类尺度的空间包络，却需要同时提供足够的力、速度与可反驱性。腱驱动传动把执行器移到手掌与前臂以缓解空间压力，但腱走线路径、力臂与绞盘尺寸三者共同决定力能力与关节速度，若按顺序逐一选择，满足其中一项要求往往以牺牲另一项为代价。

### 方法
- 提出 PACT（Pose-Robust Actuation Co-Design for Tendon-Driven Robot Hands）框架，在依赖姿态的力需求与传动带宽约束下，联合优化腱走线、力臂与绞盘尺寸。
- 采用可行力 formulation，在所有关节上施加执行器边界与平衡约束。
- 以最大最小（max-min）目标最大化最弱姿态下的任务力覆盖。

### 实验设置
- 将该框架应用于一个四自由度手指。
- 优化结果产生非对称 N + 1 腱拓扑，并使用准直驱执行器。
- 在八个姿态下评估任务力覆盖，并在第七十百分位人类尺寸包络内评估最小孤立关节屈伸带宽。

### 关键结果
- 八个姿态下任务力覆盖为 0.88–1.00。
- 预测的最小孤立关节屈伸带宽为 5 Hz。
- 原型实测与预测的偏差最高达 24.5%，主要原因是未建模的传动损耗。

### 结论
结果表明，将走线与传动系统协同设计，可以在不放松带宽约束的前提下满足依赖姿态的力需求，为人形尺寸机器人手达到人类水平性能提供了路径。

## Overview

Humanoid robotic hands must provide sufficient force, speed, and backdrivability within a human-scale envelope. Tendon-driven transmissions address this challenge by relocating actuators to the palm and forearm, but routing paths, moment arms, and capstan dimensions jointly determine both force capability and joint speed, so selecting them sequentially satisfies one requirement at the expense of the other. This paper presents a pose-robust actuation co-design for tendon-driven robot hands (PACT) framework that optimizes tendon routing, moment arms, and capstan dimensions under pose-dependent force requirements and drivetrain-bandwidth constraints. A feasible-force formulation enforces actuator bounds and equilibrium at all joints, while a max-min objective maximizes task-force coverage at the weakest pose. Applied to a four-degree-of-freedom finger, the framework produces an asymmetric N + 1 tendon topology using quasi-direct-drive actuators. Across eight poses, the design achieves task-force coverage of 0.88-1.00 and a predicted 5 Hz minimum isolated-joint flexion/extension bandwidth within a 70th-percentile human-size envelope. Prototype measurements deviate from predictions by up to 24.5%, primarily due to unmodeled transmission losses. These results indicate that co-designing routing with the drivetrain can meet pose-dependent force requirements without relaxing the bandwidth constraint, paving the way for human-sized robotic hands with human-level performance.

## 参考
- https://arxiv.org/abs/2611.05302
