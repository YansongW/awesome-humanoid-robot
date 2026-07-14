---
$id: ent_paper_gu_usim_and_u0_a_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots'
  zh: USIM & U0
  ko: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots'
summary:
  en: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (USIM & U0), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences,
    Key Laboratory of Cognition and Decision Intelligence for Complex Systems.'
  zh: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (USIM & U0), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences,
    Key Laboratory of Cognition and Decision Intelligence for Complex Systems.'
  ko: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (USIM & U0), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Institute of Automation, Chinese Academy of Sciences,
    Key Laboratory of Cognition and Decision Intelligence for Complex Systems.'
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
- usim_u0
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.07869v4.
sources:
- id: src_001
  type: paper
  title: 'USIM and U0: A Vision-Language-Action Dataset and Model for General Underwater Robots (arXiv)'
  url: https://arxiv.org/abs/2510.07869
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: USIM & U0 source
  url: https://doi.org/10.48550/arXiv.2510.07869
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Underwater environments pose unique challenges for robotic navigation and manipulation. While existing research has primarily focused on task-specific methods, studies on general-purpose intelligence for multi-task execution remain scarce. To address this gap, we propose a unified framework for general-purpose underwater robots that integrates perception and action driven by language instructions. First, we develop a data synthesis pipeline to construct USIM, a simulation-based dataset which comprises over 905K frames from 2275 trajectories, totaling approximately 25 hours of BlueROV2 interactions. Furthermore, we propose U0, a vision-language-action (VLA) model capable of executing various tasks from obstacle-avoidance navigation to three-dimensional mobile manipulation. The model features a convolution-attention-based perception (CAP) module, which incorporates target pose estimation as an auxiliary task to explicitly bolster the model's spatial awareness. For evaluation, we establish a systematic assessment framework and an automated pipeline encompassing both offline metrics and online task execution. Experimental results demonstrate that the USIM dataset significantly empowers existing VLA models to adapt to underwater scenarios. Notably, our U0 model achieves state-of-the-art performance: it reduces the offline mean action prediction error to 0.0359 and achieves an overall online success rate of 43.1%, marking a 5.5% improvement over existing competitive baselines (below 37.6%), with navigation tasks reaching as high as 87.5%. These results validate the feasibility of general-purpose intelligence in underwater robotics, providing a foundation for scalable dataset synthesis and aquatic embodied agents.

## 核心内容
Underwater environments pose unique challenges for robotic navigation and manipulation. While existing research has primarily focused on task-specific methods, studies on general-purpose intelligence for multi-task execution remain scarce. To address this gap, we propose a unified framework for general-purpose underwater robots that integrates perception and action driven by language instructions. First, we develop a data synthesis pipeline to construct USIM, a simulation-based dataset which comprises over 905K frames from 2275 trajectories, totaling approximately 25 hours of BlueROV2 interactions. Furthermore, we propose U0, a vision-language-action (VLA) model capable of executing various tasks from obstacle-avoidance navigation to three-dimensional mobile manipulation. The model features a convolution-attention-based perception (CAP) module, which incorporates target pose estimation as an auxiliary task to explicitly bolster the model's spatial awareness. For evaluation, we establish a systematic assessment framework and an automated pipeline encompassing both offline metrics and online task execution. Experimental results demonstrate that the USIM dataset significantly empowers existing VLA models to adapt to underwater scenarios. Notably, our U0 model achieves state-of-the-art performance: it reduces the offline mean action prediction error to 0.0359 and achieves an overall online success rate of 43.1%, marking a 5.5% improvement over existing competitive baselines (below 37.6%), with navigation tasks reaching as high as 87.5%. These results validate the feasibility of general-purpose intelligence in underwater robotics, providing a foundation for scalable dataset synthesis and aquatic embodied agents.

## 参考
- http://arxiv.org/abs/2510.07869v4

