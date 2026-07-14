---
$id: ent_paper_syed_expres_vla_specializing_vision_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval'
  zh: ExpReS-VLA
  ko: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval'
summary:
  en: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (ExpReS-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University.'
  zh: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (ExpReS-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University.'
  ko: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (ExpReS-VLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Carnegie Mellon University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- expres_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.06202v2.
sources:
- id: src_001
  type: paper
  title: 'ExpReS-VLA: Specializing Vision-Language-Action Models Through Experience Replay and Retrieval (arXiv)'
  url: https://arxiv.org/abs/2511.06202
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ExpReS-VLA source
  url: https://doi.org/10.48550/arXiv.2511.06202
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the $k$ most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including $π_0$ (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

## 核心内容
Vision-Language-Action (VLA) models like OpenVLA demonstrate impressive zero-shot generalization across robotic manipulation tasks but struggle to adapt to specific deployment environments where consistent high performance on a limited set of tasks is more valuable than broad generalization. We present EXPierence replayed, REtrieval augmented, Specialized VLA (ExpReS-VLA), a method that enables rapid on-device adaptation of pre-trained VLAs to target domains while preventing catastrophic forgetting through compressed experience replay and retrieval-augmented generation. Our approach maintains a memory-efficient buffer by storing extracted embeddings from OpenVLA's frozen vision backbone, reducing storage requirements by 97% compared to raw image-action pairs. During deployment, ExpReS-VLA retrieves the $k$ most similar past experiences using cosine similarity to augment training batches, while a prioritized experience replay buffer preserves recently successful trajectories. To leverage failed attempts, we introduce Thresholded Hybrid Contrastive Loss (THCL), enabling the model to learn from both successful and unsuccessful demonstrations. Experiments on the LIBERO benchmark show improvements from 82.6% to 93.1% on spatial reasoning and 61% to 72.3% on long-horizon tasks over base OpenVLA, with gains across architectures including $π_0$ (+3.2 points) and OpenVLA-OFT (+1.7 points). Physical robot experiments across five tasks demonstrate 98% success on both in-distribution and out-of-distribution conditions, improving from 84.7% and 32% respectively for naive fine-tuning. Adaptation completes in 31 seconds using 12 demonstrations on a single RTX 5090.

## 参考
- http://arxiv.org/abs/2511.06202v2

