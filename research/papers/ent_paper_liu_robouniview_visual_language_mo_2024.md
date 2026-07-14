---
$id: ent_paper_liu_robouniview_visual_language_mo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation'
  zh: RoboUniView
  ko: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation'
summary:
  en: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (RoboUniView), is a 2024
    generalized vision-language-action model for robotic manipulation, introduced by Meituan.'
  zh: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (RoboUniView), is a 2024
    generalized vision-language-action model for robotic manipulation, introduced by Meituan.'
  ko: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (RoboUniView), is a 2024
    generalized vision-language-action model for robotic manipulation, introduced by Meituan.'
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
- robouniview
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.18977v3.
sources:
- id: src_001
  type: paper
  title: 'RoboUniView: Visual-Language Model with Unified View Representation for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2406.18977
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboUniView source
  url: https://doi.org/10.48550/arXiv.2406.18977
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Utilizing Vision-Language Models (VLMs) for robotic manipulation represents a novel paradigm, aiming to enhance the model's ability to generalize to new objects and instructions. However, due to variations in camera specifications and mounting positions, existing methods exhibit significant performance disparities across different robotic platforms. To address this challenge, we propose RoboUniView in this paper, an innovative approach that decouples visual feature extraction from action learning. We first learn a unified view representation from multi-perspective views by pre-training on readily accessible data, and then derive actions from this unified view representation to control robotic manipulation. This unified view representation more accurately mirrors the physical world and is not constrained by the robotic platform's camera parameters. Thanks to this methodology, we achieve state-of-the-art performance on the demanding CALVIN benchmark, enhancing the success rate in the $D \to D$ setting from 93.0% to 96.2%, and in the $ABC \to D$ setting from 92.2% to 94.2%. Moreover, our model exhibits outstanding adaptability and flexibility: it maintains high performance under unseen camera parameters, can utilize multiple datasets with varying camera parameters, and is capable of joint cross-task learning across datasets. Code is provided for re-implementation. https://github.com/liufanfanlff/RoboUniview

## 核心内容
Utilizing Vision-Language Models (VLMs) for robotic manipulation represents a novel paradigm, aiming to enhance the model's ability to generalize to new objects and instructions. However, due to variations in camera specifications and mounting positions, existing methods exhibit significant performance disparities across different robotic platforms. To address this challenge, we propose RoboUniView in this paper, an innovative approach that decouples visual feature extraction from action learning. We first learn a unified view representation from multi-perspective views by pre-training on readily accessible data, and then derive actions from this unified view representation to control robotic manipulation. This unified view representation more accurately mirrors the physical world and is not constrained by the robotic platform's camera parameters. Thanks to this methodology, we achieve state-of-the-art performance on the demanding CALVIN benchmark, enhancing the success rate in the $D \to D$ setting from 93.0% to 96.2%, and in the $ABC \to D$ setting from 92.2% to 94.2%. Moreover, our model exhibits outstanding adaptability and flexibility: it maintains high performance under unseen camera parameters, can utilize multiple datasets with varying camera parameters, and is capable of joint cross-task learning across datasets. Code is provided for re-implementation. https://github.com/liufanfanlff/RoboUniview

## 参考
- http://arxiv.org/abs/2406.18977v3

