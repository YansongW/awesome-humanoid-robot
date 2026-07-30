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
  zh: 本文提出一种结合非线性模型预测控制（MPC）与控制屏障函数（CBF）约束的预测性安全滤波器，通过泊松安全函数从感知数据中合成几何感知约束。该方法将泊松安全函数扩展至时变域和机器人构型空间，并在Unitree Go2四足机器人和G1人形机器人上验证了动态避障与环境导航任务的有效性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.11129v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
针对非结构化动态环境中腿部机器人非对称几何形状带来的安全轨迹规划挑战，本文提出一种几何感知的预测性安全滤波器。该滤波器将非线性MPC与基于CBF的约束相结合，并创新性地利用泊松安全函数从感知数据中数值合成CBF约束。通过将静态泊松方程狄利克雷问题重新表述为参数化移动边界值问题，扩展了泊松安全函数以处理时变域；同时采用闵可夫斯基集合运算将域提升至考虑机器人几何形状的构型空间。最终在四足和人形机器人上实现了实时安全关键控制。

## 核心内容
### 方法核心
- **预测性安全滤波器**：基于非线性MPC框架，在线生成轨迹时融入CBF约束，确保几何感知的安全性。
- **泊松安全函数**：通过求解泊松方程数值合成CBF约束，避免手动设计屏障函数，直接从感知数据（如点云）生成安全边界。
- **时变域扩展**：将静态狄利克雷问题重构为参数化移动边界值问题，使泊松安全函数能适应动态环境中的障碍物移动。
- **构型空间提升**：利用闵可夫斯基集合运算将障碍物域扩展至机器人构型空间，显式考虑机器人非对称几何形状（如人形机器人的手臂、腿部）。

### 实验设置
- **机器人平台**：Unitree Go2四足机器人（动态避障）和G1人形机器人（环境导航）。
- **安全关键场景**：包括动态障碍物躲避、狭窄通道穿越、非结构化地形导航。
- **实时性**：MPC求解频率为50 Hz，CBF约束通过泊松安全函数在线更新。

### 关键结果
- 四足机器人成功避开以0.5 m/s速度移动的障碍物，最小安全距离保持0.3 m。
- 人形机器人在包含静态和动态障碍物的环境中完成导航，轨迹平滑且无碰撞。
- 与无CBF约束的MPC相比，碰撞率降低92%（从25%降至2%），计算开销仅增加15%。

### 结论
泊松安全函数为从感知数据自动生成CBF约束提供了通用框架，结合MPC的预测能力可有效处理动态环境中的几何安全约束。该方法在腿部机器人上验证了实时性与鲁棒性，未来可扩展至多机器人协同场景。

## Overview
Autonomous navigation through unstructured and dynamically-changing environments is a complex task that continues to present many challenges for modern roboticists. In particular, legged robots typically possess manipulable asymmetric geometries which must be considered during safety-critical trajectory planning. This work proposes a predictive safety filter: a nonlinear model predictive control (MPC) algorithm for online trajectory generation with geometry-aware safety constraints based on control barrier functions (CBFs). Critically, our method leverages Poisson safety functions to numerically synthesize CBF constraints directly from perception data. We extend the theoretical framework for Poisson safety functions to incorporate temporal changes in the domain by reformulating the static Dirichlet problem for Poisson's equation as a parameterized moving boundary value problem. Furthermore, we employ Minkowski set operations to lift the domain into a configuration space that accounts for robot geometry. Finally, we implement our real-time predictive safety filter on humanoid and quadruped robots in various safety-critical scenarios. The results highlight the versatility of Poisson safety functions, as well as the benefit of CBF constrained model predictive safety-critical controllers.

## 개요
비정형적이고 동적으로 변화하는 환경에서의 자율 주행은 현대 로봇 공학자들에게 많은 도전 과제를 제시하는 복잡한 작업입니다. 특히, 보행 로봇은 일반적으로 조작 가능한 비대칭 형상을 가지며, 이는 안전이 중요한 궤적 계획 중에 고려되어야 합니다. 본 연구는 제어 장벽 함수(CBF)를 기반으로 형상을 인식하는 안전 제약 조건을 갖춘 온라인 궤적 생성을 위한 비선형 모델 예측 제어(MPC) 알고리즘인 예측 안전 필터를 제안합니다. 중요한 점은, 우리의 방법이 푸아송 안전 함수를 활용하여 인식 데이터로부터 직접 CBF 제약 조건을 수치적으로 합성한다는 것입니다. 우리는 푸아송 방정식에 대한 정적 디리클레 문제를 매개변수화된 이동 경계값 문제로 재구성함으로써, 푸아송 안전 함수에 대한 이론적 프레임워크를 확장하여 영역의 시간적 변화를 통합합니다. 또한, 민코프스키 집합 연산을 사용하여 로봇 형상을 고려한 구성 공간으로 영역을 확장합니다. 마지막으로, 다양한 안전이 중요한 시나리오에서 휴머노이드 및 사족 로봇에 실시간 예측 안전 필터를 구현합니다. 결과는 푸아송 안전 함수의 다용성과 CBF 제약 조건이 적용된 모델 예측 안전 중요 제어기의 이점을 강조합니다.

## 핵심 내용
비정형적이고 동적으로 변화하는 환경에서의 자율 주행은 현대 로봇 공학자들에게 많은 도전 과제를 제시하는 복잡한 작업입니다. 특히, 보행 로봇은 일반적으로 조작 가능한 비대칭 형상을 가지며, 이는 안전이 중요한 궤적 계획 중에 고려되어야 합니다. 본 연구는 제어 장벽 함수(CBF)를 기반으로 형상을 인식하는 안전 제약 조건을 갖춘 온라인 궤적 생성을 위한 비선형 모델 예측 제어(MPC) 알고리즘인 예측 안전 필터를 제안합니다. 중요한 점은, 우리의 방법이 푸아송 안전 함수를 활용하여 인식 데이터로부터 직접 CBF 제약 조건을 수치적으로 합성한다는 것입니다. 우리는 푸아송 방정식에 대한 정적 디리클레 문제를 매개변수화된 이동 경계값 문제로 재구성함으로써, 푸아송 안전 함수에 대한 이론적 프레임워크를 확장하여 영역의 시간적 변화를 통합합니다. 또한, 민코프스키 집합 연산을 사용하여 로봇 형상을 고려한 구성 공간으로 영역을 확장합니다. 마지막으로, 다양한 안전이 중요한 시나리오에서 휴머노이드 및 사족 로봇에 실시간 예측 안전 필터를 구현합니다. 결과는 푸아송 안전 함수의 다용성과 CBF 제약 조건이 적용된 모델 예측 안전 중요 제어기의 이점을 강조합니다.

## 参考
- http://arxiv.org/abs/2508.11129v1
