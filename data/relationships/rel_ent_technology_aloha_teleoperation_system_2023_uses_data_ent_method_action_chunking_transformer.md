---
$id: rel_ent_technology_aloha_teleoperation_system_2023_uses_data_ent_method_action_chunking_transformer
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses_data
source:
  id: ent_technology_aloha_teleoperation_system_2023
  name:
    en: ALOHA Teleoperation System
    zh: ALOHA 遥操作系统
target:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
domains:
  source:
  - 04_data_collection
  - 07_ai_models_algorithms
  target:
  - 07_ai_models_algorithms
description:
  en: ALOHA hardware collects demonstrations used to train ACT.
  zh: ALOHA硬件采集用于训练ACT的演示数据。
  ko: ALOHA 하드웨어는 ACT 학습에 사용되는 시연 데이터를 수집합니다.
verification:
  confidence: medium
  notes: 'bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review | WP4 2026-08-11: endpoint
    id rewritten (ent_technology_aloha_teleoperation_system_2023→ent_technology_aloha_teleoperation_system_2023, ent_method_action_chunking_transformer→ent_method_action_chunking_transformer);
    original file rel_ent_technology_aloha_teleoperation_system_2023_uses_data_ent_paper_action_chunking_with_transform_2023.'
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
