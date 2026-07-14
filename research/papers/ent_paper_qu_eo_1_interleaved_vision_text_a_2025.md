---
$id: ent_paper_qu_eo_1_interleaved_vision_text_a_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control'
  zh: EO-1
  ko: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control'
summary:
  en: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control (EO-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen).'
  zh: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control (EO-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen).'
  ko: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control (EO-1), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Harbin Institute of Technology (Shenzhen).'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- eo_1
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.21112v5.
sources:
- id: src_001
  type: paper
  title: 'EO-1: Interleaved Vision-Text-Action Pretraining for General Robot Control (arXiv)'
  url: https://arxiv.org/abs/2508.21112
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EO-1 source
  url: https://doi.org/10.48550/arXiv.2508.21112
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The human ability to seamlessly perform multimodal reasoning and physical interaction in the open world is a core goal for general purpose embodied intelligent systems. Recent vision-language-action (VLA) models, which are co-trained on large-scale robot and visual-text data, have demonstrated notable progress in general robot control. However, they still fail to achieve human-level flexibility in interleaved reasoning and interaction. In this work, we introduce EO-Robotics, consists of EO-1 model and EO-Data1.5M dataset. EO-1 is a unified embodied foundation model that achieves superior performance in multimodal embodied reasoning and robot control through interleaved vision-text-action pre-training. The development of EO-1 is based on two key pillars: (i) a unified architecture that processes multimodal inputs indiscriminately (image, text, video, and action), and (ii) a massive, high-quality multimodal embodied reasoning dataset, EO-Data1.5M, which contains over 1.5 million samples with emphasis on interleaved vision-text-action comprehension. EO-1 is trained through synergies between auto-regressive decoding and flow matching denoising on EO-Data1.5M, enabling seamless robot action generation and multimodal embodied reasoning. Extensive experiments demonstrate the effectiveness of interleaved vision-text-action learning for open-world understanding and generalization, validated through a variety of long-horizon, dexterous manipulation tasks across multiple embodiments. This paper details the architecture of EO-1, the data construction strategy of EO-Data1.5M, and the training methodology, offering valuable insights for developing advanced embodied foundation models. Project Page: https://eo-robotics.ai/eo-1.

## 核心内容
The human ability to seamlessly perform multimodal reasoning and physical interaction in the open world is a core goal for general purpose embodied intelligent systems. Recent vision-language-action (VLA) models, which are co-trained on large-scale robot and visual-text data, have demonstrated notable progress in general robot control. However, they still fail to achieve human-level flexibility in interleaved reasoning and interaction. In this work, we introduce EO-Robotics, consists of EO-1 model and EO-Data1.5M dataset. EO-1 is a unified embodied foundation model that achieves superior performance in multimodal embodied reasoning and robot control through interleaved vision-text-action pre-training. The development of EO-1 is based on two key pillars: (i) a unified architecture that processes multimodal inputs indiscriminately (image, text, video, and action), and (ii) a massive, high-quality multimodal embodied reasoning dataset, EO-Data1.5M, which contains over 1.5 million samples with emphasis on interleaved vision-text-action comprehension. EO-1 is trained through synergies between auto-regressive decoding and flow matching denoising on EO-Data1.5M, enabling seamless robot action generation and multimodal embodied reasoning. Extensive experiments demonstrate the effectiveness of interleaved vision-text-action learning for open-world understanding and generalization, validated through a variety of long-horizon, dexterous manipulation tasks across multiple embodiments. This paper details the architecture of EO-1, the data construction strategy of EO-Data1.5M, and the training methodology, offering valuable insights for developing advanced embodied foundation models. Project Page: https://eo-robotics.ai/eo-1.

## 参考
- http://arxiv.org/abs/2508.21112v5

