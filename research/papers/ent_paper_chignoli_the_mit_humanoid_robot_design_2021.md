---
$id: ent_paper_chignoli_the_mit_humanoid_robot_design_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors'
  zh: MIT人形机器人：面向杂技行为的设计、运动规划与控制
  ko: 'MIT 휴머노이드 로봇: 곡예 동작을 위한 설계, 운동 계획 및 제어'
summary:
  en: This paper presents the design, actuator-aware kino-dynamic planning, and landing control of the MIT Humanoid robot,
    demonstrating back flips, front flips, and spinning jumps in a realistic dynamics simulation that includes validated actuator
    and battery models.
  zh: 本文介绍了MIT Humanoid机器人的设计、运动规划与控制方法，实现了后空翻、前空翻和旋转跳跃等高难度特技动作。核心贡献包括开发了两种新型本体感受执行器、执行器感知的运动规划器以及结合模型预测控制与全身脉冲控制的着陆控制器。所有特技行为均在包含验证执行器与电池模型的逼真动力学仿真中成功演示。
  ko: 본 논문은 MIT 휴머노이드 로봇의 설계, 액추에이터 인식 키노다이나믹 계획법 및 착륙 제어를 제시하며, 경험적으로 검증된 액추에이터 및 배터리 모델을 포함한 사실적인 동역학 시뮬레이션에서 백플립, 프론트플립,
    스핀 점프를 시연한다.
domains:
- 06_design_engineering
- 02_components
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
- system
tags:
- humanoid_robot
- acrobatic_behaviors
- proprioceptive_actuator
- kino_dynamic_planning
- actuator_aware_planning
- centroidal_dynamics
- model_predictive_control
- whole_body_impulse_control
- landing_control
- dynamic_simulation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.09025v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (615 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'The MIT Humanoid Robot: Design, Motion Planning, and Control For Acrobatic Behaviors'
  url: https://arxiv.org/abs/2104.09025
  date: '2021'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
该研究系统性地解决了人形机器人特技动作（如空翻和旋转跳跃）所需的硬件设计、运动规划与控制问题。团队首先开发了两种新型本体感受执行器，并通过定制测功机实验验证其性能。在运动规划中，通过近似构型依赖的反作用力极限，将执行器的扭矩、速度和功率限制纳入运动学-动力学规划器；在仿真中则结合执行器动力学与机器人全身动力学。着陆控制方面，通过动态一致的方式连接模型预测控制与全身脉冲控制，实现了长时域最优控制与高带宽全身动力学反馈的融合。执行器在整个运动过程中的扭矩输出基于包含电池电压降和反电动势的模型进行了验证。

## 核心内容
### 硬件设计
- 开发了两种新型本体感受执行器，通过定制测功机实验评估其扭矩、速度和功率性能。
- 执行器模型包含电池电压降和反电动势效应，用于验证全运动过程中的扭矩输出。

### 运动规划
- 采用执行器感知的运动学-动力学规划器，通过近似构型依赖的反作用力极限来反映执行器的扭矩、速度和功率限制。
- 动力学仿真中集成了执行器动力学与机器人全身动力学。

### 着陆控制
- 将模型预测控制与全身脉冲控制通过动态一致的方式连接，实现长时域最优控制与高带宽全身动力学反馈。
- 该方法兼顾了规划的时间跨度与实时反馈的响应速度。

### 实验验证
- 在逼真的动力学仿真中成功演示了后空翻、前空翻和旋转跳跃等特技行为。
- 所有仿真均基于经过验证的执行器与电池模型，确保结果的可信度。

## Overview
Demonstrating acrobatic behavior of a humanoid robot such as flips and spinning jumps requires systematic approaches across hardware design, motion planning, and control. In this paper, we present a new humanoid robot design, an actuator-aware kino-dynamic motion planner, and a landing controller as part of a practical system design for highly dynamic motion control of the humanoid robot. To achieve the impulsive motions, we develop two new proprioceptive actuators and experimentally evaluate their performance using our custom-designed dynamometer. The actuator's torque, velocity, and power limits are reflected in our kino-dynamic motion planner by approximating the configuration-dependent reaction force limits and in our dynamics simulator by including actuator dynamics along with the robot's full-body dynamics. For the landing control, we effectively integrate model-predictive control and whole-body impulse control by connecting them in a dynamically consistent way to accomplish both the long-time horizon optimal control and high-bandwidth full-body dynamics-based feedback. Actuators' torque output over the entire motion are validated based on the velocity-torque model including battery voltage droop and back-EMF voltage. With the carefully designed hardware and control framework, we successfully demonstrate dynamic behaviors such as back flips, front flips, and spinning jumps in our realistic dynamics simulation.

## 参考
- http://arxiv.org/abs/2104.09025v1

## 개요
이 연구는 휴머노이드 로봇의 묘기 동작(예: 공중제비 및 회전 점프)에 필요한 하드웨어 설계, 운동 계획 및 제어 문제를 체계적으로 해결합니다. 팀은 먼저 두 가지 새로운 고유수용성 액추에이터를 개발하고, 맞춤형 다이나모미터 실험을 통해 성능을 검증했습니다. 운동 계획에서는 구성에 의존하는 반작용력 한계를 근사화하여 액추에이터의 토크, 속도 및 전력 제한을 운동학-동역학 계획기에 통합했으며, 시뮬레이션에서는 액추에이터 동역학과 로봇 전신 동역학을 결합했습니다. 착지 제어에서는 모델 예측 제어와 전신 임펄스 제어를 동적으로 일관된 방식으로 연결하여, 장시간 영역 최적 제어와 고대역폭 전신 동역학 피드백의 융합을 구현했습니다. 전체 운동 과정에서의 액추에이터 토크 출력은 배터리 전압 강하와 역기전력을 포함한 모델을 기반으로 검증되었습니다.

## 핵심 내용
### 하드웨어 설계
- 두 가지 새로운 고유수용성 액추에이터를 개발하고, 맞춤형 다이나모미터 실험을 통해 토크, 속도 및 전력 성능을 평가했습니다.
- 액추에이터 모델은 배터리 전압 강하와 역기전력 효과를 포함하여 전체 운동 과정에서의 토크 출력을 검증하는 데 사용되었습니다.

### 운동 계획
- 구성에 의존하는 반작용력 한계를 근사화하여 액추에이터의 토크, 속도 및 전력 제한을 반영하는 액추에이터 인지 운동학-동역학 계획기를 채택했습니다.
- 동역학 시뮬레이션에는 액추에이터 동역학과 로봇 전신 동역학이 통합되었습니다.

### 착지 제어
- 모델 예측 제어와 전신 임펄스 제어를 동적으로 일관된 방식으로 연결하여, 장시간 영역 최적 제어와 고대역폭 전신 동역학 피드백을 구현했습니다.
- 이 방법은 계획의 시간 범위와 실시간 피드백의 응답 속도를 모두 고려합니다.

### 실험 검증
- 사실적인 동역학 시뮬레이션에서 뒤공중제비, 앞공중제비 및 회전 점프와 같은 묘기 동작을 성공적으로 시연했습니다.
- 모든 시뮬레이션은 검증된 액추에이터 및 배터리 모델을 기반으로 하여 결과의 신뢰성을 보장합니다.
