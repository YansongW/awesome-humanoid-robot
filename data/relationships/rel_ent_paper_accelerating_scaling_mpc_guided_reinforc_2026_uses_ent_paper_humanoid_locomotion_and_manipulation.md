---
$id: rel_ent_paper_accelerating_scaling_mpc_guided_reinforc_2026_uses_ent_paper_humanoid_locomotion_and_manipulation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_accelerating_scaling_mpc_guided_reinforc_2026
  name:
    en: Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation
    zh: 面向人形运动与操作的MPC引导强化学习加速扩展
target:
  id: ent_paper_humanoid_locomotion_and_manipulation
  name:
    en: 人形机器人运动与操作
    zh: 人形机器人运动与操作
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Accelerating and Scaling MPC-Guided Reinforcement Learning for Humanoid Locomotion and Manipulation uses 人形机器人运动与操作.
  zh: 面向人形运动与操作的MPC引导强化学习加速扩展使用人形机器人运动与操作。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 本文使用MPC-RL框架，将CD-MPC生成的预测轨迹转化为landmark奖励来引导PPO训练。
    | 证据: 本文提出 MPC-RL 框架，将质心动力学 MPC（CD-MPC）在训练时生成的预测轨迹转化为 landmark 奖励，用于引导 PPO 训练人形机器人运动与操作策略，部署时无需 MPC。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_accelerating_scaling_mpc_guided_reinforc_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_accelerating_scaling_mpc_guided_reinforc_2026/
  accessed_at: '2026-08-06'
---
