---
$id: ent_paper_tactile_genesis_exploring_tact_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks'
  zh: 'Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks'
  ko: 'Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks'
summary:
  en: 'arXiv:2606.22332v2 Announce Type: replace Abstract: Tactile sensing is critical for contact-rich dexterous manipulation,
    yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware
    cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same
    learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform
    that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware
    proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation
    platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis,
    dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput
    by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating
    sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient
    on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin,
    while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far
    less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel
    is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design
    for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/'
  zh: 'arXiv:2606.22332v2 Announce Type: replace Abstract: Tactile sensing is critical for contact-rich dexterous manipulation,
    yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware
    cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same
    learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform
    that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware
    proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation
    platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis,
    dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput
    by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating
    sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient
    on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin,
    while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far
    less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel
    is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design
    for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/'
  ko: 'arXiv:2606.22332v2 Announce Type: replace Abstract: Tactile sensing is critical for contact-rich dexterous manipulation,
    yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware
    cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same
    learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform
    that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware
    proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation
    platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis,
    dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput
    by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating
    sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient
    on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin,
    while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far
    less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel
    is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design
    for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/'
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
- tactile_genesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.22332v2.
sources:
- id: src_001
  type: paper
  title: 'Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks (arXiv)'
  url: https://arxiv.org/abs/2606.22332
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Tactile sensing is critical for contact-rich dexterous manipulation, yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin, while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/

## 核心内容
Tactile sensing is critical for contact-rich dexterous manipulation, yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin, while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/

## 参考
- http://arxiv.org/abs/2606.22332v2

## Overview
Tactile sensing is critical for contact-rich dexterous manipulation, yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin, while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/

## Content
Tactile sensing is critical for contact-rich dexterous manipulation, yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin, while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/

## 개요
촉각 감지는 접촉이 많은 정밀 조작에 필수적이지만, 정책이 어떤 촉각 추상화를 필요로 하는지, 그리고 언제 더 풍부한 촉각 필드가 하드웨어 비용을 정당화하는지는 여전히 불분명합니다. 이를 실증적으로 연구하기는 어렵습니다. 각 센서는 사실상 새로운 로봇을 정의하며, 어떤 연구실도 모든 센서에 걸쳐 동일한 학습 실험을 재현할 수 없기 때문입니다. 우리는 Tactile Genesis를 제시합니다. 이는 GPU 병렬 촉각 센서 시뮬레이션 플랫폼으로, 공통 인터페이스 아래에서 이진 접촉, 접촉 깊이, 택셀당 운동학적 힘/토크, 엘라스토머 마커 변위, 형상 인식 근접 감지, 접촉 오디오, 그리고 복셀화된 온도 필드(로봇 학습 물리 시뮬레이션 플랫폼 중 최초)를 제공하며, 구성 가능한 배치, 해상도 및 현실적인 노이즈 모델(드리프트, 히스테리시스, 데드 택셀, 크로스토크)을 갖추고 있습니다. 이 플랫폼은 단일 GPU에서 20,000개 이상의 병렬 환경과 1,000개 이상의 택셀로 확장 가능하며, 이전 촉각 시뮬레이터 대비 처리량을 3~20배 향상시킵니다. 우리는 세 가지 정밀 조작 작업에서 교사-학생 정책을 훈련하고, 센서 유형, 배치, 해상도 및 노이즈를 제거(ablation)하며, 실제 XHand1로의 전이를 검증합니다. 고유 감각(proprioception)만으로는 모든 작업에 불충분합니다. 센서 배치가 센서 유형보다 우세합니다. 손끝만 커버하는 것은 전체 손 커버리지에 비해 크게 뒤처지며, 손바닥과 근위 지골을 추가하면 특권 교사(privileged teacher)와의 격차를 대부분 좁힙니다. 해상도는 커버리지보다 훨씬 덜 중요합니다. 전체 손에 200개의 택셀을 배치하는 것으로 작업 전반에 충분합니다. 우리는 택셀당 힘/토크가 일관되게 가장 유용한 센서 유형임을 발견했습니다. 이러한 결과는 로봇 손 개선을 위한 미래 촉각 하드웨어 설계와 정밀 조작에서 정책 측 관찰 선택 모두에 구체적인 지침을 제공합니다. https://neuroagents-lab.github.io/tactile-genesis/

## 핵심 내용
촉각 감지는 접촉이 많은 정밀 조작에 필수적이지만, 정책이 어떤 촉각 추상화를 필요로 하는지, 그리고 언제 더 풍부한 촉각 필드가 하드웨어 비용을 정당화하는지는 여전히 불분명합니다. 이를 실증적으로 연구하기는 어렵습니다. 각 센서는 사실상 새로운 로봇을 정의하며, 어떤 연구실도 모든 센서에 걸쳐 동일한 학습 실험을 재현할 수 없기 때문입니다. 우리는 Tactile Genesis를 제시합니다. 이는 GPU 병렬 촉각 센서 시뮬레이션 플랫폼으로, 공통 인터페이스 아래에서 이진 접촉, 접촉 깊이, 택셀당 운동학적 힘/토크, 엘라스토머 마커 변위, 형상 인식 근접 감지, 접촉 오디오, 그리고 복셀화된 온도 필드(로봇 학습 물리 시뮬레이션 플랫폼 중 최초)를 제공하며, 구성 가능한 배치, 해상도 및 현실적인 노이즈 모델(드리프트, 히스테리시스, 데드 택셀, 크로스토크)을 갖추고 있습니다. 이 플랫폼은 단일 GPU에서 20,000개 이상의 병렬 환경과 1,000개 이상의 택셀로 확장 가능하며, 이전 촉각 시뮬레이터 대비 처리량을 3~20배 향상시킵니다. 우리는 세 가지 정밀 조작 작업에서 교사-학생 정책을 훈련하고, 센서 유형, 배치, 해상도 및 노이즈를 제거(ablation)하며, 실제 XHand1로의 전이를 검증합니다. 고유 감각(proprioception)만으로는 모든 작업에 불충분합니다. 센서 배치가 센서 유형보다 우세합니다. 손끝만 커버하는 것은 전체 손 커버리지에 비해 크게 뒤처지며, 손바닥과 근위 지골을 추가하면 특권 교사(privileged teacher)와의 격차를 대부분 좁힙니다. 해상도는 커버리지보다 훨씬 덜 중요합니다. 전체 손에 200개의 택셀을 배치하는 것으로 작업 전반에 충분합니다. 우리는 택셀당 힘/토크가 일관되게 가장 유용한 센서 유형임을 발견했습니다. 이러한 결과는 로봇 손 개선을 위한 미래 촉각 하드웨어 설계와 정밀 조작에서 정책 측 관찰 선택 모두에 구체적인 지침을 제공합니다. https://neuroagents-lab.github.io/tactile-genesis/
