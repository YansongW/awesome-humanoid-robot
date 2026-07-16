---
$id: rel_ent_process_p9_1_1_is_part_of_ent_process_p9
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p9_1_1
  name:
    en: List of heat sources and power consumption
    zh: 热源与功耗清单
target:
  id: ent_process_p9
  name:
    en: Thermal Management simulation and iteration
    zh: 热管理仿真与迭代（Thermal Management）
domains:
  source_domain: 06_design_engineering
  target_domain: 06_design_engineering
description:
  en: List of heat sources and power consumption is part of Thermal Management simulation and iteration.
  zh: 热源与功耗清单is_part_of热管理仿真与迭代（Thermal Management）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明源（热源列表与功耗）属于目标（热管理仿真与迭代）这一工作包。 | 证据: **所属阶段/工作包**：热管理仿真与迭代（Thermal
    Management）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p9_1_1
  url: https://kg.rounds-tech.com/entry/ent_process_p9_1_1/
  accessed_at: '2026-07-16'
---
