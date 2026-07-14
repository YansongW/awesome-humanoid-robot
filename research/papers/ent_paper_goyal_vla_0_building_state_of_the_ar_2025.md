---
$id: ent_paper_goyal_vla_0_building_state_of_the_ar_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification'
  zh: VLA-0
  ko: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification'
summary:
  en: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (VLA-0), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Nvidia.'
  zh: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (VLA-0), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Nvidia.'
  ko: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (VLA-0), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Nvidia.'
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
- vision_language_action
- vla
- vla_0
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.13054v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-0: Building State-of-the-Art VLAs with Zero Modification (arXiv)'
  url: https://arxiv.org/abs/2510.13054
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-0 source
  url: https://doi.org/10.48550/arXiv.2510.13054
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action models (VLAs) hold immense promise for enabling generalist robot manipulation. However, the best way to build them remains an open question. Current approaches often add complexity, such as modifying the existing vocabulary of a Vision-Language Model (VLM) with action tokens or introducing special action heads. Curiously, the simplest strategy of representing actions directly as text has remained largely unexplored. This work introduces VLA-0 to investigate this idea. We find that VLA-0 is not only effective; it is surprisingly powerful. With the right design, VLA-0 outperforms more involved models. On LIBERO, a popular benchmark for evaluating VLAs, VLA-0 outperforms all existing methods trained on the same robotic data, including $π_0.5$-KI, OpenVLA-OFT and SmolVLA. Furthermore, without large-scale robotics-specific training, it outperforms methods trained on large-scale robotic data, like $π_0.5$-KI, $π_0$, GR00T-N1 and MolmoAct. These findings also translate to the real world, where VLA-0 outperforms SmolVLA, a VLA model pre-trained on large-scale real data. This paper summarizes our unexpected findings and spells out the specific techniques required to unlock the high performance of this simple yet potent VLA design. Visual results, code, and trained models are provided here: https://vla0.github.io/.

## 核心内容
Vision-Language-Action models (VLAs) hold immense promise for enabling generalist robot manipulation. However, the best way to build them remains an open question. Current approaches often add complexity, such as modifying the existing vocabulary of a Vision-Language Model (VLM) with action tokens or introducing special action heads. Curiously, the simplest strategy of representing actions directly as text has remained largely unexplored. This work introduces VLA-0 to investigate this idea. We find that VLA-0 is not only effective; it is surprisingly powerful. With the right design, VLA-0 outperforms more involved models. On LIBERO, a popular benchmark for evaluating VLAs, VLA-0 outperforms all existing methods trained on the same robotic data, including $π_0.5$-KI, OpenVLA-OFT and SmolVLA. Furthermore, without large-scale robotics-specific training, it outperforms methods trained on large-scale robotic data, like $π_0.5$-KI, $π_0$, GR00T-N1 and MolmoAct. These findings also translate to the real world, where VLA-0 outperforms SmolVLA, a VLA model pre-trained on large-scale real data. This paper summarizes our unexpected findings and spells out the specific techniques required to unlock the high performance of this simple yet potent VLA design. Visual results, code, and trained models are provided here: https://vla0.github.io/.

## 参考
- http://arxiv.org/abs/2510.13054v1

