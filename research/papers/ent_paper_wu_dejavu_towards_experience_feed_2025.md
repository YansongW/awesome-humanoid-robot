---
$id: ent_paper_wu_dejavu_towards_experience_feed_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence'
  zh: Dejavu
  ko: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence'
summary:
  en: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (Dejavu), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University.'
  zh: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (Dejavu), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University.'
  ko: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (Dejavu), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dejavu
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10181v3.
sources:
- id: src_001
  type: paper
  title: 'Dejavu: Towards Experience Feedback Learning for Embodied Intelligence (arXiv)'
  url: https://arxiv.org/abs/2510.10181
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Embodied agents face a fundamental limitation: once deployed in real-world environments, they cannot easily acquire new knowledge to improve task performance. In this paper, we propose Dejavu, a general post-deployment learning framework that augments a frozen Vision-Language-Action (VLA) policy with retrieved execution memories through an Experience Feedback Network (EFN). EFN identifies contextually relevant prior action experiences and conditions action prediction on the retrieved guidance. We train EFN with reinforcement learning and semantic similarity rewards, encouraging the predicted actions to align with past behaviors under the current observation. During deployment, EFN continually expands its memory with new trajectories, enabling the agent to exhibit ``learning from experience.'' Experiments across diverse embodied tasks show that EFN improves adaptability, robustness, and success rates over frozen baselines. Our Project Page is https://dejavu2025.github.io/.

## 核心内容
Embodied agents face a fundamental limitation: once deployed in real-world environments, they cannot easily acquire new knowledge to improve task performance. In this paper, we propose Dejavu, a general post-deployment learning framework that augments a frozen Vision-Language-Action (VLA) policy with retrieved execution memories through an Experience Feedback Network (EFN). EFN identifies contextually relevant prior action experiences and conditions action prediction on the retrieved guidance. We train EFN with reinforcement learning and semantic similarity rewards, encouraging the predicted actions to align with past behaviors under the current observation. During deployment, EFN continually expands its memory with new trajectories, enabling the agent to exhibit ``learning from experience.'' Experiments across diverse embodied tasks show that EFN improves adaptability, robustness, and success rates over frozen baselines. Our Project Page is https://dejavu2025.github.io/.

## 参考
- http://arxiv.org/abs/2510.10181v3

