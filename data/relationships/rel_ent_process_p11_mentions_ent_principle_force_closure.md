---
$id: rel_ent_process_p11_mentions_ent_principle_force_closure
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: mentions
source:
  id: ent_process_p11
  name:
    en: Dexterous Hand Selection/Design and Integration
    zh: 灵巧手选型/设计与集成（Dexterous Hand）
target:
  id: ent_principle_force_closure
  name:
    en: Force Closure
    zh: 力闭合
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Dexterous Hand Selection/Design and Integration mentions Force Closure.
  zh: 灵巧手选型/设计与集成（Dexterous Hand）提及力闭合。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中“力闭合”出现在子任务标题中，但仅作为概念被提及，没有明确的关系方向。 | 证据:
    ##### Grasp Pose Generation and Force Closure Analysis'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p11
  url: https://kg.rounds-tech.com/entry/ent_process_p11/
  accessed_at: '2026-07-16'
---
