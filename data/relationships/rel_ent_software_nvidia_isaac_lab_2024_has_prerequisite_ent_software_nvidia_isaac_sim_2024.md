---
$id: rel_ent_software_nvidia_isaac_lab_2024_has_prerequisite_ent_software_nvidia_isaac_sim_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_nvidia_isaac_lab_2024
  name:
    en: NVIDIA Isaac Lab
    zh: NVIDIA Isaac Lab
target:
  id: ent_software_nvidia_isaac_sim_2024
  name:
    en: NVIDIA Isaac Sim
    zh: NVIDIA Isaac Sim
domains:
  source_domain: 08_software_middleware
  target_domain: 08_software_middleware
description:
  en: NVIDIA Isaac Lab has prerequisite NVIDIA Isaac Sim.
  zh: NVIDIA Isaac Lab前置依赖NVIDIA Isaac Sim。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Isaac Lab构建在Isaac Sim之上，必须先理解Isaac Sim才能使用Isaac
    Lab。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
