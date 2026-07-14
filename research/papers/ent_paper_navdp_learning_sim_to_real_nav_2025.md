---
$id: ent_paper_navdp_learning_sim_to_real_nav_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance'
  zh: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance'
  ko: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance'
summary:
  en: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance is a 2025 work on navigation
    for humanoid robots.'
  zh: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance is a 2025 work on navigation
    for humanoid robots.'
  ko: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance is a 2025 work on navigation
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- navdp
- navigation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.08712v3.
sources:
- id: src_001
  type: paper
  title: 'NavDP: Learning Sim-to-Real Navigation Diffusion Policy with Privileged Information Guidance (arXiv)'
  url: https://arxiv.org/abs/2505.08712
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Learning to navigate in dynamic and complex open-world environments is a critical yet challenging capability for autonomous robots. Existing approaches often rely on cascaded modular frameworks, which require extensive hyperparameter tuning or learning from limited real-world demonstration data. In this paper, we propose Navigation Diffusion Policy (NavDP), an end-to-end network trained solely in simulation that enables zero-shot sim-to-real transfer across diverse environments and robot embodiments. The core of NavDP is a unified transformer-based architecture that jointly learns trajectory generation and trajectory evaluation, both conditioned solely on local RGB-D observation. By learning to predict critic values for contrastive trajectory samples, our proposed approach effectively leverages supervision from privileged information available in simulation, thereby fostering accurate spatial understanding and enabling the distinction between safe and dangerous behaviors. To support this, we develop an efficient data generation pipeline in simulation and construct a large-scale dataset encompassing over one million meters of navigation experience across 3,000 scenes. Empirical experiments in both simulated and real-world environments demonstrate that NavDP significantly outperforms prior state-of-the-art methods. Furthermore, we identify key factors influencing the generalization performance of NavDP. The dataset and code are publicly available at https://wzcai99.github.io/navigation-diffusion-policy.github.io.

## 核心内容
Learning to navigate in dynamic and complex open-world environments is a critical yet challenging capability for autonomous robots. Existing approaches often rely on cascaded modular frameworks, which require extensive hyperparameter tuning or learning from limited real-world demonstration data. In this paper, we propose Navigation Diffusion Policy (NavDP), an end-to-end network trained solely in simulation that enables zero-shot sim-to-real transfer across diverse environments and robot embodiments. The core of NavDP is a unified transformer-based architecture that jointly learns trajectory generation and trajectory evaluation, both conditioned solely on local RGB-D observation. By learning to predict critic values for contrastive trajectory samples, our proposed approach effectively leverages supervision from privileged information available in simulation, thereby fostering accurate spatial understanding and enabling the distinction between safe and dangerous behaviors. To support this, we develop an efficient data generation pipeline in simulation and construct a large-scale dataset encompassing over one million meters of navigation experience across 3,000 scenes. Empirical experiments in both simulated and real-world environments demonstrate that NavDP significantly outperforms prior state-of-the-art methods. Furthermore, we identify key factors influencing the generalization performance of NavDP. The dataset and code are publicly available at https://wzcai99.github.io/navigation-diffusion-policy.github.io.

## 参考
- http://arxiv.org/abs/2505.08712v3

