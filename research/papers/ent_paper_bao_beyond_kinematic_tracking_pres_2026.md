---
$id: ent_paper_bao_beyond_kinematic_tracking_pres_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control'
  zh: 'Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control'
  ko: 'Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control'
summary:
  en: Whole-body control plays a crucial role in enabling humanoid robots to execute expressive motions. Faithful execution
    requires preserving both the intended action and its expressive characteristics. Existing whole-body trackers typically
    balance joint and keypoint tracking with physical stability across diverse motions, but these objectives do not necessarily
    prioritize the expressive ...
  zh: 该论文关注人形机器人全身控制中动作表现力特征的保留问题，指出平均位置跟踪误差更低并不必然意味着动态与姿态特征保留得更好。作者提出一种残差学习框架，引入针对幅度、能量、身体扩展、身体倾斜与骨盆高度的补偿目标，并通过运动感知门控按身体部位活跃度分配修正能力。在
    Unitree G1 上针对八类动作开展的仿真与实物实验表明，该方法相比对应基线能更好地保留动态与姿态运动特征。
  ko: Whole-body control plays a crucial role in enabling humanoid robots to execute expressive motions. Faithful execution
    requires preserving both the intended action and its expressive characteristics. Existing whole-body trackers typically
    balance joint and keypoint tracking with physical stability across diverse motions, but these objectives do not necessarily
    prioritize the expressive ...
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
- humanoid_whole_body_control
- residual_learning
- motion_expressiveness
- motion_aware_gating
- policy_distillation
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.19393);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.19393 Beyond Kinematic Tracking: Preserving Expressive Characteristics in Humanoid Whole-Body Control'
  url: https://arxiv.org/abs/2610.19393
  date: '2026-10-14'
  accessed_at: '2026-10-19'
---

## 概述

人形机器人要忠实执行富有表现力的动作，不仅要复现目标动作本身，还需保留其表现力特征。现有全身跟踪器通常在关节与关键点跟踪和物理稳定性之间做权衡，但这些目标未必优先考虑每个动作的表现力特征。作者的分析表明，较低的平均位置跟踪误差并不能保证更好地保留动态与姿态运动特征。为此，论文提出一种残差学习框架，以幅度、能量、身体扩展、身体倾斜和骨盆高度为补偿目标，并借助运动感知门控按身体部位活跃度分配修正能力，在活跃部位保留更大的修正范围、在其他部位加以限制。针对每个冻结的跟踪器，作者训练运动特定的残差策略，并将其蒸馏为跨动作类别共享的统一策略；在 Unitree G1 上的仿真与实物实验覆盖八类动作，结果显示该方法在保留动态与姿态运动特征方面优于对应基线。

## 核心内容

### 问题背景

- 全身控制是人形机器人执行富有表现力动作的关键环节，忠实执行需要同时保留预期动作及其表现力特征。
- 现有全身跟踪器通常在不同动作之间平衡关节与关键点跟踪以及物理稳定性，但这些目标并不一定优先考虑每个动作的表现力特征。
- 作者的分析显示：平均位置跟踪误差更低，并不保证动态与姿态运动特征被更好地保留。

### 方法

- 提出一种残差学习框架，其补偿目标针对幅度、能量、身体扩展、身体倾斜与骨盆高度。
- 引入运动感知门控（motion-aware gating），按身体部位活跃度分配修正能力：在更活跃的部位保留更大的修正范围，在其他部位则加以限制，从而集中补偿并减少对底层跟踪行为的干扰。
- 针对每个冻结的跟踪器训练运动特定的残差策略，并将其蒸馏为跨动作类别共享的统一策略。

### 实验设置

- 在 Unitree G1 上进行仿真与实物实验。
- 实验覆盖八类动作。

### 关键结果

- 与对应基线相比，该方法在八类动作上展现出更优的动态与姿态运动特征保留效果。

### 结论

- 保留动作的表现力特征不能仅依赖降低平均位置跟踪误差，需要针对表现力相关目标进行专门补偿；残差学习配合运动感知门控与策略蒸馏为实现这一目标提供了可行途径。

## Overview

Whole-body control plays a crucial role in enabling humanoid robots to execute expressive motions. Faithful execution requires preserving both the intended action and its expressive characteristics. Existing whole-body trackers typically balance joint and keypoint tracking with physical stability across diverse motions, but these objectives do not necessarily prioritize the expressive characteristics of each action. Our analysis shows that lower average positional tracking error does not guarantee better preservation of dynamic and postural motion characteristics. To address this gap, we propose a residual learning framework with compensation objectives targeting amplitude, energy, body expansion, body lean, and pelvis height. To concentrate compensation while limiting interference with the underlying tracking behavior, motion-aware gating allocates correction capacity according to body-part activity, preserving larger correction ranges in more active parts and restricting them elsewhere. For each frozen tracker, we train motion-specific residual policies and distill them into a unified policy shared across motion categories. Simulation and physical experiments on the Unitree G1 across eight motion categories demonstrate superior preservation of dynamic and postural motion characteristics compared with the corresponding baselines.

## 参考
- https://arxiv.org/abs/2610.19393
