---
$id: rel_ent_paper_rapid_locomotion_reinforcement_2022_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_rapid_locomotion_reinforcement_2022
  name:
    en: Rapid Locomotion via Reinforcement Learning
    zh: Rapid Locomotion via Reinforcement Learning
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Rapid Locomotion via Reinforcement Learning mentions Proximal Policy Optimization (PPO).
  zh: Rapid Locomotion via Reinforcement Learning提及近端策略优化（PPO）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - 教师 πT(x_t, d_t) = π_{θb}(x_t, g_{θd}(d_t))：编码器
    g_{θd} 将 12 维域参数 d_t（质量、质心、摩擦、电机强度等）压缩为 8 维潜变量 z_t，策略主体 π_{θb} 据此输出动作，用 PPO 联合优化。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_rapid_locomotion_reinforcement_2022
  url: https://kg.rounds-tech.com/entry/ent_paper_rapid_locomotion_reinforcement_2022/
  accessed_at: '2026-08-06'
---
