---
$id: ent_operator_task_jacobian
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: operator
names:
  en: Task Jacobian
  zh: 任务 Jacobian
  ko: 작업 Jacobian
summary:
  en: The matrix that maps joint-space velocities and accelerations to the velocity/acceleration of a task coordinate in operational space.
  zh: 将关节空间速度和加速度映射到操作空间任务坐标速度/加速度的矩阵。
  ko: 관절 공간 속도와 가속도를 작업 공간의 작업 좌표 속도/가속도로 매핑하는 행렬이다.
domains:
- 07_ai_models_algorithms
- 00_foundations
layers:
- intelligence
- foundations
functional_roles:
- knowledge
tags:
- jacobian
- task_space
- differential_kinematics
- linear_algebra
- humanoid_control
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard linear-algebra operator in robotics.
sources:
- id: src_001
  type: paper
  title: 'Robotics, Vision and Control'
  url: https://petercorke.com/rvc/home/
  date: '2017'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_foundation_linear_algebra
  relationship: has_prerequisite
  description:
    en: The Jacobian is built from partial derivatives, a core linear-algebra concept.
    zh: Jacobian 由偏导数构成，是线性代数的核心概念。
    ko: Jacobian은 편미분으로 구성되며, 선형대수학의 핵심 개념이다.
---

## 抽象

> **生活实例**：想象你有一根长杆，末端系着一个小球。你想让小球水平移动，但小球的位置取决于你手握杆的角度和杆的长度。Jacobian 就是告诉你“手怎么动，小球就怎么动”的换算表。
>
> **自然语言逻辑**：机器人的任务空间（如手掌位置）是关节角度的函数；对这个函数求一阶偏导数得到 Jacobian；Jacobian 把关节速度/加速度线性映射到任务速度/加速度。

## Overview

The task Jacobian `J` relates the time derivative of a task-space coordinate `x` to the joint velocity `q̇`:

```
ẋ = J(q) q̇
```

For whole-body control, common task Jacobians include the center-of-mass Jacobian, the foot Jacobian, and the end-effector Jacobian. Its time derivative `J̇` appears in acceleration mappings such as `ẍ = J q̈ + J̇ q̇`.

## Relevance to Humanoid Robotics

Without the task Jacobian, controllers could not translate high-level task objectives into joint commands. It is the bridge between task space and joint space.
