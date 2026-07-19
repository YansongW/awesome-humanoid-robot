---
$id: rel_ent_company_maxon_group_2024_has_prerequisite_ent_component_bldc_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_company_maxon_group_2024
  name:
    en: Maxon Group
    zh: Maxon
target:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    zh: 无刷直流电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Maxon Group has prerequisite Brushless DC Motor.
  zh: Maxon前置依赖无刷直流电机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Maxon主要生产BLDC电机，需先理解其基本原理。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
