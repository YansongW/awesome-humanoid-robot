---
$id: ent_paper_ru_adaptive_aerial_loco_manipulat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation
  zh: Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation
  ko: Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation
summary:
  en: Loco-manipulation extends the workspace of conventional manipulation by combining mobility with physical interaction,
    while aerial loco-manipulation further expands this capability into three-dimensional space, enabling robots to reach
    environments inaccessible to ground-based systems. Moving to an aerial platform, however, gives rise to a demanding control
    problem, since the vehicle must track ...
  zh: ALMA 是一个面向空中作业机器人（飞行平台搭载机械臂）的自适应飞行控制框架，由 Jingyu Ru、Xiangyuan Xie 等人提出。其核心是上下文飞行策略：利用动作条件化的未来测量表征预测来训练上下文，使策略能从近期测量与动作中保留与飞行控制相关的响应信息；同时借助
    LLM 分析控制难点并生成新的机械臂运动结构，以扩展训练经验。仿真中位置 RMSE 相对最强基线最多降低 24.7%，同一策略零样本迁移到真实空中作业平台后，在周期性机械臂运动下悬停位置 RMSE 相对真实世界基线降低 79.6%。
  ko: Loco-manipulation extends the workspace of conventional manipulation by combining mobility with physical interaction,
    while aerial loco-manipulation further expands this capability into three-dimensional space, enabling robots to reach
    environments inaccessible to ground-based systems. Moving to an aerial platform, however, gives rise to a demanding control
    problem, since the vehicle must track ...
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
- aerial_loco_manipulation
- adaptive_flight_control
- context_adaptive_policy
- llm_assisted_task_generation
- sim_to_real_transfer
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.30810);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.30810 Adaptive Aerial Loco-Manipulation Policy Learning via LLM-Assisted Proactive Task Generation
  url: https://arxiv.org/abs/2610.30810
  date: '2026-10-22'
  accessed_at: '2026-10-26'
---

## 概述

空中作业操作把移动能力与物理交互结合并拓展到三维空间，但机械臂运动与接触会持续改变质心、惯量并给机体带来力与力矩扰动，使三维轨迹跟踪成为困难的控制问题。传统控制器依赖显式建模与估计，学习型控制器虽可从经验中推断动力学，但控制奖励无法直接指导历史响应信息的保留，固定任务采样也容易让持续存在的跟踪难点得不到充分探索。为此作者提出 ALMA：一个在外部机械臂指令下实现自适应飞行控制的空中作业操作框架。它采用上下文飞行策略，从近期测量与动作中自适应，并通过动作条件化的未来测量表征预测来训练上下文，使其保留对飞行控制有用的响应信息；同时用 LLM 驱动的进化过程分析观测到的控制困难，提出新的机械臂运动结构以扩充训练经验。仿真中位置 RMSE 相对最强基线最多降低 24.7%，同一策略零样本迁移到真实空中作业平台，在周期性机械臂运动下悬停位置 RMSE 相对真实世界基线降低 79.6%。

## 核心内容

### 问题背景

空中作业操作将移动操作的能力延伸到三维空间，使机器人能够到达地面系统难以进入的环境。但把作业操作搬到飞行平台上会带来苛刻的控制难题：飞行器需要在三维空间中精确跟踪轨迹，而机械臂的运动及其与环境交互会持续改变质心、改变惯量，并对机体施加力与力矩扰动。传统控制器通过显式模型与估计来处理这些效应；学习型控制器则从经验中推断动力学，但控制奖励并不能为“从历史中保留哪些响应信息”提供直接目标，固定的任务采样也可能使持续存在的跟踪困难得不到充分探索。

### 方法

作者提出 ALMA，一个在外部机械臂指令下实现自适应飞行控制的空中作业操作框架，主要包含两部分：

- **上下文飞行策略**：策略从近期的测量与动作中进行自适应。其上下文通过动作条件化的未来测量表征预测来训练，从而让上下文保留与飞行控制相关的响应信息。
- **LLM 辅助的主动任务生成**：为扩大可用于自适应的经验，采用一个进化过程，利用大语言模型（LLM）分析观测到的控制困难，并提出新的机械臂运动结构，供后续训练使用。

### 实验设置与关键结果

- 仿真实验中，ALMA 的位置 RMSE 相对最强基线最多降低 **24.7%**。
- 同一策略零样本迁移到真实空中作业平台；在周期性机械臂运动下，悬停位置 RMSE 相对真实世界基线降低 **79.6%**。

### 结论

ALMA 通过让上下文显式保留与飞行控制相关的历史响应信息，并借助 LLM 主动生成针对控制难点的机械臂运动结构，提升了空中作业操作中的自适应飞行控制性能，且策略可零样本迁移到真实平台。

## Overview

Loco-manipulation extends the workspace of conventional manipulation by combining mobility with physical interaction, while aerial loco-manipulation further expands this capability into three-dimensional space, enabling robots to reach environments inaccessible to ground-based systems. Moving to an aerial platform, however, gives rise to a demanding control problem, since the vehicle must track trajectories accurately in three dimensions while the motion of the arm and its interaction with the environment continuously shift the center of mass, alter the inertia, and impose force and moment disturbances on the body. Conventional controllers address these effects through explicit models and estimation, whereas learning-based controllers infer dynamics from experience, yet control rewards provide no direct target for the response information retained from history, and fixed task sampling can leave persistent tracking difficulties insufficiently explored. We present ALMA, an aerial loco-manipulation framework for adaptive flight control under external arm commands. ALMA employs a contextual flight policy that adapts from recent measurements and actions, using action-conditioned prediction of future measurement representations to train its context to retain response information relevant to flight control. To expand the experience available for this adaptation, an evolutionary process uses a large language model (LLM) to analyze observed control difficulties and propose new structures of arm motion for subsequent training. In simulation, ALMA reduces position root-mean-square error (RMSE) by up to 24.7% relative to the strongest baseline, while the same policy transfers zero-shot to the aerial manipulator and reduces hover position RMSE by 79.6% during periodic arm motion relative to the real-world baseline.

## 参考
- https://arxiv.org/abs/2610.30810
