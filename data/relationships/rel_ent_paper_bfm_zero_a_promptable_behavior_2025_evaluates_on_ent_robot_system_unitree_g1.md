---
$id: rel_ent_paper_bfm_zero_a_promptable_behavior_2025_evaluates_on_ent_robot_system_unitree_g1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_bfm_zero_a_promptable_behavior_2025
  name:
    en: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning'
    zh: BFM-Zero｜使用无监督强化学习的人形控制的即时行为基础模型
target:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1 Humanoid Robot
    zh: Unitree G1 人形机器人
domains:
  source_domain: 06_design_engineering
  target_domain: 02_components
description:
  en: 'BFM-Zero: A Promptable Behavioral Foundation Model for Humanoid Control Using Unsupervised Reinforcement Learning is
    evaluated on Unitree G1 Humanoid Robot.'
  zh: BFM-Zero｜使用无监督强化学习的人形控制的即时行为基础模型评测于Unitree G1 人形机器人。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明源论文在Unitree G1人形机器人上进行真实世界实验，因此在该机器人上评估。
    | 证据: 在 Unitree G1 人形机器人上的真实世界实验中，BFM-Zero 展示了零样本运动跟踪、目标到达和奖励优化等多样化能力，并通过少量样本的优化实现自适应。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_bfm_zero_a_promptable_behavior_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_bfm_zero_a_promptable_behavior_2025/
  accessed_at: '2026-07-31'
---
