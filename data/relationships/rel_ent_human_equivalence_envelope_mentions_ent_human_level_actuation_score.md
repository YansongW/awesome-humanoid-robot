---
$id: rel_ent_human_equivalence_envelope_mentions_ent_human_level_actuation_score
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_human_equivalence_envelope
  name:
    en: Human-Equivalence Envelope
    zh: 人等效包络
target:
  id: ent_human_level_actuation_score
  name:
    en: Human-Level Actuation Score
    zh: 类人驱动评分
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 10_evaluation_benchmarks
description:
  en: Human-Equivalence Envelope mentions Human-Level Actuation Score.
  zh: 人等效包络提及类人驱动评分。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p4_wiki_ch25. Evidence: 在 Wiki 第 25 章同一小节共现'
sources:
- id: src_001
  type: other
  title: Wiki 第 25 章
  url: https://kg.rounds-tech.com/wiki/chapters/chapter-25/
  accessed_at: '2026-07-16'
---
