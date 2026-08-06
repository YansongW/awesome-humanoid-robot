---
$id: rel_ent_paper_reinforcement_prototypical_representatio_2021_mentions_ent_algorithm_sac
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_reinforcement_prototypical_representatio_2021
  name:
    en: Reinforcement Learning with Prototypical Representations
    zh: Reinforcement Learning with Prototypical Representations
target:
  id: ent_algorithm_sac
  name:
    en: Soft Actor-Critic (SAC)
    zh: 软演员-评论家（SAC）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Reinforcement Learning with Prototypical Representations mentions Soft Actor-Critic (SAC).
  zh: Reinforcement Learning with Prototypical Representations提及软演员-评论家（SAC）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 现有方法要么依赖任务奖励驱动表示学习（如 DrQ），导致表示与特定任务绑定，无法跨任务泛化；要么在无奖励时采用自监督目标（如
    CURL、SAC-AE），但缺乏探索信号，在稀疏奖励环境下失效。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_reinforcement_prototypical_representatio_2021
  url: https://kg.rounds-tech.com/entry/ent_paper_reinforcement_prototypical_representatio_2021/
  accessed_at: '2026-08-06'
---
