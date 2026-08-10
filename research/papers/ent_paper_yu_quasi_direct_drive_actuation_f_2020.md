---
$id: ent_paper_yu_quasi_direct_drive_actuation_f_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Quasi-Direct Drive Actuation for a Lightweight Hip Exoskeleton with High Backdrivability and High Bandwidth
  zh: 用于高反驱性和高带宽轻量化髋关节外骨骼的准直驱驱动
  ko: 높은 역구동성 및 높은 대역폭을 가진 경량 고관절 외골격용 준직구동 구동
summary:
  en: This paper presents a custom quasi-direct-drive actuator and a 3.4 kg bilateral hip exoskeleton that achieves 17.5 Nm
    nominal torque, 0.4 Nm backdrive torque, 62.4 Hz bandwidth, and a simple controller validated during walking and squatting.
  zh: 本文提出一种基于定制准直驱（QDD）执行器的轻量级双侧髋部外骨骼，总重3.4 kg，可实现17.5 Nm额定扭矩、0.4 Nm反向驱动扭矩及62.4 Hz带宽。该设计通过“设计即控制”理念简化了控制器，并在行走（0.8-1.4 m/s）和深蹲（2秒节奏）任务中验证了性能，扭矩跟踪误差仅1.09
    Nm（峰值扭矩的5.4%）。
  ko: 본 논문은 맞춤형 준직구동 구동기와 17.5 Nm 정격 토크, 0.4 Nm 역구동 토크, 62.4 Hz 대역폭을 달성하고 보행 및 스쿼팅에서 간단한 제어기를 검증한 3.4 kg 양측 고관절 외골격을 제시한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- component
