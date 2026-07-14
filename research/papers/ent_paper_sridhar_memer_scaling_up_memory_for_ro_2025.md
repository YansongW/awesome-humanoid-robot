---
$id: ent_paper_sridhar_memer_scaling_up_memory_for_ro_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval'
  zh: MemER
  ko: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval'
summary:
  en: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (MemER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University.'
  zh: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (MemER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University.'
  ko: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (MemER), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Stanford University.'
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
- memer
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.20328v1.
sources:
- id: src_001
  type: paper
  title: 'MemER: Scaling Up Memory for Robot Control via Experience Retrieval (arXiv)'
  url: https://arxiv.org/abs/2510.20328
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MemER source
  url: https://doi.org/10.48550/arXiv.2510.20328
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humans routinely rely on memory to perform tasks, yet most robot policies lack this capability; our goal is to endow robot policies with the same ability. Naively conditioning on long observation histories is computationally expensive and brittle under covariate shift, while indiscriminate subsampling of history leads to irrelevant or redundant information. We propose a hierarchical policy framework, where the high-level policy is trained to select and track previous relevant keyframes from its experience. The high-level policy uses selected keyframes and the most recent frames when generating text instructions for a low-level policy to execute. This design is compatible with existing vision-language-action (VLA) models and enables the system to efficiently reason over long-horizon dependencies. In our experiments, we finetune Qwen2.5-VL-7B-Instruct and $π_{0.5}$ as the high-level and low-level policies respectively, using demonstrations supplemented with minimal language annotations. Our approach, MemER, outperforms prior methods on three real-world long-horizon robotic manipulation tasks that require minutes of memory. Videos and code can be found at https://jen-pan.github.io/memer/.

## 核心内容
Humans routinely rely on memory to perform tasks, yet most robot policies lack this capability; our goal is to endow robot policies with the same ability. Naively conditioning on long observation histories is computationally expensive and brittle under covariate shift, while indiscriminate subsampling of history leads to irrelevant or redundant information. We propose a hierarchical policy framework, where the high-level policy is trained to select and track previous relevant keyframes from its experience. The high-level policy uses selected keyframes and the most recent frames when generating text instructions for a low-level policy to execute. This design is compatible with existing vision-language-action (VLA) models and enables the system to efficiently reason over long-horizon dependencies. In our experiments, we finetune Qwen2.5-VL-7B-Instruct and $π_{0.5}$ as the high-level and low-level policies respectively, using demonstrations supplemented with minimal language annotations. Our approach, MemER, outperforms prior methods on three real-world long-horizon robotic manipulation tasks that require minutes of memory. Videos and code can be found at https://jen-pan.github.io/memer/.

## 参考
- http://arxiv.org/abs/2510.20328v1

