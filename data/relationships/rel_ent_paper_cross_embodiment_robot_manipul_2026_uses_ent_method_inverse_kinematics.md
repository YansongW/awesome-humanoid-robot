---
$id: rel_ent_paper_cross_embodiment_robot_manipul_2026_uses_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_paper_cross_embodiment_robot_manipul_2026
  name:
    en: Cross-Embodiment Robot Manipulation via a Unified Hand Action Space
    zh: Cross-Embodiment Robot Manipulation via a Unified Hand Action Space
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 06_design_engineering
description:
  en: Cross-Embodiment Robot Manipulation via a Unified Hand Action Space uses Inverse Kinematics.
  zh: Cross-Embodiment Robot Manipulation via a Unified Hand Action Space使用逆运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 论文使用级联逆运动学算法映射共享表示。 | 证据: UHAS represents robotic
    hand actions as geometric deformations of a canonical sphere and uses a Cascade Inverse Kinematics (CIK) algorithm to
    map the shared representation to embodiment-specific joint configurations.'
sources:
- id: src_001
  type: other
  title: KG body of ent_paper_cross_embodiment_robot_manipul_2026
  url: https://kg.rounds-tech.com/entry/ent_paper_cross_embodiment_robot_manipul_2026/
  accessed_at: '2026-07-16'
---
