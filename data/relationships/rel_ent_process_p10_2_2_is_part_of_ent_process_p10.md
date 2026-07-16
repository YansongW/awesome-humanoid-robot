---
$id: rel_ent_process_p10_2_2_is_part_of_ent_process_p10
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p10_2_2
  name:
    en: Gait Planning and Terrain Adaptation
    zh: 步态规划与地形适应
target:
  id: ent_process_p10
  name:
    en: Motion Control Algorithm Development and Validation
    zh: 运动控制算法开发与验证（Motion Control）
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Gait Planning and Terrain Adaptation is part of Motion Control Algorithm Development and Validation.
  zh: 步态规划与地形适应is_part_of运动控制算法开发与验证（Motion Control）。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据表明源方法属于运动控制算法开发与验证这一工作包。 | 证据: **所属阶段/工作包**：运动控制算法开发与验证（Motion
    Control）'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p10_2_2
  url: https://kg.rounds-tech.com/entry/ent_process_p10_2_2/
  accessed_at: '2026-07-16'
---
