---
$id: rel_ent_technology_ethercat_2024_has_prerequisite_ent_technology_can_bus_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
target:
  id: ent_technology_can_bus_2024
  name:
    en: CAN Bus
    zh: CAN 总线
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: EtherCAT has prerequisite CAN Bus.
  zh: EtherCAT前置依赖CAN 总线。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: CAN总线是现场总线的基础，理解它有助于对比学习EtherCAT的更高性能和确定性特性。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
