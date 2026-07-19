---
$id: rel_ent_comp_servo_motor_has_prerequisite_ent_component_joint_encoder_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_comp_servo_motor
  name:
    en: High-Performance Servo Motor
    zh: 高性能伺服电机
target:
  id: ent_component_joint_encoder_2024
  name:
    en: Joint Encoder
    zh: 关节编码器
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: High-Performance Servo Motor has prerequisite Joint Encoder.
  zh: 高性能伺服电机前置依赖关节编码器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 伺服电机需要编码器反馈实现闭环控制。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
