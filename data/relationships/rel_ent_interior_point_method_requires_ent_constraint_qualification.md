---
$id: rel_ent_interior_point_method_requires_ent_constraint_qualification
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: requires
source:
  id: ent_interior_point_method
  name:
    en: Interior-point method
    zh: 内点法
target:
  id: ent_constraint_qualification
  name:
    en: Constraint qualification
    zh: 约束规范
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Interior-point method requires Constraint qualification.
  zh: 内点法requires约束规范。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 内点法的收敛理论通常假设约束规范，以保证 KKT 系统良态。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_interior_point_method
  url: https://kg.rounds-tech.com/entry/ent_interior_point_method/
  accessed_at: '2026-07-16'
---
