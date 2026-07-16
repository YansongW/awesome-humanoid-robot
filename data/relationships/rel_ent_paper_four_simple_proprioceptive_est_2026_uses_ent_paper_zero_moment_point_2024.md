---
$id: rel_ent_paper_four_simple_proprioceptive_est_2026_uses_ent_paper_zero_moment_point_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_four_simple_proprioceptive_est_2026
  name:
    en: Four Simple Proprioceptive Estimators for Legged Robots
    zh: Four Simple Proprioceptive Estimators for Legged Robots
target:
  id: ent_paper_zero_moment_point_2024
  name:
    en: Zero Moment Point
    zh: 零力矩点
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Four Simple Proprioceptive Estimators for Legged Robots uses Zero Moment Point.
  zh: Four Simple Proprioceptive Estimators for Legged Robots使用零力矩点。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用零力矩点（ZMP）方法推导地面反作用力。 | 证据: These estimators
    employ physics-based analytical or filtering methods, such as using joint kinematics and IMU data fused via an Extended
    Kalman Filter (EKF) to estimate body posture, and deriving ground reaction forces and the Zero Moment Point (ZMP)'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_four_simple_proprioceptive_est_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_four_simple_proprioceptive_est_2026/
  accessed_at: '2026-07-16'
---
