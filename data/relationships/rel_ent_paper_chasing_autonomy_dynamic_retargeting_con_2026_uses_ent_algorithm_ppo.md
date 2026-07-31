---
$id: rel_ent_paper_chasing_autonomy_dynamic_retargeting_con_2026_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_chasing_autonomy_dynamic_retargeting_con_2026
  name:
    en: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running'
    zh: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running'
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running uses Proximal
    Policy Optimization (PPO).'
  zh: 'Chasing Autonomy: Dynamic Retargeting and Control Guided RL for Performant and Controllable Humanoid Running使用近端策略优化（PPO）。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明该论文使用PPO算法来训练策略网络。 | 证据: - **控制策略**：基于Proximal
    Policy Optimization (PPO) 算法训练策略网络，输入包含机器人本体感知（关节位置/速度、IMU数据）与速度指令'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_chasing_autonomy_dynamic_retargeting_con_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_chasing_autonomy_dynamic_retargeting_con_2026/
  accessed_at: '2026-07-31'
---
