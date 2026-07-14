---
$id: ent_paper_dai_actionflow_a_pipelined_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge'
  zh: ActionFlow
  ko: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge'
summary:
  en: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge (ActionFlow), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science and Technology, University of Science and Technology
    of China, Suzhou Institute for Advanced Research, University of Science and Technology of China, IEIT SYSTEMS Co., Ltd..'
  zh: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge (ActionFlow), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science and Technology, University of Science and Technology
    of China, Suzhou Institute for Advanced Research, University of Science and Technology of China, IEIT SYSTEMS Co., Ltd..'
  ko: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge (ActionFlow), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Computer Science and Technology, University of Science and Technology
    of China, Suzhou Institute for Advanced Research, University of Science and Technology of China, IEIT SYSTEMS Co., Ltd..'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- actionflow
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20276v1.
sources:
- id: src_001
  type: paper
  title: 'ActionFlow: A Pipelined Action Acceleration for Vision Language Models on Edge (arXiv)'
  url: https://arxiv.org/abs/2512.20276
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ActionFlow source
  url: https://doi.org/10.48550/arXiv.2512.20276
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hin dered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typi cally operate at only 3-5 Hz on edge devices due to the memory bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge plat forms. At the core of ActionFlow is a Cross-Request Pipelin ing strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dy namic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

## 核心内容
Vision-Language-Action (VLA) models have emerged as a unified paradigm for robotic perception and control, enabling emergent generalization and long-horizon task execution. However, their deployment in dynamic, real-world environments is severely hin dered by high inference latency. While smooth robotic interaction requires control frequencies of 20 to 30 Hz, current VLA models typi cally operate at only 3-5 Hz on edge devices due to the memory bound nature of autoregressive decoding. Existing optimizations often require extensive retraining or compromise model accuracy. To bridge this gap, we introduce ActionFlow, a system-level inference framework tailored for resource-constrained edge plat forms. At the core of ActionFlow is a Cross-Request Pipelin ing strategy, a novel scheduler that redefines VLA inference as a macro-pipeline of micro-requests. The strategy intelligently batches memory-bound Decode phases with compute-bound Prefill phases across continuous time steps to maximize hardware utilization. Furthermore, to support this scheduling, we propose a Cross Request State Packed Forward operator and a Unified KV Ring Buffer, which fuse fragmented memory operations into efficient dense computations. Experimental results demonstrate that ActionFlow achieves a 2.55x improvement in FPS on the OpenVLA-7B model without retraining, enabling real-time dy namic manipulation on edge hardware. Our work is available at https://anonymous.4open.science/r/ActionFlow-1D47.

## 参考
- http://arxiv.org/abs/2512.20276v1

