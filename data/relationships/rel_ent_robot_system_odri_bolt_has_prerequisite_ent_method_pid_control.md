---
$id: rel_ent_robot_system_odri_bolt_has_prerequisite_ent_method_pid_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_odri_bolt
  name:
    en: ODRI Bolt (Open Dynamic Robot Initiative)
    zh: ODRI Bolt 开源双足机器人
target:
  id: ent_method_pid_control
  name:
    en: PID Control
    zh: PID控制
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: ODRI Bolt (Open Dynamic Robot Initiative) has prerequisite PID Control.
  zh: ODRI Bolt 开源双足机器人前置依赖PID控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: ODRI Bolt的电机控制依赖PID控制算法。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
