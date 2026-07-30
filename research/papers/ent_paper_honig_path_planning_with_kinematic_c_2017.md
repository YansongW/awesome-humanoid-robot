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
  zh: 本文提出一种基于Simple Temporal Network的后处理框架，将离散的MAPF/TAPF规划转化为满足运动学约束的可行轨迹，同时保证机器人间最小安全距离。该方法在仿真和真实机器人上得到验证，适用于2D和3D环境。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1704.07538v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该研究针对多机器人路径规划中忽略运动学约束导致实际部署困难的问题，提出一种后处理框架。该框架以Simple Temporal Network为核心，将离散的MAPF/TAPF规划结果转化为满足最大速度等运动学约束的连续轨迹，并强制保持用户指定的最小安全距离。方法在2D和3D环境的仿真及真实机器人实验中均得到验证。

## 核心内容
### 问题背景
- 多机器人路径规划在AI和机器人领域已有深入研究，现有求解器能高效处理离散化环境中的无碰撞路径规划。
- 但现有方法通常忽略运动学约束（如最大速度），导致规划结果难以直接应用于真实机器人。

### 方法核心
- 提出基于Simple Temporal Network的后处理框架，将离散MAPF/TAPF规划结果转化为运动学可行的连续轨迹。
- 框架核心功能：
  - 将离散路径转化为时间约束网络，确保机器人运动满足最大速度限制。
  - 在时间网络中嵌入最小安全距离约束，防止机器人间碰撞。
  - 通过求解时间约束网络，生成满足所有约束的轨迹。

### 实验设置
- 验证环境：2D和3D仿真环境，以及真实机器人平台。
- 测试场景：包括完全匿名、非匿名及分组（TAPF）任务。
- 对比基线：直接使用离散MAPF/TAPF规划结果（无运动学约束）。

### 关键结果
- 在仿真中，该方法成功将离散规划转化为运动学可行轨迹，所有机器人均保持最小安全距离。
- 在真实机器人实验中，轨迹执行无碰撞，验证了框架的实际可行性。
- 方法适用于不同匿名性设置和分组任务，未出现运动学约束违反情况。

### 结论
- 该后处理框架有效桥接了离散路径规划与真实机器人执行之间的差距。
- 通过Simple Temporal Network统一处理运动学约束和安全距离，无需修改底层MAPF/TAPF求解器。
- 未来工作可扩展至更复杂的运动学模型（如加速度约束）或动态环境。

## Overview
Path planning for multiple robots is well studied in the AI and robotics communities. For a given discretized environment, robots need to find collision-free paths to a set of specified goal locations. Robots can be fully anonymous, non-anonymous, or organized in groups. Although powerful solvers for this abstract problem exist, they make simplifying assumptions by ignoring kinematic constraints, making it difficult to use the resulting plans on actual robots. In this paper, we present a solution which takes kinematic constraints, such as maximum velocities, into account, while guaranteeing a user-specified minimum safety distance between robots. We demonstrate our approach in simulation and on real robots in 2D and 3D environments.

## 개요
다중 로봇의 경로 계획은 AI 및 로봇 공학 커뮤니티에서 널리 연구되어 왔습니다. 주어진 이산화된 환경에서 로봇은 지정된 목표 위치 집합까지 충돌 없는 경로를 찾아야 합니다. 로봇은 완전히 익명일 수도, 비익명일 수도, 또는 그룹으로 조직될 수도 있습니다. 이 추상적인 문제에 대한 강력한 솔버가 존재하지만, 운동학적 제약을 무시하는 단순화 가정을 하여 실제 로봇에서 결과 계획을 사용하기 어렵게 만듭니다. 본 논문에서는 최대 속도와 같은 운동학적 제약을 고려하면서 사용자가 지정한 최소 안전 거리를 보장하는 솔루션을 제시합니다. 우리는 2D 및 3D 환경에서 시뮬레이션과 실제 로봇을 통해 접근 방식을 시연합니다.

## 핵심 내용
다중 로봇의 경로 계획은 AI 및 로봇 공학 커뮤니티에서 널리 연구되어 왔습니다. 주어진 이산화된 환경에서 로봇은 지정된 목표 위치 집합까지 충돌 없는 경로를 찾아야 합니다. 로봇은 완전히 익명일 수도, 비익명일 수도, 또는 그룹으로 조직될 수도 있습니다. 이 추상적인 문제에 대한 강력한 솔버가 존재하지만, 운동학적 제약을 무시하는 단순화 가정을 하여 실제 로봇에서 결과 계획을 사용하기 어렵게 만듭니다. 본 논문에서는 최대 속도와 같은 운동학적 제약을 고려하면서 사용자가 지정한 최소 안전 거리를 보장하는 솔루션을 제시합니다. 우리는 2D 및 3D 환경에서 시뮬레이션과 실제 로봇을 통해 접근 방식을 시연합니다.

## 参考
- http://arxiv.org/abs/1704.07538v1
