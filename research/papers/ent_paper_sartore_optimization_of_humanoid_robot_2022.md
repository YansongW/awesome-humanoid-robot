---
$id: ent_paper_sartore_optimization_of_humanoid_robot_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting
  zh: 面向人机工效协作负载提升的人形机器人设计优化
  ko: 인간-로봇 인체공학적 하중 리프팅을 위한 휴머노이드 로봇 설계 최적화
summary:
  en: Sartore, Rapetti, and Pucci formulate a nonlinear hardware-design optimization of humanoid link geometry and density
    to minimize agents' energy expenditure during collaborative payload lifting, then apply the method to evolve the iCub
    design into the ergoCub humanoid, extending the ergonomic payload height range and reducing robot energy expenditure by
    about 33%.
  zh: Sartore、Rapetti 与 Pucci 提出了一种非线性硬件设计优化方法，通过调整人形机器人的连杆几何与密度参数，最小化人机协作搬运重物时的能量消耗。该方法将 iCub 机器人优化为 ergoCub，将符合人体工学的负载高度范围从
    0.8–1.2 m 扩展至 0.8–1.5 m，并使机器人能耗降低约 33%。
  ko: Sartore, Rapetti, Pucci는 인간 모델을 포함한 비선형 하드웨어 설계 최적화 문제를 제안하여 협업 하중 리프팅에서 작업자들의 에너지 소비를 최소화하고, 이를 iCub에서 ergoCub 휴머노이드
    설계에 적용하여 인체공학적 작업 높이 범위를 확장하고 로봇 에너지 소비를 약 33% 감소시켰다.
domains:
- 06_design_engineering
- 02_components
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- ergonomic_collaboration
- payload_lifting
- hardware_optimization
- humanoid_design
- energy_expenditure
- physical_human_robot_interaction
- ergocub
- icub
- link_geometry
- density_parameterization
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.13503v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting
  url: https://arxiv.org/abs/2211.13503
  date: '2022'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
本文在现有的人机协作控制架构基础上，进一步将机器人硬件参数作为优化变量，以提升协作搬运的工效学表现。优化变量涵盖机器人运动学与动力学参数，并确保其物理一致性，同时将人体模型纳入优化框架。通过最大化交互工效（以双方能量消耗为指标），该方法综合考虑了机器人运动学、动力学、硬件约束及人体几何特征。最终，该优化方法被用于设计 ergoCub 机器人，使其具备与人类进行工效交互的具身智能。

## 核心内容
### 方法概述
- 提出一种非线性硬件设计优化方法，目标是最小化人机协作搬运重物时的总能量消耗。
- 优化变量包括机器人连杆几何参数与密度，这些参数需满足运动学与动力学的物理一致性约束。
- 人体模型被显式纳入优化问题，确保交互过程中的工效学表现。

### 优化框架
- 优化问题中同时考虑机器人运动学、动力学、硬件约束以及人体几何特征。
- 工效学指标由双方能量消耗共同定义，优化目标为最大化该指标。

### 实验设置与结果
- 以 iCub 人形机器人作为优化起点，设计出 ergoCub 机器人。
- 优化后的 ergoCub 机器人能够搬运重物的高度范围从 iCub 的 0.8–1.2 m 扩展至 0.8–1.5 m。
- 机器人能量消耗降低约 33%，同时保持人体工效学表现，整体交互质量得到提升。

## Overview
When a human and a humanoid robot collaborate physically, ergonomics is a key factor to consider. Assuming a given humanoid robot, several control architectures exist nowadays to address ergonomic physical human-robot collaboration. This paper takes one step further by considering robot hardware parameters as optimization variables in the problem of collaborative payload lifting. The variables that parametrize robot's kinematics and dynamics ensure their physical consistency, and the human model is considered in the optimization problem. By leveraging the proposed modelling framework, the ergonomy of the interaction is maximized, here given by the agents' energy expenditure. Robot kinematic, dynamics, hardware constraints and human geometries are considered when solving the associated optimization problem. The proposed methodology is used to identify optimum hardware parameters for the design of the ergoCub robot, a humanoid possessing a degree of embodied intelligence for ergonomic interaction with humans. For the optimization problem, the starting point is the iCub humanoid robot. The obtained robot design reaches loads at heights in the range of 0.8-1.5 m with respect to the iCub robot whose range is limited to 0.8-1.2 m. The robot energy expenditure is decreased by about 33%, meanwhile, the human ergonomy is preserved, leading overall to an improved interaction.

