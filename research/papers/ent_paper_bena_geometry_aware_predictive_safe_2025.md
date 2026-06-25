---
$id: ent_paper_bena_geometry_aware_predictive_safe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Geometry-Aware Predictive Safety Filters on Humanoids: From Poisson Safety
    Functions to CBF Constrained MPC'
  zh: 面向人形机器人的几何感知预测安全滤波器：从泊松安全函数到 CBF 约束模型预测控制
  ko: '휴머노이드를 위한 기하-aware 예측 안전 필터: 푸아송 안전 함수에서 CBF 제약 MPC로'
summary:
  en: This paper proposes a predictive safety filter that combines nonlinear model
    predictive control (MPC) with control barrier function (CBF) constraints synthesized
    from perception data via Poisson safety functions. It extends Poisson safety functions
    to time-varying domains and robot configuration space using moving-boundary and
    Minkowski-set operations, and validates the approach on Unitree Go2 quadruped
    and G1 humanoid robots in dynamic collision avoidance and environmental navigation
    tasks.
  zh: 本文提出了一种预测安全滤波器，将非线性模型预测控制（MPC）与通过泊松安全函数从感知数据中合成的控制障碍函数（CBF）约束相结合。该方法通过移动边界和闵可夫斯基集合运算将泊松安全函数扩展到时变域和机器人构型空间，并在
    Unitree Go2 四足机器人和 G1 人形机器人的动态避障与环境导航任务中进行了验证。
  ko: 본 논문은 비선형 모델 예측 제어(MPC)와 푸아송 안전 함수를 통해 지각 데이터에서 합성된 제어 장벽 함수(CBF) 제약을 결합한 예측
    안전 필터를 제안한다. 이동 경계 및 밍코프스키 집합 연산을 사용하여 푸아송 안전 함수를 시변 영역과 로봇 구성 공간으로 확장하고, Unitree
    Go2 사족 로봇과 G1 휴머노이드 로봇의 동적 충돌 회피 및 환경 탐색 작업에서 검증하였다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- predictive_safety_filter
- model_predictive_control
- control_barrier_functions
- poisson_safety_functions
- geometry_aware_safety
- minkowski_difference
- moving_boundary_problem
- dynamic_collision_avoidance
- safe_navigation
- unitree_g1
- unitree_go2
- legged_robots
- humanoid_navigation
- perception_based_control
- occupancy_map
- cbf_constrained_mpc
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from the full arXiv paper text; requires human review before
    verification.
sources:
- id: src_001
  type: paper
  title: 'Geometry-Aware Predictive Safety Filters on Humanoids: From Poisson Safety
    Functions to CBF Constrained MPC'
  url: https://arxiv.org/abs/2508.11129
  date: '2025'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: evaluates_on
  description:
    en: The predictive safety filter is experimentally validated on the Unitree G1
      humanoid robot in dynamic collision avoidance and environmental navigation scenarios.
    zh: 预测安全滤波器在 Unitree G1 人形机器人的动态避障和环境导航场景下进行了实验验证。
    ko: 예측 안전 필터는 Unitree G1 휴머노이드 로봇에서 동적 충돌 회피 및 환경 탐색 시나리오로 실험적으로 검증되었다.
- id: ent_oem_unitree_robotics
  relationship: cites
  description:
    en: The paper identifies Unitree by model name as the manufacturer of the Go2
      quadruped and G1 humanoid platforms used in the experiments.
    zh: 论文通过型号名称将 Unitree 认定为实验中使用的 Go2 四足机器人和 G1 人形机器人平台的制造商。
    ko: 논문은 실험에 사용된 Go2 사족 로봇과 G1 휴머노이드 플랫폼의 제조사로서 Unitree를 모델명으로 식별한다.
---



## Overview

Legged robots with manipulable, asymmetric geometries must navigate unstructured and dynamically-changing environments while keeping both translation and rotation safe. This paper proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm that generates online trajectories subject to geometry-aware safety constraints derived from control barrier functions (CBFs). The core idea is to synthesize these CBF constraints directly from perception data by using Poisson safety functions, which are obtained by solving a Dirichlet problem for Poisson's equation over the safe spatial domain. The authors extend this construction in two directions: they reformulate the static Dirichlet problem as a parameterized moving boundary value problem to predict how the safe set evolves over a finite horizon, and they use Minkowski set operations to lift the domain into a higher-dimensional configuration space that captures robot orientation and shape.

The resulting Poisson safety function h_QT(y, q, t) is incorporated into a discrete-time CBF constrained MPC formulation for a single-integrator reduced-order model with two translational and one rotational degree of freedom. A mid-level MPC+CBF predictive safety filter outputs velocity references that are tracked by a low-level reinforcement-learning locomotion controller, with an additional QP-based waist controller on the humanoid to track heading commands without losing balance. The numerical PDE is solved with successive over-relaxation on a checkerboard-parallelized grid, and the MPC quadratic program is solved at 100 Hz with OSQP.

Experiments are conducted on a Unitree Go2 quadruped and a Unitree G1 humanoid in two scenarios: dynamic collision avoidance against a moving dodgeball, and tele-operated environmental navigation through a narrow corridor for 100 seconds. The humanoid additionally carries an oblong payload to emphasize rotational safety. Both robots successfully maintain positive Poisson safety values throughout the maneuvers, demonstrating that geometry-aware predictive filtering allows simultaneous translational and rotational avoidance in real time.

## Key Contributions

- Reformulates the static Dirichlet problem for Poisson safety functions as a time-varying moving boundary problem for forward safety prediction.
- Lifts the Poisson domain into higher-dimensional configuration space via Minkowski set operations to account for robot orientation and geometry.
- Formulates a novel real-time MPC+CBF predictive safety filter using the extended Poisson safety function for a single-integrator reduced-order model.
- Experimentally validates the approach on Unitree Go2 quadruped and Unitree G1 humanoid robots in dynamic collision avoidance and environmental navigation tasks.

## Relevance to Humanoid Robotics

The paper is directly relevant to humanoid robotics because it targets safe, real-time navigation of a legged machine with asymmetric geometry in human-occupied, dynamic spaces. The Unitree G1 experiments explicitly show the humanoid carrying an oblong payload and maneuvering through a narrow corridor by rotating its body to reduce its effective footprint, behavior that would not arise from point-mass or centroid-only safety formulations. This demonstrates that geometry-aware predictive safety filtering can mitigate deadlock and collision risk for humanoids in industrial or service settings where orientation matters.

From a knowledge-base perspective, the work bridges theoretical safety-critical control (CBFs, Poisson PDEs, MPC) with embodied humanoid and quadruped hardware, providing a concrete algorithmic reference for perception-based collision avoidance. Its limitations—formal guarantees not claimed for time-varying environments, offboard PDE solve latency, and 2D overhead-camera occupancy sensing—also help scope the maturity of the method for real-world deployment.
