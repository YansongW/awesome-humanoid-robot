---
$id: rel_ent_component_ati_force_torque_sensor_2024_has_prerequisite_ent_component_six_axis_force_torque_sensor_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_ati_force_torque_sensor_2024
  name:
    en: ATI Force Torque Sensor
    zh: ATI 力/力矩传感器
target:
  id: ent_component_six_axis_force_torque_sensor_2024
  name:
    en: Six Axis Force Torque Sensor
    zh: 六维力传感器
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ATI Force Torque Sensor has prerequisite Six Axis Force Torque Sensor.
  zh: ATI 力/力矩传感器前置依赖六维力传感器。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 六轴力/力矩传感器是更通用的力觉传感器，理解其原理有助于理解ATI专用传感器。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
