---
$id: rel_ent_paper_awr_advantage_weighted_regress_2026_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_awr_advantage_weighted_regress_2026
  name:
    en: 'AWR: Advantage Weighted Regression'
    zh: 优势加权回归
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'AWR: Advantage Weighted Regression mentions Proximal Policy Optimization (PPO).'
  zh: 优势加权回归提及近端策略优化（PPO）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 与当时主流的基于重要性采样或信任域约束的算法（如PPO、TRPO）相比，AWR完全摒弃了复杂的裁剪或约束机制，仅通过一个简单的加权回归步骤即可完成策略迭代。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_awr_advantage_weighted_regress_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_awr_advantage_weighted_regress_2026/
  accessed_at: '2026-07-16'
---
