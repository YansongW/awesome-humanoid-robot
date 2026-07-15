---
$id: ent_paper_zhang_up_vla_a_unified_understanding_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent'
  zh: UP-VLA
  ko: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent'
summary:
  en: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent (UP-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, and published at ICML 2025.'
  zh: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent (UP-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, and published at ICML 2025.'
  ko: 'UP-VLA: A Unified Understanding and Prediction Model for Embodied Agent (UP-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, and published at ICML 2025.'
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
- up_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2501.18867v3.
sources:
- id: src_001
  type: paper
  title: UP-VLA source
  url: https://openreview.net/forum?id=V7JPraxi5j
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities. However, prior research has shown that VLMs often focus on high-level semantic content and neglect low-level features, limiting their ability to capture detailed spatial information and understand physical dynamics. These aspects, which are crucial for embodied control tasks, remain underexplored in existing pre-training paradigms. In this paper, we investigate the training paradigm for VLAs, and introduce \textbf{UP-VLA}, a \textbf{U}nified VLA model training with both multi-modal \textbf{U}nderstanding and future \textbf{P}rediction objectives, enhancing both high-level semantic comprehension and low-level spatial understanding. Experimental results show that UP-VLA achieves a 33% improvement on the Calvin ABC-D benchmark compared to the previous state-of-the-art method. Additionally, UP-VLA demonstrates improved success rates in real-world manipulation tasks, particularly those requiring precise spatial information.

## 核心内容
Recent advancements in Vision-Language-Action (VLA) models have leveraged pre-trained Vision-Language Models (VLMs) to improve the generalization capabilities. VLMs, typically pre-trained on vision-language understanding tasks, provide rich semantic knowledge and reasoning abilities. However, prior research has shown that VLMs often focus on high-level semantic content and neglect low-level features, limiting their ability to capture detailed spatial information and understand physical dynamics. These aspects, which are crucial for embodied control tasks, remain underexplored in existing pre-training paradigms. In this paper, we investigate the training paradigm for VLAs, and introduce \textbf{UP-VLA}, a \textbf{U}nified VLA model training with both multi-modal \textbf{U}nderstanding and future \textbf{P}rediction objectives, enhancing both high-level semantic comprehension and low-level spatial understanding. Experimental results show that UP-VLA achieves a 33% improvement on the Calvin ABC-D benchmark compared to the previous state-of-the-art method. Additionally, UP-VLA demonstrates improved success rates in real-world manipulation tasks, particularly those requiring precise spatial information.

## 参考
- http://arxiv.org/abs/2501.18867v3

