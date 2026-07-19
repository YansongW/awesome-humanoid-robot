---
$id: rel_ent_technology_quasi_direct_drive_actuator_2024_has_prerequisite_ent_method_pid_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_technology_quasi_direct_drive_actuator_2024
  name:
    en: Quasi Direct Drive Actuator
    zh: 准直驱执行器
target:
  id: ent_method_pid_control
  name:
    en: PID Control
    zh: PID控制
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Quasi Direct Drive Actuator has prerequisite PID Control.
  zh: 准直驱执行器前置依赖PID控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: PID控制是执行器底层电流/速度/位置环的基础'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
