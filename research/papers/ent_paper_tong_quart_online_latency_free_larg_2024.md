---
$id: ent_paper_tong_quart_online_latency_free_larg_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning'
  zh: QUART-Online
  ko: 'QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning'
summary:
  en: 'QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning (QUART-Online), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at ICRA25.'
  zh: 'QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning (QUART-Online), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at ICRA25.'
  ko: 'QUART-Online: Latency-Free Large Multimodal Language Model for Quadruped Robot Learning (QUART-Online), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at ICRA25.'
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
- quart_online
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2412.15576v5.
sources:
- id: src_001
  type: website
  title: QUART-Online source
  url: https://doi.org/10.1109/ICRA55743.2025.11127693
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
This paper addresses the inherent inference latency challenges associated with deploying multimodal large language models (MLLM) in quadruped vision-language-action (QUAR-VLA) tasks. Our investigation reveals that conventional parameter reduction techniques ultimately impair the performance of the language foundation model during the action instruction tuning phase, making them unsuitable for this purpose. We introduce a novel latency-free quadruped MLLM model, dubbed QUART-Online, designed to enhance inference efficiency without degrading the performance of the language foundation model. By incorporating Action Chunk Discretization (ACD), we compress the original action representation space, mapping continuous action values onto a smaller set of discrete representative vectors while preserving critical information. Subsequently, we fine-tune the MLLM to integrate vision, language, and compressed actions into a unified semantic space. Experimental results demonstrate that QUART-Online operates in tandem with the existing MLLM system, achieving real-time inference in sync with the underlying controller frequency, significantly boosting the success rate across various tasks by 65%. Our project page is https://quart-online.github.io.

## 核心内容
This paper addresses the inherent inference latency challenges associated with deploying multimodal large language models (MLLM) in quadruped vision-language-action (QUAR-VLA) tasks. Our investigation reveals that conventional parameter reduction techniques ultimately impair the performance of the language foundation model during the action instruction tuning phase, making them unsuitable for this purpose. We introduce a novel latency-free quadruped MLLM model, dubbed QUART-Online, designed to enhance inference efficiency without degrading the performance of the language foundation model. By incorporating Action Chunk Discretization (ACD), we compress the original action representation space, mapping continuous action values onto a smaller set of discrete representative vectors while preserving critical information. Subsequently, we fine-tune the MLLM to integrate vision, language, and compressed actions into a unified semantic space. Experimental results demonstrate that QUART-Online operates in tandem with the existing MLLM system, achieving real-time inference in sync with the underlying controller frequency, significantly boosting the success rate across various tasks by 65%. Our project page is https://quart-online.github.io.

## 参考
- http://arxiv.org/abs/2412.15576v5

