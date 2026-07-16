---
$id: rel_ent_paper_song_avi_action_from_volumetric_inf_2025_uses_ent_method_action_token_prediction
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_song_avi_action_from_volumetric_inf_2025
  name:
    en: 'Avi: Action from Volumetric Inference'
    zh: Avi
target:
  id: ent_method_action_token_prediction
  name:
    en: Action Token Prediction
    zh: 动作 token 预测
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Avi: Action from Volumetric Inference uses Action Token Prediction.'
  zh: Avi使用动作 token 预测。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 该论文的VLA模型使用动作令牌预测来生成机器人动作'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_song_avi_action_from_volumetric_inf_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_song_avi_action_from_volumetric_inf_2025/
  accessed_at: '2026-07-16'
---
