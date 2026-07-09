---
$id: rel_ent_method_field_oriented_control_used_in_ent_component_rotary_actuator_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: enables
source:
  id: ent_method_field_oriented_control
  name:
    en: Field-Oriented Control
    zh: 磁场定向控制
    ko: ''
target:
  id: ent_component_rotary_actuator_2024
  name:
    en: Rotary Actuator
    zh: 旋转执行器
    ko: ''
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: FOC is widely used inside rotary actuator servo drives for PMSM/BLDC motors in humanoid joints.
  zh: FOC 广泛用于人形机器人关节旋转执行器中的 PMSM/BLDC 伺服驱动。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-09'
  confidence: medium
  notes: Industry standard for high-performance servo drives; specific product references need verification.
sources:
- id: src_mohan_2003
  type: other
  title: 'N. Mohan, Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink, Wiley, 2013'
  url: https://doi.org/10.1002/9781118704810
  date: '2013-01-01'
  accessed_at: '2026-07-09'
---
