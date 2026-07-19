---
$id: rel_ent_component_ati_force_torque_sensor_2024_has_prerequisite_ent_method_forward_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_ati_force_torque_sensor_2024
  name:
    en: ATI Force Torque Sensor
    zh: ATI 力/力矩传感器
target:
  id: ent_method_forward_kinematics
  name:
    en: Forward Kinematics
    zh: 正运动学
domains:
  source_domain: 02_components
  target_domain: 06_design_engineering
description:
  en: ATI Force Torque Sensor has prerequisite Forward Kinematics.
  zh: ATI 力/力矩传感器前置依赖正运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 需要正向运动学来将传感器读数映射到机器人关节和末端执行器。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
