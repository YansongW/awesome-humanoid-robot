---
$id: rel_ent_process_p7_1_1_is_part_of_ent_process_p7
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p7_1_1
  name:
    en: Selection and import of simulation platform
    zh: 仿真平台选型与导入
target:
  id: ent_process_p7
  name:
    en: Construction and verification of Simulation platform
    zh: 仿真平台搭建与验证（Simulation）
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: Selection and import of simulation platform is part of Construction and verification of Simulation platform.
  zh: 仿真平台选型与导入is_part_of仿真平台搭建与验证（Simulation）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法属于仿真平台搭建与验证这一工作包 | 证据: **所属阶段/工作包**：仿真平台搭建与验证（Simulation）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p7_1_1
  url: https://kg.rounds-tech.com/entry/ent_process_p7_1_1/
  accessed_at: '2026-07-16'
---
