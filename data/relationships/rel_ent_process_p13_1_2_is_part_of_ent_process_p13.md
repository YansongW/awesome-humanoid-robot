---
$id: rel_ent_process_p13_1_2_is_part_of_ent_process_p13
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p13_1_2
  name:
    en: In-house/Third-party PCB Design
    zh: 自研/外购 PCB 设计
target:
  id: ent_process_p13
  name:
    en: Electronics & Power Systems
    zh: 电子电气与能源系统（Electronics & Power）
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: In-house/Third-party PCB Design is part of Electronics & Power Systems.
  zh: 自研/外购 PCB 设计is_part_of电子电气与能源系统（Electronics & Power）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 自研/外购 PCB 设计属于电子电气与能源系统工作包 | 证据: **所属阶段/工作包**：电子电气与能源系统（Electronics
    & Power）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p13_1_2
  url: https://kg.rounds-tech.com/entry/ent_process_p13_1_2/
  accessed_at: '2026-07-16'
---