## 개요
인간과 휴머노이드 로봇이 물리적으로 협력할 때, 인간공학은 고려해야 할 핵심 요소입니다. 주어진 휴머노이드 로봇을 가정할 때, 현재 인간공학적 물리적 인간-로봇 협력을 다루기 위한 여러 제어 아키텍처가 존재합니다. 본 논문은 협력적 중량물 들어올리기 문제에서 로봇 하드웨어 매개변수를 최적화 변수로 고려하여 한 걸음 더 나아갑니다. 로봇의 운동학과 동역학을 매개변수화하는 변수들은 물리적 일관성을 보장하며, 인간 모델도 최적화 문제에 포함됩니다. 제안된 모델링 프레임워크를 활용하여 상호작용의 인간공학적 효율이 최대화되며, 이는 에이전트의 에너지 소비로 표현됩니다. 관련 최적화 문제를 해결할 때 로봇의 운동학, 동역학, 하드웨어 제약 조건 및 인간의 기하학적 특성이 고려됩니다. 제안된 방법론은 인간과의 인간공학적 상호작용을 위해 어느 정도의 체화된 지능을 갖춘 휴머노이드인 ergoCub 로봇 설계에 최적의 하드웨어 매개변수를 식별하는 데 사용됩니다. 최적화 문제의 시작점은 iCub 휴머노이드 로봇입니다. 얻어진 로봇 설계는 0.8-1.2m 범위로 제한된 iCub 로봇에 비해 0.8-1.5m 높이의 하중에 도달합니다. 로봇의 에너지 소비는 약 33% 감소하는 동시에 인간의 인간공학적 효율은 유지되어, 전반적으로 개선된 상호작용을 이끌어냅니다.

## 핵심 내용
인간과 휴머노이드 로봇이 물리적으로 협력할 때, 인간공학은 고려해야 할 핵심 요소입니다. 주어진 휴머노이드 로봇을 가정할 때, 현재 인간공학적 물리적 인간-로봇 협력을 다루기 위한 여러 제어 아키텍처가 존재합니다. 본 논문은 협력적 중량물 들어올리기 문제에서 로봇 하드웨어 매개변수를 최적화 변수로 고려하여 한 걸음 더 나아갑니다. 로봇의 운동학과 동역학을 매개변수화하는 변수들은 물리적 일관성을 보장하며, 인간 모델도 최적화 문제에 포함됩니다. 제안된 모델링 프레임워크를 활용하여 상호작용의 인간공학적 효율이 최대화되며, 이는 에이전트의 에너지 소비로 표현됩니다. 관련 최적화 문제를 해결할 때 로봇의 운동학, 동역학, 하드웨어 제약 조건 및 인간의 기하학적 특성이 고려됩니다. 제안된 방법론은 인간과의 인간공학적 상호작용을 위해 어느 정도의 체화된 지능을 갖춘 휴머노이드인 ergoCub 로봇 설계에 최적의 하드웨어 매개변수를 식별하는 데 사용됩니다. 최적화 문제의 시작점은 iCub 휴머노이드 로봇입니다. 얻어진 로봇 설계는 0.8-1.2m 범위로 제한된 iCub 로봇에 비해 0.8-1.5m 높이의 하중에 도달합니다. 로봇의 에너지 소비는 약 33% 감소하는 동시에 인간의 인간공학적 효율은 유지되어, 전반적으로 개선된 상호작용을 이끌어냅니다.

## 参考
- http://arxiv.org/abs/2211.13503v1
