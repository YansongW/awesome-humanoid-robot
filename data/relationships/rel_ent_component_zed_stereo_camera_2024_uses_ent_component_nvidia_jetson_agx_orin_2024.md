---
$id: rel_ent_component_zed_stereo_camera_2024_uses_ent_component_nvidia_jetson_agx_orin_2024
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: uses
source:
  id: ent_component_zed_stereo_camera_2024
  name:
    en: ZED Stereo Camera
    zh: ZED 立体相机
target:
  id: ent_component_nvidia_jetson_agx_orin_2024
  name:
    en: NVIDIA Jetson AGX Orin
    zh: NVIDIA Jetson AGX Orin
domains:
  source_domain: 02_components
  target_domain: 02_components
description:
  en: ZED Stereo Camera uses NVIDIA Jetson AGX Orin.
  zh: ZED 立体相机使用NVIDIA Jetson AGX Orin。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-16'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p6_llm_link. Evidence: ZED相机通常与NVIDIA Jetson平台配合进行深度估计和空间AI处理。'
sources:
- id: src_001
  type: other
  title: KG body of ent_component_zed_stereo_camera_2024
  url: https://kg.rounds-tech.com/entry/ent_component_zed_stereo_camera_2024/
  accessed_at: '2026-07-16'
---
