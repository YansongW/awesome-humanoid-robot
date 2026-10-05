---
$id: ent_paper_luo_ceer2_directional_and_tunable_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CEER2: Directional and Tunable End-Effector and Root Compliance for Humanoid Loco-Manipulation'
  zh: 'CEER2: Directional and Tunable End-Effector and Root Compliance for Humanoid Loco-Manipulation'
  ko: 'CEER2: Directional and Tunable End-Effector and Root Compliance for Humanoid Loco-Manipulation'
summary:
  en: Humanoids are increasingly capable of tracking complex whole-body motions, but physical interaction introduces a different
    challenge. When a robot makes contact with a person or the environment, it needs to respond to external forces while preserving
    the motion needed for the task. This response can vary across directions in the end-effectors and on the body. For example,
    an end effector may need ...
  zh: 该工作提出了面向人形机器人移动操作（loco-manipulation）的柔顺框架 CEER2，将方向性且可调的末端执行器（EE）柔顺与可选的整体根部柔顺相结合，用于外力抑制或力跟随。作者为 Xinyuan Luo、Chunyuan
    Yang、Boyuan Chen、Xianyi Cheng。方法上采用分层强化学习控制器，通过高层 EE 与根部指令调制固定的全身跟踪策略，并从本体感知历史中估计交互力。
  ko: Humanoids are increasingly capable of tracking complex whole-body motions, but physical interaction introduces a different
    challenge. When a robot makes contact with a person or the environment, it needs to respond to external forces while preserving
    the motion needed for the task. This response can vary across directions in the end-effectors and on the body. For example,
    an end effector may need ...
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
- compliance_control
- variable_stiffness
- hierarchical_reinforcement_learning
- whole_body_control
- force_estimation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-05'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-05). Bibliographic metadata from arXiv API (2609.38709);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.38709 CEER2: Directional and Tunable End-Effector and Root Compliance for Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2609.38709
  date: '2026-09-30'
  accessed_at: '2026-10-05'
---

## 概述

人形机器人已能跟踪复杂的全身运动，但与人和环境发生物理接触时，机器人需要在响应外力的同时保持任务所需的运动，且这种响应在不同方向上可能不同。为此，作者提出一种用于人形移动操作的柔顺框架，把方向性、可调的末端执行器柔顺与可选择的根部柔顺结合起来，后者可用于外力抑制或力跟随。实现上采用分层强化学习控制器，用高层的 EE 与根部指令调制一个固定的全身跟踪策略，交互力则由本体感知历史估计得到。在仿真与真机实验中，该框架展示了方向刚度控制、在线刚度调整、不同的根部柔顺行为、柔顺操作以及协作搬运等能力。

## 核心内容

### 问题背景
人形机器人跟踪复杂全身运动的能力不断提升，但物理交互带来了另一类挑战：当机器人与人体或环境接触时，既要对外部力作出响应，又要保留完成任务所需的运动。这种响应在不同方向上并不一致——例如末端执行器可能需要在某一方向上顺应接触力，同时在另一方向上保持运动精度；机器人本体则可能需要抵抗外力，也可能需要随外力一起运动。

### 方法
- 提出一个面向人形移动操作的柔顺框架，将**方向性且可调的末端执行器（EE）柔顺**与**可选择的根部柔顺**结合，根部柔顺可用于外力抑制（force rejection）或力跟随（force following）。
- 采用**分层强化学习控制器**：由高层下达 EE 与根部指令，调制一个**固定的全身跟踪策略**。
- 交互力通过**本体感知历史**进行估计。

### 实验与结果
在仿真与真机实验中，作者在一台人形机器人上展示了以下能力：
- 方向刚度控制（directional stiffness control）
- 在线刚度调整（online stiffness adjustment）
- 不同的根部柔顺行为（distinct root compliance）
- 柔顺操作（compliant manipulation）
- 协作搬运（collaborative carrying）

### 结论
该框架使人形机器人在移动操作中能够按方向、按需调节末端执行器与根部的柔顺特性，从而在接触交互中兼顾外力响应与任务运动保持。

## Overview

Humanoids are increasingly capable of tracking complex whole-body motions, but physical interaction introduces a different challenge. When a robot makes contact with a person or the environment, it needs to respond to external forces while preserving the motion needed for the task. This response can vary across directions in the end-effectors and on the body. For example, an end effector may need to accommodate contact force in one direction while maintaining motion accuracy in another, while the robot body may resist an external force or move with it. We present a compliance framework for humanoid loco-manipulation that combines directional and tunable end-effector (EE) compliance with selectable root compliance for external force rejection or force following. A hierarchical reinforcement learning controller modulates a fixed whole-body tracking policy through high-level EE and root commands, while interaction forces are estimated from proprioceptive history. Our simulation and real-world experiments on a humanoid demonstrate directional stiffness control, online stiffness adjustment, distinct root compliance, compliant manipulation, and collaborative carrying.

## 参考
- https://arxiv.org/abs/2609.38709
