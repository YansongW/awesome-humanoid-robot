---
$id: rel_ent_software_gazebo_has_prerequisite_ent_foundation_classical_mechanics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_gazebo
  name:
    en: Gazebo
    zh: Gazebo
target:
  id: ent_foundation_classical_mechanics
  name:
    en: Classical Mechanics
    zh: 经典力学
domains:
  source_domain: 08_software_middleware
  target_domain: 00_foundations
description:
  en: Gazebo has prerequisite Classical Mechanics.
  zh: Gazebo前置依赖经典力学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 经典力学是物理引擎仿真的基础，Gazebo依赖物理引擎模拟运动。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
