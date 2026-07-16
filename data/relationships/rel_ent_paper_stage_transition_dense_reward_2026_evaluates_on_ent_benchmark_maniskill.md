---
$id: rel_ent_paper_stage_transition_dense_reward_2026_evaluates_on_ent_benchmark_maniskill
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_stage_transition_dense_reward_2026
  name:
    en: Stage-Transition Dense Reward Modeling for Reinforcement Learning
    zh: Stage-Transition Dense Reward Modeling for Reinforcement Learning
target:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: Stage-Transition Dense Reward Modeling for Reinforcement Learning is evaluated on ManiSkill.
  zh: Stage-Transition Dense Reward Modeling for Reinforcement Learning评测于ManiSkill。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 该论文在ManiSkill基准上进行了实验，以评估其方法。 | 证据: Experiments
    on 14 manipulation tasks across MetaWorld, ManiSkill, and Franka Kitchen show that STDR consistently improves sample efficiency
    and success rates over multiple baselines, and matches or surpasses handcrafted dense rewards on several chall'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_stage_transition_dense_reward_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_stage_transition_dense_reward_2026/
  accessed_at: '2026-07-16'
---
