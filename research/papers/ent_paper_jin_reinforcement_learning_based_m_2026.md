---
$id: ent_paper_jin_reinforcement_learning_based_m_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator
  zh: Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator
  ko: Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator
summary:
  en: Legged robots equipped with manipulators offer promising capabilities for loco-manipulation tasks in unstructured environments.
    However, achieving task-consistent end-effector behavior during locomotion remains challenging due to terrain-induced
    disturbances and the strong coupling between locomotion and manipulation, particularly for small-scale quadruped platforms.
    A reinforcement-learning ...
  zh: 该论文提出一种基于强化学习的四足机械臂全身控制框架，用于复杂地形上的移动操作任务。作者来自相关研究团队（Yanzhou Jin 等），核心贡献在于将混合任务表示与任务优先级全身学习相结合，在运动过程中保持末端执行器的任务一致性，并搭建轻量化四足机械臂平台进行验证。实机实验在坡度达
    30 度的斜坡、楼梯和可变形地形上成功部署。
  ko: Legged robots equipped with manipulators offer promising capabilities for loco-manipulation tasks in unstructured environments.
    However, achieving task-consistent end-effector behavior during locomotion remains challenging due to terrain-induced
    disturbances and the strong coupling between locomotion and manipulation, particularly for small-scale quadruped platforms.
    A reinforcement-learning ...
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
- quadruped_manipulator
- whole_body_control
- reinforcement_learning
- loco_manipulation
- terrain_adaptation
- task_consistency
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.23548);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.23548 Reinforcement Learning Based Multi-Terrain Adaptive Whole-Body Control for a Quadruped Manipulator
  url: https://arxiv.org/abs/2610.23548
  date: '2026-10-16'
  accessed_at: '2026-10-19'
---

## 概述

带机械臂的腿足机器人有望在非结构化环境中执行移动操作任务，但地形扰动以及运动与操作之间的强耦合，使运动过程中保持末端执行器行为与任务一致变得困难，这在小型四足平台上尤为突出。为此，作者提出一种基于强化学习的全身控制框架，通过混合任务表示与任务优先级全身学习来协调运动与操作，同时维持末端执行器的任务一致性行为。为验证该框架，作者还研制了轻量化四足机械臂平台，并在真实环境中开展实验。结果表明，该策略可在坡度达 30 度的斜坡、楼梯及可变形地形上成功部署，说明学习型全身控制策略用于真实环境四足移动操作具有可行性，也凸显了任务一致性全身协调对地形自适应移动操作的重要性。

## 核心内容

### 问题背景
带机械臂的腿足机器人具备在非结构化环境中执行移动操作（loco-manipulation）的潜力。然而，地形引起的扰动以及运动与操作之间的强耦合，使得在移动过程中保持末端执行器行为与任务一致十分困难，对小型四足平台而言挑战更大。

### 方法
作者提出一种基于强化学习的全身控制框架，用于复杂地形上的四足移动操作。该框架包含两个关键设计：
- 混合任务表示（hybrid task representation）；
- 任务优先级全身学习（task-prioritized whole-body learning）。

二者共同用于协调运动与操作，并在移动过程中保持末端执行器的任务一致性行为。

### 实验设置
作者研制了一个轻量化四足机械臂平台，用于在小型四足系统上验证所提框架，并开展真实环境实验。

### 关键结果
实机实验在以下复杂地形上成功部署：
- 坡度达 30 度的斜坡；
- 楼梯；
- 可变形地形。

### 结论
结果证明了将学习型全身控制策略部署于真实环境四足移动操作的可行性，并凸显了任务一致性全身协调对地形自适应移动操作的重要性。

## Overview

Legged robots equipped with manipulators offer promising capabilities for loco-manipulation tasks in unstructured environments. However, achieving task-consistent end-effector behavior during locomotion remains challenging due to terrain-induced disturbances and the strong coupling between locomotion and manipulation, particularly for small-scale quadruped platforms. A reinforcement-learning based whole-body control framework is proposed for quadruped loco-manipulation on complex terrain. The proposed framework combines a hybrid task representation with task-prioritized whole-body learning to coordinate locomotion and manipulation while preserving task-consistent end-effector behavior. A lightweight quadruped manipulator platform is further developed to validate the proposed framework on a small-scale quadruped system. Real-world experiments demonstrate successful deployment on complex terrains such as slopes up to 30 degrees, stairs, and deformable terrain. These results demonstrate the feasibility of deploying learned whole-body control policy for quadruped loco-manipulation in real-world environments and highlight the importance of task-consistent whole-body coordination for terrain-adaptive loco-manipulation.

## 参考
- https://arxiv.org/abs/2610.23548
