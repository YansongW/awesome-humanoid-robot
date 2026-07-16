---
$id: rel_ent_continuity_equation_is_prerequisite_for_ent_flow_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_prerequisite_for
source:
  id: ent_continuity_equation
  name:
    en: Continuity equation
    zh: 连续性方程
target:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Continuity equation is prerequisite for Flow matching.
  zh: 连续性方程is_prerequisite_for流匹配。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 流匹配按设计构造满足连续性方程的概率路径。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_continuity_equation
  url: https://kg.rounds-tech.com/entry/ent_continuity_equation/
  accessed_at: '2026-07-16'
---
