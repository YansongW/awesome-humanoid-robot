---
$id: ent_paper_wang_specprune_vla_accelerating_vis_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning'
  zh: SpecPrune-VLA
  ko: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning'
summary:
  en: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (SpecPrune-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Infinigence-AI,
    SII.'
  zh: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (SpecPrune-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Infinigence-AI,
    SII.'
  ko: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (SpecPrune-VLA),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by Shanghai Jiao Tong University, Infinigence-AI,
    SII.'
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
- specprune_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.05614v3.
sources:
- id: src_001
  type: paper
  title: 'SpecPrune-VLA: Accelerating Vision-Language-Action Models via Action-Aware Self-Speculative Pruning (arXiv)'
  url: https://arxiv.org/abs/2509.05614
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: SpecPrune-VLA source
  url: https://doi.org/10.48550/arXiv.2509.05614
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Pruning is a typical acceleration technique for compute-bound models by removing computation on unimportant values. Recently, it has been applied to accelerate Vision-Language-Action (VLA) model inference. However, existing acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios. In this paper, we point out spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and propose the key insight that token selection should combine local information with global context of the model. Based on this, we propose SpecPrune-VLA, a training-free, two-level pruning method with heuristic control. (1) Action-level static pruning. We leverage global history and local attention to statically reduce visual tokens per action. (2) Layer-level dynamic pruning. We prune tokens adaptively per layer based on layer-wise importance. (3) Lightweight action-aware controller: We classify actions as coarse- or fine-grained by the speed of the end effector and adjust pruning aggressiveness accordingly. Extensive experiments show that SpecPrune-VLA achieves up to 1.57$\times$ speedup in LIBERO simulation and 1.70$\times$ on real-world tasks, with negligible success rate degradation.

## 核心内容
Pruning is a typical acceleration technique for compute-bound models by removing computation on unimportant values. Recently, it has been applied to accelerate Vision-Language-Action (VLA) model inference. However, existing acceleration methods focus on local information from the current action step and ignore the global context, leading to >20% success rate drop and limited speedup in some scenarios. In this paper, we point out spatial-temporal consistency in VLA tasks: input images in consecutive steps exhibit high similarity, and propose the key insight that token selection should combine local information with global context of the model. Based on this, we propose SpecPrune-VLA, a training-free, two-level pruning method with heuristic control. (1) Action-level static pruning. We leverage global history and local attention to statically reduce visual tokens per action. (2) Layer-level dynamic pruning. We prune tokens adaptively per layer based on layer-wise importance. (3) Lightweight action-aware controller: We classify actions as coarse- or fine-grained by the speed of the end effector and adjust pruning aggressiveness accordingly. Extensive experiments show that SpecPrune-VLA achieves up to 1.57$\times$ speedup in LIBERO simulation and 1.70$\times$ on real-world tasks, with negligible success rate degradation.

## 参考
- http://arxiv.org/abs/2509.05614v3

