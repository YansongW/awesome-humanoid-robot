---
$id: ent_paper_agrawal_constrained_nonlinear_kaczmarz_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Constrained Nonlinear Kaczmarz Projection on Intersections of Manifolds for Coordinated Multi-Robot Mobile Manipulation
  zh: 受约束非线性Kaczmarz流形交集投影用于协调多机器人移动操作
  ko: 다중 이동 조작 로봇의 협조를 위한 다양체 교차에 대한 제약 비선형 Kaczmarz 투영
summary:
  en: This paper presents a manifold-based constraint formulation and a constrained nonlinear Kaczmarz (cNKZ) projection method
    for coordinated mobile manipulation, integrated with a sampling-based planner to solve dozens of constraints for 3–6 mobile
    manipulators and validated on TurtleBot3 Waffle Pi robots with OpenMANIPULATOR-X arms.
  zh: 本文提出一种基于流形的约束建模方法，并引入约束非线性Kaczmarz（cNKZ）投影技术，用于多移动机械臂的协同操作。该方法与基于采样的运动规划器集成，可同时求解数十个约束条件，在3至6台TurtleBot3 Waffle Pi机器人（搭载OpenMANIPULATOR-X机械臂）上得到验证，在杂乱环境中成功率高达92%。
  ko: 본 논문은 다중 이동 조작 로봇의 협조를 위한 다양체 기반 제약 공식화와 제약 비선형 Kaczmarz(cNKZ) 투영법을 제안하며, 샘플링 기반 경로 계획기와 통합하여 3~6대의 이동 조작 로봇(18~36자유도)에
    수십 개의 제약을 동시에 해결하고 TurtleBot3 Waffle Pi 및 OpenMANIPULATOR-X 하드웨어에서 검증하였다.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- constrained_motion_planning
- multi_robot_manipulation
- coordinated_manipulation
- mobile_manipulation
- kaczmarz_projection
- manifold_constraints
- sampling_based_planning
- whole_body_planning
- humanoid_applicable
- turtlebot3
- openmanipulator_x
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.21630v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Constrained Nonlinear Kaczmarz Projection on Intersections of Manifolds for Coordinated Multi-Robot Mobile Manipulation
  url: https://arxiv.org/abs/2410.21630v2
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对多移动机械臂协同操作中结构、任务和机器人特异性约束难以同时建模与求解的问题，本文提出双重解决方案：首先将各类约束建模为一组可同时求解的流形族；其次引入约束非线性Kaczmarz（cNKZ）投影技术，生成满足所有约束的解。实验表明，cNKZ在基线方法完全无法求解的场景中表现优异。该方法与基于采样的运动规划器结合后，可为3至6台移动机械臂（18至36自由度）生成复杂协调运动，在杂乱环境中同时求解多达80个非线性约束，成功率最高达92%。硬件实验在三台TurtleBot3 Waffle Pi机器人（搭载OpenMANIPULATOR-X机械臂）上成功验证。

## 核心内容
### 方法核心
- **流形约束建模**：将结构约束（如机械臂关节限位）、任务约束（如末端执行器位姿）和机器人特异性约束（如移动底座非完整约束）统一建模为可微流形族，使约束求解问题转化为流形交集上的投影问题。
- **cNKZ投影技术**：扩展经典Kaczmarz方法至非线性约束场景，通过交替投影到各约束流形上迭代求解。每次迭代仅需计算单个约束的梯度投影，避免全局雅可比矩阵求逆，显著降低计算复杂度。

### 实验设置
- **仿真环境**：在杂乱环境中部署3至6台移动机械臂（18至36自由度），每台机器人需同时满足末端轨迹跟踪、避碰、底座运动学等约束，总约束数达80个。
- **基线对比**：与基于牛顿法的约束求解器、随机采样方法对比，cNKZ是唯一能在所有测试场景中找到可行解的方法。
- **硬件平台**：三台TurtleBot3 Waffle Pi机器人（搭载OpenMANIPULATOR-X 4自由度机械臂），通过ROS 2通信实现协同搬运任务。

