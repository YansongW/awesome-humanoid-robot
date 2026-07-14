---
$id: ent_paper_kim_contrastive_representation_reg_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contrastive Representation Regularization for Vision-Language-Action Models
  zh: RS-CL
  ko: Contrastive Representation Regularization for Vision-Language-Action Models
summary:
  en: Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, RLWRLD.
  zh: Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, RLWRLD.
  ko: Contrastive Representation Regularization for Vision-Language-Action Models (RS-CL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by KAIST, UC Berkeley, RLWRLD.
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
- robotic_manipulation
- rs_cl
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.01711v4.
sources:
- id: src_001
  type: paper
  title: Contrastive Representation Regularization for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2510.01711
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RS-CL source
  url: https://doi.org/10.48550/arXiv.2510.01711
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown strong capabilities in robot manipulation by leveraging rich representations from pre-trained Vision-Language Models (VLMs). However, their representations arguably remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive information. To address the issue, we introduce Robot State-aware Contrastive Loss (RS-CL), a simple and effective representation regularization for VLA models, designed to bridge the gap between VLM representations and robotic signals. In particular, RS-CL aligns the representations more closely with the robot's proprioceptive states by using relative distances between the states as soft supervision. Complementing the original action prediction objective, RS-CL enhances control-relevant representation learning, while being lightweight and fully compatible with standard VLA training pipelines. Our empirical results demonstrate that RS-CL substantially improves the performance of state-of-the-art VLA models; it pushes the prior art to 69.7% achieving the state-of-the-art performance on the RoboCasa-Kitchen benchmark, and boosts success rates from 45.0% to 58.3% on challenging real-robot manipulation tasks.

## 核心内容
Vision-Language-Action (VLA) models have shown strong capabilities in robot manipulation by leveraging rich representations from pre-trained Vision-Language Models (VLMs). However, their representations arguably remain suboptimal, lacking sensitivity to robotic signals such as control actions and proprioceptive information. To address the issue, we introduce Robot State-aware Contrastive Loss (RS-CL), a simple and effective representation regularization for VLA models, designed to bridge the gap between VLM representations and robotic signals. In particular, RS-CL aligns the representations more closely with the robot's proprioceptive states by using relative distances between the states as soft supervision. Complementing the original action prediction objective, RS-CL enhances control-relevant representation learning, while being lightweight and fully compatible with standard VLA training pipelines. Our empirical results demonstrate that RS-CL substantially improves the performance of state-of-the-art VLA models; it pushes the prior art to 69.7% achieving the state-of-the-art performance on the RoboCasa-Kitchen benchmark, and boosts success rates from 45.0% to 58.3% on challenging real-robot manipulation tasks.

## 参考
- http://arxiv.org/abs/2510.01711v4

