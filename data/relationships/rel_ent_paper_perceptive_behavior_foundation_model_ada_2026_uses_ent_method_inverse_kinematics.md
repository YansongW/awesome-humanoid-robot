---
$id: rel_ent_paper_perceptive_behavior_foundation_model_ada_2026_uses_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_perceptive_behavior_foundation_model_ada_2026
  name:
    en: 'Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain'
    zh: 妙动科技 地形感知人形行为基座模型
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: 'Perceptive Behavior Foundation Model: Adapting Human Motion Priors to Robot-Centric Terrain uses Inverse Kinematics.'
  zh: 妙动科技 地形感知人形行为基座模型使用逆运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用多点逆运动学（Inverse Kinematics）来求解腿部关节。 | 证据:
    **Multi-Point Inverse Kinematics**: Solve damped support-aware multi-point Jacobian IK for twelve leg joints, stacking
    ankle, toe, and heel point Jacobians from both feet, including pose preservation, continuity, penetration penalties, and
    damped lea'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_perceptive_behavior_foundation_model_ada_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_perceptive_behavior_foundation_model_ada_2026/
  accessed_at: '2026-08-06'
---
