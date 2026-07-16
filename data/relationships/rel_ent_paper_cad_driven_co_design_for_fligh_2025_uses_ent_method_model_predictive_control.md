---
$id: rel_ent_paper_cad_driven_co_design_for_fligh_2025_uses_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_cad_driven_co_design_for_fligh_2025
  name:
    en: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids
    zh: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids uses Model Predictive Control (MPC).
  zh: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids使用模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文使用动量线性化模型预测控制（MPC）策略。 | 证据: A minimum-jerk
    trajectory is used to assess flight performance, providing position and velocity references for a momentum-based linearized
    Model Predictive Control (MPC) strategy.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_cad_driven_co_design_for_fligh_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_cad_driven_co_design_for_fligh_2025/
  accessed_at: '2026-07-16'
---
