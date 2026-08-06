---
$id: rel_ent_paper_amo_adaptive_motion_optimizati_2025_1_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_amo_adaptive_motion_optimizati_2025_1
  name:
    en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
    zh: AMO｜超灵巧人形全身控制的自适应运动优化
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 02_components
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
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: 核心贡献有二：一是混合运动合成，融合AMASS数据集的手臂轨迹与概率采样的躯干姿态，经Crocoddyl的BoxFDDP轨迹优化生成满足动力学约束的AMO数据集，消除MoCap方法的“具身差距”；二是可泛化策略训练，通过教师-学生蒸馏（PPO）学习连续映射，支持分布外（O.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_amo_adaptive_motion_optimizati_2025_1
  url: https://kg.rounds-tech.com/entry/ent_paper_amo_adaptive_motion_optimizati_2025_1/
  accessed_at: '2026-08-06'
---
