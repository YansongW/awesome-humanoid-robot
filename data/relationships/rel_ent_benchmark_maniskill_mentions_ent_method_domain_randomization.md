---
$id: rel_ent_benchmark_maniskill_mentions_ent_method_domain_randomization
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_benchmark_maniskill
  name:
    en: ManiSkill
    zh: ManiSkill
target:
  id: ent_method_domain_randomization
  name:
    en: Domain Randomization
    zh: 域随机化
domains:
  source_domain: 10_evaluation_benchmarks
  target_domain: 07_ai_models_algorithms
description:
  en: ManiSkill mentions Domain Randomization.
  zh: ManiSkill提及域随机化。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p4_wiki_ch18. Evidence: 在 Wiki 第 18 章同一小节共现'
sources:
- id: src_001
  type: other
  title: Wiki 第 18 章
  url: https://kg.rounds-tech.com/wiki/chapters/chapter-18/
  accessed_at: '2026-07-16'
---
