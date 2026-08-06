---
$id: rel_ent_paper_amo_adaptive_motion_optimizati_2025_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_amo_adaptive_motion_optimizati_2025
  name:
    en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
    zh: AMO｜超灵巧人形全身控制的自适应运动优化
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 06_design_engineering
  target_domain: 07_ai_models_algorithms
description:
  en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control mentions Proximal Policy Optimization
    (PPO).'
  zh: AMO｜超灵巧人形全身控制的自适应运动优化提及近端策略优化（PPO）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: **下半身RL策略**：IsaacGym并行仿真，PPO训练教师策略（可观测特权信息：真实速度、躯干姿态、高度、脚接触），蒸馏为学生策略（仅真实观测
    + 25步历史）。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_amo_adaptive_motion_optimizati_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_amo_adaptive_motion_optimizati_2025/
  accessed_at: '2026-08-06'
---
