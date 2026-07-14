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
  en: Presents a Simple Temporal Network postprocessing framework that converts discrete MAPF/TAPF plans into kinematically
    feasible trajectories while enforcing a minimum safety distance between robots, validated in simulation and on real robots.
  zh: 提出一种基于简单时间网络的后处理框架，将离散MAPF/TAPF规划结果转换为满足运动学约束的轨迹，并保证机器人之间的最小安全距离，已在仿真和真实机器人上验证。
  ko: 이산화된 MAPF/TAPF 계획을 운동학적으로 실행 가능한 궤적으로 변환하면서 로봇 간 최소 안전 거리를 보장하는 단순 시간 네트워크 기반 후처리 프레임워크를 제시하고 시뮬레이션 및 실제 로봇으로 검증한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1704.07538v1.
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
## 概述
Path planning for multiple robots is well studied in the AI and robotics communities. For a given discretized environment, robots need to find collision-free paths to a set of specified goal locations. Robots can be fully anonymous, non-anonymous, or organized in groups. Although powerful solvers for this abstract problem exist, they make simplifying assumptions by ignoring kinematic constraints, making it difficult to use the resulting plans on actual robots. In this paper, we present a solution which takes kinematic constraints, such as maximum velocities, into account, while guaranteeing a user-specified minimum safety distance between robots. We demonstrate our approach in simulation and on real robots in 2D and 3D environments.

## 核心内容
Path planning for multiple robots is well studied in the AI and robotics communities. For a given discretized environment, robots need to find collision-free paths to a set of specified goal locations. Robots can be fully anonymous, non-anonymous, or organized in groups. Although powerful solvers for this abstract problem exist, they make simplifying assumptions by ignoring kinematic constraints, making it difficult to use the resulting plans on actual robots. In this paper, we present a solution which takes kinematic constraints, such as maximum velocities, into account, while guaranteeing a user-specified minimum safety distance between robots. We demonstrate our approach in simulation and on real robots in 2D and 3D environments.

## 参考
- http://arxiv.org/abs/1704.07538v1

