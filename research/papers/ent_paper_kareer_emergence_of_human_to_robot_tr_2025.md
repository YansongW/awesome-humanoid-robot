---
$id: ent_paper_kareer_emergence_of_human_to_robot_tr_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Emergence of Human to Robot Transfer in Vision-Language-Action Models
  zh: Emergence of Human to Robot Transfer in Vision-Language-Action Models
  ko: Emergence of Human to Robot Transfer in Vision-Language-Action Models
summary:
  en: Emergence of Human to Robot Transfer in Vision-Language-Action Models (Emergence of Human to Robot Transfer in Vision-Language-Action
    Models), is a 2025 large vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Georgia
    Institute of Technology.
  zh: Emergence of Human to Robot Transfer in Vision-Language-Action Models (Emergence of Human to Robot Transfer in Vision-Language-Action
    Models), is a 2025 large vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Georgia
    Institute of Technology.
  ko: Emergence of Human to Robot Transfer in Vision-Language-Action Models (Emergence of Human to Robot Transfer in Vision-Language-Action
    Models), is a 2025 large vision-language-action model for robotic manipulation, introduced by Physical Intelligence, Georgia
    Institute of Technology.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- emergence_of_human_to_robot_tr
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.22414v1.
sources:
- id: src_001
  type: paper
  title: Emergence of Human to Robot Transfer in Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2512.22414
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Emergence of Human to Robot Transfer in Vision-Language-Action Models source
  url: https://doi.org/10.48550/arXiv.2512.22414
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models can enable broad open world generalization, but require large and diverse datasets. It is appealing to consider whether some of this data can come from human videos, which cover diverse real-world situations and are easy to obtain. However, it is difficult to train VLAs with human videos alone, and establishing a mapping between humans and robots requires manual engineering and presents a major research challenge. Drawing inspiration from advances in large language models, where the ability to learn from diverse supervision emerges with scale, we ask whether a similar phenomenon holds for VLAs that incorporate human video data. We introduce a simple co-training recipe, and find that human-to-robot transfer emerges once the VLA is pre-trained on sufficient scenes, tasks, and embodiments. Our analysis suggests that this emergent capability arises because diverse pretraining produces embodiment-agnostic representations for human and robot data. We validate these findings through a series of experiments probing human to robot skill transfer and find that with sufficiently diverse robot pre-training our method can nearly double the performance on generalization settings seen only in human data.

## 核心内容
Vision-language-action (VLA) models can enable broad open world generalization, but require large and diverse datasets. It is appealing to consider whether some of this data can come from human videos, which cover diverse real-world situations and are easy to obtain. However, it is difficult to train VLAs with human videos alone, and establishing a mapping between humans and robots requires manual engineering and presents a major research challenge. Drawing inspiration from advances in large language models, where the ability to learn from diverse supervision emerges with scale, we ask whether a similar phenomenon holds for VLAs that incorporate human video data. We introduce a simple co-training recipe, and find that human-to-robot transfer emerges once the VLA is pre-trained on sufficient scenes, tasks, and embodiments. Our analysis suggests that this emergent capability arises because diverse pretraining produces embodiment-agnostic representations for human and robot data. We validate these findings through a series of experiments probing human to robot skill transfer and find that with sufficiently diverse robot pre-training our method can nearly double the performance on generalization settings seen only in human data.

## 参考
- http://arxiv.org/abs/2512.22414v1

