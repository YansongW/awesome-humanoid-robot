---
$id: ent_paper_kang_clip_rt_learning_language_cond_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision'
  zh: CLIP-RT
  ko: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision'
summary:
  en: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (CLIP-RT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Seoul National University, and published at RSS25.'
  zh: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (CLIP-RT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Seoul National University, and published at RSS25.'
  ko: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (CLIP-RT), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Seoul National University, and published at RSS25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- clip_rt
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.00508v4.
sources:
- id: src_001
  type: paper
  title: 'CLIP-RT: Learning Language-Conditioned Robotic Policies from Natural Language Supervision (arXiv)'
  url: https://arxiv.org/abs/2411.00508
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CLIP-RT source
  url: https://doi.org/10.48550/arXiv.2411.00508
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Teaching robots desired skills in real-world environments remains challenging, especially for non-experts. A key bottleneck is that collecting robotic data often requires expertise or specialized hardware, limiting accessibility and scalability. We posit that natural language offers an intuitive and accessible interface for robot learning. To this end, we study two aspects: (1) enabling non-experts to collect robotic data through natural language supervision (e.g., "move the arm to the right") and (2) training robot policies directly from this supervision. Specifically, we introduce a data collection framework that collects robot demonstrations based on natural language supervision and further augments these demonstrations. We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor policies from this supervision. CLIP-RT adapts the pretrained CLIP model and learns to predict language-based motion primitives via contrastive imitation learning. We train CLIP-RT on the Open X-Embodiment dataset and finetune it on in-domain data collected by our framework. In real-world evaluations, CLIP-RT demonstrates strong capabilities in learning novel manipulation skills, outperforming OpenVLA (7B parameters) by 24% in average success rates, while using 7x fewer parameters (1B). We further assess CLIP-RT's capabilities in few-shot generalization and collaborative scenarios involving large pretrained models or humans. In simulated environments, CLIP-RT also yields strong performance, achieving a 93.1% average success rate on the LIBERO benchmark with an inference throughput of 163 Hz.

## 核心内容
Teaching robots desired skills in real-world environments remains challenging, especially for non-experts. A key bottleneck is that collecting robotic data often requires expertise or specialized hardware, limiting accessibility and scalability. We posit that natural language offers an intuitive and accessible interface for robot learning. To this end, we study two aspects: (1) enabling non-experts to collect robotic data through natural language supervision (e.g., "move the arm to the right") and (2) training robot policies directly from this supervision. Specifically, we introduce a data collection framework that collects robot demonstrations based on natural language supervision and further augments these demonstrations. We then present CLIP-RT, a new vision-language-action (VLA) model that learns language-conditioned visuomotor policies from this supervision. CLIP-RT adapts the pretrained CLIP model and learns to predict language-based motion primitives via contrastive imitation learning. We train CLIP-RT on the Open X-Embodiment dataset and finetune it on in-domain data collected by our framework. In real-world evaluations, CLIP-RT demonstrates strong capabilities in learning novel manipulation skills, outperforming OpenVLA (7B parameters) by 24% in average success rates, while using 7x fewer parameters (1B). We further assess CLIP-RT's capabilities in few-shot generalization and collaborative scenarios involving large pretrained models or humans. In simulated environments, CLIP-RT also yields strong performance, achieving a 93.1% average success rate on the LIBERO benchmark with an inference throughput of 163 Hz.

## 参考
- http://arxiv.org/abs/2411.00508v4