tags:
- quasi_direct_drive
- qdd
- hip_exoskeleton
- wearable_robot
- actuator
- backdrivability
- high_bandwidth
- bldc_motor
- planetary_gearbox
- design_for_control
- lower_limb_assist
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2004.00467v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (819 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Quasi-Direct Drive Actuation for a Lightweight Hip Exoskeleton with High Backdrivability and High Bandwidth
  url: https://arxiv.org/abs/2004.00467
  date: '2020'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
该研究针对下肢可穿戴机器人对执行器轻量化、高反向驱动性与高带宽的需求，提出一种定制准直驱（QDD）执行器，并基于此构建了3.4 kg双侧髋部外骨骼。与传统串联弹性执行器（SEA）需在带宽与柔顺性间权衡不同，QDD通过高扭矩密度电机与低减速比齿轮实现性能突破。实验表明，该外骨骼在行走和深蹲任务中展现出17.5 Nm额定扭矩、0.4 Nm反向驱动扭矩及62.4 Hz带宽，扭矩跟踪误差仅1.09 Nm（峰值扭矩的5.4%），且控制器可适应不同速度的行走与深蹲节奏。

## 核心内容
### 核心设计理念
- **“设计即控制”哲学**：通过精密机械设计简化控制算法，避免复杂补偿策略。
- **准直驱（QDD）执行器**：采用高扭矩密度电机+低减速比齿轮，在保持高反向驱动性的同时提升带宽。

### 系统架构
- **外骨骼本体**：双侧髋部结构，总重3.4 kg，包含定制QDD执行器、轻量化框架及绑带。
- **执行器参数**：
  - 额定扭矩：17.5 Nm
  - 反向驱动扭矩：0.4 Nm（衡量被动柔顺性）
  - 控制带宽：62.4 Hz（远高于典型SEA的10-30 Hz）

### 实验验证
- **任务场景**：
  - 行走速度范围：0.8-1.4 m/s
  - 深蹲节奏：2秒/次
- **性能指标**：
  - 扭矩跟踪误差：1.09 Nm（均方根值），占峰值扭矩的5.4%
  - 控制器无需复杂力/阻抗调节，仅依赖低增益反馈

### 对比优势
- 与现有SEA外骨骼相比，反向驱动性提升约10倍（0.4 Nm vs 3-5 Nm），带宽提升2-6倍。
- 在保持高扭矩输出的同时，避免了SEA因弹性元件导致的相位滞后问题。

### 结论
该工作验证了QDD执行器在轻量化外骨骼中的可行性，为下肢辅助机器人提供了高反向驱动性与高带宽的实用方案，且控制器设计简洁，易于扩展至其他运动模式。

## Overview
High-performance actuators are crucial to enable mechanical versatility of lower-limb wearable robots, which are required to be lightweight, highly backdrivable, and with high bandwidth. State-of-the-art actuators, e.g., series elastic actuators (SEAs), have to compromise bandwidth to improve compliance (i.e., backdrivability). In this paper, we describe the design and human-robot interaction modeling of a portable hip exoskeleton based on our custom quasi-direct drive (QDD) actuation (i.e., a high torque density motor with low ratio gear). We also present a model-based performance benchmark comparison of representative actuators in terms of torque capability, control bandwidth, backdrivability, and force tracking accuracy. This paper aims to corroborate the underlying philosophy of "design for control", namely meticulous robot design can simplify control algorithms while ensuring high performance. Following this idea, we create a lightweight bilateral hip exoskeleton (overall mass is 3.4 kg) to reduce joint loadings during normal activities, including walking and squatting. Experimental results indicate that the exoskeleton is able to produce high nominal torque (17.5 Nm), high backdrivability (0.4 Nm backdrive torque), high bandwidth (62.4 Hz), and high control accuracy (1.09 Nm root mean square tracking error, i.e., 5.4% of the desired peak torque). Its controller is versatile to assist walking at different speeds (0.8-1.4 m/s) and squatting at 2 s cadence. This work demonstrates significant improvement in backdrivability and control bandwidth compared with state-of-the-art exoskeletons powered by the conventional actuation or SEA.

## 参考
- http://arxiv.org/abs/2004.00467v1

## 개요
이 연구는 하지 웨어러블 로봇의 액추에이터 경량화, 높은 역구동성 및 높은 대역폭 요구를 충족하기 위해 맞춤형 준직접구동(QDD) 액추에이터를 제안하고, 이를 기반으로 3.4 kg 양측 고관절 외골격을 구축했습니다. 기존의 직렬 탄성 액추에이터(SEA)가 대역폭과 유연성 사이에서 절충해야 했던 것과 달리, QDD는 고토크 밀도 모터와 저감속비 기어를 통해 성능 돌파구를 달성했습니다. 실험 결과, 이 외골격은 보행 및 스쿼트 작업에서 17.5 Nm 정격 토크, 0.4 Nm 역구동 토크 및 62.4 Hz 대역폭을 보여주었으며, 토크 추적 오차는 1.09 Nm(최대 토크의 5.4%)에 불과했고, 컨트롤러는 다양한 속도의 보행 및 스쿼트 리듬에 적응할 수 있었습니다.

## 핵심 내용
### 핵심 설계 철학
- **"설계가 곧 제어" 철학**: 정밀 기계 설계를 통해 제어 알고리즘을 단순화하고 복잡한 보상 전략을 피합니다.
- **준직접구동(QDD) 액추에이터**: 고토크 밀도 모터와 저감속비 기어를 채택하여 높은 역구동성을 유지하면서 대역폭을 향상시킵니다.

### 시스템 아키텍처
- **외골격 본체**: 양측 고관절 구조, 총 중량 3.4 kg, 맞춤형 QDD 액추에이터, 경량 프레임 및 스트랩 포함.
- **액추에이터 파라미터**:
  - 정격 토크: 17.5 Nm
  - 역구동 토크: 0.4 Nm(수동 유연성 측정)
  - 제어 대역폭: 62.4 Hz(일반적인 SEA의 10-30 Hz보다 훨씬 높음)

### 실험 검증
- **작업 시나리오**:
  - 보행 속도 범위: 0.8-1.4 m/s
  - 스쿼트 리듬: 2초/회
- **성능 지표**:
  - 토크 추적 오차: 1.09 Nm(제곱평균제곱근), 최대 토크의 5.4% 차지
  - 컨트롤러는 복잡한 힘/임피던스 조정 없이 저이득 피드백만 의존

### 비교 우위
- 기존 SEA 외골격과 비교하여 역구동성이 약 10배 향상(0.4 Nm vs 3-5 Nm), 대역폭은 2-6배 향상.
- 높은 토크 출력을 유지하면서 SEA의 탄성 요소로 인한 위상 지연 문제를 피함.

### 결론
이 연구는 QDD 액추에이터가 경량 외골격에서의 실현 가능성을 검증했으며, 하지 보조 로봇에 높은 역구동성과 높은 대역폭을 갖춘 실용적인 솔루션을 제공했습니다. 또한 컨트롤러 설계가 간결하여 다른 운동 모드로 확장하기 쉽습니다.
