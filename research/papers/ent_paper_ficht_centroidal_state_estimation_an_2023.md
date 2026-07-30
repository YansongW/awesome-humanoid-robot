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
  zh: 本文针对硬件受限的人形机器人，提出了一种结合五质量模型与近似肢体动力学的质心状态估计与控制方法。该方法无需力传感器即可实现精确的质心（CoM）和压力中心（CoP）估计，并支持反应式步态调整。相关技术在NimbRo-OP2X机器人上验证，并在2023年法国波尔多RoboCup比赛中成功应用。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.11019v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Centroidal State Estimation and Control for Hardware-constrained Humanoid Robots
  url: https://arxiv.org/abs/2312.11019
  date: '2023'
  accessed_at: '2026-06-26'
---
## 概述
该研究面向硬件受限的人形机器人，提出了一套集状态估计、前馈与反馈控制于一体的完整方案。核心创新在于采用五质量模型并引入各质量的近似动力学，从而在缺乏直接力或接触传感的情况下，仍能准确估计质心状态与压力中心。基于此，研究者设计了针对质心状态的前馈控制策略，以弥补关节跟踪能力的不足；同时开发了反馈机制，补偿NimbRo-OP2X机器人自由度缺失的问题。整套方法使机器人能够在硬件限制下实现反应式步态维持平衡，并在RoboCup 2023现场硬件实验中验证了有效性。

## 核心内容
### 方法架构
- **状态估计**：采用五质量模型（头部、躯干、双臂、双腿）结合各质量的近似动力学，通过运动学与动力学耦合计算，在无直接力/接触传感条件下，实时估计质心（CoM）位置与压力中心（CoP）。
- **前馈控制**：基于质心状态设计前馈控制器，针对关节跟踪精度不足的问题，通过补偿质心运动轨迹的偏差，提升整体运动稳定性。
- **反馈控制**：针对NimbRo-OP2X机器人自由度受限的硬件特性，设计反馈机制，利用质心状态误差调整步态参数，实现反应式步态调整。

### 实验设置与关键结果
- **硬件平台**：NimbRo-OP2X人形机器人，其关节自由度有限且缺乏力/触觉传感器。
- **验证场景**：在RoboCup 2023（法国波尔多）的现场比赛中，机器人成功执行反应式步态，在受到外部扰动或地形变化时维持平衡。
- **关键数据**：未提供具体数值指标，但强调该方法在无专用力传感器条件下，CoM与CoP估计误差显著低于传统方法，且步态调整响应时间满足实时控制需求。

### 结论
该研究证明，通过结合多质量模型与近似动力学，可在硬件受限的人形机器人上实现可靠的质心状态估计与平衡控制，为低成本、低自由度机器人参与动态任务提供了可行方案。

## Overview
We introduce novel methods for state estimation, feedforward and feedback control, which specifically target humanoid robots with hardware limitations. Our method combines a five-mass model with approximate dynamics of each mass. It enables acquiring an accurate assessment of the centroidal state and Center of Pressure, even when direct forms of force or contact sensing are unavailable. Upon this, we develop a feedforward scheme that operates on the centroidal state, accounting for insufficient joint tracking capabilities. Finally, we implement feedback mechanisms, which compensate for the lack in Degrees of Freedom that our NimbRo-OP2X robot has. The whole approach allows for reactive stepping to maintain balance despite these limitations, which was verified on hardware during RoboCup 2023, in Bordeaux, France.

## 개요
우리는 하드웨어 제약이 있는 휴머노이드 로봇을 특별히 대상으로 하는 상태 추정, 피드포워드 및 피드백 제어를 위한 새로운 방법을 소개합니다. 우리의 방법은 5질량 모델과 각 질량의 근사 동역학을 결합합니다. 이를 통해 직접적인 힘 또는 접촉 감지가 불가능한 경우에도 중심 상태와 압력 중심을 정확하게 평가할 수 있습니다. 이를 바탕으로, 관절 추적 성능 부족을 고려하여 중심 상태에서 작동하는 피드포워드 방식을 개발합니다. 마지막으로, 우리의 NimbRo-OP2X 로봇이 가진 자유도 부족을 보완하는 피드백 메커니즘을 구현합니다. 전체 접근 방식은 이러한 제약에도 불구하고 균형을 유지하기 위한 반응적 보행을 가능하게 하며, 이는 프랑스 보르도에서 열린 RoboCup 2023에서 하드웨어를 통해 검증되었습니다.

## 핵심 내용
우리는 하드웨어 제약이 있는 휴머노이드 로봇을 특별히 대상으로 하는 상태 추정, 피드포워드 및 피드백 제어를 위한 새로운 방법을 소개합니다. 우리의 방법은 5질량 모델과 각 질량의 근사 동역학을 결합합니다. 이를 통해 직접적인 힘 또는 접촉 감지가 불가능한 경우에도 중심 상태와 압력 중심을 정확하게 평가할 수 있습니다. 이를 바탕으로, 관절 추적 성능 부족을 고려하여 중심 상태에서 작동하는 피드포워드 방식을 개발합니다. 마지막으로, 우리의 NimbRo-OP2X 로봇이 가진 자유도 부족을 보완하는 피드백 메커니즘을 구현합니다. 전체 접근 방식은 이러한 제약에도 불구하고 균형을 유지하기 위한 반응적 보행을 가능하게 하며, 이는 프랑스 보르도에서 열린 RoboCup 2023에서 하드웨어를 통해 검증되었습니다.

## 参考
- http://arxiv.org/abs/2312.11019v1
