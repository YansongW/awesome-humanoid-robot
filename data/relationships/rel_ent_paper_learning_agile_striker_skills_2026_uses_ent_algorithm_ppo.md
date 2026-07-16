---
$id: rel_ent_paper_learning_agile_striker_skills_2026_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_learning_agile_striker_skills_2026
  name:
    en: Learning Agile Striker Skills for Humanoid Soccer Robots from Noisy Sensory Input
    zh: 从嘈杂的感官输入中学习人形足球机器人的敏捷前锋技能
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Learning Agile Striker Skills for Humanoid Soccer Robots from Noisy Sensory Input uses Proximal Policy Optimization
    (PPO).
  zh: 从嘈杂的感官输入中学习人形足球机器人的敏捷前锋技能使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用近端策略优化（PPO）算法训练教师策略。 | 证据: 首先，在仿真环境中构建包含完整状态信息的教师策略，该策略利用多视角观测、本体状态序列及仿真交互数据恢复场景与目标表征，并通过近端策略优化（PPO）算法进行训练。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_learning_agile_striker_skills_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_learning_agile_striker_skills_2026/
  accessed_at: '2026-07-16'
---
