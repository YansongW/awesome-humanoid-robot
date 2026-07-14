---
$id: ent_paper_wang_lola_long_horizon_latent_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation'
  zh: LoLA
  ko: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation'
summary:
  en: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation (LoLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
  zh: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation (LoLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
  ko: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation (LoLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Institute of Microelectronics, Chinese Academy of Sciences, University of
    Chinese Academy of Sciences, Microsoft Research.'
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
- lola
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.20166v1.
sources:
- id: src_001
  type: paper
  title: 'LoLA: Long Horizon Latent Action Learning for General Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.20166
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: LoLA source
  url: https://doi.org/10.48550/arXiv.2512.20166
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
The capability of performing long-horizon, language-guided robotic manipulation tasks critically relies on leveraging historical information and generating coherent action sequences. However, such capabilities are often overlooked by existing Vision-Language-Action (VLA) models. To solve this challenge, we propose LoLA (Long Horizon Latent Action Learning), a framework designed for robot manipulation that integrates long-term multi-view observations and robot proprioception to enable multi-step reasoning and action generation. We first employ Vision-Language Models to encode rich contextual features from historical sequences and multi-view observations. We further introduces a key module, State-Aware Latent Re-representation, which transforms visual inputs and language commands into actionable robot motion space. Unlike existing VLA approaches that merely concatenate robot proprioception (e.g., joint angles) with VL embeddings, this module leverages such robot states to explicitly ground VL representations in physical scale through a learnable "embodiment-anchored" latent space. We trained LoLA on diverse robotic pre-training datasets and conducted extensive evaluations on simulation benchmarks (SIMPLER and LIBERO), as well as two real-world tasks on Franka and Bi-Manual Aloha robots. Results show that LoLA significantly outperforms prior state-of-the-art methods (e.g., pi0), particularly in long-horizon manipulation tasks.

## 核心内容
The capability of performing long-horizon, language-guided robotic manipulation tasks critically relies on leveraging historical information and generating coherent action sequences. However, such capabilities are often overlooked by existing Vision-Language-Action (VLA) models. To solve this challenge, we propose LoLA (Long Horizon Latent Action Learning), a framework designed for robot manipulation that integrates long-term multi-view observations and robot proprioception to enable multi-step reasoning and action generation. We first employ Vision-Language Models to encode rich contextual features from historical sequences and multi-view observations. We further introduces a key module, State-Aware Latent Re-representation, which transforms visual inputs and language commands into actionable robot motion space. Unlike existing VLA approaches that merely concatenate robot proprioception (e.g., joint angles) with VL embeddings, this module leverages such robot states to explicitly ground VL representations in physical scale through a learnable "embodiment-anchored" latent space. We trained LoLA on diverse robotic pre-training datasets and conducted extensive evaluations on simulation benchmarks (SIMPLER and LIBERO), as well as two real-world tasks on Franka and Bi-Manual Aloha robots. Results show that LoLA significantly outperforms prior state-of-the-art methods (e.g., pi0), particularly in long-horizon manipulation tasks.

## 参考
- http://arxiv.org/abs/2512.20166v1

