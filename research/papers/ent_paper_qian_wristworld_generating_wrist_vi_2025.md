---
$id: ent_paper_qian_wristworld_generating_wrist_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation'
  zh: WristWorld
  ko: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation'
summary:
  en: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation (WristWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Hong Kong University of Science and Technology, National
    University of Singapore, Beijing Innovation Center of Humanoid Robotics.'
  zh: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation (WristWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Hong Kong University of Science and Technology, National
    University of Singapore, Beijing Innovation Center of Humanoid Robotics.'
  ko: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation (WristWorld), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Hong Kong University of Science and Technology, National
    University of Singapore, Beijing Innovation Center of Humanoid Robotics.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- wristworld
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07313v1.
sources:
- id: src_001
  type: paper
  title: 'WristWorld: Generating Wrist-Views via 4D World Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2510.07313
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: WristWorld source
  url: https://doi.org/10.48550/arXiv.2510.07313
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Wrist-view observations are crucial for VLA models as they capture fine-grained hand-object interactions that directly enhance manipulation performance. Yet large-scale datasets rarely include such recordings, resulting in a substantial gap between abundant anchor views and scarce wrist views. Existing world models cannot bridge this gap, as they require a wrist-view first frame and thus fail to generate wrist-view videos from anchor views alone. Amid this gap, recent visual geometry models such as VGGT emerge with geometric and cross-view priors that make it possible to address extreme viewpoint shifts. Inspired by these insights, we propose WristWorld, the first 4D world model that generates wrist-view videos solely from anchor views. WristWorld operates in two stages: (i) Reconstruction, which extends VGGT and incorporates our Spatial Projection Consistency (SPC) Loss to estimate geometrically consistent wrist-view poses and 4D point clouds; (ii) Generation, which employs our video generation model to synthesize temporally coherent wrist-view videos from the reconstructed perspective. Experiments on Droid, Calvin, and Franka Panda demonstrate state-of-the-art video generation with superior spatial consistency, while also improving VLA performance, raising the average task completion length on Calvin by 3.81% and closing 42.4% of the anchor-wrist view gap.

## 核心内容
Wrist-view observations are crucial for VLA models as they capture fine-grained hand-object interactions that directly enhance manipulation performance. Yet large-scale datasets rarely include such recordings, resulting in a substantial gap between abundant anchor views and scarce wrist views. Existing world models cannot bridge this gap, as they require a wrist-view first frame and thus fail to generate wrist-view videos from anchor views alone. Amid this gap, recent visual geometry models such as VGGT emerge with geometric and cross-view priors that make it possible to address extreme viewpoint shifts. Inspired by these insights, we propose WristWorld, the first 4D world model that generates wrist-view videos solely from anchor views. WristWorld operates in two stages: (i) Reconstruction, which extends VGGT and incorporates our Spatial Projection Consistency (SPC) Loss to estimate geometrically consistent wrist-view poses and 4D point clouds; (ii) Generation, which employs our video generation model to synthesize temporally coherent wrist-view videos from the reconstructed perspective. Experiments on Droid, Calvin, and Franka Panda demonstrate state-of-the-art video generation with superior spatial consistency, while also improving VLA performance, raising the average task completion length on Calvin by 3.81% and closing 42.4% of the anchor-wrist view gap.

## 参考
- http://arxiv.org/abs/2510.07313v1

