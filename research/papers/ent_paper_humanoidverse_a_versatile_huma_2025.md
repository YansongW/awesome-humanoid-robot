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

## Overview
Physics-based human motion control can make a simulated character walk, sit, and manipulate objects with high physical realism. Almost always, though, this happens in short, isolated clips that are re-initialized between interactions. We instead aim for continuous, reset-free long-horizon motion: a physically simulated humanoid that repeatedly walks to a displaced object, lifts it with a balanced whole-body posture, carries it past obstacles, and places it at a goal, over and over within a single uninterrupted take. The hard part is not any individual motion but the transitions between them. Without a reset, each cycle must end in a state that both leaves the object just placed undisturbed and lets the next cycle begin, yet every placement leaves the character off-balance in a non-canonical pose where naive end-to-end reinforcement learning fails. Our key idea is to treat this handoff as a two-sided problem of recoverability: the character must disengage from the object it just placed so the prior success is preserved, and settle into a state from which a balanced continuation exists. Instead of engineering a transition by hand, we learn to shape where each cycle ends so that it lands in this recoverable region. We introduce LHM-Humanoid. One goal-conditioned controller completes a fetch--carry--place cycle and, through a learned release-and-retreat behavior, steers its terminal state into this region; a second controller then takes over from the resulting state distribution. Both are regularized by an adversarial motion prior and distilled into a single goal-conditioned policy that runs the whole sequence as one reset-free rollout. Across 350 cluttered layouts spanning four room types, LHM-Humanoid produces far more successful and stable long-horizon motion than end-to-end RL, hierarchical RL, and prior physics-based human-scene-interaction methods, on both seen and unseen scenes.

## Content
Physics-based human motion control can make a simulated character walk, sit, and manipulate objects with high physical realism. Almost always, though, this happens in short, isolated clips that are re-initialized between interactions. We instead aim for continuous, reset-free long-horizon motion: a physically simulated humanoid that repeatedly walks to a displaced object, lifts it with a balanced whole-body posture, carries it past obstacles, and places it at a goal, over and over within a single uninterrupted take. The hard part is not any individual motion but the transitions between them. Without a reset, each cycle must end in a state that both leaves the object just placed undisturbed and lets the next cycle begin, yet every placement leaves the character off-balance in a non-canonical pose where naive end-to-end reinforcement learning fails. Our key idea is to treat this handoff as a two-sided problem of recoverability: the character must disengage from the object it just placed so the prior success is preserved, and settle into a state from which a balanced continuation exists. Instead of engineering a transition by hand, we learn to shape where each cycle ends so that it lands in this recoverable region. We introduce LHM-Humanoid. One goal-conditioned controller completes a fetch--carry--place cycle and, through a learned release-and-retreat behavior, steers its terminal state into this region; a second controller then takes over from the resulting state distribution. Both are regularized by an adversarial motion prior and distilled into a single goal-conditioned policy that runs the whole sequence as one reset-free rollout. Across 350 cluttered layouts spanning four room types, LHM-Humanoid produces far more successful and stable long-horizon motion than end-to-end RL, hierarchical RL, and prior physics-based human-scene-interaction methods, on both seen and unseen scenes.

