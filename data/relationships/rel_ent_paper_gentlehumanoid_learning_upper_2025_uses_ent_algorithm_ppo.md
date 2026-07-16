---
$id: rel_ent_paper_gentlehumanoid_learning_upper_2025_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_gentlehumanoid_learning_upper_2025
  name:
    en: 'GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction'
    zh: GentleHumanoid｜学习上半身顺应性以进行丰富的人与物交互
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'GentleHumanoid: Learning Upper-body Compliance for Contact-rich Human and Object Interaction uses Proximal Policy Optimization
    (PPO).'
  zh: GentleHumanoid｜学习上半身顺应性以进行丰富的人与物交互使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文说明高层语义信息被输入至基于近端策略优化（PPO）的强化学习策略网络，表明使用了该算法。
    | 证据: 随后，这些高层语义信息被输入至一个基于近端策略优化（PPO）的强化学习策略网络，该网络负责生成末端执行器（腕手）的期望目标位姿与力/力矩指令。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_gentlehumanoid_learning_upper_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_gentlehumanoid_learning_upper_2025/
  accessed_at: '2026-07-16'
---
