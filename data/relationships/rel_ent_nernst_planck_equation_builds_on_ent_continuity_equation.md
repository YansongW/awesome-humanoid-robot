---
$id: rel_ent_nernst_planck_equation_builds_on_ent_continuity_equation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: builds_on
source:
  id: ent_nernst_planck_equation
  name:
    en: Nernst-Planck equation
    zh: 能斯特-普朗克方程
target:
  id: ent_continuity_equation
  name:
    en: Continuity equation
    zh: 连续性方程
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Nernst-Planck equation builds on Continuity equation.
  zh: 能斯特-普朗克方程builds_on连续性方程。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 与连续性方程结合，能斯特-普朗克通量给出离子浓度随时间演化的输运方程。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_nernst_planck_equation
  url: https://kg.rounds-tech.com/entry/ent_nernst_planck_equation/
  accessed_at: '2026-07-16'
---
