---
$id: ent_paper_lin_evo_1_lightweight_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment'
  zh: Evo-1
  ko: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment'
summary:
  en: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment (Evo-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Imperial College London.'
  zh: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment (Evo-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Imperial College London.'
  ko: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment (Evo-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Imperial College London.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- evo_1
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.04555v2.
sources:
- id: src_001
  type: paper
  title: 'Evo-1: Lightweight Vision-Language-Action Model with Preserved Semantic Alignment (arXiv)'
  url: https://arxiv.org/abs/2511.04555
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Evo-1 source
  url: https://doi.org/10.48550/arXiv.2511.04555
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have emerged as a powerful framework that unifies perception, language, and control, enabling robots to perform diverse tasks through multimodal understanding. However, current VLA models typically contain massive parameters and rely heavily on large-scale robot data pretraining, leading to high computational costs during training, as well as limited deployability for real-time inference. Moreover, most training paradigms often degrade the perceptual representations of the vision-language backbone, resulting in overfitting and poor generalization to downstream tasks. In this work, we present Evo-1, a lightweight VLA model that reduces computation and improves deployment efficiency, while maintaining strong performance without pretraining on robot data. Evo-1 builds on a native multimodal Vision-Language model (VLM), incorporating a novel cross-modulated diffusion transformer along with an optimized integration module, together forming an effective architecture. We further introduce a two-stage training paradigm that progressively aligns action with perception, preserving the representations of the VLM. Notably, with only 0.77 billion parameters, Evo-1 achieves state-of-the-art results on the Meta-World and RoboTwin suite, surpassing the previous best models by 12.4% and 6.9%, respectively, and also attains a competitive result of 94.8% on LIBERO. In real-world evaluations, Evo-1 attains a 78% success rate with high inference frequency and low memory overhead, outperforming all baseline methods. We release code, data, and model weights to facilitate future research on lightweight and efficient VLA models.

## 核心内容
Vision-Language-Action (VLA) models have emerged as a powerful framework that unifies perception, language, and control, enabling robots to perform diverse tasks through multimodal understanding. However, current VLA models typically contain massive parameters and rely heavily on large-scale robot data pretraining, leading to high computational costs during training, as well as limited deployability for real-time inference. Moreover, most training paradigms often degrade the perceptual representations of the vision-language backbone, resulting in overfitting and poor generalization to downstream tasks. In this work, we present Evo-1, a lightweight VLA model that reduces computation and improves deployment efficiency, while maintaining strong performance without pretraining on robot data. Evo-1 builds on a native multimodal Vision-Language model (VLM), incorporating a novel cross-modulated diffusion transformer along with an optimized integration module, together forming an effective architecture. We further introduce a two-stage training paradigm that progressively aligns action with perception, preserving the representations of the VLM. Notably, with only 0.77 billion parameters, Evo-1 achieves state-of-the-art results on the Meta-World and RoboTwin suite, surpassing the previous best models by 12.4% and 6.9%, respectively, and also attains a competitive result of 94.8% on LIBERO. In real-world evaluations, Evo-1 attains a 78% success rate with high inference frequency and low memory overhead, outperforming all baseline methods. We release code, data, and model weights to facilitate future research on lightweight and efficient VLA models.

## 参考
- http://arxiv.org/abs/2511.04555v2

