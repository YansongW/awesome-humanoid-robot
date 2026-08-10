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
  zh: Tactile Genesis 是一个由 NeuroAgents Lab 开发的 GPU 并行触觉传感器仿真平台，首次在机器人学习物理仿真中引入体素化温度场。该平台支持多种触觉抽象（如接触深度、力/力矩、音频等），可在单 GPU 上扩展至超过
    20,000 个并行环境和 1,000 个触觉单元，吞吐量较以往仿真器提升 3 至 20 倍。通过三个灵巧操作任务的教师-学生策略训练，研究发现传感器放置位置比类型更重要，而每触觉单元的力/力矩是最有效的传感器类型。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.22332v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (980 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Tactile Genesis: Exploring Tactile Sensors at Scale for Learning Dexterous Tasks (arXiv)'
  url: https://arxiv.org/abs/2606.22332
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述
Tactile Genesis 解决了触觉传感器在灵巧操作研究中难以跨传感器类型进行公平比较的问题。该平台在统一接口下提供二进制接触、接触深度、每触觉单元运动学力/力矩、弹性体标记位移、几何感知接近度、接触音频以及体素化温度场（机器人学习物理仿真平台首创），并支持可配置的放置位置、分辨率和真实噪声模型（漂移、迟滞、死触觉单元、串扰）。在单 GPU 上，它可并行运行超过 20,000 个环境和 1,000 个触觉单元，吞吐量比以往触觉仿真器提高 3 到 20 倍。通过在三个灵巧操作任务上训练教师-学生策略，并消融传感器类型、放置位置、分辨率和噪声，研究验证了向真实 XHand1 的迁移效果。

## 核心内容
### 核心贡献
Tactile Genesis 是一个 GPU 并行触觉传感器仿真平台，旨在系统研究不同触觉抽象对灵巧操作策略的影响。其关键创新包括：
- **统一接口**：支持二进制接触、接触深度、每触觉单元运动学力/力矩、弹性体标记位移、几何感知接近度、接触音频和体素化温度场（机器人学习物理仿真平台首创）。
- **可配置性**：传感器放置位置、分辨率可调，并集成真实噪声模型（漂移、迟滞、死触觉单元、串扰）。
- **高性能**：单 GPU 上可扩展至超过 20,000 个并行环境和 1,000 个触觉单元，吞吐量较以往触觉仿真器提升 3 至 20 倍。

### 实验设置
- **任务**：三个灵巧操作任务，使用教师-学生策略训练。
- **硬件**：策略迁移至真实 XHand1 进行验证。
- **消融实验**：系统消融传感器类型、放置位置、分辨率和噪声。

### 关键发现
- **本体感觉不足**：在所有任务中，仅依赖本体感觉均无法完成任务。
- **放置位置主导类型**：仅指尖覆盖的性能远低于全手覆盖；添加手掌和近端指节后，性能接近特权教师策略。
- **分辨率不如覆盖范围重要**：全手放置 200 个触觉单元即可满足所有任务需求。
- **最佳传感器类型**：每触觉单元的力/力矩在所有任务中表现最稳定。

### 结论
这些结果为未来灵巧操作中触觉硬件设计和策略观测选择提供了具体指导。项目页面：https://neuroagents-lab.github.io/tactile-genesis/

## Overview
Tactile sensing is critical for contact-rich dexterous manipulation, yet it remains unclear which tactile abstractions a policy needs and when richer tactile fields justify their hardware cost. This is hard to study empirically: each sensor effectively defines a new robot, and no lab can replicate the same learning experiment across all of them. We present Tactile Genesis, a GPU-parallel tactile sensor simulation platform that exposes binary contact, contact depth, per-taxel kinematic force/torque, elastomer marker displacement, geometry-aware proximity, contact audio, and a voxelized temperature field (the first of its kind in robot learning physics simulation platforms) under a common interface, with configurable placement, resolution, and a realistic noise model (drift, hysteresis, dead taxels, crosstalk). It scales past 20,000 parallel environments and 1,000 taxels on a single GPU, improving throughput by 3 to 20 times over previous tactile simulators. We train teacher-student policies on three dexterous tasks, ablating sensor type, placement, resolution, and noise, and verify transfer to the real XHand1. Proprioception alone is insufficient on every task. Sensor placement dominates sensor type: fingertip-only coverage trails whole-hand coverage by a wide margin, while adding the palm and proximal phalanges closes most of the gap to the privileged teacher. Resolution matters far less than coverage: placing 200 taxels across the whole hand suffices across tasks. We find that force/torque per taxel is consistently the most useful sensor type. These results give concrete guidance for both future tactile hardware design for improving robot hands and policy-side observation choice in dexterous manipulation. https://neuroagents-lab.github.io/tactile-genesis/

## 参考
- http://arxiv.org/abs/2606.22332v2

## 개요
Tactile Genesis는 촉각 센서가 정밀 조작 연구에서 센서 유형 간 공정한 비교가 어려운 문제를 해결합니다. 이 플랫폼은 통합 인터페이스 아래에서 이진 접촉, 접촉 깊이, 촉각 유닛별 운동학적 힘/토크, 엘라스토머 마커 변위, 기하학적 인식 근접도, 접촉 오디오, 그리고 복셀화된 온도장(로봇 학습 물리 시뮬레이션 플랫폼 최초)을 지원하며, 구성 가능한 배치 위치, 해상도, 실제 노이즈 모델(드리프트, 히스테리시스, 죽은 촉각 유닛, 크로스토크)을 제공합니다. 단일 GPU에서 20,000개 이상의 환경과 1,000개의 촉각 유닛을 병렬로 실행할 수 있으며, 처리량은 기존 촉각 시뮬레이터보다 3~20배 향상됩니다. 세 가지 정밀 조작 작업에서 교사-학생 정책을 훈련하고 센서 유형, 배치 위치, 해상도, 노이즈를 절제 실험함으로써 실제 XHand1로의 전이 효과를 검증했습니다.

## 핵심 내용
### 핵심 기여
Tactile Genesis는 서로 다른 촉각 추상화가 정밀 조작 정책에 미치는 영향을 체계적으로 연구하기 위해 설계된 GPU 병렬 촉각 센서 시뮬레이션 플랫폼입니다. 주요 혁신은 다음과 같습니다:
- **통합 인터페이스**: 이진 접촉, 접촉 깊이, 촉각 유닛별 운동학적 힘/토크, 엘라스토머 마커 변위, 기하학적 인식 근접도, 접촉 오디오, 복셀화된 온도장(로봇 학습 물리 시뮬레이션 플랫폼 최초)을 지원합니다.
- **구성 가능성**: 센서 배치 위치, 해상도를 조정할 수 있으며 실제 노이즈 모델(드리프트, 히스테리시스, 죽은 촉각 유닛, 크로스토크)이 통합되어 있습니다.
- **고성능**: 단일 GPU에서 20,000개 이상의 병렬 환경과 1,000개의 촉각 유닛으로 확장 가능하며, 처리량은 기존 촉각 시뮬레이터보다 3~20배 향상됩니다.

### 실험 설정
- **작업**: 교사-학생 정책 훈련을 사용한 세 가지 정밀 조작 작업.
- **하드웨어**: 정책을 실제 XHand1로 전이하여 검증.
- **절제 실험**: 센서 유형, 배치 위치, 해상도, 노이즈를 체계적으로 절제.

### 주요 발견
- **고유 감각 부족**: 모든 작업에서 고유 감각만으로는 작업을 완료할 수 없습니다.
- **배치 위치가 유형보다 우세**: 손끝만 덮는 성능은 전체 손 덮기보다 훨씬 낮습니다. 손바닥과 근위 지절을 추가하면 특권 교사 정책에 근접한 성능을 보입니다.
- **해상도보다 적용 범위가 중요**: 전체 손에 200개의 촉각 유닛을 배치하면 모든 작업 요구를 충족할 수 있습니다.
- **최적의 센서 유형**: 촉각 유닛별 힘/토크가 모든 작업에서 가장 안정적인 성능을 보입니다.

### 결론
이러한 결과는 향후 정밀 조작에서 촉각 하드웨어 설계와 정책 관측 선택에 대한 구체적인 지침을 제공합니다. 프로젝트 페이지: https://neuroagents-lab.github.io/tactile-genesis/
