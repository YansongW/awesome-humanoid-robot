---
$id: ent_paper_clear_closed_loop_reinforcemen_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving'
  zh: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving'
  ko: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving'
summary:
  en: 'arXiv:2607.02841v1 Announce Type: new Abstract: End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor
    information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers
    have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception,
    language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts
    imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories.
    Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop
    planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning
    (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained
    VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL
    for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design
    a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to
    dramatically increase the number of simulation environments running in parallel while avoiding resource contention and
    maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and
    sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.'
  zh: 'arXiv:2607.02841v1 Announce Type: new Abstract: End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor
    information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers
    have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception,
    language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts
    imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories.
    Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop
    planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning
    (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained
    VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL
    for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design
    a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to
    dramatically increase the number of simulation environments running in parallel while avoiding resource contention and
    maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and
    sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.'
  ko: 'arXiv:2607.02841v1 Announce Type: new Abstract: End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor
    information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers
    have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception,
    language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts
    imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories.
    Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop
    planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning
    (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained
    VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL
    for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design
    a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to
    dramatically increase the number of simulation environments running in parallel while avoiding resource contention and
    maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and
    sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.'
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
- clear
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.02841v1.
sources:
- id: src_001
  type: paper
  title: 'CLEAR: Closed-Loop Reinforcement Learning at Scale for End-to-End Autonomous Driving (arXiv)'
  url: https://arxiv.org/abs/2607.02841
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception, language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories. Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.

## 核心内容
End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception, language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories. Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.

## 参考
- http://arxiv.org/abs/2607.02841v1

## Overview
End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception, language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories. Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.

## Content
End-to-end autonomous driving (E2E-AD) aims to directly map raw sensor information to driving actions. Recently, with the rapid advancement of multi-modal large language models (MLLMs), researchers have proposed the paradigm of Vision-Language-Action (VLA) models for E2E-AD, where it seeks to integrate visual perception, language understanding and action prediction within a single policy. However, existing VLA-based policies largely adopts imitation learning, where it only learns to drive by optimizing distance-based metrics w.r.t. logged expert trajectories. Such distribution shift between open-loop training and closed-loop inference leads to suboptimal performance in closed-loop planning. To close this gap, we present CLEAR, a system that enables closed-loop training using Reinforcement Learning (RL) at scale for E2E-AD. We propose to learn a novel residual waypoint policy around the waypoint prior from pretrained VLA policies, effectively harnessing the knowledge within. On another front, one of the key challenges to scale up RL for vision-based policies is the number of parallel simulation environments since RL is data hungry. To that end, we design a heterogeneous pipeline that places the simulator and the VLA learner on distinct compute groups, which allows us to dramatically increase the number of simulation environments running in parallel while avoiding resource contention and maintaining training stability. We show that with a simple reward, CLEAR significantly outperforms previous methods and sets new state-of-the-art performance on the challenging benchmarks of CARLA longest6 v2 and Bench2Drive.

## 개요
엔드투엔드 자율주행(E2E-AD)은 원시 센서 정보를 주행 동작에 직접 매핑하는 것을 목표로 합니다. 최근 다중 모달 대규모 언어 모델(MLLM)의 급속한 발전과 함께 연구자들은 E2E-AD를 위한 Vision-Language-Action(VLA) 모델 패러다임을 제안했으며, 이는 시각적 인식, 언어 이해 및 행동 예측을 단일 정책 내에 통합하고자 합니다. 그러나 기존 VLA 기반 정책은 대부분 모방 학습을 채택하여, 기록된 전문가 궤적에 대한 거리 기반 메트릭을 최적화함으로써 주행을 학습합니다. 이러한 개방 루프 학습과 폐쇄 루프 추론 간의 분포 변화는 폐쇄 루프 계획에서 최적 이하의 성능을 초래합니다. 이러한 격차를 해소하기 위해, 우리는 E2E-AD를 위한 대규모 강화 학습(RL)을 사용한 폐쇄 루프 학습을 가능하게 하는 시스템인 CLEAR를 제시합니다. 우리는 사전 훈련된 VLA 정책의 웨이포인트 사전 정보를 기반으로 새로운 잔차 웨이포인트 정책을 학습하여, 내부 지식을 효과적으로 활용할 것을 제안합니다. 다른 측면에서, 시각 기반 정책을 위한 RL을 확장하는 주요 과제 중 하나는 RL이 데이터를 많이 필요로 하기 때문에 병렬 시뮬레이션 환경의 수입니다. 이를 위해, 우리는 시뮬레이터와 VLA 학습자를 별도의 컴퓨팅 그룹에 배치하는 이기종 파이프라인을 설계하여, 리소스 경합을 피하고 훈련 안정성을 유지하면서 병렬로 실행되는 시뮬레이션 환경의 수를 극적으로 증가시킬 수 있습니다. 우리는 간단한 보상으로 CLEAR가 이전 방법들을 크게 능가하며, CARLA longest6 v2 및 Bench2Drive의 도전적인 벤치마크에서 새로운 최첨단 성능을 달성함을 보여줍니다.

## 핵심 내용
엔드투엔드 자율주행(E2E-AD)은 원시 센서 정보를 주행 동작에 직접 매핑하는 것을 목표로 합니다. 최근 다중 모달 대규모 언어 모델(MLLM)의 급속한 발전과 함께 연구자들은 E2E-AD를 위한 Vision-Language-Action(VLA) 모델 패러다임을 제안했으며, 이는 시각적 인식, 언어 이해 및 행동 예측을 단일 정책 내에 통합하고자 합니다. 그러나 기존 VLA 기반 정책은 대부분 모방 학습을 채택하여, 기록된 전문가 궤적에 대한 거리 기반 메트릭을 최적화함으로써 주행을 학습합니다. 이러한 개방 루프 학습과 폐쇄 루프 추론 간의 분포 변화는 폐쇄 루프 계획에서 최적 이하의 성능을 초래합니다. 이러한 격차를 해소하기 위해, 우리는 E2E-AD를 위한 대규모 강화 학습(RL)을 사용한 폐쇄 루프 학습을 가능하게 하는 시스템인 CLEAR를 제시합니다. 우리는 사전 훈련된 VLA 정책의 웨이포인트 사전 정보를 기반으로 새로운 잔차 웨이포인트 정책을 학습하여, 내부 지식을 효과적으로 활용할 것을 제안합니다. 다른 측면에서, 시각 기반 정책을 위한 RL을 확장하는 주요 과제 중 하나는 RL이 데이터를 많이 필요로 하기 때문에 병렬 시뮬레이션 환경의 수입니다. 이를 위해, 우리는 시뮬레이터와 VLA 학습자를 별도의 컴퓨팅 그룹에 배치하는 이기종 파이프라인을 설계하여, 리소스 경합을 피하고 훈련 안정성을 유지하면서 병렬로 실행되는 시뮬레이션 환경의 수를 극적으로 증가시킬 수 있습니다. 우리는 간단한 보상으로 CLEAR가 이전 방법들을 크게 능가하며, CARLA longest6 v2 및 Bench2Drive의 도전적인 벤치마크에서 새로운 최첨단 성능을 달성함을 보여줍니다.
