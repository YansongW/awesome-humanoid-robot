---
$id: ent_paper_zhang_dreamvla_a_vision_language_act_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge'
  zh: DreamVLA
  ko: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge'
summary:
  en: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (DreamVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Eastern Institute of Technology, Tsinghua
    University, Galbot, Peking University, University of Illinois at Urbana-Champaign, University of Science and Technology
    of China.'
  zh: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (DreamVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Eastern Institute of Technology, Tsinghua
    University, Galbot, Peking University, University of Illinois at Urbana-Champaign, University of Science and Technology
    of China.'
  ko: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (DreamVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong University, Eastern Institute of Technology, Tsinghua
    University, Galbot, Peking University, University of Illinois at Urbana-Champaign, University of Science and Technology
    of China.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dreamvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.04447v3.
sources:
- id: src_001
  type: paper
  title: 'DreamVLA: A Vision-Language-Action Model Dreamed with Comprehensive World Knowledge (arXiv)'
  url: https://arxiv.org/abs/2507.04447
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DreamVLA source
  url: https://doi.org/10.48550/arXiv.2507.04447
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation. However, existing methods are limited to challenging image-based forecasting, which suffers from redundant information and lacks comprehensive and critical world knowledge, including dynamic, spatial and semantic information. To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. Specifically, DreamVLA introduces a dynamic-region-guided world knowledge prediction, integrated with the spatial and semantic cues, which provide compact yet comprehensive representations for action planning. This design aligns with how humans interact with the world by first forming abstract multimodal reasoning chains before acting. To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and keeping each representation clean and disentangled. Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features. Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.

## 核心内容
Recent advances in vision-language-action (VLA) models have shown promise in integrating image generation with action prediction to improve generalization and reasoning in robot manipulation. However, existing methods are limited to challenging image-based forecasting, which suffers from redundant information and lacks comprehensive and critical world knowledge, including dynamic, spatial and semantic information. To address these limitations, we propose DreamVLA, a novel VLA framework that integrates comprehensive world knowledge forecasting to enable inverse dynamics modeling, thereby establishing a perception-prediction-action loop for manipulation tasks. Specifically, DreamVLA introduces a dynamic-region-guided world knowledge prediction, integrated with the spatial and semantic cues, which provide compact yet comprehensive representations for action planning. This design aligns with how humans interact with the world by first forming abstract multimodal reasoning chains before acting. To mitigate interference among the dynamic, spatial and semantic information during training, we adopt a block-wise structured attention mechanism that masks their mutual attention, preventing information leakage and keeping each representation clean and disentangled. Moreover, to model the conditional distribution over future actions, we employ a diffusion-based transformer that disentangles action representations from shared latent features. Extensive experiments on both real-world and simulation environments demonstrate that DreamVLA achieves 76.7% success rate on real robot tasks and 4.44 average length on the CALVIN ABC-D benchmarks.

## 参考
- http://arxiv.org/abs/2507.04447v3

