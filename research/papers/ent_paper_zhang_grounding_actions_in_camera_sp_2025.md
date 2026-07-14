---
$id: ent_paper_zhang_grounding_actions_in_camera_sp_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy'
  zh: OC-VLA
  ko: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy'
summary:
  en: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (OC-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Shanghai AI Lab, SenseTime Research, Nanjing University,
    Tsinghua University.'
  zh: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (OC-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Shanghai AI Lab, SenseTime Research, Nanjing University,
    Tsinghua University.'
  ko: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (OC-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Zhejiang University, Shanghai AI Lab, SenseTime Research, Nanjing University,
    Tsinghua University.'
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
- oc_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.13103v1.
sources:
- id: src_001
  type: paper
  title: 'Grounding Actions in Camera Space: Observation-Centric Vision-Language-Action Policy (arXiv)'
  url: https://arxiv.org/abs/2508.13103
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OC-VLA source
  url: https://doi.org/10.48550/arXiv.2508.13103
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces. Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies. To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space. Leveraging the camera's extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets across heterogeneous viewpoints. This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations. The proposed approach is readily compatible with existing VLA architectures, requiring no substantial modifications. Comprehensive evaluations on both simulated and real-world robotic manipulation tasks demonstrate that OC-VLA accelerates convergence, enhances task success rates, and improves cross-view generalization. The code will be publicly available.

## 核心内容
Vision-Language-Action (VLA) models frequently encounter challenges in generalizing to real-world environments due to inherent discrepancies between observation and action spaces. Although training data are collected from diverse camera perspectives, the models typically predict end-effector poses within the robot base coordinate frame, resulting in spatial inconsistencies. To mitigate this limitation, we introduce the Observation-Centric VLA (OC-VLA) framework, which grounds action predictions directly in the camera observation space. Leveraging the camera's extrinsic calibration matrix, OC-VLA transforms end-effector poses from the robot base coordinate system into the camera coordinate system, thereby unifying prediction targets across heterogeneous viewpoints. This lightweight, plug-and-play strategy ensures robust alignment between perception and action, substantially improving model resilience to camera viewpoint variations. The proposed approach is readily compatible with existing VLA architectures, requiring no substantial modifications. Comprehensive evaluations on both simulated and real-world robotic manipulation tasks demonstrate that OC-VLA accelerates convergence, enhances task success rates, and improves cross-view generalization. The code will be publicly available.

## 参考
- http://arxiv.org/abs/2508.13103v1

