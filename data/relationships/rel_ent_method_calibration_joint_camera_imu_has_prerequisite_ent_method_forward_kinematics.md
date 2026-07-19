---
$id: rel_ent_method_calibration_joint_camera_imu_has_prerequisite_ent_method_forward_kinematics
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_method_calibration_joint_camera_imu
  name:
    en: Joint-Camera-IMU Calibration
    zh: 联合标定
target:
  id: ent_method_forward_kinematics
  name:
    en: Forward Kinematics
    zh: 正运动学
domains:
  source_domain: 04_assembly_integration_testing
  target_domain: 06_design_engineering
description:
  en: Joint-Camera-IMU Calibration has prerequisite Forward Kinematics.
  zh: 联合标定前置依赖正运动学。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 正向运动学提供了关节空间与笛卡尔空间映射的基础'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
