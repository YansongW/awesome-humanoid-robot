---
$id: ent_paper_zhang_humble_human_motion_driven_beh_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion'
  zh: 'HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion'
  ko: 'HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion'
summary:
  en: Despite recent advances in humanoid locomotion, controllers optimized for command tracking and robustness tend to produce
    mechanical gaits, whereas controllers tied to human motion data often fail to generalize to commands outside the data
    distribution. This work introduces a learning framework that balances these competing objectives to synthesize real-time
    steerable, robust, and biomimetic ...
  zh: HuMBLE 是一个由多机构团队提出的学习框架，能够从人类运动数据中合成实时可操控、鲁棒且仿生的运动策略，兼顾指令跟踪与人类步态风格。该方法先通过教师-学生蒸馏学习自然运动先验策略，再用多任务强化学习微调以扩展指令覆盖范围与鲁棒性。框架在
    Boston Dynamics Atlas R1、Atlas D1 与 Unitree G1 三款人形机器人上完成验证。
  ko: Despite recent advances in humanoid locomotion, controllers optimized for command tracking and robustness tend to produce
    mechanical gaits, whereas controllers tied to human motion data often fail to generalize to commands outside the data
    distribution. This work introduces a learning framework that balances these competing objectives to synthesize real-time
    steerable, robust, and biomimetic ...
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
- motion_imitation
- reinforcement_learning
- teacher_student_distillation
- whole_body_control
- sim_to_real
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.10489);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.10489 HuMBLE: Human Motion-Driven Behavior Learning for Embodied Locomotion'
  url: https://arxiv.org/abs/2610.10489
  date: '2026-10-07'
  accessed_at: '2026-10-12'
---

## 概述

针对人形机器人运动控制中"机械步态"与"难以泛化到数据分布外指令"这两类相互竞争的目标，HuMBLE 提出了一种平衡二者的学习框架。作者使用自建的运动数据集（覆盖多种速度与方向），先以强化学习训练一个全身参考条件策略，再将其蒸馏为仅依赖本体感知与平面躯干速度操控指令的轻量先验策略。随后通过多任务强化学习对先验策略进行微调，其中一个目标条件任务跟踪任意指令，另一个参考引导任务以人类数据作为显式风格正则项，从而在扩展指令覆盖与鲁棒性的同时保留人类步态特征。该框架在 Boston Dynamics Atlas R1、Atlas D1 和 Unitree G1 上验证，并在室内外用户直接操控及分层控制栈的运动层集成等真实场景中展现出鲁棒性能。

## 核心内容

### 问题背景
人形机器人运动控制存在两类倾向：一类控制器针对指令跟踪与鲁棒性优化，往往产生机械化的步态；另一类控制器绑定人类运动数据，却难以泛化到数据分布之外的指令。HuMBLE 的目标是同时兼顾这两方面，从人类数据中合成实时可操控、鲁棒且仿生的运动策略。

### 方法
- **数据**：使用团队自建的运动数据集，覆盖多种速度与方向。
- **自然运动先验学习**：采用教师-学生蒸馏流程。首先用强化学习（RL）训练一个全身参考条件策略作为教师；随后将其蒸馏为一个轻量先验策略，该学生策略仅以本体感知和平面躯干速度操控指令为条件。
- **多任务微调**：对先验策略进行多任务 RL 微调，以扩展指令覆盖范围与鲁棒性，使其超越原始数据分布。微调包含两个任务：一个目标条件任务用于跟踪任意指令；一个参考引导任务用于跟踪人类数据，充当显式的风格正则项。

### 实验设置
- **验证平台**：三款人形机器人——Boston Dynamics Atlas R1、Atlas D1 与 Unitree G1。
- **真实场景**：包括室内与室外环境下的用户直接操控运动，以及作为分层控制栈中运动层的集成。
- **对比与消融**：与不使用人类数据训练的 Tabula Rasa RL 策略进行基准对比，并开展消融研究。

### 关键结果
- 在多种真实场景中表现出鲁棒性能，涵盖室内外用户直接操控以及分层控制栈中的运动层集成。
- 与 Tabula Rasa RL 策略的基准对比及消融研究确认：该框架产出的策略轻量且可部署，能够仅凭一个操控指令重建协调的全身行为。
- 该策略在保持鲁棒性与完全可操控性的同时，保留了人类步态特征。

### 结论
HuMBLE 通过"教师-学生蒸馏 + 多任务 RL 微调"的组合，在指令跟踪、鲁棒性与仿生步态之间取得平衡，得到轻量、可部署且完全可操控的人形运动策略。

## Overview

Despite recent advances in humanoid locomotion, controllers optimized for command tracking and robustness tend to produce mechanical gaits, whereas controllers tied to human motion data often fail to generalize to commands outside the data distribution. This work introduces a learning framework that balances these competing objectives to synthesize real-time steerable, robust, and biomimetic locomotion policies from human data. Using an in-house curated locomotion dataset covering diverse speeds and directions, we first learn a natural locomotion prior policy through a teacher-student distillation process. Specifically, we train a full-body reference-conditioned policy with Reinforcement Learning (RL), then distill it into a lightweight prior policy conditioned solely on proprioception and a planar torso-velocity steering command. Next, we fine-tune the prior policy with multi-task RL to expand command coverage and robustness beyond the data distribution, pairing a goal-conditioned task that tracks arbitrary commands with a reference-guided task that tracks the human data as an explicit style regularizer. We validate our framework on three humanoid robots: the Boston Dynamics Atlas R1, Atlas D1, and Unitree G1. Experimental results demonstrate robust performance across real-world scenarios, including direct user-controlled locomotion in indoor and outdoor environments, and integration as the locomotion layer within hierarchical control stacks. Benchmarks against Tabula Rasa RL policies trained without human data and ablation studies confirm that our framework yields a lightweight, deployable policy that reconstructs coordinated whole-body behavior from a steering command, retaining the human gait characteristics while remaining robust and fully steerable.

## 参考
- https://arxiv.org/abs/2610.10489
