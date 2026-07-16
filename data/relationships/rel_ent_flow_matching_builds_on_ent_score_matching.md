---
$id: rel_ent_flow_matching_builds_on_ent_score_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: builds_on
source:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
target:
  id: ent_score_matching
  name:
    en: Score matching
    zh: 分数匹配
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Flow matching builds on Score matching.
  zh: 流匹配builds_on分数匹配。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 与分数匹配类似，流匹配也学习数据空间上的向量场，但它直接回归速度而非分数。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_flow_matching
  url: https://kg.rounds-tech.com/entry/ent_flow_matching/
  accessed_at: '2026-07-16'
---