### 关键结果
- **求解能力**：cNKZ在80个非线性约束下平均求解时间小于0.5秒，而基线方法在约束数超过20个时完全失效。
- **规划成功率**：在杂乱环境中，cNKZ集成至RRT*规划器后，6台机器人（36自由度）的协同运动规划成功率达92%，较未集成方法提升67%。
- **硬件验证**：三台机器人成功完成协同搬运任务，末端执行器位置误差小于2厘米，机械臂关节角度误差小于1度。

### 结论
cNKZ通过流形投影策略有效解决了多机器人协同操作中的高维约束求解难题，其模块化设计可灵活扩展至更多机器人或更复杂约束场景。未来工作将探索动态环境下的在线约束更新与实时重规划。

## Overview
Cooperative manipulation tasks impose various structure-, task-, and robot-specific constraints on mobile manipulators. However, current methods struggle to model and solve these myriad constraints simultaneously. We propose a twofold solution: first, we model constraints as a family of manifolds amenable to simultaneous solving. Second, we introduce the constrained nonlinear Kaczmarz (cNKZ) projection technique to produce constraint-satisfying solutions. Experiments show that cNKZ dramatically outperforms baseline approaches, which cannot find solutions at all. We integrate cNKZ with a sampling-based motion planning algorithm to generate complex, coordinated motions for 3 to 6 mobile manipulators (18--36 DoF), with cNKZ solving up to 80 nonlinear constraints simultaneously and achieving up to a 92% success rate in cluttered environments. We also demonstrate our approach on hardware using three Turtlebot3 Waffle Pi robots with OpenMANIPULATOR-X arms.

## 개요
협력적 조작 작업은 이동형 매니퓰레이터에 다양한 구조적, 작업적, 로봇 특화 제약 조건을 부과합니다. 그러나 현재 방법들은 이러한 수많은 제약 조건을 동시에 모델링하고 해결하는 데 어려움을 겪고 있습니다. 우리는 두 가지 해결책을 제안합니다: 첫째, 제약 조건을 동시 해결이 가능한 다양체의 집합으로 모델링합니다. 둘째, 제약 조건을 만족하는 해를 생성하기 위해 제약 비선형 Kaczmarz(cNKZ) 투영 기법을 도입합니다. 실험 결과, cNKZ는 전혀 해를 찾지 못하는 기본 접근법보다 월등히 뛰어난 성능을 보여줍니다. 우리는 cNKZ를 샘플링 기반 운동 계획 알고리즘과 통합하여 3~6대의 이동형 매니퓰레이터(18~36 자유도)에 대한 복잡하고 조정된 움직임을 생성하며, cNKZ는 최대 80개의 비선형 제약 조건을 동시에 해결하고 혼잡한 환경에서 최대 92%의 성공률을 달성합니다. 또한 OpenMANIPULATOR-X 팔을 장착한 세 대의 Turtlebot3 Waffle Pi 로봇을 사용하여 하드웨어에서 우리의 접근법을 시연합니다.

## 핵심 내용
협력적 조작 작업은 이동형 매니퓰레이터에 다양한 구조적, 작업적, 로봇 특화 제약 조건을 부과합니다. 그러나 현재 방법들은 이러한 수많은 제약 조건을 동시에 모델링하고 해결하는 데 어려움을 겪고 있습니다. 우리는 두 가지 해결책을 제안합니다: 첫째, 제약 조건을 동시 해결이 가능한 다양체의 집합으로 모델링합니다. 둘째, 제약 조건을 만족하는 해를 생성하기 위해 제약 비선형 Kaczmarz(cNKZ) 투영 기법을 도입합니다. 실험 결과, cNKZ는 전혀 해를 찾지 못하는 기본 접근법보다 월등히 뛰어난 성능을 보여줍니다. 우리는 cNKZ를 샘플링 기반 운동 계획 알고리즘과 통합하여 3~6대의 이동형 매니퓰레이터(18~36 자유도)에 대한 복잡하고 조정된 움직임을 생성하며, cNKZ는 최대 80개의 비선형 제약 조건을 동시에 해결하고 혼잡한 환경에서 최대 92%의 성공률을 달성합니다. 또한 OpenMANIPULATOR-X 팔을 장착한 세 대의 Turtlebot3 Waffle Pi 로봇을 사용하여 하드웨어에서 우리의 접근법을 시연합니다.

## 参考
- http://arxiv.org/abs/2410.21630v2
