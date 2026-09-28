---
$id: ent_paper_panchal_smoothness_as_a_constraint_for_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Smoothness as a Constraint for Stable Humanoid Locomotion
  zh: Smoothness as a Constraint for Stable Humanoid Locomotion
  ko: Smoothness as a Constraint for Stable Humanoid Locomotion
summary:
  en: 'Embodied AI systems, particularly humanoid robots deployed in real world scenarios require whole-body control policies
    that are both task-responsive and physically smooth. However, smoothness is not uniform across the body: lower body must
    remain sufficiently reactive, while the upper body must be tightly regulated to preserve stability. Existing reinforcement
    learning approaches typically impose ...'
  zh: DeCap（Decoupled Constraint-aware policy）是一种约束强化学习算法，由 Utsav Panchal、Denis Kleyko、Unal Artan 与 Amy Loutfi 提出，用于人形机器人全身控制。该方法将全身平滑性解耦为上半身与下半身两组显式约束，并引入有界障碍惩罚以改善可行性边界附近的约束满足。在真实世界人形机器人全身控制任务上，DeCap
    相比基于奖励的平滑策略将上半身动作速率降低 2.50 倍、加速度降低 2.18 倍。
  ko: 'Embodied AI systems, particularly humanoid robots deployed in real world scenarios require whole-body control policies
    that are both task-responsive and physically smooth. However, smoothness is not uniform across the body: lower body must
    remain sufficiently reactive, while the upper body must be tightly regulated to preserve stability. Existing reinforcement
    learning approaches typically impose ...'
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
- humanoid_locomotion
- whole_body_control
- constrained_reinforcement_learning
- smoothness_constraint
- sim_to_real
- barrier_penalty
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.24552);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.24552 Smoothness as a Constraint for Stable Humanoid Locomotion
  url: https://arxiv.org/abs/2609.24552
  date: '2026-09-21'
  accessed_at: '2026-09-28'
---

## 概述

面向真实场景的具身智能系统，尤其是人形机器人，需要既响应任务又物理平滑的全身控制策略。然而平滑性在身体各部位并不一致：下半身需保持足够反应性，上半身则需严格约束以维持稳定。现有强化学习方法通常通过奖励函数中的辅助项施加平滑性，这些项与任务目标相互竞争，且将身体视为均质整体，无法直接控制决定平滑行为的物理量。为此作者提出 DeCap，一种将全身平滑性解耦为上半身与下半身独立约束组的约束强化学习算法，每组将平滑性表述为对物理运动极限的显式约束。为提升可行性边界附近的约束满足度，DeCap 引入有界障碍惩罚，在接近极限时主动激活并在约束极限处保持有界。在真实世界人形机器人全身控制任务上，DeCap 显著降低了上半身动作速率与加速度，同时改善了下半身平滑性并减少瞬态运动，且一组固定的平滑性约束可跨多种地形迁移，减轻了奖励调参负担。

## 核心内容

### 问题背景
真实世界部署的人形机器人需要全身控制策略同时具备任务响应能力与物理平滑性。但平滑性需求在身体各部位并不统一：下半身必须保持足够的反应性，上半身则需被严格约束以维持整体稳定。现有强化学习方案多将平滑性作为奖励函数中的辅助项，这类辅助项会与任务目标产生竞争，且把身体当作均质整体处理，无法直接控制导致平滑行为的物理量。

### 方法
作者提出 DeCap（Decoupled Constraint-aware policy），一种约束强化学习算法，其核心设计包括：
- 将全身平滑性解耦为上半身与下半身两个独立的约束组；
- 每个约束组把平滑性表述为对物理运动极限的显式约束；
- 引入有界障碍惩罚（bounded barrier penalty），在接近约束极限时主动激活，并在约束极限处保持有界，从而改善可行性边界附近的约束满足。

### 实验设置
在真实世界人形机器人全身控制任务上进行验证，并与基于奖励的平滑策略进行对比。

### 关键结果
- 相比基于奖励的平滑策略，DeCap 将上半身动作速率降低 2.50 倍，加速度降低 2.18 倍；
- 同时改善了下半身的平滑性，并减少了瞬态运动；
- 一组固定的平滑性约束可跨多种地形迁移，从而减轻了大规模奖励调参的需求。

### 结论
将平滑性从奖励项转为显式解耦约束，能够在不牺牲下半身反应性的前提下严格规范上半身运动，并在多种地形间保持一致的约束效果，为真实世界人形机器人全身控制提供了一种减少奖励调参依赖的可行路径。

## Overview

Embodied AI systems, particularly humanoid robots deployed in real world scenarios require whole-body control policies that are both task-responsive and physically smooth. However, smoothness is not uniform across the body: lower body must remain sufficiently reactive, while the upper body must be tightly regulated to preserve stability. Existing reinforcement learning approaches typically impose smoothness through auxiliary terms in the reward function, which compete with task objectives, treating the body as uniform and provide no direct control over the physical quantities responsible for smooth behavior. We introduce DeCap (Decoupled Constraint-aware policy), a constrained reinforcement learning algorithm that decouples whole-body smoothness into separate upper- and lower-body constraint groups, each formulates smoothness as explicit constraints on physical motion limits. To improve constraint satisfaction near feasibility boundaries, DeCap incorporates a bounded barrier penalty that activates proactively as limits are approached and remains bounded at the constraint limit. On real-world humanoid whole-body control task, DeCap reduces upper-body action rate by 2.50x and acceleration by 2.18x relative to reward-based smoothness policies, while also improving lower-body smoothness and reducing transient motion. We demonstrate that a fixed set of smoothness constraints transfers across diverse terrains, alleviating the need of extensive reward tuning.

## 参考
- https://arxiv.org/abs/2609.24552
