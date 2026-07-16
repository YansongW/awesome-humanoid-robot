---
$id: rel_ent_process_p16_is_part_of_ent_paper_production_ramp_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p16
  name:
    en: Pilot & Production Ramp
    zh: 小批量试产与量产准备（Pilot & Production Ramp）
target:
  id: ent_paper_production_ramp_2024
  name:
    en: Production Ramp
    zh: 产能爬坡
domains:
  source_domain: 05_mass_production
  target_domain: 05_mass_production
description:
  en: Pilot & Production Ramp is part of Production Ramp.
  zh: 小批量试产与量产准备（Pilot & Production Ramp）is_part_of产能爬坡。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 小批量试产与量产准备是量产准备阶段的一部分。 | 证据: 小批量试产与量产准备（Pilot
    & Production Ramp）是人形机器人产品开发全流程中的第 16 个阶段，在 WBS V3 中展开为若干三级子任务。'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p16
  url: https://kg.rounds-tech.com/entry/ent_process_p16/
  accessed_at: '2026-07-16'
---
