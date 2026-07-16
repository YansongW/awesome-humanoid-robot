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
  zh: 本文介绍了一种定制准直驱执行器和一个3.4公斤的双侧髋关节外骨骼，实现了17.5牛·米额定扭矩、0.4牛·米反驱扭矩、62.4赫兹带宽，并在行走和蹲起中验证了简单的控制器。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2004.00467v1.
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
High-performance actuators are crucial to enable mechanical versatility of lower-limb wearable robots, which are required to be lightweight, highly backdrivable, and with high bandwidth. State-of-the-art actuators, e.g., series elastic actuators (SEAs), have to compromise bandwidth to improve compliance (i.e., backdrivability). In this paper, we describe the design and human-robot interaction modeling of a portable hip exoskeleton based on our custom quasi-direct drive (QDD) actuation (i.e., a high torque density motor with low ratio gear). We also present a model-based performance benchmark comparison of representative actuators in terms of torque capability, control bandwidth, backdrivability, and force tracking accuracy. This paper aims to corroborate the underlying philosophy of "design for control", namely meticulous robot design can simplify control algorithms while ensuring high performance. Following this idea, we create a lightweight bilateral hip exoskeleton (overall mass is 3.4 kg) to reduce joint loadings during normal activities, including walking and squatting. Experimental results indicate that the exoskeleton is able to produce high nominal torque (17.5 Nm), high backdrivability (0.4 Nm backdrive torque), high bandwidth (62.4 Hz), and high control accuracy (1.09 Nm root mean square tracking error, i.e., 5.4% of the desired peak torque). Its controller is versatile to assist walking at different speeds (0.8-1.4 m/s) and squatting at 2 s cadence. This work demonstrates significant improvement in backdrivability and control bandwidth compared with state-of-the-art exoskeletons powered by the conventional actuation or SEA.

## 核心内容
High-performance actuators are crucial to enable mechanical versatility of lower-limb wearable robots, which are required to be lightweight, highly backdrivable, and with high bandwidth. State-of-the-art actuators, e.g., series elastic actuators (SEAs), have to compromise bandwidth to improve compliance (i.e., backdrivability). In this paper, we describe the design and human-robot interaction modeling of a portable hip exoskeleton based on our custom quasi-direct drive (QDD) actuation (i.e., a high torque density motor with low ratio gear). We also present a model-based performance benchmark comparison of representative actuators in terms of torque capability, control bandwidth, backdrivability, and force tracking accuracy. This paper aims to corroborate the underlying philosophy of "design for control", namely meticulous robot design can simplify control algorithms while ensuring high performance. Following this idea, we create a lightweight bilateral hip exoskeleton (overall mass is 3.4 kg) to reduce joint loadings during normal activities, including walking and squatting. Experimental results indicate that the exoskeleton is able to produce high nominal torque (17.5 Nm), high backdrivability (0.4 Nm backdrive torque), high bandwidth (62.4 Hz), and high control accuracy (1.09 Nm root mean square tracking error, i.e., 5.4% of the desired peak torque). Its controller is versatile to assist walking at different speeds (0.8-1.4 m/s) and squatting at 2 s cadence. This work demonstrates significant improvement in backdrivability and control bandwidth compared with state-of-the-art exoskeletons powered by the conventional actuation or SEA.

## 参考
- http://arxiv.org/abs/2004.00467v1

## Overview
High-performance actuators are crucial to enable mechanical versatility of lower-limb wearable robots, which are required to be lightweight, highly backdrivable, and with high bandwidth. State-of-the-art actuators, e.g., series elastic actuators (SEAs), have to compromise bandwidth to improve compliance (i.e., backdrivability). In this paper, we describe the design and human-robot interaction modeling of a portable hip exoskeleton based on our custom quasi-direct drive (QDD) actuation (i.e., a high torque density motor with low ratio gear). We also present a model-based performance benchmark comparison of representative actuators in terms of torque capability, control bandwidth, backdrivability, and force tracking accuracy. This paper aims to corroborate the underlying philosophy of "design for control", namely meticulous robot design can simplify control algorithms while ensuring high performance. Following this idea, we create a lightweight bilateral hip exoskeleton (overall mass is 3.4 kg) to reduce joint loadings during normal activities, including walking and squatting. Experimental results indicate that the exoskeleton is able to produce high nominal torque (17.5 Nm), high backdrivability (0.4 Nm backdrive torque), high bandwidth (62.4 Hz), and high control accuracy (1.09 Nm root mean square tracking error, i.e., 5.4% of the desired peak torque). Its controller is versatile to assist walking at different speeds (0.8-1.4 m/s) and squatting at 2 s cadence. This work demonstrates significant improvement in backdrivability and control bandwidth compared with state-of-the-art exoskeletons powered by the conventional actuation or SEA.

