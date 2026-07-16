---
$id: rel_ent_process_p6_1_2_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p6_1_2
  name:
    en: DH/modify the DH parameter definition
    zh: DH / 修改 DH 参数定义
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 06_design_engineering
  target_domain: 08_software_middleware
description:
  en: DH/modify the DH parameter definition uses Pinocchio.
  zh: DH / 修改 DH 参数定义使用Pinocchio。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: DH参数定义方法使用了Pinocchio作为工具。 | 证据: **方法 / 工具**：解析法、Pinocchio/RBDL、符号计算'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p6_1_2
  url: https://kg.rounds-tech.com/entry/ent_process_p6_1_2/
  accessed_at: '2026-07-16'
---
