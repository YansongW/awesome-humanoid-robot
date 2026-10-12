---
$id: ent_paper_dang_hulk_learning_whole_body_force_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids'
  zh: 'HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids'
  ko: 'HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids'
summary:
  en: Humanoid loco-manipulation of large, heavy objects demands forceful interaction across the entire body. However, such
    payloads shift a humanoid's center of mass and impose sustained loads across the upper body, challenging balance and command
    tracking. We present HULK, a whole-body control framework for forceful loco-manipulation. Using model predictive control
    (MPC) to guide reinforcement ...
  zh: HULK 是一个面向人形机器人全身强力 loco-manipulation 的控制框架，由 An Dang、Arturo Flores Alvarez、Yu-Ming Chen、Conor Mc Gartoll、Helen Sun、Aaron
    Ames、Nima Fazeli、Manikantan Nambi 提出。该方法用 MPC 引导强化学习并引入负载动力学预测，训练出两个教师策略（腕部受力下的手臂运动跟踪、抱持大型物体时的行走），再通过 capture-point control
    barrier function 增强平衡，最终蒸馏为单一策略。在仿真与 Unitree G1 上评估，带 barrier function 的教师在每臂 10 kg 负载下取得最低的前向与侧向速度跟踪误差，并将 DCM 偏移幅度较仅用
    MPC 引导强化学习降低 35.7%，腕力教师可承受最高 130 N 的躯干推力扰动。
  ko: Humanoid loco-manipulation of large, heavy objects demands forceful interaction across the entire body. However, such
    payloads shift a humanoid's center of mass and impose sustained loads across the upper body, challenging balance and command
    tracking. We present HULK, a whole-body control framework for forceful loco-manipulation. Using model predictive control
    (MPC) to guide reinforcement ...
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
- whole_body_control
- model_predictive_control
- reinforcement_learning
- control_barrier_function
- unitree_g1
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-12'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-12). Bibliographic metadata from arXiv API (2610.08970);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2610.08970 HULK: Learning Whole-Body Forceful Loco-Manipulation for Humanoids'
  url: https://arxiv.org/abs/2610.08970
  date: '2026-10-06'
  accessed_at: '2026-10-12'
---

## 概述

HULK 针对人形机器人搬运大型重物时全身需强力交互的问题：负载会改变质心并给上半身带来持续载荷，从而威胁平衡与指令跟踪。作者采用 model predictive control（MPC）结合负载动力学预测来引导强化学习，训练两个教师策略，分别负责腕部受力下的手臂运动跟踪，以及将大型物体贴身后行走。训练中引入 capture-point control barrier function 增强腕力教师的负载平衡能力，并将两个教师蒸馏为单一策略。评估覆盖仿真与 Unitree G1 实机，在仿真中带 barrier function 的教师在每臂 10 kg 负载下速度跟踪误差最低，DCM 偏移幅度较仅用 MPC 引导强化学习降低 35.7%，腕力教师可抵抗最高 130 N 的躯干推力。

## 核心内容

### 问题背景
人形机器人搬运大型、沉重物体时，需要全身参与强力交互。此类负载会移动机器人的质心，并在上半身施加持续载荷，给平衡维持与指令跟踪带来挑战。

### 方法
- 提出 HULK，一个面向强力 loco-manipulation 的全身控制框架。
- 使用 model predictive control（MPC）引导强化学习，并利用负载动力学预测提供指导。
- 训练两个教师策略：
  - 一个在腕部受力条件下跟踪手臂运动；
  - 另一个在将大型物体贴靠身体的情况下行走。
- 在训练阶段，用 capture-point control barrier function 增强腕力教师，以改善负载下的平衡。
- 将两个教师蒸馏为单一策略。

### 实验设置
- 评估覆盖仿真环境与 Unitree G1 平台。

### 关键结果
- 在仿真中，带 barrier function 的教师在每臂 10 kg 负载下，于所评估的控制器中取得最低的前向与侧向速度跟踪误差。
- 相比仅使用 MPC 引导的强化学习，该教师将 aggregate divergent component of motion（DCM）偏移幅度降低 35.7%。
- 腕力教师能够承受最高 130 N 的躯干推力扰动。

### 结论
HULK 通过 MPC 引导强化学习、双教师训练与 capture-point control barrier function，实现了人形机器人在负载下的全身强力 loco-manipulation，并在仿真与 Unitree G1 上验证了速度跟踪、DCM 偏移抑制与抗推力扰动能力。

## Overview

Humanoid loco-manipulation of large, heavy objects demands forceful interaction across the entire body. However, such payloads shift a humanoid's center of mass and impose sustained loads across the upper body, challenging balance and command tracking. We present HULK, a whole-body control framework for forceful loco-manipulation. Using model predictive control (MPC) to guide reinforcement learning with predictions of the loaded dynamics, we train two teachers: one tracks arm motions under wrist forces, and the other locomotes while holding large objects against the body. A capture-point control barrier function augments the wrist-force teacher during training to improve balance under load. We distill both teachers into a single policy. Evaluation spans simulation and the Unitree G1. In simulation, the teacher with the barrier function achieves the lowest forward and lateral velocity tracking errors at 10 kg per arm among evaluated controllers and reduces aggregate divergent component of motion (DCM) excursion magnitude by 35.7% relative to MPC-guided reinforcement learning alone. Our wrist-force teacher withstands torso push disturbances of up to 130 N.

## 参考
- https://arxiv.org/abs/2610.08970
