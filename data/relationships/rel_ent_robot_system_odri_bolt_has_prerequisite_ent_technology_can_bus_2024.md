---
$id: rel_ent_robot_system_odri_bolt_has_prerequisite_ent_technology_can_bus_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_odri_bolt
  name:
    en: ODRI Bolt (Open Dynamic Robot Initiative)
    zh: ODRI Bolt 开源双足机器人
target:
  id: ent_technology_can_bus_2024
  name:
    en: CAN Bus
    zh: CAN 总线
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: ODRI Bolt (Open Dynamic Robot Initiative) has prerequisite CAN Bus.
  zh: ODRI Bolt 开源双足机器人前置依赖CAN 总线。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: ODRI Bolt使用CAN总线进行关节通信和实时控制。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
