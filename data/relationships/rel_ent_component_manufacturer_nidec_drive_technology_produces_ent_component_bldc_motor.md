---
$id: rel_ent_component_manufacturer_nidec_drive_technology_produces_ent_component_bldc_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: produces
source:
  id: ent_component_manufacturer_nidec_drive_technology
  name:
    en: Nidec Drive Technology
    zh: 尼得科传动技术
target:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    zh: 无刷直流电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Nidec Drive Technology produces Brushless DC Motor.
  zh: 尼得科传动技术生产无刷直流电机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 尼得科更广泛的电机产品组合包括用于机器人执行器的无刷直流电机和精密伺服电机。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_component_manufacturer_nidec_drive_technology
  url: https://kg.rounds-tech.com/entry/ent_component_manufacturer_nidec_drive_technology/
  accessed_at: '2026-07-16'
---
