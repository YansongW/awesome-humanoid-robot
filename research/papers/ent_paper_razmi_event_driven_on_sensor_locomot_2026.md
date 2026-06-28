---
$id: ent_paper_razmi_event_driven_on_sensor_locomot_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Event-Driven On-Sensor Locomotion Mode Recognition Using a Shank-Mounted IMU
    with Embedded Machine Learning for Exoskeleton Control
  zh: 基于嵌入式机器学习和胫部惯性测量单元的事件驱动式外骨骼运动模式识别
  ko: 임베디드 머신러닝을 활용한 경골 장착 IMU의 사건 기반 보행 모드 인식 및 외골격 제어
summary:
  en: This paper presents a wearable human activity recognition system that performs
    real-time locomotion mode recognition (stance, level walking, stair ascent) directly
    on the embedded Machine Learning Core of a shank-mounted LSM6DSV16X IMU, enabling
    interrupt-driven, low-power control of a lower-limb exoskeleton without continuously
    streaming raw sensor data to the host microcontroller.
  zh: 本论文提出了一种可穿戴人体活动识别系统，利用嵌入在胫部LSM6DSV16X惯性测量单元中的机器学习核心，直接对站立、平地行走和楼梯上行三种运动模式进行实时识别，从而以事件驱动、低功耗的方式支持下肢外骨骼控制，无需将原始传感器数据持续传输给主微控制器。
  ko: 본 논문은 경골에 장착된 LSM6DSV16X IMU의 임베디드 머신러닝 코어에서 직접 실시간으로 보행 모드(서기, 평지 보행, 계단 상승)를
    인식하여, 원시 센서 데이터를 호스트 마이크로컨트롤러로 지속적으로 전송하지 않고도 사건 기반의 저전력 하지 외골격 제어를 가능하게 하는 웨어러블
    인간 활동 인식 시스템을 제시한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    the full arXiv text before verification.
sources:
- id: src_001
  type: paper
  title: Event-Driven On-Sensor Locomotion Mode Recognition Using a Shank-Mounted
    IMU with Embedded Machine Learning for Exoskeleton Control
  url: https://arxiv.org/abs/2602.21418
  date: '2026'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

This paper proposes a wearable human activity recognition (HAR) system that performs real-time locomotion mode recognition directly inside a shank-mounted inertial measurement unit (IMU). The target application is low-latency control of a lower-limb exoskeleton. Instead of continuously streaming raw inertial data to a host microcontroller for classification, the system runs inference on the embedded Machine Learning Core (MLC) of the STMicroelectronics LSM6DSV16X IMU.

The study focuses on three representative locomotion modes: stance, level walking, and stair ascent. Data were collected from adult participants, and a lightweight decision-tree model was configured and deployed for on-sensor execution using ST MEMS Studio. During operation, the IMU asserts an interrupt when motion or a new classification is detected; the microcontroller wakes, reads the MLC output registers, and forwards the inferred mode to the exoskeleton controller. This architecture is intended to reduce computation and communication overhead, preserve battery energy, and improve robustness in distinguishing level walking from stair ascent for torque-assist control.

## Key Contributions

- Demonstrates fully on-sensor locomotion mode recognition using the embedded MLC of a single shank-mounted IMU.
- Proposes an interrupt-driven architecture that lets the host microcontroller remain in a low-power state and read only activity labels.
- Reduces computation and communication overhead by eliminating continuous raw inertial data streaming.
- Provides a practical pathway for low-latency, energy-efficient context recognition in lower-limb exoskeletons.

## Relevance to Humanoid Robotics

Although the paper is centered on lower-limb exoskeletons, its on-sensor inference and event-driven microcontroller architecture advances the sensing, low-latency control, and power-efficiency building blocks relevant to humanoid robot locomotion. Wearable, low-power perception at the edge is directly transferable to humanoid systems that require real-time gait mode detection and energy-aware embedded control. The work therefore contributes know-how at the intersection of intelligent components and control software, even though it does not study humanoid robots explicitly.
