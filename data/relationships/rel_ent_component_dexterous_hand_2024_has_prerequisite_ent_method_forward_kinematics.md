---
$id: rel_ent_component_dexterous_hand_2024_has_prerequisite_ent_method_forward_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_dexterous_hand_2024
  name:
    en: Dexterous Hand
    zh: 灵巧手
target:
  id: ent_method_forward_kinematics
  name:
    en: Forward Kinematics
    zh: 正运动学
domains:
  source_domain: 02_components
  target_domain: 06_design_engineering
description:
  en: Dexterous Hand has prerequisite Forward Kinematics.
  zh: 灵巧手前置依赖正运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 正向运动学用于计算手指末端位置，是灵巧手抓取规划的基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
