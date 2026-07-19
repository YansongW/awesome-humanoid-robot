---
$id: rel_ent_method_model_predictive_control_has_prerequisite_ent_method_pid_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
target:
  id: ent_method_pid_control
  name:
    en: PID Control
    zh: PID控制
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Model Predictive Control (MPC) has prerequisite PID Control.
  zh: 模型预测控制（MPC）前置依赖PID控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: MPC是比PID更高级的控制方法，理解基础反馈控制有助于掌握优化控制的思想。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
