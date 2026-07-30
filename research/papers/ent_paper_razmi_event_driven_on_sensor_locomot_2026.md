---
$id: ent_paper_razmi_event_driven_on_sensor_locomot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Event-Driven On-Sensor Locomotion Mode Recognition Using a Shank-Mounted IMU with Embedded Machine Learning for Exoskeleton
    Control
  zh: 基于嵌入式机器学习和胫部惯性测量单元的事件驱动式外骨骼运动模式识别
  ko: 임베디드 머신러닝을 활용한 경골 장착 IMU의 사건 기반 보행 모드 인식 및 외골격 제어
summary:
  en: This paper presents a wearable human activity recognition system that performs real-time locomotion mode recognition
    (stance, level walking, stair ascent) directly on the embedded Machine Learning Core of a shank-mounted LSM6DSV16X IMU,
    enabling interrupt-driven, low-power control of a lower-limb exoskeleton without continuously streaming raw sensor data
    to the host microcontroller.
  zh: 本文提出一种穿戴式人体活动识别系统，直接在佩戴于小腿的LSM6DSV16X IMU嵌入式机器学习核心上实时识别步态模式（站立、平地行走、上楼梯），用于外骨骼的低功耗中断驱动控制，无需持续向主微控制器传输原始传感器数据。
  ko: 본 논문은 경골에 장착된 LSM6DSV16X IMU의 임베디드 머신러닝 코어에서 직접 실시간으로 보행 모드(서기, 평지 보행, 계단 상승)를 인식하여, 원시 센서 데이터를 호스트 마이크로컨트롤러로 지속적으로
    전송하지 않고도 사건 기반의 저전력 하지 외골격 제어를 가능하게 하는 웨어러블 인간 활동 인식 시스템을 제시한다.
domains:
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- intelligence
- component
- knowledge
tags:
- embedded_ml
- imu
- wearable_sensing
- locomotion_mode_recognition
- exoskeleton_control
- low_power
- decision_tree
- on_sensor_inference
- har
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.21418v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Event-Driven On-Sensor Locomotion Mode Recognition Using a Shank-Mounted IMU with Embedded Machine Learning for Exoskeleton
    Control
  url: https://arxiv.org/abs/2602.21418
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该系统由STMicroelectronics的LSM6DSV16X IMU实现，其嵌入式机器学习核心（MLC）直接执行轻量级决策树模型，完成步态模式分类。与传统方案不同，主微控制器仅在IMU触发中断时读取识别结果，其余时间保持低功耗状态。实验聚焦三种代表性步态模式，数据采集自成年受试者，模型通过ST MEMS Studio配置部署，无需编写自定义机器学习代码。这种架构显著降低了计算与通信开销，在区分平地行走与上楼梯时表现出鲁棒性，适用于外骨骼的力矩辅助控制。

## 核心内容
### 方法
- 系统基于STMicroelectronics LSM6DSV16X IMU的嵌入式机器学习核心（MLC），该核心可直接在传感器内部运行预训练的决策树模型。
- 模型通过ST MEMS Studio工具配置，无需在主微控制器上编写自定义机器学习代码，实现轻量化部署。
- 采用中断驱动架构：IMU在检测到运动或新分类结果时触发中断，主微控制器被唤醒后读取MLC输出寄存器，并将识别结果转发至外骨骼控制器。

### 实验设置
- 数据采集自成年受试者，覆盖三种代表性步态模式：站立、平地行走、上楼梯。
- 模型为轻量级决策树，针对传感器级执行优化，确保实时性与低功耗。

### 关键数字与结论
- 系统在传感器端完成推理，主微控制器仅在中断触发时工作，显著降低功耗。
- 相比持续传输原始数据的传统方案，该架构减少计算与通信开销，同时提升区分平地行走与上楼梯的鲁棒性。
- 实验验证了系统在外骨骼力矩辅助控制中的有效性，支持低延迟、低功耗的实时步态识别。

