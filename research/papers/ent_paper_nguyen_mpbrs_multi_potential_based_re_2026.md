---
$id: ent_paper_nguyen_mpbrs_multi_potential_based_re_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion'
  zh: 'MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion'
  ko: 'MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion'
summary:
  en: Designing and tuning reward functions remains one of the main challenges in building effective reinforcement learning
    (RL) pipelines for humanoid locomotion. While shaping rewards can accelerate learning, naively formulated terms often
    conflict with the desired behavior, overfit to a specific robot, or become unstable under small weight changes. Potential-Based
    Reward Shaping (PBRS) offers an ...
  zh: MPBRS 是一种面向人形机器人运动控制的统一奖励配置方法，由 Van Chung Nguyen 与 Hung Manh La 提出。该方法基于多势函数奖励塑形（Multi-Potential-Based Reward Shaping），在九种人形机器人上复用同一套奖励结构与权重，仅需机器人特定的关节/连杆映射与默认姿态等元数据。实验表明，相比标准奖励塑形，MPBRS
    具有更一致的缩放行为并降低了对权重调整的敏感性。
  ko: Designing and tuning reward functions remains one of the main challenges in building effective reinforcement learning
    (RL) pipelines for humanoid locomotion. While shaping rewards can accelerate learning, naively formulated terms often
    conflict with the desired behavior, overfit to a specific robot, or become unstable under small weight changes. Potential-Based
    Reward Shaping (PBRS) offers an ...
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
- reward_shaping
- humanoid_locomotion
- potential_based_reward_shaping
- reinforcement_learning
- reward_configuration
- cross_robot_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.30334);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.30334 MPBRS: Multi-Potential-Based Reward Shaping for Unified Reward Configuration in Humanoid Locomotion'
  url: https://arxiv.org/abs/2610.30334
  date: '2026-10-21'
  accessed_at: '2026-10-26'
---

## 概述

在人形机器人强化学习流程中，奖励函数的设计与调参长期是主要难点：直接构造的塑形项容易与目标行为冲突、过拟合到特定机器人，或在权重微小变化下变得不稳定。势函数奖励塑形（PBRS）通过势函数差分构造塑形项，可在不改变最优策略的前提下引导探索。本文研究面向人形机器人运动控制的多势函数奖励塑形（MPBRS），并提出一种统一的奖励配置。作者在九种人形机器人上评估同一套奖励结构与权重，只需提供机器人特定的元数据（关节/连杆映射与默认姿态），而无需为每个机器人重新设计奖励。结果显示，与标准塑形相比，MPBRS 在不同机器人间表现出更一致的缩放行为与更低的调参敏感性，从而在不改变最优策略的情况下更易调参。

## 核心内容

### 问题背景

为人形机器人构建有效的强化学习流程时，奖励函数的设计与调参是主要挑战之一。奖励塑形虽可加速学习，但朴素构造的奖励项常与期望行为相冲突、对特定机器人过拟合，或在权重小幅变动时表现不稳定。势函数奖励塑形（PBRS）提供了另一条路径：以势函数之差构造塑形奖励，在不改变最优策略的前提下引导探索。

### 方法

- 研究面向人形机器人运动控制的多势函数奖励塑形（MPBRS）。
- 提出一种统一的奖励配置，使同一套奖励结构与权重可跨机器人复用。
- 跨机器人迁移仅依赖机器人特定元数据，即关节/连杆映射与默认姿态，无需逐机器人重新设计奖励。

### 实验设置

在九种人形机器人上评估同一奖励结构与权重。

### 关键结果

- 与标准塑形相比，MPBRS 表现出更一致的缩放行为。
- MPBRS 降低了跨机器人的调参敏感性，使调参更容易。
- 上述特性在不改变最优策略的前提下实现。

### 结论

MPBRS 为多机器人人形运动控制提供了一种统一、易调且不改变最优策略的奖励配置方案，减少了对逐机器人奖励重设计的依赖。

## Overview

Designing and tuning reward functions remains one of the main challenges in building effective reinforcement learning (RL) pipelines for humanoid locomotion. While shaping rewards can accelerate learning, naively formulated terms often conflict with the desired behavior, overfit to a specific robot, or become unstable under small weight changes. Potential-Based Reward Shaping (PBRS) offers an alternative solution: shaping the reward via differences of a potential function to guide exploration without changing the optimal policy. In this paper, we study Multi-PBRS for humanoid locomotion and propose a unified reward configuration. We then evaluate the same reward structure and weights across nine humanoid robots, requiring only robot-specific metadata (joint/link mappings and default poses) rather than per-robot reward redesign. Our experiments show that, compared to standard shaping, MPBRS provides more consistent scaling behavior and reduced tuning sensitivity across robots, making it easier to tune without altering the optimal policy.

## 参考
- https://arxiv.org/abs/2610.30334
