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
  reviewed_at: '2026-07-13'
  confidence: high
  notes: Body populated from Wiki chapter section by scripts/fill_gap_bodies_from_wiki.py; pending human review and translation
    to en/ko.
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
