---
$id: rel_ent_component_hollow_cup_motor_2024_has_prerequisite_ent_method_pid_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_hollow_cup_motor_2024
  name:
    en: Hollow Cup Motor
    zh: 空心杯电机
target:
  id: ent_method_pid_control
  name:
    en: PID Control
    zh: PID控制
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Hollow Cup Motor has prerequisite PID Control.
  zh: 空心杯电机前置依赖PID控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: PID控制用于空心杯电机的速度和位置控制。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
