---
$id: rel_ent_software_nvidia_isaac_sim_2024_has_prerequisite_ent_component_nvidia_jetson_agx_orin_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_nvidia_isaac_sim_2024
  name:
    en: NVIDIA Isaac Sim
    zh: NVIDIA Isaac Sim
target:
  id: ent_component_nvidia_jetson_agx_orin_2024
  name:
    en: NVIDIA Jetson AGX Orin
    zh: NVIDIA Jetson AGX Orin
domains:
  source_domain: 08_software_middleware
  target_domain: 02_components
description:
  en: NVIDIA Isaac Sim has prerequisite NVIDIA Jetson AGX Orin.
  zh: NVIDIA Isaac Sim前置依赖NVIDIA Jetson AGX Orin。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: NVIDIA Jetson AGX Orin是运行Isaac Sim的常见硬件平台，理解其能力有助于仿真部署。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
