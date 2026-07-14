---
$id: ent_paper_xu_vla_cache_efficient_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching'
  zh: VLA-Cache
  ko: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching'
summary:
  en: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (VLA-Cache), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney, Shanghai Jiao Tong University, and published at NIPS25.'
  zh: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (VLA-Cache), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney, Shanghai Jiao Tong University, and published at NIPS25.'
  ko: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (VLA-Cache), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Sydney, Shanghai Jiao Tong University, and published at NIPS25.'
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
- vla_cache
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.02175v2.
sources:
- id: src_001
  type: paper
  title: 'VLA-Cache: Efficient Vision-Language-Action Manipulation via Adaptive Token Caching (arXiv)'
  url: https://arxiv.org/abs/2502.02175
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-Cache source
  url: https://doi.org/10.48550/arXiv.2502.02175
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have demonstrated strong multi-modal reasoning capabilities, enabling direct action generation from visual perception and language instructions in an end-to-end manner. However, their substantial computational cost poses a challenge for real-time robotic control, where rapid decision-making is essential. This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames. Exploiting the temporal continuity in robotic manipulation, VLA-Cache identifies minimally changed tokens between adjacent frames and reuses their cached key-value representations, thereby circumventing redundant computations. Additionally, to maintain action precision, VLA-Cache selectively re-computes task-relevant tokens that are environmentally sensitive, ensuring the fidelity of critical visual information. To further optimize efficiency, we introduce a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens for recomputation. Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7x speedup in CUDA latency and a 15% increase in control frequency, with negligible loss on task success rate. The code and videos can be found at our project page: https://vla-cache.github.io.

## 核心内容
Vision-Language-Action (VLA) models have demonstrated strong multi-modal reasoning capabilities, enabling direct action generation from visual perception and language instructions in an end-to-end manner. However, their substantial computational cost poses a challenge for real-time robotic control, where rapid decision-making is essential. This paper introduces VLA-Cache, a training-free inference acceleration method that reduces computational overhead by adaptively caching and reusing static visual tokens across frames. Exploiting the temporal continuity in robotic manipulation, VLA-Cache identifies minimally changed tokens between adjacent frames and reuses their cached key-value representations, thereby circumventing redundant computations. Additionally, to maintain action precision, VLA-Cache selectively re-computes task-relevant tokens that are environmentally sensitive, ensuring the fidelity of critical visual information. To further optimize efficiency, we introduce a layer adaptive token reusing strategy that dynamically adjusts the reuse ratio based on attention concentration across decoder layers, prioritizing critical tokens for recomputation. Extensive experiments on two simulation platforms (LIBERO and SIMPLER) and a real-world robotic system demonstrate that VLA-Cache achieves up to 1.7x speedup in CUDA latency and a 15% increase in control frequency, with negligible loss on task success rate. The code and videos can be found at our project page: https://vla-cache.github.io.

## 参考
- http://arxiv.org/abs/2502.02175v2

