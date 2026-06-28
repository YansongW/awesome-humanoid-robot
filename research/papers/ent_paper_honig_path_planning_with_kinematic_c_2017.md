---
$id: ent_paper_honig_path_planning_with_kinematic_c_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Path Planning With Kinematic Constraints For Robot Groups
  zh: 机器人群组运动学约束路径规划
  ko: 운동학적 제약을 고려한 로봇 그룹 경로 계획
summary:
  en: Presents a Simple Temporal Network postprocessing framework that converts discrete
    MAPF/TAPF plans into kinematically feasible trajectories while enforcing a minimum
    safety distance between robots, validated in simulation and on real robots.
  zh: 提出一种基于简单时间网络的后处理框架，将离散MAPF/TAPF规划结果转换为满足运动学约束的轨迹，并保证机器人之间的最小安全距离，已在仿真和真实机器人上验证。
  ko: 이산화된 MAPF/TAPF 계획을 운동학적으로 실행 가능한 궤적으로 변환하면서 로봇 간 최소 안전 거리를 보장하는 단순 시간 네트워크 기반
    후처리 프레임워크를 제시하고 시뮬레이션 및 실제 로봇으로 검증한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- multi_robot_path_planning
- kinematic_constraints
- simple_temporal_networks
- collision_avoidance
- safety_distance
- mapf
- tapf
- warehouse_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    full paper before full verification.
sources:
- id: src_001
  type: paper
  title: Path Planning With Kinematic Constraints For Robot Groups
  url: https://arxiv.org/abs/1704.07538
  date: '2017'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Multi-robot path planning on discretized environments is commonly solved using MAPF (Multi-Agent Path Finding) or TAPF (Target-Assignment and Path-Finding) solvers. However, these solvers typically produce abstract, time-stepped paths that ignore kinematic constraints such as velocity limits, acceleration limits, and minimum safety distances between physical robots. This paper addresses the gap by presenting a postprocessing framework based on Simple Temporal Networks (STNs) that takes a discrete solver output and converts it into continuous-time, kinematically feasible trajectories.

The core idea is to represent the discrete plan as a Temporal Plan Graph, where nodes correspond to events such as robots entering or leaving grid cells, and edges encode temporal constraints derived from the robots' kinematic limits. Additional "safety-marker" events are inserted to guarantee that any two robots maintain at least a user-specified minimum distance at all times. The resulting STN is solved to obtain executable arrival and departure times for each event, yielding a collision-free trajectory set.

The authors evaluate their approach on randomly generated 10×10×5 grid maps and a warehouse-like multi-robot domain with up to 100 robots. They validate the method both in V-REP simulation and on physical iRobot Create2 differential-drive robots, and they also discuss extensions to 6-legged robots and quadcopters in 3D environments.

## Key Contributions

- STN-based postprocessing framework for enforcing kinematic constraints on MAPF/TAPF solutions.
- Temporal Plan Graph augmented with safety-marker events to guarantee a user-specified minimum robot-robot separation.
- Empirical scalability evaluation on warehouse-like domains with up to 100 robots.
- Validation in V-REP simulation and on physical iRobot Create2 robots.

## Relevance to Humanoid Robotics

Although the paper does not explicitly study humanoid robots, its coordination framework is directly applicable to fleets of humanoid robots operating in shared industrial or warehouse workspaces. Enforcing kinematic constraints and minimum safety distances between multiple robots is a foundational requirement for any multi-humanoid deployment where robots must navigate among humans, machinery, and each other without collisions. The STN-based timing model provides a principled way to convert high-level discrete plans into executable continuous trajectories, which is equally relevant to bipedal humanoid locomotion as it is to differential-drive or aerial platforms.
