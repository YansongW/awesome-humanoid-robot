---
$id: ent_paper_khazoom_tailoring_solution_accuracy_fo_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Tailoring Solution Accuracy for Fast Whole-body Model Predictive Control of
    Legged Robots
  zh: 针对腿式机器人快速全身模型预测控制的求解精度定制
  ko: 족보 로봇을 위한 고속 전신 모델 예측 제어의 해 정확도 조정
summary:
  en: Presents a whole-body nonlinear model predictive control framework that uses
    one SQP iteration per control step with an ADMM-based QP solver to achieve real-time
    rates on the MIT Humanoid, and enforces self-collision constraints via control
    barrier functions at the initial timestep.
  zh: 提出了一种每控制步使用一次SQP迭代和基于ADMM的QP求解器的全身非线性模型预测控制框架，以在MIT人形机器人上实现实时控制，并通过在初始时间步引入控制障碍函数来强制自碰撞约束。
  ko: ADMM 기반 QP 솔버를 사용하여 제어 단계당 하나의 SQP 반복으로 전신 비선형 모델 예측 제어 프레임워크를 제시하여 MIT 휴머노이드에서
    실시간 속도를 달성하고, 초기 시간 단계에서 제어 장벽 함수를 통해 자기 충돌 제약을 강제합니다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full-text review needed
    to confirm exact solver settings, CBF formulation, and hardware deployment details.
sources:
- id: src_001
  type: paper
  title: Tailoring Solution Accuracy for Fast Whole-body Model Predictive Control
    of Legged Robots
  url: https://arxiv.org/abs/2407.10789
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3455907
theoretical_depth:
- method
---

## Overview

Whole-body nonlinear model predictive control has become tractable for humanoid robots thanks to recent solver advances, but enforcing inequality constraints in real time remains expensive because accurate solutions demand many iterations. This paper argues that high-accuracy solutions are often unnecessary on real hardware due to discretization errors, model mismatch, and delays. The authors therefore implement a whole-body NMPC scheme that performs a single sequential quadratic programming iteration per control step and solves the resulting QP subproblems with an alternating-direction method of multipliers solver to obtain low-accuracy but fast solutions.

The formulation handles general equality and inequality constraints, including contact, friction-cone, joint-limit, torque-limit, and self-collision constraints. To avoid the computational burden of enforcing self-collision avoidance across the full horizon, the authors add control barrier function constraints only at the initial timestep. The controller is demonstrated on the MIT Humanoid, a 24-degree-of-freedom, 1.04 m, 24 kg biped, using an UP Xtreme i12 computer.

## Key Contributions

- Demonstrates that low-accuracy ADMM QP solutions are sufficient for real-time whole-body NMPC of legged robots.
- Incorporates control barrier function constraints at the first NMPC timestep to enforce self-collision avoidance with minimal added computation.
- Validates the approach through hardware experiments on the MIT Humanoid, including walking, crossed-leg motions, arm coordination, and push recovery.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it enables real-time whole-body trajectory optimization on a full-size humanoid with contact and self-collision constraints. By planning coordinated arm and leg motions, the controller improves stability during walking and recovery from large disturbances. The reported hardware deployment at 90 Hz for a problem with 32 timesteps, 2004 variables, and 3768 constraints shows that the method is practical for current humanoid platforms, bridging the gap between high-fidelity MPC formulations and real-time execution.
