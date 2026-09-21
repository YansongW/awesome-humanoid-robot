---
$id: ent_paper_chen_learning_holistic_whole_body_l_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Holistic Whole-Body Loco-Manipulation with a Bipedal Mobile Manipulator
  zh: Learning Holistic Whole-Body Loco-Manipulation with a Bipedal Mobile Manipulator
  ko: Learning Holistic Whole-Body Loco-Manipulation with a Bipedal Mobile Manipulator
summary:
  en: Bipedal loco-manipulation enables robots to interact with objects beyond the nominal workspace of their arms by coordinating
    locomotion and manipulation. Realizing this capability requires a low-level whole-body controller that translates task-level
    manipulation goals into coordinated arm and leg motions while maintaining balance. We present a unified whole-body controller
    trained with ...
  zh: 本文提出一个面向双足移动操作机器人的统一全身控制器，通过强化学习直接将 6-DoF 末端执行器目标映射为双足基座与机械臂的协调动作。作者来自 Zhongyu Chen、Yuxuan Nai、Qian Chen 等组成的团队。核心设计包括调节末端跟踪、行走与平衡之间权衡的奖励门控策略，以及融合窗口化
    Transformer 编码、GRU 循环记忆与辅助动力学预测的时间上下文估计器。
  ko: Bipedal loco-manipulation enables robots to interact with objects beyond the nominal workspace of their arms by coordinating
    locomotion and manipulation. Realizing this capability requires a low-level whole-body controller that translates task-level
    manipulation goals into coordinated arm and leg motions while maintaining balance. We present a unified whole-body controller
    trained with ...
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
- whole_body_control
- bipedal_loco_manipulation
- reinforcement_learning
- mobile_manipulator
- end_effector_tracking
- temporal_context_estimator
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.18930);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2609.18930 Learning Holistic Whole-Body Loco-Manipulation with a Bipedal Mobile Manipulator
  url: https://arxiv.org/abs/2609.18930
  date: '2026-09-16'
  accessed_at: '2026-09-21'
---

## 概述

双足移动操作让机器人能够通过协调行走与操作，触及手臂名义工作空间之外的物体，但实现这一能力需要底层全身控制器在保持平衡的同时把任务级操作目标转化为手臂与腿部的协同运动。本文提出一个用强化学习训练的统一全身控制器，直接把 6-DoF 末端执行器目标映射为双足基座和机械臂的协调动作，无需显式的基座速度或落脚点指令即可自主协调伸展、姿态调整与迈步。训练中采用奖励门控策略来调节末端跟踪、行走与平衡之间的权衡，并用时间上下文估计器从观测历史中提取动力学相关信息，该估计器结合了窗口化 Transformer 编码、循环 GRU 记忆与辅助动力学预测。真机实验表明，同一控制器可支持 VR 遥操作、学习得到的扩散策略以及脚本轨迹三类指令下的伸展、姿态调整与迈步，为多种操作任务提供了统一的末端执行器接口。

## 核心内容

### 问题背景

双足移动操作的价值在于突破机械臂名义工作空间的限制：机器人可以通过协调行走与操作去接触更远处的物体。但这一能力依赖一个底层全身控制器，它必须把任务级的操作目标翻译成手臂与腿部的协同动作，同时维持平衡。传统做法通常需要显式的基座速度指令或落脚点指令，增加了任务层与底层控制之间的接口负担。

### 方法

本文提出一个用强化学习训练的统一全身控制器，其核心特点是直接以 6-DoF 末端执行器目标作为输入，输出双足基座与机械臂的协调动作。给定一个末端执行器目标，控制器能够自主协调伸展、姿态调整与迈步，不需要显式的基座速度或落脚点命令。

方法包含两个关键组件：

- **奖励门控策略（reward-gating strategy）**：在训练过程中调节末端执行器跟踪、行走与平衡三者之间的权衡。
- **时间上下文估计器（temporal context estimator）**：从观测历史中提取与动力学相关的信息，由三部分构成——窗口化 Transformer 编码、循环 GRU 记忆，以及辅助动力学预测。

### 实验设置

真机实验使用同一控制器，在三种不同来源的指令下进行测试：

- VR 遥操作指令；
- 学习得到的扩散策略（diffusion policy）；
- 脚本轨迹（scripted trajectories）。

### 关键结果

实验表明，同一个控制器在上述三类指令下均能支持伸展、姿态调整与迈步三类行为，从而为多样化的操作任务提供一个通用的末端执行器接口。

### 结论

该工作说明，仅以末端执行器目标为接口的统一全身控制器，可以在双足移动操作平台上同时完成平衡维持、行走与操作协调，并兼容遥操作、学习策略与脚本轨迹等多种上层指令来源。

## Overview

Bipedal loco-manipulation enables robots to interact with objects beyond the nominal workspace of their arms by coordinating locomotion and manipulation. Realizing this capability requires a low-level whole-body controller that translates task-level manipulation goals into coordinated arm and leg motions while maintaining balance. We present a unified whole-body controller trained with reinforcement learning that directly maps 6-DoF end-effector targets to coordinated actions for the bipedal base and robotic arm. Given only an end-effector target, the learned controller autonomously coordinates reaching, postural adaptation, and stepping without explicit base-velocity or footstep commands. A reward-gating strategy regulates the trade-offs among end-effector tracking, locomotion, and balance during training, while a temporal context estimator combines windowed Transformer encoding, recurrent GRU memory, and auxiliary dynamics prediction to extract dynamics-relevant information from observation history. Real-robot experiments demonstrate that the same controller supports reaching, postural adaptation, and stepping under commands from VR teleoperation, a learned diffusion policy, and scripted trajectories, providing a common end-effector interface for diverse manipulation tasks.

## 参考
- https://arxiv.org/abs/2609.18930
