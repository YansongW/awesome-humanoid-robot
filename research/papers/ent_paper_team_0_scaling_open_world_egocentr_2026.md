---
$id: ent_paper_team_0_scaling_open_world_egocentr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '$λ_0$: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation'
  zh: '$λ_0$: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation'
  ko: '$λ_0$: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation'
summary:
  en: Humanoid loco-manipulation requires coordinated whole-body interaction with the physical world, yet collecting robot
    demonstrations at scale remains costly. Human demonstrations offer a scalable alternative, but existing egocentric human
    supervision often omits locomotion and posture, while embodiment differences and controller dynamics hinder accurate end-effector
    execution. We introduce ...
  zh: Lambda-humanoid Team 构建了 HumanVerse，一个 500 小时的开源世界人类全身移动操作数据集，将第一人称视角视频与同步的身体和手部运动配对。团队提出人-人形机器人迁移流水线，通过视角与手臂外观对齐及离线运动参考与控制器输入精修来降低末端执行器误差，并据此训练出人形基础模型
    $λ_0$。在 Unitree G1 上实现零样本迁移，$λ_0$ 在 SIMPLE 上达到 90.0% 成功率，真实世界移动操作任务平均成功率为 62.5%。
  ko: Humanoid loco-manipulation requires coordinated whole-body interaction with the physical world, yet collecting robot
    demonstrations at scale remains costly. Human demonstrations offer a scalable alternative, but existing egocentric human
    supervision often omits locomotion and posture, while embodiment differences and controller dynamics hinder accurate end-effector
    execution. We introduce ...
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
- humanoid_loco_manipulation
- egocentric_human_data
- human_to_humanoid_transfer
- humanoid_foundation_model
- whole_body_control
- zero_shot_transfer
- end
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.18950);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.18950 $λ_0$: Scaling Open-World Egocentric Human Data for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2610.18950
  date: '2026-10-13'
  accessed_at: '2026-10-19'
---

## 概述

人形机器人的全身移动操作需要与物理世界进行协调的全身交互，但大规模采集机器人演示成本高昂，而现有第一人称人类监督数据往往缺失移动与姿态信息，且具身差异与控制器动力学使末端执行器执行不准确。为此，Lambda-humanoid Team 提出 HumanVerse，一个 500 小时的开源世界人类移动操作数据集，将第一人称视频与同步的身体和手部运动配对。团队设计了人-人形机器人迁移流水线，对齐相机视角与手臂外观，并离线精修运动参考与控制器输入，在保持全身协调的同时减小末端执行器误差。该流水线通过向 Unitree G1 的零样本迁移在代表性全身操作与长程移动操作任务上得到验证，且无需目标任务的机器人演示。在此基础上，团队开发了面向全身移动操作的人形基础模型 $λ_0$，利用机器人对齐的人类演示为中训练提供监督；增加全身人类数据可稳定提升下游任务进展，$λ_0$ 在 SIMPLE 上取得 90.0% 成功率，在真实世界移动操作任务上平均成功率为 62.5%。

## 核心内容

### 问题背景

人形机器人的移动操作（loco-manipulation）要求全身协调地与物理世界交互。在规模化采集机器人演示数据成本高昂的背景下，人类演示被视为可扩展的替代方案。然而现有第一人称（egocentric）人类监督数据通常缺失移动与姿态信息，同时人形机器人与人类之间的具身差异以及控制器动力学差异，会导致末端执行器执行不准确。

### 方法

- **HumanVerse 数据集**：规模为 500 小时的开源世界人类移动操作数据，将第一人称视角视频与同步的身体运动、手部运动配对。
- **人-人形机器人迁移流水线**：对齐相机视角与手臂外观，并对运动参考与控制器输入进行离线精修，以在保持全身协调的前提下降低末端执行器误差。
- **$λ_0$ 基础模型**：面向全身移动操作的人形基础模型，以机器人对齐后的人类演示作为中训练（mid-training）阶段的监督信号。

### 实验设置

- 迁移验证平台为 Unitree G1，采用零样本迁移方式，不依赖目标任务的机器人演示。
- 验证任务涵盖代表性的全身操作任务与长程移动操作任务。
- 评测基准包括 SIMPLE，以及真实世界移动操作任务。

### 关键结果

- 增加全身人类数据可稳定提升下游任务进展。
- $λ_0$ 在 SIMPLE 上达到 90.0% 成功率。
- $λ_0$ 在真实世界移动操作任务上平均成功率为 62.5%。

### 结论

该研究验证了以人类第一人称数据支撑人形全身移动操作的可行路径，并期望为面向人形基础模型的可扩展全身人类数据采集提供指导，以实现与物理世界更丰富的交互。

## Overview

Humanoid loco-manipulation requires coordinated whole-body interaction with the physical world, yet collecting robot demonstrations at scale remains costly. Human demonstrations offer a scalable alternative, but existing egocentric human supervision often omits locomotion and posture, while embodiment differences and controller dynamics hinder accurate end-effector execution. We introduce HumanVerse, a 500-hour dataset of open-world human loco-manipulation pairing egocentric video with synchronized body and hand motion. Our human-to-humanoid pipeline aligns camera viewpoints and arm appearance, and refines motion references and controller inputs offline to reduce end-effector errors while preserving whole-body coordination. We validate the pipeline through zero-shot transfer to Unitree G1 on representative whole-body manipulation and long-range loco-manipulation tasks, without target-task robot demonstrations. Building on this pipeline, we develop $λ_0$, a humanoid foundation model for whole-body loco-manipulation, with robot-aligned human demonstrations providing supervision for mid-training. Increasing whole-body human data consistently improves downstream task progress. $λ_0$ achieves 90.0% success on SIMPLE and 62.5% across real-world loco-manipulation tasks. We expect this study to guide scalable whole-body human data collection toward humanoid foundation models for richer interaction with the physical world. Homepage: https://lambdahumanoid.github.io/

## 参考
- https://arxiv.org/abs/2610.18950
