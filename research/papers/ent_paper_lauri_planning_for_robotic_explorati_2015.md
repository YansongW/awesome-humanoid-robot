---
$id: ent_paper_lauri_planning_for_robotic_explorati_2015
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Planning for robotic exploration based on forward simulation
  zh: 基于前向仿真的机器人探索规划
  ko: 전방 시뮬레이션 기반 로봇 탐사 계획
summary:
  en: Lauri and Ritala formulate robotic exploration as a POMDP with a mutual-information
    reward and solve it using open-loop forward-simulation planning, introducing a
    sample-based mutual-information approximation that integrates with such planners;
    they combine the approach with frontier-based exploration and evaluate it in simulated
    and real indoor environments.
  zh: Lauri与Ritala将机器人探索问题建模为以互信息为奖励的部分可观测马尔可夫决策过程（POMDP），并采用开环前向仿真规划求解，提出了一种可与前向仿真规划器结合使用的基于样本的互信息近似方法；他们将该方法与基于边界的探索相结合，并在仿真与真实室内环境中进行了评估。
  ko: Lauri와 Ritala는 로봇 탐사를 상호 정보량 보상을 갖는 POMDP로 공식화하고 개루프 전방 시뮬레이션 계획을 사용하여 풀며, 이러한
    계획기와 통합할 수 있는 표본 기반 상호 정보량 근사법을 제안한다; 이들은 접근법을 경계 기반 탐사와 결합하고 시뮬레이션 및 실제 실내 환경에서
    평가한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- exploration_planning
- pomdp
- mutual_information
- forward_simulation
- open_loop_planning
- frontier_based_exploration
- occupancy_grid
- rbpf_slam
- mobile_robotics
- information_theoretic
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the arXiv PDF; metadata and core claims match the published
    abstract and body, but hardware details and exact benchmark names require human
    cross-check before full verification.
sources:
- id: src_001
  type: paper
  title: Planning for robotic exploration based on forward simulation
  url: https://arxiv.org/abs/1502.02474
  date: '2015'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Lauri and Ritala address the problem of controlling a mobile robot to explore a partially known environment. They formulate exploration as a partially observable Markov decision process (POMDP) whose objective is to maximize the expected information collected about the environment. Because exact POMDP solutions are computationally intractable, they solve an open-loop approximation of the POMDP using forward-simulation planners.

The authors derive a new sample-based approximation of mutual information that can be computed without running full SLAM filter updates during planning. This approximation is designed for occupancy-grid representations and ray-traced observations from a laser range finder, and it is compatible with forward-simulation algorithms such as POMCP and sequential Monte Carlo planning. They also propose a hybrid strategy that falls back to frontier-based exploration when the POMDP planner gets stuck.

The approach is implemented in ROS with the Stage simulator for simulation studies and is transferred to a real robot equipped with a laser range finder. Experiments are reported in simulated maze, office, and outdoor environments, as well as in a real campus library, comparing the POMDP planner against frontier exploration.

## Key Contributions

- A sample-based approximation for mutual information that couples with forward-simulation planners without requiring full SLAM updates during planning.
- A POMDP-based non-myopic exploration method solved via open-loop forward simulation.
- A combination of POMDP-based exploration with frontier-based exploration to mitigate local minima.
- Empirical validation in simulated maze, office, and outdoor environments plus a real-world library trial.

## Relevance to Humanoid Robotics

Autonomous exploration and information-theoretic mapping are core capabilities for humanoid robots deployed in unstructured or semi-structured facilities such as factories or warehouses. The POMDP formulation and the sample-based mutual-information approximation provide a principled way to plan information-gathering actions under partial observability, which is directly applicable to humanoid navigation, site survey, and mapping tasks. The frontier fallback strategy also offers a practical way to scale non-myopic planning to large open areas where a finite-horizon POMDP planner could otherwise get trapped.
