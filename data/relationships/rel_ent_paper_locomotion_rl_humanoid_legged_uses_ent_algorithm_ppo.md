---
$id: rel_ent_paper_locomotion_rl_humanoid_legged_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_locomotion_rl_humanoid_legged
  name:
    en: Locomotion RL（Humanoid / Legged）
    zh: Locomotion RL（Humanoid / Legged）
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Locomotion RL（Humanoid / Legged） uses Proximal Policy Optimization (PPO).
  zh: Locomotion RL（Humanoid / Legged）使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 强化学习 locomotion 通常使用PPO。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_locomotion_rl_humanoid_legged
  url: https://kg.rounds-tech.com/entry/ent_paper_locomotion_rl_humanoid_legged/
  accessed_at: '2026-07-31'
---
