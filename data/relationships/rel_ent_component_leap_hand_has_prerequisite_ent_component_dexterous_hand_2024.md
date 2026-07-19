---
$id: rel_ent_component_leap_hand_has_prerequisite_ent_component_dexterous_hand_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_leap_hand
  name:
    en: LEAP Hand
    zh: LEAP 灵巧手
target:
  id: ent_component_dexterous_hand_2024
  name:
    en: Dexterous Hand
    zh: 灵巧手
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: LEAP Hand has prerequisite Dexterous Hand.
  zh: LEAP 灵巧手前置依赖灵巧手。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: LEAP Hand是一种灵巧手，先理解灵巧手的一般概念有助于掌握其具体设计。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
