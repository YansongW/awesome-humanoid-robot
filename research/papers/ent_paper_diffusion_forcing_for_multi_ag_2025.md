---
$id: ent_paper_diffusion_forcing_for_multi_ag_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
  zh: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
  ko: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling
summary:
  en: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  zh: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
  ko: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling is a 2025 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- diffusion_forcing_for_multi_ag
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.17900v2.
sources:
- id: src_001
  type: paper
  title: Diffusion Forcing for Multi-Agent Interaction Sequence Modeling (arXiv)
  url: https://arxiv.org/abs/2512.17900
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Understanding and generating multi-person interactions is a fundamental challenge with broad implications for robotics and social computing. While humans naturally coordinate in groups, modeling such interactions remains difficult due to long temporal horizons, strong inter-agent dependencies, and variable group sizes. Existing motion generation methods are largely task-specific and do not generalize to flexible multi-agent generation. We introduce MAGNet (Multi-Agent Generative Network), a unified autoregressive diffusion framework for multi-agent motion generation that supports a wide range of interaction tasks through flexible conditioning and sampling. MAGNet performs dyadic and polyadic prediction, partner inpainting, partner prediction, and agentic generation all within a single model, and can autoregressively generate ultra-long sequences spanning hundreds of motion steps. We explicitly model inter-agent coupling during autoregressive denoising, enabling coherent coordination across agents. As a result, MAGNet captures both tightly synchronized activities (e.g., dancing, boxing) and loosely structured social interactions. Our approach performs on par with specialized methods on dyadic benchmarks while naturally extending to polyadic scenarios involving three or more interacting people. Please watch the supplemental video, where the temporal dynamics and spatial coordination of generated interactions are best appreciated. Project page: https://von31.github.io/MAGNet/

## 核心内容
Understanding and generating multi-person interactions is a fundamental challenge with broad implications for robotics and social computing. While humans naturally coordinate in groups, modeling such interactions remains difficult due to long temporal horizons, strong inter-agent dependencies, and variable group sizes. Existing motion generation methods are largely task-specific and do not generalize to flexible multi-agent generation. We introduce MAGNet (Multi-Agent Generative Network), a unified autoregressive diffusion framework for multi-agent motion generation that supports a wide range of interaction tasks through flexible conditioning and sampling. MAGNet performs dyadic and polyadic prediction, partner inpainting, partner prediction, and agentic generation all within a single model, and can autoregressively generate ultra-long sequences spanning hundreds of motion steps. We explicitly model inter-agent coupling during autoregressive denoising, enabling coherent coordination across agents. As a result, MAGNet captures both tightly synchronized activities (e.g., dancing, boxing) and loosely structured social interactions. Our approach performs on par with specialized methods on dyadic benchmarks while naturally extending to polyadic scenarios involving three or more interacting people. Please watch the supplemental video, where the temporal dynamics and spatial coordination of generated interactions are best appreciated. Project page: https://von31.github.io/MAGNet/

## 参考
- http://arxiv.org/abs/2512.17900v2

