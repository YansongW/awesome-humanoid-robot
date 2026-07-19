---
$id: rel_ent_software_nvidia_isaac_sim_2024_has_prerequisite_ent_software_gazebo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_nvidia_isaac_sim_2024
  name:
    en: NVIDIA Isaac Sim
    zh: NVIDIA Isaac Sim
target:
  id: ent_software_gazebo
  name:
    en: Gazebo
    zh: Gazebo
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: NVIDIA Isaac Sim has prerequisite Gazebo.
  zh: NVIDIA Isaac Sim前置依赖Gazebo。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Gazebo是传统仿真器，Isaac Sim作为更先进的GPU加速仿真器，先理解传统仿真有助于理解其优势。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
