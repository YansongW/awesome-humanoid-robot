---
$id: rel_ent_method_model_predictive_control_solves_ent_qp_standard_form
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: solves
source:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control
    zh: 模型预测控制
target:
  id: ent_qp_standard_form
  name:
    en: Quadratic Program Standard Form
    zh: 二次规划标准型
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: Each MPC iteration solves a quadratic program when the system dynamics and constraints are linearized.
  zh: 当系统动态与约束被线性化时，每次 MPC 迭代求解一个二次规划。
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-09'
  confidence: high
  notes: Standard formulation in linear MPC.
sources:
- id: src_borrelli_bemporad_morari_2017
  type: other
  title: "F. Borrelli, A. Bemporad, and M. Morari, Predictive Control for Linear and Hybrid Systems, Cambridge, 2017"
  url: https://doi.org/10.1017/9781139061799
  date: '2017-01-01'
  accessed_at: '2026-07-09'
---
