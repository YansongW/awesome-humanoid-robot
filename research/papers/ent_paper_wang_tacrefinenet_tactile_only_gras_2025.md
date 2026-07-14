---
$id: ent_paper_wang_tacrefinenet_tactile_only_gras_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses'
  zh: TacRefineNet
  ko: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses'
summary:
  en: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses (TacRefineNet), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xiaomi Robotics.'
  zh: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses (TacRefineNet), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xiaomi Robotics.'
  ko: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses (TacRefineNet), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Xiaomi Robotics.'
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
- tacrefinenet
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.25746v1.
sources:
- id: src_001
  type: paper
  title: 'TacRefineNet: Tactile-Only Grasp Refinement Between Arbitrary In-Hand Object Poses (arXiv)'
  url: https://arxiv.org/abs/2509.25746
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: TacRefineNet source
  url: https://doi.org/10.48550/arXiv.2509.25746
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Despite progress in both traditional dexterous grasping pipelines and recent Vision-Language-Action (VLA) approaches, the grasp execution stage remains prone to pose inaccuracies, especially in long-horizon tasks, which undermines overall performance. To address this "last-mile" challenge, we propose TacRefineNet, a tactile-only framework that achieves fine in-hand pose refinement of known objects in arbitrary target poses using multi-finger fingertip sensing. Our method iteratively adjusts the end-effector pose based on tactile feedback, aligning the object to the desired configuration. We design a multi-branch policy network that fuses tactile inputs from multiple fingers along with proprioception to predict precise control updates. To train this policy, we combine large-scale simulated data from a physics-based tactile model in MuJoCo with real-world data collected from a physical system. Comparative experiments show that pretraining on simulated data and fine-tuning with a small amount of real data significantly improves performance over simulation-only training. Extensive real-world experiments validate the effectiveness of the method, achieving millimeter-level grasp accuracy using only tactile input. To our knowledge, this is the first method to enable arbitrary in-hand pose refinement via multi-finger tactile sensing alone. Project website is available at https://sites.google.com/view/tacrefinenet

## 核心内容
Despite progress in both traditional dexterous grasping pipelines and recent Vision-Language-Action (VLA) approaches, the grasp execution stage remains prone to pose inaccuracies, especially in long-horizon tasks, which undermines overall performance. To address this "last-mile" challenge, we propose TacRefineNet, a tactile-only framework that achieves fine in-hand pose refinement of known objects in arbitrary target poses using multi-finger fingertip sensing. Our method iteratively adjusts the end-effector pose based on tactile feedback, aligning the object to the desired configuration. We design a multi-branch policy network that fuses tactile inputs from multiple fingers along with proprioception to predict precise control updates. To train this policy, we combine large-scale simulated data from a physics-based tactile model in MuJoCo with real-world data collected from a physical system. Comparative experiments show that pretraining on simulated data and fine-tuning with a small amount of real data significantly improves performance over simulation-only training. Extensive real-world experiments validate the effectiveness of the method, achieving millimeter-level grasp accuracy using only tactile input. To our knowledge, this is the first method to enable arbitrary in-hand pose refinement via multi-finger tactile sensing alone. Project website is available at https://sites.google.com/view/tacrefinenet

## 参考
- http://arxiv.org/abs/2509.25746v1

