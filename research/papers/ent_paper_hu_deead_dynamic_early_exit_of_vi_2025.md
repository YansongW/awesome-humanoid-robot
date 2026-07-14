---
$id: ent_paper_hu_deead_dynamic_early_exit_of_vi_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving'
  zh: DeeAD
  ko: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving'
summary:
  en: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (DeeAD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by City University of Hongkong, Mohamed bin Zayed University of Artificial
    Intelligence.'
  zh: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (DeeAD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by City University of Hongkong, Mohamed bin Zayed University of Artificial
    Intelligence.'
  ko: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (DeeAD), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by City University of Hongkong, Mohamed bin Zayed University of Artificial
    Intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- deead
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.20720v1.
sources:
- id: src_001
  type: paper
  title: 'DeeAD: Dynamic Early Exit of Vision-Language Action for Efficient Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.20720
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DeeAD source
  url: https://doi.org/10.48550/arXiv.2511.20720
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language Action (VLA) models unify perception, reasoning, and trajectory generation for autonomous driving, but suffer from significant inference latency due to deep transformer stacks. We present DeeAD, a training-free, action-guided early-exit framework that accelerates VLA planning by evaluating the physical feasibility of intermediate trajectories. Instead of relying on confidence scores, DeeAD terminates inference when predicted trajectories align with lightweight planning priors (e.g., Navigation or Low-precision Planning) within a tolerable deviation (<2m). To improve efficiency, we introduce a multi-hop controller that adaptively skips redundant layers based on the change rate of scores. DeeAD integrates into existing VLA models, such as ORION, without requiring retraining. Experiments on the Bench2Drive benchmark demonstrate up to 28% transformer-layer sparsity and 29% latency reduction, while preserving planning quality and safety.

## 核心内容
Vision-Language Action (VLA) models unify perception, reasoning, and trajectory generation for autonomous driving, but suffer from significant inference latency due to deep transformer stacks. We present DeeAD, a training-free, action-guided early-exit framework that accelerates VLA planning by evaluating the physical feasibility of intermediate trajectories. Instead of relying on confidence scores, DeeAD terminates inference when predicted trajectories align with lightweight planning priors (e.g., Navigation or Low-precision Planning) within a tolerable deviation (<2m). To improve efficiency, we introduce a multi-hop controller that adaptively skips redundant layers based on the change rate of scores. DeeAD integrates into existing VLA models, such as ORION, without requiring retraining. Experiments on the Bench2Drive benchmark demonstrate up to 28% transformer-layer sparsity and 29% latency reduction, while preserving planning quality and safety.

## 参考
- http://arxiv.org/abs/2511.20720v1

