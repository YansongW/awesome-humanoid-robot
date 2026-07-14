---
$id: ent_paper_park_quantization_aware_imitation_l_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Quantization-Aware Imitation-Learning for Resource-Efficient Robotic Control
  zh: QAIL+QBC
  ko: Quantization-Aware Imitation-Learning for Resource-Efficient Robotic Control
summary:
  en: Quantization-Aware Imitation-Learning for Resource-Efficient Robotic Control (QAIL+QBC), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Hanyang University, Hyundai Motor Company.
  zh: Quantization-Aware Imitation-Learning for Resource-Efficient Robotic Control (QAIL+QBC), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Hanyang University, Hyundai Motor Company.
  ko: Quantization-Aware Imitation-Learning for Resource-Efficient Robotic Control (QAIL+QBC), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Hanyang University, Hyundai Motor Company.
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
- qailqbc
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.01034v1.
sources:
- id: src_001
  type: paper
  title: Quantization-Aware Imitation-Learning for Resource-Efficient Robotic Control (arXiv)
  url: https://arxiv.org/abs/2412.01034
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: QAIL+QBC source
  url: https://doi.org/10.48550/arXiv.2412.01034
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Deep neural network (DNN)-based policy models like vision-language-action (VLA) models are transformative in automating complex decision-making across applications by interpreting multi-modal data. However, scaling these models greatly increases computational costs, which presents challenges in fields like robot manipulation and autonomous driving that require quick, accurate responses. To address the need for deployment on resource-limited hardware, we propose a new quantization framework for IL-based policy models that fine-tunes parameters to enhance robustness against low-bit precision errors during training, thereby maintaining efficiency and reliability under constrained conditions. Our evaluations with representative robot manipulation for 4-bit weight-quantization on a real edge GPU demonstrate that our framework achieves up to 2.5x speedup and 2.5x energy savings while preserving accuracy. For 4-bit weight and activation quantized self-driving models, the framework achieves up to 3.7x speedup and 3.1x energy saving on a low-end GPU. These results highlight the practical potential of deploying IL-based policy models on resource-constrained devices.

## 核心内容
Deep neural network (DNN)-based policy models like vision-language-action (VLA) models are transformative in automating complex decision-making across applications by interpreting multi-modal data. However, scaling these models greatly increases computational costs, which presents challenges in fields like robot manipulation and autonomous driving that require quick, accurate responses. To address the need for deployment on resource-limited hardware, we propose a new quantization framework for IL-based policy models that fine-tunes parameters to enhance robustness against low-bit precision errors during training, thereby maintaining efficiency and reliability under constrained conditions. Our evaluations with representative robot manipulation for 4-bit weight-quantization on a real edge GPU demonstrate that our framework achieves up to 2.5x speedup and 2.5x energy savings while preserving accuracy. For 4-bit weight and activation quantized self-driving models, the framework achieves up to 3.7x speedup and 3.1x energy saving on a low-end GPU. These results highlight the practical potential of deploying IL-based policy models on resource-constrained devices.

## 参考
- http://arxiv.org/abs/2412.01034v1

