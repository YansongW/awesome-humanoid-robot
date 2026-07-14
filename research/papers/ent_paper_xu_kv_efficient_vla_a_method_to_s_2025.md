---
$id: ent_paper_xu_kv_efficient_vla_a_method_to_s_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache'
  zh: KV-Efficient VLA
  ko: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache'
summary:
  en: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (KV-Efficient VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by University of Toronto, Tsinghua University.'
  zh: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (KV-Efficient VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by University of Toronto, Tsinghua University.'
  ko: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (KV-Efficient VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by University of Toronto, Tsinghua University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- kv_efficient_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21354v2.
sources:
- id: src_001
  type: paper
  title: 'KV-Efficient VLA: A Method to Speed up Vision Language Models with RNN-Gated Chunked KV Cache (arXiv)'
  url: https://arxiv.org/abs/2509.21354
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models offer a unified framework for robotic perception and control, but their ability to scale to real-world, long-horizon tasks is limited by the high computational cost of attention and the large memory required for storing key-value (KV) pairs during inference, particularly when retaining historical image tokens as context. Recent methods have focused on scaling backbone architectures to improve generalization, with less emphasis on addressing inference inefficiencies essential for real-time use. In this work, we present KV-Efficient VLA, a model-agnostic memory compression approach designed to address these limitations by introducing a lightweight mechanism to selectively retain high-utility context. Our method partitions the KV cache into fixed-size chunks and employs a recurrent gating module to summarize and filter the historical context according to learned utility scores. This design aims to preserve recent fine-grained detail while aggressively pruning stale, low-relevance memory. Based on experiments, our approach can yield an average of 24.6% FLOPs savings, 1.34x inference speedup, and 1.87x reduction in KV memory. Our method integrates seamlessly into recent VLA stacks, enabling scalable inference without modifying downstream control logic.

## 核心内容
Vision-Language-Action (VLA) models offer a unified framework for robotic perception and control, but their ability to scale to real-world, long-horizon tasks is limited by the high computational cost of attention and the large memory required for storing key-value (KV) pairs during inference, particularly when retaining historical image tokens as context. Recent methods have focused on scaling backbone architectures to improve generalization, with less emphasis on addressing inference inefficiencies essential for real-time use. In this work, we present KV-Efficient VLA, a model-agnostic memory compression approach designed to address these limitations by introducing a lightweight mechanism to selectively retain high-utility context. Our method partitions the KV cache into fixed-size chunks and employs a recurrent gating module to summarize and filter the historical context according to learned utility scores. This design aims to preserve recent fine-grained detail while aggressively pruning stale, low-relevance memory. Based on experiments, our approach can yield an average of 24.6% FLOPs savings, 1.34x inference speedup, and 1.87x reduction in KV memory. Our method integrates seamlessly into recent VLA stacks, enabling scalable inference without modifying downstream control logic.

## 参考
- http://arxiv.org/abs/2509.21354v2

