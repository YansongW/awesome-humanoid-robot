---
$id: rel_ent_score_matching_builds_on_ent_flow_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: builds_on
source:
  id: ent_score_matching
  name:
    en: Score matching
    zh: 分数匹配
target:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
domains:
  source_domain: 00_foundations
  target_domain: 00_foundations
description:
  en: Score matching builds on Flow matching.
  zh: 分数匹配builds_on流匹配。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p0b_related_entities. Evidence: 分数匹配与流匹配都学习引导样本在分布间转移的向量场，但流匹配直接回归速度场。'
sources:
- id: src_001
  type: other
  title: KG frontmatter of ent_score_matching
  url: https://kg.rounds-tech.com/entry/ent_score_matching/
  accessed_at: '2026-07-16'
---
