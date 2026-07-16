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
  en: Presents a LabVIEW-based real-time monitoring and multi-fault pre-diagnosis system for three-phase motors, using NI
    cDAQ hardware to acquire vibration, speed, temperature, current, and voltage signals and applying order-analysis algorithms
    with local/cloud MySQL storage.
  zh: 提出了一种基于LabVIEW的三相电机实时状态监测与多故障预诊断系统，利用NI cDAQ硬件采集振动、转速、温度、电流和电压信号，并采用阶次分析算法，实现本地与云端MySQL存储。
  ko: LabVIEW 기반의 삼상 모터 실시간 상태 모니터링 및 다중 고장 사전 진단 시스템을 제안하며, NI cDAQ 하드웨어로 진동·회전속도·온도·전류·전압 신호를 수집하고 오더 분석 알고리즘을 적용하여 로컬 및
    클라우드 MySQL 저장을 구현한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1806.09998v1.
sources:
- id: src_001
  type: paper
  title: Real time state monitoring and fault diagnosis system for motor based on LabVIEW
  url: https://arxiv.org/abs/1806.09998
  date: '2018'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
- method
---
## 概述
Motor is the most widely used production equipment in industrial field. In order to realize the real-time state monitoring and multi-fault pre-diagnosis of three-phase motor, this paper presents a design of three-phase motor state monitoring and fault diagnosis system based on LabVIEW.   The multi-dimensional vibration acceleration, rotational speed, temperature, current and voltage signals of the motor are collected with NI cDAQ acquisition equipment in real time and high speed. At the same time, the model of motor health state and fault state is established. The order analysis algorithm is used to analyze the data at an advanced level, and the diagnosis and classification of different fault types are realized. The system is equipped with multi-channel acquisition, display, analysis and storage. Combined with the current cloud transmission technology, we will back up the data to the cloud to be used by other terminals.

## 核心内容
Motor is the most widely used production equipment in industrial field. In order to realize the real-time state monitoring and multi-fault pre-diagnosis of three-phase motor, this paper presents a design of three-phase motor state monitoring and fault diagnosis system based on LabVIEW.   The multi-dimensional vibration acceleration, rotational speed, temperature, current and voltage signals of the motor are collected with NI cDAQ acquisition equipment in real time and high speed. At the same time, the model of motor health state and fault state is established. The order analysis algorithm is used to analyze the data at an advanced level, and the diagnosis and classification of different fault types are realized. The system is equipped with multi-channel acquisition, display, analysis and storage. Combined with the current cloud transmission technology, we will back up the data to the cloud to be used by other terminals.

## 参考
- http://arxiv.org/abs/1806.09998v1

## Overview
Motors are the most widely used production equipment in the industrial field. To enable real-time condition monitoring and multi-fault pre-diagnosis of three-phase motors, this paper presents a design of a three-phase motor condition monitoring and fault diagnosis system based on LabVIEW. The system collects multi-dimensional vibration acceleration, rotational speed, temperature, current, and voltage signals of the motor in real time and at high speed using NI cDAQ acquisition equipment. At the same time, models of motor healthy and faulty states are established. The order analysis algorithm is employed for advanced data analysis, enabling the diagnosis and classification of different fault types. The system features multi-channel acquisition, display, analysis, and storage. Combined with current cloud transmission technology, data is backed up to the cloud for use by other terminals.

## Content
Motors are the most widely used production equipment in the industrial field. To enable real-time condition monitoring and multi-fault pre-diagnosis of three-phase motors, this paper presents a design of a three-phase motor condition monitoring and fault diagnosis system based on LabVIEW. The system collects multi-dimensional vibration acceleration, rotational speed, temperature, current, and voltage signals of the motor in real time and at high speed using NI cDAQ acquisition equipment. At the same time, models of motor healthy and faulty states are established. The order analysis algorithm is employed for advanced data analysis, enabling the diagnosis and classification of different fault types. The system features multi-channel acquisition, display, analysis, and storage. Combined with current cloud transmission technology, data is backed up to the cloud for use by other terminals.

## 개요
모터는 산업 현장에서 가장 널리 사용되는 생산 장비입니다. 3상 모터의 실시간 상태 모니터링 및 다중 고장 사전 진단을 실현하기 위해, 본 논문은 LabVIEW 기반의 3상 모터 상태 모니터링 및 고장 진단 시스템 설계를 제시합니다. NI cDAQ 수집 장비를 사용하여 모터의 다차원 진동 가속도, 회전 속도, 온도, 전류 및 전압 신호를 실시간 고속으로 수집합니다. 동시에 모터의 건강 상태 및 고장 상태 모델을 구축합니다. 오더 분석 알고리즘을 사용하여 데이터를 고급 수준에서 분석하고, 다양한 고장 유형의 진단 및 분류를 실현합니다. 시스템은 다채널 수집, 표시, 분석 및 저장 기능을 갖추고 있습니다. 현재의 클라우드 전송 기술과 결합하여 데이터를 클라우드에 백업하여 다른 단말기에서 사용할 수 있도록 합니다.

## 핵심 내용
모터는 산업 현장에서 가장 널리 사용되는 생산 장비입니다. 3상 모터의 실시간 상태 모니터링 및 다중 고장 사전 진단을 실현하기 위해, 본 논문은 LabVIEW 기반의 3상 모터 상태 모니터링 및 고장 진단 시스템 설계를 제시합니다. NI cDAQ 수집 장비를 사용하여 모터의 다차원 진동 가속도, 회전 속도, 온도, 전류 및 전압 신호를 실시간 고속으로 수집합니다. 동시에 모터의 건강 상태 및 고장 상태 모델을 구축합니다. 오더 분석 알고리즘을 사용하여 데이터를 고급 수준에서 분석하고, 다양한 고장 유형의 진단 및 분류를 실현합니다. 시스템은 다채널 수집, 표시, 분석 및 저장 기능을 갖추고 있습니다. 현재의 클라우드 전송 기술과 결합하여 데이터를 클라우드에 백업하여 다른 단말기에서 사용할 수 있도록 합니다.
