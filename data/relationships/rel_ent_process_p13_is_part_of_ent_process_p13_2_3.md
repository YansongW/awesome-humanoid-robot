---
$id: rel_ent_process_p13_is_part_of_ent_process_p13_2_3
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p13
  name:
    en: Electronics & Power Systems
    zh: 电子电气与能源系统（Electronics & Power）
target:
  id: ent_process_p13_2_3
  name:
    en: Charging and Energy Management
    zh: 充电与能源管理
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Electronics & Power Systems is part of Charging and Energy Management.
  zh: 电子电气与能源系统（Electronics & Power）is_part_of充电与能源管理。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 充电与能源管理是电子电气与能源系统的一部分 | 证据: ##### Charging and
    Energy Management'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p13
  url: https://kg.rounds-tech.com/entry/ent_process_p13/
  accessed_at: '2026-07-16'
---
