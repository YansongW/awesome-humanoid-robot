---
$id: rel_ent_process_p13_3_1_mentions_ent_method_fmea
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p13_3_1
  name:
    en: Hardware emergency stop and safety chain
    zh: 硬件急停与安全链
target:
  id: ent_method_fmea
  name:
    en: Failure Mode and Effects Analysis (FMEA)
    zh: 失效模式与影响分析（FMEA）
domains:
  source_domain: 02_components
  target_domain: 05_mass_production
description:
  en: Hardware emergency stop and safety chain mentions Failure Mode and Effects Analysis (FMEA).
  zh: 硬件急停与安全链提及失效模式与影响分析（FMEA）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: Safety system schematic, FMEA, emergency stop
    response time < target'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p13_3_1
  url: https://kg.rounds-tech.com/entry/ent_process_p13_3_1/
  accessed_at: '2026-07-16'
---
