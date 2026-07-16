---
$id: rel_ent_process_p13_uses_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p13
  name:
    en: Electronics & Power Systems
    zh: 电子电气与能源系统（Electronics & Power）
target:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: Electronics & Power Systems uses EtherCAT.
  zh: 电子电气与能源系统（Electronics & Power）使用EtherCAT。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 电子电气与能源系统使用 EtherCAT 作为通信技术 | 证据: - **方法 / 工具**：CAN-FD、EtherCAT、Ethernet、TSN、PTP
    时间同步'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p13
  url: https://kg.rounds-tech.com/entry/ent_process_p13/
  accessed_at: '2026-07-16'
---
