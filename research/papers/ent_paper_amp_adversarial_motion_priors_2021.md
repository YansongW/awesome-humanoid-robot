---
$id: ent_paper_amp_adversarial_motion_priors_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
  zh: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
  ko: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
summary:
  en: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control is a 2021 work on physics-based character
    animation for humanoid robots, with open-source code available.'
  zh: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control is a 2021 work on physics-based character
    animation for humanoid robots, with open-source code available.'
  ko: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control is a 2021 work on physics-based character
    animation for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- amp
- character_animation
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.02180v2.
sources:
- id: src_001
  type: paper
  title: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (arXiv)'
  url: https://arxiv.org/abs/2104.02180
  date: '2021'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control project page'
  url: https://xbpeng.github.io/projects/AMP/index.html
  date: '2021'
  accessed_at: '2026-07-01'
---
## 概述
Synthesizing graceful and life-like behaviors for physically simulated characters has been a fundamental challenge in computer animation. Data-driven methods that leverage motion tracking are a prominent class of techniques for producing high fidelity motions for a wide range of behaviors. However, the effectiveness of these tracking-based methods often hinges on carefully designed objective functions, and when applied to large and diverse motion datasets, these methods require significant additional machinery to select the appropriate motion for the character to track in a given scenario. In this work, we propose to obviate the need to manually design imitation objectives and mechanisms for motion selection by utilizing a fully automated approach based on adversarial imitation learning. High-level task objectives that the character should perform can be specified by relatively simple reward functions, while the low-level style of the character's behaviors can be specified by a dataset of unstructured motion clips, without any explicit clip selection or sequencing. These motion clips are used to train an adversarial motion prior, which specifies style-rewards for training the character through reinforcement learning (RL). The adversarial RL procedure automatically selects which motion to perform, dynamically interpolating and generalizing from the dataset. Our system produces high-quality motions that are comparable to those achieved by state-of-the-art tracking-based techniques, while also being able to easily accommodate large datasets of unstructured motion clips. Composition of disparate skills emerges automatically from the motion prior, without requiring a high-level motion planner or other task-specific annotations of the motion clips. We demonstrate the effectiveness of our framework on a diverse cast of complex simulated characters and a challenging suite of motor control tasks.

## 核心内容
Synthesizing graceful and life-like behaviors for physically simulated characters has been a fundamental challenge in computer animation. Data-driven methods that leverage motion tracking are a prominent class of techniques for producing high fidelity motions for a wide range of behaviors. However, the effectiveness of these tracking-based methods often hinges on carefully designed objective functions, and when applied to large and diverse motion datasets, these methods require significant additional machinery to select the appropriate motion for the character to track in a given scenario. In this work, we propose to obviate the need to manually design imitation objectives and mechanisms for motion selection by utilizing a fully automated approach based on adversarial imitation learning. High-level task objectives that the character should perform can be specified by relatively simple reward functions, while the low-level style of the character's behaviors can be specified by a dataset of unstructured motion clips, without any explicit clip selection or sequencing. These motion clips are used to train an adversarial motion prior, which specifies style-rewards for training the character through reinforcement learning (RL). The adversarial RL procedure automatically selects which motion to perform, dynamically interpolating and generalizing from the dataset. Our system produces high-quality motions that are comparable to those achieved by state-of-the-art tracking-based techniques, while also being able to easily accommodate large datasets of unstructured motion clips. Composition of disparate skills emerges automatically from the motion prior, without requiring a high-level motion planner or other task-specific annotations of the motion clips. We demonstrate the effectiveness of our framework on a diverse cast of complex simulated characters and a challenging suite of motor control tasks.

## 参考
- http://arxiv.org/abs/2104.02180v2

