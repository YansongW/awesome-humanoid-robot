---
$id: ent_paper_humanoidpano_hybrid_spherical_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots'
  zh: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots'
  ko: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots'
summary:
  en: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots is a 2025 work on navigation
    for humanoid robots.'
  zh: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots is a 2025 work on navigation
    for humanoid robots.'
  ko: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots is a 2025 work on navigation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoidpano
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.09010v2.
sources:
- id: src_001
  type: paper
  title: 'HumanoidPano: Hybrid Spherical Panoramic-LiDAR Cross-Modal Perception for Humanoid Robots (arXiv)'
  url: https://arxiv.org/abs/2503.09010
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations. Unlike conventional robot perception systems that rely on monocular cameras or standard multi-sensor configurations, our method establishes geometrically-aware modality alignment through a spherical vision transformer, enabling seamless fusion of 360 visual context with LiDAR's precise depth measurements. First, Spherical Geometry-aware Constraints (SGC) leverage panoramic camera ray properties to guide distortion-regularized sampling offsets for geometric alignment. Second, Spatial Deformable Attention (SDA) aggregates hierarchical 3D features via spherical offsets, enabling efficient 360°-to-BEV fusion with geometrically complete object representations. Third, Panoramic Augmentation (AUG) combines cross-view transformations and semantic alignment to enhance BEV-panoramic feature consistency during data augmentation. Extensive evaluations demonstrate state-of-the-art performance on the 360BEV-Matterport benchmark. Real-world deployment on humanoid platforms validates the system's capability to generate accurate BEV segmentation maps through panoramic-LiDAR co-perception, directly enabling downstream navigation tasks in complex environments. Our work establishes a new paradigm for embodied perception in humanoid robotics.

## 核心内容
The perceptual system design for humanoid robots poses unique challenges due to inherent structural constraints that cause severe self-occlusion and limited field-of-view (FOV). We present HumanoidPano, a novel hybrid cross-modal perception framework that synergistically integrates panoramic vision and LiDAR sensing to overcome these limitations. Unlike conventional robot perception systems that rely on monocular cameras or standard multi-sensor configurations, our method establishes geometrically-aware modality alignment through a spherical vision transformer, enabling seamless fusion of 360 visual context with LiDAR's precise depth measurements. First, Spherical Geometry-aware Constraints (SGC) leverage panoramic camera ray properties to guide distortion-regularized sampling offsets for geometric alignment. Second, Spatial Deformable Attention (SDA) aggregates hierarchical 3D features via spherical offsets, enabling efficient 360°-to-BEV fusion with geometrically complete object representations. Third, Panoramic Augmentation (AUG) combines cross-view transformations and semantic alignment to enhance BEV-panoramic feature consistency during data augmentation. Extensive evaluations demonstrate state-of-the-art performance on the 360BEV-Matterport benchmark. Real-world deployment on humanoid platforms validates the system's capability to generate accurate BEV segmentation maps through panoramic-LiDAR co-perception, directly enabling downstream navigation tasks in complex environments. Our work establishes a new paradigm for embodied perception in humanoid robotics.

## 参考
- http://arxiv.org/abs/2503.09010v2

