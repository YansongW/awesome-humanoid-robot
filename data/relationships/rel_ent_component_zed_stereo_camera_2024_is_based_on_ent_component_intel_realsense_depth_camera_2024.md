---
$id: rel_ent_component_zed_stereo_camera_2024_is_based_on_ent_component_intel_realsense_depth_camera_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: is_based_on
source:
  id: ent_component_zed_stereo_camera_2024
  name:
    en: ZED Stereo Camera
    zh: ZED 立体相机
target:
  id: ent_component_intel_realsense_depth_camera_2024
  name:
    en: Intel RealSense Depth Camera
    zh: Intel RealSense 深度相机
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ZED Stereo Camera is based on Intel RealSense Depth Camera.
  zh: ZED 立体相机基于Intel RealSense 深度相机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: ZED立体相机与Intel RealSense深度相机都是用于机器人导航的立体视觉传感器。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_zed_stereo_camera_2024
  url: https://kg.rounds-tech.com/entry/ent_component_zed_stereo_camera_2024/
  accessed_at: '2026-07-16'
---
