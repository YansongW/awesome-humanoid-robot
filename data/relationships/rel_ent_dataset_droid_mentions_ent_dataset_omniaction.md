---
$id: rel_ent_dataset_droid_mentions_ent_dataset_omniaction
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_dataset_droid
  name:
    en: DROID
    zh: DROID 机器人操作数据集
target:
  id: ent_dataset_omniaction
  name:
    en: OmniAction Dataset
    zh: OmniAction 数据集
domains:
  source_domain: 09_data_datasets
  target_domain: 09_data_datasets
description:
  en: DROID mentions OmniAction Dataset.
  zh: DROID 机器人操作数据集提及OmniAction 数据集。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p4_wiki_ch21. Evidence: 在 Wiki 第 21 章同一小节共现'
sources:
- id: src_001
  type: other
  title: Wiki 第 21 章
  url: https://kg.rounds-tech.com/wiki/chapters/chapter-21/
  accessed_at: '2026-07-16'
---
