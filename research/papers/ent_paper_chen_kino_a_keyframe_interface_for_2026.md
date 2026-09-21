---
$id: ent_paper_chen_kino_a_keyframe_interface_for_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation'
  zh: 'KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation'
  ko: 'KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation'
summary:
  en: Humanoid loco-manipulation requires robots to interpret task instructions and scene semantics while executing coordinated
    whole-body motions. We propose a hierarchical framework that uses motion keyframes as an intermediate representation between
    Vision-Language Model (VLM) planning and Reinforcement Learning (RL) control. Each keyframe specifies a target whole-body
    robot pose and, when ...
  zh: KINO 是一个面向人形机器人 loco-manipulation 的分层框架，由 Sitong Chen、Fatemeh Zargarbashi、Jin Cheng、Tianxu An 与 Stelian Coros 提出，以运动关键帧作为
    VLM 规划与 RL 控制之间的中间表示。VLM 根据语言指令、场景观测与执行反馈，从预定义关键帧库中依次选取任务相关关键帧，再由关键帧条件的全身策略生成关节级动作。作者提出基于显著性的关键帧采样策略，使稀疏 VLM 关键帧下的端到端任务成功率从
    44% 提升至 92%。
  ko: Humanoid loco-manipulation requires robots to interpret task instructions and scene semantics while executing coordinated
    whole-body motions. We propose a hierarchical framework that uses motion keyframes as an intermediate representation between
    Vision-Language Model (VLM) planning and Reinforcement Learning (RL) control. Each keyframe specifies a target whole-body
    robot pose and, when ...
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
- vlm_planning
- whole_body_control
- keyframe_representation
- reinforcement_learning
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-09-21'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-09-21). Bibliographic metadata from arXiv API (2609.18869);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2609.18869 KINO: A Keyframe Interface for VLM Planning and Whole-Body Control in Humanoid Loco-Manipulation'
  url: https://arxiv.org/abs/2609.18869
  date: '2026-09-16'
  accessed_at: '2026-09-21'
---

## 概述

人形机器人执行 loco-manipulation 任务时，既要理解任务指令与场景语义，又要完成协调的全身运动。KINO 采用分层结构，把运动关键帧当作 VLM 规划与 RL 控制之间的中间表示：每个关键帧描述一个目标全身位姿，并在适用时描述一个物体位姿。给定语言指令、场景观测和执行反馈，VLM 从预定义关键帧库中挑选后续的任务相关关键帧，这些关键帧会被重定向到当前场景以适配物体的位姿与尺寸。随后，一个以关键帧为条件的全身策略生成关节级动作以达成这些目标。为训练底层策略，作者引入基于显著性的关键帧采样策略，在使用稀疏 VLM 关键帧时把端到端任务成功率从 44% 提高到 92%。该框架在仿真与 Unitree G1 人形机器人上针对物体拾取、搬运和放置任务进行了评估，系统能完成单手与双手操作，并可泛化到训练参考数据之外的放置位置。

## 核心内容

### 问题背景
人形机器人 loco-manipulation 要求机器人同时理解任务指令与场景语义，并执行协调的全身运动。这一需求使得高层任务规划与底层全身控制之间的衔接成为关键问题。

### 方法
KINO 提出一个分层框架，以运动关键帧作为 Vision-Language Model (VLM) 规划与 Reinforcement Learning (RL) 控制之间的中间表示。

- **关键帧表示**：每个关键帧指定一个目标全身机器人位姿，并在适用时指定一个物体位姿。
- **VLM 规划**：给定语言指令、场景观测与执行反馈，VLM 从预定义的关键帧库中依次选择任务相关的关键帧。
- **关键帧重定向**：被选中的关键帧会重定向到当前场景，以考虑物体的位姿与尺寸。
- **全身控制**：一个以关键帧为条件的全身策略生成关节级动作，以达成这些目标。
- **训练策略**：作者提出基于显著性的关键帧采样策略用于底层策略训练。

### 实验设置
框架在仿真环境以及 Unitree G1 人形机器人上进行评估，任务涵盖物体拾取、搬运与放置。

### 关键结果
- 基于显著性的关键帧采样策略在使用稀疏 VLM 关键帧时，将端到端任务成功率从 44% 提升至 92%。
- 系统成功完成单手与双手操作。
- 系统可泛化到训练参考数据之外的放置位置。

### 结论
KINO 通过关键帧这一中间表示，将 VLM 规划与 RL 全身控制有效衔接，并在仿真与真实人形机器人上验证了其在拾取、搬运、放置任务中的有效性，同时展现出对未见放置位置的泛化能力。

## Overview

Humanoid loco-manipulation requires robots to interpret task instructions and scene semantics while executing coordinated whole-body motions. We propose a hierarchical framework that uses motion keyframes as an intermediate representation between Vision-Language Model (VLM) planning and Reinforcement Learning (RL) control. Each keyframe specifies a target whole-body robot pose and, when applicable, an object pose. Given a language instruction, scene observations, and execution feedback, the VLM selects successive task-relevant keyframes from a predefined library. The selected keyframes are retargeted to the current scene to account for object poses and dimensions. A keyframe-conditioned whole-body policy then generates joint-level actions to reach these goals. We introduce a saliency-based keyframe sampling strategy for low-level policy training that improves end-to-end task success rate from 44% to 92% when using sparse VLM keyframes. We evaluate our framework on object pickup, transport, and placement tasks in simulation and on a Unitree G1 humanoid. The system successfully performs both one- and two-handed manipulation and generalises to placement locations beyond the training reference data.

## 参考
- https://arxiv.org/abs/2609.18869
