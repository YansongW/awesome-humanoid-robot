---
$id: rel_ent_component_intel_realsense_depth_camera_2024_has_prerequisite_ent_component_rgbd_camera
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_intel_realsense_depth_camera_2024
  name:
    en: Intel RealSense Depth Camera
    zh: Intel RealSense 深度相机
target:
  id: ent_component_rgbd_camera
  name:
    en: RGB-D Camera
    zh: RGB-D相机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: Intel RealSense Depth Camera has prerequisite RGB-D Camera.
  zh: Intel RealSense 深度相机前置依赖RGB-D相机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: RealSense深度相机是RGB-D相机的一种具体实现，理解通用RGB-D原理是掌握具体产品的基础。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
