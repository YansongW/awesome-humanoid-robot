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

