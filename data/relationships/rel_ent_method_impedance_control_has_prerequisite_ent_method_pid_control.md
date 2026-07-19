---
$id: rel_ent_method_impedance_control_has_prerequisite_ent_method_pid_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_impedance_control
  name:
    en: Impedance Control
    zh: 阻抗控制
target:
  id: ent_method_pid_control
  name:
    en: PID Control
    zh: PID控制
domains:
  source_domain: 07_ai_models_algorithms
  target_domain: 07_ai_models_algorithms
description:
  en: Impedance Control has prerequisite PID Control.
  zh: 阻抗控制前置依赖PID控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 阻抗控制建立在基础反馈控制概念之上，PID控制提供了理解力-位置关系的起点。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
