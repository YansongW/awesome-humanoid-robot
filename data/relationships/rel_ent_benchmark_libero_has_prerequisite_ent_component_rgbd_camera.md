---
$id: rel_ent_benchmark_libero_has_prerequisite_ent_component_rgbd_camera
$schema: ../schema/v1/relationship_schema.json
$version: 1
type: has_prerequisite
source:
  id: ent_benchmark_libero
  name:
    en: LIBERO
    zh: LIBERO
target:
  id: ent_component_rgbd_camera
  name:
    en: RGB-D Camera
    zh: RGB-D相机
domains:
  source_domain: 09_data_datasets
  target_domain: 02_components
description:
  en: LIBERO has prerequisite RGB-D Camera.
  zh: LIBERO前置依赖RGB-D相机。
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-17'
  confidence: medium
  notes: 'Mined by build_latent_relationships.py rule p7_learning_chain. Evidence: LIBERO任务依赖RGB-D视觉输入，需先理解该传感器。'
sources:
- id: src_001
  type: other
  title: 0→1 路线图学习链
  url: https://kg.rounds-tech.com/wiki/roadmap/
  accessed_at: '2026-07-17'
---
