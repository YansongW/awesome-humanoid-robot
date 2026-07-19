---
$id: rel_ent_component_zed_stereo_camera_2024_has_prerequisite_ent_foundation_linear_algebra
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_component_zed_stereo_camera_2024
  name:
    en: ZED Stereo Camera
    zh: ZED 立体相机
target:
  id: ent_foundation_linear_algebra
  name:
    en: Linear Algebra
    zh: 线性代数
domains:
  source_domain: 02_components
  target_domain: 00_foundations
description:
  en: ZED Stereo Camera has prerequisite Linear Algebra.
  zh: ZED 立体相机前置依赖线性代数。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: 立体视觉中的相机标定和三维重建依赖线性代数。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
