---
$id: rel_ent_component_frameless_torque_motor_2024_has_prerequisite_ent_component_bldc_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_frameless_torque_motor_2024
  name:
    en: Frameless Torque Motor
    zh: 无框力矩电机
target:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    zh: 无刷直流电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Frameless Torque Motor has prerequisite Brushless DC Motor.
  zh: 无框力矩电机前置依赖无刷直流电机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 无框力矩电机是一种特殊类型的无刷直流电机，理解BLDC是基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
