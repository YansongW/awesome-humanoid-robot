---
$id: ent_paper_shukla_catch_it_all_generalizable_dyn_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand'
  zh: 'Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand'
  ko: 'Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand'
summary:
  en: Catching arbitrary objects requires generalization to novel projectiles and real-time adaptation to unpredictable contact
    dynamics under noisy visual observations. This paper presents Catch It All!, a sim-to-real catching framework for humanoid
    robots that generalizes and adapts to unseen objects with variable physical properties for underhand and overhand catches,
    using only one egocentric ...
  zh: Catch It All! 是一个面向人形机器人的 sim-to-real 抓接框架，由 Arth Shukla、Kehlani Fay、Huaze Liu、Darin Djapri、Alexiy Buynitsky、Nicklas
    Hansen 提出。该系统仅使用单个第一人称视角相机，即可对未见过的物体完成下手与上手抓接，并泛化到几何形状、形变性与弹性各异的物体。作者通过抓取奖励设计与安全感知课程学习，实现了接近硬件极限（腕部力矩低至 5 Nm）的高频动作执行，并在
    Unitree G1 上零样本部署验证。
  ko: Catching arbitrary objects requires generalization to novel projectiles and real-time adaptation to unpredictable contact
    dynamics under noisy visual observations. This paper presents Catch It All!, a sim-to-real catching framework for humanoid
    robots that generalizes and adapts to unseen objects with variable physical properties for underhand and overhand catches,
    using only one egocentric ...
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
- dynamic_catching
- sim_to_real
- dexterous_hand
- humanoid_robot
- grasp_policy
- zero_shot_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.39044);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.39044 Catch It All!: Generalizable Dynamic Catching with a Dexterous Hand'
  url: https://arxiv.org/abs/2610.39044
  date: '2026-10-28'
  accessed_at: '2026-11-02'
---

## 概述

该工作针对任意物体抓接中的泛化与实时适应难题：面对未知抛射物、不可预测的接触动力学以及带噪声的视觉观测，机器人需要同时具备泛化能力与快速反应能力。作者构建了一个 sim-to-real 抓接框架，仅依赖单个第一人称视角相机学习策略，使其能够泛化到几何形状、可形变性、弹性与物理属性各不相同的未见物体。为获得适应物体位姿与形状的有效抓取，研究团队精心设计了抓取奖励；同时引入安全感知的课程学习，使高频动作执行在接近硬件极限时仍然安全，腕部力矩限制低至 5 Nm。系统在 Unitree G1 上以零样本方式部署，对训练中未出现的 9 个物体成功完成下手与上手抓接，涵盖低回弹毛绒玩具、半形变玩具与薯片袋，以及接触时高回弹的刚弹性物体。

## 核心内容

### 问题背景

抓接任意物体是一项具有挑战性的机器人任务，其难点主要体现在三个方面：需要对新颖的抛射物具备泛化能力；需要在噪声视觉观测下对不可预测的接触动力学做出实时适应；还需要在接近硬件极限的条件下保证执行安全。现有方法往往难以同时满足泛化性与实时性要求。

### 方法

作者提出 Catch It All!，一个面向人形机器人的 sim-to-real 抓接框架，其核心设计包括：

- **单一第一人称视角感知**：系统仅使用一个 egocentric camera，不依赖外部或多视角视觉系统。
- **策略泛化**：学习到的策略能够泛化到几何形状、可形变性、弹性及物理属性各不相同的未见物体。
- **抓取奖励设计**：通过精心设计的抓取奖励，使机器人学到能够实时适应物体位姿与形状的有效抓取。
- **安全感知课程**：提供 safety-aware curricula，使高频动作执行在接近硬件极限时仍保持安全，其中包括低至 5 Nm 的腕部力矩限制。

### 实验设置

系统以零样本（zero-shot）方式部署在 Unitree G1 人形机器人上，仅使用单个第一人称视角相机。测试对象为训练阶段未出现的 9 个物体，覆盖下手抓接与上手抓接两种模式。

### 关键结果

- 在 9 个未见物体上成功完成下手与上手抓接。
- 测试物体涵盖低回弹毛绒玩具、半形变玩具与薯片袋，以及接触时高回弹的刚弹性物体。
- 验证了系统在腕部力矩限制低至 5 Nm 条件下的安全高频执行能力。

### 结论

Catch It All! 展示了仅凭单个第一人称视角相机即可实现可泛化的动态抓接，能够应对物理属性差异显著的未见物体，并在接近硬件极限的安全约束下完成实时抓接动作，为人形机器人在真实环境中的动态操作提供了可行路径。

## Overview

Catching arbitrary objects requires generalization to novel projectiles and real-time adaptation to unpredictable contact dynamics under noisy visual observations. This paper presents Catch It All!, a sim-to-real catching framework for humanoid robots that generalizes and adapts to unseen objects with variable physical properties for underhand and overhand catches, using only one egocentric camera. We learn policies which generalize to unseen objects with varying geometry, deformability, elasticity, and physical properties. Effective grasps which adapt real-time to object poses and shapes are learned through careful grasp reward design. We provide safety-aware curricula which enable safe, high-frequency action execution near hardware limits, including wrist torque limits as low as 5 Nm. We validate our system by deploying zero-shot on a Unitree G1. With only one egocentric camera, Catch It All! successfully performs underhand and overhand catches on 9 unseen objects not seen during training, including low-rebound plushes, semi-deformable toys and chip bags, and rigid-elastic objects with high rebound on contact.

## 参考
- https://arxiv.org/abs/2610.39044
