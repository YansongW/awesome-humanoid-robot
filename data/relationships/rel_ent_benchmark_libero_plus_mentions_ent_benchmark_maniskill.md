---
$id: rel_ent_benchmark_libero_plus_mentions_ent_benchmark_maniskill
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_benchmark_libero_plus
  name:
    en: LIBERO-Plus
    zh: LIBERO-Plus
target:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 10_evaluation_benchmarks
description:
  en: LIBERO-Plus mentions ManiSkill.
  zh: LIBERO-Plus提及ManiSkill。
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
