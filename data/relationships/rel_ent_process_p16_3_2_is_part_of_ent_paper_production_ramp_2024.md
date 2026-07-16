---
$id: rel_ent_process_p16_3_2_is_part_of_ent_paper_production_ramp_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p16_3_2
  name:
    en: Cost Accounting and cost reduction
    zh: 成本核算与降本
target:
  id: ent_paper_production_ramp_2024
  name:
    en: Production Ramp
    zh: 产能爬坡
domains:
  source_domain: 05_mass_production
  target_domain: 05_mass_production
description:
  en: Cost Accounting and cost reduction is part of Production Ramp.
  zh: 成本核算与降本is_part_of产能爬坡。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Cost Accounting and cost reduction 属于包含 Production
    Ramp 的阶段 | 证据: **所属阶段/工作包**：小批量试产与量产准备（Pilot & Production Ramp）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p16_3_2
  url: https://kg.rounds-tech.com/entry/ent_process_p16_3_2/
  accessed_at: '2026-07-16'
---
