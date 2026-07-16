---
$id: rel_ent_component_allegro_hand_manufactured_by_ent_component_manufacturer_wonik_robotics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: manufactured_by
source:
  id: ent_component_allegro_hand
  name:
    en: Allegro Hand
    zh: Allegro 灵巧手
target:
  id: ent_component_manufacturer_wonik_robotics
  name:
    en: Wonik Robotics
    zh: Wonik Robotics
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Allegro Hand manufactured by Wonik Robotics.
  zh: Allegro 灵巧手manufactured_byWonik Robotics。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Allegro Hand 由 Wonik Robotics 生产。 | 证据: 由 Wonik
    Robotics 生产的商用16自由度四指灵巧机器人手，因扭矩控制关节和 ROS 兼容性而广泛用于操作研究。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_allegro_hand
  url: https://kg.rounds-tech.com/entry/ent_component_allegro_hand/
  accessed_at: '2026-07-16'
---
