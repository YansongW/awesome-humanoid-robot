---
$id: rel_ent_robot_agility_robotics_digit_2023_uses_hardware_from_ent_component_intel_realsense_depth_camera_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses_hardware_from
source:
  id: ent_robot_agility_robotics_digit_2023
  name:
    en: Agility Robotics Digit
    zh: Agility Robotics Digit
target:
  id: ent_component_intel_realsense_depth_camera_2024
  name:
    en: Intel RealSense Depth Camera
    zh: Intel RealSense 深度相机
domains:
  source_domain: 06_design_engineering
  target_domain: 02_components
description:
  en: Agility Robotics Digit uses hardware from Intel RealSense Depth Camera.
  zh: Agility Robotics Digituses_hardware_fromIntel RealSense 深度相机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: Digit的感知系统包括Intel RealSense深度相机。 | 证据: Digit
    的感知系统包括 4 颗 Intel RealSense 深度相机、LiDAR、IMU 与力传感器，可在无需外部基础设施的情况下自主导航。'
sources:
- id: src_001
  type: other
  title: KG body of ent_robot_agility_robotics_digit_2023
  url: https://kg.rounds-tech.com/entry/ent_robot_agility_robotics_digit_2023/
  accessed_at: '2026-07-16'
---
