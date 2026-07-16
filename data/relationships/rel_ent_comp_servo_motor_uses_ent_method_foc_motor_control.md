---
$id: rel_ent_comp_servo_motor_uses_ent_method_foc_motor_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_comp_servo_motor
  name:
    en: High-Performance Servo Motor
    zh: 高性能伺服电机
target:
  id: ent_method_foc_motor_control
  name:
    en: Field-Oriented Control (FOC)
    zh: 磁场定向控制（FOC）
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: High-Performance Servo Motor uses Field-Oriented Control (FOC).
  zh: 高性能伺服电机使用磁场定向控制（FOC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 交流伺服电机使用磁场定向控制（FOC）。 | 证据: AC servo motors typically
    use Field-Oriented Control (FOC).'
sources:
- id: src_001
  type: other
  title: KG body of ent_comp_servo_motor
  url: https://kg.rounds-tech.com/entry/ent_comp_servo_motor/
  accessed_at: '2026-07-16'
---
