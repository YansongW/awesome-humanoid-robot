---
$id: rel_ent_software_pinocchio_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_pinocchio
  name:
    en: Pinocchio
    zh: Pinocchio
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    zh: 线性代数
domains:
  source_domain: 08_software_middleware
  target_domain: 00_foundations
description:
  en: Pinocchio has prerequisite Linear Algebra.
  zh: Pinocchio前置依赖线性代数。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 线性代数是Pinocchio中刚体动力学和运动学计算的基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
