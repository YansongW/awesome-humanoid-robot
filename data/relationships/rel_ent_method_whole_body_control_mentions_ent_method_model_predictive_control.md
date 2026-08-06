---
$id: rel_ent_method_whole_body_control_mentions_ent_method_model_predictive_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_method_whole_body_control
  name:
    en: Whole-Body Control (WBC)
    zh: 全身控制（WBC）
target:
  id: ent_method_model_predictive_control
  name:
    en: Model Predictive Control (MPC)
    zh: 模型预测控制（MPC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Whole-Body Control (WBC) mentions Model Predictive Control (MPC).
  zh: 全身控制（WBC）提及模型预测控制（MPC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: | 维度 | 预计算步态 + 稳定器 | **WBC（QP）** | 全身 MPC | 端到端
    RL 策略 |'
sources:
- id: src_001
  type: other
  title: KG body of ent_method_whole_body_control
  url: https://kg.rounds-tech.com/entry/ent_method_whole_body_control/
  accessed_at: '2026-08-06'
---
