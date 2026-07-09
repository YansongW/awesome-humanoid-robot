---
$id: rel_ent_tech_on_device_vla_inference_uses_ent_method_action_token_prediction
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_tech_on_device_vla_inference
  name:
    en: On-Device VLA Inference
    ko: ''
target:
  id: ent_method_action_token_prediction
  name:
    en: Action Token Prediction
    ko: ''
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: On-device VLA inference uses action token prediction as its core action-generation method.
  zh: 端侧 VLA 推理将动作 token 预测作为其核心动作生成方法。
  ko: 온디바이스 VLA 추론은 액션 토큰 예측을 핵심 액션 생성 방법으로 사용한다.
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Created as part of the VLA knowledge-chain demonstration.
sources:
- id: src_openvla_2024
  type: paper
  title: 'OpenVLA: An Open-Source Vision-Language-Action Model'
  url: https://arxiv.org/abs/2406.09246
  date: '2024-06-13'
  accessed_at: '2026-06-26'
---
