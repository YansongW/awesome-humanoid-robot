---
$id: rel_ent_component_harmonic_drive_reducer_has_prerequisite_ent_foundation_classical_mechanics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_harmonic_drive_reducer
  name:
    en: Harmonic Drive Reducer
    zh: 谐波减速器
target:
  id: ent_foundation_classical_mechanics
  name:
    en: Classical Mechanics
    zh: 经典力学
domains:
  source_domain: 02_components
  target_domain: 00_foundations
description:
  en: Harmonic Drive Reducer has prerequisite Classical Mechanics.
  zh: 谐波减速器前置依赖经典力学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 理解齿轮传动、扭矩和速度的物理原理是学习减速器的基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
