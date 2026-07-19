---
$id: rel_ent_software_nvidia_isaac_sim_2024_has_prerequisite_ent_technology_urdf_robot_description_format_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_nvidia_isaac_sim_2024
  name:
    en: NVIDIA Isaac Sim
    zh: NVIDIA Isaac Sim
target:
  id: ent_technology_urdf_robot_description_format_2024
  name:
    en: URDF Robot Description Format
    zh: URDF 机器人描述格式
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: NVIDIA Isaac Sim has prerequisite URDF Robot Description Format.
  zh: NVIDIA Isaac Sim前置依赖URDF 机器人描述格式。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: URDF是机器人描述标准格式，Isaac Sim也支持导入URDF模型。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
