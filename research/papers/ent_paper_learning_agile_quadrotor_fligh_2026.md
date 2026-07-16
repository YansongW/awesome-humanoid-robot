---
$id: ent_paper_learning_agile_quadrotor_fligh_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning Agile Quadrotor Flight in the Real World
  zh: Learning Agile Quadrotor Flight in the Real World
  ko: Learning Agile Quadrotor Flight in the Real World
summary:
  en: 'arXiv:2602.10111v2 Announce Type: replace Abstract: Learning-based controllers have achieved impressive performance
    in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification
    for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution
    scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these
    evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining
    their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical
    limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive
    framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive
    Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a
    simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation
    Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that
    our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base
    policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore
    that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained
    performance improvement in aggressive flight regimes.'
  zh: 'arXiv:2602.10111v2 Announce Type: replace Abstract: Learning-based controllers have achieved impressive performance
    in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification
    for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution
    scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these
    evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining
    their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical
    limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive
    framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive
    Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a
    simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation
    Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that
    our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base
    policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore
    that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained
    performance improvement in aggressive flight regimes.'
  ko: 'arXiv:2602.10111v2 Announce Type: replace Abstract: Learning-based controllers have achieved impressive performance
    in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification
    for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution
    scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these
    evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining
    their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical
    limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive
    framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive
    Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a
    simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation
    Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that
    our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base
    policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore
    that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained
    performance improvement in aggressive flight regimes.'
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
- learning_agile_quadrotor_fligh
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.10111v2.
sources:
- id: src_001
  type: paper
  title: Learning Agile Quadrotor Flight in the Real World (arXiv)
  url: https://arxiv.org/abs/2602.10111
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

## 核心内容
Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. {Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

## 参考
- http://arxiv.org/abs/2602.10111v2

## Overview
Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

## Content
Learning-based controllers have achieved impressive performance in agile quadrotor flight but typically rely on massive training in simulation, necessitating accurate system identification for effective Sim2Real transfer. However, even with precise modeling, fixed policies remain susceptible to out-of-distribution scenarios, ranging from external aerodynamic disturbances to internal hardware degradation. To ensure safety under these evolving uncertainties, such controllers are forced to operate with conservative safety margins, inherently constraining their agility outside of controlled settings. While online adaptation offers a potential remedy, safely exploring physical limits remains a critical bottleneck due to data scarcity and safety risks. To bridge this gap, we propose a self-adaptive framework that eliminates the need for precise system identification or offline Sim2Real transfer. We introduce Adaptive Temporal Scaling (ATS) to actively explore platform physical limits, and employ online residual learning to augment a simple nominal model. Based on the learned hybrid model, we further propose Real-world Anchored Short-horizon Backpropagation Through Time (RASH-BPTT) to achieve efficient and robust in-flight policy updates. Extensive experiments demonstrate that our quadrotor reliably executes agile maneuvers near actuator saturation limits. The system evolves a conservative base policy with a peak speed of 1.9 m/s to 7.3 m/s within approximately 100 seconds of flight time. These findings underscore that real-world adaptation serves not merely to compensate for modeling errors, but as a practical mechanism for sustained performance improvement in aggressive flight regimes.

## 개요
학습 기반 제어기는 민첩한 쿼드로터 비행에서 인상적인 성능을 달성했지만, 일반적으로 시뮬레이션에서 대규모 훈련에 의존하며, 효과적인 Sim2Real 전이를 위해 정확한 시스템 식별이 필요합니다. 그러나 정밀한 모델링이 있더라도 고정된 정책은 외부 공기역학적 교란부터 내부 하드웨어 성능 저하에 이르기까지 분포 외 시나리오에 취약합니다. 이러한 변화하는 불확실성 하에서 안전을 보장하기 위해, 이러한 제어기는 보수적인 안전 마진으로 작동해야 하며, 이는 통제된 환경 외부에서의 민첩성을 본질적으로 제한합니다. 온라인 적응이 잠재적 해결책을 제공하지만, 데이터 부족과 안전 위험으로 인해 물리적 한계를 안전하게 탐색하는 것은 여전히 중요한 병목 현상입니다. 이러한 격차를 해소하기 위해, 우리는 정밀한 시스템 식별이나 오프라인 Sim2Real 전이가 필요 없는 자가 적응 프레임워크를 제안합니다. 우리는 적응형 시간 스케일링(ATS)을 도입하여 플랫폼의 물리적 한계를 적극적으로 탐색하고, 온라인 잔차 학습을 사용하여 간단한 명목 모델을 보강합니다. 학습된 하이브리드 모델을 기반으로, 우리는 실세계 고정 단기 시간 역전파(RASH-BPTT)를 추가로 제안하여 효율적이고 강건한 비행 중 정책 업데이트를 달성합니다. 광범위한 실험을 통해 우리의 쿼드로터가 액추에이터 포화 한계 근처에서 민첩한 기동을 안정적으로 실행함을 입증했습니다. 시스템은 약 100초의 비행 시간 내에 최고 속도 1.9m/s에서 7.3m/s로 보수적인 기본 정책을 진화시킵니다. 이러한 결과는 실제 적응이 단순히 모델링 오류를 보상하는 것이 아니라, 공격적인 비행 영역에서 지속적인 성능 향상을 위한 실용적인 메커니즘으로 작용함을 강조합니다.

## 핵심 내용
학습 기반 제어기는 민첩한 쿼드로터 비행에서 인상적인 성능을 달성했지만, 일반적으로 시뮬레이션에서 대규모 훈련에 의존하며, 효과적인 Sim2Real 전이를 위해 정확한 시스템 식별이 필요합니다. 그러나 정밀한 모델링이 있더라도 고정된 정책은 외부 공기역학적 교란부터 내부 하드웨어 성능 저하에 이르기까지 분포 외 시나리오에 취약합니다. 이러한 변화하는 불확실성 하에서 안전을 보장하기 위해, 이러한 제어기는 보수적인 안전 마진으로 작동해야 하며, 이는 통제된 환경 외부에서의 민첩성을 본질적으로 제한합니다. 온라인 적응이 잠재적 해결책을 제공하지만, 데이터 부족과 안전 위험으로 인해 물리적 한계를 안전하게 탐색하는 것은 여전히 중요한 병목 현상입니다. 이러한 격차를 해소하기 위해, 우리는 정밀한 시스템 식별이나 오프라인 Sim2Real 전이가 필요 없는 자가 적응 프레임워크를 제안합니다. 우리는 적응형 시간 스케일링(ATS)을 도입하여 플랫폼의 물리적 한계를 적극적으로 탐색하고, 온라인 잔차 학습을 사용하여 간단한 명목 모델을 보강합니다. 학습된 하이브리드 모델을 기반으로, 우리는 실세계 고정 단기 시간 역전파(RASH-BPTT)를 추가로 제안하여 효율적이고 강건한 비행 중 정책 업데이트를 달성합니다. 광범위한 실험을 통해 우리의 쿼드로터가 액추에이터 포화 한계 근처에서 민첩한 기동을 안정적으로 실행함을 입증했습니다. 시스템은 약 100초의 비행 시간 내에 최고 속도 1.9m/s에서 7.3m/s로 보수적인 기본 정책을 진화시킵니다. 이러한 결과는 실제 적응이 단순히 모델링 오류를 보상하는 것이 아니라, 공격적인 비행 영역에서 지속적인 성능 향상을 위한 실용적인 메커니즘으로 작용함을 강조합니다.
