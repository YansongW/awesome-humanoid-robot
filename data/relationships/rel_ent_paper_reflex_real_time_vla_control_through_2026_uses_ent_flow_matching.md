---
$id: rel_ent_paper_reflex_real_time_vla_control_through_2026_uses_ent_flow_matching
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_reflex_real_time_vla_control_through_2026
  name:
    en: 'Reflex: Real-Time VLA Control through Streaming Inference'
    zh: 'Reflex: Real-Time VLA Control through Streaming Inference'
target:
  id: ent_flow_matching
  name:
    en: Flow matching
    zh: 流匹配
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 00_foundations
description:
  en: 'Reflex: Real-Time VLA Control through Streaming Inference uses Flow matching.'
  zh: 'Reflex: Real-Time VLA Control through Streaming Inference使用流匹配。'
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-08-06'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文Reflex针对Flow matching VLA模型，指出其迭代去噪特性与实时机器人不兼容。
    | 证据: Flow matching Vision-Language-Action (VLA) models promise precise continuous control, but their iterative denoising
    nature introduces fundamental incompatibilities with real-time robotics: global timestep injection invalidates KV-caching,
    forcing a c'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_reflex_real_time_vla_control_through_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_reflex_real_time_vla_control_through_2026/
  accessed_at: '2026-08-06'
---
