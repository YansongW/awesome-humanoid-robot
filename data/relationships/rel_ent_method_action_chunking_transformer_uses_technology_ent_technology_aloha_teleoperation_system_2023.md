---
$id: rel_ent_method_action_chunking_transformer_uses_technology_ent_technology_aloha_teleoperation_system_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses_technology
source:
  id: ent_method_action_chunking_transformer
  name:
    en: Action Chunking with Transformers (ACT)
    zh: 动作分块变压器（ACT）
target:
  id: ent_technology_aloha_teleoperation_system_2023
  name:
    en: ALOHA Teleoperation System
    zh: ALOHA 遥操作系统
domains:
  source:
  - 07_ai_models_algorithms
  target:
  - 04_data_collection
  - 07_ai_models_algorithms
description:
  en: ACT is commonly trained on demonstrations collected via ALOHA.
  zh: ACT通常使用通过ALOHA采集的演示数据训练。
  ko: ACT는 일반적으로 ALOHA를 통해 수집된 시연 데이터로 학습됩니다.
verification:
  confidence: medium
  notes: 'bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review | WP4 2026-08-11: endpoint
    id rewritten (ent_method_action_chunking_transformer→ent_method_action_chunking_transformer, ent_technology_aloha_teleoperation_system_2023→ent_technology_aloha_teleoperation_system_2023);
    original file rel_ent_paper_action_chunking_with_transform_2023_uses_technology_ent_technology_aloha_teleoperation_system_2023.'
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
