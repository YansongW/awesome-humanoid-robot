---
$id: rel_ent_dataset_droid_used_with_ent_software_nvidia_isaac_sim_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_dataset_droid
  name:
    en: DROID
    zh: DROID 机器人操作数据集
    ko: DROID
target:
  id: ent_software_nvidia_isaac_sim_2024
  name:
    en: NVIDIA Isaac Sim
    zh: NVIDIA Isaac Sim
    ko: NVIDIA Isaac Sim
domains:
  source:
  - 09_data_datasets
  target:
  - 08_software_middleware
  - 07_ai_models_algorithms
description:
  en: DROID data can be replayed or augmented in Isaac Sim for policy training.
  zh: DROID数据可在Isaac Sim中回放或增强以训练策略。
  ko: DROID 데이터는 Isaac Sim에서 정책 학습을 위해 재생 또는 증강될 수 있습니다.
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





