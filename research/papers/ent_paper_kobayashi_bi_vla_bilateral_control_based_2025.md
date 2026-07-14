---
$id: ent_paper_kobayashi_bi_vla_bilateral_control_based_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation'
  zh: Bi-VLA 2025
  ko: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation'
summary:
  en: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA 2025),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Osaka, Kobe University.'
  zh: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA 2025),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Osaka, Kobe University.'
  ko: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA 2025),
    is a 2025 large vision-language-action model for robotic manipulation, introduced by The University of Osaka, Kobe University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- bi_vla_2025
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.18865v1.
sources:
- id: src_001
  type: paper
  title: 'Bi-VLA: Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (arXiv)'
  url: https://arxiv.org/abs/2509.18865
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Bi-VLA 2025 source
  url: https://doi.org/10.48550/arXiv.2509.18865
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We propose Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA), a novel framework that extends bilateral control-based imitation learning to handle more than one task within a single model. Conventional bilateral control methods exploit joint angle, velocity, torque, and vision for precise manipulation but require task-specific models, limiting their generality. Bi-VLA overcomes this limitation by utilizing robot joint angle, velocity, and torque data from leader-follower bilateral control with visual features and natural language instructions through SigLIP and FiLM-based fusion. We validated Bi-VLA on two task types: one requiring supplementary language cues and another distinguishable solely by vision. Real-robot experiments showed that Bi-VLA successfully interprets vision-language combinations and improves task success rates compared to conventional bilateral control-based imitation learning. Our Bi-VLA addresses the single-task limitation of prior bilateral approaches and provides empirical evidence that combining vision and language significantly enhances versatility. Experimental results validate the effectiveness of Bi-VLA in real-world tasks. For additional material, please visit the website: https://mertcookimg.github.io/bi-vla/

## 核心内容
We propose Bilateral Control-Based Imitation Learning via Vision-Language Fusion for Action Generation (Bi-VLA), a novel framework that extends bilateral control-based imitation learning to handle more than one task within a single model. Conventional bilateral control methods exploit joint angle, velocity, torque, and vision for precise manipulation but require task-specific models, limiting their generality. Bi-VLA overcomes this limitation by utilizing robot joint angle, velocity, and torque data from leader-follower bilateral control with visual features and natural language instructions through SigLIP and FiLM-based fusion. We validated Bi-VLA on two task types: one requiring supplementary language cues and another distinguishable solely by vision. Real-robot experiments showed that Bi-VLA successfully interprets vision-language combinations and improves task success rates compared to conventional bilateral control-based imitation learning. Our Bi-VLA addresses the single-task limitation of prior bilateral approaches and provides empirical evidence that combining vision and language significantly enhances versatility. Experimental results validate the effectiveness of Bi-VLA in real-world tasks. For additional material, please visit the website: https://mertcookimg.github.io/bi-vla/

## 参考
- http://arxiv.org/abs/2509.18865v1

