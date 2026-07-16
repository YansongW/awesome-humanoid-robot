---
$id: ent_paper_khazoom_tailoring_solution_accuracy_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Tailoring Solution Accuracy for Fast Whole-body Model Predictive Control of Legged Robots
  zh: 针对腿式机器人快速全身模型预测控制的求解精度定制
  ko: 족보 로봇을 위한 고속 전신 모델 예측 제어의 해 정확도 조정
summary:
  en: Presents a whole-body nonlinear model predictive control framework that uses one SQP iteration per control step with
    an ADMM-based QP solver to achieve real-time rates on the MIT Humanoid, and enforces self-collision constraints via control
    barrier functions at the initial timestep.
  zh: 提出了一种每控制步使用一次SQP迭代和基于ADMM的QP求解器的全身非线性模型预测控制框架，以在MIT人形机器人上实现实时控制，并通过在初始时间步引入控制障碍函数来强制自碰撞约束。
  ko: ADMM 기반 QP 솔버를 사용하여 제어 단계당 하나의 SQP 반복으로 전신 비선형 모델 예측 제어 프레임워크를 제시하여 MIT 휴머노이드에서 실시간 속도를 달성하고, 초기 시간 단계에서 제어 장벽 함수를 통해
    자기 충돌 제약을 강제합니다.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- model_predictive_control
- nonlinear_mpc
- whole_body_control
- legged_robots
- admm
- qp_solver
- osqp
- control_barrier_functions
- self_collision_avoidance
- mit_humanoid
- real_time_control
- sequential_quadratic_programming
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2407.10789v2.
sources:
- id: src_001
  type: paper
  title: Tailoring Solution Accuracy for Fast Whole-body Model Predictive Control of Legged Robots
  url: https://arxiv.org/abs/2407.10789
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3455907
theoretical_depth:
- method
---
## 概述
Thanks to recent advancements in accelerating non-linear model predictive control (NMPC), it is now feasible to deploy whole-body NMPC at real-time rates for humanoid robots. However, enforcing inequality constraints in real time for such high-dimensional systems remains challenging due to the need for additional iterations. This paper presents an implementation of whole-body NMPC for legged robots that provides low-accuracy solutions to NMPC with general equality and inequality constraints. Instead of aiming for highly accurate optimal solutions, we leverage the alternating direction method of multipliers to rapidly provide low-accuracy solutions to quadratic programming subproblems. Our extensive simulation results indicate that real robots often cannot benefit from highly accurate solutions due to dynamics discretization errors, inertial modeling errors and delays. We incorporate control barrier functions (CBFs) at the initial timestep of the NMPC for the self-collision constraints, resulting in up to a 26-fold reduction in the number of self-collisions without adding computational burden. The controller is reliably deployed on hardware at 90 Hz for a problem involving 32 timesteps, 2004 variables, and 3768 constraints. The NMPC delivers sufficiently accurate solutions, enabling the MIT Humanoid to plan complex crossed-leg and arm motions that enhance stability when walking and recovering from significant disturbances.

## 核心内容
Thanks to recent advancements in accelerating non-linear model predictive control (NMPC), it is now feasible to deploy whole-body NMPC at real-time rates for humanoid robots. However, enforcing inequality constraints in real time for such high-dimensional systems remains challenging due to the need for additional iterations. This paper presents an implementation of whole-body NMPC for legged robots that provides low-accuracy solutions to NMPC with general equality and inequality constraints. Instead of aiming for highly accurate optimal solutions, we leverage the alternating direction method of multipliers to rapidly provide low-accuracy solutions to quadratic programming subproblems. Our extensive simulation results indicate that real robots often cannot benefit from highly accurate solutions due to dynamics discretization errors, inertial modeling errors and delays. We incorporate control barrier functions (CBFs) at the initial timestep of the NMPC for the self-collision constraints, resulting in up to a 26-fold reduction in the number of self-collisions without adding computational burden. The controller is reliably deployed on hardware at 90 Hz for a problem involving 32 timesteps, 2004 variables, and 3768 constraints. The NMPC delivers sufficiently accurate solutions, enabling the MIT Humanoid to plan complex crossed-leg and arm motions that enhance stability when walking and recovering from significant disturbances.

## 参考
- http://arxiv.org/abs/2407.10789v2

## Overview
Thanks to recent advancements in accelerating non-linear model predictive control (NMPC), it is now feasible to deploy whole-body NMPC at real-time rates for humanoid robots. However, enforcing inequality constraints in real time for such high-dimensional systems remains challenging due to the need for additional iterations. This paper presents an implementation of whole-body NMPC for legged robots that provides low-accuracy solutions to NMPC with general equality and inequality constraints. Instead of aiming for highly accurate optimal solutions, we leverage the alternating direction method of multipliers to rapidly provide low-accuracy solutions to quadratic programming subproblems. Our extensive simulation results indicate that real robots often cannot benefit from highly accurate solutions due to dynamics discretization errors, inertial modeling errors and delays. We incorporate control barrier functions (CBFs) at the initial timestep of the NMPC for the self-collision constraints, resulting in up to a 26-fold reduction in the number of self-collisions without adding computational burden. The controller is reliably deployed on hardware at 90 Hz for a problem involving 32 timesteps, 2004 variables, and 3768 constraints. The NMPC delivers sufficiently accurate solutions, enabling the MIT Humanoid to plan complex crossed-leg and arm motions that enhance stability when walking and recovering from significant disturbances.

