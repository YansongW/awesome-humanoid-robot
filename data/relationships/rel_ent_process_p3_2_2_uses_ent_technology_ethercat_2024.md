---
$id: rel_ent_process_p3_2_2_uses_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p3_2_2
  name:
    en: Communication network architecture
    zh: 通信网络架构
target:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
domains:
  source_domain: 06_design_engineering
  target_domain: 08_software_middleware
description:
  en: Communication network architecture uses EtherCAT.
  zh: 通信网络架构使用EtherCAT。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法使用了目标技术EtherCAT | 证据: **方法 / 工具**：CAN-FD
    / EtherCAT / Ethernet / TSN 带宽与时延分析'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p3_2_2
  url: https://kg.rounds-tech.com/entry/ent_process_p3_2_2/
  accessed_at: '2026-07-16'
---
