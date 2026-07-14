---
$id: ent_paper_zhou_vla_4d_embedding_4d_awareness_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation'
  zh: VLA-4D
  ko: 'VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation'
summary:
  en: 'VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation
    (VLA-4D), is a 2025 large vision-language-action model for robotic manipulation, introduced by School of Computing, National
    University of Singapore, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology.'
  zh: 'VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation
    (VLA-4D), is a 2025 large vision-language-action model for robotic manipulation, introduced by School of Computing, National
    University of Singapore, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology.'
  ko: 'VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation
    (VLA-4D), is a 2025 large vision-language-action model for robotic manipulation, introduced by School of Computing, National
    University of Singapore, School of Artificial Intelligence and Automation, Huazhong University of Science and Technology.'
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
- vla_4d
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.17199v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-4D: Embedding 4D Awareness into Vision-Language-Action Models for SpatioTemporally Coherent Robotic Manipulation
    (arXiv)'
  url: https://arxiv.org/abs/2511.17199
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-4D source
  url: https://doi.org/10.48550/arXiv.2511.17199
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models show potential for general robotic tasks, but remain challenging in spatiotemporally coherent manipulation, which requires fine-grained representations. Typically, existing methods embed 3D positions into visual representations to enhance the spatial precision of actions. However, these methods struggle to achieve temporally coherent control over action execution. In this work, we propose VLA-4D, a general VLA model with 4D awareness for spatiotemporally coherent robotic manipulation. Our model is guided by two key designs: 1) 4D-aware visual representation. We extract visual features, embed 1D time into 3D positions for 4D embeddings, and fuse them into a unified visual representation via a cross-attention mechanism. 2) Spatiotemporal action representation. We extend conventional spatial action representations with temporal information to enable the spatiotemporal planning, and align the multimodal representations into the LLM for spatiotemporal action prediction. Within this unified framework, the designed visual and action representations jointly make robotic manipulation spatially-smooth and temporally-coherent. In addition, we extend the VLA dataset with temporal action annotations for fine-tuning our model. Extensive experiments have been conducted to verify the superiority of our method across different tasks of robotic manipulation.

## 核心内容
Vision-language-action (VLA) models show potential for general robotic tasks, but remain challenging in spatiotemporally coherent manipulation, which requires fine-grained representations. Typically, existing methods embed 3D positions into visual representations to enhance the spatial precision of actions. However, these methods struggle to achieve temporally coherent control over action execution. In this work, we propose VLA-4D, a general VLA model with 4D awareness for spatiotemporally coherent robotic manipulation. Our model is guided by two key designs: 1) 4D-aware visual representation. We extract visual features, embed 1D time into 3D positions for 4D embeddings, and fuse them into a unified visual representation via a cross-attention mechanism. 2) Spatiotemporal action representation. We extend conventional spatial action representations with temporal information to enable the spatiotemporal planning, and align the multimodal representations into the LLM for spatiotemporal action prediction. Within this unified framework, the designed visual and action representations jointly make robotic manipulation spatially-smooth and temporally-coherent. In addition, we extend the VLA dataset with temporal action annotations for fine-tuning our model. Extensive experiments have been conducted to verify the superiority of our method across different tasks of robotic manipulation.

## 参考
- http://arxiv.org/abs/2511.17199v1

