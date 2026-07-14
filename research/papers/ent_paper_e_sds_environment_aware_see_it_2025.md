---
$id: ent_paper_e_sds_environment_aware_see_it_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion'
  zh: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion'
  ko: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion'
summary:
  en: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.'
  zh: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.'
  ko: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid Locomotion
    is a 2025 work on locomotion for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- e_sds
- humanoid
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.16446v1.
sources:
- id: src_001
  type: paper
  title: 'E-SDS: Environment-aware See it, Do it, Sorted - Automated Environment-Aware Reinforcement Learning for Humanoid
    Locomotion (arXiv)'
  url: https://arxiv.org/abs/2512.16446
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language models (VLMs) show promise in automating reward design in humanoid locomotion, which could eliminate the need for tedious manual engineering. However, current VLM-based methods are essentially "blind", as they lack the environmental perception required to navigate complex terrain. We present E-SDS (Environment-aware See it, Do it, Sorted), a framework that closes this perception gap. E-SDS integrates VLMs with real-time terrain sensor analysis to automatically generate reward functions that facilitate training of robust perceptive locomotion policies, grounded by example videos. Evaluated on a Unitree G1 humanoid across four distinct terrains (simple, gaps, obstacles, stairs), E-SDS uniquely enabled successful stair descent, while policies trained with manually-designed rewards or a non-perceptive automated baseline were unable to complete the task. In all terrains, E-SDS also reduced velocity tracking error by 51.9-82.6%. Our framework reduces the human effort of reward design from days to less than two hours while simultaneously producing more robust and capable locomotion policies.

## 核心内容
Vision-language models (VLMs) show promise in automating reward design in humanoid locomotion, which could eliminate the need for tedious manual engineering. However, current VLM-based methods are essentially "blind", as they lack the environmental perception required to navigate complex terrain. We present E-SDS (Environment-aware See it, Do it, Sorted), a framework that closes this perception gap. E-SDS integrates VLMs with real-time terrain sensor analysis to automatically generate reward functions that facilitate training of robust perceptive locomotion policies, grounded by example videos. Evaluated on a Unitree G1 humanoid across four distinct terrains (simple, gaps, obstacles, stairs), E-SDS uniquely enabled successful stair descent, while policies trained with manually-designed rewards or a non-perceptive automated baseline were unable to complete the task. In all terrains, E-SDS also reduced velocity tracking error by 51.9-82.6%. Our framework reduces the human effort of reward design from days to less than two hours while simultaneously producing more robust and capable locomotion policies.

## 参考
- http://arxiv.org/abs/2512.16446v1

