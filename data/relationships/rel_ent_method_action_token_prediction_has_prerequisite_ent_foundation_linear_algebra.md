---
$id: rel_ent_method_action_token_prediction_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_action_token_prediction
  name:
    en: Action Token Prediction
    ko: ''
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    ko: ''
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: Action token prediction has linear algebra as a prerequisite foundation.
  zh: 动作 token 预测以线性代数为前置基础。
  ko: 액션 토큰 예측은 선형대수학을 전제 기초로 한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Created as part of the VLA knowledge-chain demonstration.
sources:
- id: src_vaswani_2017
  type: paper
  title: Vaswani et al., Attention Is All You Need, NeurIPS 2017
  url: https://arxiv.org/abs/1706.03762
  date: '2017-06-12'
  accessed_at: '2026-06-26'
---
