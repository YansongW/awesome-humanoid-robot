---
$id: ent_paper_yuan_depthvla_enhancing_vision_lang_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning'
  zh: DepthVLA
  ko: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning'
summary:
  en: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (DepthVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Galaxea AI.'
  zh: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (DepthVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Galaxea AI.'
  ko: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (DepthVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Galaxea AI.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- depthvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.13375v1.
sources:
- id: src_001
  type: paper
  title: 'DepthVLA: Enhancing Vision-Language-Action Models with Depth-Aware Spatial Reasoning (arXiv)'
  url: https://arxiv.org/abs/2510.13375
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DepthVLA source
  url: https://doi.org/10.48550/arXiv.2510.13375
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently shown impressive generalization and language-guided manipulation capabilities. However, their performance degrades on tasks requiring precise spatial reasoning due to limited spatial reasoning inherited from Vision-Language Models (VLMs). Existing VLAs rely on extensive action-data pretraining to ground VLMs in 3D space, which reduces training efficiency and is still insufficient for accurate spatial understanding. In this work, we present DepthVLA, a simple yet effective VLA architecture that explicitly incorporates spatial awareness through a pretrained depth prediction module. DepthVLA adopts a mixture-of-transformers design that unifies a VLM, a depth transformer, and an action expert with fully shared attentions, forming an end-to-end model with enhanced spatial reasoning. Extensive evaluations in both real-world and simulated environments show that DepthVLA outperforms state-of-the-art approaches, achieving 78.5% vs. 65.0% progress in real-world tasks, 94.9% vs. 93.6% in the LIBERO simulator, and 74.8% vs. 58.8% in the Simpler simulator. Our code will be made publicly available.

## 核心内容
Vision-Language-Action (VLA) models have recently shown impressive generalization and language-guided manipulation capabilities. However, their performance degrades on tasks requiring precise spatial reasoning due to limited spatial reasoning inherited from Vision-Language Models (VLMs). Existing VLAs rely on extensive action-data pretraining to ground VLMs in 3D space, which reduces training efficiency and is still insufficient for accurate spatial understanding. In this work, we present DepthVLA, a simple yet effective VLA architecture that explicitly incorporates spatial awareness through a pretrained depth prediction module. DepthVLA adopts a mixture-of-transformers design that unifies a VLM, a depth transformer, and an action expert with fully shared attentions, forming an end-to-end model with enhanced spatial reasoning. Extensive evaluations in both real-world and simulated environments show that DepthVLA outperforms state-of-the-art approaches, achieving 78.5% vs. 65.0% progress in real-world tasks, 94.9% vs. 93.6% in the LIBERO simulator, and 74.8% vs. 58.8% in the Simpler simulator. Our code will be made publicly available.

## 参考
- http://arxiv.org/abs/2510.13375v1

