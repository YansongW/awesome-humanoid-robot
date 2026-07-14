---
$id: ent_paper_wang_spec_vla_speculative_decoding_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance'
  zh: Spec-VLA
  ko: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance'
summary:
  en: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (Spec-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by NLP2CT Lab, University of Macau, Infinigence AI,
    Tsinghua University, Zhongguancun Academy, NICS-EFC Lab.'
  zh: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (Spec-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by NLP2CT Lab, University of Macau, Infinigence AI,
    Tsinghua University, Zhongguancun Academy, NICS-EFC Lab.'
  ko: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (Spec-VLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by NLP2CT Lab, University of Macau, Infinigence AI,
    Tsinghua University, Zhongguancun Academy, NICS-EFC Lab.'
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
- spec_vla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.22424v2.
sources:
- id: src_001
  type: paper
  title: 'Spec-VLA: Speculative Decoding for Vision-Language-Action Models with Relaxed Acceptance (arXiv)'
  url: https://arxiv.org/abs/2507.22424
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Spec-VLA source
  url: https://doi.org/10.48550/arXiv.2507.22424
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have made substantial progress by leveraging the robust capabilities of Visual Language Models (VLMs). However, VLMs' significant parameter size and autoregressive (AR) decoding nature impose considerable computational demands on VLA models. While Speculative Decoding (SD) has shown efficacy in accelerating Large Language Models (LLMs) by incorporating efficient drafting and parallel verification, allowing multiple tokens to be generated in one forward pass, its application to VLA models remains unexplored. This work introduces Spec-VLA, an SD framework designed to accelerate VLA models. Due to the difficulty of the action prediction task and the greedy decoding mechanism of the VLA models, the direct application of the advanced SD framework to the VLA prediction task yields a minor speed improvement. To boost the generation speed, we propose an effective mechanism to relax acceptance utilizing the relative distances represented by the action tokens of the VLA model. Empirical results across diverse test scenarios affirm the effectiveness of the Spec-VLA framework, and further analysis substantiates the impact of our proposed strategies, which enhance the acceptance length by 44%, achieving 1.42 times speedup compared with the OpenVLA baseline, without compromising the success rate. The success of the Spec-VLA framework highlights the potential for broader application of speculative execution in VLA prediction scenarios.

## 核心内容
Vision-Language-Action (VLA) models have made substantial progress by leveraging the robust capabilities of Visual Language Models (VLMs). However, VLMs' significant parameter size and autoregressive (AR) decoding nature impose considerable computational demands on VLA models. While Speculative Decoding (SD) has shown efficacy in accelerating Large Language Models (LLMs) by incorporating efficient drafting and parallel verification, allowing multiple tokens to be generated in one forward pass, its application to VLA models remains unexplored. This work introduces Spec-VLA, an SD framework designed to accelerate VLA models. Due to the difficulty of the action prediction task and the greedy decoding mechanism of the VLA models, the direct application of the advanced SD framework to the VLA prediction task yields a minor speed improvement. To boost the generation speed, we propose an effective mechanism to relax acceptance utilizing the relative distances represented by the action tokens of the VLA model. Empirical results across diverse test scenarios affirm the effectiveness of the Spec-VLA framework, and further analysis substantiates the impact of our proposed strategies, which enhance the acceptance length by 44%, achieving 1.42 times speedup compared with the OpenVLA baseline, without compromising the success rate. The success of the Spec-VLA framework highlights the potential for broader application of speculative execution in VLA prediction scenarios.

## 参考
- http://arxiv.org/abs/2507.22424v2

