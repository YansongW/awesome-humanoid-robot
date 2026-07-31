---
$id: rel_ent_paper_deepmind_control_suite_2018_uses_ent_software_mujoco_physics_engine_2022
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_deepmind_control_suite_2018
  name:
    en: DeepMind Control Suite
    zh: DeepMind Control Suite
target:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 08_software_middleware
description:
  en: DeepMind Control Suite uses MuJoCo Physics Engine.
  zh: DeepMind Control Suite使用MuJoCo 物理引擎。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: DeepMind Control Suite的所有任务都依托MuJoCo物理引擎运行。
    | 证据: DeepMind Control Suite 是一套专为强化学习研究设计的连续控制任务库，所有任务均采用 Python 编写并依托 MuJoCo 物理引擎运行，确保了易用性和可修改性。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_deepmind_control_suite_2018
  url: https://kg.rounds-tech.com/entry/ent_paper_deepmind_control_suite_2018/
  accessed_at: '2026-07-31'
---
