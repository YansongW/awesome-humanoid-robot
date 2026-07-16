---
$id: ent_paper_learning_gait_aware_quadruped_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications
  zh: Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications
  ko: Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications
summary:
  en: 'arXiv:2607.00442v1 Announce Type: new Abstract: Reinforcement learning (RL) for quadruped locomotion commonly depends
    on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit
    control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints
    expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking,
    and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a
    dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes
    (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth
    approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible
    with Proximal Policy Optimization (PPO). We instantiate the approach on Google''s Barkour quadruped robot in MuJoCo XLA
    (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify
    learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity
    tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.'
  zh: 'arXiv:2607.00442v1 Announce Type: new Abstract: Reinforcement learning (RL) for quadruped locomotion commonly depends
    on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit
    control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints
    expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking,
    and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a
    dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes
    (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth
    approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible
    with Proximal Policy Optimization (PPO). We instantiate the approach on Google''s Barkour quadruped robot in MuJoCo XLA
    (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify
    learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity
    tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.'
  ko: 'arXiv:2607.00442v1 Announce Type: new Abstract: Reinforcement learning (RL) for quadruped locomotion commonly depends
    on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit
    control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints
    expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking,
    and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a
    dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes
    (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth
    approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible
    with Proximal Policy Optimization (PPO). We instantiate the approach on Google''s Barkour quadruped robot in MuJoCo XLA
    (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify
    learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity
    tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.'
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
- robotics
- learning_gait_aware_quadruped
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00442v1.
sources:
- id: src_001
  type: paper
  title: Learning Gait-Aware Quadruped Locomotion with Temporal Logic Specifications (arXiv)
  url: https://arxiv.org/abs/2607.00442
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述
Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking, and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.

## 核心内容
Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking, and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.

## 参考
- http://arxiv.org/abs/2607.00442v1

## Overview
Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking, and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.

## Content
Reinforcement learning (RL) for quadruped locomotion commonly depends on fixed, hand-crafted, and Markovian reward functions that limit both interpretability of learned policies and lack explicit control over gait behaviors. We introduce a framework where distinct gaits are specified using parameterized constraints expressed in Signal Temporal Logic (STL). These include safety bounds, gait synchronization constraints, command tracking, and actuation bounds. From these specifications, we develop a reward shaping mechanism that provides learning agents a dense, continuous reward landscape that encodes desired behavior. We define parametric STL templates for three speed regimes (walking-trot, trot, bound), calibrate their parameters from reference rollouts, and compute rewards from using smooth approximations of STL robustness over the rollouts. The generated rewards can be used to provide shaped gradients compatible with Proximal Policy Optimization (PPO). We instantiate the approach on Google's Barkour quadruped robot in MuJoCo XLA (MJX). We use parallelization within the simulator to improve training speeds and use domain randomization to robustify learned policies. We show that compared to a baseline of hand-crafted rewards, the STL-shaped rewards yield tighter velocity tracking and more stable training. Videos can be found on our project website: https://stl-locomotion.github.io/.

## 개요
사족 보행을 위한 강화 학습(RL)은 일반적으로 고정되고 수작업으로 설계된 마르코프 보상 함수에 의존하며, 이는 학습된 정책의 해석 가능성을 제한하고 보행 동작에 대한 명시적 제어가 부족합니다. 본 연구에서는 신호 시간 논리(STL)로 표현된 매개변수화된 제약 조건을 사용하여 다양한 보행을 지정하는 프레임워크를 소개합니다. 여기에는 안전 경계, 보행 동기화 제약 조건, 명령 추적 및 작동 경계가 포함됩니다. 이러한 명세를 바탕으로 학습 에이전트에 원하는 동작을 인코딩하는 조밀하고 연속적인 보상 공간을 제공하는 보상 형성 메커니즘을 개발합니다. 세 가지 속도 영역(걷기-트로트, 트로트, 바운드)에 대한 매개변수화된 STL 템플릿을 정의하고, 참조 롤아웃에서 매개변수를 보정한 후 롤아웃에 대한 STL 강건성의 매끄러운 근사를 사용하여 보상을 계산합니다. 생성된 보상은 근접 정책 최적화(PPO)와 호환되는 형성된 그래디언트를 제공하는 데 사용할 수 있습니다. 이 접근 방식을 Google의 Barkour 사족 로봇에 MuJoCo XLA(MJX) 환경에서 구현합니다. 시뮬레이터 내 병렬화를 사용하여 훈련 속도를 향상시키고 도메인 무작위화를 사용하여 학습된 정책을 강건하게 만듭니다. 수작업 보상 기준선과 비교하여 STL 형성 보상이 더 정밀한 속도 추적과 더 안정적인 훈련을 제공함을 보여줍니다. 비디오는 프로젝트 웹사이트에서 확인할 수 있습니다: https://stl-locomotion.github.io/.

## 핵심 내용
사족 보행을 위한 강화 학습(RL)은 일반적으로 고정되고 수작업으로 설계된 마르코프 보상 함수에 의존하며, 이는 학습된 정책의 해석 가능성을 제한하고 보행 동작에 대한 명시적 제어가 부족합니다. 본 연구에서는 신호 시간 논리(STL)로 표현된 매개변수화된 제약 조건을 사용하여 다양한 보행을 지정하는 프레임워크를 소개합니다. 여기에는 안전 경계, 보행 동기화 제약 조건, 명령 추적 및 작동 경계가 포함됩니다. 이러한 명세를 바탕으로 학습 에이전트에 원하는 동작을 인코딩하는 조밀하고 연속적인 보상 공간을 제공하는 보상 형성 메커니즘을 개발합니다. 세 가지 속도 영역(걷기-트로트, 트로트, 바운드)에 대한 매개변수화된 STL 템플릿을 정의하고, 참조 롤아웃에서 매개변수를 보정한 후 롤아웃에 대한 STL 강건성의 매끄러운 근사를 사용하여 보상을 계산합니다. 생성된 보상은 근접 정책 최적화(PPO)와 호환되는 형성된 그래디언트를 제공하는 데 사용할 수 있습니다. 이 접근 방식을 Google의 Barkour 사족 로봇에 MuJoCo XLA(MJX) 환경에서 구현합니다. 시뮬레이터 내 병렬화를 사용하여 훈련 속도를 향상시키고 도메인 무작위화를 사용하여 학습된 정책을 강건하게 만듭니다. 수작업 보상 기준선과 비교하여 STL 형성 보상이 더 정밀한 속도 추적과 더 안정적인 훈련을 제공함을 보여줍니다. 비디오는 프로젝트 웹사이트에서 확인할 수 있습니다: https://stl-locomotion.github.io/.
