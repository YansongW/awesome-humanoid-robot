---
$id: ent_paper_zheng_x_vla_soft_prompted_transforme_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model'
  zh: X-VLA
  ko: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model'
summary:
  en: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model (X-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua
    University, Shanghai AI Lab, Peking University.'
  zh: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model (X-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua
    University, Shanghai AI Lab, Peking University.'
  ko: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model (X-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua
    University, Shanghai AI Lab, Peking University.'
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
- vision_language_action
- vla
- x_vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10274v1.
sources:
- id: src_001
  type: paper
  title: 'X-VLA: Soft-Prompted Transformer as Scalable Cross-Embodiment Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2510.10274
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: X-VLA source
  url: https://doi.org/10.48550/arXiv.2510.10274
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Successful generalist Vision-Language-Action (VLA) models rely on effective training across diverse robotic platforms with large-scale, cross-embodiment, heterogeneous datasets. To facilitate and leverage the heterogeneity in rich, diverse robotic data sources, we propose a novel Soft Prompt approach with minimally added parameters, by infusing prompt learning concepts into cross-embodiment robot learning and introducing separate sets of learnable embeddings for each distinct data source. These embeddings serve as embodiment-specific prompts, which in unity empower VLA models with effective exploitation of varying cross-embodiment features. Our new X-VLA, a neat flow-matching-based VLA architecture, relies exclusively on soft-prompted standard Transformer encoders, enjoying both scalability and simplicity. Evaluated across 6 simulations as well as 3 real-world robots, our 0.9B instantiation-X-VLA-0.9B simultaneously achieves SOTA performance over a sweep of benchmarks, demonstrating superior results on a wide axes of capabilities, from flexible dexterity to quick adaptation across embodiments, environments, and tasks. Website: https://thu-air-dream.github.io/X-VLA/

## 核心内容
Successful generalist Vision-Language-Action (VLA) models rely on effective training across diverse robotic platforms with large-scale, cross-embodiment, heterogeneous datasets. To facilitate and leverage the heterogeneity in rich, diverse robotic data sources, we propose a novel Soft Prompt approach with minimally added parameters, by infusing prompt learning concepts into cross-embodiment robot learning and introducing separate sets of learnable embeddings for each distinct data source. These embeddings serve as embodiment-specific prompts, which in unity empower VLA models with effective exploitation of varying cross-embodiment features. Our new X-VLA, a neat flow-matching-based VLA architecture, relies exclusively on soft-prompted standard Transformer encoders, enjoying both scalability and simplicity. Evaluated across 6 simulations as well as 3 real-world robots, our 0.9B instantiation-X-VLA-0.9B simultaneously achieves SOTA performance over a sweep of benchmarks, demonstrating superior results on a wide axes of capabilities, from flexible dexterity to quick adaptation across embodiments, environments, and tasks. Website: https://thu-air-dream.github.io/X-VLA/

## 参考
- http://arxiv.org/abs/2510.10274v1

