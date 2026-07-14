---
$id: ent_paper_li_mimicdreamer_aligning_human_an_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training'
  zh: MimicDreamer
  ko: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training'
summary:
  en: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (MimicDreamer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by GigaAI, CASIA, NJUST, Tsinghua University.'
  zh: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (MimicDreamer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by GigaAI, CASIA, NJUST, Tsinghua University.'
  ko: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (MimicDreamer), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by GigaAI, CASIA, NJUST, Tsinghua University.'
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
- mimicdreamer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22199v2.
sources:
- id: src_001
  type: paper
  title: 'MimicDreamer: Aligning Human and Robot Demonstrations for Scalable VLA Training (arXiv)'
  url: https://arxiv.org/abs/2509.22199
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MimicDreamer source
  url: https://doi.org/10.48550/arXiv.2509.22199
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.

## 核心内容
Vision Language Action (VLA) models derive their generalization capability from diverse training data, yet collecting embodied robot interaction data remains prohibitively expensive. In contrast, human demonstration videos are far more scalable and cost-efficient to collect, and recent studies confirm their effectiveness in training VLA models. However, a significant domain gap persists between human videos and robot-executed videos, including unstable camera viewpoints, visual discrepancies between human hands and robotic arms, and differences in motion dynamics. To bridge this gap, we propose MimicDreamer, a framework that turns fast, low-cost human demonstrations into robot-usable supervision by jointly aligning vision, viewpoint, and actions to directly support policy training. For visual alignment, we propose H2R Aligner, a video diffusion model that generates high-fidelity robot demonstration videos by transferring motion from human manipulation footage. For viewpoint stabilization, EgoStabilizer is proposed, which canonicalizes egocentric videos via homography and inpaints occlusions and distortions caused by warping. For action alignment, we map human hand trajectories to the robot frame and apply a constrained inverse kinematics solver to produce feasible, low-jitter joint commands with accurate pose tracking. Empirically, VLA models trained purely on our synthesized human-to-robot videos achieve few-shot execution on real robots. Moreover, scaling training with human data significantly boosts performance compared to models trained solely on real robot data; our approach improves the average success rate by 14.7\% across six representative manipulation tasks.

## 参考
- http://arxiv.org/abs/2509.22199v2

