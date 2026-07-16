---
$id: rel_ent_paper_hiwet_hierarchical_world_frame_2026_1_uses_ent_algorithm_ppo
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_hiwet_hierarchical_world_frame_2026_1
  name:
    en: 'HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid Loco-Manipulation'
    zh: HiWET｜用于长时程人形移动操作的分层世界坐标系末端执行器跟踪
target:
  id: ent_algorithm_ppo
  name:
    en: Proximal Policy Optimization (PPO)
    zh: 近端策略优化（PPO）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: 'HiWET: Hierarchical World-Frame End-Effector Tracking for Long-Horizon Humanoid Loco-Manipulation uses Proximal Policy
    Optimization (PPO).'
  zh: HiWET｜用于长时程人形移动操作的分层世界坐标系末端执行器跟踪使用近端策略优化（PPO）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: HiWET论文中明确提到中层采用基于近端策略优化（PPO）的强化学习策略训练。 | 证据:
    中层采用基于近端策略优化（PPO）的强化学习策略训练，生成末端执行器或腕手目标的位置与姿态。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_hiwet_hierarchical_world_frame_2026_1
  url: https://kg.rounds-tech.com/entry/ent_paper_hiwet_hierarchical_world_frame_2026_1/
  accessed_at: '2026-07-16'
---
