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
  zh: 'Trajectory planning for multiple robots in shared environments is a challenging problem especially when there is limited
    communication available or no central entity. In this article, we present Real-time planning using Linear Spatial Separations,
    or RLSS: a real-time decentralized trajectory planning algorithm for cooperative multi-robot teams in static environments.
    The algorithm requires relatively few robot capabilities, namely sensing the positions of robots and obstacles without
    higher-order derivatives and the ability of distinguishing robots from obstacles. There is no communication re'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2302.12863v2.
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
Trajectory planning for multiple robots in shared environments is a challenging problem especially when there is limited communication available or no central entity. In this article, we present Real-time planning using Linear Spatial Separations, or RLSS: a real-time decentralized trajectory planning algorithm for cooperative multi-robot teams in static environments. The algorithm requires relatively few robot capabilities, namely sensing the positions of robots and obstacles without higher-order derivatives and the ability of distinguishing robots from obstacles. There is no communication requirement and the robots' dynamic limits are taken into account. RLSS generates and solves convex quadratic optimization problems that are kinematically feasible and guarantees collision avoidance if the resulting problems are feasible. We demonstrate the algorithm's performance in real-time in simulations and on physical robots. We compare RLSS to two state-of-the-art planners and show empirically that RLSS does avoid deadlocks and collisions in forest-like and maze-like environments, significantly improving prior work, which result in collisions and deadlocks in such environments.

## 核心内容
Trajectory planning for multiple robots in shared environments is a challenging problem especially when there is limited communication available or no central entity. In this article, we present Real-time planning using Linear Spatial Separations, or RLSS: a real-time decentralized trajectory planning algorithm for cooperative multi-robot teams in static environments. The algorithm requires relatively few robot capabilities, namely sensing the positions of robots and obstacles without higher-order derivatives and the ability of distinguishing robots from obstacles. There is no communication requirement and the robots' dynamic limits are taken into account. RLSS generates and solves convex quadratic optimization problems that are kinematically feasible and guarantees collision avoidance if the resulting problems are feasible. We demonstrate the algorithm's performance in real-time in simulations and on physical robots. We compare RLSS to two state-of-the-art planners and show empirically that RLSS does avoid deadlocks and collisions in forest-like and maze-like environments, significantly improving prior work, which result in collisions and deadlocks in such environments.

## 参考
- http://arxiv.org/abs/2302.12863v2


