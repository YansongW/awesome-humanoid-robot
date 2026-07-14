---
$id: ent_paper_wen_dexvla_vision_language_model_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control'
  zh: DexVLA
  ko: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control'
summary:
  en: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (DexVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Midea Group, East China Normal University.'
  zh: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (DexVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Midea Group, East China Normal University.'
  ko: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (DexVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Midea Group, East China Normal University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dexvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.05855v3.
sources:
- id: src_001
  type: paper
  title: 'DexVLA: Vision-Language Model with Plug-In Diffusion Expert for General Robot Control (arXiv)'
  url: https://arxiv.org/abs/2502.05855
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: DexVLA source
  url: https://doi.org/10.48550/arXiv.2502.05855
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Enabling robots to perform diverse tasks across varied environments is a central challenge in robot learning. While vision-language-action (VLA) models have shown promise for generalizable robot skills, realizing their full potential requires addressing limitations in action representation and efficient training. Current VLA models often focus on scaling the vision-language model (VLM) component, while the action space representation remains a critical bottleneck. This paper introduces DexVLA, a novel framework designed to enhance the efficiency and generalization capabilities of VLAs for complex, long-horizon tasks across diverse robot embodiments. DexVLA features a novel diffusion-based action expert, scaled to one billion parameters, designed for cross-embodiment learning. A novel embodiment curriculum learning strategy facilitates efficient training: (1) pre-training the diffusion expert that is separable from the VLA on cross-embodiment data, (2) aligning the VLA model to specific embodiments, and (3) post-training for rapid adaptation to new tasks. We conduct comprehensive experiments across multiple embodiments, including single-arm, bimanual, and dexterous hand, demonstrating DexVLA's adaptability to challenging tasks without task-specific adaptation, its ability to learn dexterous skills on novel embodiments with limited data, and its capacity to complete complex, long-horizon tasks using only direct language prompting, such as laundry folding. In all settings, our method demonstrates superior performance compared to state-of-the-art models like Octo, OpenVLA, and Diffusion Policy.

## 核心内容
Enabling robots to perform diverse tasks across varied environments is a central challenge in robot learning. While vision-language-action (VLA) models have shown promise for generalizable robot skills, realizing their full potential requires addressing limitations in action representation and efficient training. Current VLA models often focus on scaling the vision-language model (VLM) component, while the action space representation remains a critical bottleneck. This paper introduces DexVLA, a novel framework designed to enhance the efficiency and generalization capabilities of VLAs for complex, long-horizon tasks across diverse robot embodiments. DexVLA features a novel diffusion-based action expert, scaled to one billion parameters, designed for cross-embodiment learning. A novel embodiment curriculum learning strategy facilitates efficient training: (1) pre-training the diffusion expert that is separable from the VLA on cross-embodiment data, (2) aligning the VLA model to specific embodiments, and (3) post-training for rapid adaptation to new tasks. We conduct comprehensive experiments across multiple embodiments, including single-arm, bimanual, and dexterous hand, demonstrating DexVLA's adaptability to challenging tasks without task-specific adaptation, its ability to learn dexterous skills on novel embodiments with limited data, and its capacity to complete complex, long-horizon tasks using only direct language prompting, such as laundry folding. In all settings, our method demonstrates superior performance compared to state-of-the-art models like Octo, OpenVLA, and Diffusion Policy.

## 参考
- http://arxiv.org/abs/2502.05855v3

