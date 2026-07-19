---
$id: rel_ent_method_openvla_has_prerequisite_ent_dataset_open_x_embodiment
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_openvla
  name:
    en: OpenVLA
    zh: OpenVLA
target:
  id: ent_dataset_open_x_embodiment
  name:
    en: Open X-Embodiment Dataset
    zh: Open X-Embodiment 数据集
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 09_data_datasets
description:
  en: OpenVLA has prerequisite Open X-Embodiment Dataset.
  zh: OpenVLA前置依赖Open X-Embodiment 数据集。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: OpenVLA直接使用Open X-Embodiment数据集进行训练，需要理解该数据集的结构和内容。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
