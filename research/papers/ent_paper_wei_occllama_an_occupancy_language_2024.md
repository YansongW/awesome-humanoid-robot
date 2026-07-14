---
$id: ent_paper_wei_occllama_an_occupancy_language_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving'
  zh: OccLLaMA
  ko: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving'
summary:
  en: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (OccLLaMA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Academy for Engineering & Technology, Fudan University, Institute for AI
    Industry Research, Tsinghua University.'
  zh: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (OccLLaMA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Academy for Engineering & Technology, Fudan University, Institute for AI
    Industry Research, Tsinghua University.'
  ko: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (OccLLaMA), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Academy for Engineering & Technology, Fudan University, Institute for AI
    Industry Research, Tsinghua University.'
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
- occllama
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2409.03272v1.
sources:
- id: src_001
  type: paper
  title: 'OccLLaMA: An Occupancy-Language-Action Generative World Model for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2409.03272
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OccLLaMA source
  url: https://doi.org/10.48550/arXiv.2409.03272
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The rise of multi-modal large language models(MLLMs) has spurred their applications in autonomous driving. Recent MLLM-based methods perform action by learning a direct mapping from perception to action, neglecting the dynamics of the world and the relations between action and world dynamics. In contrast, human beings possess world model that enables them to simulate the future states based on 3D internal visual representation and plan actions accordingly. To this end, we propose OccLLaMA, an occupancy-language-action generative world model, which uses semantic occupancy as a general visual representation and unifies vision-language-action(VLA) modalities through an autoregressive model. Specifically, we introduce a novel VQVAE-like scene tokenizer to efficiently discretize and reconstruct semantic occupancy scenes, considering its sparsity and classes imbalance. Then, we build a unified multi-modal vocabulary for vision, language and action. Furthermore, we enhance LLM, specifically LLaMA, to perform the next token/scene prediction on the unified vocabulary to complete multiple tasks in autonomous driving. Extensive experiments demonstrate that OccLLaMA achieves competitive performance across multiple tasks, including 4D occupancy forecasting, motion planning, and visual question answering, showcasing its potential as a foundation model in autonomous driving.

## 核心内容
The rise of multi-modal large language models(MLLMs) has spurred their applications in autonomous driving. Recent MLLM-based methods perform action by learning a direct mapping from perception to action, neglecting the dynamics of the world and the relations between action and world dynamics. In contrast, human beings possess world model that enables them to simulate the future states based on 3D internal visual representation and plan actions accordingly. To this end, we propose OccLLaMA, an occupancy-language-action generative world model, which uses semantic occupancy as a general visual representation and unifies vision-language-action(VLA) modalities through an autoregressive model. Specifically, we introduce a novel VQVAE-like scene tokenizer to efficiently discretize and reconstruct semantic occupancy scenes, considering its sparsity and classes imbalance. Then, we build a unified multi-modal vocabulary for vision, language and action. Furthermore, we enhance LLM, specifically LLaMA, to perform the next token/scene prediction on the unified vocabulary to complete multiple tasks in autonomous driving. Extensive experiments demonstrate that OccLLaMA achieves competitive performance across multiple tasks, including 4D occupancy forecasting, motion planning, and visual question answering, showcasing its potential as a foundation model in autonomous driving.

## 参考
- http://arxiv.org/abs/2409.03272v1

