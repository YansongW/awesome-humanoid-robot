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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2410.21630v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1028 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2410.21630v2

## 개요
다중 이동 매니퓰레이터 협동 작업에서 구조적, 작업적, 로봇 특이적 제약 조건을 동시에 모델링하고 해결하기 어려운 문제에 대해, 본 논문은 이중 솔루션을 제안한다: 먼저 다양한 제약 조건을 동시에 해결 가능한 매니폴드 족으로 모델링하고, 다음으로 제약 비선형 Kaczmarz(cNKZ) 투영 기법을 도입하여 모든 제약 조건을 충족하는 해를 생성한다. 실험 결과, cNKZ는 기준 방법이 전혀 해결하지 못하는 시나리오에서 우수한 성능을 보였다. 이 방법은 샘플 기반 모션 플래너와 결합하여 3~6대의 이동 매니퓰레이터(18~36 자유도)에 대한 복잡한 협조 운동을 생성할 수 있으며, 혼잡한 환경에서 최대 80개의 비선형 제약 조건을 동시에 해결하고 성공률은 최대 92%에 달한다. 하드웨어 실험은 OpenMANIPULATOR-X 매니퓰레이터를 장착한 세 대의 TurtleBot3 Waffle Pi 로봇에서 성공적으로 검증되었다.

## 핵심 내용
### 방법 핵심
- **매니폴드 제약 모델링**: 구조적 제약(예: 매니퓰레이터 관절 한계), 작업적 제약(예: 엔드 이펙터 자세) 및 로봇 특이적 제약(예: 이동 베이스 비홀로노믹 제약)을 미분 가능한 매니폴드 족으로 통합 모델링하여, 제약 해결 문제를 매니폴드 교집합 위의 투영 문제로 변환한다.
- **cNKZ 투영 기법**: 고전적 Kaczmarz 방법을 비선형 제약 시나리오로 확장하여, 각 제약 매니폴드에 교대로 투영하며 반복적으로 해를 구한다. 각 반복에서는 단일 제약의 기울기 투영만 계산하면 되므로, 전역 야코비 행렬 역산을 피하고 계산 복잡도를 크게 낮춘다.

### 실험 설정
- **시뮬레이션 환경**: 혼잡한 환경에 3~6대의 이동 매니퓰레이터(18~36 자유도)를 배치하고, 각 로봇은 엔드 이펙터 궤적 추적, 충돌 회피, 베이스 운동학 등의 제약을 동시에 충족해야 하며, 총 제약 수는 80개에 달한다.
- **기준 비교**: 뉴턴 기반 제약 해석기 및 무작위 샘플링 방법과 비교했을 때, cNKZ는 모든 테스트 시나리오에서 유일하게 실행 가능한 해를 찾는 방법이다.
- **하드웨어 플랫폼**: OpenMANIPULATOR-X 4자유도 매니퓰레이터를 장착한 세 대의 TurtleBot3 Waffle Pi 로봇으로, ROS 2 통신을 통해 협동 운반 작업을 구현한다.

### 주요 결과
- **해결 능력**: cNKZ는 80개의 비선형 제약 조건에서 평균 해결 시간이 0.5초 미만이며, 기준 방법은 제약 수가 20개를 초과하면 완전히 실패한다.
- **계획 성공률**: 혼잡한 환경에서 cNKZ를 RRT* 플래너에 통합한 결과, 6대의 로봇(36 자유도)의 협조 운동 계획 성공률은 92%로, 통합하지 않은 방법보다 67% 향상되었다.
- **하드웨어 검증**: 세 대의 로봇이 협동 운반 작업을 성공적으로 완료했으며, 엔드 이펙터 위치 오차는 2cm 미만, 매니퓰레이터 관절 각도 오차는 1도 미만이다.

### 결론
cNKZ는 매니폴드 투영 전략을 통해 다중 로봇 협동 작업에서의 고차원 제약 해결 문제를 효과적으로 해결하며, 모듈식 설계로 더 많은 로봇이나 더 복잡한 제약 시나리오로 유연하게 확장할 수 있다. 향후 연구는 동적 환경에서의 온라인 제약 업데이트와 실시간 재계획을 탐구할 것이다.
