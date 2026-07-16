---
$id: ent_paper_softmimic_learning_compliant_w_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'SoftMimic: Learning Compliant Whole-body Control from Examples'
  zh: 'SoftMimic: Learning Compliant Whole-body Control from Examples'
  ko: 'SoftMimic: Learning Compliant Whole-body Control from Examples'
summary:
  en: 'SoftMimic: Learning Compliant Whole-body Control from Examples is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  zh: 'SoftMimic: Learning Compliant Whole-body Control from Examples is a 2025 work on loco-manipulation and whole-body-control
    for humanoid robots.'
  ko: 'SoftMimic: Learning Compliant Whole-body Control from Examples is a 2025 work on loco-manipulation and whole-body-control
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
- loco_manipulation
- softmimic
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.17792v1.
sources:
- id: src_001
  type: paper
  title: 'SoftMimic: Learning Compliant Whole-body Control from Examples (arXiv)'
  url: https://arxiv.org/abs/2510.17792
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
We introduce SoftMimic, a framework for learning compliant whole-body control policies for humanoid robots from example motions. Imitating human motions with reinforcement learning allows humanoids to quickly learn new skills, but existing methods incentivize stiff control that aggressively corrects deviations from a reference motion, leading to brittle and unsafe behavior when the robot encounters unexpected contacts. In contrast, SoftMimic enables robots to respond compliantly to external forces while maintaining balance and posture. Our approach leverages an inverse kinematics solver to generate an augmented dataset of feasible compliant motions, which we use to train a reinforcement learning policy. By rewarding the policy for matching compliant responses rather than rigidly tracking the reference motion, SoftMimic learns to absorb disturbances and generalize to varied tasks from a single motion clip. We validate our method through simulations and real-world experiments, demonstrating safe and effective interaction with the environment.

## 核心内容
We introduce SoftMimic, a framework for learning compliant whole-body control policies for humanoid robots from example motions. Imitating human motions with reinforcement learning allows humanoids to quickly learn new skills, but existing methods incentivize stiff control that aggressively corrects deviations from a reference motion, leading to brittle and unsafe behavior when the robot encounters unexpected contacts. In contrast, SoftMimic enables robots to respond compliantly to external forces while maintaining balance and posture. Our approach leverages an inverse kinematics solver to generate an augmented dataset of feasible compliant motions, which we use to train a reinforcement learning policy. By rewarding the policy for matching compliant responses rather than rigidly tracking the reference motion, SoftMimic learns to absorb disturbances and generalize to varied tasks from a single motion clip. We validate our method through simulations and real-world experiments, demonstrating safe and effective interaction with the environment.

## 参考
- http://arxiv.org/abs/2510.17792v1

## Overview
We introduce SoftMimic, a framework for learning compliant whole-body control policies for humanoid robots from example motions. Imitating human motions with reinforcement learning allows humanoids to quickly learn new skills, but existing methods incentivize stiff control that aggressively corrects deviations from a reference motion, leading to brittle and unsafe behavior when the robot encounters unexpected contacts. In contrast, SoftMimic enables robots to respond compliantly to external forces while maintaining balance and posture. Our approach leverages an inverse kinematics solver to generate an augmented dataset of feasible compliant motions, which we use to train a reinforcement learning policy. By rewarding the policy for matching compliant responses rather than rigidly tracking the reference motion, SoftMimic learns to absorb disturbances and generalize to varied tasks from a single motion clip. We validate our method through simulations and real-world experiments, demonstrating safe and effective interaction with the environment.

## Content
We introduce SoftMimic, a framework for learning compliant whole-body control policies for humanoid robots from example motions. Imitating human motions with reinforcement learning allows humanoids to quickly learn new skills, but existing methods incentivize stiff control that aggressively corrects deviations from a reference motion, leading to brittle and unsafe behavior when the robot encounters unexpected contacts. In contrast, SoftMimic enables robots to respond compliantly to external forces while maintaining balance and posture. Our approach leverages an inverse kinematics solver to generate an augmented dataset of feasible compliant motions, which we use to train a reinforcement learning policy. By rewarding the policy for matching compliant responses rather than rigidly tracking the reference motion, SoftMimic learns to absorb disturbances and generalize to varied tasks from a single motion clip. We validate our method through simulations and real-world experiments, demonstrating safe and effective interaction with the environment.

## 개요
우리는 SoftMimic을 소개합니다. 이는 예시 동작으로부터 휴머노이드 로봇의 순응적 전신 제어 정책을 학습하기 위한 프레임워크입니다. 강화 학습을 통해 인간의 동작을 모방하면 휴머노이드가 새로운 기술을 빠르게 습득할 수 있지만, 기존 방법은 기준 동작에서의 이탈을 적극적으로 보정하는 경직된 제어를 장려하여 로봇이 예상치 못한 접촉을 만날 때 취약하고 안전하지 않은 행동을 초래합니다. 반면, SoftMimic은 로봇이 균형과 자세를 유지하면서 외부 힘에 순응적으로 반응할 수 있도록 합니다. 우리의 접근 방식은 역기구학 솔버를 활용하여 실행 가능한 순응 동작의 증강 데이터셋을 생성하고, 이를 강화 학습 정책을 훈련하는 데 사용합니다. 정책이 기준 동작을 엄격히 추적하는 대신 순응적 반응을 일치시키도록 보상함으로써, SoftMimic은 교란을 흡수하고 단일 동작 클립에서 다양한 작업으로 일반화하는 방법을 학습합니다. 우리는 시뮬레이션과 실제 실험을 통해 이 방법을 검증하여 환경과의 안전하고 효과적인 상호작용을 입증합니다.

## 핵심 내용
우리는 SoftMimic을 소개합니다. 이는 예시 동작으로부터 휴머노이드 로봇의 순응적 전신 제어 정책을 학습하기 위한 프레임워크입니다. 강화 학습을 통해 인간의 동작을 모방하면 휴머노이드가 새로운 기술을 빠르게 습득할 수 있지만, 기존 방법은 기준 동작에서의 이탈을 적극적으로 보정하는 경직된 제어를 장려하여 로봇이 예상치 못한 접촉을 만날 때 취약하고 안전하지 않은 행동을 초래합니다. 반면, SoftMimic은 로봇이 균형과 자세를 유지하면서 외부 힘에 순응적으로 반응할 수 있도록 합니다. 우리의 접근 방식은 역기구학 솔버를 활용하여 실행 가능한 순응 동작의 증강 데이터셋을 생성하고, 이를 강화 학습 정책을 훈련하는 데 사용합니다. 정책이 기준 동작을 엄격히 추적하는 대신 순응적 반응을 일치시키도록 보상함으로써, SoftMimic은 교란을 흡수하고 단일 동작 클립에서 다양한 작업으로 일반화하는 방법을 학습합니다. 우리는 시뮬레이션과 실제 실험을 통해 이 방법을 검증하여 환경과의 안전하고 효과적인 상호작용을 입증합니다.
