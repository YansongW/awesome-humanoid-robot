---
$id: rel_ent_component_bldc_motor_uses_ent_method_foc_motor_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    zh: 无刷直流电机
target:
  id: ent_method_foc_motor_control
  name:
    en: Field-Oriented Control (FOC)
    zh: 磁场定向控制（FOC）
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Brushless DC Motor uses Field-Oriented Control (FOC).
  zh: 无刷直流电机使用磁场定向控制（FOC）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据说明磁场定向控制用于无刷直流电机的电流分解与独立控制，表明电机使用该控制方法。 |
    证据: - **Field-Oriented Control (FOC)**: Decomposes the stator current vector into the rotor rotating coordinate system
    for independent control, making AC motors as easy to control torque as DC motors.'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_bldc_motor
  url: https://kg.rounds-tech.com/entry/ent_component_bldc_motor/
  accessed_at: '2026-07-16'
---
