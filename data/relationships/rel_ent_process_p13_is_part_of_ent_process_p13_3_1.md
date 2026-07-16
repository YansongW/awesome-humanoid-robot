---
$id: rel_ent_process_p13_is_part_of_ent_process_p13_3_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p13
  name:
    en: Electronics & Power Systems
    zh: 电子电气与能源系统（Electronics & Power）
target:
  id: ent_process_p13_3_1
  name:
    en: Hardware emergency stop and safety chain
    zh: 硬件急停与安全链
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Electronics & Power Systems is part of Hardware emergency stop and safety chain.
  zh: 电子电气与能源系统（Electronics & Power）is_part_of硬件急停与安全链。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 硬件急停与安全链是电子电气与能源系统的一部分 | 证据: 1 输入梳理与目标量化**：整理「硬件急停与安全链」所需的上游输入、参考标准与资源，将完成标准转化为可量化的验收指标，并明确
    Owner 与里程碑。'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p13
  url: https://kg.rounds-tech.com/entry/ent_process_p13/
  accessed_at: '2026-07-16'
---
