---
$id: rel_ent_benchmark_maniskill_has_prerequisite_ent_software_mujoco_physics_engine_2022
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
target:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 08_software_middleware
description:
  en: ManiSkill has prerequisite MuJoCo Physics Engine.
  zh: ManiSkill前置依赖MuJoCo 物理引擎。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: ManiSkill基于MuJoCo，需先熟悉其物理仿真。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
