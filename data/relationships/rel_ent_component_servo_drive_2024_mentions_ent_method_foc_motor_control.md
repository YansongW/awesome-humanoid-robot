---
$id: rel_ent_component_servo_drive_2024_mentions_ent_method_foc_motor_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_component_servo_drive_2024
  name:
    en: Servo Drive
    zh: 伺服驱动器
target:
  id: ent_method_foc_motor_control
  name:
    en: Field-Oriented Control (FOC)
    zh: 磁场定向控制（FOC）
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Servo Drive mentions Field-Oriented Control (FOC).
  zh: 伺服驱动器提及磁场定向控制（FOC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 伺服驱动器把控制器指令转换为电机功率输出，通常采用 FOC 控制，包含电流环、速度环和位置环。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_servo_drive_2024
  url: https://kg.rounds-tech.com/entry/ent_component_servo_drive_2024/
  accessed_at: '2026-07-16'
---
