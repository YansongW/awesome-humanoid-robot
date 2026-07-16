---
$id: rel_ent_paper_four_simple_proprioceptive_est_2026_uses_ent_principle_zero_moment_point
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_four_simple_proprioceptive_est_2026
  name:
    en: Four Simple Proprioceptive Estimators for Legged Robots
    zh: Four Simple Proprioceptive Estimators for Legged Robots
target:
  id: ent_principle_zero_moment_point
  name:
    en: Zero Moment Point (ZMP)
    zh: 零力矩点（ZMP）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: Four Simple Proprioceptive Estimators for Legged Robots uses Zero Moment Point (ZMP).
  zh: Four Simple Proprioceptive Estimators for Legged Robots使用零力矩点（ZMP）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用零力矩点（ZMP）原理来推导地面反作用力。 | 证据: 这些估计器均采用基于物理模型的解析或滤波方法，例如利用关节运动学与IMU数据通过扩展卡尔曼滤波（EKF）融合估计身体姿态，以及通过足底接触力与关节力矩的平衡关系推导地面反作用力与零力矩点（ZMP）。'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_four_simple_proprioceptive_est_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_four_simple_proprioceptive_est_2026/
  accessed_at: '2026-07-16'
---
