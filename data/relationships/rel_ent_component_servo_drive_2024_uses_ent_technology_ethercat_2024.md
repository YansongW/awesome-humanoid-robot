---
$id: rel_ent_component_servo_drive_2024_uses_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_servo_drive_2024
  name:
    en: Servo Drive
    zh: 伺服驱动器
target:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: Servo Drive uses EtherCAT.
  zh: 伺服驱动器使用EtherCAT。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 伺服驱动器通过EtherCAT总线与控制器通信，即使用EtherCAT。 | 证据: -
    **总线通信**：驱动器与控制器通过 CAN/EtherCAT/RS485 等总线交换数据。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_servo_drive_2024
  url: https://kg.rounds-tech.com/entry/ent_component_servo_drive_2024/
  accessed_at: '2026-07-16'
---
