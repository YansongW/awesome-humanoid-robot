---
$id: ent_paper_wang_cot4ad_a_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving'
  zh: CoT4AD
  ko: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving'
summary:
  en: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (CoT4AD), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University.'
  zh: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (CoT4AD), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University.'
  ko: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (CoT4AD), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Peking University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- cot4ad
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.22532v1.
sources:
- id: src_001
  type: paper
  title: 'CoT4AD: A Vision-Language-Action Model with Explicit Chain-of-Thought Reasoning for Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2511.22532
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: CoT4AD source
  url: https://doi.org/10.48550/arXiv.2511.22532
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have recently attracted growing attention in end-to-end autonomous driving for their strong reasoning capabilities and rich world knowledge. However, existing VLAs often suffer from limited numerical reasoning ability and overly simplified input-output mappings, which hinder their performance in complex driving scenarios requiring step-by-step causal reasoning. To address these challenges, we propose CoT4AD, a novel VLA framework that introduces Chain-of-Thought (CoT) reasoning for autonomous driving to enhance both numerical and causal reasoning in Vision-Language Models (VLMs). CoT4AD integrates visual observations and language instructions to perform semantic reasoning, scene understanding, and trajectory planning. During training, it explicitly models a perception-question-prediction-action CoT to align the reasoning space with the action space across multiple driving tasks. During inference, it performs implicit CoT reasoning to enable consistent numerical reasoning and robust decision-making in dynamic environments. Extensive experiments on both real-world and simulated benchmarks, including nuScenes and Bench2Drive, demonstrate that CoT4AD achieves state-of-the-art performance in both open-loop and closed-loop evaluations. Code will be released upon paper acceptance.

## 核心内容
Vision-Language-Action (VLA) models have recently attracted growing attention in end-to-end autonomous driving for their strong reasoning capabilities and rich world knowledge. However, existing VLAs often suffer from limited numerical reasoning ability and overly simplified input-output mappings, which hinder their performance in complex driving scenarios requiring step-by-step causal reasoning. To address these challenges, we propose CoT4AD, a novel VLA framework that introduces Chain-of-Thought (CoT) reasoning for autonomous driving to enhance both numerical and causal reasoning in Vision-Language Models (VLMs). CoT4AD integrates visual observations and language instructions to perform semantic reasoning, scene understanding, and trajectory planning. During training, it explicitly models a perception-question-prediction-action CoT to align the reasoning space with the action space across multiple driving tasks. During inference, it performs implicit CoT reasoning to enable consistent numerical reasoning and robust decision-making in dynamic environments. Extensive experiments on both real-world and simulated benchmarks, including nuScenes and Bench2Drive, demonstrate that CoT4AD achieves state-of-the-art performance in both open-loop and closed-loop evaluations. Code will be released upon paper acceptance.

## 参考
- http://arxiv.org/abs/2511.22532v1

