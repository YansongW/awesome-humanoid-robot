---
$id: rel_ent_component_servo_drive_2024_has_prerequisite_ent_foundation_classical_mechanics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_servo_drive_2024
  name:
    en: Servo Drive
    zh: 伺服驱动器
target:
  id: ent_foundation_classical_mechanics
  name:
    en: Classical Mechanics
    zh: 经典力学
domains:
  source_domain: 02_components
  target_domain: 00_foundations
description:
  en: Servo Drive has prerequisite Classical Mechanics.
  zh: 伺服驱动器前置依赖经典力学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 理解电机转矩和负载动力学需要经典力学。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
