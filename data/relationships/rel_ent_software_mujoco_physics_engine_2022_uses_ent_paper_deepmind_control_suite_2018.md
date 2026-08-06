---
$id: rel_ent_software_mujoco_physics_engine_2022_uses_ent_paper_deepmind_control_suite_2018
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
target:
  id: ent_paper_deepmind_control_suite_2018
  name:
    en: DeepMind Control Suite
    zh: DeepMind Control Suite
domains:
  source_domain: 08_software_middleware
  target_domain: 07_ai_models_algorithms
description:
  en: MuJoCo Physics Engine uses DeepMind Control Suite.
  zh: MuJoCo 物理引擎使用DeepMind Control Suite。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据明确说明DeepMind Control Suite建立在MuJoCo上，因此MuJoCo被该基准使用。
    | 证据: - **DeepMind Control Suite**（`ent_paper_deepmind_control_suite_2018`）：建立在 MuJoCo 上的经典连续控制基准，几乎定义了 RL 论文的实验范式；'
sources:
- id: src_001
  type: other
  title: KG body of ent_software_mujoco_physics_engine_2022
  url: https://kg.rounds-tech.com/entry/ent_software_mujoco_physics_engine_2022/
  accessed_at: '2026-08-06'
---
