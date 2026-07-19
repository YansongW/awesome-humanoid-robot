---
$id: rel_ent_component_dexterous_hand_2024_has_prerequisite_ent_method_inverse_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_dexterous_hand_2024
  name:
    en: Dexterous Hand
    zh: 灵巧手
target:
  id: ent_method_inverse_kinematics
  name:
    en: Inverse Kinematics
    zh: 逆运动学
domains:
  source_domain: 02_components
  target_domain: 06_design_engineering
description:
  en: Dexterous Hand has prerequisite Inverse Kinematics.
  zh: 灵巧手前置依赖逆运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 逆运动学用于将期望的指尖位置映射到关节角度，实现精确控制。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
