---
$id: rel_ent_paper_humanoid_manipulation_interfac_2026_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_humanoid_manipulation_interfac_2026
  name:
    en: 'Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations'
    zh: 人形操作接口｜基于机器人无关示范的人形全身操作
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'Humanoid Manipulation Interface: Humanoid Whole-Body Manipulation from Robot-Free Demonstrations uses Proximal Policy
    Optimization (PPO).'
  zh: 人形操作接口｜基于机器人无关示范的人形全身操作使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文底层采用近端策略优化（PPO）算法来学习全身轨迹。 | 证据: 底层采用近端策略优化（PPO）或强化学习（RL）策略，从原始传感器数据中学习全身轨迹与动作序列；中层则引入分层技能与专家策略，将连续动作空间离散化为可复用的技能单元，例如“抓取”、“行走”、“平衡调整”等。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_humanoid_manipulation_interfac_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_humanoid_manipulation_interfac_2026/
  accessed_at: '2026-07-16'
---
