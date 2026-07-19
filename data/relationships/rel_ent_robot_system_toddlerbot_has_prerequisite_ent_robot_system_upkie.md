---
$id: rel_ent_robot_system_toddlerbot_has_prerequisite_ent_robot_system_upkie
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
target:
  id: ent_robot_system_upkie
  name:
    en: Upkie Wheeled Biped Robot
    zh: Upkie 轮足双足机器人
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ToddlerBot has prerequisite Upkie Wheeled Biped Robot.
  zh: ToddlerBot 幼儿机器人前置依赖Upkie 轮足双足机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Upkie是轮式双足机器人，比ToddlerBot更简单，适合作为双足机器人入门基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
