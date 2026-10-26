---
$id: ent_paper_chen_memory_before_goal_role_of_pre_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation'
  zh: 'Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation'
  ko: 'Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation'
summary:
  en: 'Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave
    the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present
    WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts
    on its goal. SAM3 tracks the task ...'
  zh: 本文提出 WholeBodyMem，一种面向人形机器人全身视觉-语言-动作（VLA）策略的对象引导感知记忆模块，用于解决动态场景中任务线索随时间消失所导致的非马尔可夫问题。作者包括 Chenyuan Chen、Ran Ding、Lechen
    Zhang、Zewen He 与 Yoshihiko Nakamura。该方法借助 SAM3 跟踪任务对象，并由对象事件在自适应预算内因果地选取关键帧，使动作专家通过交叉注意力读取这些历史帧；同时作者构建了包含六项仿真与六项真实 Unitree
    G1 任务的人形记忆基准 HuMeGo，将基础策略成功率从仿真 29.1% 提升至 72.6%、真机 36.7% 提升至 88.3%。
  ko: 'Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave
    the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present
    WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts
    on its goal. SAM3 tracks the task ...'
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
- humanoid_loco_manipulation
- vision_language_action
- perceptual_memory
- object_tracking
- memory_benchmark
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-26'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-26). Bibliographic metadata from arXiv API (2610.31166);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.31166 Memory before Goal: Role of Pre-History Memory for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2610.31166
  date: '2026-10-22'
  accessed_at: '2026-10-26'
- id: src_002
  type: website
  title: Project page
  url: https://memory-before-goal.github.io
  accessed_at: '2026-10-26'
---

## 概述

动态场景中的人形机器人移动操作本质上是非马尔可夫的：对象变化或被遮挡会使线索消失，机器人在转身行走时目标也会离开视野，而现有的全身 VLA 策略只能感知当前时刻。为此，作者提出 WholeBodyMem，一种对象引导的感知记忆机制，在机器人执行目标动作之前保留此前观察到的对象事件历史。该方法使用 SAM3 跟踪任务对象，并由对象事件因果地在自适应预算内挑选关键帧，动作专家再通过交叉注意力将这些关键帧与编码外观、几何与时间的对象 token 一并读取。作者同时贡献了 HuMeGo 基准，涵盖六项仿真任务与六项基于 Unitree G1 的真实世界任务。实验表明，保留正确的帧比保留更多的帧更有效，WholeBodyMem 优于无记忆与均匀记忆基线，并显著提升基础策略在仿真、真机以及标准 SIMPLE 任务上的成功率。

## 核心内容

### 问题背景

人形机器人在动态场景中执行移动操作时面临非马尔可夫性：对象发生改变或被遮挡会使线索消失，机器人转身行走时目标也会离开视野。然而，现有的全身视觉-语言-动作（VLA）策略仅能观察当前时刻，缺乏对动作执行前对象事件历史的利用。

### 方法

- **WholeBodyMem**：一种对象引导的感知记忆模块，用于在机器人对目标采取行动之前保留此前观察到的对象事件前史。
- **对象跟踪**：使用 SAM3 跟踪任务对象。
- **关键帧选择**：由对象事件因果地在自适应预算内选取关键帧，强调"保留正确的帧"而非"保留更多的帧"。
- **记忆读取**：动作专家通过交叉注意力读取所选关键帧，并与编码外观、几何与时间的对象 token 一同处理。

### 实验设置

作者贡献了 **HuMeGo** 人形记忆基准，包含六项仿真任务与六项基于 Unitree G1 的真实世界任务，并额外在标准 SIMPLE 任务上进行评估。

### 关键结果

- 仿真环境：基础策略成功率由 29.1% 提升至 72.6%。
- 真实机器人：成功率由 36.7% 提升至 88.3%。
- 标准 SIMPLE 任务：成功率由 70.2% 提升至 86.9%。
- WholeBodyMem 在上述设置中均优于无记忆基线与均匀记忆基线。

### 结论

在非马尔可夫的动态移动操作场景中，对象事件驱动的选择性历史记忆能够有效弥补当前帧感知的不足，显著提升全身 VLA 策略在仿真与真实人形机器人上的任务成功率。

## Overview

Humanoid loco-manipulation in dynamic scenes is non-Markovian: cues vanish as objects change or are hidden, or leave the view as the robot turns and walks, yet whole-body vision-language-action (VLA) policies see only the present. We present WholeBodyMem, an object-guided perceptual memory that keeps the pre-history of object events seen before the robot acts on its goal. SAM3 tracks the task objects, and their events causally select key frames within an adaptive budget, which the action expert reads by cross-attention together with object tokens encoding appearance, geometry and time. We also contribute HuMeGo, a humanoid memory benchmark with six simulated and six real-world Unitree G1 tasks. Keeping the right frames rather than more frames, WholeBodyMem surpasses memoryless and uniform-memory baselines, raising its base policy's success from 29.1% to 72.6% in simulation and from 36.7% to 88.3% on the real robot, while also improving the standard SIMPLE tasks (70.2% to 86.9%).

## 参考
- https://arxiv.org/abs/2610.31166
- https://memory-before-goal.github.io
