---
$id: rel_ent_principle_zero_moment_point_based_on_ent_formalism_euler_lagrange_equations
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_principle_zero_moment_point
  name:
    en: Zero Moment Point
    zh: 零力矩点
target:
  id: ent_formalism_euler_lagrange_equations
  name:
    en: Euler-Lagrange Equations
    zh: 欧拉-拉格朗日方程
domains:
  source_domain: 06_design_engineering
  target_domain: 00_foundations
description:
  en: The ZMP condition is derived from the moment balance of the robot's equations of motion, commonly expressed via Euler-Lagrange
    dynamics.
  zh: ZMP 条件来源于机器人运动方程的力矩平衡，通常由欧拉-拉格朗日动力学表达。
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-09'
  confidence: high
  notes: Standard derivation in bipedal robotics literature.
sources:
- id: src_vukobratovic_2004_zmp
  type: paper
  title: M. Vukobratović and B. Borovac, Zero-Moment Point — Thirty Five Years of Its Life, IJHR, 2004
  url: https://doi.org/10.1142/S0219843604000083
  date: '2004-03-01'
  accessed_at: '2026-07-09'
---
