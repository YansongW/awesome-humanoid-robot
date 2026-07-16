---
$id: rel_ent_constraint_qualification_is_prerequisite_for_ent_active_set_method
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_prerequisite_for
source:
  id: ent_constraint_qualification
  name:
    en: Constraint qualification
    zh: 约束规范
target:
  id: ent_active_set_method
  name:
    en: Active-set method
    zh: 起作用集法
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Constraint qualification is prerequisite for Active-set method.
  zh: 约束规范is_prerequisite_for起作用集法。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 起作用集方法利用起作用约束集合，其梯度需满足约束规范以保证迭代可靠。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_constraint_qualification
  url: https://kg.rounds-tech.com/entry/ent_constraint_qualification/
  accessed_at: '2026-07-16'
---
