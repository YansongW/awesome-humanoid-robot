---
$id: rel_ent_component_frameless_torque_motor_2024_has_prerequisite_ent_method_field_oriented_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_frameless_torque_motor_2024
  name:
    en: Frameless Torque Motor
    zh: 无框力矩电机
target:
  id: ent_method_field_oriented_control
  name:
    en: Field-Oriented Control
    zh: 磁场定向控制
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Frameless Torque Motor has prerequisite Field-Oriented Control.
  zh: 无框力矩电机前置依赖磁场定向控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 磁场定向控制是高性能力矩电机控制的核心方法。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
