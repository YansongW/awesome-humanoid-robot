---
$id: rel_ent_software_mujoco_physics_engine_2022_has_prerequisite_ent_foundation_classical_mechanics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
target:
  id: ent_foundation_classical_mechanics
  name:
    en: Classical Mechanics
    zh: 经典力学
domains:
  source_domain: 08_software_middleware
  target_domain: 00_foundations
description:
  en: MuJoCo Physics Engine has prerequisite Classical Mechanics.
  zh: MuJoCo 物理引擎前置依赖经典力学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 经典力学是MuJoCo物理引擎仿真动力学的基础理论。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
