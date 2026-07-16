---
$id: rel_ent_application_healthcare_discusses_ent_concept_robot_as_a_service
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: discusses
source:
  id: ent_application_healthcare
  name:
    en: Healthcare Assistance
    zh: 医疗健康
target:
  id: ent_concept_robot_as_a_service
  name:
    en: Robot-as-a-Service (RaaS)
    zh: 机器人即服务（RaaS）
domains:
  source_domain: 11_applications_markets
  target_domain: 11_applications_markets
description:
  en: Healthcare Assistance discusses Robot-as-a-Service (RaaS).
  zh: 医疗健康discusses机器人即服务（RaaS）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: 医疗辅助场景可能涉及机器人即服务模式。'
sources:
- id: src_001
  type: other
  title: KG body of ent_application_healthcare
  url: https://kg.rounds-tech.com/entry/ent_application_healthcare/
  accessed_at: '2026-07-16'
---
