---
$id: ent_paper_lin_onetwovla_a_unified_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning'
  zh: OneTwoVLA
  ko: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning'
summary:
  en: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning (OneTwoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, Shanghai Artificial Intelligence
    Laboratory, Fudan University, Spirit AI.'
  zh: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning (OneTwoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, Shanghai Artificial Intelligence
    Laboratory, Fudan University, Spirit AI.'
  ko: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning (OneTwoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Shanghai Qi Zhi Institute, Shanghai Artificial Intelligence
    Laboratory, Fudan University, Spirit AI.'
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
- onetwovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.11917v2.
sources:
- id: src_001
  type: paper
  title: 'OneTwoVLA: A Unified Vision-Language-Action Model with Adaptive Reasoning (arXiv)'
  url: https://arxiv.org/abs/2505.11917
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: OneTwoVLA source
  url: https://doi.org/10.48550/arXiv.2505.11917
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
General-purpose robots capable of performing diverse tasks require synergistic reasoning and acting capabilities. However, recent dual-system approaches, which separate high-level reasoning from low-level acting, often suffer from challenges such as limited mutual understanding of capabilities between systems and latency issues. This paper introduces OneTwoVLA, a single unified vision-language-action model that can perform both acting (System One) and reasoning (System Two). Crucially, OneTwoVLA adaptively switches between two modes: explicitly reasoning at critical moments during task execution, and generating actions based on the most recent reasoning at other times. To further unlock OneTwoVLA's reasoning and generalization capabilities, we design a scalable pipeline for synthesizing embodied reasoning-centric vision-language data, used for co-training with robot data. We validate OneTwoVLA's effectiveness through extensive experiments, highlighting its superior performance across four key capabilities: long-horizon task planning, error detection and recovery, natural human-robot interaction, and generalizable visual grounding, enabling the model to perform long-horizon, highly dexterous manipulation tasks such as making hotpot or mixing cocktails.

## 核心内容
General-purpose robots capable of performing diverse tasks require synergistic reasoning and acting capabilities. However, recent dual-system approaches, which separate high-level reasoning from low-level acting, often suffer from challenges such as limited mutual understanding of capabilities between systems and latency issues. This paper introduces OneTwoVLA, a single unified vision-language-action model that can perform both acting (System One) and reasoning (System Two). Crucially, OneTwoVLA adaptively switches between two modes: explicitly reasoning at critical moments during task execution, and generating actions based on the most recent reasoning at other times. To further unlock OneTwoVLA's reasoning and generalization capabilities, we design a scalable pipeline for synthesizing embodied reasoning-centric vision-language data, used for co-training with robot data. We validate OneTwoVLA's effectiveness through extensive experiments, highlighting its superior performance across four key capabilities: long-horizon task planning, error detection and recovery, natural human-robot interaction, and generalizable visual grounding, enabling the model to perform long-horizon, highly dexterous manipulation tasks such as making hotpot or mixing cocktails.

## 参考
- http://arxiv.org/abs/2505.11917v2

