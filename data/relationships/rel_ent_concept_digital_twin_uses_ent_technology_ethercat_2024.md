---
$id: rel_ent_concept_digital_twin_uses_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_concept_digital_twin
  name:
    en: Digital Twin
    zh: 数字孪生
target:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: Digital Twin uses EtherCAT.
  zh: 数字孪生使用EtherCAT。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明Digital Twin使用EtherCAT实现数据同步。 | 证据: **数据接口**：ROS
    2、DDS、EtherCAT 等实现虚实数据同步。'
sources:
- id: src_001
  type: other
  title: KG body of ent_concept_digital_twin
  url: https://kg.rounds-tech.com/entry/ent_concept_digital_twin/
  accessed_at: '2026-07-16'
---
