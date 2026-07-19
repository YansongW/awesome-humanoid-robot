---
$id: rel_ent_benchmark_libero_has_prerequisite_ent_benchmark_maniskill
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_benchmark_libero
  name:
    en: LIBERO
    zh: LIBERO
target:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
domains:
  source_domain: 09_data_datasets
  target_domain: 10_evaluation_benchmarks
description:
  en: LIBERO has prerequisite ManiSkill.
  zh: LIBERO前置依赖ManiSkill。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: LIBERO是操作基准测试的进阶，ManiSkill提供了更基础的评估框架。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
