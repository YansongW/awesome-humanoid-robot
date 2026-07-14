---
$id: ent_paper_simgenhoi_physically_realistic_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL'
  zh: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL'
  ko: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL'
summary:
  en: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL is a 2025 work
    on physics-based character animation for humanoid robots.'
  zh: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL is a 2025 work
    on physics-based character animation for humanoid robots.'
  ko: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL is a 2025 work
    on physics-based character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- physics_based
- simgenhoi
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.14120v1.
sources:
- id: src_001
  type: paper
  title: 'SimGenHOI: Physically Realistic Whole-Body Humanoid-Object Interaction via Generative Modeling and RL (arXiv)'
  url: https://arxiv.org/abs/2508.14120
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Generating physically realistic humanoid-object interactions (HOI) is a fundamental challenge in robotics. Existing HOI generation approaches, such as diffusion-based models, often suffer from artifacts such as implausible contacts, penetrations, and unrealistic whole-body actions, which hinder successful execution in physical environments. To address these challenges, we introduce SimGenHOI, a unified framework that combines the strengths of generative modeling and reinforcement learning to produce controllable and physically plausible HOI. Our HOI generative model, based on Diffusion Transformers (DiT), predicts a set of key actions conditioned on text prompts, object geometry, sparse object waypoints, and the initial humanoid pose. These key actions capture essential interaction dynamics and are interpolated into smooth motion trajectories, naturally supporting long-horizon generation. To ensure physical realism, we design a contact-aware whole-body control policy trained with reinforcement learning, which tracks the generated motions while correcting artifacts such as penetration and foot sliding. Furthermore, we introduce a mutual fine-tuning strategy, where the generative model and the control policy iteratively refine each other, improving both motion realism and tracking robustness. Extensive experiments demonstrate that SimGenHOI generates realistic, diverse, and physically plausible humanoid-object interactions, achieving significantly higher tracking success rates in simulation and enabling long-horizon manipulation tasks. Code will be released upon acceptance on our project page: https://xingxingzuo.github.io/simgen_hoi.

## 核心内容
Generating physically realistic humanoid-object interactions (HOI) is a fundamental challenge in robotics. Existing HOI generation approaches, such as diffusion-based models, often suffer from artifacts such as implausible contacts, penetrations, and unrealistic whole-body actions, which hinder successful execution in physical environments. To address these challenges, we introduce SimGenHOI, a unified framework that combines the strengths of generative modeling and reinforcement learning to produce controllable and physically plausible HOI. Our HOI generative model, based on Diffusion Transformers (DiT), predicts a set of key actions conditioned on text prompts, object geometry, sparse object waypoints, and the initial humanoid pose. These key actions capture essential interaction dynamics and are interpolated into smooth motion trajectories, naturally supporting long-horizon generation. To ensure physical realism, we design a contact-aware whole-body control policy trained with reinforcement learning, which tracks the generated motions while correcting artifacts such as penetration and foot sliding. Furthermore, we introduce a mutual fine-tuning strategy, where the generative model and the control policy iteratively refine each other, improving both motion realism and tracking robustness. Extensive experiments demonstrate that SimGenHOI generates realistic, diverse, and physically plausible humanoid-object interactions, achieving significantly higher tracking success rates in simulation and enabling long-horizon manipulation tasks. Code will be released upon acceptance on our project page: https://xingxingzuo.github.io/simgen_hoi.

## 参考
- http://arxiv.org/abs/2508.14120v1

