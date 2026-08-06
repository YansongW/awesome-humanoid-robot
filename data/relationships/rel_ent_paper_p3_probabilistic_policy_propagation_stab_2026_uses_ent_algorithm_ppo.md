---
$id: rel_ent_paper_p3_probabilistic_policy_propagation_stab_2026_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_p3_probabilistic_policy_propagation_stab_2026
  name:
    en: 'P3: Probabilistic Policy Propagation for Stable VAE-Based Robot Learning'
    zh: 'P3: Probabilistic Policy Propagation for Stable VAE-Based Robot Learning'
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'P3: Probabilistic Policy Propagation for Stable VAE-Based Robot Learning uses Proximal Policy Optimization (PPO).'
  zh: 'P3: Probabilistic Policy Propagation for Stable VAE-Based Robot Learning使用近端策略优化（PPO）。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文P3在其方法中使用了PPO算法，并指出了其与随机潜在变量的不匹配问题。 | 证据:
    However, their stochastic latent creates a mismatch with Proximal Policy Optimization (PPO): an effective policy marginalizes
    over the latent distribution, whereas former implementations estimate its probability ratio and KL divergence using only
    one'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_p3_probabilistic_policy_propagation_stab_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_p3_probabilistic_policy_propagation_stab_2026/
  accessed_at: '2026-08-06'
---
