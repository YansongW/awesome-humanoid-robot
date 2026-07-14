---
$id: ent_paper_lin_storm_search_guided_generative_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'STORM: Search-Guided Generative World Models for Robotic Manipulation'
  zh: STORM
  ko: 'STORM: Search-Guided Generative World Models for Robotic Manipulation'
summary:
  en: 'STORM: Search-Guided Generative World Models for Robotic Manipulation (STORM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University.'
  zh: 'STORM: Search-Guided Generative World Models for Robotic Manipulation (STORM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University.'
  ko: 'STORM: Search-Guided Generative World Models for Robotic Manipulation (STORM), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Sun Yat-sen University.'
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
- storm
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.18477v1.
sources:
- id: src_001
  type: paper
  title: 'STORM: Search-Guided Generative World Models for Robotic Manipulation (arXiv)'
  url: https://arxiv.org/abs/2512.18477
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: STORM source
  url: https://doi.org/10.48550/arXiv.2512.18477
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We present STORM (Search-Guided Generative World Models), a novel framework for spatio-temporal reasoning in robotic manipulation that unifies diffusion-based action generation, conditional video prediction, and search-based planning. Unlike prior Vision-Language-Action (VLA) models that rely on abstract latent dynamics or delegate reasoning to language components, STORM grounds planning in explicit visual rollouts, enabling interpretable and foresight-driven decision-making. A diffusion-based VLA policy proposes diverse candidate actions, a generative video world model simulates their visual and reward outcomes, and Monte Carlo Tree Search (MCTS) selectively refines plans through lookahead evaluation. Experiments on the SimplerEnv manipulation benchmark demonstrate that STORM achieves a new state-of-the-art average success rate of 51.0 percent, outperforming strong baselines such as CogACT. Reward-augmented video prediction substantially improves spatio-temporal fidelity and task relevance, reducing Frechet Video Distance by over 75 percent. Moreover, STORM exhibits robust re-planning and failure recovery behavior, highlighting the advantages of search-guided generative world models for long-horizon robotic manipulation.

## 核心内容
We present STORM (Search-Guided Generative World Models), a novel framework for spatio-temporal reasoning in robotic manipulation that unifies diffusion-based action generation, conditional video prediction, and search-based planning. Unlike prior Vision-Language-Action (VLA) models that rely on abstract latent dynamics or delegate reasoning to language components, STORM grounds planning in explicit visual rollouts, enabling interpretable and foresight-driven decision-making. A diffusion-based VLA policy proposes diverse candidate actions, a generative video world model simulates their visual and reward outcomes, and Monte Carlo Tree Search (MCTS) selectively refines plans through lookahead evaluation. Experiments on the SimplerEnv manipulation benchmark demonstrate that STORM achieves a new state-of-the-art average success rate of 51.0 percent, outperforming strong baselines such as CogACT. Reward-augmented video prediction substantially improves spatio-temporal fidelity and task relevance, reducing Frechet Video Distance by over 75 percent. Moreover, STORM exhibits robust re-planning and failure recovery behavior, highlighting the advantages of search-guided generative world models for long-horizon robotic manipulation.

## 参考
- http://arxiv.org/abs/2512.18477v1

