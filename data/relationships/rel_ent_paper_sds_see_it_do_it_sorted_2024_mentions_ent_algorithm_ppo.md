---
$id: rel_ent_paper_sds_see_it_do_it_sorted_2024_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_sds_see_it_do_it_sorted_2024
  name:
    en: 'SDS -- See it, Do it, Sorted: Quadruped Skill Synthesis from Single Video Demonstration'
    zh: 'SDS -- See it, Do it, Sorted: Quadruped Skill Synthesis from Single Video Demonstration'
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'SDS -- See it, Do it, Sorted: Quadruped Skill Synthesis from Single Video Demonstration mentions Proximal Policy Optimization
    (PPO).'
  zh: 'SDS -- See it, Do it, Sorted: Quadruped Skill Synthesis from Single Video Demonstration提及近端策略优化（PPO）。'
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 该方法采用时空网格视觉编码（$G_{v}$）对视频帧进行结构化分解，再通过结构化输入分解（SUS）生成奖励函数，随后利用PPO算法训练策略，并通过闭环进化机制（以训练录像和性能指标为自监督信号）持续优化奖励函数。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_sds_see_it_do_it_sorted_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_sds_see_it_do_it_sorted_2024/
  accessed_at: '2026-07-31'
---
