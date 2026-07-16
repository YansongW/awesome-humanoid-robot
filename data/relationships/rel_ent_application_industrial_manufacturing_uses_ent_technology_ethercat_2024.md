---
$id: rel_ent_application_industrial_manufacturing_uses_ent_technology_ethercat_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_application_industrial_manufacturing
  name:
    en: Industrial Manufacturing
    zh: 工业制造
target:
  id: ent_technology_ethercat_2024
  name:
    en: EtherCAT
    zh: EtherCAT
domains:
  source_domain: 11_applications_markets
  target_domain: 08_software_middleware
description:
  en: Industrial Manufacturing uses EtherCAT.
  zh: 工业制造使用EtherCAT。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 工业制造应用场景使用了EtherCAT技术。 | 证据: - **Agility Digit
    / Figure 02**：采用 NVIDIA Jetson 或类似平台处理多相机感知与导航，下层通过 EtherCAT 或类似总线连接关节驱动器。'
sources:
- id: src_001
  type: other
  title: KG body of ent_application_industrial_manufacturing
  url: https://kg.rounds-tech.com/entry/ent_application_industrial_manufacturing/
  accessed_at: '2026-07-16'
---
