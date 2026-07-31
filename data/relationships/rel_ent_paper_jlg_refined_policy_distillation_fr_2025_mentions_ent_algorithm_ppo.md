---
$id: rel_ent_paper_jlg_refined_policy_distillation_fr_2025_mentions_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_paper_jlg_refined_policy_distillation_fr_2025
  name:
    en: 'Refined Policy Distillation: From VLA Generalists to RL Experts'
    zh: RPD
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'Refined Policy Distillation: From VLA Generalists to RL Experts mentions Proximal Policy Optimization (PPO).'
  zh: RPD提及近端策略优化（PPO）。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p5b_acronym. Evidence: - **训练流程**：学生策略在环境中执行动作，教师VLA提供参考动作作为行为克隆的监督信号；强化学习部分使用PPO算法优化策略，行为克隆部分使用均方误差损失对齐学生与教师动作。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_jlg_refined_policy_distillation_fr_2025
  url: https://kg.rounds-tech.com/entry/ent_paper_jlg_refined_policy_distillation_fr_2025/
  accessed_at: '2026-07-31'
---