## Overview
This work presents a wearable human activity recognition (HAR) system that performs real-time inference directly inside a shank-mounted inertial measurement unit (IMU) to support low-latency control of a lower-limb exoskeleton. Unlike conventional approaches that continuously stream raw inertial data to a microcontroller for classification, the proposed system executes activity recognition at the sensor level using the embedded Machine Learning Core (MLC) of the STMicroelectronics LSM6DSV16X IMU, allowing the host microcontroller to remain in a low-power state and read only the recognized activity label from IMU registers. While the system generalizes to multiple human activities, this paper focuses on three representative locomotion modes - stance, level walking, and stair ascent - using data collected from adult participants. A lightweight decision-tree model was configured and deployed for on-sensor execution using ST MEMS Studio, enabling continuous operation without custom machine learning code on the microcontroller. During operation, the IMU asserts an interrupt when motion or a new classification is detected; the microcontroller wakes, reads the MLC output registers, and forwards the inferred mode to the exoskeleton controller. This interrupt-driven, on-sensor inference architecture reduces computation and communication overhead while preserving battery energy and improving robustness in distinguishing level walking from stair ascent for torque-assist control.

## 개요
본 연구는 하지 외골격의 저지연 제어를 지원하기 위해 정강이에 장착된 관성 측정 장치(IMU) 내에서 직접 실시간 추론을 수행하는 웨어러블 인간 활동 인식(HAR) 시스템을 제시합니다. 원시 관성 데이터를 지속적으로 마이크로컨트롤러로 스트리밍하여 분류하는 기존 방식과 달리, 제안된 시스템은 STMicroelectronics LSM6DSV16X IMU에 내장된 머신러닝 코어(MLC)를 사용하여 센서 수준에서 활동 인식을 실행합니다. 이를 통해 호스트 마이크로컨트롤러는 저전력 상태를 유지하고 IMU 레지스터에서 인식된 활동 레이블만 읽을 수 있습니다. 시스템은 여러 인간 활동에 일반화되지만, 본 논문은 성인 참가자로부터 수집된 데이터를 사용하여 세 가지 대표적인 이동 모드(정지, 평지 보행, 계단 오르기)에 초점을 맞춥니다. 경량 결정 트리 모델이 ST MEMS Studio를 사용하여 구성 및 배포되어 센서 내 실행이 가능하도록 하였으며, 마이크로컨트롤러에 사용자 정의 머신러닝 코드 없이 연속 작동이 가능합니다. 작동 중 IMU는 움직임 또는 새로운 분류가 감지되면 인터럽트를 발생시키고, 마이크로컨트롤러가 깨어나 MLC 출력 레지스터를 읽은 후 추론된 모드를 외골격 컨트롤러로 전달합니다. 이 인터럽트 기반의 센서 내 추론 아키텍처는 계산 및 통신 오버헤드를 줄이면서 배터리 에너지를 보존하고, 토크 지원 제어를 위해 평지 보행과 계단 오르기를 구분하는 강건성을 향상시킵니다.

## 핵심 내용
본 연구는 하지 외골격의 저지연 제어를 지원하기 위해 정강이에 장착된 관성 측정 장치(IMU) 내에서 직접 실시간 추론을 수행하는 웨어러블 인간 활동 인식(HAR) 시스템을 제시합니다. 원시 관성 데이터를 지속적으로 마이크로컨트롤러로 스트리밍하여 분류하는 기존 방식과 달리, 제안된 시스템은 STMicroelectronics LSM6DSV16X IMU에 내장된 머신러닝 코어(MLC)를 사용하여 센서 수준에서 활동 인식을 실행합니다. 이를 통해 호스트 마이크로컨트롤러는 저전력 상태를 유지하고 IMU 레지스터에서 인식된 활동 레이블만 읽을 수 있습니다. 시스템은 여러 인간 활동에 일반화되지만, 본 논문은 성인 참가자로부터 수집된 데이터를 사용하여 세 가지 대표적인 이동 모드(정지, 평지 보행, 계단 오르기)에 초점을 맞춥니다. 경량 결정 트리 모델이 ST MEMS Studio를 사용하여 구성 및 배포되어 센서 내 실행이 가능하도록 하였으며, 마이크로컨트롤러에 사용자 정의 머신러닝 코드 없이 연속 작동이 가능합니다. 작동 중 IMU는 움직임 또는 새로운 분류가 감지되면 인터럽트를 발생시키고, 마이크로컨트롤러가 깨어나 MLC 출력 레지스터를 읽은 후 추론된 모드를 외골격 컨트롤러로 전달합니다. 이 인터럽트 기반의 센서 내 추론 아키텍처는 계산 및 통신 오버헤드를 줄이면서 배터리 에너지를 보존하고, 토크 지원 제어를 위해 평지 보행과 계단 오르기를 구분하는 강건성을 향상시킵니다.

## 参考
- http://arxiv.org/abs/2602.21418v1
