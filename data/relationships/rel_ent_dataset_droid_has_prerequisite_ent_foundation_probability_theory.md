---
$id: rel_ent_dataset_droid_has_prerequisite_ent_foundation_probability_theory
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_dataset_droid
  name:
    en: DROID
    zh: DROID 机器人操作数据集
target:
  id: ent_foundation_probability_theory
  name:
    en: Probability Theory
    zh: 概率论
domains:
  source_domain: 09_data_datasets
  target_domain: 00_foundations
description:
  en: DROID has prerequisite Probability Theory.
  zh: DROID 机器人操作数据集前置依赖概率论。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 数据集中的采样偏差和统计特性分析需要概率论。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
