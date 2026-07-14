---
$id: ent_paper_ppf_pre_training_and_preservat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion'
  zh: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion'
  ko: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion'
summary:
  en: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
  zh: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
  ko: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- ppf
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.09833v2.
sources:
- id: src_001
  type: paper
  title: 'PPF: Pre-training and Preservative Fine-tuning of Humanoid Locomotion (arXiv)'
  url: https://arxiv.org/abs/2504.09833
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid locomotion is a challenging task due to its inherent complexity and high-dimensional dynamics, as well as the need to adapt to diverse and unpredictable environments. In this work, we introduce a novel learning framework for effectively training a humanoid locomotion policy that imitates the behavior of a model-based controller while extending its capabilities to handle more complex locomotion tasks, such as more challenging terrain and higher velocity commands. Our framework consists of three key components: pre-training through imitation of the model-based controller, fine-tuning via reinforcement learning, and model-assumption-based regularization (MAR) during fine-tuning. In particular, MAR aligns the policy with actions from the model-based controller only in states where the model assumption holds to prevent catastrophic forgetting. We evaluate the proposed framework through comprehensive simulation tests and hardware experiments on a full-size humanoid robot, Digit, demonstrating a forward speed of 1.5 m/s and robust locomotion across diverse terrains, including slippery, sloped, uneven, and sandy terrains.

## 核心内容
Humanoid locomotion is a challenging task due to its inherent complexity and high-dimensional dynamics, as well as the need to adapt to diverse and unpredictable environments. In this work, we introduce a novel learning framework for effectively training a humanoid locomotion policy that imitates the behavior of a model-based controller while extending its capabilities to handle more complex locomotion tasks, such as more challenging terrain and higher velocity commands. Our framework consists of three key components: pre-training through imitation of the model-based controller, fine-tuning via reinforcement learning, and model-assumption-based regularization (MAR) during fine-tuning. In particular, MAR aligns the policy with actions from the model-based controller only in states where the model assumption holds to prevent catastrophic forgetting. We evaluate the proposed framework through comprehensive simulation tests and hardware experiments on a full-size humanoid robot, Digit, demonstrating a forward speed of 1.5 m/s and robust locomotion across diverse terrains, including slippery, sloped, uneven, and sandy terrains.

## 参考
- http://arxiv.org/abs/2504.09833v2