## Content
High-performance actuators are crucial to enable mechanical versatility of lower-limb wearable robots, which are required to be lightweight, highly backdrivable, and with high bandwidth. State-of-the-art actuators, e.g., series elastic actuators (SEAs), have to compromise bandwidth to improve compliance (i.e., backdrivability). In this paper, we describe the design and human-robot interaction modeling of a portable hip exoskeleton based on our custom quasi-direct drive (QDD) actuation (i.e., a high torque density motor with low ratio gear). We also present a model-based performance benchmark comparison of representative actuators in terms of torque capability, control bandwidth, backdrivability, and force tracking accuracy. This paper aims to corroborate the underlying philosophy of "design for control", namely meticulous robot design can simplify control algorithms while ensuring high performance. Following this idea, we create a lightweight bilateral hip exoskeleton (overall mass is 3.4 kg) to reduce joint loadings during normal activities, including walking and squatting. Experimental results indicate that the exoskeleton is able to produce high nominal torque (17.5 Nm), high backdrivability (0.4 Nm backdrive torque), high bandwidth (62.4 Hz), and high control accuracy (1.09 Nm root mean square tracking error, i.e., 5.4% of the desired peak torque). Its controller is versatile to assist walking at different speeds (0.8-1.4 m/s) and squatting at 2 s cadence. This work demonstrates significant improvement in backdrivability and control bandwidth compared with state-of-the-art exoskeletons powered by the conventional actuation or SEA.

## 개요
고성능 액추에이터는 하지 착용 로봇의 기계적 다용성을 가능하게 하는 데 필수적이며, 이는 경량, 높은 역구동성, 높은 대역폭을 요구합니다. 최신 액추에이터, 예를 들어 직렬 탄성 액추에이터(SEA)는 순응성(즉, 역구동성)을 개선하기 위해 대역폭을 희생해야 합니다. 본 논문에서는 맞춤형 준직접 구동(QDD) 액추에이션(즉, 저비율 기어를 갖춘 고토크 밀도 모터)을 기반으로 한 휴대용 고관절 외골격의 설계와 인간-로봇 상호작용 모델링을 설명합니다. 또한 토크 성능, 제어 대역폭, 역구동성, 힘 추적 정확도 측면에서 대표적인 액추에이터의 모델 기반 성능 벤치마크 비교를 제시합니다. 이 논문은 "제어를 위한 설계"라는 기본 철학을 입증하는 것을 목표로 하며, 즉 세심한 로봇 설계가 높은 성능을 보장하면서 제어 알고리즘을 단순화할 수 있음을 보여줍니다. 이 아이디어에 따라, 우리는 걷기와 스쿼트를 포함한 일상 활동 중 관절 부하를 줄이기 위해 경량 양측 고관절 외골격(총 질량 3.4 kg)을 제작했습니다. 실험 결과는 외골격이 높은 공칭 토크(17.5 Nm), 높은 역구동성(0.4 Nm 역구동 토크), 높은 대역폭(62.4 Hz), 높은 제어 정확도(1.09 Nm 평균 제곱근 추적 오차, 즉 목표 최대 토크의 5.4%)를 생성할 수 있음을 보여줍니다. 제어기는 다양한 속도(0.8-1.4 m/s)에서의 걷기와 2초 주기의 스쿼트를 지원하는 데 다용도로 사용됩니다. 이 연구는 기존 액추에이션 또는 SEA로 구동되는 최신 외골격과 비교하여 역구동성과 제어 대역폭에서 상당한 개선을 입증합니다.

## 핵심 내용
고성능 액추에이터는 하지 착용 로봇의 기계적 다용성을 가능하게 하는 데 필수적이며, 이는 경량, 높은 역구동성, 높은 대역폭을 요구합니다. 최신 액추에이터, 예를 들어 직렬 탄성 액추에이터(SEA)는 순응성(즉, 역구동성)을 개선하기 위해 대역폭을 희생해야 합니다. 본 논문에서는 맞춤형 준직접 구동(QDD) 액추에이션(즉, 저비율 기어를 갖춘 고토크 밀도 모터)을 기반으로 한 휴대용 고관절 외골격의 설계와 인간-로봇 상호작용 모델링을 설명합니다. 또한 토크 성능, 제어 대역폭, 역구동성, 힘 추적 정확도 측면에서 대표적인 액추에이터의 모델 기반 성능 벤치마크 비교를 제시합니다. 이 논문은 "제어를 위한 설계"라는 기본 철학을 입증하는 것을 목표로 하며, 즉 세심한 로봇 설계가 높은 성능을 보장하면서 제어 알고리즘을 단순화할 수 있음을 보여줍니다. 이 아이디어에 따라, 우리는 걷기와 스쿼트를 포함한 일상 활동 중 관절 부하를 줄이기 위해 경량 양측 고관절 외골격(총 질량 3.4 kg)을 제작했습니다. 실험 결과는 외골격이 높은 공칭 토크(17.5 Nm), 높은 역구동성(0.4 Nm 역구동 토크), 높은 대역폭(62.4 Hz), 높은 제어 정확도(1.09 Nm 평균 제곱근 추적 오차, 즉 목표 최대 토크의 5.4%)를 생성할 수 있음을 보여줍니다. 제어기는 다양한 속도(0.8-1.4 m/s)에서의 걷기와 2초 주기의 스쿼트를 지원하는 데 다용도로 사용됩니다. 이 연구는 기존 액추에이션 또는 SEA로 구동되는 최신 외골격과 비교하여 역구동성과 제어 대역폭에서 상당한 개선을 입증합니다.
