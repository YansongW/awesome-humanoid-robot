---
$id: ent_paper_zhang_reasoning_vla_a_fast_and_gener_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving'
  zh: Reasoning-VLA
  ko: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving'
summary:
  en: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (Reasoning-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University, National University
    of Singapore, University of Science and Technology of China, Tsinghua University, University of New South Wales.'
  zh: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (Reasoning-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University, National University
    of Singapore, University of Science and Technology of China, Tsinghua University, University of New South Wales.'
  ko: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (Reasoning-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Lanzhou University, National University
    of Singapore, University of Science and Technology of China, Tsinghua University, University of New South Wales.'
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
- reasoning_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.19912v1.
sources:
- id: src_001
  type: paper
  title: 'Reasoning-VLA: A Fast and General Vision-Language-Action Reasoning Model for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.19912
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Reasoning-VLA source
  url: https://doi.org/10.48550/arXiv.2511.19912
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving. However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios. In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework. The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus. These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel. To promote robust generalization, we consolidate eight publicly available autonomous driving datasets into a standardized, Chain-of-Thought reasoning-based, and easy-to-use data format for model training. Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves state-of-the-art performance, superior generalization capability, and the excellent inference speed reported to date.

## 核心内容
Vision-Language-Action (VLA) models have recently shown strong decision-making capabilities in autonomous driving. However, existing VLAs often struggle with achieving efficient inference and generalizing to novel autonomous vehicle configurations and driving scenarios. In this paper, we propose Reasoning-VLA, a general and fast action-generation VLA framework. The proposed model employs a set of learnable action queries, initialized via Gaussian sampling from ground-truth trajectories within the training corpus. These learnable queries interact with reasoning-enhanced vision-language features to generate continuous action trajectories in parallel. To promote robust generalization, we consolidate eight publicly available autonomous driving datasets into a standardized, Chain-of-Thought reasoning-based, and easy-to-use data format for model training. Leveraging both supervised learning and reinforcement learning fine-tuning, extensive empirical evaluations across multiple benchmarks demonstrate that Reasoning-VLA achieves state-of-the-art performance, superior generalization capability, and the excellent inference speed reported to date.

## 参考
- http://arxiv.org/abs/2511.19912v1

