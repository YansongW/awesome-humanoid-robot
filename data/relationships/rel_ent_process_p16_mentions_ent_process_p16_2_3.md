---
$id: rel_ent_process_p16_mentions_ent_process_p16_2_3
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p16
  name:
    en: Pilot & Production Ramp
    zh: 小批量试产与量产准备（Pilot & Production Ramp）
target:
  id: ent_process_p16_2_3
  name:
    en: Handling of incoming material and process exception
    zh: 来料与过程异常处理
domains:
  source_domain: 05_mass_production
  target_domain: 05_mass_production
description:
  en: Pilot & Production Ramp mentions Handling of incoming material and process exception.
  zh: 小批量试产与量产准备（Pilot & Production Ramp）提及来料与过程异常处理。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据仅列出''来料与过程异常处理''作为标题，没有明确的关系描述。 | 证据: #####
    来料与过程异常处理'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p16
  url: https://kg.rounds-tech.com/entry/ent_process_p16/
  accessed_at: '2026-07-16'
---
