---
$id: rel_ent_paper_guidewalk_learning_unified_aut_2026_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_guidewalk_learning_unified_aut_2026
  name:
    en: 'GuideWalk: Learning Unified Autonomous Navigation and Locomotion for Humanoid Robots across Versatile Terrains'
    zh: 把可通过性感知的导航规划与地形自适应运动控制用复合教师蒸馏成统一策略，再经 RL+行为克隆微调，在楼梯/斜坡/窄梁上既避障又稳步
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'GuideWalk: Learning Unified Autonomous Navigation and Locomotion for Humanoid Robots across Versatile Terrains uses
    Proximal Policy Optimization (PPO).'
  zh: 把可通过性感知的导航规划与地形自适应运动控制用复合教师蒸馏成统一策略，再经 RL+行为克隆微调，在楼梯/斜坡/窄梁上既避障又稳步使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 论文使用PPO算法进行强化学习微调'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_guidewalk_learning_unified_aut_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_guidewalk_learning_unified_aut_2026/
  accessed_at: '2026-07-16'
---
