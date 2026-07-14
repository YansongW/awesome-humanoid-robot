---
$id: ent_paper_li_towards_generalist_robot_polic_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models'
  zh: RoboVLMs
  ko: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models'
summary:
  en: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (RoboVLMs), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua University, ByteDance Research, CASIA MAIS-NLPR,
    Shanghai Jiao Tong University, National University of Singapore.'
  zh: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (RoboVLMs), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua University, ByteDance Research, CASIA MAIS-NLPR,
    Shanghai Jiao Tong University, National University of Singapore.'
  ko: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (RoboVLMs), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Tsinghua University, ByteDance Research, CASIA MAIS-NLPR,
    Shanghai Jiao Tong University, National University of Singapore.'
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
- robovlms
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.14058v4.
sources:
- id: src_001
  type: paper
  title: 'Towards Generalist Robot Policies: What Matters in Building Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2412.14058
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RoboVLMs source
  url: https://doi.org/10.48550/arXiv.2412.14058
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
To utilize Foundation Vision Language Models (VLMs) for robotic tasks and motion planning, the community has proposed different methods for injecting action components into VLMs and building the Vision-Language-Action models (VLAs). In this work, we disclose the key factors that significantly influence the performance of VLA on robot manipulation problems and focus on answering three essential design choices: which backbone to select, how to formulate the VLA architectures, and when to add cross-embodiment data. The obtained results convince us firmly to explain why we prefer VLA and develop a new family of VLAs, RoboVLMs, which require very few manual designs and achieve a new state-of-the-art performance in three simulation tasks and real-world experiments. Through our extensive experiments, which include over 8 VLM backbones, 4 policy architectures, and over 600 distinct designed experiments, we provide a detailed guidebook for the future design of VLAs. In addition to the study, the highly flexible RoboVLMs framework, which supports easy integrations of new VLMs and free combinations of various design choices, is made public to facilitate future research. We open-source all details, including codes, models, datasets, and toolkits, along with detailed training and evaluation recipes at: robovlms.github.io.

## 核心内容
To utilize Foundation Vision Language Models (VLMs) for robotic tasks and motion planning, the community has proposed different methods for injecting action components into VLMs and building the Vision-Language-Action models (VLAs). In this work, we disclose the key factors that significantly influence the performance of VLA on robot manipulation problems and focus on answering three essential design choices: which backbone to select, how to formulate the VLA architectures, and when to add cross-embodiment data. The obtained results convince us firmly to explain why we prefer VLA and develop a new family of VLAs, RoboVLMs, which require very few manual designs and achieve a new state-of-the-art performance in three simulation tasks and real-world experiments. Through our extensive experiments, which include over 8 VLM backbones, 4 policy architectures, and over 600 distinct designed experiments, we provide a detailed guidebook for the future design of VLAs. In addition to the study, the highly flexible RoboVLMs framework, which supports easy integrations of new VLMs and free combinations of various design choices, is made public to facilitate future research. We open-source all details, including codes, models, datasets, and toolkits, along with detailed training and evaluation recipes at: robovlms.github.io.

## 参考
- http://arxiv.org/abs/2412.14058v4

