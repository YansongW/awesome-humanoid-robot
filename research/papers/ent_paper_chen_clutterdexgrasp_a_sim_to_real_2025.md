---
$id: ent_paper_chen_clutterdexgrasp_a_sim_to_real_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes'
  zh: ClutterDexGrasp
  ko: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes'
summary:
  en: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes (ClutterDexGrasp), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Duke University, and published at CoRL25.'
  zh: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes (ClutterDexGrasp), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Duke University, and published at CoRL25.'
  ko: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes (ClutterDexGrasp), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Duke University, and published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- clutterdexgrasp
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.14317v3.
sources:
- id: src_001
  type: paper
  title: 'ClutterDexGrasp: A Sim-to-Real System for General Dexterous Grasping in Cluttered Scenes (arXiv)'
  url: https://arxiv.org/abs/2506.14317
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ClutterDexGrasp source
  url: https://doi.org/10.48550/arXiv.2506.14317
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes. Recent vision-language-action models offer a potential solution but require extensive real-world demonstrations, making them costly and difficult to scale. To address these limitations, we revisit the sim-to-real transfer pipeline and develop key techniques that enable zero-shot deployment in reality while maintaining robust generalization. We propose ClutterDexGrasp, a two-stage teacher-student framework for closed-loop target-oriented dexterous grasping in cluttered scenes. The framework features a teacher policy trained in simulation using clutter density curriculum learning, incorporating both a geometry and spatially-embedded scene representation and a novel comprehensive safety curriculum, enabling general, dynamic, and safe grasping behaviors. Through imitation learning, we distill the teacher's knowledge into a student 3D diffusion policy (DP3) that operates on partial point cloud observations. To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes, demonstrating robust performance across diverse objects and layouts. More details and videos are available at https://clutterdexgrasp.github.io/.

## 核心内容
Dexterous grasping in cluttered scenes presents significant challenges due to diverse object geometries, occlusions, and potential collisions. Existing methods primarily focus on single-object grasping or grasp-pose prediction without interaction, which are insufficient for complex, cluttered scenes. Recent vision-language-action models offer a potential solution but require extensive real-world demonstrations, making them costly and difficult to scale. To address these limitations, we revisit the sim-to-real transfer pipeline and develop key techniques that enable zero-shot deployment in reality while maintaining robust generalization. We propose ClutterDexGrasp, a two-stage teacher-student framework for closed-loop target-oriented dexterous grasping in cluttered scenes. The framework features a teacher policy trained in simulation using clutter density curriculum learning, incorporating both a geometry and spatially-embedded scene representation and a novel comprehensive safety curriculum, enabling general, dynamic, and safe grasping behaviors. Through imitation learning, we distill the teacher's knowledge into a student 3D diffusion policy (DP3) that operates on partial point cloud observations. To the best of our knowledge, this represents the first zero-shot sim-to-real closed-loop system for target-oriented dexterous grasping in cluttered scenes, demonstrating robust performance across diverse objects and layouts. More details and videos are available at https://clutterdexgrasp.github.io/.

## 参考
- http://arxiv.org/abs/2506.14317v3

