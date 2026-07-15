---
$id: ent_paper_huang_a3vlm_actionable_articulation_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'A3VLM: Actionable Articulation-Aware Vision Language Model'
  zh: A3VLM
  ko: 'A3VLM: Actionable Articulation-Aware Vision Language Model'
summary:
  en: 'A3VLM: Actionable Articulation-Aware Vision Language Model (A3VLM), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by SJTU, Shanghai AI Lab, Rutgers University, Yuandao AI, PKU, CUHK MMLab, and published
    at CoRL24.'
  zh: 'A3VLM: Actionable Articulation-Aware Vision Language Model (A3VLM), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by SJTU, Shanghai AI Lab, Rutgers University, Yuandao AI, PKU, CUHK MMLab, and published
    at CoRL24.'
  ko: 'A3VLM: Actionable Articulation-Aware Vision Language Model (A3VLM), is a 2024 large vision-language-action model for
    robotic manipulation, introduced by SJTU, Shanghai AI Lab, Rutgers University, Yuandao AI, PKU, CUHK MMLab, and published
    at CoRL24.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- a3vlm
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.07549v2.
sources:
- id: src_001
  type: paper
  title: A3VLM source
  url: https://proceedings.mlr.press/v270/huang25b.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Vision Language Models (VLMs) have received significant attention in recent years in the robotics community. VLMs are shown to be able to perform complex visual reasoning and scene understanding tasks, which makes them regarded as a potential universal solution for general robotics problems such as manipulation and navigation. However, previous VLMs for robotics such as RT-1, RT-2, and ManipLLM have focused on directly learning robot-centric actions. Such approaches require collecting a significant amount of robot interaction data, which is extremely costly in the real world. Thus, we propose A3VLM, an object-centric, actionable, articulation-aware vision language model. A3VLM focuses on the articulation structure and action affordances of objects. Its representation is robot-agnostic and can be translated into robot actions using simple action primitives. Extensive experiments in both simulation benchmarks and real-world settings demonstrate the effectiveness and stability of A3VLM. We release our code and other materials at https://github.com/changhaonan/A3VLM.

## 核心内容
Vision Language Models (VLMs) have received significant attention in recent years in the robotics community. VLMs are shown to be able to perform complex visual reasoning and scene understanding tasks, which makes them regarded as a potential universal solution for general robotics problems such as manipulation and navigation. However, previous VLMs for robotics such as RT-1, RT-2, and ManipLLM have focused on directly learning robot-centric actions. Such approaches require collecting a significant amount of robot interaction data, which is extremely costly in the real world. Thus, we propose A3VLM, an object-centric, actionable, articulation-aware vision language model. A3VLM focuses on the articulation structure and action affordances of objects. Its representation is robot-agnostic and can be translated into robot actions using simple action primitives. Extensive experiments in both simulation benchmarks and real-world settings demonstrate the effectiveness and stability of A3VLM. We release our code and other materials at https://github.com/changhaonan/A3VLM.

## 参考
- http://arxiv.org/abs/2406.07549v2

