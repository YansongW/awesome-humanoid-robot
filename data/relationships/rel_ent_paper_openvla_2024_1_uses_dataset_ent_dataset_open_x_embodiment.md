---
$id: rel_ent_paper_openvla_2024_1_uses_dataset_ent_dataset_open_x_embodiment
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses_dataset
source:
  id: ent_paper_openvla_2024_1
  name:
    en: OpenVLA
    zh: OpenVLA
    ko: OpenVLA
target:
  id: ent_dataset_open_x_embodiment
  name:
    en: Open X-Embodiment Dataset
    zh: Open X-Embodiment 数据集
    ko: Open X-Embodiment 데이터셋
domains:
  source:
  - 09_data_datasets
  target:
  - 07_ai_models_algorithms
description:
  en: Open X-Embodiment data is used to train OpenVLA.
  zh: Open X-Embodiment数据用于训练OpenVLA。
  ko: Open X-Embodiment 데이터는 OpenVLA 학습에 사용됩니다.
verification:
  confidence: medium
  notes: bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review
  status: partially_verified
  sources: []
  reviewed_by: ai_autonomous
  reviewed_at: '2026-07-02T00:21:22.207515+00:00'
sources:
- type: website
  url: ''
  description: Workflow relationship curated from public project pages and literature.
  id: curated_workflow_relationship
---






