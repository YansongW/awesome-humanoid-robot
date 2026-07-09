---
$id: rel_ent_method_model_predictive_control_requires_ent_foundation_convex_optimization
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: requires
source:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control
    zh: 模型预测控制
target:
  id: ent_foundation_convex_optimization
  name:
    en: Convex Optimization
    zh: 凸优化
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: Stability and tractability of MPC rely on convex optimization theory and efficient QP solvers.
  zh: MPC 的稳定性与可解性依赖于凸优化理论与高效 QP 求解器。
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-09'
  confidence: high
  notes: Convex QP formulation is the default in linear MPC.
sources:
- id: src_borrelli_bemporad_morari_2017
  type: other
  title: "F. Borrelli, A. Bemporad, and M. Morari, Predictive Control for Linear and Hybrid Systems, Cambridge, 2017"
  url: https://doi.org/10.1017/9781139061799
  date: '2017-01-01'
  accessed_at: '2026-07-09'
---
