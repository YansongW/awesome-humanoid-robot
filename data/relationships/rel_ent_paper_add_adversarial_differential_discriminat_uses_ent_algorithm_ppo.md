---
$id: rel_ent_paper_add_adversarial_differential_discriminat_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_add_adversarial_differential_discriminat
  name:
    en: 'ADD: Adversarial Differential Discriminator for Physics-Based Character Control'
    zh: 'ADD: Adversarial Differential Discriminator for Physics-Based Character Control'
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'ADD: Adversarial Differential Discriminator for Physics-Based Character Control uses Proximal Policy Optimization (PPO).'
  zh: 'ADD: Adversarial Differential Discriminator for Physics-Based Character Control使用近端策略优化（PPO）。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 对抗性判别器通常与强化学习算法如PPO结合用于物理角色控制。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_add_adversarial_differential_discriminat
  url: https://kg.rounds-tech.com/entry/ent_paper_add_adversarial_differential_discriminat/
  accessed_at: '2026-07-31'
---
