---
$id: ent_paper_jiang_asyncvla_asynchronous_flow_mat_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models'
  zh: AsyncVLA
  ko: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models'
summary:
  en: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (AsyncVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Tsinghua University, Zhejiang University, Lumos
    Robotics.'
  zh: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (AsyncVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Tsinghua University, Zhejiang University, Lumos
    Robotics.'
  ko: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (AsyncVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Shanghai AI Laboratory, Tsinghua University, Zhejiang University, Lumos
    Robotics.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- asyncvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.14148v2.
sources:
- id: src_001
  type: paper
  title: 'AsyncVLA: Asynchronous Flow Matching for Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.14148
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AsyncVLA source
  url: https://doi.org/10.48550/arXiv.2511.14148
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have recently emerged as a powerful paradigm for building generalist robots. However, traditional VLA models that generate actions through flow matching (FM) typically rely on rigid and uniform time schedules, i.e., synchronous FM (SFM). Without action context awareness and asynchronous self-correction, SFM becomes unstable in long-horizon tasks, where a single action error can cascade into failure. In this work, we propose asynchronous flow matching VLA (AsyncVLA), a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. AsyncVLA breaks from the vanilla SFM in VLA models by generating the action tokens in a non-uniform time schedule with action context awareness. Besides, our method introduces the confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Moreover, we propose a unified training procedure for SFM and AFM that endows a single model with both modes, improving KV-cache utilization. Extensive experiments on robotic manipulation benchmarks demonstrate that AsyncVLA is data-efficient and exhibits self-correction ability. AsyncVLA outperforms existing methods across both simulation and real-world evaluations. Our code is available at https://github.com/YuhuaJiang2002/AsyncVLA.

## 核心内容
Vision-language-action (VLA) models have recently emerged as a powerful paradigm for building generalist robots. However, traditional VLA models that generate actions through flow matching (FM) typically rely on rigid and uniform time schedules, i.e., synchronous FM (SFM). Without action context awareness and asynchronous self-correction, SFM becomes unstable in long-horizon tasks, where a single action error can cascade into failure. In this work, we propose asynchronous flow matching VLA (AsyncVLA), a novel framework that introduces temporal flexibility in asynchronous FM (AFM) and enables self-correction in action generation. AsyncVLA breaks from the vanilla SFM in VLA models by generating the action tokens in a non-uniform time schedule with action context awareness. Besides, our method introduces the confidence rater to extract confidence of the initially generated actions, enabling the model to selectively refine inaccurate action tokens before execution. Moreover, we propose a unified training procedure for SFM and AFM that endows a single model with both modes, improving KV-cache utilization. Extensive experiments on robotic manipulation benchmarks demonstrate that AsyncVLA is data-efficient and exhibits self-correction ability. AsyncVLA outperforms existing methods across both simulation and real-world evaluations. Our code is available at https://github.com/YuhuaJiang2002/AsyncVLA.

## 参考
- http://arxiv.org/abs/2511.14148v2

