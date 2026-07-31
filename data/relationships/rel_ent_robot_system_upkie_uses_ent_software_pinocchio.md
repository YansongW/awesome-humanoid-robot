---
$id: rel_ent_robot_system_upkie_uses_ent_software_pinocchio
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_robot_system_upkie
  name:
    en: Upkie Wheeled Biped Robot
    zh: Upkie 轮足双足机器人
target:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
domains:
  source_domain: 02_components
  target_domain: 08_software_middleware
description:
  en: Upkie Wheeled Biped Robot uses Pinocchio.
  zh: Upkie 轮足双足机器人使用Pinocchio。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明Upkie兼容Pinocchio等库，即使用Pinocchio。 | 证据: -
    不依赖 ROS（可用 xacro/URDF 描述，兼容 Pinocchio 等库）。'
sources:
- id: src_001
  type: other
  title: KG body of ent_robot_system_upkie
  url: https://kg.rounds-tech.com/entry/ent_robot_system_upkie/
  accessed_at: '2026-07-31'
---
