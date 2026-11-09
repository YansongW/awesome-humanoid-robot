---
$id: ent_paper_valenzuela_crisp_constraint_resolved_inte_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation'
  zh: 'CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation'
  ko: 'CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation'
summary:
  en: This paper presents a layered control framework that recasts high-dimensional system dynamics as a composition of dynamically
    interconnected subsystems, with dynamic dual-arm manipulation on the humanoid serving as a representative application.
    The humanoid is decomposed into a single rigid body (SRB) representing the torso and floating-base dynamic models representing
    the articulated arms and ...
  zh: 本文提出一种分层控制框架 CRISP，将高维人形机器人动力学重构为多个动态互联子系统的组合，并以动态双臂协同操作作为代表性应用场景。作者将人形机器人分解为表示躯干的单刚体（SRB）模型与表示手臂和下肢的浮动基动力学模型，把肩部刚性连接与末端执行器间闭链约束统一表示为完整约束，由
    Lagrange 乘子参数化交互力旋量。高层 NMPC 联合优化子系统状态轨迹、手臂力矩、地面反作用力（GRFs）与交互力旋量，并在 G1 人形机器人上通过数值仿真与硬件实验验证了在线运行的可行性。
  ko: This paper presents a layered control framework that recasts high-dimensional system dynamics as a composition of dynamically
    interconnected subsystems, with dynamic dual-arm manipulation on the humanoid serving as a representative application.
    The humanoid is decomposed into a single rigid body (SRB) representing the torso and floating-base dynamic models representing
    the articulated arms and ...
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
- humanoid_robot
- dual_arm_manipulation
- whole_body_control
- model_predictive_control
- holonomic_constraints
- interaction_wrench
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-11-09'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-11-09). Bibliographic metadata from arXiv API (2611.07268);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2611.07268 CRISP: Constraint-Resolved Interactions between Subsystems for Predictive Whole-Body Cooperation'
  url: https://arxiv.org/abs/2611.07268
  date: '2026-11-05'
  accessed_at: '2026-11-09'
---

## 概述

该工作面向人形机器人双臂协同操作中的高维动力学与约束耦合难题，提出分层控制框架 CRISP，把整体系统拆解为躯干单刚体与手臂、下肢浮动基模型等动态互联子系统。子系统间的刚性连接与协同操作时末端执行器形成的闭链被建模为完整约束，其对应的 Lagrange 乘子直接参数化肩部与末端之间的交互力旋量。高层非线性模型预测控制（NMPC）同时优化各子系统状态轨迹、手臂力矩、地面反作用力与交互力旋量，从而在保持子系统动态耦合的前提下实现在线力旋量设计与优化。优化得到的手臂力矩直接用于双臂协同操作，而给定的地面反作用力则映射为下肢关节力矩以实现全身协调。作者在 G1 人形机器人上通过数值仿真与硬件实验验证了框架，结果显示交互力旋量与仿真接触测量一致、双臂协同轨迹跟踪良好，且 NMPC 在线运行下全身协调稳定。

## 核心内容

### 问题背景
人形机器人执行动态双臂协同操作时，系统维度高、子系统间存在强动态耦合，肩部刚性连接与末端执行器闭链约束使整体动力学难以直接用于实时优化控制。本文将该高维动力学重新表述为若干动态互联子系统的组合，以在保留耦合关系的同时降低控制问题的组织复杂度。

### 方法
- **系统分解**：将人形机器人分解为表示躯干的单刚体（SRB）模型，以及表示手臂与下肢的浮动基动力学模型。
- **约束建模**：手臂与躯干之间的刚性连接、协同操作中末端执行器之间形成的闭链运动链，均表示为完整约束（holonomic constraints）。
- **交互力参数化**：由相应的 Lagrange 乘子参数化在肩部传递及末端执行器之间传递的交互力旋量。
- **高层 NMPC**：非线性模型预测控制联合优化子系统状态轨迹、手臂力矩、地面反作用力（GRFs）与交互力旋量，支持在线进行力旋量设计与优化，同时保持各独立建模子系统之间的动态耦合。
- **控制分配**：优化后的手臂力矩直接施加于双臂协同操作；给定的 GRFs 被映射为下肢关节力矩，实现全身协调。

### 实验设置
验证通过数值仿真与 G1 人形机器人硬件实验完成，NMPC 以在线方式运行。

### 关键结果
- 优化得到的交互力旋量与仿真接触测量结果一致。
- 实现双臂协同轨迹跟踪。
- 在执行在线 NMPC 的同时实现稳定的全身协调。

### 结论
所提出的分层框架能够在保持子系统动态耦合的前提下在线联合优化交互力旋量与全身控制量，并在 G1 人形机器人上验证了双臂协同操作与全身协调的有效性。

## Overview

This paper presents a layered control framework that recasts high-dimensional system dynamics as a composition of dynamically interconnected subsystems, with dynamic dual-arm manipulation on the humanoid serving as a representative application. The humanoid is decomposed into a single rigid body (SRB) representing the torso and floating-base dynamic models representing the articulated arms and lower-body. The rigid connections between arm and torso and the closed kinematic chain formed between the end-effectors during cooperative manipulation are represented as holonomic constraints. The corresponding Lagrange multipliers parametrize the interaction wrenches transmitted at the shoulders and between the end-effectors. The high-level nonlinear model predictive control (NMPC) jointly optimizes the subsystem state trajectories, arm torques, ground reaction forces (GRFs), and interaction wrenches, enabling online wrench design and optimization while preserving the dynamic coupling among the independently modeled subsystems. The optimized arm torques are applied directly for cooperative dual-arm manipulation, whereas the prescribed GRFs are mapped to lower-body joint torque for whole-body coordination. We validate the proposed framework through numerical simulations and hardware experiments on a G1 humanoid robot. The results demonstrate optimal interaction wrenches consistent with simulated contact measurement, cooperative dual-arm trajectory tracking, and stable whole-body coordination while executing the NMPC in online manner.

## 参考
- https://arxiv.org/abs/2611.07268
