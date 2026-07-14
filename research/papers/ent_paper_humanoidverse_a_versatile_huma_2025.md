---
$id: ent_paper_humanoidverse_a_versatile_huma_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement'
  zh: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement'
  ko: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement'
summary:
  en: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  zh: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
  ko: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement is a 2025 work on loco-manipulation
    and whole-body-control for humanoid robots.'
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
- humanoidverse
- loco_manipulation
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.16943v3.
sources:
- id: src_001
  type: paper
  title: 'HumanoidVerse: A Versatile Humanoid for Vision-Language Guided Multi-Object Rearrangement (arXiv)'
  url: https://arxiv.org/abs/2508.16943
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Physics-based human motion control can make a simulated character walk, sit, and manipulate objects with high physical realism. Almost always, though, this happens in short, isolated clips that are re-initialized between interactions. We instead aim for continuous, reset-free long-horizon motion: a physically simulated humanoid that repeatedly walks to a displaced object, lifts it with a balanced whole-body posture, carries it past obstacles, and places it at a goal, over and over within a single uninterrupted take. The hard part is not any individual motion but the transitions between them. Without a reset, each cycle must end in a state that both leaves the object just placed undisturbed and lets the next cycle begin, yet every placement leaves the character off-balance in a non-canonical pose where naive end-to-end reinforcement learning fails. Our key idea is to treat this handoff as a two-sided problem of recoverability: the character must disengage from the object it just placed so the prior success is preserved, and settle into a state from which a balanced continuation exists. Instead of engineering a transition by hand, we learn to shape where each cycle ends so that it lands in this recoverable region. We introduce LHM-Humanoid. One goal-conditioned controller completes a fetch--carry--place cycle and, through a learned release-and-retreat behavior, steers its terminal state into this region; a second controller then takes over from the resulting state distribution. Both are regularized by an adversarial motion prior and distilled into a single goal-conditioned policy that runs the whole sequence as one reset-free rollout. Across 350 cluttered layouts spanning four room types, LHM-Humanoid produces far more successful and stable long-horizon motion than end-to-end RL, hierarchical RL, and prior physics-based human-scene-interaction methods, on both seen and unseen scenes.

## 核心内容
Physics-based human motion control can make a simulated character walk, sit, and manipulate objects with high physical realism. Almost always, though, this happens in short, isolated clips that are re-initialized between interactions. We instead aim for continuous, reset-free long-horizon motion: a physically simulated humanoid that repeatedly walks to a displaced object, lifts it with a balanced whole-body posture, carries it past obstacles, and places it at a goal, over and over within a single uninterrupted take. The hard part is not any individual motion but the transitions between them. Without a reset, each cycle must end in a state that both leaves the object just placed undisturbed and lets the next cycle begin, yet every placement leaves the character off-balance in a non-canonical pose where naive end-to-end reinforcement learning fails. Our key idea is to treat this handoff as a two-sided problem of recoverability: the character must disengage from the object it just placed so the prior success is preserved, and settle into a state from which a balanced continuation exists. Instead of engineering a transition by hand, we learn to shape where each cycle ends so that it lands in this recoverable region. We introduce LHM-Humanoid. One goal-conditioned controller completes a fetch--carry--place cycle and, through a learned release-and-retreat behavior, steers its terminal state into this region; a second controller then takes over from the resulting state distribution. Both are regularized by an adversarial motion prior and distilled into a single goal-conditioned policy that runs the whole sequence as one reset-free rollout. Across 350 cluttered layouts spanning four room types, LHM-Humanoid produces far more successful and stable long-horizon motion than end-to-end RL, hierarchical RL, and prior physics-based human-scene-interaction methods, on both seen and unseen scenes.

## 参考
- http://arxiv.org/abs/2508.16943v3

