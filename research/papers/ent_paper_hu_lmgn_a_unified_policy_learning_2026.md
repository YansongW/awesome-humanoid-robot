---
$id: ent_paper_hu_lmgn_a_unified_policy_learning_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation'
  zh: 'LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation'
  ko: 'LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation'
summary:
  en: Legged robots equipped with manipulators have shown significant potential in the fields of daily life and industry in
    complex environments. However, existing methods mainly focus on global navigation or manipulation independently, while
    overlooking the last-mile navigation problem, where the robot must jointly determine the base placement, approach direction,
    and grasp execution to achieve ...
  zh: LMGN 是面向四足机器人 loco-manipulation 的统一策略学习模型，由 Xuenmin Hu、Qingxue Qian、Wei Luo、Benyi Ma、Bo Tang、Long Chen 提出，旨在解决"最后一公里"抓取导航问题，即机器人需联合决定基座落点、接近方向与抓取执行。模型引入
    ED-DR 表示显式刻画可抓取基座位置与接近方向特征，并设计语义对齐的 HMoE 策略建模分阶段行为，在 Habitat 与 Isaac Gym 仿真中持续优于现有方法。
  ko: Legged robots equipped with manipulators have shown significant potential in the fields of daily life and industry in
    complex environments. However, existing methods mainly focus on global navigation or manipulation independently, while
    overlooking the last-mile navigation problem, where the robot must jointly determine the base placement, approach direction,
    and grasp execution to achieve ...
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
- loco_manipulation
- last_mile_navigation
- quadruped_robot
- grasp_navigation
- mixture_of_experts
- policy_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.07515);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.07515 LMGN: A Unified Policy Learning Model for Last-Mile Grasp-Navigation'
  url: https://arxiv.org/abs/2611.07515
  date: '2026-11-05'
  accessed_at: '2026-11-09'
---

## 概述

现有带机械臂的足式机器人研究多将全局导航与操作分开处理，忽略了最后一公里导航这一关键环节：机器人必须同时确定基座放置、接近方向与抓取执行，且不同操作阶段需要不同的控制行为。为此，作者提出 LMGN 统一策略学习模型，首先用 Explicit Distance and Directional Reachability（ED-DR）表示显式编码与抓取兼容的基座落点及接近方向特征，再构建语义对齐的 Hierarchical Mixture-of-Experts（HMoE）策略，对基座调整、预抓取对齐、抓取执行与物体抬升等阶段进行分阶段建模。训练上提出联合对齐导航与操作、阶段相关专家路由与动作级一致性的优化方法。在 Habitat 与 Isaac Gym 上的实验表明，LMGN 稳定超越当前最优方法，说明将抓取感知可达性与阶段感知策略学习结合能显著提升最后一公里导航与目标抓取成功率。

## 核心内容

### 问题背景
带机械臂的足式机器人在日常生活与工业复杂环境中潜力显著，但现有方法多分别研究全局导航或操作，忽视了最后一公里导航问题。该场景要求机器人联合确定基座放置、接近方向与抓取执行，才能可靠抓取目标；同时不同操作阶段需要不同的控制行为，给统一策略学习带来挑战。

### 方法
- **ED-DR 表示**：提出 Explicit Distance and Directional Reachability 表示，显式刻画与抓取兼容的基座落点及接近方向特征。
- **HMoE 策略**：设计语义对齐的 Hierarchical Mixture-of-Experts 策略，对基座调整、预抓取对齐、抓取执行与物体抬升等阶段的分阶段行为建模。
- **优化方法**：提出联合对齐导航与操作、阶段相关专家路由以及动作级一致性的优化方式，用于训练 HMoE 策略。

### 实验设置
在 Habitat 与 Isaac Gym 两个仿真器上开展大量实验，与当前最优方法进行对比。

### 关键结果
LMGN 在两个仿真环境中持续优于现有最优方法，表明将抓取感知可达性与阶段感知策略学习相结合，可显著提升机器人最后一公里导航与目标抓取的成功率。

### 结论
面向四足机器人 loco-manipulation 的最后一公里抓取导航，统一建模基座落点、接近方向与分阶段抓取行为是有效路径。

## Overview

Legged robots equipped with manipulators have shown significant potential in the fields of daily life and industry in complex environments. However, existing methods mainly focus on global navigation or manipulation independently, while overlooking the last-mile navigation problem, where the robot must jointly determine the base placement, approach direction, and grasp execution to achieve reliable object grasping, and different manipulation stages require distinct control behaviors. To address these challenges, we propose Last-Mile Grasp-Navigation (LMGN), a unified policy learning model for Quadruped robot loco-manipulation. An Explicit Distance and Directional Reachability (ED-DR) representation is first introduced to explicitly represent the features of grasp-compatible base placement and approach direction. We then develop a semantically aligned Hierarchical Mixture-of-Experts (HMoE) policy that models stage-aware behaviors across the stages of base adjustment, pre-grasp alignment and grasp execution, and object lift. Finally, a new optimization method that jointly aligns navigation and manipulation, stage-dependent expert routing, and action-level consistency is proposed to optimize the HMoE policy. Extensive experiments on the Habitat and Isaac Gym simulators demonstrate that LMGN consistently outperforms state-of-the-art methods, denoting that integrating grasp-aware reachability with stage-aware policy learning significantly improves the success rates of last-mile navigation and target grasp for robots.

## 参考
- https://arxiv.org/abs/2611.07515
