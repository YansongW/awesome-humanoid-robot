---
$id: rel_ent_software_pinocchio_has_prerequisite_ent_foundation_classical_mechanics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
target:
  id: ent_foundation_classical_mechanics
  name:
    en: Classical Mechanics
    zh: 经典力学
domains:
  source_domain: 08_software_middleware
  target_domain: 00_foundations
description:
  en: Pinocchio has prerequisite Classical Mechanics.
  zh: Pinocchio前置依赖经典力学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 经典力学是机器人动力学建模的理论基础，Pinocchio实现这些计算。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
