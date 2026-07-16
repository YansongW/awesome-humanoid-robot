---
$id: rel_ent_benchmark_humanoidbench_mentions_ent_concept_world_model
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_benchmark_humanoidbench
  name:
    en: HumanoidBench
    zh: HumanoidBench
target:
  id: ent_concept_world_model
  name:
    en: World Model
    zh: 世界模型
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: HumanoidBench mentions World Model.
  zh: HumanoidBench提及世界模型。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p4_wiki_ch30. Evidence: 在 Wiki 第 30 章同一小节共现'
sources:
- id: src_001
  type: other
  title: Wiki 第 30 章
  url: https://kg.rounds-tech.com/wiki/chapters/chapter-30/
  accessed_at: '2026-07-16'
---
