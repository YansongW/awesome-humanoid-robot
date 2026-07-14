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
  en: Lauri and Ritala formulate robotic exploration as a POMDP with a mutual-information reward and solve it using open-loop
    forward-simulation planning, introducing a sample-based mutual-information approximation that integrates with such planners;
    they combine the approach with frontier-based exploration and evaluate it in simulated and real indoor environments.
  zh: Lauri与Ritala将机器人探索问题建模为以互信息为奖励的部分可观测马尔可夫决策过程（POMDP），并采用开环前向仿真规划求解，提出了一种可与前向仿真规划器结合使用的基于样本的互信息近似方法；他们将该方法与基于边界的探索相结合，并在仿真与真实室内环境中进行了评估。
  ko: Lauri와 Ritala는 로봇 탐사를 상호 정보량 보상을 갖는 POMDP로 공식화하고 개루프 전방 시뮬레이션 계획을 사용하여 풀며, 이러한 계획기와 통합할 수 있는 표본 기반 상호 정보량 근사법을 제안한다;
    이들은 접근법을 경계 기반 탐사와 결합하고 시뮬레이션 및 실제 실내 환경에서 평가한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1502.02474v2.
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
## 概述
We address the problem of controlling a mobile robot to explore a partially known environment. The robot's objective is the maximization of the amount of information collected about the environment. We formulate the problem as a partially observable Markov decision process (POMDP) with an information-theoretic objective function, and solve it applying forward simulation algorithms with an open-loop approximation. We present a new sample-based approximation for mutual information useful in mobile robotics. The approximation can be seamlessly integrated with forward simulation planning algorithms. We investigate the usefulness of POMDP based planning for exploration, and to alleviate some of its weaknesses propose a combination with frontier based exploration. Experimental results in simulated and real environments show that, depending on the environment, applying POMDP based planning for exploration can improve performance over frontier exploration.

## 核心内容
We address the problem of controlling a mobile robot to explore a partially known environment. The robot's objective is the maximization of the amount of information collected about the environment. We formulate the problem as a partially observable Markov decision process (POMDP) with an information-theoretic objective function, and solve it applying forward simulation algorithms with an open-loop approximation. We present a new sample-based approximation for mutual information useful in mobile robotics. The approximation can be seamlessly integrated with forward simulation planning algorithms. We investigate the usefulness of POMDP based planning for exploration, and to alleviate some of its weaknesses propose a combination with frontier based exploration. Experimental results in simulated and real environments show that, depending on the environment, applying POMDP based planning for exploration can improve performance over frontier exploration.

## 参考
- http://arxiv.org/abs/1502.02474v2

