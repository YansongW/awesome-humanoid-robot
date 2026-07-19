---
$id: rel_ent_robot_system_berkeley_humanoid_lite_has_prerequisite_ent_component_imu_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_robot_system_berkeley_humanoid_lite
  name:
    en: Berkeley Humanoid Lite
    zh: 伯克利轻量人形机器人
target:
  id: ent_component_imu_2024
  name:
    en: Inertial Measurement Unit
    zh: 惯性测量单元
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Berkeley Humanoid Lite has prerequisite Inertial Measurement Unit.
  zh: 伯克利轻量人形机器人前置依赖惯性测量单元。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: IMU是双足机器人姿态估计和平衡控制的关键传感器。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
