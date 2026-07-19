---
$id: rel_ent_robot_system_poppy_humanoid_has_prerequisite_ent_component_dynamixel_xl330_m288_t
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_poppy_humanoid
  name:
    en: Poppy Humanoid
    zh: Poppy 人形机器人
target:
  id: ent_component_dynamixel_xl330_m288_t
  name:
    en: ROBOTIS DYNAMIXEL XL330-M288-T
    zh: ROBOTIS DYNAMIXEL XL330-M288-T 舵机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Poppy Humanoid has prerequisite ROBOTIS DYNAMIXEL XL330-M288-T.
  zh: Poppy 人形机器人前置依赖ROBOTIS DYNAMIXEL XL330-M288-T 舵机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Poppy使用DYNAMIXEL XL系列伺服电机作为执行器。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