## 개요
물리 기반 인간 동작 제어는 시뮬레이션된 캐릭터가 높은 물리적 사실성으로 걷고, 앉고, 물체를 조작할 수 있게 합니다. 하지만 거의 항상 이러한 동작은 상호작용 사이에 재초기화되는 짧고 고립된 클립에서 발생합니다. 우리는 대신 연속적이고 리셋 없는 장기 동작을 목표로 합니다: 물리적으로 시뮬레이션된 휴머노이드가 한 번의 중단 없는 테이크 내에서 반복적으로 이동된 물체로 걸어가고, 균형 잡힌 전신 자세로 들어 올리고, 장애물을 지나 운반한 후 목표 지점에 놓는 동작을 반복합니다. 어려운 점은 개별 동작이 아니라 그 사이의 전환입니다. 리셋 없이 각 주기는 방금 놓은 물체를 방해하지 않으면서 다음 주기가 시작될 수 있는 상태로 끝나야 하지만, 모든 배치는 캐릭터를 비정규적인 자세로 불균형하게 만들어 순진한 종단간 강화 학습이 실패하게 만듭니다. 우리의 핵심 아이디어는 이 핸드오프를 회복 가능성의 양면 문제로 다루는 것입니다: 캐릭터는 방금 놓은 물체에서 분리되어 이전 성공을 유지하고, 균형 잡힌 연속이 가능한 상태로 안착해야 합니다. 수동으로 전환을 설계하는 대신, 각 주기가 이 회복 가능한 영역에 도달하도록 끝나는 지점을 형성하는 방법을 학습합니다. 우리는 LHM-Humanoid를 소개합니다. 하나의 목표 조건 제어기는 fetch-carry-place 주기를 완료하고, 학습된 release-and-retreat 행동을 통해 종단 상태를 이 영역으로 유도합니다; 두 번째 제어기는 결과 상태 분포에서 이를 이어받습니다. 둘 다 적대적 동작 사전에 의해 정규화되고, 전체 시퀀스를 하나의 리셋 없는 롤아웃으로 실행하는 단일 목표 조건 정책으로 증류됩니다. 네 가지 방 유형에 걸친 350개의 복잡한 배치에서 LHM-Humanoid는 보이는 장면과 보이지 않는 장면 모두에서 종단간 RL, 계층적 RL 및 기존 물리 기반 인간-장면 상호작용 방법보다 훨씬 더 성공적이고 안정적인 장기 동작을 생성합니다.

## 핵심 내용
물리 기반 인간 동작 제어는 시뮬레이션된 캐릭터가 높은 물리적 사실성으로 걷고, 앉고, 물체를 조작할 수 있게 합니다. 하지만 거의 항상 이러한 동작은 상호작용 사이에 재초기화되는 짧고 고립된 클립에서 발생합니다. 우리는 대신 연속적이고 리셋 없는 장기 동작을 목표로 합니다: 물리적으로 시뮬레이션된 휴머노이드가 한 번의 중단 없는 테이크 내에서 반복적으로 이동된 물체로 걸어가고, 균형 잡힌 전신 자세로 들어 올리고, 장애물을 지나 운반한 후 목표 지점에 놓는 동작을 반복합니다. 어려운 점은 개별 동작이 아니라 그 사이의 전환입니다. 리셋 없이 각 주기는 방금 놓은 물체를 방해하지 않으면서 다음 주기가 시작될 수 있는 상태로 끝나야 하지만, 모든 배치는 캐릭터를 비정규적인 자세로 불균형하게 만들어 순진한 종단간 강화 학습이 실패하게 만듭니다. 우리의 핵심 아이디어는 이 핸드오프를 회복 가능성의 양면 문제로 다루는 것입니다: 캐릭터는 방금 놓은 물체에서 분리되어 이전 성공을 유지하고, 균형 잡힌 연속이 가능한 상태로 안착해야 합니다. 수동으로 전환을 설계하는 대신, 각 주기가 이 회복 가능한 영역에 도달하도록 끝나는 지점을 형성하는 방법을 학습합니다. 우리는 LHM-Humanoid를 소개합니다. 하나의 목표 조건 제어기는 fetch-carry-place 주기를 완료하고, 학습된 release-and-retreat 행동을 통해 종단 상태를 이 영역으로 유도합니다; 두 번째 제어기는 결과 상태 분포에서 이를 이어받습니다. 둘 다 적대적 동작 사전에 의해 정규화되고, 전체 시퀀스를 하나의 리셋 없는 롤아웃으로 실행하는 단일 목표 조건 정책으로 증류됩니다. 네 가지 방 유형에 걸친 350개의 복잡한 배치에서 LHM-Humanoid는 보이는 장면과 보이지 않는 장면 모두에서 종단간 RL, 계층적 RL 및 기존 물리 기반 인간-장면 상호작용 방법보다 훨씬 더 성공적이고 안정적인 장기 동작을 생성합니다.
