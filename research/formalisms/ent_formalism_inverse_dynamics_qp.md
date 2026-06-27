---
$id: ent_formalism_inverse_dynamics_qp
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Inverse-Dynamics QP Formulation
  zh: 逆动力学二次规划形式化
  ko: 역동역학 QP 공식화
summary:
  en: A quadratic-program formulation that computes generalized accelerations, contact forces, and joint torques by minimizing task-tracking errors subject to floating-base dynamics and physical constraints.
  zh: 一种二次规划形式化，通过最小化任务跟踪误差并受浮动基动力学和物理约束，计算广义加速度、接触力和关节力矩。
  ko: 부유 기반 동역학과 물리적 제약 조건 하에서 작업 추종 오차를 최소화하여 일반화 가속도, 접촉력, 관절 토크를 계산하는 이차 계획법 공식화이다.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- intelligence
- knowledge
tags:
- inverse_dynamics
- quadratic_programming
- qp_formulation
- floating_base
- humanoid_control
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard formulation in WBC literature.
sources:
- id: src_001
  type: paper
  title: 'Hierarchical QP whole-body control: from theory to practice'
  url: https://arxiv.org/abs/1910.13329
  date: '2019'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_equation_weighted_task_error_objective
  relationship: includes
  description:
    en: The QP objective includes a weighted sum of task errors.
    zh: QP 目标包含任务误差的加权和。
    ko: QP 목적 함수는 작업 오차의 가중합을 포함한다.
- id: ent_principle_newton_euler_equations
  relationship: derived_from
  description:
    en: The equality constraints encode the Newton-Euler floating-base dynamics.
    zh: 等式约束编码了牛顿-欧拉浮动基动力学。
    ko: 등식 제약은 뉴턴-오일러 부유 기반 동역학을 인코딩한다.
---

## 抽象

> **生活实例**：如果你想让机器人从蹲姿站起来，你得知道每个关节该怎么转、脚底需要多大力、身体重心往哪移。逆动力学 QP 就是把这些“想知道的”放进一个统一的数学公式里：目标函数让动作尽量接近想要的轨迹，约束条件则保证物理定律不被违背。
>
> **自然语言逻辑**：把机器人所有关节加速度、接触力和关节力矩作为决策变量；写出任务跟踪误差的目标函数；再把浮动基动力学、力矩限制、关节限制写成等式/不等式约束；最后交给 QP 求解器。

## Overview

The inverse-dynamics QP formulation casts whole-body control as an optimization problem. The decision variables typically include generalized accelerations `q̈`, contact forces `λ`, and joint torques `τ`. The objective penalizes deviations from desired task accelerations, while equality constraints enforce the floating-base equations of motion and inequality constraints encode torque limits, joint limits, and friction cones.

## Key Characteristics

- Decision variables combine motion, force, and torque.
- Objective is usually a weighted least-squares task error.
- Constraints include dynamics, limits, and contact models.
- Can be solved by active-set or interior-point QP solvers.

## Relevance to Humanoid Robotics

This formulation is the mathematical core of many state-of-the-art humanoid controllers. It lets designers specify high-level tasks (e.g., keep the CoM over the support polygon) and automatically compute the low-level torques that realize them.
