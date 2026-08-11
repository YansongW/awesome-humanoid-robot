---
$id: rel_ent_paper_lift_towards_bridging_the_gap_2026_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_lift_towards_bridging_the_gap_2026
  name:
    en: 'LIFT: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control'
    zh: LIFT：用大批量 SAC 预训练 + 物理先验世界模型微调，把人形 sim-to-real 压到 1 小时
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control mentions Proximal
    Policy Optimization (PPO).
  zh: Towards Bridging the Gap between Large-Scale Pretraining and Efficient Finetuning for Humanoid Control提及近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中仅提及PPO是一种用于人形控制的强化学习方法，并未表明源论文使用或基于PPO。 |
    证据: Reinforcement learning (RL) is widely used for humanoid control, with on-policy methods such as Proximal Policy Optimization
    (PPO) enabling robust training via large-scale parallel simulation and, in some cases, zero-shot deployment to real robots.
    | WP3 2026-08-06: endpoint rewritten (ent_paper_lift_towards_bridging_the_gap_2026→ent_paper_lift_towards_bridging_the_gap_2026,
    ent_algorithm_ppo→ent_algorithm_ppo) after merge. Original file rel_ent_paper_towards_bridging_the_gap_betwe_2026_mentions_ent_algorithm_ppo.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_lift_towards_bridging_the_gap_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_lift_towards_bridging_the_gap_2026/
  accessed_at: '2026-07-16'
---
