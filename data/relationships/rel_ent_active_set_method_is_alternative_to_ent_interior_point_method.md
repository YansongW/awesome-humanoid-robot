---
$id: rel_ent_active_set_method_is_alternative_to_ent_interior_point_method
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_alternative_to
source:
  id: ent_active_set_method
  name:
    en: Active-set method
    zh: 起作用集法
target:
  id: ent_interior_point_method
  name:
    en: Interior-point method
    zh: 内点法
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Active-set method is alternative to Interior-point method.
  zh: 起作用集法is_alternative_to内点法。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 内点法通过始终严格位于可行域内部来求解同一类约束问题，而非追踪起作用集。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_active_set_method
  url: https://kg.rounds-tech.com/entry/ent_active_set_method/
  accessed_at: '2026-07-16'
---
