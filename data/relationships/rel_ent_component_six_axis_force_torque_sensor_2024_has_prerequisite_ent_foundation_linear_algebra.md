---
$id: rel_ent_component_six_axis_force_torque_sensor_2024_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_six_axis_force_torque_sensor_2024
  name:
    en: Six Axis Force Torque Sensor
    zh: 六维力传感器
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    zh: 线性代数
domains:
  source_domain: 02_components
  target_domain: 00_foundations
description:
  en: Six Axis Force Torque Sensor has prerequisite Linear Algebra.
  zh: 六维力传感器前置依赖线性代数。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 六维力/力矩的坐标变换和矩阵运算需要线性代数。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
