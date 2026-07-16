---
$id: ent_paper_ficht_centroidal_state_estimation_an_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Centroidal State Estimation and Control for Hardware-constrained Humanoid Robots
  zh: 面向硬件受限人形机器人的质心状态估计与控制
  ko: 하드웨어 제약이 있는 휴머노이드 로봇을 위한 중심 상태 추정 및 제어
summary:
  en: Introduces centroidal state estimation and control methods for humanoid robots with hardware limitations, combining
    a five-mass model with approximate limb dynamics to enable accurate CoM and CoP estimation and reactive stepping without
    force sensing.
  zh: 针对硬件受限的人形机器人，提出了一种结合五质量模型与近似肢体动力学的质心状态估计与控制方法，可在无力传感器的条件下实现准确的质心/压力中心估计与反应式步态平衡。
  ko: 하드웨어 제약이 있는 휴머노이드 로봇을 위해 5질량 모델과 근사된 사지 역학을 결합한 중심 상태 추정 및 제어 방법을 제안하여, 힘 센서 없이도 정확한 질량 중심/압력 중심 추정과 반응형 보행 균형을 실현한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- centroidal_state_estimation
- humanoid_balance_control
- push_recovery
- hardware_constrained_robots
- five_mass_model
- center_of_pressure
- capture_point
- nimbro_op2x
- robocup_2023
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.11019v1.
sources:
- id: src_001
  type: paper
  title: Centroidal State Estimation and Control for Hardware-constrained Humanoid Robots
  url: https://arxiv.org/abs/2312.11019
  date: '2023'
  accessed_at: '2026-06-26'
---
## 概述
We introduce novel methods for state estimation, feedforward and feedback control, which specifically target humanoid robots with hardware limitations. Our method combines a five-mass model with approximate dynamics of each mass. It enables acquiring an accurate assessment of the centroidal state and Center of Pressure, even when direct forms of force or contact sensing are unavailable. Upon this, we develop a feedforward scheme that operates on the centroidal state, accounting for insufficient joint tracking capabilities. Finally, we implement feedback mechanisms, which compensate for the lack in Degrees of Freedom that our NimbRo-OP2X robot has. The whole approach allows for reactive stepping to maintain balance despite these limitations, which was verified on hardware during RoboCup 2023, in Bordeaux, France.

## 核心内容
We introduce novel methods for state estimation, feedforward and feedback control, which specifically target humanoid robots with hardware limitations. Our method combines a five-mass model with approximate dynamics of each mass. It enables acquiring an accurate assessment of the centroidal state and Center of Pressure, even when direct forms of force or contact sensing are unavailable. Upon this, we develop a feedforward scheme that operates on the centroidal state, accounting for insufficient joint tracking capabilities. Finally, we implement feedback mechanisms, which compensate for the lack in Degrees of Freedom that our NimbRo-OP2X robot has. The whole approach allows for reactive stepping to maintain balance despite these limitations, which was verified on hardware during RoboCup 2023, in Bordeaux, France.

## 参考
- http://arxiv.org/abs/2312.11019v1

## Overview
We introduce novel methods for state estimation, feedforward and feedback control, which specifically target humanoid robots with hardware limitations. Our method combines a five-mass model with approximate dynamics of each mass. It enables acquiring an accurate assessment of the centroidal state and Center of Pressure, even when direct forms of force or contact sensing are unavailable. Upon this, we develop a feedforward scheme that operates on the centroidal state, accounting for insufficient joint tracking capabilities. Finally, we implement feedback mechanisms, which compensate for the lack in Degrees of Freedom that our NimbRo-OP2X robot has. The whole approach allows for reactive stepping to maintain balance despite these limitations, which was verified on hardware during RoboCup 2023, in Bordeaux, France.

## Content
We introduce novel methods for state estimation, feedforward and feedback control, which specifically target humanoid robots with hardware limitations. Our method combines a five-mass model with approximate dynamics of each mass. It enables acquiring an accurate assessment of the centroidal state and Center of Pressure, even when direct forms of force or contact sensing are unavailable. Upon this, we develop a feedforward scheme that operates on the centroidal state, accounting for insufficient joint tracking capabilities. Finally, we implement feedback mechanisms, which compensate for the lack in Degrees of Freedom that our NimbRo-OP2X robot has. The whole approach allows for reactive stepping to maintain balance despite these limitations, which was verified on hardware during RoboCup 2023, in Bordeaux, France.

## 개요
우리는 하드웨어 제약이 있는 휴머노이드 로봇을 특별히 대상으로 하는 상태 추정, 피드포워드 및 피드백 제어를 위한 새로운 방법을 소개합니다. 우리의 방법은 5질량 모델과 각 질량의 근사 동역학을 결합합니다. 이를 통해 직접적인 힘 또는 접촉 감지가 불가능한 경우에도 중심 상태와 압력 중심을 정확하게 평가할 수 있습니다. 이를 바탕으로, 관절 추적 성능 부족을 고려하여 중심 상태에서 작동하는 피드포워드 방식을 개발합니다. 마지막으로, 우리의 NimbRo-OP2X 로봇이 가진 자유도 부족을 보완하는 피드백 메커니즘을 구현합니다. 전체 접근 방식은 이러한 제약에도 불구하고 균형을 유지하기 위한 반응적 보행을 가능하게 하며, 이는 프랑스 보르도에서 열린 RoboCup 2023에서 하드웨어를 통해 검증되었습니다.

## 핵심 내용
우리는 하드웨어 제약이 있는 휴머노이드 로봇을 특별히 대상으로 하는 상태 추정, 피드포워드 및 피드백 제어를 위한 새로운 방법을 소개합니다. 우리의 방법은 5질량 모델과 각 질량의 근사 동역학을 결합합니다. 이를 통해 직접적인 힘 또는 접촉 감지가 불가능한 경우에도 중심 상태와 압력 중심을 정확하게 평가할 수 있습니다. 이를 바탕으로, 관절 추적 성능 부족을 고려하여 중심 상태에서 작동하는 피드포워드 방식을 개발합니다. 마지막으로, 우리의 NimbRo-OP2X 로봇이 가진 자유도 부족을 보완하는 피드백 메커니즘을 구현합니다. 전체 접근 방식은 이러한 제약에도 불구하고 균형을 유지하기 위한 반응적 보행을 가능하게 하며, 이는 프랑스 보르도에서 열린 RoboCup 2023에서 하드웨어를 통해 검증되었습니다.
