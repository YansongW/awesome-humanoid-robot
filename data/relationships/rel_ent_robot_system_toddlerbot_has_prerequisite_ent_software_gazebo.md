---
$id: rel_ent_robot_system_toddlerbot_has_prerequisite_ent_software_gazebo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
target:
  id: ent_software_gazebo
  name:
    en: Gazebo
    zh: Gazebo
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: ToddlerBot has prerequisite Gazebo.
  zh: ToddlerBot 幼儿机器人前置依赖Gazebo。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Gazebo是常用的开源仿真器，可用于在开发ToddlerBot之前测试双足控制算法。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
