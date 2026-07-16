---
$id: rel_ent_process_p6_is_part_of_ent_process_p6_2_1
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_part_of
source:
  id: ent_process_p6
  name:
    en: URDF modeling and Kinematics & URDF
    zh: URDF 建模与运动学校核（Kinematics & URDF）
target:
  id: ent_process_p6_2_1
  name:
    en: Verification of forward and inverse kinematics solution
    zh: 正逆运动学解算验证
domains:
  source_domain: 06_design_engineering
  target_domain: 06_design_engineering
description:
  en: URDF modeling and Kinematics & URDF is part of Verification of forward and inverse kinematics solution.
  zh: URDF 建模与运动学校核（Kinematics & URDF）is_part_of正逆运动学解算验证。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 源方法属于目标验证过程的一部分 | 证据: ##### 正逆运动学解算验证'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p6
  url: https://kg.rounds-tech.com/entry/ent_process_p6/
  accessed_at: '2026-07-16'
---
