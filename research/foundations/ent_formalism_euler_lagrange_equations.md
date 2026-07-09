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
  reviewed_at: '2026-07-09'
  confidence: high
  notes: Curated names and summary from data/gap-entity-polish.yaml; placeholder body rewritten. Pending domain-expert final
    review.
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

# Euler-Lagrange Equations / 欧拉-拉格朗日方程 / 오일러-라그랑주 방정식

## 抽象

> **生活实例**：在所有可能的运动轨迹中，真实发生的那一条让某种“总成本”取极值。欧拉-拉格朗日方程就是这个极值条件的数学表达。
>
> **自然语言逻辑**：先写出系统的动能 $T$ 和势能 $V$，构造拉格朗日量 $\mathcal{L}=T-V$；然后要求作用量 $S=\int \mathcal{L}\,dt$ 取驻值，即可得到系统的运动方程。

## 形式化定义

设广义坐标为 $q(t) \in \mathbb{R}^n$，拉格朗日量 $\mathcal{L}(q, \dot{q}, t)$，则欧拉-拉格朗日方程为：

$$\frac{d}{dt}\frac{\partial \mathcal{L}}{\partial \dot{q}_i} - \frac{\partial \mathcal{L}}{\partial q_i} = \tau_i, \quad i = 1, \dots, n,$$

其中 $\tau_i$ 为广义非保守力。对于完整、理想约束的机械系统，通常取 $\mathcal{L} = T - V$。

## 与其他知识点的关系

- `derived_from` → [ent_lagrangian]
- `equivalent_to` → [ent_newton_euler_equations]
- `enables` → 机器人动力学建模 / ZMP / 全身控制
