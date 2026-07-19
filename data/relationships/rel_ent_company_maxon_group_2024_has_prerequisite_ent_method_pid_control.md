---
$id: rel_ent_company_maxon_group_2024_has_prerequisite_ent_method_pid_control
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_company_maxon_group_2024
  name:
    en: Maxon Group
    zh: Maxon
target:
  id: ent_method_pid_control
  name:
    en: PID Control
    zh: PID控制
domains:
  source_domain: 02_components
  target_domain: 07_ai_models_algorithms
description:
  en: Maxon Group has prerequisite PID Control.
  zh: Maxon前置依赖PID控制。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: Maxon电机驱动器使用PID控制算法。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
