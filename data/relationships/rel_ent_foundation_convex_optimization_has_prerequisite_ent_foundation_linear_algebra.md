---
$id: rel_ent_foundation_convex_optimization_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_foundation_convex_optimization
  name:
    en: Convex Optimization
    zh: 凸优化
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    zh: 线性代数
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Convex Optimization has prerequisite Linear Algebra.
  zh: 凸优化前置依赖线性代数。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 凸优化中的向量空间和矩阵运算需要线性代数基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
