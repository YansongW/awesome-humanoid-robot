---
$id: rel_ent_component_frameless_torque_motor_2024_is_part_of_ent_robot_system_tesla_optimus
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_component_frameless_torque_motor_2024
  name:
    en: Frameless Torque Motor
    zh: 无框力矩电机
target:
  id: ent_robot_system_tesla_optimus
  name:
    en: Tesla Optimus
    zh: Tesla Optimus
domains:
  source_domain: 02_components
  target_domain: 05_mass_production
description:
  en: Frameless Torque Motor is part of Tesla Optimus.
  zh: 无框力矩电机is_part_ofTesla Optimus。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据指出特斯拉Optimus的旋转关节采用无框力矩电机，表明该电机是Optimus的一部分。
    | 证据: Tesla Optimus 的旋转关节 reportedly 采用无框力矩电机加谐波减速器的一体化方案[14]。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_frameless_torque_motor_2024
  url: https://kg.rounds-tech.com/entry/ent_component_frameless_torque_motor_2024/
  accessed_at: '2026-07-16'
---
