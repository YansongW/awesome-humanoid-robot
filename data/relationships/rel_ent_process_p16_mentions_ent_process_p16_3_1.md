---
$id: rel_ent_process_p16_mentions_ent_process_p16_3_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p16
  name:
    en: Pilot & Production Ramp
    zh: 小批量试产与量产准备（Pilot & Production Ramp）
target:
  id: ent_process_p16_3_1
  name:
    en: Pilot Run
    zh: 小批量试产（Pilot Run）
domains:
  source_domain: 05_mass_production
  target_domain: 05_mass_production
description:
  en: Pilot & Production Ramp mentions Pilot Run.
  zh: 小批量试产与量产准备（Pilot & Production Ramp）提及小批量试产（Pilot Run）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p4_wiki_ch10. Evidence: 在 Wiki 第 10 章同一小节共现'
sources:
- id: src_001
  type: other
  title: Wiki 第 10 章
  url: https://kg.rounds-tech.com/wiki/chapters/chapter-10/
  accessed_at: '2026-07-16'
---
