---
$id: ent_paper_song_avi_action_from_volumetric_inf_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Avi: Action from Volumetric Inference'
  zh: Avi
  ko: 'Avi: Action from Volumetric Inference'
summary:
  en: 'Avi: Action from Volumetric Inference (Avi), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by University of California, Los Angeles, University of pennsylvania.'
  zh: 'Avi: Action from Volumetric Inference (Avi), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by University of California, Los Angeles, University of pennsylvania.'
  ko: 'Avi: Action from Volumetric Inference (Avi), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by University of California, Los Angeles, University of pennsylvania.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- avi
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.21746v1.
sources:
- id: src_001
  type: paper
  title: 'Avi: Action from Volumetric Inference (arXiv)'
  url: https://arxiv.org/abs/2510.21746
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Avi source
  url: https://doi.org/10.48550/arXiv.2510.21746
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We propose Avi, a novel 3D Vision-Language-Action (VLA) architecture that reframes robotic action generation as a problem of 3D perception and spatial reasoning, rather than low-level policy learning. While existing VLA models primarily operate on 2D visual inputs and are trained end-to-end on task-specific action policies, Avi leverages 3D point clouds and language-grounded scene understanding to compute actions through classical geometric transformations. Most notably, Avi does not train on previous action tokens, rather, we build upon a 3D Multi-modal Large Language Model (MLLM) to generate the next point cloud and explicitly calculate the actions through classical transformations. This approach enables generalizable behaviors that are robust to occlusions, camera pose variations, and changes in viewpoint. By treating the robotic decision-making process as a structured reasoning task over 3D representations, Avi bridges the gap between high-level language instructions and low-level actuation without requiring opaque policy learning. Our preliminary results highlight the potential of 3D vision-language reasoning as a foundation for scalable, robust robotic systems. Check it out at https://avi-3drobot.github.io/.

## 核心内容
We propose Avi, a novel 3D Vision-Language-Action (VLA) architecture that reframes robotic action generation as a problem of 3D perception and spatial reasoning, rather than low-level policy learning. While existing VLA models primarily operate on 2D visual inputs and are trained end-to-end on task-specific action policies, Avi leverages 3D point clouds and language-grounded scene understanding to compute actions through classical geometric transformations. Most notably, Avi does not train on previous action tokens, rather, we build upon a 3D Multi-modal Large Language Model (MLLM) to generate the next point cloud and explicitly calculate the actions through classical transformations. This approach enables generalizable behaviors that are robust to occlusions, camera pose variations, and changes in viewpoint. By treating the robotic decision-making process as a structured reasoning task over 3D representations, Avi bridges the gap between high-level language instructions and low-level actuation without requiring opaque policy learning. Our preliminary results highlight the potential of 3D vision-language reasoning as a foundation for scalable, robust robotic systems. Check it out at https://avi-3drobot.github.io/.

## 参考
- http://arxiv.org/abs/2510.21746v1

