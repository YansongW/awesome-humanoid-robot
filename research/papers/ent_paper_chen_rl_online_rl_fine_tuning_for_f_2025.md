---
$id: ent_paper_chen_rl_online_rl_fine_tuning_for_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models'
  zh: π_RL
  ko: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models'
summary:
  en: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models (π_RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Peking University, Institute of Automation, Chinese
    Academy of Sciences, Carnegie Mellon University, Infinigence AI, Zhongguancun Academy.'
  zh: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models (π_RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Peking University, Institute of Automation, Chinese
    Academy of Sciences, Carnegie Mellon University, Infinigence AI, Zhongguancun Academy.'
  ko: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models (π_RL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua University, Peking University, Institute of Automation, Chinese
    Academy of Sciences, Carnegie Mellon University, Infinigence AI, Zhongguancun Academy.'
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
- rl
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25889v3.
sources:
- id: src_001
  type: paper
  title: 'πRL: Online RL Fine-tuning for Flow-based Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2510.25889
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: π_RL source
  url: https://doi.org/10.48550/arXiv.2510.25889
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models enable robots to understand and perform complex tasks from multimodal input. Although recent work explores using reinforcement learning (RL) to automate the laborious data collection process in scaling supervised fine-tuning (SFT), applying RL to large-scale flow-based VLAs (\eg, $π_0$, $π_{0.5}$) remains challenging due to intractable action log-likelihoods raised from flow matching. We address this challenge with $π_{\texttt{RL}}$, featuring two technical approaches: (1) \textbf{Flow-Noise} models the denoising process as a discrete-time MDP with a learnable noise network for exact log-likelihood computation. (2) \textbf{Flow-SDE} integrates denoising with agent-environment interaction, formulating a two-layer MDP that employs ODE-to-SDE conversion for efficient RL exploration. We evaluate $π_{\texttt{RL}}$ across various benchmarks, with experiments demonstrating that RL yields significant performance improvements in both in-distribution and out-of-distribution settings.

## 核心内容
Vision-Language-Action (VLA) models enable robots to understand and perform complex tasks from multimodal input. Although recent work explores using reinforcement learning (RL) to automate the laborious data collection process in scaling supervised fine-tuning (SFT), applying RL to large-scale flow-based VLAs (\eg, $π_0$, $π_{0.5}$) remains challenging due to intractable action log-likelihoods raised from flow matching. We address this challenge with $π_{\texttt{RL}}$, featuring two technical approaches: (1) \textbf{Flow-Noise} models the denoising process as a discrete-time MDP with a learnable noise network for exact log-likelihood computation. (2) \textbf{Flow-SDE} integrates denoising with agent-environment interaction, formulating a two-layer MDP that employs ODE-to-SDE conversion for efficient RL exploration. We evaluate $π_{\texttt{RL}}$ across various benchmarks, with experiments demonstrating that RL yields significant performance improvements in both in-distribution and out-of-distribution settings.

## 参考
- http://arxiv.org/abs/2510.25889v3

