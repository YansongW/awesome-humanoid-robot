---
$id: ent_paper_add_physics_based_motion_imita_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators'
  zh: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators'
  ko: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators'
summary:
  en: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators is a 2025 work on physics-based character
    animation for humanoid robots.'
  zh: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators is a 2025 work on physics-based character
    animation for humanoid robots.'
  ko: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators is a 2025 work on physics-based character
    animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- add
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.04961v2.
sources:
- id: src_001
  type: paper
  title: 'ADD: Physics-Based Motion Imitation with Adversarial Differential Discriminators (arXiv)'
  url: https://arxiv.org/abs/2505.04961v1
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Multi-objective optimization problems, which require the simultaneous optimization of multiple objectives, are prevalent across numerous applications. Existing multi-objective optimization methods often rely on manually-tuned aggregation functions to formulate a joint optimization objective. The performance of such hand-tuned methods is heavily dependent on careful weight selection, a time-consuming and laborious process. These limitations also arise in the setting of reinforcement-learning-based motion tracking methods for physically simulated characters, where intricately crafted reward functions are typically used to achieve high-fidelity results. Such solutions not only require domain expertise and significant manual tuning, but also limit the applicability of the resulting reward function across diverse skills. To bridge this gap, we present a novel adversarial multi-objective optimization technique that is broadly applicable to a range of multi-objective reinforcement-learning tasks, including motion tracking. Our proposed Adversarial Differential Discriminator (ADD) receives a single positive sample, yet is still effective at guiding the optimization process. We demonstrate that our technique can enable characters to closely replicate a variety of acrobatic and agile behaviors, achieving comparable quality to state-of-the-art motion-tracking methods, without relying on manually-designed reward functions. Code and results are available at https://add-moo.github.io/.

## 核心内容
Multi-objective optimization problems, which require the simultaneous optimization of multiple objectives, are prevalent across numerous applications. Existing multi-objective optimization methods often rely on manually-tuned aggregation functions to formulate a joint optimization objective. The performance of such hand-tuned methods is heavily dependent on careful weight selection, a time-consuming and laborious process. These limitations also arise in the setting of reinforcement-learning-based motion tracking methods for physically simulated characters, where intricately crafted reward functions are typically used to achieve high-fidelity results. Such solutions not only require domain expertise and significant manual tuning, but also limit the applicability of the resulting reward function across diverse skills. To bridge this gap, we present a novel adversarial multi-objective optimization technique that is broadly applicable to a range of multi-objective reinforcement-learning tasks, including motion tracking. Our proposed Adversarial Differential Discriminator (ADD) receives a single positive sample, yet is still effective at guiding the optimization process. We demonstrate that our technique can enable characters to closely replicate a variety of acrobatic and agile behaviors, achieving comparable quality to state-of-the-art motion-tracking methods, without relying on manually-designed reward functions. Code and results are available at https://add-moo.github.io/.

## 参考
- http://arxiv.org/abs/2505.04961v2

