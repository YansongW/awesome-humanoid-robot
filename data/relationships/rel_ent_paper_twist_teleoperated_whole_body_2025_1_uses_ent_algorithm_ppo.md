---
$id: rel_ent_paper_twist_teleoperated_whole_body_2025_1_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_twist_teleoperated_whole_body_2025_1
  name:
    en: 'TWIST: Teleoperated Whole-Body Imitation System'
    zh: TWIST｜遥控全身模仿系统
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 09_data_datasets
  target_domain: 07_ai_models_algorithms
description:
  en: 'TWIST: Teleoperated Whole-Body Imitation System uses Proximal Policy Optimization (PPO).'
  zh: TWIST｜遥控全身模仿系统使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: TWIST系统采用近端策略优化（PPO）进行初步训练。 | 证据: 在此基础上，系统采用近端策略优化（PPO）与强化学习（RL）策略进行初步训练，再通过行为克隆（ACT）与模仿学习对动作序列进行精细化调整，最终输出可复用的全身轨迹与低层控制器目标。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_twist_teleoperated_whole_body_2025_1
  url: https://kg.rounds-tech.com/entry/ent_paper_twist_teleoperated_whole_body_2025_1/
  accessed_at: '2026-07-16'
---
