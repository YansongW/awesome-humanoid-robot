---
$id: rel_ent_paper_rove_unlocking_human_intervent_2026_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_rove_unlocking_human_intervent_2026
  name:
    en: 'ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning'
    zh: ROVE｜通过强化学习解锁人形操作的人类干预
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'ROVE: Unlocking Human Interventions for Humanoid Manipulation via Reinforcement Learning uses Proximal Policy Optimization
    (PPO).'
  zh: ROVE｜通过强化学习解锁人形操作的人类干预使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: ROVE在策略学习阶段使用近端策略优化（PPO）进行强化学习训练。 | 证据: 在策略学习阶段，框架并行采用两条技术路线：一是基于近端策略优化（PPO）的强化学习训练，通过与环境交互不断优化动作策略；二是利用扩散策略或流匹配方法生成平滑、连续的动作轨迹。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_rove_unlocking_human_intervent_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_rove_unlocking_human_intervent_2026/
  accessed_at: '2026-07-16'
---
