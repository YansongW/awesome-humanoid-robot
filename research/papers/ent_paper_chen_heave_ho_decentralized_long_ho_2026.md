---
$id: ent_paper_chen_heave_ho_decentralized_long_ho_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration'
  zh: 'Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration'
  ko: 'Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration'
summary:
  en: Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing
    this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization
    across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation.
    At the low level, we develop a ...
  zh: Heave-Ho 是一个面向长时程多 humanoid 协作运动与操作的去中心化框架，由 Ting-Hsuan Chen、Siheng Zhao 等研究者提出。其低层采用多智能体后训练方法，将 humanoid 基础跟踪模型适配到机器人间物理耦合交互，仅凭局部观测实现协调去中心化控制；高层训练视觉-语言规划器并设计基于语音的领-从协调机制，在无网络通信条件下同步去中心化执行。系统以两台相同
    humanoid 训练，可扩展至最多十台机器人团队，并无需重训练即可泛化到异构团队；作者同时提出包含 12 项任务（2 至 10 台 humanoid，含异构团队）的 HH-Bench 基准。
  ko: Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing
    this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization
    across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation.
    At the low level, we develop a ...
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
- multi_humanoid_collaboration
- decentralized_control
- long_horizon_planning
- loco_manipulation
- vision_language_planner
- humanoid_benchmark
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-23'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-23). Bibliographic metadata from arXiv API (2611.22275);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.22275 Heave-Ho: Decentralized Long-Horizon Multi-Humanoid Collaboration'
  url: https://arxiv.org/abs/2611.22275
  date: '2026-11-17'
  accessed_at: '2026-11-23'
- id: src_002
  type: website
  title: Project page
  url: https://heaveho-humanoid.github.io/
  accessed_at: '2026-11-23'
---

## 概述

Heave-Ho 针对多 humanoid 协作中的全身交互协调、长时程规划一致性与机器人间精确同步难题，提出一套去中心化框架。低层通过多智能体后训练，把 humanoid 基础跟踪模型改造为适应机器人间物理耦合的控制器，使各机器人仅依赖局部观测即可协同行动。高层则训练视觉-语言规划器，并借助基于语音的领-从机制在无网络通信下同步各机器人的执行。该系统仅用两台相同 humanoid 训练，却能扩展到最多十台机器人，并对异构团队具备零重训练泛化能力。为系统评估这些能力，作者构建了 HH-Bench，覆盖 2 至 10 台 humanoid 的 12 项任务（含异构团队），实验显示 Heave-Ho 稳定优于基线方法，真实世界实验也验证了其在挑战性任务上的稳健去中心化协作。

## 核心内容

### 问题背景
多 humanoid 协作有望把机器人能力拓展到单机难以达到的水平，但其实现依赖三个难点：协调的全身交互、连贯的长时程规划，以及机器人之间的精确同步。现有方法难以同时满足这些要求，尤其难以在去中心化、无网络通信的条件下完成长时程协作。

### 方法
- **低层控制**：提出多智能体后训练框架，将 humanoid 基础跟踪模型适配到 humanoid 之间的物理耦合交互，使各机器人仅凭局部观测即可实现协调的去中心化控制。
- **高层规划与协调**：训练视觉-语言规划器，并设计基于语音的领-从协调机制，在无网络通信的情况下同步去中心化执行。
- **训练与扩展**：系统以两台相同 humanoid 进行训练，可扩展到最多十台机器人组成的团队，并无需重训练即可泛化到异构团队。

### 实验设置与基准
作者提出 HH-Bench 基准，包含 12 项任务，涉及 2 至 10 台 humanoid 组成的团队，其中包括异构团队。

### 关键结果
系统性评估表明，Heave-Ho 在各项评测中稳定优于基线方法；真实世界实验进一步展示了其在挑战性任务上的稳健去中心化协作能力。

### 结论
Heave-Ho 通过低层多智能体后训练与高层视觉-语言规划及语音领-从协调的结合，实现了无网络通信条件下的长时程多 humanoid 去中心化协作，并具备向更大规模及异构团队扩展的能力。

## Overview

Collaboration promises to extend humanoid capabilities beyond what individual robots can achieve. However, realizing this potential requires coordinated whole-body interactions, coherent long-horizon planning, and precise synchronization across robots. We introduce Heave-Ho, a decentralized framework for long-horizon collaborative multi-humanoid loco-manipulation. At the low level, we develop a multi-agent post-training framework that adapts a humanoid foundation tracking model to physically coupled interactions between humanoids, enabling coordinated decentralized control from local observations alone. At the high level, we train a vision-language planner and design a speech-based leader-follower coordination mechanism to synchronize decentralized execution without network communication. Trained with two identical humanoids, our system scales to teams of up to ten robots and generalizes to heterogeneous teams without retraining. To benchmark these capabilities, we introduce HH-Bench, comprising 12 tasks involving teams of 2 to 10 humanoids, including heterogeneous teams. Systematic evaluations show that Heave-Ho consistently outperforms baseline methods, while real-world experiments demonstrate robust decentralized collaboration across challenging tasks.

## 参考
- https://arxiv.org/abs/2611.22275
- https://heaveho-humanoid.github.io/
