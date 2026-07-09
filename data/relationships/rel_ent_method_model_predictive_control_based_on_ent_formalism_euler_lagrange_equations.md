---
$id: rel_ent_method_model_predictive_control_based_on_ent_formalism_euler_lagrange_equations
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control
    zh: 模型预测控制
    ko: ''
target:
  id: ent_formalism_euler_lagrange_equations
  name:
    en: Euler-Lagrange Equations
    zh: 欧拉-拉格朗日方程
    ko: ''
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: MPC for humanoids commonly uses floating-base dynamics derived from Euler-Lagrange equations as the prediction model.
  zh: 人形机器人的 MPC 通常以欧拉-拉格朗日方程导出的浮动基动力学作为预测模型。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-09'
  confidence: medium
  notes: Requires manual review of specific humanoid MPC references.
sources:
- id: src_kuindersma_et_al_2016
  type: paper
  title: S. Kuindersma et al., Optimization-based Locomotion Planning, Estimation, and Control Design for Atlas, Autonomous
    Robots, 2016
  url: https://doi.org/10.1007/s10514-016-9572-3
  date: '2016-08-01'
  accessed_at: '2026-07-09'
---
