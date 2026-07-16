---
$id: rel_ent_process_p15_1_1_is_part_of_ent_process_p15
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p15_1_1
  name:
    en: Integration and debugging of leg system
    zh: 腿部系统集成与调试
target:
  id: ent_process_p15
  name:
    en: Integration & V & V testing
    zh: 整机集成与验证测试（Integration & V&V）
domains:
  source_domain: 04_assembly_integration_testing
  target_domain: 04_assembly_integration_testing
description:
  en: Integration and debugging of leg system is part of Integration & V & V testing.
  zh: 腿部系统集成与调试is_part_of整机集成与验证测试（Integration & V&V）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明源方法属于目标工作包。 | 证据: **所属阶段/工作包**：整机集成与验证测试（Integration
    & V&V）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p15_1_1
  url: https://kg.rounds-tech.com/entry/ent_process_p15_1_1/
  accessed_at: '2026-07-16'
---
