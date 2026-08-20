---
$id: rel_ent_method_domain_randomization_mentions_ent_method_action_chunking_transformer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_method_domain_randomization
  name:
    en: Domain Randomization
    zh: 域随机化
target:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Domain Randomization mentions Action Chunking with Transformers.
  zh: 域随机化提及基于Transformer的动作分块。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p4_wiki_ch18. Evidence: 在 Wiki 第 18 章同一小节共现 | WP4 2026-08-11: endpoint
    id rewritten (ent_method_domain_randomization→ent_method_domain_randomization, ent_method_action_chunking_transformer→ent_method_action_chunking_transformer);
    original file rel_ent_method_domain_randomization_mentions_ent_paper_action_chunking_with_transform_2023.'
sources:
- id: src_001
  type: other
  title: Wiki 第 18 章
  url: https://kg.rounds-tech.com/wiki/chapters/chapter-18/
  accessed_at: '2026-07-16'
---
