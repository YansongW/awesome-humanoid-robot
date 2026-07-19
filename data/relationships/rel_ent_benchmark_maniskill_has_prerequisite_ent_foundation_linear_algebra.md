---
$id: rel_ent_benchmark_maniskill_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    zh: 线性代数
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 00_foundations
description:
  en: ManiSkill has prerequisite Linear Algebra.
  zh: ManiSkill前置依赖线性代数。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 操作任务中的运动学和动力学计算依赖线性代数。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
