---
$id: ent_paper_cen_rynnvla_002_a_unified_vision_l_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RynnVLA-002: A Unified Vision-Language-Action and World Model'
  zh: RynnVLA-002
  ko: 'RynnVLA-002: A Unified Vision-Language-Action and World Model'
summary:
  en: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (RynnVLA-002), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by DAMO Academy, Hupan Lab, Zhejiang University.'
  zh: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (RynnVLA-002), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by DAMO Academy, Hupan Lab, Zhejiang University.'
  ko: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (RynnVLA-002), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by DAMO Academy, Hupan Lab, Zhejiang University.'
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
- rynnvla_002
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.17502v3.
sources:
- id: src_001
  type: paper
  title: 'RynnVLA-002: A Unified Vision-Language-Action and World Model (arXiv)'
  url: https://arxiv.org/abs/2511.17502
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RynnVLA-002 source
  url: https://doi.org/10.48550/arXiv.2511.17502
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce RynnVLA-002, a unified Vision-Language-Action (VLA) and world model. The world model leverages action and visual inputs to predict future image states, learning the underlying physics of the environment to refine action generation. Conversely, the VLA model produces subsequent actions from image observations, enhancing visual understanding and supporting the world model's image generation. The unified framework of RynnVLA-002 enables joint learning of environmental dynamics and action planning. Our experiments show that RynnVLA-002 surpasses individual VLA and world models, demonstrating their mutual enhancement. We evaluate RynnVLA-002 in both simulation and real-world robot tasks. RynnVLA-002 achieves 97.4% success rate on the LIBERO simulation benchmark without pretraining, while in real-world LeRobot experiments, its integrated world model boosts the overall success rate by 50%.

## 核心内容
We introduce RynnVLA-002, a unified Vision-Language-Action (VLA) and world model. The world model leverages action and visual inputs to predict future image states, learning the underlying physics of the environment to refine action generation. Conversely, the VLA model produces subsequent actions from image observations, enhancing visual understanding and supporting the world model's image generation. The unified framework of RynnVLA-002 enables joint learning of environmental dynamics and action planning. Our experiments show that RynnVLA-002 surpasses individual VLA and world models, demonstrating their mutual enhancement. We evaluate RynnVLA-002 in both simulation and real-world robot tasks. RynnVLA-002 achieves 97.4% success rate on the LIBERO simulation benchmark without pretraining, while in real-world LeRobot experiments, its integrated world model boosts the overall success rate by 50%.

## 参考
- http://arxiv.org/abs/2511.17502v3

