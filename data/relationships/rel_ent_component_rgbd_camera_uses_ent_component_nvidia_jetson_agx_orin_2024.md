---
$id: rel_ent_component_rgbd_camera_uses_ent_component_nvidia_jetson_agx_orin_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_rgbd_camera
  name:
    en: RGB-D Camera
    zh: RGB-D相机
target:
  id: ent_component_nvidia_jetson_agx_orin_2024
  name:
    en: NVIDIA Jetson AGX Orin
    zh: NVIDIA Jetson AGX Orin
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: RGB-D Camera uses NVIDIA Jetson AGX Orin.
  zh: RGB-D相机使用NVIDIA Jetson AGX Orin。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: RGB-D相机通常与NVIDIA Jetson AGX Orin等高性能计算平台配合处理视觉数据。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_rgbd_camera
  url: https://kg.rounds-tech.com/entry/ent_component_rgbd_camera/
  accessed_at: '2026-07-16'
---
