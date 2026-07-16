---
$id: rel_ent_process_p11_has_prerequisite_ent_process_p11_2_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_process_p11
  name:
    en: Dexterous Hand Selection/Design and Integration
    zh: 灵巧手选型/设计与集成（Dexterous Hand）
target:
  id: ent_process_p11_2_1
  name:
    en: Grasp Pose Generation and Force Closure Analysis
    zh: 抓取姿态生成与力闭合分析
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Dexterous Hand Selection/Design and Integration has prerequisite Grasp Pose Generation and Force Closure Analysis.
  zh: 灵巧手选型/设计与集成（Dexterous Hand）前置依赖抓取姿态生成与力闭合分析。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据中“抓取姿态生成与力闭合分析”作为子任务标题，表明它是“灵巧手选型/设计与集成”的前提或子步骤。
    | 证据: ##### 抓取姿态生成与力闭合分析'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p11
  url: https://kg.rounds-tech.com/entry/ent_process_p11/
  accessed_at: '2026-07-16'
---
