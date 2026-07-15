---
$id: ent_paper_yuan_robopoint_a_vision_language_mo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics'
  zh: RoboPoint
  ko: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics'
summary:
  en: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics (RoboPoint), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by University of Washington, NVIDIA, Allen Institute
    for Artificial Intelligence, Universidad Católica San Pablo, and published at CoRL 2024.'
  zh: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics (RoboPoint), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by University of Washington, NVIDIA, Allen Institute
    for Artificial Intelligence, Universidad Católica San Pablo, and published at CoRL 2024.'
  ko: 'RoboPoint: A Vision-Language Model for Spatial Affordance Prediction for Robotics (RoboPoint), is a 2024 generalized
    vision-language-action model for robotic manipulation, introduced by University of Washington, NVIDIA, Allen Institute
    for Artificial Intelligence, Universidad Católica San Pablo, and published at CoRL 2024.'
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
- robopoint
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10721v1.
sources:
- id: src_001
  type: paper
  title: RoboPoint source
  url: https://proceedings.mlr.press/v270/yuan25c.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
From rearranging objects on a table to putting groceries into shelves, robots must plan precise action points to perform tasks accurately and reliably. In spite of the recent adoption of vision language models (VLMs) to control robot behavior, VLMs struggle to precisely articulate robot actions using language. We introduce an automatic synthetic data generation pipeline that instruction-tunes VLMs to robotic domains and needs. Using the pipeline, we train RoboPoint, a VLM that predicts image keypoint affordances given language instructions. Compared to alternative approaches, our method requires no real-world data collection or human demonstration, making it much more scalable to diverse environments and viewpoints. In addition, RoboPoint is a general model that enables several downstream applications such as robot navigation, manipulation, and augmented reality (AR) assistance. Our experiments demonstrate that RoboPoint outperforms state-of-the-art VLMs (GPT-4o) and visual prompting techniques (PIVOT) by 21.8% in the accuracy of predicting spatial affordance and by 30.5% in the success rate of downstream tasks. Project website: https://robo-point.github.io.

## 核心内容
From rearranging objects on a table to putting groceries into shelves, robots must plan precise action points to perform tasks accurately and reliably. In spite of the recent adoption of vision language models (VLMs) to control robot behavior, VLMs struggle to precisely articulate robot actions using language. We introduce an automatic synthetic data generation pipeline that instruction-tunes VLMs to robotic domains and needs. Using the pipeline, we train RoboPoint, a VLM that predicts image keypoint affordances given language instructions. Compared to alternative approaches, our method requires no real-world data collection or human demonstration, making it much more scalable to diverse environments and viewpoints. In addition, RoboPoint is a general model that enables several downstream applications such as robot navigation, manipulation, and augmented reality (AR) assistance. Our experiments demonstrate that RoboPoint outperforms state-of-the-art VLMs (GPT-4o) and visual prompting techniques (PIVOT) by 21.8% in the accuracy of predicting spatial affordance and by 30.5% in the success rate of downstream tasks. Project website: https://robo-point.github.io.

## 参考
- http://arxiv.org/abs/2406.10721v1

