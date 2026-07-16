---
$id: rel_ent_process_p6_2_1_uses_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_process_p6_2_1
  name:
    en: Verification of forward and inverse kinematics solution
    zh: 正逆运动学解算验证
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 06_design_engineering
  target_domain: 06_design_engineering
description:
  en: Verification of forward and inverse kinematics solution uses Inverse Kinematics.
  zh: 正逆运动学解算验证使用逆运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 正逆运动学解验证使用了逆运动学方法/工具。 | 证据: **Method/Tool**:
    Analytical/Numerical Inverse Kinematics, Random Pose Sampling, Singularity Analysis'
sources:
- id: src_001
  type: other
  title: KG body of ent_process_p6_2_1
  url: https://kg.rounds-tech.com/entry/ent_process_p6_2_1/
  accessed_at: '2026-07-16'
---
