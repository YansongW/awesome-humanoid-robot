---
$id: rel_ent_constraint_qualification_is_prerequisite_for_ent_interior_point_method
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_prerequisite_for
source:
  id: ent_constraint_qualification
  name:
    en: Constraint qualification
    zh: 约束规范
target:
  id: ent_interior_point_method
  name:
    en: Interior-point method
    zh: 内点法
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Constraint qualification is prerequisite for Interior-point method.
  zh: 约束规范is_prerequisite_for内点法。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 内点法保持严格不等式可行性，因此隐式依赖约束规范以保证收敛到 KKT 点。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_constraint_qualification
  url: https://kg.rounds-tech.com/entry/ent_constraint_qualification/
  accessed_at: '2026-07-16'
---
