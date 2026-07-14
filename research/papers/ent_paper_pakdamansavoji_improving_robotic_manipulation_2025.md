---
$id: ent_paper_pakdamansavoji_improving_robotic_manipulation_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Improving Robotic Manipulation Robustness via NICE Scene Surgery
  zh: NICE
  ko: Improving Robotic Manipulation Robustness via NICE Scene Surgery
summary:
  en: Improving Robotic Manipulation Robustness via NICE Scene Surgery (NICE), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Huawei Canada.
  zh: Improving Robotic Manipulation Robustness via NICE Scene Surgery (NICE), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Huawei Canada.
  ko: Improving Robotic Manipulation Robustness via NICE Scene Surgery (NICE), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Huawei Canada.
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
- nice
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22777v1.
sources:
- id: src_001
  type: paper
  title: Improving Robotic Manipulation Robustness via NICE Scene Surgery (arXiv)
  url: https://arxiv.org/abs/2511.22777
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: NICE source
  url: https://doi.org/10.48550/arXiv.2511.22777
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets.   Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

## 核心内容
Learning robust visuomotor policies for robotic manipulation remains a challenge in real-world settings, where visual distractors can significantly degrade performance and safety. In this work, we propose an effective and scalable framework, Naturalistic Inpainting for Context Enhancement (NICE). Our method minimizes out-of-distribution (OOD) gap in imitation learning by increasing visual diversity through construction of new experiences using existing demonstrations. By utilizing image generative frameworks and large language models, NICE performs three editing operations, object replacement, restyling, and removal of distracting (non-target) objects. These changes preserve spatial relationships without obstructing target objects and maintain action-label consistency. Unlike previous approaches, NICE requires no additional robot data collection, simulator access, or custom model training, making it readily applicable to existing robotic datasets.   Using real-world scenes, we showcase the capability of our framework in producing photo-realistic scene enhancement. For downstream tasks, we use NICE data to finetune a vision-language model (VLM) for spatial affordance prediction and a vision-language-action (VLA) policy for object manipulation. Our evaluations show that NICE successfully minimizes OOD gaps, resulting in over 20% improvement in accuracy for affordance prediction in highly cluttered scenes. For manipulation tasks, success rate increases on average by 11% when testing in environments populated with distractors in different quantities. Furthermore, we show that our method improves visual robustness, lowering target confusion by 6%, and enhances safety by reducing collision rate by 7%.

## 参考
- http://arxiv.org/abs/2511.22777v1

