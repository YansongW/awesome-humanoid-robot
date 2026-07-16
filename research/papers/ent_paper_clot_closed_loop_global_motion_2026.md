---
$id: ent_paper_clot_closed_loop_global_motion_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation'
  zh: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation'
  ko: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation'
summary:
  en: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation is a 2026 work on teleoperation for
    humanoid robots.'
  zh: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation is a 2026 work on teleoperation for
    humanoid robots.'
  ko: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation is a 2026 work on teleoperation for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- clot
- humanoid
- teleoperation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.15060v2.
sources:
- id: src_001
  type: paper
  title: 'CLOT: Closed-Loop Global Motion Tracking for Whole-Body Humanoid Teleoperation (arXiv)'
  url: https://arxiv.org/abs/2602.15060
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids. Although recent learning-based tracking methods enable agile and coordinated motions, they typically operate in the robot's local frame and neglect global pose feedback, leading to drift and instability during extended execution. In this work, we present CLOT, a real-time whole-body humanoid teleoperation system that achieves closed-loop global motion tracking via high-frequency localization feedback. CLOT synchronizes operator and robot poses in a closed loop, enabling drift-free human-to-humanoid mimicry over long timehorizons. However, directly imposing global tracking rewards in reinforcement learning, often results in aggressive and brittle corrections. To address this, we propose a data-driven randomization strategy that decouples observation trajectories from reward evaluation, enabling smooth and stable global corrections. We further regularize the policy with an adversarial motion prior to suppress unnatural behaviors. To support CLOT, we collect 20 hours of carefully curated human motion data for training the humanoid teleoperation policy. We design a transformer-based policy and train it for over 1300 GPU hours. The policy is deployed on a full-sized humanoid with 31 DoF (excluding hands). Both simulation and real-world experiments verify high-dynamic motion, high-precision tracking, and strong robustness in sim-to-real humanoid teleoperation. Motion data, demos and code can be found in our website.

## 核心内容
Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids. Although recent learning-based tracking methods enable agile and coordinated motions, they typically operate in the robot's local frame and neglect global pose feedback, leading to drift and instability during extended execution. In this work, we present CLOT, a real-time whole-body humanoid teleoperation system that achieves closed-loop global motion tracking via high-frequency localization feedback. CLOT synchronizes operator and robot poses in a closed loop, enabling drift-free human-to-humanoid mimicry over long timehorizons. However, directly imposing global tracking rewards in reinforcement learning, often results in aggressive and brittle corrections. To address this, we propose a data-driven randomization strategy that decouples observation trajectories from reward evaluation, enabling smooth and stable global corrections. We further regularize the policy with an adversarial motion prior to suppress unnatural behaviors. To support CLOT, we collect 20 hours of carefully curated human motion data for training the humanoid teleoperation policy. We design a transformer-based policy and train it for over 1300 GPU hours. The policy is deployed on a full-sized humanoid with 31 DoF (excluding hands). Both simulation and real-world experiments verify high-dynamic motion, high-precision tracking, and strong robustness in sim-to-real humanoid teleoperation. Motion data, demos and code can be found in our website.

## 参考
- http://arxiv.org/abs/2602.15060v2

## Overview
Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids. Although recent learning-based tracking methods enable agile and coordinated motions, they typically operate in the robot's local frame and neglect global pose feedback, leading to drift and instability during extended execution. In this work, we present CLOT, a real-time whole-body humanoid teleoperation system that achieves closed-loop global motion tracking via high-frequency localization feedback. CLOT synchronizes operator and robot poses in a closed loop, enabling drift-free human-to-humanoid mimicry over long time horizons. However, directly imposing global tracking rewards in reinforcement learning often results in aggressive and brittle corrections. To address this, we propose a data-driven randomization strategy that decouples observation trajectories from reward evaluation, enabling smooth and stable global corrections. We further regularize the policy with an adversarial motion prior to suppress unnatural behaviors. To support CLOT, we collect 20 hours of carefully curated human motion data for training the humanoid teleoperation policy. We design a transformer-based policy and train it for over 1300 GPU hours. The policy is deployed on a full-sized humanoid with 31 DoF (excluding hands). Both simulation and real-world experiments verify high-dynamic motion, high-precision tracking, and strong robustness in sim-to-real humanoid teleoperation. Motion data, demos and code can be found on our website.

