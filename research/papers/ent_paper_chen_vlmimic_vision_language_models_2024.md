---
$id: ent_paper_chen_vlmimic_vision_language_models_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions'
  zh: VLMimic
  ko: 'VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions'
summary:
  en: 'VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions (VLMimic), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Beijing Institute of Technology, The University of Hong Kong, Peking University,
    and published at NIPS24.'
  zh: 'VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions (VLMimic), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Beijing Institute of Technology, The University of Hong Kong, Peking University,
    and published at NIPS24.'
  ko: 'VLMimic: Vision Language Models are Visual Imitation Learner for Fine-grained Actions (VLMimic), is a 2024 large vision-language-action
    model for robotic manipulation, introduced by Beijing Institute of Technology, The University of Hong Kong, Peking University,
    and published at NIPS24.'
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
- vlmimic
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.20927v3.
sources:
- id: src_001
  type: website
  title: VLMimic source
  url: http://papers.nips.cc/paper_files/paper/2024/hash/8e6f3d53b2bef98fce17e699557f5f11-Abstract-Conference.html
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
Visual imitation learning (VIL) provides an efficient and intuitive strategy for robotic systems to acquire novel skills. Recent advancements in Vision Language Models (VLMs) have demonstrated remarkable performance in vision and language reasoning capabilities for VIL tasks. Despite the progress, current VIL methods naively employ VLMs to learn high-level plans from human videos, relying on pre-defined motion primitives for executing physical interactions, which remains a major bottleneck. In this work, we present VLMimic, a novel paradigm that harnesses VLMs to directly learn even fine-grained action levels, only given a limited number of human videos. Specifically, VLMimic first grounds object-centric movements from human videos, and learns skills using hierarchical constraint representations, facilitating the derivation of skills with fine-grained action levels from limited human videos. These skills are refined and updated through an iterative comparison strategy, enabling efficient adaptation to unseen environments. Our extensive experiments exhibit that our VLMimic, using only 5 human videos, yields significant improvements of over 27% and 21% in RLBench and real-world manipulation tasks, and surpasses baselines by over 37% in long-horizon tasks.

## 核心内容
Visual imitation learning (VIL) provides an efficient and intuitive strategy for robotic systems to acquire novel skills. Recent advancements in Vision Language Models (VLMs) have demonstrated remarkable performance in vision and language reasoning capabilities for VIL tasks. Despite the progress, current VIL methods naively employ VLMs to learn high-level plans from human videos, relying on pre-defined motion primitives for executing physical interactions, which remains a major bottleneck. In this work, we present VLMimic, a novel paradigm that harnesses VLMs to directly learn even fine-grained action levels, only given a limited number of human videos. Specifically, VLMimic first grounds object-centric movements from human videos, and learns skills using hierarchical constraint representations, facilitating the derivation of skills with fine-grained action levels from limited human videos. These skills are refined and updated through an iterative comparison strategy, enabling efficient adaptation to unseen environments. Our extensive experiments exhibit that our VLMimic, using only 5 human videos, yields significant improvements of over 27% and 21% in RLBench and real-world manipulation tasks, and surpasses baselines by over 37% in long-horizon tasks.

## 参考
- http://arxiv.org/abs/2410.20927v3

