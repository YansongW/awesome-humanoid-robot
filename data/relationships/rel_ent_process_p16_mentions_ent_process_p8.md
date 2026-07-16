---
$id: rel_ent_process_p16_mentions_ent_process_p8
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p16
  name:
    en: Pilot & Production Ramp
    zh: 小批量试产与量产准备（Pilot & Production Ramp）
target:
  id: ent_process_p8
  name:
    en: Structural FEA and iteration
    zh: 结构强度仿真与迭代（Structural FEA）
domains:
  source_domain: 05_mass_production
  target_domain: 06_design_engineering
description:
  en: Pilot & Production Ramp mentions Structural FEA and iteration.
  zh: 小批量试产与量产准备（Pilot & Production Ramp）提及结构强度仿真与迭代（Structural FEA）。
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
