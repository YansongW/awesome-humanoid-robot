---
$id: rel_ent_ficks_law_is_prerequisite_for_ent_nernst_planck_equation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_prerequisite_for
source:
  id: ent_ficks_law
  name:
    en: Fick's law
    zh: 菲克定律
target:
  id: ent_nernst_planck_equation
  name:
    en: Nernst-Planck equation
    zh: 能斯特-普朗克方程
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Fick's law is prerequisite for Nernst-Planck equation.
  zh: 菲克定律is_prerequisite_for能斯特-普朗克方程。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 能斯特-普朗克方程在菲克定律基础上增加了电场引起的迁移通量，是其推广。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_ficks_law
  url: https://kg.rounds-tech.com/entry/ent_ficks_law/
  accessed_at: '2026-07-16'
---
