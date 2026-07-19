---
$id: rel_ent_benchmark_humanoidbench_has_prerequisite_ent_method_sim_to_real
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_benchmark_humanoidbench
  name:
    en: HumanoidBench
    zh: HumanoidBench
target:
  id: ent_method_sim_to_real
  name:
    en: Sim-to-Real Transfer
    zh: Sim-to-Real迁移
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: HumanoidBench has prerequisite Sim-to-Real Transfer.
  zh: HumanoidBench前置依赖Sim-to-Real迁移。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 基准测试用于Sim-to-Real迁移研究，需先理解该概念。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
