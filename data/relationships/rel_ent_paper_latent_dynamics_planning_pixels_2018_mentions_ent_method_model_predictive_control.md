---
$id: rel_ent_paper_latent_dynamics_planning_pixels_2018_mentions_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_latent_dynamics_planning_pixels_2018
  name:
    en: Learning Latent Dynamics for Planning from Pixels
    zh: Learning Latent Dynamics for Planning from Pixels
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Learning Latent Dynamics for Planning from Pixels mentions Model Predictive Control (MPC).
  zh: Learning Latent Dynamics for Planning from Pixels提及模型预测控制（MPC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据提及MPC作为背景，说明其局限性，但没有明确的使用或开发关系。 | 证据: 在 PlaNet
    之前，从像素直接做模型预测控制（MPC）几乎不可行：视频预测模型要么是确定性的（无法处理多模态未来），要么是纯随机的（训练不稳定、长期预测坍缩）。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_latent_dynamics_planning_pixels_2018
  url: https://kg.rounds-tech.com/entry/ent_paper_latent_dynamics_planning_pixels_2018/
  accessed_at: '2026-08-06'
---