## Content
Long-horizon whole-body humanoid teleoperation remains challenging due to accumulated global pose drift, particularly on full-sized humanoids. Although recent learning-based tracking methods enable agile and coordinated motions, they typically operate in the robot's local frame and neglect global pose feedback, leading to drift and instability during extended execution. In this work, we present CLOT, a real-time whole-body humanoid teleoperation system that achieves closed-loop global motion tracking via high-frequency localization feedback. CLOT synchronizes operator and robot poses in a closed loop, enabling drift-free human-to-humanoid mimicry over long time horizons. However, directly imposing global tracking rewards in reinforcement learning often results in aggressive and brittle corrections. To address this, we propose a data-driven randomization strategy that decouples observation trajectories from reward evaluation, enabling smooth and stable global corrections. We further regularize the policy with an adversarial motion prior to suppress unnatural behaviors. To support CLOT, we collect 20 hours of carefully curated human motion data for training the humanoid teleoperation policy. We design a transformer-based policy and train it for over 1300 GPU hours. The policy is deployed on a full-sized humanoid with 31 DoF (excluding hands). Both simulation and real-world experiments verify high-dynamic motion, high-precision tracking, and strong robustness in sim-to-real humanoid teleoperation. Motion data, demos and code can be found on our website.

## 개요
장시간 전신 휴머노이드 원격 조작은 특히 대형 휴머노이드에서 누적되는 전역 자세 드리프트로 인해 여전히 어려운 과제입니다. 최근의 학습 기반 추적 방법은 민첩하고 조화로운 움직임을 가능하게 하지만, 일반적으로 로봇의 로컬 프레임에서 작동하며 전역 자세 피드백을 무시하여 장시간 실행 시 드리프트와 불안정성을 초래합니다. 본 연구에서는 고주파 위치 추정 피드백을 통해 폐루프 전역 움직임 추적을 달성하는 실시간 전신 휴머노이드 원격 조작 시스템인 CLOT을 제시합니다. CLOT은 연산자와 로봇의 자세를 폐루프로 동기화하여 장시간에 걸쳐 드리프트 없는 인간-휴머노이드 모방을 가능하게 합니다. 그러나 강화 학습에서 전역 추적 보상을 직접 적용하면 종종 공격적이고 취약한 보정이 발생합니다. 이를 해결하기 위해 관찰 궤적을 보상 평가에서 분리하는 데이터 기반 무작위화 전략을 제안하여 부드럽고 안정적인 전역 보정을 가능하게 합니다. 또한 적대적 움직임 사전을 사용하여 정책을 정규화함으로써 비자연스러운 행동을 억제합니다. CLOT을 지원하기 위해 휴머노이드 원격 조작 정책 훈련을 위해 20시간의 엄선된 인간 움직임 데이터를 수집했습니다. 트랜스포머 기반 정책을 설계하고 1300 GPU 시간 이상 훈련했습니다. 이 정책은 손을 제외한 31 자유도를 가진 대형 휴머노이드에 배포되었습니다. 시뮬레이션 및 실제 실험을 통해 시뮬레이션-실제 휴머노이드 원격 조작에서 고동적 움직임, 고정밀 추적 및 강력한 견고성을 검증했습니다. 움직임 데이터, 데모 및 코드는 웹사이트에서 확인할 수 있습니다.

## 핵심 내용
장시간 전신 휴머노이드 원격 조작은 특히 대형 휴머노이드에서 누적되는 전역 자세 드리프트로 인해 여전히 어려운 과제입니다. 최근의 학습 기반 추적 방법은 민첩하고 조화로운 움직임을 가능하게 하지만, 일반적으로 로봇의 로컬 프레임에서 작동하며 전역 자세 피드백을 무시하여 장시간 실행 시 드리프트와 불안정성을 초래합니다. 본 연구에서는 고주파 위치 추정 피드백을 통해 폐루프 전역 움직임 추적을 달성하는 실시간 전신 휴머노이드 원격 조작 시스템인 CLOT을 제시합니다. CLOT은 연산자와 로봇의 자세를 폐루프로 동기화하여 장시간에 걸쳐 드리프트 없는 인간-휴머노이드 모방을 가능하게 합니다. 그러나 강화 학습에서 전역 추적 보상을 직접 적용하면 종종 공격적이고 취약한 보정이 발생합니다. 이를 해결하기 위해 관찰 궤적을 보상 평가에서 분리하는 데이터 기반 무작위화 전략을 제안하여 부드럽고 안정적인 전역 보정을 가능하게 합니다. 또한 적대적 움직임 사전을 사용하여 정책을 정규화함으로써 비자연스러운 행동을 억제합니다. CLOT을 지원하기 위해 휴머노이드 원격 조작 정책 훈련을 위해 20시간의 엄선된 인간 움직임 데이터를 수집했습니다. 트랜스포머 기반 정책을 설계하고 1300 GPU 시간 이상 훈련했습니다. 이 정책은 손을 제외한 31 자유도를 가진 대형 휴머노이드에 배포되었습니다. 시뮬레이션 및 실제 실험을 통해 시뮬레이션-실제 휴머노이드 원격 조작에서 고동적 움직임, 고정밀 추적 및 강력한 견고성을 검증했습니다. 움직임 데이터, 데모 및 코드는 웹사이트에서 확인할 수 있습니다.
