---
$id: rel_ent_technology_aloha_teleoperation_system_2023_has_prerequisite_ent_technology_can_bus_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_technology_aloha_teleoperation_system_2023
  name:
    en: ALOHA Teleoperation System
    zh: ALOHA 遥操作系统
target:
  id: ent_technology_can_bus_2024
  name:
    en: CAN Bus
    zh: CAN 总线
domains:
  source_domain: 09_data_datasets
  target_domain: 08_software_middleware
description:
  en: ALOHA Teleoperation System has prerequisite CAN Bus.
  zh: ALOHA 遥操作系统前置依赖CAN 总线。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: CAN总线是机器人底层通信的基础，理解它有助于掌握遥操作系统的硬件数据流。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
