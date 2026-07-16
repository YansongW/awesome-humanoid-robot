---
$id: rel_ent_process_p14_1_2_uses_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p14_1_2
  name:
    en: Real-time control framework
    zh: 实时控制框架
target:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: Real-time control framework uses EtherCAT.
  zh: 实时控制框架使用EtherCAT。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据显示实时控制框架使用EtherCAT作为方法/工具 | 证据: **方法 / 工具**：EtherCAT
    主站、RTOS、控制周期保证、抖动分析'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p14_1_2
  url: https://kg.rounds-tech.com/entry/ent_process_p14_1_2/
  accessed_at: '2026-07-16'
---
