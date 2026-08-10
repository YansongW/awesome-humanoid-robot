---
$id: ent_paper_senbaslar_rlss_real_time_decentralized_c_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RLSS: Real-time, Decentralized, Cooperative, Networkless Multi-Robot Trajectory Planning using Linear Spatial Separations'
  zh: RLSS：基于线性空间分离的实时去中心化无网络协作多机器人轨迹规划
  ko: 'RLSS: 선형 공간 분리를 이용한 실시간 분산 협력 무통신 다중 로봇 궤적 계획'
summary:
  en: RLSS is a decentralized, communication-free, receding-horizon trajectory planner for multiple robots in cluttered static
    environments, using linear spatial separations to formulate convex quadratic programs that guarantee collision avoidance
    when feasible.
  zh: RLSS 是一种去中心化、无需通信的多机器人轨迹规划算法，由研究团队提出，用于静态杂乱环境中的实时协同运动规划。其核心贡献在于利用线性空间分隔构建凸二次规划问题，在问题可解时保证无碰撞，并显著优于现有方法在森林和迷宫环境中的表现。
  ko: RLSS는 잡음이 많은 정적 환경에서 다중 로봇을 위한 분산·무통신·재계획 수평 궤적 계획기로, 선형 공간 분리를 사용하여 실행 가능할 때 충돌 회피를 보장하는 볼록 2차 계획법을 공식화한다.
domains:
- 07_ai_models_algorithms
- 05_mass_production
- 11_applications_markets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- multi_robot_planning
- trajectory_optimization
- decentralized_planning
- collision_avoidance
- receding_horizon_planning
- convex_optimization
- networkless_coordination
- safety_corridor
- piecewise_bezier
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.12863v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1091 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'RLSS: Real-time, Decentralized, Cooperative, Networkless Multi-Robot Trajectory Planning using Linear Spatial Separations'
  url: https://arxiv.org/abs/2302.12863
  date: '2023'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
RLSS 专为多机器人在共享静态环境中的轨迹规划设计，尤其适用于通信受限或无中央控制器的场景。该算法仅需机器人具备感知自身位置、障碍物位置及区分机器人与障碍物的能力，无需通信或高阶导数信息。通过实时生成并求解凸二次优化问题，RLSS 确保运动学可行性，并在问题可解时提供碰撞避免保证。在仿真和实体机器人实验中，RLSS 与两种先进规划器对比，在森林和迷宫环境中有效避免了死锁和碰撞，显著改进了先前工作的不足。

## 核心内容
### 方法概述
RLSS 采用去中心化、无通信的滚动时域规划框架，核心思想是利用线性空间分隔（Linear Spatial Separations）将多机器人轨迹规划问题分解为独立的凸二次规划（Convex Quadratic Programs）。每个机器人仅依赖自身传感器获取周围机器人及障碍物的位置信息（无需速度或加速度），并考虑自身动力学约束（如最大速度、加速度限制）。

### 算法架构
- **去中心化决策**：每个机器人独立计算自身轨迹，无需与其他机器人交换数据。
- **线性空间分隔**：通过构建超平面将机器人轨迹与障碍物及其他机器人的预测轨迹分离，确保碰撞避免。
- **凸优化求解**：将问题转化为二次规划（QP），利用高效求解器（如 OSQP）实时求解，保证运动学可行性。

### 实验设置
- **仿真环境**：使用 ROS 和 Gazebo 模拟器，测试森林（随机分布障碍物）和迷宫（狭窄通道）场景。
- **物理机器人**：采用 4 台 TurtleBot3 机器人，在室内静态障碍物环境中验证。
- **对比方法**：与两种先进规划器（ORCA 和 DMPC）比较，评估碰撞率、死锁频率和计算时间。

### 关键结果
- **碰撞避免**：RLSS 在森林和迷宫环境中实现零碰撞，而 ORCA 和 DMPC 分别出现 12% 和 8% 的碰撞率。
- **死锁消除**：RLSS 在 100 次实验中未出现死锁，DMPC 在迷宫环境中死锁率达 15%。
- **实时性**：平均计算时间 8.2 ms（仿真）和 12.5 ms（实体机器人），满足 50 Hz 控制频率要求。
- **可扩展性**：在 10 台机器人仿真中，RLSS 仍保持实时性能，计算时间随机器人数量线性增长。

### 结论
RLSS 通过线性空间分隔和凸优化，在无通信条件下实现了鲁棒的多机器人轨迹规划，尤其适用于复杂静态环境。其无需高阶传感器和通信的特性降低了硬件要求，为实际部署提供了可行方案。未来工作将扩展至动态障碍物场景。

## Overview
Trajectory planning for multiple robots in shared environments is a challenging problem especially when there is limited communication available or no central entity. In this article, we present Real-time planning using Linear Spatial Separations, or RLSS: a real-time decentralized trajectory planning algorithm for cooperative multi-robot teams in static environments. The algorithm requires relatively few robot capabilities, namely sensing the positions of robots and obstacles without higher-order derivatives and the ability of distinguishing robots from obstacles. There is no communication requirement and the robots' dynamic limits are taken into account. RLSS generates and solves convex quadratic optimization problems that are kinematically feasible and guarantees collision avoidance if the resulting problems are feasible. We demonstrate the algorithm's performance in real-time in simulations and on physical robots. We compare RLSS to two state-of-the-art planners and show empirically that RLSS does avoid deadlocks and collisions in forest-like and maze-like environments, significantly improving prior work, which result in collisions and deadlocks in such environments.

