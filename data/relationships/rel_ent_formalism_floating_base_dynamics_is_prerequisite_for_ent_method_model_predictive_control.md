---
$id: rel_ent_formalism_floating_base_dynamics_is_prerequisite_for_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_prerequisite_for
source:
  id: ent_formalism_floating_base_dynamics
  name:
    en: Floating-Base Dynamics
    zh: 浮动基动力学
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: Floating-Base Dynamics is prerequisite for Model Predictive Control (MPC).
  zh: 浮动基动力学is_prerequisite_for模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 浮动基动力学是人形机器人模型预测控制的数学基础，即前者是后者的前提。 | 证据: 这是人形机器人模型预测控制（MPC）与全身控制（WBC）的数学基础。'
sources:
- id: src_001
  type: other
  title: KG body of ent_formalism_floating_base_dynamics
  url: https://kg.rounds-tech.com/entry/ent_formalism_floating_base_dynamics/
  accessed_at: '2026-07-16'
---
