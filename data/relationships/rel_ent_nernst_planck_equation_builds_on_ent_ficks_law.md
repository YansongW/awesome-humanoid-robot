---
$id: rel_ent_nernst_planck_equation_builds_on_ent_ficks_law
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: builds_on
source:
  id: ent_nernst_planck_equation
  name:
    en: Nernst-Planck equation
    zh: 能斯特-普朗克方程
target:
  id: ent_ficks_law
  name:
    en: Fick's law
    zh: 菲克定律
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Nernst-Planck equation builds on Fick's law.
  zh: 能斯特-普朗克方程builds_on菲克定律。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 能斯特-普朗克通量在菲克定律基础上增加了电迁移项。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_nernst_planck_equation
  url: https://kg.rounds-tech.com/entry/ent_nernst_planck_equation/
  accessed_at: '2026-07-16'
---
