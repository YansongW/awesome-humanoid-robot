---
$id: rel_ent_component_dynamixel_xm430_w210_t_has_prerequisite_ent_component_joint_encoder_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_dynamixel_xm430_w210_t
  name:
    en: ROBOTIS DYNAMIXEL XM430-W210-T
    zh: ROBOTIS DYNAMIXEL XM430-W210-T 舵机
target:
  id: ent_component_joint_encoder_2024
  name:
    en: Joint Encoder
    zh: 关节编码器
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ROBOTIS DYNAMIXEL XM430-W210-T has prerequisite Joint Encoder.
  zh: ROBOTIS DYNAMIXEL XM430-W210-T 舵机前置依赖关节编码器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 该舵机具有绝对编码器反馈，理解编码器原理有助于利用其反馈数据。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
