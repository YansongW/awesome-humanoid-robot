---
$id: ent_paper_pertsch_fast_efficient_action_tokeniza_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models'
  zh: FAST
  ko: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models'
summary:
  en: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (FAST), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, UC Berkeley, Stanford, and published at RSS25.'
  zh: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (FAST), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, UC Berkeley, Stanford, and published at RSS25.'
  ko: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (FAST), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Physical Intelligence, UC Berkeley, Stanford, and published at RSS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- fast
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.09747v1.
sources:
- id: src_001
  type: paper
  title: 'FAST: Efficient Action Tokenization for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2501.09747
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FAST source
  url: https://doi.org/10.48550/arXiv.2501.09747
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Autoregressive sequence models, such as Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors. However, such models require us to choose a tokenization of our continuous action signals, which determines how the discrete symbols predicted by the model map to continuous robot actions. We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from high-frequency robot data. To address this challenge, we propose a new compression-based tokenization scheme for robot actions, based on the discrete cosine transform. Our tokenization approach, Frequency-space Action Sequence Tokenization (FAST), enables us to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods fail completely. Based on FAST, we release FAST+, a universal robot action tokenizer, trained on 1M real robot action trajectories. It can be used as a black-box tokenizer for a wide range of robot action sequences, with diverse action spaces and control frequencies. Finally, we show that, when combined with the pi0 VLA, our method can scale to training on 10k hours of robot data and match the performance of diffusion VLAs, while reducing training time by up to 5x.

## 核心内容
Autoregressive sequence models, such as Transformer-based vision-language action (VLA) policies, can be tremendously effective for capturing complex and generalizable robotic behaviors. However, such models require us to choose a tokenization of our continuous action signals, which determines how the discrete symbols predicted by the model map to continuous robot actions. We find that current approaches for robot action tokenization, based on simple per-dimension, per-timestep binning schemes, typically perform poorly when learning dexterous skills from high-frequency robot data. To address this challenge, we propose a new compression-based tokenization scheme for robot actions, based on the discrete cosine transform. Our tokenization approach, Frequency-space Action Sequence Tokenization (FAST), enables us to train autoregressive VLAs for highly dexterous and high-frequency tasks where standard discretization methods fail completely. Based on FAST, we release FAST+, a universal robot action tokenizer, trained on 1M real robot action trajectories. It can be used as a black-box tokenizer for a wide range of robot action sequences, with diverse action spaces and control frequencies. Finally, we show that, when combined with the pi0 VLA, our method can scale to training on 10k hours of robot data and match the performance of diffusion VLAs, while reducing training time by up to 5x.

## 参考
- http://arxiv.org/abs/2501.09747v1

