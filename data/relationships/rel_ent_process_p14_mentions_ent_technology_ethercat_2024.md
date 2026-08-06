---
$id: rel_ent_process_p14_mentions_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
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
    | 证据: - **方法 / 工具**：EtherCAT 主站、RTOS、控制周期保证、抖动分析 | WP2.3 2026-08-06: type retyped uses->mentions after DeepSeek review.
    Reason: 证据仅列出EtherCAT主站作为方法/工具，未明确支持''uses''强关系，且目标为技术类型，宜降级为提及关系。. Original file rel_ent_process_p14_uses_ent_technology_ethercat_2024.'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p14
  url: https://kg.rounds-tech.com/entry/ent_process_p14/
  accessed_at: '2026-07-16'
---
