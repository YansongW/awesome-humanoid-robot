---
$id: rel_ent_component_bldc_motor_uses_ent_method_field_oriented_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    zh: 无刷直流电机
target:
  id: ent_method_field_oriented_control
  name:
    en: Field-Oriented Control
    zh: 磁场定向控制
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Brushless DC Motor uses Field-Oriented Control.
  zh: 无刷直流电机使用磁场定向控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据描述无刷直流电机通过Clark变换实现磁场定向控制，表明电机使用该控制方法。 | 证据:
    The core idea of **Field-Oriented Control** is to transform the currents from the three-phase stationary coordinate system
    to the two-phase stationary \(\alpha\beta\) coordinate system via **Clark transformation**, and then to the rotor-rotating
    \(dq'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_bldc_motor
  url: https://kg.rounds-tech.com/entry/ent_component_bldc_motor/
  accessed_at: '2026-07-16'
---
