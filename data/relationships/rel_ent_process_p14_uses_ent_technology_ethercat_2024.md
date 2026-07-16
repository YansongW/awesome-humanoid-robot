---
$id: rel_ent_process_p14_uses_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p14
  name:
    en: Software & Integration
    zh: 软件中间件与系统集成（Software & Integration）
target:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: Software & Integration uses EtherCAT.
  zh: 软件中间件与系统集成（Software & Integration）使用EtherCAT。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据列出EtherCAT主站作为Software & Integration使用的方法/工具。
    | 证据: - **方法 / 工具**：EtherCAT 主站、RTOS、控制周期保证、抖动分析'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p14
  url: https://kg.rounds-tech.com/entry/ent_process_p14/
  accessed_at: '2026-07-16'
---
