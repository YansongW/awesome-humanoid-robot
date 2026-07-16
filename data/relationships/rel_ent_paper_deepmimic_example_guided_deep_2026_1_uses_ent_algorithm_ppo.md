---
$id: rel_ent_paper_deepmimic_example_guided_deep_2026_1_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_deepmimic_example_guided_deep_2026_1
  name:
    en: 'DeepMimic: Example-Guided Deep RL of Physics-Based Character Skills'
    zh: 深度模仿：基于示例引导的物理角色技能深度强化学习
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'DeepMimic: Example-Guided Deep RL of Physics-Based Character Skills uses Proximal Policy Optimization (PPO).'
  zh: 深度模仿：基于示例引导的物理角色技能深度强化学习使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据明确说明该算法采用PPO作为基础优化器。 | 证据: 该算法采用近端策略优化（PPO）作为基础优化器，并引入一个由运动示例数据驱动的奖励函数。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_deepmimic_example_guided_deep_2026_1
  url: https://kg.rounds-tech.com/entry/ent_paper_deepmimic_example_guided_deep_2026_1/
  accessed_at: '2026-07-16'
---
