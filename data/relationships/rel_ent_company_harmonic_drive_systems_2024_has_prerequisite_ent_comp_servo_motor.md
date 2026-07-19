---
$id: rel_ent_company_harmonic_drive_systems_2024_has_prerequisite_ent_comp_servo_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_company_harmonic_drive_systems_2024
  name:
    en: Harmonic Drive Systems
    zh: 哈默纳科
target:
  id: ent_comp_servo_motor
  name:
    en: High-Performance Servo Motor
    zh: 高性能伺服电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Harmonic Drive Systems has prerequisite High-Performance Servo Motor.
  zh: 哈默纳科前置依赖高性能伺服电机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 谐波减速器通常与伺服电机配合使用。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
