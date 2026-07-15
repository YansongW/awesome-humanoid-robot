---
$id: ent_paper_li_3ds_vla_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 3DS-VLA
  zh: 3DS-VLA
  ko: 3DS-VLA
summary:
  en: 3DS-VLA (3DS-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by CFCS, School
    of Computer Science, Peking University, PKU-Agibot Lab, State Key Laboratory of Multimedia Information Processing, School
    of Computer Science, Peking University, CUHK, and published at CoRL25.
  zh: 3DS-VLA (3DS-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by CFCS, School
    of Computer Science, Peking University, PKU-Agibot Lab, State Key Laboratory of Multimedia Information Processing, School
    of Computer Science, Peking University, CUHK, and published at CoRL25.
  ko: 3DS-VLA (3DS-VLA), is a 2025 large vision-language-action model for robotic manipulation, introduced by CFCS, School
    of Computer Science, Peking University, PKU-Agibot Lab, State Key Laboratory of Multimedia Information Processing, School
    of Computer Science, Peking University, CUHK, and published at CoRL25.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- 3ds_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2403.09631v1.
sources:
- id: src_001
  type: paper
  title: 3DS-VLA source
  url: https://proceedings.mlr.press/v305/li25g.html
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world. Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between actions and dynamics. In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly. To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a generative world model. Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the embodied environment. Furthermore, to inject generation abilities into the model, we train a series of embodied diffusion models and align them into the LLM for predicting the goal images and point clouds. To train our 3D-VLA, we curate a large-scale 3D embodied instruction dataset by extracting vast 3D-related information from existing robotics datasets. Our experiments on held-in datasets demonstrate that 3D-VLA significantly improves the reasoning, multimodal generation, and planning capabilities in embodied environments, showcasing its potential in real-world applications.

## 核心内容
Recent vision-language-action (VLA) models rely on 2D inputs, lacking integration with the broader realm of the 3D physical world. Furthermore, they perform action prediction by learning a direct mapping from perception to action, neglecting the vast dynamics of the world and the relations between actions and dynamics. In contrast, human beings are endowed with world models that depict imagination about future scenarios to plan actions accordingly. To this end, we propose 3D-VLA by introducing a new family of embodied foundation models that seamlessly link 3D perception, reasoning, and action through a generative world model. Specifically, 3D-VLA is built on top of a 3D-based large language model (LLM), and a set of interaction tokens is introduced to engage with the embodied environment. Furthermore, to inject generation abilities into the model, we train a series of embodied diffusion models and align them into the LLM for predicting the goal images and point clouds. To train our 3D-VLA, we curate a large-scale 3D embodied instruction dataset by extracting vast 3D-related information from existing robotics datasets. Our experiments on held-in datasets demonstrate that 3D-VLA significantly improves the reasoning, multimodal generation, and planning capabilities in embodied environments, showcasing its potential in real-world applications.

## 参考
- http://arxiv.org/abs/2403.09631v1

