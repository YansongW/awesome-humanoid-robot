---
$id: ent_formalism_euler_lagrange_equations
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Euler-Lagrange Equations
  zh: 欧拉-拉格朗日方程
  ko: 오일러-라그랑주 방정식
summary:
  en: Second-order differential equations derived from the stationarity of the action integral, giving the equations of motion
    for mechanical systems in generalized coordinates.
  zh: 由作用量变分驻值条件导出的二阶微分方程组，给出广义坐标下机械系统的运动方程。
  ko: 작용 적분의 정지 조건에서 도출된 2차 미분방정식으로, 일반화 좌표에서 기계 시스템의 용동 방정식을 제공.
domains:
- 00_foundations
- 06_design_engineering
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- mechanics
- classical_mechanics
- variational_principle
- lagrangian
- dynamics
- equations_of_motion
- wiki_gap
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-08.md#8.4.2 拉格朗日动力学 by scripts/backfill_nonpaper_entries.py.
sources:
- id: src_goldstein_2002
  type: other
  title: H. Goldstein, C. Poole, and J. Safko, Classical Mechanics, 3rd ed., Addison-Wesley, 2002
  url: https://doi.org/10.2307/2522307
  date: '2002-01-01'
  accessed_at: '2026-07-09'
- id: src_spong_hutchinson_vidyasagar_2006
  type: other
  title: M. W. Spong, S. Hutchinson, and M. Vidyasagar, Robot Modeling and Control, Wiley, 2006
  url: https://doi.org/10.1002/0470173876
  date: '2006-01-01'
  accessed_at: '2026-07-09'
related_entities:
- id: ent_lagrangian
  relationship: derived_from
  description:
    en: The Euler-Lagrange equations follow from stationarity of the action integral of the Lagrangian.
    zh: 欧拉-拉格朗日方程由拉格朗日量的作用量变分取驻值导出。
- id: ent_newton_euler_equations
  relationship: mentions
  description:
    en: For rigid-body systems, Euler-Lagrange and Newton-Euler formulations yield the same equations of motion.
    zh: 对刚体系统，欧拉-拉格朗日与牛顿-欧拉两种形式等价。
---
## 概述
欧拉-拉格朗日方程是人形机器人领域的重要formalism。以下内容整理自项目 Wiki，供深入查阅。

## 核心内容
**拉格朗日方法（Lagrangian dynamics）**从能量角度出发，自动导出系统运动方程，适合串联机械臂和树形结构机器人[3][6]。定义拉格朗日量：

$$
L = T - V
$$

其中 $T$ 为系统总动能，$V$ 为总势能。对于关节变量 $q_i$，欧拉-拉格朗日方程为：

$$
\frac{d}{dt}\left(\frac{\partial L}{\partial \dot{q}_i}\right) - \frac{\partial L}{\partial q_i} = \tau_i
$$

其中 $\tau_i$ 为对应关节的广义力/力矩。

!!! note "术语解释：拉格朗日量、动能、势能、广义力、欧拉-拉格朗日方程"
    - **拉格朗日量（Lagrangian）**：系统动能与势能之差，$L = T - V$。
    - **动能（kinetic energy）**：由于运动而具有的能量，$T = \frac{1}{2}\dot{\mathbf{q}}^T \mathbf{M}(\mathbf{q}) \dot{\mathbf{q}}$。
    - **势能（potential energy）**：由于位置或形变而具有的能量，如重力势能 $V_g = mgh$。
    - **广义力（generalized force）**：与广义坐标对应的力或力矩。
    - **欧拉-拉格朗日方程**：由能量推导运动方程的标准形式。

机器人动力学方程的标准形式为：

$$
\mathbf{M}(\mathbf{q})\ddot{\mathbf{q}} + \mathbf{C}(\mathbf{q}, \dot{\mathbf{q}})\dot{\mathbf{q}} + \mathbf{g}(\mathbf{q}) = \boldsymbol{\tau} + \mathbf{J}^T \mathbf{F}_{\text{ext}}
$$

其中：
- $\mathbf{M}(\mathbf{q})$：质量矩阵（正定对称）。
- $\mathbf{C}(\mathbf{q}, \dot{\mathbf{q}})$：科氏力与离心力项。
- $\mathbf{g}(\mathbf{q})$：重力项。
- $\boldsymbol{\tau}$：关节驱动力矩。
- $\mathbf{F}_{\text{ext}}$：末端外部接触力。

!!! note "术语解释：质量矩阵、科氏力、离心力、重力项、接触力"
    - **质量矩阵（mass matrix）**：把关节加速度映射为惯性力矩的矩阵。
    - **科氏力（Coriolis force）**：由于坐标系旋转与相对运动耦合产生的惯性力。
    - **离心力（centrifugal force）**：由于旋转而产生的径向惯性力。
    - **重力项（gravity term）**：由重力场引起的广义力。
    - **接触力（contact force）**：机器人与外界接触时产生的力。

## 参考
- [H. Goldstein, C. Poole, and J. Safko, Classical Mechanics, 3rd ed., Addison-Wesley, 2002](https://doi.org/10.2307/2522307)
- [M. W. Spong, S. Hutchinson, and M. Vidyasagar, Robot Modeling and Control, Wiley, 2006](https://doi.org/10.1002/0470173876)
- 项目 Wiki：chapter-08.md#8.4.2 拉格朗日动力学

