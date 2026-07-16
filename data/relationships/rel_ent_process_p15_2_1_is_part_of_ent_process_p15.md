---
$id: rel_ent_process_p15_2_1_is_part_of_ent_process_p15
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p15_2_1
  name:
    en: Safety function test
    zh: 安全功能测试
target:
  id: ent_process_p15
  name:
    en: Integration & V & V testing
    zh: 整机集成与验证测试（Integration & V&V）
domains:
  source_domain: 04_assembly_integration_testing
  target_domain: 04_assembly_integration_testing
description:
  en: Safety function test is part of Integration & V & V testing.
  zh: 安全功能测试is_part_of整机集成与验证测试（Integration & V&V）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 安全功能测试是整机集成与验证测试的一部分。 | 证据: **所属阶段/工作包**：整机集成与验证测试（Integration
    & V&V）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p15_2_1
  url: https://kg.rounds-tech.com/entry/ent_process_p15_2_1/
  accessed_at: '2026-07-16'
---
