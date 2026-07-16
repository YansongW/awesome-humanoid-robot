---
$id: rel_ent_process_p10_2_1_uses_ent_principle_capture_point
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p10_2_1
  name:
    en: Standing and Anti-Interference Balance Control
    zh: 站立与抗扰平衡控制
target:
  id: ent_principle_capture_point
  name:
    en: Capture Point
    zh: 捕获点
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Standing and Anti-Interference Balance Control uses Capture Point.
  zh: 站立与抗扰平衡控制使用捕获点。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据列出源方法使用的工具包括目标原理。 | 证据: **方法 / 工具**：LQR、MPC、ZMP/Capture
    Point、角动量控制'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p10_2_1
  url: https://kg.rounds-tech.com/entry/ent_process_p10_2_1/
  accessed_at: '2026-07-16'
---
