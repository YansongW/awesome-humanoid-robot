---
$id: rel_ent_company_leaderdrive_2024_has_prerequisite_ent_component_harmonic_drive_reducer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_company_leaderdrive_2024
  name:
    en: Leaderdrive
    zh: 绿的谐波
target:
  id: ent_component_harmonic_drive_reducer
  name:
    en: Harmonic Drive Reducer
    zh: 谐波减速器
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Leaderdrive has prerequisite Harmonic Drive Reducer.
  zh: 绿的谐波前置依赖谐波减速器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Leaderdrive是谐波减速器制造商，需先了解该产品。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
