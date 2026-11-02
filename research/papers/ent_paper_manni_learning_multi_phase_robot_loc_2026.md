---
$id: ent_paper_manni_learning_multi_phase_robot_loc_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization
  zh: Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization
  ko: Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization
summary:
  en: Complex whole-body loco-manipulation requires executing diverse maneuvers, such as crouching, grasping, and locomotion,
    within a single long-horizon task. While performing simple pick-and-place behaviors is well-established, scaling to complex,
    long-horizon tasks remains difficult. Currently, this challenge is addressed by relying on human motion data and correspondingly
    humanoid platforms, which ...
  zh: 该工作提出一种基于阶段条件策略优化的方法，用于训练单一策略完成长时程多阶段机器人移动操作任务。作者将 proximal policy optimization (PPO) 扩展为使用阶段条件 critic、阶段门控奖励函数与多阶段重置课程，并结合解耦的分层控制架构以适配不同硬件。方法在
    Unitree G1 与配备机械臂的 Boston Dynamics Spot 上完成了多阶段移动操作技能验证，并通过消融实验检验了设计选择。
  ko: Complex whole-body loco-manipulation requires executing diverse maneuvers, such as crouching, grasping, and locomotion,
    within a single long-horizon task. While performing simple pick-and-place behaviors is well-established, scaling to complex,
    long-horizon tasks remains difficult. Currently, this challenge is addressed by relying on human motion data and correspondingly
    humanoid platforms, which ...
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
- phase_conditioned_policy
- proximal_policy_optimization
- hierarchical_control
- humanoid_robotics
- curriculum_learning
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-02'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-02). Bibliographic metadata from arXiv API (2610.36270);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.36270 Learning Multi-Phase Robot Loco-Manipulation via Phase-Conditioned Policy Optimization
  url: https://arxiv.org/abs/2610.36270
  date: '2026-10-26'
  accessed_at: '2026-11-02'
---

## 概述

复杂全身移动操作要求在单一长时程任务中完成下蹲、抓取与移动等多种动作，而现有方法多依赖人类运动数据与人形平台，限制了平台独立性并带来大量数据处理开销。该研究改为扩展 proximal policy optimization (PPO)，利用任务先验结构塑造行为，训练可跨多种机器人硬件执行多阶段任务的单一策略。其核心设计包括阶段条件 critic、阶段门控奖励函数与多阶段重置课程，以引导探索；同时采用解耦的分层控制架构，将底层平衡动力学与高层阶段执行分离。作者在 Unitree G1 与配备机械臂的 Boston Dynamics Spot 硬件上展示了多阶段移动操作技能，并通过消融实验验证了各项设计选择。该方法仅通过环境交互即可获得复杂移动操作行为，并将高层任务结构直接融入策略学习。

## 核心内容

### 问题背景
复杂全身移动操作需要在单个长时程任务中执行下蹲、抓取、移动等多种机动动作。简单的抓取放置行为已较为成熟，但扩展到复杂长时程任务仍然困难。当前做法通常依赖人类运动数据及相应的人形平台，这限制了平台独立性，并引入大量数据处理开销。

### 方法
- 将 proximal policy optimization (PPO) 扩展，用于在多种机器人硬件上为多阶段任务训练单一策略，并利用先验任务结构塑造行为。
- 对 PPO 的具体改造包括：阶段条件 critic、阶段门控奖励函数，以及多阶段重置课程，用以引导探索。
- 为支持不同硬件，采用解耦的分层控制架构，将底层平衡动力学与高层阶段执行分离。

### 实验设置
- 在硬件上验证：Unitree G1，以及配备机械臂的 Boston Dynamics Spot。
- 通过消融实验验证设计选择。

### 关键结果
- 在两个硬件平台上展示了多阶段移动操作技能。
- 消融实验支持了所提设计选择的有效性。

### 结论
该方法仅通过环境交互即可习得复杂移动操作行为，并将高层任务结构直接融入策略学习，从而避免依赖人类运动数据，提升平台独立性。

## Overview

Complex whole-body loco-manipulation requires executing diverse maneuvers, such as crouching, grasping, and locomotion, within a single long-horizon task. While performing simple pick-and-place behaviors is well-established, scaling to complex, long-horizon tasks remains difficult. Currently, this challenge is addressed by relying on human motion data and correspondingly humanoid platforms, which limits platform independence and introduces substantial data processing overhead. Instead, we extend proximal policy optimization (PPO) to train a single policy for multi-phase tasks across diverse robotic hardware, leveraging prior task structure to shape behavior. Our method adapts PPO using a phase-conditioned critic, phase-gated reward functions, and a multi-phase reset curriculum to guide exploration. To support varied hardware, we employ a decoupled hierarchical control architecture that separates lower-level balancing dynamics from high-level phase execution. We demonstrate multi-stage loco-manipulation skills on hardware on both the Unitree G1 and a Boston Dynamics Spot equipped with a manipulator arm, and validate our design choices through ablations. Our approach enables the acquisition of complex loco-manipulation behaviors purely through environment interaction while directly incorporating high-level task structure into policy learning.

## 参考
- https://arxiv.org/abs/2610.36270
