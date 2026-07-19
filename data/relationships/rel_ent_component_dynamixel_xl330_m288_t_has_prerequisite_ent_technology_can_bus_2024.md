---
$id: rel_ent_component_dynamixel_xl330_m288_t_has_prerequisite_ent_technology_can_bus_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_dynamixel_xl330_m288_t
  name:
    en: ROBOTIS DYNAMIXEL XL330-M288-T
    zh: ROBOTIS DYNAMIXEL XL330-M288-T 舵机
target:
  id: ent_technology_can_bus_2024
  name:
    en: CAN Bus
    zh: CAN 总线
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: ROBOTIS DYNAMIXEL XL330-M288-T has prerequisite CAN Bus.
  zh: ROBOTIS DYNAMIXEL XL330-M288-T 舵机前置依赖CAN 总线。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 该舵机使用TTL通信，但理解CAN总线有助于理解更高级的机器人通信架构。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
