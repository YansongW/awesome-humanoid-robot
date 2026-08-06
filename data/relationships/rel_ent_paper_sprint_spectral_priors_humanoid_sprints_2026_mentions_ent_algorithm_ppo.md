---
$id: rel_ent_paper_sprint_spectral_priors_humanoid_sprints_2026_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_sprint_spectral_priors_humanoid_sprints_2026
  name:
    en: 'SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints'
    zh: 'SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints'
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints mentions Proximal Policy Optimization (PPO).'
  zh: 'SPRINT: Efficient Spectral Priors for Humanoid Athletic Sprints提及近端策略优化（PPO）。'
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - **POMDP + PPO**：非对称 Actor-Critic（AAC），actor
    仅用本体感觉（角速度、投影重力、命令、关节运动学、先前残差），critic 用特权状态（线性速度 + 频谱参考轨迹）。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_sprint_spectral_priors_humanoid_sprints_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_sprint_spectral_priors_humanoid_sprints_2026/
  accessed_at: '2026-08-06'
---
