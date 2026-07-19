---
$id: rel_ent_software_nvidia_isaac_lab_2024_has_prerequisite_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_nvidia_isaac_lab_2024
  name:
    en: NVIDIA Isaac Lab
    zh: NVIDIA Isaac Lab
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 08_software_middleware
  target_domain: 07_ai_models_algorithms
description:
  en: NVIDIA Isaac Lab has prerequisite Proximal Policy Optimization (PPO).
  zh: NVIDIA Isaac Lab前置依赖近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: PPO是Isaac Lab中常用的强化学习算法，必须先理解。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
