---
$id: rel_ent_component_rgbd_camera_is_based_on_ent_component_intel_realsense_depth_camera_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_component_rgbd_camera
  name:
    en: RGB-D Camera
    zh: RGB-D相机
target:
  id: ent_component_intel_realsense_depth_camera_2024
  name:
    en: Intel RealSense Depth Camera
    zh: Intel RealSense 深度相机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: RGB-D Camera is based on Intel RealSense Depth Camera.
  zh: RGB-D相机基于Intel RealSense 深度相机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: RGB-D相机与Intel RealSense深度相机属于同类视觉传感器，共享深度感知技术基础。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_rgbd_camera
  url: https://kg.rounds-tech.com/entry/ent_component_rgbd_camera/
  accessed_at: '2026-07-16'
---
