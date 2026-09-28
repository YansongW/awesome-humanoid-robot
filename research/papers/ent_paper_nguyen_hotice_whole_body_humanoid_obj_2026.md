---
$id: ent_paper_nguyen_hotice_whole_body_humanoid_obj_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments'
  zh: 'HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments'
  ko: 'HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments'
summary:
  en: Object transportation is a fundamental capability for humanoid robots operating in real-world, human-centric environments,
    yet existing methods struggle when clutter constrains free space around both the robot and its carried payload. We present
    HOTICE, a whole-body humanoid learning framework for transporting objects through such cluttered environments. First,
    we introduce Humanoid-Object ...
  zh: HOTICE 是一个面向人形机器人的全身学习框架，用于在杂乱环境中搬运物体。作者来自 Toan Nguyen、Weiduo Yuan、Siheng Zhao、Yue Wang、Daniel Seita 团队，核心贡献包括 Humanoid-Object
    Decoupled Potential Fields、双智能体强化学习架构以及 specialist-to-generalist 蒸馏策略。该方法在 MuJoCo 仿真与真实 Unitree G1 人形机器人上验证，可搬运不同形状物体并泛化到未见过的杂乱场景。
  ko: Object transportation is a fundamental capability for humanoid robots operating in real-world, human-centric environments,
    yet existing methods struggle when clutter constrains free space around both the robot and its carried payload. We present
    HOTICE, a whole-body humanoid learning framework for transporting objects through such cluttered environments. First,
    we introduce Humanoid-Object ...
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
- object_transportation
- reinforcement_learning
- sim2real
- cluttered_environments
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-28'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-28). Bibliographic metadata from arXiv API (2609.25363);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.25363 HOTICE: Whole-Body Humanoid Object Transportation in Cluttered Environments'
  url: https://arxiv.org/abs/2609.25363
  date: '2026-09-21'
  accessed_at: '2026-09-28'
---

## 概述

在真实人类中心环境中，搬运物体是人形机器人的基础能力，但当机器人本体与所携带负载周围的可通行空间同时受到杂乱物限制时，现有方法往往难以应对。HOTICE 针对这一问题提出全身学习框架：一方面用 Humanoid-Object Decoupled Potential Fields 同时为机器人和被搬运物体编码避障引导，实现两者协调的障碍感知运动；另一方面针对全身 loco-manipulation 动作空间过大的问题，设计双智能体强化学习架构，将上下半身控制解耦，并通过共享状态观测与奖励保持全身协调。为让策略泛化到多样杂乱场景，作者进一步采用 specialist-to-generalist 蒸馏策略，将带特权信息的教师策略蒸馏为单一可部署的学生策略。实验在 MuJoCo 仿真和真实 Unitree G1 人形机器人上进行，结果表明 HOTICE 能可靠协调全身运动与物体感知避障，泛化到此前未见的杂乱环境，并在 sim2real 部署中取得良好表现。

## 核心内容

### 问题背景
物体搬运是人形机器人在真实、以人为中心的环境中运行的基础能力。然而，当杂乱物同时限制机器人本体与其所携带负载周围的自由空间时，已有方法表现不佳。HOTICE 旨在解决这类杂乱环境下的全身人形物体搬运问题。

### 方法
- **Humanoid-Object Decoupled Potential Fields**：联合编码机器人本体与所搬运物体的避障引导，使两者获得协调且具备障碍感知的运动。
- **双智能体强化学习架构**：针对全身 loco-manipulation 固有的巨大动作空间，将上半身与下半身控制解耦，同时通过共享状态观测与奖励维持全身协调。
- **specialist-to-generalist 蒸馏策略**：为训练可泛化到多样杂乱场景的策略，将带特权信息的教师策略蒸馏为单一可部署的学生策略。

### 实验设置
- 在 MuJoCo 仿真环境中进行评估。
- 在真实 Unitree G1 人形机器人上进行验证。
- 测试对象为不同形状的物体，场景为杂乱环境。

### 关键结果
- HOTICE 在多种杂乱场景下实现了有效且稳健的物体搬运。
- 能够可靠协调全身运动与物体感知避障。
- 可有效泛化到此前未见的杂乱环境。
- 在 sim2real 部署中取得良好性能。

### 结论
HOTICE 通过解耦势场引导、双智能体强化学习与教师到学生蒸馏的组合，为人形机器人在杂乱环境中搬运物体提供了可行方案，并在仿真与真实硬件上验证了其有效性与泛化能力。

## Overview

Object transportation is a fundamental capability for humanoid robots operating in real-world, human-centric environments, yet existing methods struggle when clutter constrains free space around both the robot and its carried payload. We present HOTICE, a whole-body humanoid learning framework for transporting objects through such cluttered environments. First, we introduce Humanoid-Object Decoupled Potential Fields, which jointly encode collision-avoidance guidance for the robot and the carried object, enabling coordinated, obstacle-aware motion for both. Second, to address the large action space inherent to whole-body loco-manipulation, we design a dual-agent reinforcement learning architecture that decouples upper- and lower-body control while preserving whole-body coordination via shared state observations and rewards. To train a policy that generalizes across diverse cluttered scenes, we further employ a specialist-to-generalist distillation strategy, in which privileged teacher policies are distilled into a single deployable student policy. We evaluate HOTICE in MuJoCo simulation and on a real Unitree G1 humanoid, demonstrating effective and robust object transportation across cluttered scenarios for objects of varying shapes. Our results show that HOTICE reliably coordinates whole-body motion and object-aware collision avoidance, generalizing effectively to previously unseen cluttered environments while achieving strong performance in sim2real deployment.

## 参考
- https://arxiv.org/abs/2609.25363
