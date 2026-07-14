---
$id: ent_paper_li_embodiment_transfer_learning_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Embodiment Transfer Learning for Vision-Language-Action Models
  zh: ET-VLA
  ko: Embodiment Transfer Learning for Vision-Language-Action Models
summary:
  en: Embodiment Transfer Learning for Vision-Language-Action Models (ET-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Shanghai University.
  zh: Embodiment Transfer Learning for Vision-Language-Action Models (ET-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Shanghai University.
  ko: Embodiment Transfer Learning for Vision-Language-Action Models (ET-VLA), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Shanghai University.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- et_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01224v1.
sources:
- id: src_001
  type: paper
  title: Embodiment Transfer Learning for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2511.01224
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ET-VLA source
  url: https://doi.org/10.48550/arXiv.2511.01224
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have significantly advanced robotic learning, enabling training on large-scale, cross-embodiment data and fine-tuning for specific robots. However, state-of-the-art autoregressive VLAs struggle with multi-robot collaboration. We introduce embodiment transfer learning, denoted as ET-VLA, a novel framework for efficient and effective transfer of pre-trained VLAs to multi-robot. ET-VLA's core is Synthetic Continued Pretraining (SCP), which uses synthetically generated data to warm up the model for the new embodiment, bypassing the need for real human demonstrations and reducing data collection costs. SCP enables the model to learn correct actions and precise action token numbers. Following SCP, the model is fine-tuned on target embodiment data. To further enhance the model performance on multi-embodiment, we present the Embodied Graph-of-Thought technique, a novel approach that formulates each sub-task as a node, that allows the VLA model to distinguish the functionalities and roles of each embodiment during task execution. Our work considers bimanual robots, a simple version of multi-robot to verify our approaches. We validate the effectiveness of our method on both simulation benchmarks and real robots covering three different bimanual embodiments. In particular, our proposed ET-VLA \space can outperform OpenVLA on six real-world tasks over 53.2%. We will open-source all codes to support the community in advancing VLA models for robot learning.

## 核心内容
Vision-language-action (VLA) models have significantly advanced robotic learning, enabling training on large-scale, cross-embodiment data and fine-tuning for specific robots. However, state-of-the-art autoregressive VLAs struggle with multi-robot collaboration. We introduce embodiment transfer learning, denoted as ET-VLA, a novel framework for efficient and effective transfer of pre-trained VLAs to multi-robot. ET-VLA's core is Synthetic Continued Pretraining (SCP), which uses synthetically generated data to warm up the model for the new embodiment, bypassing the need for real human demonstrations and reducing data collection costs. SCP enables the model to learn correct actions and precise action token numbers. Following SCP, the model is fine-tuned on target embodiment data. To further enhance the model performance on multi-embodiment, we present the Embodied Graph-of-Thought technique, a novel approach that formulates each sub-task as a node, that allows the VLA model to distinguish the functionalities and roles of each embodiment during task execution. Our work considers bimanual robots, a simple version of multi-robot to verify our approaches. We validate the effectiveness of our method on both simulation benchmarks and real robots covering three different bimanual embodiments. In particular, our proposed ET-VLA \space can outperform OpenVLA on six real-world tasks over 53.2%. We will open-source all codes to support the community in advancing VLA models for robot learning.

## 参考
- http://arxiv.org/abs/2511.01224v1

