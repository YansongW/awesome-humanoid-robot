---
$id: rel_ent_process_p11_2_1_is_part_of_ent_process_p11
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p11_2_1
  name:
    en: Grasp Pose Generation and Force Closure Analysis
    zh: 抓取姿态生成与力闭合分析
target:
  id: ent_process_p11
  name:
    en: Dexterous Hand Selection/Design and Integration
    zh: 灵巧手选型/设计与集成（Dexterous Hand）
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Grasp Pose Generation and Force Closure Analysis is part of Dexterous Hand Selection/Design and Integration.
  zh: 抓取姿态生成与力闭合分析is_part_of灵巧手选型/设计与集成（Dexterous Hand）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源属于目标的工作包/阶段。 | 证据: **所属阶段/工作包**：灵巧手选型/设计与集成（Dexterous
    Hand）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p11_2_1
  url: https://kg.rounds-tech.com/entry/ent_process_p11_2_1/
  accessed_at: '2026-07-16'
---
