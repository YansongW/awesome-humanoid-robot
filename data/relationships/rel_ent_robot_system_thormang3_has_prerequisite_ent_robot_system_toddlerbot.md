---
$id: rel_ent_robot_system_thormang3_has_prerequisite_ent_robot_system_toddlerbot
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_thormang3
  name:
    en: THORMANG3
    zh: THORMANG3 全尺寸人形机器人
target:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: THORMANG3 has prerequisite ToddlerBot.
  zh: THORMANG3 全尺寸人形机器人前置依赖ToddlerBot 幼儿机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: ToddlerBot是更小、更简单的开源双足机器人，适合作为理解全尺寸人形机器人THORMANG3的基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
