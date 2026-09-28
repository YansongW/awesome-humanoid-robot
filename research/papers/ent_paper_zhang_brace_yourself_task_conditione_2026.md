---
$id: ent_paper_zhang_brace_yourself_task_conditione_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Brace Yourself: Task-Conditioned Environmental Bracing for Forceful Humanoid Manipulation'
  zh: 'Brace Yourself: Task-Conditioned Environmental Bracing for Forceful Humanoid Manipulation'
  ko: 'Brace Yourself: Task-Conditioned Environmental Bracing for Forceful Humanoid Manipulation'
summary:
  en: Forceful manipulation is challenging for humanoid robots because interaction forces can disturb whole-body balance.
    We introduce the Supporting Hand Strategy (SHS), which enables a humanoid to brace against the environment with one hand
    while performing forceful manipulation with the other. SHS optimises a task-conditioned support configuration that guides
    two synchronous reinforcement-learning ...
  zh: 本文提出 Supporting Hand Strategy (SHS)，让 humanoid 机器人用一只手支撑环境、另一只手执行强力操作，从而缓解交互力对全身平衡的干扰。作者为 Zongyuan Zhang、Christopher
    Lehnert、Will N. Browne 与 Jonathan M. Roberts。在 Unitree G1 上，SHS 实现最高 60 N 的可用接触力，而无环境支撑时最大持续力仅为 13.5 N，并显著改善了力跟踪表现。
  ko: Forceful manipulation is challenging for humanoid robots because interaction forces can disturb whole-body balance.
    We introduce the Supporting Hand Strategy (SHS), which enables a humanoid to brace against the environment with one hand
    while performing forceful manipulation with the other. SHS optimises a task-conditioned support configuration that guides
    two synchronous reinforcement-learning ...
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
- humanoid_manipulation
- forceful_manipulation
- reinforcement_learning
- environmental_bracing
- whole_body_balance
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.25486);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.25486 Brace Yourself: Task-Conditioned Environmental Bracing for Forceful Humanoid Manipulation'
  url: https://arxiv.org/abs/2609.25486
  date: '2026-09-21'
  accessed_at: '2026-09-28'
- id: src_002
  type: website
  title: Project page
  url: https://youtu.be/zPrGLxWJzI4
  accessed_at: '2026-09-28'
---

## 概述

强力操作对人形机器人而言十分困难，因为交互力会破坏全身平衡。为此，作者提出 Supporting Hand Strategy (SHS)：机器人以一只手抵住环境形成支撑，另一只手完成强力操作。SHS 通过优化一个由任务条件决定的支撑构型，来引导两个同步的强化学习策略，整个过程不依赖人类运动数据，也不需要在线全身轨迹规划。在 Unitree G1 平台上，SHS 达到最高 60 N 的可用接触力，远高于无环境支撑时 13.5 N 的最大持续力，同时相比与任务无关的支撑构型大幅提升了力跟踪效果。相同策略无需重新训练即可泛化到不同任务区域，说明 SHS 是一种简单且能显著扩展人形机器人强力操作能力的机制。

## 核心内容

### 问题背景
人形机器人在执行强力操作时，交互力会干扰全身平衡，因此难以稳定施加较大的力。现有做法往往依赖人类运动数据或在线全身轨迹规划，复杂度较高。

### 方法
作者提出 Supporting Hand Strategy (SHS)：让机器人用一只手抵住环境作为支撑，另一只手进行强力操作。SHS 优化一个由任务条件决定的支撑构型，并用它引导两个同步的强化学习策略。该方法不需要人类运动数据，也不需要在线全身轨迹规划。

### 实验设置
实验在 Unitree G1 人形机器人上进行，对比了有环境支撑与无环境支撑两种情况，并进一步与任务无关的支撑构型进行比较。

### 关键结果
- 在 Unitree G1 上，SHS 实现可用的接触力最高达 60 N。
- 无环境支撑时，最大持续力仅为 13.5 N。
- 相比任务无关的支撑构型，SHS 显著改善了力跟踪表现。
- 同一套策略无需重新训练即可泛化到不同的任务区域。

### 结论
SHS 提供了一种简单机制，能够大幅扩展人形机器人的强力操作能力。

## Overview

Forceful manipulation is challenging for humanoid robots because interaction forces can disturb whole-body balance. We introduce the Supporting Hand Strategy (SHS), which enables a humanoid to brace against the environment with one hand while performing forceful manipulation with the other. SHS optimises a task-conditioned support configuration that guides two synchronous reinforcement-learning policies, without human motion data or online whole-body trajectory planning. On a Unitree G1, SHS achieved usable contact forces up to 60 N, compared with a maximum sustained force of 13.5 N without environmental bracing, while substantially improving force tracking over a task-independent support configuration. The same policies generalised to different task regions without retraining. SHS therefore provides a simple mechanism for substantially extending humanoid forceful-manipulation capability.

## 参考
- https://arxiv.org/abs/2609.25486
- https://youtu.be/zPrGLxWJzI4
