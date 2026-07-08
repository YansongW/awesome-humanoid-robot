---
$id: ent_paper_senbaslar_rlss_real_time_decentralized_c_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RLSS: Real-time, Decentralized, Cooperative, Networkless Multi-Robot Trajectory
    Planning using Linear Spatial Separations'
  zh: RLSS：基于线性空间分离的实时去中心化无网络协作多机器人轨迹规划
  ko: 'RLSS: 선형 공간 분리를 이용한 실시간 분산 협력 무통신 다중 로봇 궤적 계획'
summary:
  en: RLSS is a decentralized, communication-free, receding-horizon trajectory planner
    for multiple robots in cluttered static environments, using linear spatial separations
    to formulate convex quadratic programs that guarantee collision avoidance when
    feasible.
  zh: RLSS是一种针对杂乱静态环境中多机器人的去中心化、无通信、滚动时域轨迹规划器，利用线性空间分离构建保证可行时避免碰撞的凸二次规划。
  ko: RLSS는 잡음이 많은 정적 환경에서 다중 로봇을 위한 분산·무통신·재계획 수평 궤적 계획기로, 선형 공간 분리를 사용하여 실행 가능할
    때 충돌 회피를 보장하는 볼록 2차 계획법을 공식화한다.
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
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; page-level citation checks
    against the full PDF are still required before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'RLSS: Real-time, Decentralized, Cooperative, Networkless Multi-Robot Trajectory
    Planning using Linear Spatial Separations'
  url: https://arxiv.org/abs/2302.12863
  date: '2023'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

Trajectory planning for multiple robots in shared environments becomes especially difficult when no central planner is available and robots cannot communicate with one another. This paper proposes Real-time planning using Linear Spatial Separations (RLSS), a decentralized, receding-horizon algorithm designed for cooperative multi-robot teams operating in static, cluttered environments. The algorithm needs only to sense the positions of robots and obstacles, distinguish robots from obstacles, and respect individual dynamic limits; it does not require inter-robot communication or higher-order state derivatives.

At each planning cycle, RLSS performs best-effort A* discrete planning to find a coarse route, constructs safe corridors around that route using hard-margin support-vector-machine hyperplanes—termed linear spatial separations—and then optimizes a dynamically feasible trajectory over piecewise Bézier curves by solving a convex quadratic program. A final temporal-rescaling step enforces velocity and acceleration limits. When the resulting optimization problem is feasible, the planner guarantees collision avoidance.

The authors evaluate RLSS in simulation and on physical ground and aerial robots, including Turtlebot2, Turtlebot3, iRobot Create2, and Crazyflie 2.0 quadrotors, using onboard ODROID single-board computers and VICON tracking. Empirical tests in forest-like and maze-like environments with thousands of obstacles show that RLSS avoids deadlocks and collisions in scenarios where prior methods fail.

## Key Contributions

- A real-time decentralized multi-robot trajectory planner that requires no inter-robot communication and only position sensing plus the ability to distinguish robots from obstacles.
- A kinematically feasible convex quadratic-program formulation based on linear spatial separations that guarantees collision avoidance whenever the program is feasible.
- An extended Buffered Voronoi Cell baseline (eBVC) that handles obstacles and richer discrete linear dynamics.
- An empirical comparison of RLSS, eBVC, and RSFC in complex forest-like and maze-like environments containing thousands of obstacles.

## Relevance to Humanoid Robotics

Humanoid robot fleets deployed on shared production floors or in logistics warehouses must often navigate among humans, equipment, and each other without relying on a central planner or reliable communication links. RLSS directly addresses this need by providing a decentralized, communication-free, real-time collision-avoidance and trajectory-planning method that respects dynamic limits. The same planning machinery can in principle coordinate multiple humanoid platforms or multi-limb systems in a common workspace.

Because the planner is convex-QP-based and runs on low-power onboard computers demonstrated in the paper, it is compatible with the embedded compute constraints of humanoid robots. Its empirical success in dense, obstacle-rich environments also suggests applicability to cluttered factory floors, although its assumptions of synchronized planning and static convex obstacles will need to be relaxed for highly dynamic humanoid settings.
