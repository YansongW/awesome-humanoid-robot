---
$id: rel_ent_process_p16_1_3_is_part_of_ent_process_p16
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p16_1_3
  name:
    en: Assembly line planning and SOP
    zh: 装配线规划与 SOP
target:
  id: ent_process_p16
  name:
    en: Pilot & Production Ramp
    zh: 小批量试产与量产准备（Pilot & Production Ramp）
domains:
  source_domain: 05_mass_production
  target_domain: 05_mass_production
description:
  en: Assembly line planning and SOP is part of Pilot & Production Ramp.
  zh: 装配线规划与 SOPis_part_of小批量试产与量产准备（Pilot & Production Ramp）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 装配线规划与SOP属于小批量试产与量产准备阶段的一部分 | 证据: **所属阶段/工作包**：小批量试产与量产准备（Pilot
    & Production Ramp）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p16_1_3
  url: https://kg.rounds-tech.com/entry/ent_process_p16_1_3/
  accessed_at: '2026-07-16'
---
