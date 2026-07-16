---
$id: rel_ent_paper_track_any_motions_under_any_di_2025_mentions_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_track_any_motions_under_any_di_2025
  name:
    en: Track Any Motions under Any Disturbances
    zh: 跟踪任何干扰下的任何动作
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: Track Any Motions under Any Disturbances mentions Model Predictive Control (MPC).
  zh: 跟踪任何干扰下的任何动作提及模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中仅将MPC作为传统方法进行对比讨论，并未表明源论文使用或基于MPC。 | 证据:
    传统基于模型预测控制（MPC）的方法虽能处理部分扰动，但通常需要精确的动力学模型和简化的接触假设，难以应对高维、非线性的全身运动。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_track_any_motions_under_any_di_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_track_any_motions_under_any_di_2025/
  accessed_at: '2026-07-16'
---
