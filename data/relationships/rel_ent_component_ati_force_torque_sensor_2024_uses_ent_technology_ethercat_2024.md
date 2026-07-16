---
$id: rel_ent_component_ati_force_torque_sensor_2024_uses_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_ati_force_torque_sensor_2024
  name:
    en: ATI Force Torque Sensor
    zh: ATI 力/力矩传感器
target:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: ATI Force Torque Sensor uses EtherCAT.
  zh: ATI 力/力矩传感器使用EtherCAT。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中列出EtherCAT作为通信方式，表明ATI力扭矩传感器使用EtherCAT技术。
    | 证据: | 通信 | TCP/IP/USB/EtherNet/IP | 模拟/DAQ/EtherCAT | EtherCAT/Ethernet/CAN |'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_ati_force_torque_sensor_2024
  url: https://kg.rounds-tech.com/entry/ent_component_ati_force_torque_sensor_2024/
  accessed_at: '2026-07-16'
---
