---
$id: rel_ent_process_p15_is_part_of_ent_process_p15_3_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p15
  name:
    en: Integration & V & V testing
    zh: 整机集成与验证测试（Integration & V&V）
target:
  id: ent_process_p15_3_1
  name:
    en: Joint and machine endurance test
    zh: 关节与整机耐久测试
domains:
  source_domain: 04_assembly_integration_testing
  target_domain: 04_assembly_integration_testing
description:
  en: Integration & V & V testing is part of Joint and machine endurance test.
  zh: 整机集成与验证测试（Integration & V&V）is_part_of关节与整机耐久测试。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明源方法包含目标方法作为子项。 | 证据: ##### 关节与整机耐久测试'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p15
  url: https://kg.rounds-tech.com/entry/ent_process_p15/
  accessed_at: '2026-07-16'
---
