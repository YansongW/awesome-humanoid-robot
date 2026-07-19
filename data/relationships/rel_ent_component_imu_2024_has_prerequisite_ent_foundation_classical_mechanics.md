---
$id: rel_ent_component_imu_2024_has_prerequisite_ent_foundation_classical_mechanics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_imu_2024
  name:
    en: Inertial Measurement Unit
    zh: 惯性测量单元
target:
  id: ent_foundation_classical_mechanics
  name:
    en: Classical Mechanics
    zh: 经典力学
domains:
  source_domain: 02_components
  target_domain: 00_foundations
description:
  en: Inertial Measurement Unit has prerequisite Classical Mechanics.
  zh: 惯性测量单元前置依赖经典力学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 理解加速度、角速度和姿态的物理概念是使用IMU的基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
