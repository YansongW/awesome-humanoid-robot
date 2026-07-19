---
$id: rel_ent_technology_mjcf_simulation_format_2024_has_prerequisite_ent_software_mujoco_physics_engine_2022
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_technology_mjcf_simulation_format_2024
  name:
    en: MJCF Simulation Format
    zh: MJCF 仿真格式
target:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: MJCF Simulation Format has prerequisite MuJoCo Physics Engine.
  zh: MJCF 仿真格式前置依赖MuJoCo 物理引擎。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: MJCF是MuJoCo的原生格式，必须先理解MuJoCo引擎本身才能有效使用其建模格式。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
