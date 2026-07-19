---
$id: rel_ent_principle_current_velocity_position_loops_has_prerequisite_ent_component_servo_drive_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_principle_current_velocity_position_loops
  name:
    en: Current / Velocity / Position Control Loops
    zh: 电流环/速度环/位置环
target:
  id: ent_component_servo_drive_2024
  name:
    en: Servo Drive
    zh: 伺服驱动器
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Current / Velocity / Position Control Loops has prerequisite Servo Drive.
  zh: 电流环/速度环/位置环前置依赖伺服驱动器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 伺服驱动器是执行电流-速度-位置环控制的硬件载体。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
