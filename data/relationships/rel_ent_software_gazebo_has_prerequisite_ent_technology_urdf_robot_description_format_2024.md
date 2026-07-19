---
$id: rel_ent_software_gazebo_has_prerequisite_ent_technology_urdf_robot_description_format_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_gazebo
  name:
    en: Gazebo
    zh: Gazebo
target:
  id: ent_technology_urdf_robot_description_format_2024
  name:
    en: URDF Robot Description Format
    zh: URDF 机器人描述格式
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: Gazebo has prerequisite URDF Robot Description Format.
  zh: Gazebo前置依赖URDF 机器人描述格式。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: URDF是Gazebo中描述机器人模型的标准格式，必须先理解。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
