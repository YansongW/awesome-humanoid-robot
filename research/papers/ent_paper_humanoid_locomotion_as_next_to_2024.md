---
$id: ent_paper_humanoid_locomotion_as_next_to_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Locomotion as Next Token Prediction
  zh: Humanoid Locomotion as Next Token Prediction
  ko: Humanoid Locomotion as Next Token Prediction
summary:
  en: Humanoid Locomotion as Next Token Prediction is a 2024 work on locomotion for humanoid robots.
  zh: Humanoid Locomotion as Next Token Prediction is a 2024 work on locomotion for humanoid robots.
  ko: Humanoid Locomotion as Next Token Prediction is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoid_locomotion_as_next_to
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.19469v1.
sources:
- id: src_001
  type: paper
  title: Humanoid Locomotion as Next Token Prediction (arXiv)
  url: https://arxiv.org/abs/2402.19469
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Humanoid Locomotion as Next Token Prediction project page
  url: https://humanoid-next-token-prediction.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
We cast real-world humanoid control as a next token prediction problem, akin to predicting the next word in language. Our model is a causal transformer trained via autoregressive prediction of sensorimotor trajectories. To account for the multi-modal nature of the data, we perform prediction in a modality-aligned way, and for each input token predict the next token from the same modality. This general formulation enables us to leverage data with missing modalities, like video trajectories without actions. We train our model on a collection of simulated trajectories coming from prior neural network policies, model-based controllers, motion capture data, and YouTube videos of humans. We show that our model enables a full-sized humanoid to walk in San Francisco zero-shot. Our model can transfer to the real world even when trained on only 27 hours of walking data, and can generalize to commands not seen during training like walking backward. These findings suggest a promising path toward learning challenging real-world control tasks by generative modeling of sensorimotor trajectories.

## 核心内容
We cast real-world humanoid control as a next token prediction problem, akin to predicting the next word in language. Our model is a causal transformer trained via autoregressive prediction of sensorimotor trajectories. To account for the multi-modal nature of the data, we perform prediction in a modality-aligned way, and for each input token predict the next token from the same modality. This general formulation enables us to leverage data with missing modalities, like video trajectories without actions. We train our model on a collection of simulated trajectories coming from prior neural network policies, model-based controllers, motion capture data, and YouTube videos of humans. We show that our model enables a full-sized humanoid to walk in San Francisco zero-shot. Our model can transfer to the real world even when trained on only 27 hours of walking data, and can generalize to commands not seen during training like walking backward. These findings suggest a promising path toward learning challenging real-world control tasks by generative modeling of sensorimotor trajectories.

## 参考
- http://arxiv.org/abs/2402.19469v1

