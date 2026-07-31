---
$id: rel_ent_paper_ultra_unified_multimodal_contr_2026_evaluates_on_ent_robot_system_unitree_g1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: evaluates_on
source:
  id: ent_paper_ultra_unified_multimodal_contr_2026
  name:
    en: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation'
    zh: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation'
target:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1 Humanoid Robot
    zh: Unitree G1 人形机器人
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 02_components
description:
  en: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation is evaluated on Unitree G1 Humanoid
    Robot.'
  zh: 'ULTRA: Unified Multimodal Control for Autonomous Humanoid Whole-Body Loco-Manipulation评测于Unitree G1 人形机器人。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: ULTRA在仿真与真实Unitree G1人形机器人上进行了评估。 | 证据: ULTRA
    在仿真与真实 Unitree G1 人形机器人上进行了评估，结果表明其能够从自我中心感知出发，泛化至自主、目标导向的全身移动操作任务，性能持续优于仅依赖有限技能的跟踪基线。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_ultra_unified_multimodal_contr_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_ultra_unified_multimodal_contr_2026/
  accessed_at: '2026-07-31'
---
