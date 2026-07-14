---
$id: ent_paper_tedi_temporally_entangled_diff_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
  zh: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
  ko: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
summary:
  en: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.'
  zh: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.'
  ko: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- tedi
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.15042v2.
sources:
- id: src_001
  type: paper
  title: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis (arXiv)'
  url: https://arxiv.org/abs/2307.15042
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
The gradual nature of a diffusion process that synthesizes samples in small increments constitutes a key ingredient of Denoising Diffusion Probabilistic Models (DDPM), which have presented unprecedented quality in image synthesis and been recently explored in the motion domain. In this work, we propose to adapt the gradual diffusion concept (operating along a diffusion time-axis) into the temporal-axis of the motion sequence. Our key idea is to extend the DDPM framework to support temporally varying denoising, thereby entangling the two axes. Using our special formulation, we iteratively denoise a motion buffer that contains a set of increasingly-noised poses, which auto-regressively produces an arbitrarily long stream of frames. With a stationary diffusion time-axis, in each diffusion step we increment only the temporal-axis of the motion such that the framework produces a new, clean frame which is removed from the beginning of the buffer, followed by a newly drawn noise vector that is appended to it. This new mechanism paves the way towards a new framework for long-term motion synthesis with applications to character animation and other domains.

## 核心内容
The gradual nature of a diffusion process that synthesizes samples in small increments constitutes a key ingredient of Denoising Diffusion Probabilistic Models (DDPM), which have presented unprecedented quality in image synthesis and been recently explored in the motion domain. In this work, we propose to adapt the gradual diffusion concept (operating along a diffusion time-axis) into the temporal-axis of the motion sequence. Our key idea is to extend the DDPM framework to support temporally varying denoising, thereby entangling the two axes. Using our special formulation, we iteratively denoise a motion buffer that contains a set of increasingly-noised poses, which auto-regressively produces an arbitrarily long stream of frames. With a stationary diffusion time-axis, in each diffusion step we increment only the temporal-axis of the motion such that the framework produces a new, clean frame which is removed from the beginning of the buffer, followed by a newly drawn noise vector that is appended to it. This new mechanism paves the way towards a new framework for long-term motion synthesis with applications to character animation and other domains.

## 参考
- http://arxiv.org/abs/2307.15042v2

