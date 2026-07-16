---
$id: rel_ent_process_p10_uses_ent_component_joint_encoder_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p10
  name:
    en: Motion Control Algorithm Development and Validation
    zh: 运动控制算法开发与验证（Motion Control）
target:
  id: ent_component_joint_encoder_2024
  name:
    en: Joint Encoder
    zh: 关节编码器
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: Motion Control Algorithm Development and Validation uses Joint Encoder.
  zh: 运动控制算法开发与验证（Motion Control）使用关节编码器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法使用了IMU和关节编码器融合，涉及目标组件 | 证据: ##### IMU and
    Joint Encoder Fusion'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p10
  url: https://kg.rounds-tech.com/entry/ent_process_p10/
  accessed_at: '2026-07-16'
---
