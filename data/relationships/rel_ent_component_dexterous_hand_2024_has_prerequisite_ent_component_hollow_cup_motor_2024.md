---
$id: rel_ent_component_dexterous_hand_2024_has_prerequisite_ent_component_hollow_cup_motor_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_dexterous_hand_2024
  name:
    en: Dexterous Hand
    zh: 灵巧手
target:
  id: ent_component_hollow_cup_motor_2024
  name:
    en: Hollow Cup Motor
    zh: 空心杯电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Dexterous Hand has prerequisite Hollow Cup Motor.
  zh: 灵巧手前置依赖空心杯电机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 空心杯电机常用于灵巧手的小型关节，是驱动手指运动的核心部件。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
