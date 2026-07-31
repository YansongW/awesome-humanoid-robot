---
$id: rel_ent_robot_system_toddlerbot_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_robot_system_toddlerbot
  name:
    en: ToddlerBot
    zh: ToddlerBot 幼儿机器人
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: ToddlerBot mentions Proximal Policy Optimization (PPO).
  zh: ToddlerBot 幼儿机器人提及近端策略优化（PPO）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 10），含底层控制、RL 训练（MuJoCo / MJX，PPO）、扩散策略训练、真机部署全部代码；不依赖
    ROS。'
sources:
- id: src_001
  type: other
  title: KG body of ent_robot_system_toddlerbot
  url: https://kg.rounds-tech.com/entry/ent_robot_system_toddlerbot/
  accessed_at: '2026-07-31'
---
