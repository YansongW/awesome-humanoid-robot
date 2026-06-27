---
$id: ent_paper_liu_real_time_state_monitoring_and_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Real time state monitoring and fault diagnosis system for motor based on LabVIEW
  zh: 基于LabVIEW的电机实时状态监测与故障诊断系统
  ko: LabVIEW 기반 모터 실시간 상태 모니터링 및 고장 진단 시스템
summary:
  en: Presents a LabVIEW-based real-time monitoring and multi-fault pre-diagnosis
    system for three-phase motors, using NI cDAQ hardware to acquire vibration, speed,
    temperature, current, and voltage signals and applying order-analysis algorithms
    with local/cloud MySQL storage.
  zh: 提出了一种基于LabVIEW的三相电机实时状态监测与多故障预诊断系统，利用NI cDAQ硬件采集振动、转速、温度、电流和电压信号，并采用阶次分析算法，实现本地与云端MySQL存储。
  ko: LabVIEW 기반의 삼상 모터 실시간 상태 모니터링 및 다중 고장 사전 진단 시스템을 제안하며, NI cDAQ 하드웨어로 진동·회전속도·온도·전류·전압
    신호를 수집하고 오더 분석 알고리즘을 적용하여 로컬 및 클라우드 MySQL 저장을 구현한다.
domains:
- 02_components
- 04_assembly_integration_testing
- 05_mass_production
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- three_phase_motor
- condition_monitoring
- fault_diagnosis
- labview
- ni_cdaq
- order_analysis
- kalman_filter
- vibration_analysis
- predictive_maintenance
- cloud_backup
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from arXiv abstract and supplied metadata; full-text sections
    and exact citations were not independently inspected.
sources:
- id: src_001
  type: paper
  title: Real time state monitoring and fault diagnosis system for motor based on
    LabVIEW
  url: https://arxiv.org/abs/1806.09998
  date: '2018'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
- method
---

## Overview

This paper proposes a real-time state monitoring and multi-fault pre-diagnosis system for three-phase motors implemented in LabVIEW. The system acquires multi-dimensional signals—including vibration acceleration, rotational speed, temperature, current, and voltage—through National Instruments cDAQ hardware. Raw signals are conditioned, filtered, and amplified before being processed by algorithms such as Kalman filtering and order analysis to locate and classify fault sources. A two-layer producer-consumer software architecture is employed to maintain real-time collection performance and data integrity. Processed data are stored locally and backed up to a cloud MySQL database for access by other terminals.

The reported deployment combines an industrial personal computer (IPC), an NI cDAQ 9188 chassis, an NI 9232 vibration module, an NI 9205 analog input module, and an NI 9211 thermocouple module. Sensors include a triaxial accelerometer, tachometer, thermocouple, current/voltage sensors, and an eddy-current displacement sensor. The software stack is LabVIEW 2015 with a MySQL 5.7.20 database hosted both locally and on an Alibaba Cloud server running CentOS 7.3.

## Key Contributions

- Design of a real-time LabVIEW system for multi-parameter motor monitoring and fault diagnosis.
- High-speed multi-channel data acquisition using an NI cDAQ 9188 chassis with NI 9232, NI 9205, and NI 9211 modules.
- Application of an order-analysis algorithm for advanced fault-source location and classification.
- A two-layer producer-consumer software framework to ensure real-time collection and data integrity.
- Multi-point data backup to both local and Alibaba Cloud MySQL servers.

## Relevance to Humanoid Robotics

Three-phase motors are core actuation components in humanoid robots, and real-time condition monitoring plus fault pre-diagnosis directly supports drivetrain reliability and scaling mass production. The paper's sensor-fusion approach—combining vibration, thermal, electrical, and speed signals—is directly transferable to monitoring humanoid joint actuators during development, integration testing, and fleet operation.
