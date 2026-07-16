---
$id: rel_ent_component_servo_drive_2024_uses_ent_principle_current_velocity_position_loops
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_servo_drive_2024
  name:
    en: Servo Drive
    zh: 伺服驱动器
target:
  id: ent_principle_current_velocity_position_loops
  name:
    en: Current / Velocity / Position Control Loops
    zh: 电流环/速度环/位置环
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Servo Drive uses Current / Velocity / Position Control Loops.
  zh: 伺服驱动器使用电流环/速度环/位置环。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 伺服驱动器使用电流环/速度环/位置环控制结构。 | 证据: - **电流环/速度环/位置环**：伺服控制的三环结构，由内而外响应越来越快。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_servo_drive_2024
  url: https://kg.rounds-tech.com/entry/ent_component_servo_drive_2024/
  accessed_at: '2026-07-16'
---
