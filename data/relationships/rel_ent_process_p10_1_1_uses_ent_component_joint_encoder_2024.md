---
$id: rel_ent_process_p10_1_1_uses_ent_component_joint_encoder_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p10_1_1
  name:
    en: IMU and joint encoder fusion
    zh: IMU 与关节编码器融合
target:
  id: ent_component_joint_encoder_2024
  name:
    en: Joint Encoder
    zh: 关节编码器
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: IMU and joint encoder fusion uses Joint Encoder.
  zh: IMU 与关节编码器融合使用关节编码器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法使用目标组件作为输入或资源。 | 证据: - Organize upstream
    inputs, reference standards, and resources required for "IMU and Joint Encoder Fusion," convert completion criteria into
    quantifiable acceptance indicators, and define the owner and milestones.'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p10_1_1
  url: https://kg.rounds-tech.com/entry/ent_process_p10_1_1/
  accessed_at: '2026-07-16'
---
