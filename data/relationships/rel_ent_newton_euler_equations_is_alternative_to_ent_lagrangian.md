---
$id: rel_ent_newton_euler_equations_is_alternative_to_ent_lagrangian
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_alternative_to
source:
  id: ent_newton_euler_equations
  name:
    en: Newton-Euler equations
    zh: 牛顿-欧拉方程
target:
  id: ent_lagrangian
  name:
    en: Lagrangian
    zh: 拉格朗日量
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Newton-Euler equations is alternative to Lagrangian.
  zh: 牛顿-欧拉方程is_alternative_to拉格朗日量。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 牛顿-欧拉形式与拉格朗日形式对刚体系统等价；前者强调力/力矩平衡，后者强调能量。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_newton_euler_equations
  url: https://kg.rounds-tech.com/entry/ent_newton_euler_equations/
  accessed_at: '2026-07-16'
---
