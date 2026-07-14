---
$id: ent_paper_ni_swiftvla_unlocking_spatiotempo_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead'
  zh: SwiftVLA
  ko: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead'
summary:
  en: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead (SwiftVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by GigaAI, Peking University, Moxin (Huzhou) Technology
    Co., Ltd., Tsinghua University, X-Humanoid.'
  zh: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead (SwiftVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by GigaAI, Peking University, Moxin (Huzhou) Technology
    Co., Ltd., Tsinghua University, X-Humanoid.'
  ko: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead (SwiftVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by GigaAI, Peking University, Moxin (Huzhou) Technology
    Co., Ltd., Tsinghua University, X-Humanoid.'
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
- swiftvla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.00903v1.
sources:
- id: src_001
  type: paper
  title: 'SwiftVLA: Unlocking Spatiotemporal Dynamics for Lightweight VLA Models at Minimal Overhead (arXiv)'
  url: https://arxiv.org/abs/2512.00903
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SwiftVLA source
  url: https://doi.org/10.48550/arXiv.2512.00903
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models built on pretrained Vision-Language Models (VLMs) show strong potential but are limited in practicality due to their large parameter counts. To mitigate this issue, using a lightweight VLM has been explored, but it compromises spatiotemporal reasoning. Although some methods suggest that incorporating additional 3D inputs can help, they usually rely on large VLMs to fuse 3D and 2D inputs and still lack temporal understanding. Therefore, we propose SwiftVLA, an architecture that enhances a compact model with 4D understanding while preserving design efficiency. Specifically, our approach features a pretrained 4D visual geometry transformer with a temporal cache that extracts 4D features from 2D images. Then, to enhance the VLM's ability to exploit both 2D images and 4D features, we introduce Fusion Tokens, a set of learnable tokens trained with a future prediction objective to generate unified representations for action generation. Finally, we introduce a mask-and-reconstruct strategy that masks 4D inputs to the VLM and trains the VLA to reconstruct them, enabling the VLM to learn effective 4D representations and allowing the 4D branch to be dropped at inference with minimal performance loss. Experiments in real and simulated environments show that SwiftVLA outperforms lightweight baselines and rivals VLAs up to 7 times larger, achieving comparable performance on edge devices while being 18 times faster and reducing memory footprint by 12 times.

## 核心内容
Vision-Language-Action (VLA) models built on pretrained Vision-Language Models (VLMs) show strong potential but are limited in practicality due to their large parameter counts. To mitigate this issue, using a lightweight VLM has been explored, but it compromises spatiotemporal reasoning. Although some methods suggest that incorporating additional 3D inputs can help, they usually rely on large VLMs to fuse 3D and 2D inputs and still lack temporal understanding. Therefore, we propose SwiftVLA, an architecture that enhances a compact model with 4D understanding while preserving design efficiency. Specifically, our approach features a pretrained 4D visual geometry transformer with a temporal cache that extracts 4D features from 2D images. Then, to enhance the VLM's ability to exploit both 2D images and 4D features, we introduce Fusion Tokens, a set of learnable tokens trained with a future prediction objective to generate unified representations for action generation. Finally, we introduce a mask-and-reconstruct strategy that masks 4D inputs to the VLM and trains the VLA to reconstruct them, enabling the VLM to learn effective 4D representations and allowing the 4D branch to be dropped at inference with minimal performance loss. Experiments in real and simulated environments show that SwiftVLA outperforms lightweight baselines and rivals VLAs up to 7 times larger, achieving comparable performance on edge devices while being 18 times faster and reducing memory footprint by 12 times.

## 参考
- http://arxiv.org/abs/2512.00903v1

