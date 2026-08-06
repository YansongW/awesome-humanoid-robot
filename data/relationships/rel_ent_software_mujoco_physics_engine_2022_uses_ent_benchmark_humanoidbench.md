---
$id: rel_ent_software_mujoco_physics_engine_2022_uses_ent_benchmark_humanoidbench
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
target:
  id: ent_benchmark_humanoidbench
  name:
    en: HumanoidBench
    zh: HumanoidBench
domains:
  source_domain: 08_software_middleware
  target_domain: 07_ai_models_algorithms
description:
  en: MuJoCo Physics Engine uses HumanoidBench.
  zh: MuJoCo 物理引擎使用HumanoidBench。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据说明HumanoidBench以MuJoCo为物理后端，因此MuJoCo被该基准使用。
    | 证据: - **HumanoidBench**（`ent_benchmark_humanoidbench`）：人形机器人全身任务基准，以 MuJoCo 为物理后端；'
sources:
- id: src_001
  type: other
  title: KG body of ent_software_mujoco_physics_engine_2022
  url: https://kg.rounds-tech.com/entry/ent_software_mujoco_physics_engine_2022/
  accessed_at: '2026-08-06'
---
