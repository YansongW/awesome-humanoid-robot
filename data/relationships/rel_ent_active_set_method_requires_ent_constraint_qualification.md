---
$id: rel_ent_active_set_method_requires_ent_constraint_qualification
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: requires
source:
  id: ent_active_set_method
  name:
    en: Active-set method
    zh: 起作用集法
target:
  id: ent_constraint_qualification
  name:
    en: Constraint qualification
    zh: 约束规范
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Active-set method requires Constraint qualification.
  zh: 起作用集法requires约束规范。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 起作用集 QP 迭代的可靠收敛通常假设工作集上满足 LICQ 等约束规范。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_active_set_method
  url: https://kg.rounds-tech.com/entry/ent_active_set_method/
  accessed_at: '2026-07-16'
---
