---
$id: ent_paper_wang_sigma_the_key_for_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment'
  zh: Sigma
  ko: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment'
summary:
  en: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (Sigma), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UCSI University.'
  zh: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (Sigma), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UCSI University.'
  ko: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (Sigma), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UCSI University.'
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
- sigma
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00783v3.
sources:
- id: src_001
  type: paper
  title: 'Sigma: The Key for Vision-Language-Action Models toward Telepathic Alignment (arXiv)'
  url: https://arxiv.org/abs/2512.00783
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Sigma source
  url: https://doi.org/10.48550/arXiv.2512.00783
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
To address a fundamental limitation in cognitive systems, namely the absence of a time-updatable mediating thought space between semantics and continuous control, this work constructs and trains a vision-language-action model termed Sigma, deployed on a single RTX 4090. The model is built upon the open-source pi0.5_base backbone, with the svla_so101_pickplace dataset preprocessed into a structured training corpus. An independently designed VLA architecture is introduced to integrate deep semantic understanding with associative reasoning, enabling telepathic-style alignment between perception and action. Training proceeds through iterative optimization of data preprocessing, LoRA-based fine-tuning, and inference-stage adapter design. Evaluation is conducted using offline closed-loop replay, comparing Sigma against the untuned pi0.5_base under identical data conditions. Experimental results indicate a consistent reduction in control MSE across vector-, fragment-, and trajectory-level scales, while preserving the stability of the telepathy norm and semantic-text alignment quality. These findings demonstrate that mind-responsive alignment control can be quantitatively achieved through semantic and associative architectural integration without retraining the base model, providing a reproducible pathway for semantic alignment and intention-driven behavior.

## 核心内容
To address a fundamental limitation in cognitive systems, namely the absence of a time-updatable mediating thought space between semantics and continuous control, this work constructs and trains a vision-language-action model termed Sigma, deployed on a single RTX 4090. The model is built upon the open-source pi0.5_base backbone, with the svla_so101_pickplace dataset preprocessed into a structured training corpus. An independently designed VLA architecture is introduced to integrate deep semantic understanding with associative reasoning, enabling telepathic-style alignment between perception and action. Training proceeds through iterative optimization of data preprocessing, LoRA-based fine-tuning, and inference-stage adapter design. Evaluation is conducted using offline closed-loop replay, comparing Sigma against the untuned pi0.5_base under identical data conditions. Experimental results indicate a consistent reduction in control MSE across vector-, fragment-, and trajectory-level scales, while preserving the stability of the telepathy norm and semantic-text alignment quality. These findings demonstrate that mind-responsive alignment control can be quantitatively achieved through semantic and associative architectural integration without retraining the base model, providing a reproducible pathway for semantic alignment and intention-driven behavior.

## 参考
- http://arxiv.org/abs/2512.00783v3

