---
$id: rel_ent_method_diffusion_policy_uses_dataset_ent_dataset_droid
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses_dataset
source:
  id: ent_method_diffusion_policy
  name:
    en: Diffusion Policy
    zh: 扩散策略
target:
  id: ent_dataset_droid
  name:
    en: DROID
    zh: DROID 机器人操作数据集
domains:
  source:
  - 09_data_datasets
  target:
  - 07_ai_models_algorithms
description:
  en: DROID is used to train Diffusion Policy models.
  zh: DROID被用于训练Diffusion Policy模型。
  ko: DROID은 Diffusion Policy 모델 학습에 사용됩니다.
verification:
  confidence: medium
  notes: 'bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review | WP4 2026-08-11: endpoint
    id rewritten (ent_method_diffusion_policy→ent_method_diffusion_policy, ent_dataset_droid→ent_dataset_droid); original
    file rel_ent_paper_diffusion_policy_2023_uses_dataset_ent_dataset_droid.'
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
