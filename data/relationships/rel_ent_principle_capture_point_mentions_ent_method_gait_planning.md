---
$id: rel_ent_principle_capture_point_mentions_ent_method_gait_planning
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_principle_capture_point
  name:
    en: Capture Point
    zh: 捕获点
target:
  id: ent_method_gait_planning
  name:
    en: Gait Planning
    zh: 步态规划
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Capture Point mentions Gait Planning.
  zh: 捕获点提及步态规划。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中列出了Capture Point和Gait Planning等术语，但没有明确的方向性关系。
    | 证据: note "Terminology: Capture Point (CP), Push Recovery, Gait Planning, Dynamic Balance"'
sources:
- id: src_001
  type: other
  title: KG body of ent_principle_capture_point
  url: https://kg.rounds-tech.com/entry/ent_principle_capture_point/
  accessed_at: '2026-07-16'
---
