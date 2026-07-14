---
$id: ent_paper_sridhar_ricl_adding_in_context_adaptab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models'
  zh: RICL
  ko: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models'
summary:
  en: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (RICL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pennsylvania, and published at CoRL25.'
  zh: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (RICL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pennsylvania, and published at CoRL25.'
  ko: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (RICL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by University of Pennsylvania, and published at CoRL25.'
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
- ricl
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.02062v1.
sources:
- id: src_001
  type: paper
  title: 'RICL: Adding In-Context Adaptability to Pre-Trained Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2508.02062
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RICL source
  url: https://doi.org/10.48550/arXiv.2508.02062
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Multi-task ``vision-language-action'' (VLA) models have recently demonstrated increasing promise as generalist foundation models for robotics, achieving non-trivial performance out of the box on new tasks in new environments. However, for such models to be truly useful, an end user must have easy means to teach them to improve. For language and vision models, the emergent ability to perform in-context learning (ICL) has proven to be a versatile and highly useful interface to easily teach new tasks with no parameter finetuning. Unfortunately, VLAs pre-trained with imitation learning objectives do not naturally acquire ICL abilities. In this paper, we demonstrate that, with the right finetuning recipe and a small robot demonstration dataset, it is possible to inject in-context adaptability post hoc into such a VLA. After retraining for in-context learning (RICL), our system permits an end user to provide a small number (10-20) of demonstrations for a new task. RICL then fetches the most relevant portions of those demonstrations into the VLA context to exploit ICL, performing the new task and boosting task performance. We apply RICL to inject ICL into the $π_{0}$-FAST VLA, and show that it permits large in-context improvements for a variety of new manipulation tasks with only 20 demonstrations per task, without any parameter updates. When parameter updates on the target task demonstrations is possible, RICL finetuning further boosts performance. We release code and model weights for RICL-$π_{0}$-FAST alongside the paper to enable, for the first time, a simple in-context learning interface for new manipulation tasks. Website: https://ricl-vla.github.io.

## 核心内容
Multi-task ``vision-language-action'' (VLA) models have recently demonstrated increasing promise as generalist foundation models for robotics, achieving non-trivial performance out of the box on new tasks in new environments. However, for such models to be truly useful, an end user must have easy means to teach them to improve. For language and vision models, the emergent ability to perform in-context learning (ICL) has proven to be a versatile and highly useful interface to easily teach new tasks with no parameter finetuning. Unfortunately, VLAs pre-trained with imitation learning objectives do not naturally acquire ICL abilities. In this paper, we demonstrate that, with the right finetuning recipe and a small robot demonstration dataset, it is possible to inject in-context adaptability post hoc into such a VLA. After retraining for in-context learning (RICL), our system permits an end user to provide a small number (10-20) of demonstrations for a new task. RICL then fetches the most relevant portions of those demonstrations into the VLA context to exploit ICL, performing the new task and boosting task performance. We apply RICL to inject ICL into the $π_{0}$-FAST VLA, and show that it permits large in-context improvements for a variety of new manipulation tasks with only 20 demonstrations per task, without any parameter updates. When parameter updates on the target task demonstrations is possible, RICL finetuning further boosts performance. We release code and model weights for RICL-$π_{0}$-FAST alongside the paper to enable, for the first time, a simple in-context learning interface for new manipulation tasks. Website: https://ricl-vla.github.io.

## 参考
- http://arxiv.org/abs/2508.02062v1

