---
$id: rel_ent_paper_strategy_skill_physics_table_tennis_anim_2024_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_strategy_skill_physics_table_tennis_anim_2024
  name:
    en: Strategy and Skill Learning for Physics-based Table Tennis Animation
    zh: Strategy and Skill Learning for Physics-based Table Tennis Animation
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Strategy and Skill Learning for Physics-based Table Tennis Animation uses Proximal Policy Optimization (PPO).
  zh: Strategy and Skill Learning for Physics-based Table Tennis Animation使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文采用PPO算法作为策略学习框架。 | 证据: - **策略学习框架**：采用近端策略优化（PPO）算法，奖励函数包含击球成功率（+1.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_strategy_skill_physics_table_tennis_anim_2024
  url: https://kg.rounds-tech.com/entry/ent_paper_strategy_skill_physics_table_tennis_anim_2024/
  accessed_at: '2026-07-31'
---
