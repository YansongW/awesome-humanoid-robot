---
$id: rel_ent_process_p15_mentions_ent_process_p15_3_3
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p15
  name:
    en: Integration & V & V testing
    zh: 整机集成与验证测试（Integration & V&V）
target:
  id: ent_process_p15_3_3
  name:
    en: Preparation and pre-audit for certification
    zh: 认证准备与预审核
domains:
  source_domain: 04_assembly_integration_testing
  target_domain: 04_assembly_integration_testing
description:
  en: Integration & V & V testing mentions Preparation and pre-audit for certification.
  zh: 整机集成与验证测试（Integration & V&V）提及认证准备与预审核。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中提到了目标，但未明确源与目标之间的直接关系。 | 证据: 1 输入梳理与目标量化**：整理「认证准备与预审核」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确
    Owner 与里程碑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p15
  url: https://kg.rounds-tech.com/entry/ent_process_p15/
  accessed_at: '2026-07-16'
---
