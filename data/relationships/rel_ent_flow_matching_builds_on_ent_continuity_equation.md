---
$id: rel_ent_flow_matching_builds_on_ent_continuity_equation
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: builds_on
source:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
target:
  id: ent_continuity_equation
  name:
    en: Continuity equation
    zh: 连续性方程
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Flow matching builds on Continuity equation.
  zh: 流匹配builds_on连续性方程。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 流匹配显式构造其概率路径满足连续性方程的向量场。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_flow_matching
  url: https://kg.rounds-tech.com/entry/ent_flow_matching/
  accessed_at: '2026-07-16'
---
