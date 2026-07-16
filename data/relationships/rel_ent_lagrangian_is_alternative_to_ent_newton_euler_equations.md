---
$id: rel_ent_lagrangian_is_alternative_to_ent_newton_euler_equations
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_alternative_to
source:
  id: ent_lagrangian
  name:
    en: Lagrangian
    zh: 拉格朗日量
target:
  id: ent_newton_euler_equations
  name:
    en: Newton-Euler equations
    zh: 牛顿-欧拉方程
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Lagrangian is alternative to Newton-Euler equations.
  zh: 拉格朗日量is_alternative_to牛顿-欧拉方程。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 牛顿-欧拉方程与拉格朗日形式对刚体系统给出相同动力学，但直接通过力与力矩平衡列写。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_lagrangian
  url: https://kg.rounds-tech.com/entry/ent_lagrangian/
  accessed_at: '2026-07-16'
---
