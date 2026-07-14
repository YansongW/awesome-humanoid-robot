---
$id: ent_paper_wei_cyclemanip_enabling_cyclic_tas_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CycleManip: Enabling Cyclic Task Manipulation via Effective Historical Perception and Understanding'
  zh: CycleManip
  ko: 'CycleManip: Enabling Cyclic Task Manipulation via Effective Historical Perception and Understanding'
summary:
  en: 'CycleManip: Enabling Cyclic Task Manipulation via Effective Historical Perception and Understanding (CycleManip), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, The Chinese
    University of Hong Kong, Shenzhen.'
  zh: 'CycleManip: Enabling Cyclic Task Manipulation via Effective Historical Perception and Understanding (CycleManip), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, The Chinese
    University of Hong Kong, Shenzhen.'
  ko: 'CycleManip: Enabling Cyclic Task Manipulation via Effective Historical Perception and Understanding (CycleManip), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, The Chinese
    University of Hong Kong, Shenzhen.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cyclemanip
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.01022v2.
sources:
- id: src_001
  type: paper
  title: 'CycleManip: Enabling Cyclic Task Manipulation via Effective Historical Perception and Understanding (arXiv)'
  url: https://arxiv.org/abs/2512.01022
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CycleManip source
  url: https://doi.org/10.48550/arXiv.2512.01022
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In this paper, we explore an important yet underexplored task in robot manipulation: cycle-based manipulation, where robots need to perform cyclic or repetitive actions with an expected terminal time. These tasks are crucial in daily life, such as shaking a bottle or knocking a nail. However, few prior works have explored this task, leading to two main challenges: 1) the imitation methods often fail to complete these tasks within the expected terminal time due to the ineffective utilization of history; 2) the absence of a benchmark with sufficient data and automatic evaluation tools hinders development of effective solutions in this area. To address these challenges, we first propose the CycleManip framework to achieve cycle-based task manipulation in an end-to-end imitation manner without requiring any extra models, hierarchical structure or significant computational overhead. The core insight is to enhance effective history perception by a cost-aware sampling strategy and to improve historical understanding by multi-task learning. Second, we introduce a cycle-based task manipulation benchmark, which provides diverse cycle-based tasks, and an automatic evaluation method. Extensive experiments conducted in both simulation and real-world settings demonstrate that our method achieves high success rates in cycle-based task manipulation. The results further show strong adaptability performance in general manipulation, and the plug-and-play ability on imitation policies such as Vision-Language-Action (VLA) models. Moreover, the results show that our approach can be applied across diverse robotic platforms, including bi-arm grippers, dexterous hands, and humanoid robots.

## 核心内容
In this paper, we explore an important yet underexplored task in robot manipulation: cycle-based manipulation, where robots need to perform cyclic or repetitive actions with an expected terminal time. These tasks are crucial in daily life, such as shaking a bottle or knocking a nail. However, few prior works have explored this task, leading to two main challenges: 1) the imitation methods often fail to complete these tasks within the expected terminal time due to the ineffective utilization of history; 2) the absence of a benchmark with sufficient data and automatic evaluation tools hinders development of effective solutions in this area. To address these challenges, we first propose the CycleManip framework to achieve cycle-based task manipulation in an end-to-end imitation manner without requiring any extra models, hierarchical structure or significant computational overhead. The core insight is to enhance effective history perception by a cost-aware sampling strategy and to improve historical understanding by multi-task learning. Second, we introduce a cycle-based task manipulation benchmark, which provides diverse cycle-based tasks, and an automatic evaluation method. Extensive experiments conducted in both simulation and real-world settings demonstrate that our method achieves high success rates in cycle-based task manipulation. The results further show strong adaptability performance in general manipulation, and the plug-and-play ability on imitation policies such as Vision-Language-Action (VLA) models. Moreover, the results show that our approach can be applied across diverse robotic platforms, including bi-arm grippers, dexterous hands, and humanoid robots.

## 参考
- http://arxiv.org/abs/2512.01022v2

