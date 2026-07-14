---
$id: ent_paper_bu_towards_synergistic_generalize_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation
  zh: RoboDual
  ko: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation
summary:
  en: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation (RoboDual), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong Univeristy, The University of Hong Kong, AgiBot, Shanghai
    AI Lab.
  zh: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation (RoboDual), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong Univeristy, The University of Hong Kong, AgiBot, Shanghai
    AI Lab.
  ko: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation (RoboDual), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Shanghai Jiao Tong Univeristy, The University of Hong Kong, AgiBot, Shanghai
    AI Lab.
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
- robodual
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.08001v3.
sources:
- id: src_001
  type: paper
  title: Towards Synergistic, Generalized, and Efficient Dual-System for Robotic Manipulation (arXiv)
  url: https://arxiv.org/abs/2410.08001
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboDual source
  url: https://doi.org/10.48550/arXiv.2410.08001
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
The increasing demand for versatile robotic systems to operate in diverse and dynamic environments has emphasized the importance of a generalist policy, which leverages a large cross-embodiment data corpus to facilitate broad adaptability and high-level reasoning. However, the generalist would struggle with inefficient inference and cost-expensive training. The specialist policy, instead, is curated for specific domain data and excels at task-level precision with efficiency. Yet, it lacks the generalization capacity for a wide range of applications. Inspired by these observations, we introduce RoboDual, a synergistic dual-system that supplements the merits of both generalist and specialist policy. A diffusion transformer-based specialist is devised for multi-step action rollouts, exquisitely conditioned on the high-level task understanding and discretized action output of a vision-language-action (VLA) based generalist. Compared to OpenVLA, RoboDual achieves 26.7% improvement in real-world setting and 12% gain on CALVIN by introducing a specialist policy with merely 20M trainable parameters. It maintains strong performance with 5% of demonstration data only, and enables a 3.8 times higher control frequency in real-world deployment. Code would be made publicly available. Our project page is hosted at: https://opendrivelab.com/RoboDual/

## 核心内容
The increasing demand for versatile robotic systems to operate in diverse and dynamic environments has emphasized the importance of a generalist policy, which leverages a large cross-embodiment data corpus to facilitate broad adaptability and high-level reasoning. However, the generalist would struggle with inefficient inference and cost-expensive training. The specialist policy, instead, is curated for specific domain data and excels at task-level precision with efficiency. Yet, it lacks the generalization capacity for a wide range of applications. Inspired by these observations, we introduce RoboDual, a synergistic dual-system that supplements the merits of both generalist and specialist policy. A diffusion transformer-based specialist is devised for multi-step action rollouts, exquisitely conditioned on the high-level task understanding and discretized action output of a vision-language-action (VLA) based generalist. Compared to OpenVLA, RoboDual achieves 26.7% improvement in real-world setting and 12% gain on CALVIN by introducing a specialist policy with merely 20M trainable parameters. It maintains strong performance with 5% of demonstration data only, and enables a 3.8 times higher control frequency in real-world deployment. Code would be made publicly available. Our project page is hosted at: https://opendrivelab.com/RoboDual/

## 参考
- http://arxiv.org/abs/2410.08001v3

