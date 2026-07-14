---
$id: ent_paper_lyu_omnisat_compact_action_token_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OmniSAT: Compact Action Token, Faster Auto Regression'
  zh: OmniSAT
  ko: 'OmniSAT: Compact Action Token, Faster Auto Regression'
summary:
  en: 'OmniSAT: Compact Action Token, Faster Auto Regression (OmniSAT), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by University of Science and Technology of China.'
  zh: 'OmniSAT: Compact Action Token, Faster Auto Regression (OmniSAT), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by University of Science and Technology of China.'
  ko: 'OmniSAT: Compact Action Token, Faster Auto Regression (OmniSAT), is a 2025 large vision-language-action model for robotic
    manipulation, introduced by University of Science and Technology of China.'
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
- omnisat
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.09667v1.
sources:
- id: src_001
  type: paper
  title: 'OmniSAT: Compact Action Token, Faster Auto Regression (arXiv)'
  url: https://arxiv.org/abs/2510.09667
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OmniSAT source
  url: https://doi.org/10.48550/arXiv.2510.09667
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Existing Vision-Language-Action (VLA) models can be broadly categorized into diffusion-based and auto-regressive (AR) approaches: diffusion models capture continuous action distributions but rely on computationally heavy iterative denoising. In contrast, AR models enable efficient optimization and flexible sequence construction, making them better suited for large-scale pretraining. To further improve AR efficiency, particularly when action chunks induce extended and high-dimensional sequences, prior work applies entropy-guided and token-frequency techniques to shorten the sequence length. However, such compression struggled with \textit{poor reconstruction or inefficient compression}. Motivated by this, we introduce an Omni Swift Action Tokenizer, which learns a compact, transferable action representation. Specifically, we first normalize value ranges and temporal horizons to obtain a consistent representation with B-Spline encoding. Then, we apply multi-stage residual quantization to the position, rotation, and gripper subspaces, producing compressed discrete tokens with coarse-to-fine granularity for each part. After pre-training on the large-scale dataset Droid, the resulting discrete tokenization shortens the training sequence by 6.8$\times$, and lowers the target entropy. To further explore the potential of OmniSAT, we develop a cross-embodiment learning strategy that builds on the unified action-pattern space and jointly leverages robot and human demonstrations. It enables scalable auxiliary supervision from heterogeneous egocentric videos. Across diverse real-robot and simulation experiments, OmniSAT encompasses higher compression while preserving reconstruction quality, enabling faster AR training convergence and model performance.

## 核心内容
Existing Vision-Language-Action (VLA) models can be broadly categorized into diffusion-based and auto-regressive (AR) approaches: diffusion models capture continuous action distributions but rely on computationally heavy iterative denoising. In contrast, AR models enable efficient optimization and flexible sequence construction, making them better suited for large-scale pretraining. To further improve AR efficiency, particularly when action chunks induce extended and high-dimensional sequences, prior work applies entropy-guided and token-frequency techniques to shorten the sequence length. However, such compression struggled with \textit{poor reconstruction or inefficient compression}. Motivated by this, we introduce an Omni Swift Action Tokenizer, which learns a compact, transferable action representation. Specifically, we first normalize value ranges and temporal horizons to obtain a consistent representation with B-Spline encoding. Then, we apply multi-stage residual quantization to the position, rotation, and gripper subspaces, producing compressed discrete tokens with coarse-to-fine granularity for each part. After pre-training on the large-scale dataset Droid, the resulting discrete tokenization shortens the training sequence by 6.8$\times$, and lowers the target entropy. To further explore the potential of OmniSAT, we develop a cross-embodiment learning strategy that builds on the unified action-pattern space and jointly leverages robot and human demonstrations. It enables scalable auxiliary supervision from heterogeneous egocentric videos. Across diverse real-robot and simulation experiments, OmniSAT encompasses higher compression while preserving reconstruction quality, enabling faster AR training convergence and model performance.

## 参考
- http://arxiv.org/abs/2510.09667v1

