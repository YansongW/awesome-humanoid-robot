---
$id: ent_paper_joglekar_towards_natural_language_drive_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Natural Language-Driven Assembly Using Foundation Models
  zh: Towards Natural Language-Driven Assembly Using Foundation Models
  ko: Towards Natural Language-Driven Assembly Using Foundation Models
summary:
  en: Towards Natural Language-Driven Assembly Using Foundation Models (Towards Natural Language-Driven Assembly Using Foundation
    Models), is a 2024 large vision-language-action model for robotic manipulation, introduced by Bosch Center for Artificial
    Intelligence, Tel Aviv University.
  zh: Towards Natural Language-Driven Assembly Using Foundation Models (Towards Natural Language-Driven Assembly Using Foundation
    Models), is a 2024 large vision-language-action model for robotic manipulation, introduced by Bosch Center for Artificial
    Intelligence, Tel Aviv University.
  ko: Towards Natural Language-Driven Assembly Using Foundation Models (Towards Natural Language-Driven Assembly Using Foundation
    Models), is a 2024 large vision-language-action model for robotic manipulation, introduced by Bosch Center for Artificial
    Intelligence, Tel Aviv University.
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
- towards_natural_language_drive
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.16093v1.
sources:
- id: src_001
  type: paper
  title: Towards Natural Language-Driven Assembly Using Foundation Models (arXiv)
  url: https://arxiv.org/abs/2406.16093
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Towards Natural Language-Driven Assembly Using Foundation Models source
  url: https://doi.org/10.48550/arXiv.2406.16093
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Large Language Models (LLMs) and strong vision models have enabled rapid research and development in the field of Vision-Language-Action models that enable robotic control. The main objective of these methods is to develop a generalist policy that can control robots with various embodiments. However, in industrial robotic applications such as automated assembly and disassembly, some tasks, such as insertion, demand greater accuracy and involve intricate factors like contact engagement, friction handling, and refined motor skills. Implementing these skills using a generalist policy is challenging because these policies might integrate further sensory data, including force or torque measurements, for enhanced precision. In our method, we present a global control policy based on LLMs that can transfer the control policy to a finite set of skills that are specifically trained to perform high-precision tasks through dynamic context switching. The integration of LLMs into this framework underscores their significance in not only interpreting and processing language inputs but also in enriching the control mechanisms for diverse and intricate robotic operations.

## 核心内容
Large Language Models (LLMs) and strong vision models have enabled rapid research and development in the field of Vision-Language-Action models that enable robotic control. The main objective of these methods is to develop a generalist policy that can control robots with various embodiments. However, in industrial robotic applications such as automated assembly and disassembly, some tasks, such as insertion, demand greater accuracy and involve intricate factors like contact engagement, friction handling, and refined motor skills. Implementing these skills using a generalist policy is challenging because these policies might integrate further sensory data, including force or torque measurements, for enhanced precision. In our method, we present a global control policy based on LLMs that can transfer the control policy to a finite set of skills that are specifically trained to perform high-precision tasks through dynamic context switching. The integration of LLMs into this framework underscores their significance in not only interpreting and processing language inputs but also in enriching the control mechanisms for diverse and intricate robotic operations.

## 参考
- http://arxiv.org/abs/2406.16093v1

