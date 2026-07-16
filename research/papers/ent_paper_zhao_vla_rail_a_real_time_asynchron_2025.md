---
$id: ent_paper_zhao_vla_rail_a_real_time_asynchron_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots'
  zh: VLA-RAIL
  ko: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots'
summary:
  en: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots (VLA-RAIL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by China Mobile (Hangzhou) Information Technology Co., Ltd.,.'
  zh: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots (VLA-RAIL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by China Mobile (Hangzhou) Information Technology Co., Ltd.,.'
  ko: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots (VLA-RAIL), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by China Mobile (Hangzhou) Information Technology Co., Ltd.,.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- vision_language_action
- vla
- vla_rail
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24673v1.
sources:
- id: src_001
  type: paper
  title: 'VLA-RAIL: A Real-Time Asynchronous Inference Linker for VLA Models and Robots (arXiv)'
  url: https://arxiv.org/abs/2512.24673
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: VLA-RAIL source
  url: https://doi.org/10.48550/arXiv.2512.24673
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have achieved remarkable breakthroughs in robotics, with the action chunk playing a dominant role in these advances. Given the real-time and continuous nature of robotic motion control, the strategies for fusing a queue of successive action chunks have a profound impact on the overall performance of VLA models. Existing methods suffer from jitter, stalling, or even pauses in robotic action execution, which not only limits the achievable execution speed but also reduces the overall success rate of task completion. This paper introduces VLA-RAIL (A Real-Time Asynchronous Inference Linker), a novel framework designed to address these issues by conducting model inference and robot motion control asynchronously and guaranteeing smooth, continuous, and high-speed action execution. The core contributions of the paper are two fold: a Trajectory Smoother that effectively filters out the noise and jitter in the trajectory of one action chunk using polynomial fitting and a Chunk Fuser that seamlessly align the current executing trajectory and the newly arrived chunk, ensuring position, velocity, and acceleration continuity between two successive action chunks. We validate the effectiveness of VLA-RAIL on a benchmark of dynamic simulation tasks and several real-world manipulation tasks. Experimental results demonstrate that VLA-RAIL significantly reduces motion jitter, enhances execution speed, and improves task success rates, which will become a key infrastructure for the large-scale deployment of VLA models.

## 核心内容
Vision-Language-Action (VLA) models have achieved remarkable breakthroughs in robotics, with the action chunk playing a dominant role in these advances. Given the real-time and continuous nature of robotic motion control, the strategies for fusing a queue of successive action chunks have a profound impact on the overall performance of VLA models. Existing methods suffer from jitter, stalling, or even pauses in robotic action execution, which not only limits the achievable execution speed but also reduces the overall success rate of task completion. This paper introduces VLA-RAIL (A Real-Time Asynchronous Inference Linker), a novel framework designed to address these issues by conducting model inference and robot motion control asynchronously and guaranteeing smooth, continuous, and high-speed action execution. The core contributions of the paper are two fold: a Trajectory Smoother that effectively filters out the noise and jitter in the trajectory of one action chunk using polynomial fitting and a Chunk Fuser that seamlessly align the current executing trajectory and the newly arrived chunk, ensuring position, velocity, and acceleration continuity between two successive action chunks. We validate the effectiveness of VLA-RAIL on a benchmark of dynamic simulation tasks and several real-world manipulation tasks. Experimental results demonstrate that VLA-RAIL significantly reduces motion jitter, enhances execution speed, and improves task success rates, which will become a key infrastructure for the large-scale deployment of VLA models.

## 参考
- http://arxiv.org/abs/2512.24673v1

## Overview
Vision-Language-Action (VLA) models have achieved remarkable breakthroughs in robotics, with the action chunk playing a dominant role in these advances. Given the real-time and continuous nature of robotic motion control, the strategies for fusing a queue of successive action chunks have a profound impact on the overall performance of VLA models. Existing methods suffer from jitter, stalling, or even pauses in robotic action execution, which not only limits the achievable execution speed but also reduces the overall success rate of task completion. This paper introduces VLA-RAIL (A Real-Time Asynchronous Inference Linker), a novel framework designed to address these issues by conducting model inference and robot motion control asynchronously and guaranteeing smooth, continuous, and high-speed action execution. The core contributions of the paper are two fold: a Trajectory Smoother that effectively filters out the noise and jitter in the trajectory of one action chunk using polynomial fitting and a Chunk Fuser that seamlessly align the current executing trajectory and the newly arrived chunk, ensuring position, velocity, and acceleration continuity between two successive action chunks. We validate the effectiveness of VLA-RAIL on a benchmark of dynamic simulation tasks and several real-world manipulation tasks. Experimental results demonstrate that VLA-RAIL significantly reduces motion jitter, enhances execution speed, and improves task success rates, which will become a key infrastructure for the large-scale deployment of VLA models.

## Content
Vision-Language-Action (VLA) models have achieved remarkable breakthroughs in robotics, with the action chunk playing a dominant role in these advances. Given the real-time and continuous nature of robotic motion control, the strategies for fusing a queue of successive action chunks have a profound impact on the overall performance of VLA models. Existing methods suffer from jitter, stalling, or even pauses in robotic action execution, which not only limits the achievable execution speed but also reduces the overall success rate of task completion. This paper introduces VLA-RAIL (A Real-Time Asynchronous Inference Linker), a novel framework designed to address these issues by conducting model inference and robot motion control asynchronously and guaranteeing smooth, continuous, and high-speed action execution. The core contributions of the paper are two fold: a Trajectory Smoother that effectively filters out the noise and jitter in the trajectory of one action chunk using polynomial fitting and a Chunk Fuser that seamlessly align the current executing trajectory and the newly arrived chunk, ensuring position, velocity, and acceleration continuity between two successive action chunks. We validate the effectiveness of VLA-RAIL on a benchmark of dynamic simulation tasks and several real-world manipulation tasks. Experimental results demonstrate that VLA-RAIL significantly reduces motion jitter, enhances execution speed, and improves task success rates, which will become a key infrastructure for the large-scale deployment of VLA models.

## 개요
Vision-Language-Action (VLA) 모델은 로봇 공학에서 놀라운 돌파구를 이루었으며, 액션 청크(action chunk)가 이러한 발전에서 지배적인 역할을 하고 있습니다. 로봇 모션 제어의 실시간 및 연속적 특성을 고려할 때, 연속적인 액션 청크 큐를 융합하는 전략은 VLA 모델의 전반적인 성능에 깊은 영향을 미칩니다. 기존 방법은 로봇 동작 실행에서 지터(jitter), 지연(stalling), 또는 일시 중지(pause)를 겪으며, 이는 달성 가능한 실행 속도를 제한할 뿐만 아니라 작업 완료의 전체 성공률을 낮춥니다. 본 논문은 VLA-RAIL (A Real-Time Asynchronous Inference Linker)을 소개합니다. 이는 모델 추론과 로봇 모션 제어를 비동기적으로 수행하고 부드럽고 연속적이며 고속의 동작 실행을 보장함으로써 이러한 문제를 해결하도록 설계된 새로운 프레임워크입니다. 논문의 핵심 기여는 두 가지입니다: 다항식 피팅(polynomial fitting)을 사용하여 하나의 액션 청크 궤적에서 노이즈와 지터를 효과적으로 필터링하는 궤적 평활화기(Trajectory Smoother)와, 현재 실행 중인 궤적과 새로 도착한 청크를 원활하게 정렬하여 연속적인 두 액션 청크 간의 위치, 속도 및 가속도 연속성을 보장하는 청크 퓨저(Chunk Fuser)입니다. 우리는 동적 시뮬레이션 작업 벤치마크와 여러 실제 조작 작업에서 VLA-RAIL의 효과성을 검증합니다. 실험 결과는 VLA-RAIL이 모션 지터를 크게 줄이고 실행 속도를 향상시키며 작업 성공률을 개선하여, VLA 모델의 대규모 배포를 위한 핵심 인프라가 될 것임을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇 공학에서 놀라운 돌파구를 이루었으며, 액션 청크(action chunk)가 이러한 발전에서 지배적인 역할을 하고 있습니다. 로봇 모션 제어의 실시간 및 연속적 특성을 고려할 때, 연속적인 액션 청크 큐를 융합하는 전략은 VLA 모델의 전반적인 성능에 깊은 영향을 미칩니다. 기존 방법은 로봇 동작 실행에서 지터(jitter), 지연(stalling), 또는 일시 중지(pause)를 겪으며, 이는 달성 가능한 실행 속도를 제한할 뿐만 아니라 작업 완료의 전체 성공률을 낮춥니다. 본 논문은 VLA-RAIL (A Real-Time Asynchronous Inference Linker)을 소개합니다. 이는 모델 추론과 로봇 모션 제어를 비동기적으로 수행하고 부드럽고 연속적이며 고속의 동작 실행을 보장함으로써 이러한 문제를 해결하도록 설계된 새로운 프레임워크입니다. 논문의 핵심 기여는 두 가지입니다: 다항식 피팅(polynomial fitting)을 사용하여 하나의 액션 청크 궤적에서 노이즈와 지터를 효과적으로 필터링하는 궤적 평활화기(Trajectory Smoother)와, 현재 실행 중인 궤적과 새로 도착한 청크를 원활하게 정렬하여 연속적인 두 액션 청크 간의 위치, 속도 및 가속도 연속성을 보장하는 청크 퓨저(Chunk Fuser)입니다. 우리는 동적 시뮬레이션 작업 벤치마크와 여러 실제 조작 작업에서 VLA-RAIL의 효과성을 검증합니다. 실험 결과는 VLA-RAIL이 모션 지터를 크게 줄이고 실행 속도를 향상시키며 작업 성공률을 개선하여, VLA 모델의 대규모 배포를 위한 핵심 인프라가 될 것임을 보여줍니다.
