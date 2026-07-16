---
$id: rel_ent_material_rare_earth_supply_mentions_ent_tech_li_battery_humanoid
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_material_rare_earth_supply
  name:
    en: Rare-Earth Supply Chain
    zh: 稀土元素供应链
target:
  id: ent_tech_li_battery_humanoid
  name:
    en: Lithium-Ion Battery System for Humanoid Robots
    zh: 人形机器人锂离子电池系统
domains:
  source_domain: 01_raw_materials
  target_domain: 01_raw_materials
description:
  en: Rare-Earth Supply Chain mentions Lithium-Ion Battery System for Humanoid Robots.
  zh: 稀土元素供应链提及人形机器人锂离子电池系统。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 稀土供应链与人形机器人锂电池系统相关，作为材料来源被提及。'
sources:
- id: src_001
  type: other
  title: KG body of ent_material_rare_earth_supply
  url: https://kg.rounds-tech.com/entry/ent_material_rare_earth_supply/
  accessed_at: '2026-07-16'
---
