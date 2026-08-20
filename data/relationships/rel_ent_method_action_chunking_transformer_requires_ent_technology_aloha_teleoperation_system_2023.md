---
$id: rel_ent_method_action_chunking_transformer_requires_ent_technology_aloha_teleoperation_system_2023
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: requires
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
  en: ACT requires a teleoperation interface such as ALOHA to collect demonstrations.
  zh: ACT需要ALOHA等遥操作接口来采集演示。
  ko: ACT는 시연을 수집하기 위해 ALOHA와 같은 텔레오퍼레이션 인터페이스가 필요합니다.
verification:
  confidence: medium
  notes: 'bulk-added confidence on 2026-07-17 by backfill_rel_confidence.py; pending human review | WP4 2026-08-11: endpoint
    id rewritten (ent_method_action_chunking_transformer→ent_method_action_chunking_transformer, ent_technology_aloha_teleoperation_system_2023→ent_technology_aloha_teleoperation_system_2023);
    original file rel_ent_paper_action_chunking_with_transform_2023_requires_ent_technology_aloha_teleoperation_system_2023.'
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
