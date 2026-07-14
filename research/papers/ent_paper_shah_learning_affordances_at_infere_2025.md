---
$id: ent_paper_shah_learning_affordances_at_infere_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Affordances at Inference-Time for Vision-Language-Action Models
  zh: LITEN
  ko: Learning Affordances at Inference-Time for Vision-Language-Action Models
summary:
  en: Learning Affordances at Inference-Time for Vision-Language-Action Models (LITEN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Physical Intelligence.
  zh: Learning Affordances at Inference-Time for Vision-Language-Action Models (LITEN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Physical Intelligence.
  ko: Learning Affordances at Inference-Time for Vision-Language-Action Models (LITEN), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by UC Berkeley, Physical Intelligence.
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
- liten
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.19752v1.
sources:
- id: src_001
  type: paper
  title: Learning Affordances at Inference-Time for Vision-Language-Action Models (arXiv)
  url: https://arxiv.org/abs/2510.19752
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LITEN source
  url: https://doi.org/10.48550/arXiv.2510.19752
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Solving complex real-world control tasks often takes multiple tries: if we fail at first, we reflect on what went wrong, and change our strategy accordingly to avoid making the same mistake. In robotics, Vision-Language-Action models (VLAs) offer a promising path towards solving complex control tasks, but lack the ability to contextually and dynamically readjust behavior when they fail to accomplish a task. In this work, we introduce Learning from Inference-Time Execution (LITEN), which connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA. Our approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts. Unlike similar approaches to self-refinement in non-robotics domains, LITEN must reflect on unstructured real-world robot trajectories (e.g., raw videos), which requires structured guiderails during assessment. Our experimental results demonstrate LITEN is able to effectively learn from past experience to generate plans that use high-affordance instructions to accomplish long-horizon tasks.

## 核心内容
Solving complex real-world control tasks often takes multiple tries: if we fail at first, we reflect on what went wrong, and change our strategy accordingly to avoid making the same mistake. In robotics, Vision-Language-Action models (VLAs) offer a promising path towards solving complex control tasks, but lack the ability to contextually and dynamically readjust behavior when they fail to accomplish a task. In this work, we introduce Learning from Inference-Time Execution (LITEN), which connects a VLA low-level policy to a high-level VLM that conditions on past experiences by including them in-context, allowing it to learn the affordances and capabilities of the low-level VLA. Our approach iterates between a reasoning phase that generates and executes plans for the low-level VLA, and an assessment phase that reflects on the resulting execution and draws useful conclusions to be included in future reasoning contexts. Unlike similar approaches to self-refinement in non-robotics domains, LITEN must reflect on unstructured real-world robot trajectories (e.g., raw videos), which requires structured guiderails during assessment. Our experimental results demonstrate LITEN is able to effectively learn from past experience to generate plans that use high-affordance instructions to accomplish long-horizon tasks.

## 参考
- http://arxiv.org/abs/2510.19752v1

