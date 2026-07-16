---
$id: rel_ent_dataset_humanplus_shadowing_mentions_ent_dataset_amass_motion_dataset_2019
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_dataset_humanplus_shadowing
  name:
    en: HumanPlus Shadowing Dataset
    zh: HumanPlus Shadowing数据集
target:
  id: ent_dataset_amass_motion_dataset_2019
  name:
    en: AMASS Motion Dataset
    zh: AMASS 动作数据集
domains:
  source_domain: 09_data_datasets
  target_domain: 09_data_datasets
description:
  en: HumanPlus Shadowing Dataset mentions AMASS Motion Dataset.
  zh: HumanPlus Shadowing数据集提及AMASS 动作数据集。
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: low
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 该数据集在构建时可能参考了AMASS运动数据集作为对比或基础。'
sources:
- id: src_001
  type: other
  title: KG body of ent_dataset_humanplus_shadowing
  url: https://kg.rounds-tech.com/entry/ent_dataset_humanplus_shadowing/
  accessed_at: '2026-07-16'
---
