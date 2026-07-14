---
$id: ent_paper_dong_emma_generalizing_real_world_r_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer'
  zh: EMMA
  ko: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer'
summary:
  en: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (EMMA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Singapore University of Technology and Design, Deepmind.'
  zh: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (EMMA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Singapore University of Technology and Design, Deepmind.'
  ko: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (EMMA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Singapore University of Technology and Design, Deepmind.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- emma
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.22407v2.
sources:
- id: src_001
  type: paper
  title: 'EMMA: Generalizing Real-World Robot Manipulation via Generative Visual Transfer (arXiv)'
  url: https://arxiv.org/abs/2509.22407
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EMMA source
  url: https://doi.org/10.48550/arXiv.2509.22407
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The generalization of vision-language-action (VLA) models heavily relies on diverse training data. However, acquiring large-scale data for robot manipulation across varied object appearances is costly and labor-intensive. To address this limitation, we introduce Embodied Manipulation Media Adaptation (EMMA), a framework for augmenting VLA policies that combines a generative data engine with an effective training pipeline. We introduce DreamTransfer, a diffusion Transformer-based architecture for generating multi-view consistent and geometrically grounded embodied manipulation videos. DreamTransfer enables visual editing of robot videos through prompts, allowing for changes to the foreground, background, and lighting while preserving their 3D structure and geometric validity. We also utilize a hybrid training set of real and generated data and propose AdaMix to enhance the training process. AdaMix is a training strategy that adaptively weights samples according to policy performance to emphasize challenging samples. Comprehensive evaluations demonstrate that videos created by DreamTransfer yield substantial improvements over previous video generation techniques in multi-view consistency, geometric accuracy, and text-conditioning precision. We conduct extensive evaluations with a total of more than 1800 trials in both simulated and real-world robotic environments. In real-world robotic tasks with zero-shot visual settings, our framework achieves a relative performance increase of over 92% compared to training with real data alone, and improves by an additional 17% with AdaMix, demonstrating its efficacy in enhancing policy generalization.

## 核心内容
The generalization of vision-language-action (VLA) models heavily relies on diverse training data. However, acquiring large-scale data for robot manipulation across varied object appearances is costly and labor-intensive. To address this limitation, we introduce Embodied Manipulation Media Adaptation (EMMA), a framework for augmenting VLA policies that combines a generative data engine with an effective training pipeline. We introduce DreamTransfer, a diffusion Transformer-based architecture for generating multi-view consistent and geometrically grounded embodied manipulation videos. DreamTransfer enables visual editing of robot videos through prompts, allowing for changes to the foreground, background, and lighting while preserving their 3D structure and geometric validity. We also utilize a hybrid training set of real and generated data and propose AdaMix to enhance the training process. AdaMix is a training strategy that adaptively weights samples according to policy performance to emphasize challenging samples. Comprehensive evaluations demonstrate that videos created by DreamTransfer yield substantial improvements over previous video generation techniques in multi-view consistency, geometric accuracy, and text-conditioning precision. We conduct extensive evaluations with a total of more than 1800 trials in both simulated and real-world robotic environments. In real-world robotic tasks with zero-shot visual settings, our framework achieves a relative performance increase of over 92% compared to training with real data alone, and improves by an additional 17% with AdaMix, demonstrating its efficacy in enhancing policy generalization.

## 参考
- http://arxiv.org/abs/2509.22407v2

