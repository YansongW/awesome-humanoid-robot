---
$id: ent_paper_won_dual_stream_diffusion_for_worl_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
  zh: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
  ko: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model
summary:
  en: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (Dual-Stream Diffusion for World-Model
    Augmented Vision-Language-Action Model), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by KAIST, RLWRLD.
  zh: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (Dual-Stream Diffusion for World-Model
    Augmented Vision-Language-Action Model), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by KAIST, RLWRLD.
  ko: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (Dual-Stream Diffusion for World-Model
    Augmented Vision-Language-Action Model), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by KAIST, RLWRLD.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dual_stream_diffusion_for_worl
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.27607v3.
sources:
- id: src_001
  type: paper
  title: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model (arXiv)
  url: https://arxiv.org/abs/2510.27607
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Dual-Stream Diffusion for World-Model Augmented Vision-Language-Action Model source
  url: https://doi.org/10.48550/arXiv.2510.27607
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Augmenting vision-language-action models (VLAs) with world models is promising for robotic policy learning but faces challenges in jointly predicting states and actions due to the modality gap. To address this, we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework featuring a multimodal diffusion transformer that maintains separate modality streams while enabling cross-modal knowledge sharing. In addition, DUST utilizes independent noise perturbations and a decoupled flow matching loss to learn cross-modal causal relationships. We further introduce an asynchronous sampling method for action and vision tokens that enhances performance through inference-time scaling. Experimental results on simulated benchmarks like RoboCasa and GR-1 show that DUST achieves up to 6% gains over state-of-the-art VLA and world-modeling baselines, with inference-time scaling providing an additional 2-5% improvement. In real-world tasks using the Franka Research 3, DUST outperforms baselines by 10% in success rate. Finally, we demonstrate that DUST enables effective transfer learning through both pretraining on action-free videos and joint-training with heterogeneous robot and human datasets.

## 核心内容
Augmenting vision-language-action models (VLAs) with world models is promising for robotic policy learning but faces challenges in jointly predicting states and actions due to the modality gap. To address this, we propose DUal-STream diffusion (DUST), a world-model augmented VLA framework featuring a multimodal diffusion transformer that maintains separate modality streams while enabling cross-modal knowledge sharing. In addition, DUST utilizes independent noise perturbations and a decoupled flow matching loss to learn cross-modal causal relationships. We further introduce an asynchronous sampling method for action and vision tokens that enhances performance through inference-time scaling. Experimental results on simulated benchmarks like RoboCasa and GR-1 show that DUST achieves up to 6% gains over state-of-the-art VLA and world-modeling baselines, with inference-time scaling providing an additional 2-5% improvement. In real-world tasks using the Franka Research 3, DUST outperforms baselines by 10% in success rate. Finally, we demonstrate that DUST enables effective transfer learning through both pretraining on action-free videos and joint-training with heterogeneous robot and human datasets.

## 参考
- http://arxiv.org/abs/2510.27607v3