## Content
Thanks to recent advancements in accelerating non-linear model predictive control (NMPC), it is now feasible to deploy whole-body NMPC at real-time rates for humanoid robots. However, enforcing inequality constraints in real time for such high-dimensional systems remains challenging due to the need for additional iterations. This paper presents an implementation of whole-body NMPC for legged robots that provides low-accuracy solutions to NMPC with general equality and inequality constraints. Instead of aiming for highly accurate optimal solutions, we leverage the alternating direction method of multipliers to rapidly provide low-accuracy solutions to quadratic programming subproblems. Our extensive simulation results indicate that real robots often cannot benefit from highly accurate solutions due to dynamics discretization errors, inertial modeling errors and delays. We incorporate control barrier functions (CBFs) at the initial timestep of the NMPC for the self-collision constraints, resulting in up to a 26-fold reduction in the number of self-collisions without adding computational burden. The controller is reliably deployed on hardware at 90 Hz for a problem involving 32 timesteps, 2004 variables, and 3768 constraints. The NMPC delivers sufficiently accurate solutions, enabling the MIT Humanoid to plan complex crossed-leg and arm motions that enhance stability when walking and recovering from significant disturbances.

## 개요
비선형 모델 예측 제어(NMPC)의 가속화에 대한 최근 발전 덕분에, 인간형 로봇을 위한 전신 NMPC를 실시간 속도로 배포하는 것이 가능해졌습니다. 그러나 이러한 고차원 시스템에 대해 실시간으로 부등식 제약 조건을 적용하는 것은 추가 반복이 필요하기 때문에 여전히 어려운 과제입니다. 본 논문은 일반적인 등식 및 부등식 제약 조건을 가진 NMPC에 대해 낮은 정확도의 해를 제공하는 보행 로봇용 전신 NMPC 구현을 제시합니다. 높은 정확도의 최적 해를 목표로 하는 대신, 승수 교대 방향법(ADMM)을 활용하여 2차 계획법 하위 문제에 대한 낮은 정확도의 해를 신속하게 제공합니다. 광범위한 시뮬레이션 결과는 실제 로봇이 동역학 이산화 오차, 관성 모델링 오차 및 지연으로 인해 높은 정확도의 해로부터 이점을 얻지 못하는 경우가 많음을 보여줍니다. 우리는 자체 충돌 제약 조건을 위해 NMPC의 초기 시간 단계에서 제어 장벽 함수(CBF)를 통합하여, 계산 부담을 추가하지 않으면서 자체 충돌 횟수를 최대 26배까지 줄였습니다. 이 제어기는 32개의 시간 단계, 2004개의 변수 및 3768개의 제약 조건을 포함하는 문제에 대해 90Hz로 하드웨어에서 안정적으로 배포됩니다. NMPC는 충분히 정확한 해를 제공하여 MIT 휴머노이드가 걷기 및 큰 외란으로부터 회복 시 안정성을 향상시키는 복잡한 다리 교차 및 팔 동작을 계획할 수 있게 합니다.

## 핵심 내용
비선형 모델 예측 제어(NMPC)의 가속화에 대한 최근 발전 덕분에, 인간형 로봇을 위한 전신 NMPC를 실시간 속도로 배포하는 것이 가능해졌습니다. 그러나 이러한 고차원 시스템에 대해 실시간으로 부등식 제약 조건을 적용하는 것은 추가 반복이 필요하기 때문에 여전히 어려운 과제입니다. 본 논문은 일반적인 등식 및 부등식 제약 조건을 가진 NMPC에 대해 낮은 정확도의 해를 제공하는 보행 로봇용 전신 NMPC 구현을 제시합니다. 높은 정확도의 최적 해를 목표로 하는 대신, 승수 교대 방향법(ADMM)을 활용하여 2차 계획법 하위 문제에 대한 낮은 정확도의 해를 신속하게 제공합니다. 광범위한 시뮬레이션 결과는 실제 로봇이 동역학 이산화 오차, 관성 모델링 오차 및 지연으로 인해 높은 정확도의 해로부터 이점을 얻지 못하는 경우가 많음을 보여줍니다. 우리는 자체 충돌 제약 조건을 위해 NMPC의 초기 시간 단계에서 제어 장벽 함수(CBF)를 통합하여, 계산 부담을 추가하지 않으면서 자체 충돌 횟수를 최대 26배까지 줄였습니다. 이 제어기는 32개의 시간 단계, 2004개의 변수 및 3768개의 제약 조건을 포함하는 문제에 대해 90Hz로 하드웨어에서 안정적으로 배포됩니다. NMPC는 충분히 정확한 해를 제공하여 MIT 휴머노이드가 걷기 및 큰 외란으로부터 회복 시 안정성을 향상시키는 복잡한 다리 교차 및 팔 동작을 계획할 수 있게 합니다.