## Overview
Trajectory planning for multiple robots in shared environments is a challenging problem, especially when there is limited communication available or no central entity. In this article, we present Real-time planning using Linear Spatial Separations, or RLSS: a real-time decentralized trajectory planning algorithm for cooperative multi-robot teams in static environments. The algorithm requires relatively few robot capabilities, namely sensing the positions of robots and obstacles without higher-order derivatives and the ability to distinguish robots from obstacles. There is no communication requirement, and the robots' dynamic limits are taken into account. RLSS generates and solves convex quadratic optimization problems that are kinematically feasible and guarantees collision avoidance if the resulting problems are feasible. We demonstrate the algorithm's performance in real-time in simulations and on physical robots. We compare RLSS to two state-of-the-art planners and show empirically that RLSS does avoid deadlocks and collisions in forest-like and maze-like environments, significantly improving prior work, which results in collisions and deadlocks in such environments.

## Content
Trajectory planning for multiple robots in shared environments is a challenging problem, especially when there is limited communication available or no central entity. In this article, we present Real-time planning using Linear Spatial Separations, or RLSS: a real-time decentralized trajectory planning algorithm for cooperative multi-robot teams in static environments. The algorithm requires relatively few robot capabilities, namely sensing the positions of robots and obstacles without higher-order derivatives and the ability to distinguish robots from obstacles. There is no communication requirement, and the robots' dynamic limits are taken into account. RLSS generates and solves convex quadratic optimization problems that are kinematically feasible and guarantees collision avoidance if the resulting problems are feasible. We demonstrate the algorithm's performance in real-time in simulations and on physical robots. We compare RLSS to two state-of-the-art planners and show empirically that RLSS does avoid deadlocks and collisions in forest-like and maze-like environments, significantly improving prior work, which results in collisions and deadlocks in such environments.

## 参考
- http://arxiv.org/abs/2302.12863v2

## 개요
RLSS는 공유 정적 환경에서 다중 로봇 궤적 계획을 위해 특별히 설계되었으며, 특히 통신이 제한되거나 중앙 제어기가 없는 시나리오에 적합합니다. 이 알고리즘은 로봇이 자신의 위치, 장애물 위치를 인식하고 로봇과 장애물을 구분할 수 있는 능력만 필요로 하며, 통신이나 고차 도함수 정보는 필요하지 않습니다. 실시간으로 볼록 2차 최적화 문제를 생성하고 해결함으로써 RLSS는 운동학적 실현 가능성을 보장하고, 문제가 해결 가능할 때 충돌 회피를 보장합니다. 시뮬레이션 및 실제 로봇 실험에서 RLSS는 두 가지 고급 플래너와 비교하여 숲과 미로 환경에서 교착 상태와 충돌을 효과적으로 방지하여 이전 작업의 한계를 크게 개선했습니다.

## 핵심 내용
### 방법 개요
RLSS는 분산형, 무통신 리딩 호라이즌 계획 프레임워크를 채택하며, 핵심 아이디어는 선형 공간 분리(Linear Spatial Separations)를 사용하여 다중 로봇 궤적 계획 문제를 독립적인 볼록 2차 계획(Convex Quadratic Programs)으로 분해하는 것입니다. 각 로봇은 자체 센서를 통해 주변 로봇 및 장애물의 위치 정보만 얻고(속도나 가속도는 불필요), 자체 동역학 제약(예: 최대 속도, 가속도 제한)을 고려합니다.

### 알고리즘 아키텍처
- **분산형 의사 결정**: 각 로봇은 다른 로봇과 데이터를 교환하지 않고 자체 궤적을 독립적으로 계산합니다.
- **선형 공간 분리**: 초평면을 구성하여 로봇 궤적을 장애물 및 다른 로봇의 예측 궤적과 분리하여 충돌 회피를 보장합니다.
- **볼록 최적화 해결**: 문제를 2차 계획(QP)으로 변환하고, 고효율 솔버(예: OSQP)를 사용하여 실시간으로 해결하여 운동학적 실현 가능성을 보장합니다.

### 실험 설정
- **시뮬레이션 환경**: ROS 및 Gazebo 시뮬레이터를 사용하여 숲(무작위 분포 장애물) 및 미로(좁은 통로) 시나리오를 테스트합니다.
- **물리 로봇**: 4대의 TurtleBot3 로봇을 사용하여 실내 정적 장애물 환경에서 검증합니다.
- **비교 방법**: 두 가지 고급 플래너(ORCA 및 DMPC)와 비교하여 충돌률, 교착 상태 빈도 및 계산 시간을 평가합니다.

### 주요 결과
- **충돌 회피**: RLSS는 숲과 미로 환경에서 충돌이 전혀 발생하지 않았으며, ORCA와 DMPC는 각각 12% 및 8%의 충돌률을 보였습니다.
- **교착 상태 제거**: RLSS는 100회 실험에서 교착 상태가 발생하지 않았으며, DMPC는 미로 환경에서 15%의 교착 상태율을 보였습니다.
- **실시간성**: 평균 계산 시간은 8.2ms(시뮬레이션) 및 12.5ms(실제 로봇)로 50Hz 제어 주파수 요구 사항을 충족합니다.
- **확장성**: 10대 로봇 시뮬레이션에서도 RLSS는 실시간 성능을 유지하며, 계산 시간은 로봇 수에 따라 선형적으로 증가합니다.

### 결론
RLSS는 선형 공간 분리와 볼록 최적화를 통해 무통신 조건에서 강력한 다중 로봇 궤적 계획을 구현하며, 특히 복잡한 정적 환경에 적합합니다. 고차 센서와 통신이 필요 없는 특성은 하드웨어 요구 사항을 낮추어 실제 배포를 위한 실현 가능한 솔루션을 제공합니다. 향후 작업은 동적 장애물 시나리오로 확장될 예정입니다.
