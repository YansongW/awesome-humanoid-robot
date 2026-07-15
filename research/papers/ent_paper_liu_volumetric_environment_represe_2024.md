---
$id: ent_paper_liu_volumetric_environment_represe_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Volumetric Environment Representation for Vision-Language Navigation
  zh: VER
  ko: Volumetric Environment Representation for Vision-Language Navigation
summary:
  en: Volumetric Environment Representation for Vision-Language Navigation (VER), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by ReLER, CCAI, Zhejiang University, and published at CVPR 2024.
  zh: Volumetric Environment Representation for Vision-Language Navigation (VER), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by ReLER, CCAI, Zhejiang University, and published at CVPR 2024.
  ko: Volumetric Environment Representation for Vision-Language Navigation (VER), is a 2024 generalized vision-language-action
    model for robotic manipulation, introduced by ReLER, CCAI, Zhejiang University, and published at CVPR 2024.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- ver
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.14158v1.
sources:
- id: src_001
  type: website
  title: VER source
  url: https://doi.org/10.1109/CVPR52733.2024.01544
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language navigation (VLN) requires an agent to navigate through an 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in the comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle for capturing 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).

## 核心内容
Vision-language navigation (VLN) requires an agent to navigate through an 3D environment based on visual observations and natural language instructions. It is clear that the pivotal factor for successful navigation lies in the comprehensive scene understanding. Previous VLN agents employ monocular frameworks to extract 2D features of perspective views directly. Though straightforward, they struggle for capturing 3D geometry and semantics, leading to a partial and incomplete environment representation. To achieve a comprehensive 3D representation with fine-grained details, we introduce a Volumetric Environment Representation (VER), which voxelizes the physical world into structured 3D cells. For each cell, VER aggregates multi-view 2D features into such a unified 3D space via 2D-3D sampling. Through coarse-to-fine feature extraction and multi-task learning for VER, our agent predicts 3D occupancy, 3D room layout, and 3D bounding boxes jointly. Based on online collected VERs, our agent performs volume state estimation and builds episodic memory for predicting the next step. Experimental results show our environment representations from multi-task learning lead to evident performance gains on VLN. Our model achieves state-of-the-art performance across VLN benchmarks (R2R, REVERIE, and R4R).

## 参考
- http://arxiv.org/abs/2403.14158v1

