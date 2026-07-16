---
$id: rel_ent_robot_system_unitree_g1_uses_hardware_from_ent_component_intel_realsense_depth_camera_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses_hardware_from
source:
  id: ent_robot_system_unitree_g1
  name:
    en: Unitree G1 Humanoid Robot
    zh: Unitree G1 人形机器人
target:
  id: ent_component_intel_realsense_depth_camera_2024
  name:
    en: Intel RealSense Depth Camera
    zh: Intel RealSense 深度相机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Unitree G1 Humanoid Robot uses hardware from Intel RealSense Depth Camera.
  zh: Unitree G1 人形机器人uses_hardware_fromIntel RealSense 深度相机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p3_llm_typed. Evidence: 证据列出Unitree G1使用了Intel RealSense深度相机作为核心零部件。
    | 证据: - **核心零部件/技术来源**：自研关节电机与驱动器、3D LiDAR、Intel RealSense 深度相机、NVIDIA Jetson Orin（EDU 版）。'
sources:
- id: src_001
  type: other
  title: KG body of ent_robot_system_unitree_g1
  url: https://kg.rounds-tech.com/entry/ent_robot_system_unitree_g1/
  accessed_at: '2026-07-16'
---
