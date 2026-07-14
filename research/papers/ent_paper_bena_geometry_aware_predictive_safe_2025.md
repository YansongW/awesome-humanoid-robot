---
$id: ent_paper_bena_geometry_aware_predictive_safe_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Geometry-Aware Predictive Safety Filters on Humanoids: From Poisson Safety Functions to CBF Constrained MPC'
  zh: 面向人形机器人的几何感知预测安全滤波器：从泊松安全函数到 CBF 约束模型预测控制
  ko: '휴머노이드를 위한 기하-aware 예측 안전 필터: 푸아송 안전 함수에서 CBF 제약 MPC로'
summary:
  en: This paper proposes a predictive safety filter that combines nonlinear model predictive control (MPC) with control barrier
    function (CBF) constraints synthesized from perception data via Poisson safety functions. It extends Poisson safety functions
    to time-varying domains and robot configuration space using moving-boundary and Minkowski-set operations, and validates
    the approach on Unitree Go2 quadruped and G1 humanoid robots in dynamic collision avoidance and environmental navigation
    tasks.
  zh: 本文提出了一种预测安全滤波器，将非线性模型预测控制（MPC）与通过泊松安全函数从感知数据中合成的控制障碍函数（CBF）约束相结合。该方法通过移动边界和闵可夫斯基集合运算将泊松安全函数扩展到时变域和机器人构型空间，并在 Unitree
    Go2 四足机器人和 G1 人形机器人的动态避障与环境导航任务中进行了验证。
  ko: 본 논문은 비선형 모델 예측 제어(MPC)와 푸아송 안전 함수를 통해 지각 데이터에서 합성된 제어 장벽 함수(CBF) 제약을 결합한 예측 안전 필터를 제안한다. 이동 경계 및 밍코프스키 집합 연산을 사용하여
    푸아송 안전 함수를 시변 영역과 로봇 구성 공간으로 확장하고, Unitree Go2 사족 로봇과 G1 휴머노이드 로봇의 동적 충돌 회피 및 환경 탐색 작업에서 검증하였다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11129v1.
sources:
- id: src_001
  type: paper
  title: 'Geometry-Aware Predictive Safety Filters on Humanoids: From Poisson Safety Functions to CBF Constrained MPC'
  url: https://arxiv.org/abs/2508.11129
  date: '2025'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_robot_system_unitree_g1
  relationship: evaluates_on
  description:
    en: The predictive safety filter is experimentally validated on the Unitree G1 humanoid robot in dynamic collision avoidance
      and environmental navigation scenarios.
    zh: 预测安全滤波器在 Unitree G1 人形机器人的动态避障和环境导航场景下进行了实验验证。
    ko: 예측 안전 필터는 Unitree G1 휴머노이드 로봇에서 동적 충돌 회피 및 환경 탐색 시나리오로 실험적으로 검증되었다.
- id: ent_oem_unitree_robotics
  relationship: cites
  description:
    en: The paper identifies Unitree by model name as the manufacturer of the Go2 quadruped and G1 humanoid platforms used
      in the experiments.
    zh: 论文通过型号名称将 Unitree 认定为实验中使用的 Go2 四足机器人和 G1 人形机器人平台的制造商。
    ko: 논문은 실험에 사용된 Go2 사족 로봇과 G1 휴머노이드 플랫폼의 제조사로서 Unitree를 모델명으로 식별한다.
theoretical_depth:
- system
---
## 概述
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## 核心内容
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## 参考
- http://arxiv.org/abs/2508.11129v1

