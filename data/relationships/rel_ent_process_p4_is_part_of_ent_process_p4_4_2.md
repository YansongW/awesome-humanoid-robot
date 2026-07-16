---
$id: rel_ent_process_p4_is_part_of_ent_process_p4_4_2
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p4
  name:
    en: Design of Joint Module and Actuator & Drive
    zh: 关节模组与驱动系统设计（Actuator & Drive）
target:
  id: ent_process_p4_4_2
  name:
    en: Joint Safety and failure protection
    zh: 关节安全与故障保护
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Design of Joint Module and Actuator & Drive is part of Joint Safety and failure protection.
  zh: 关节模组与驱动系统设计（Actuator & Drive）is_part_of关节安全与故障保护。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 关节安全与故障保护是关节模组设计的一个子部分。 | 证据: ##### 关节安全与故障保护'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p4
  url: https://kg.rounds-tech.com/entry/ent_process_p4/
  accessed_at: '2026-07-16'
---
