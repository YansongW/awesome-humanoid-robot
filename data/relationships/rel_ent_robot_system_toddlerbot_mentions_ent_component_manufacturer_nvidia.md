---
$id: rel_ent_robot_system_toddlerbot_mentions_ent_component_manufacturer_nvidia
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
target:
  id: ent_component_manufacturer_nvidia
  name:
    en: NVIDIA
    zh: 英伟达
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ToddlerBot mentions NVIDIA.
  zh: ToddlerBot 幼儿机器人提及英伟达。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: | 主控 | NVIDIA Jetson Orin NX 16GB | 论文 |'
sources:
- id: src_001
  type: other
  title: KG body of ent_robot_system_toddlerbot
  url: https://kg.rounds-tech.com/entry/ent_robot_system_toddlerbot/
  accessed_at: '2026-07-31'
---
