---
$id: rel_ent_dataset_open_x_embodiment_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_dataset_open_x_embodiment
  name:
    en: Open X-Embodiment Dataset
    zh: Open X-Embodiment 数据集
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    zh: 线性代数
domains:
  source_domain: 09_data_datasets
  target_domain: 00_foundations
description:
  en: Open X-Embodiment Dataset has prerequisite Linear Algebra.
  zh: Open X-Embodiment 数据集前置依赖线性代数。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 大规模数据集的矩阵分解和特征提取需要线性代数。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
