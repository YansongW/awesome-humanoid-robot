---
$id: ent_paper_shi_memoryvla_perceptual_cognitive_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation'
  zh: MemoryVLA
  ko: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation'
summary:
  en: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation (MemoryVLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Dexmal, MEGVII Technology,
    Tianjin University, Harbin Institute of Technology, StepFun.'
  zh: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation (MemoryVLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Dexmal, MEGVII Technology,
    Tianjin University, Harbin Institute of Technology, StepFun.'
  ko: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation (MemoryVLA), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Tsinghua University, Dexmal, MEGVII Technology,
    Tianjin University, Harbin Institute of Technology, StepFun.'
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
- memoryvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19236v2.
sources:
- id: src_001
  type: paper
  title: 'MemoryVLA: Perceptual-Cognitive Memory in Vision-Language-Action Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2508.19236
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MemoryVLA source
  url: https://doi.org/10.48550/arXiv.2508.19236
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Temporal context is essential for robotic manipulation because such tasks are inherently non-Markovian, yet mainstream VLA models typically overlook it and struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived representations for immediate control, while the hippocampal system preserves verbatim episodic details and semantic gist of past experience for long-term memory. Inspired by these mechanisms, we propose MemoryVLA, a Cognition-Memory-Action framework for long-horizon robotic manipulation. A pretrained VLM encodes the observation into perceptual and cognitive tokens that form working memory, while a Perceptual-Cognitive Memory Bank stores low-level details and high-level semantics consolidated from it. Working memory retrieves decision-relevant entries from the bank, adaptively fuses them with current tokens, and updates the bank by merging redundancies. Using these tokens, a memory-conditioned diffusion action expert yields temporally aware action sequences. We evaluate MemoryVLA on 150+ simulation and real-world tasks across three robots. On SimplerEnv-Bridge, Fractal, LIBERO-5 suites and Mikasa-Robo, it achieves 71.9%, 72.7%, 96.5%, and 41.2% success rates, respectively, all outperforming state-of-the-art baselines CogACT and pi-0, with a notable +14.6 gain on Bridge and +11.8 gain on Mikasa-Robo. On 12 real-world tasks spanning general skills and long-horizon temporal dependencies, MemoryVLA achieves 84.0% success rate, with long-horizon tasks showing a +26 improvement over state-of-the-art baseline. Project Page: https://shihao1895.github.io/MemoryVLA

## 核心内容
Temporal context is essential for robotic manipulation because such tasks are inherently non-Markovian, yet mainstream VLA models typically overlook it and struggle with long-horizon, temporally dependent tasks. Cognitive science suggests that humans rely on working memory to buffer short-lived representations for immediate control, while the hippocampal system preserves verbatim episodic details and semantic gist of past experience for long-term memory. Inspired by these mechanisms, we propose MemoryVLA, a Cognition-Memory-Action framework for long-horizon robotic manipulation. A pretrained VLM encodes the observation into perceptual and cognitive tokens that form working memory, while a Perceptual-Cognitive Memory Bank stores low-level details and high-level semantics consolidated from it. Working memory retrieves decision-relevant entries from the bank, adaptively fuses them with current tokens, and updates the bank by merging redundancies. Using these tokens, a memory-conditioned diffusion action expert yields temporally aware action sequences. We evaluate MemoryVLA on 150+ simulation and real-world tasks across three robots. On SimplerEnv-Bridge, Fractal, LIBERO-5 suites and Mikasa-Robo, it achieves 71.9%, 72.7%, 96.5%, and 41.2% success rates, respectively, all outperforming state-of-the-art baselines CogACT and pi-0, with a notable +14.6 gain on Bridge and +11.8 gain on Mikasa-Robo. On 12 real-world tasks spanning general skills and long-horizon temporal dependencies, MemoryVLA achieves 84.0% success rate, with long-horizon tasks showing a +26 improvement over state-of-the-art baseline. Project Page: https://shihao1895.github.io/MemoryVLA

## 参考
- http://arxiv.org/abs/2508.19236v2

