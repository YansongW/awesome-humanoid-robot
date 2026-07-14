---
$id: ent_paper_guo_glad_geometric_latent_distilla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models'
  zh: GLaD
  ko: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models'
summary:
  en: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models (GLaD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MBZUAI, University of Illinois Chicago.'
  zh: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models (GLaD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MBZUAI, University of Illinois Chicago.'
  ko: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models (GLaD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by MBZUAI, University of Illinois Chicago.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- glad
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.09619v1.
sources:
- id: src_001
  type: paper
  title: 'GLaD: Geometric Latent Distillation for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2512.09619
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GLaD source
  url: https://doi.org/10.48550/arXiv.2512.09619
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Most existing Vision-Language-Action (VLA) models rely primarily on RGB information, while ignoring geometric cues crucial for spatial reasoning and manipulation. In this work, we introduce GLaD, a geometry-aware VLA framework that incorporates 3D geometric priors during pretraining through knowledge distillation. Rather than distilling geometric features solely into the vision encoder, we align the LLM's hidden states corresponding to visual tokens with features from a frozen geometry-aware vision transformer (VGGT), ensuring that geometric understanding is deeply integrated into the multimodal representations that drive action prediction. Pretrained on the Bridge dataset with this geometry distillation mechanism, GLaD achieves 94.1% average success rate across four LIBERO task suites, outperforming UniVLA (92.5%) which uses identical pretraining data. These results validate that geometry-aware pretraining enhances spatial reasoning and policy generalization without requiring explicit depth sensors or 3D annotations.

## 核心内容
Most existing Vision-Language-Action (VLA) models rely primarily on RGB information, while ignoring geometric cues crucial for spatial reasoning and manipulation. In this work, we introduce GLaD, a geometry-aware VLA framework that incorporates 3D geometric priors during pretraining through knowledge distillation. Rather than distilling geometric features solely into the vision encoder, we align the LLM's hidden states corresponding to visual tokens with features from a frozen geometry-aware vision transformer (VGGT), ensuring that geometric understanding is deeply integrated into the multimodal representations that drive action prediction. Pretrained on the Bridge dataset with this geometry distillation mechanism, GLaD achieves 94.1% average success rate across four LIBERO task suites, outperforming UniVLA (92.5%) which uses identical pretraining data. These results validate that geometry-aware pretraining enhances spatial reasoning and policy generalization without requiring explicit depth sensors or 3D annotations.

## 参考
- http://arxiv.org/abs/2512.09619v1

