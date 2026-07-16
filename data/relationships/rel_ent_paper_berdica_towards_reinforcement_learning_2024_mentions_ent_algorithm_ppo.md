---
$id: rel_ent_paper_berdica_towards_reinforcement_learning_2024_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_berdica_towards_reinforcement_learning_2024
  name:
    en: Towards Reinforcement Learning Controllers for Soft Robots using Learned Environments
    zh: 基于学习环境的软体机器人强化学习控制器研究
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Towards Reinforcement Learning Controllers for Soft Robots using Learned Environments mentions Proximal Policy Optimization
    (PPO).
  zh: 基于学习环境的软体机器人强化学习控制器研究提及近端策略优化（PPO）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: This paper presents a model-based reinforcement
    learning pipeline for soft pneumatic manipulators that learns a recurrent forward-dynamics model from safe actuation-space
    exploration and trains PPO actor-critic policies inside a parallel JAX/Gymnax learned environment on GPU.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_berdica_towards_reinforcement_learning_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_berdica_towards_reinforcement_learning_2024/
  accessed_at: '2026-07-16'
---
