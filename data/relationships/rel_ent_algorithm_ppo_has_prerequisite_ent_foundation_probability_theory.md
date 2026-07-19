---
$id: rel_ent_algorithm_ppo_has_prerequisite_ent_foundation_probability_theory
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
target:
  id: ent_foundation_probability_theory
  name:
    en: Probability Theory
    zh: 概率论
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: Proximal Policy Optimization (PPO) has prerequisite Probability Theory.
  zh: 近端策略优化（PPO）前置依赖概率论。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: PPO基于策略梯度，需要概率论理解期望和采样。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
