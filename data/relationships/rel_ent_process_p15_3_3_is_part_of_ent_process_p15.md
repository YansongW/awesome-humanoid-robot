---
$id: rel_ent_process_p15_3_3_is_part_of_ent_process_p15
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p15_3_3
  name:
    en: Preparation and pre-audit for certification
    zh: 认证准备与预审核
target:
  id: ent_process_p15
  name:
    en: Integration & V & V testing
    zh: 整机集成与验证测试（Integration & V&V）
domains:
  source_domain: 04_assembly_integration_testing
  target_domain: 04_assembly_integration_testing
description:
  en: Preparation and pre-audit for certification is part of Integration & V & V testing.
  zh: 认证准备与预审核is_part_of整机集成与验证测试（Integration & V&V）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 认证准备与预审是整机集成与验证测试的一部分。 | 证据: **所属阶段/工作包**：整机集成与验证测试（Integration
    & V&V）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p15_3_3
  url: https://kg.rounds-tech.com/entry/ent_process_p15_3_3/
  accessed_at: '2026-07-16'
---
