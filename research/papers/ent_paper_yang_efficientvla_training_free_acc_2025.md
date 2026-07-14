---
$id: ent_paper_yang_efficientvla_training_free_acc_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models'
  zh: EfficientVLA
  ko: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models'
summary:
  en: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (EfficientVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, Shanghai
    Jiao Tong University, Harbin Institute of Technology, Xi’an Jiaotong University, University of Electronic Science and
    Technology of China, Anyverse Intelligence, and published at NIPS25.'
  zh: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (EfficientVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, Shanghai
    Jiao Tong University, Harbin Institute of Technology, Xi’an Jiaotong University, University of Electronic Science and
    Technology of China, Anyverse Intelligence, and published at NIPS25.'
  ko: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (EfficientVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by School of Artificial Intelligence, Shanghai
    Jiao Tong University, Harbin Institute of Technology, Xi’an Jiaotong University, University of Electronic Science and
    Technology of China, Anyverse Intelligence, and published at NIPS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- efficientvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.10100v1.
sources:
- id: src_001
  type: paper
  title: 'EfficientVLA: Training-Free Acceleration and Compression for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2506.10100
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EfficientVLA source
  url: https://doi.org/10.48550/arXiv.2506.10100
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability. We introduce EfficientVLA, a structured and training-free inference acceleration framework that systematically eliminates these barriers by cohesively exploiting multifaceted redundancies. EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features. We apply our method to a standard VLA model CogACT, yielding a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

## 核心内容
Vision-Language-Action (VLA) models, particularly diffusion-based architectures, demonstrate transformative potential for embodied intelligence but are severely hampered by high computational and memory demands stemming from extensive inherent and inference-time redundancies. While existing acceleration efforts often target isolated inefficiencies, such piecemeal solutions typically fail to holistically address the varied computational and memory bottlenecks across the entire VLA pipeline, thereby limiting practical deployability. We introduce EfficientVLA, a structured and training-free inference acceleration framework that systematically eliminates these barriers by cohesively exploiting multifaceted redundancies. EfficientVLA synergistically integrates three targeted strategies: (1) pruning of functionally inconsequential layers from the language module, guided by an analysis of inter-layer redundancies; (2) optimizing the visual processing pathway through a task-aware strategy that selects a compact, diverse set of visual tokens, balancing task-criticality with informational coverage; and (3) alleviating temporal computational redundancy within the iterative diffusion-based action head by strategically caching and reusing key intermediate features. We apply our method to a standard VLA model CogACT, yielding a 1.93X inference speedup and reduces FLOPs to 28.9%, with only a 0.6% success rate drop in the SIMPLER benchmark.

## 参考
- http://arxiv.org/abs/2506.10100v1

