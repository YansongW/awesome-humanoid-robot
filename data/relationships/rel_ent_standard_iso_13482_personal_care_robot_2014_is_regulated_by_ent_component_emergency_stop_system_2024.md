---
$id: rel_ent_standard_iso_13482_personal_care_robot_2014_is_regulated_by_ent_component_emergency_stop_system_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_regulated_by
source:
  id: ent_standard_iso_13482_personal_care_robot_2014
  name:
    en: ISO 13482 Personal Care Robot Safety
    zh: ISO 13482 个人护理机器人安全
    ko: ISO 13482 개인 돌봄 로봇 안전
target:
  id: ent_component_emergency_stop_system_2024
  name:
    en: Emergency Stop System
    zh: 急停系统
    ko: Emergency Stop System
domains:
  source:
  - 12_policy_regulation_ethics
  target:
  - 02_components
  - 12_policy_regulation_ethics
description:
  en: ISO 13482 requires emergency stop systems on personal care robots.
  zh: ISO 13482要求个人护理机器人配备急停系统。
  ko: ISO 13482는 개인 돌봄 로봇에 비상 정지 시스템을 요구합니다.
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





