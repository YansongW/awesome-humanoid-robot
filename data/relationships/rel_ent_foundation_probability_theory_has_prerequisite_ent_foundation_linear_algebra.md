---
$id: rel_ent_foundation_probability_theory_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_foundation_probability_theory
  name:
    en: Probability Theory
    zh: 概率论
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    zh: 线性代数
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Probability Theory has prerequisite Linear Algebra.
  zh: 概率论前置依赖线性代数。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 概率论中的协方差矩阵和随机向量需要线性代数。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
