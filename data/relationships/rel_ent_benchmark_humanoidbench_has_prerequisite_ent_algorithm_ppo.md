---
$id: rel_ent_benchmark_humanoidbench_has_prerequisite_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_benchmark_humanoidbench
  name:
    en: HumanoidBench
    zh: HumanoidBench
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: HumanoidBench has prerequisite Proximal Policy Optimization (PPO).
  zh: HumanoidBench前置依赖近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 基准测试常使用PPO作为基线算法，需先了解。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
