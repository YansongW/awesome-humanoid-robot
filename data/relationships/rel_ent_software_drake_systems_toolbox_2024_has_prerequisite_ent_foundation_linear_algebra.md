---
$id: rel_ent_software_drake_systems_toolbox_2024_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_software_drake_systems_toolbox_2024
  name:
    en: Drake Systems Toolbox
    zh: Drake 系统工具箱
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    zh: 线性代数
domains:
  source_domain: 08_software_middleware
  target_domain: 00_foundations
description:
  en: Drake Systems Toolbox has prerequisite Linear Algebra.
  zh: Drake 系统工具箱前置依赖线性代数。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 线性代数是优化和控制理论的基础，Drake工具箱大量依赖矩阵运算。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
