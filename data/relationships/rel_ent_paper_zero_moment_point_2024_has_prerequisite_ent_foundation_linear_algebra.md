---
$id: rel_ent_paper_zero_moment_point_2024_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_paper_zero_moment_point_2024
  name:
    en: Zero Moment Point
    zh: 零力矩点
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    zh: 线性代数
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: Zero Moment Point has prerequisite Linear Algebra.
  zh: 零力矩点前置依赖线性代数。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: ZMP计算涉及坐标变换和矩阵运算，需要线性代数基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
