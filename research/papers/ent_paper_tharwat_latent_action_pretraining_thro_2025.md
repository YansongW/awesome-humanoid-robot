---
$id: ent_paper_tharwat_latent_action_pretraining_thro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Latent Action Pretraining Through World Modeling
  zh: LAWM
  ko: Latent Action Pretraining Through World Modeling
summary:
  en: Latent Action Pretraining Through World Modeling (LAWM), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Mohamed bin Zayed University of Artificial Intelligence, Alexandria University.
  zh: Latent Action Pretraining Through World Modeling (LAWM), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Mohamed bin Zayed University of Artificial Intelligence, Alexandria University.
  ko: Latent Action Pretraining Through World Modeling (LAWM), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by Mohamed bin Zayed University of Artificial Intelligence, Alexandria University.
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
- lawm
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.18428v2.
sources:
- id: src_001
  type: paper
  title: Latent Action Pretraining Through World Modeling (arXiv)
  url: https://arxiv.org/abs/2509.18428
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LAWM source
  url: https://doi.org/10.48550/arXiv.2509.18428
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have gained popularity for learning robotic manipulation tasks that follow language instructions. State-of-the-art VLAs, such as OpenVLA and $π_{0}$, were trained on large-scale, manually labeled action datasets collected through teleoperation. More recent approaches, including LAPA and villa-X, introduce latent action representations that enable unsupervised pretraining on unlabeled datasets by modeling abstract visual changes between frames. Although these methods have shown strong results, their large model sizes make deployment in real-world settings challenging. In this work, we propose LAWM, a model-agnostic framework to pretrain imitation learning models in a self-supervised way, by learning latent action representations from unlabeled video data through world modeling. These videos can be sourced from robot recordings or videos of humans performing actions with everyday objects. Our framework is able to transfer learned knowledge across tasks, environments, and embodiments. It outperforms models pretrained with ground-truth robot actions and other similar pretraining methods on the LIBERO benchmark and real-world setup, while being efficient and practical for real-world settings.

## 核心内容
Vision-Language-Action (VLA) models have gained popularity for learning robotic manipulation tasks that follow language instructions. State-of-the-art VLAs, such as OpenVLA and $π_{0}$, were trained on large-scale, manually labeled action datasets collected through teleoperation. More recent approaches, including LAPA and villa-X, introduce latent action representations that enable unsupervised pretraining on unlabeled datasets by modeling abstract visual changes between frames. Although these methods have shown strong results, their large model sizes make deployment in real-world settings challenging. In this work, we propose LAWM, a model-agnostic framework to pretrain imitation learning models in a self-supervised way, by learning latent action representations from unlabeled video data through world modeling. These videos can be sourced from robot recordings or videos of humans performing actions with everyday objects. Our framework is able to transfer learned knowledge across tasks, environments, and embodiments. It outperforms models pretrained with ground-truth robot actions and other similar pretraining methods on the LIBERO benchmark and real-world setup, while being efficient and practical for real-world settings.

## 参考
- http://arxiv.org/abs/2509.18428v2

