---
$id: rel_ent_component_dynamixel_xl330_m288_t_has_prerequisite_ent_component_bldc_motor
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_dynamixel_xl330_m288_t
  name:
    en: ROBOTIS DYNAMIXEL XL330-M288-T
    zh: ROBOTIS DYNAMIXEL XL330-M288-T 舵机
target:
  id: ent_component_bldc_motor
  name:
    en: Brushless DC Motor
    zh: 无刷直流电机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ROBOTIS DYNAMIXEL XL330-M288-T has prerequisite Brushless DC Motor.
  zh: ROBOTIS DYNAMIXEL XL330-M288-T 舵机前置依赖无刷直流电机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 该舵机内部使用无刷直流电机，理解BLDC原理有助于理解其驱动方式。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
