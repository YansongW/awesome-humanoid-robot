---
$id: rel_ent_robot_system_upkie_has_prerequisite_ent_software_mujoco_physics_engine_2022
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_upkie
  name:
    en: Upkie Wheeled Biped Robot
    zh: Upkie 轮足双足机器人
target:
  id: ent_software_mujoco_physics_engine_2022
  name:
    en: MuJoCo Physics Engine
    zh: MuJoCo 物理引擎
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: Upkie Wheeled Biped Robot has prerequisite MuJoCo Physics Engine.
  zh: Upkie 轮足双足机器人前置依赖MuJoCo 物理引擎。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: MuJoCo是基础物理引擎，用于仿真轮式双足机器人Upkie的动力学。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
