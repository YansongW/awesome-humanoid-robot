---
$id: ent_paper_zhao_occupancy_slam_simultaneously_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Occupancy-SLAM: Simultaneously Optimizing Robot Poses and Continuous Occupancy Map'
  zh: Occupancy-SLAM：同时优化机器人位姿与连续占用地图
  ko: 'Occupancy-SLAM: 로봇 포즈와 연속 점유 지도를 동시에 최적화'
summary:
  en: An optimization-based SLAM approach that jointly optimizes robot trajectory and a continuous occupancy map from 2D laser
    scans and odometry using a Gauss-Newton variant.
  zh: In this paper, we propose an optimization based SLAM approach to simultaneously optimize the robot trajectory and the
    occupancy map using 2D laser scans (and odometry) information. The key novelty is that the robot poses and the occupancy
    map are optimized together, which is significantly different from existing occupancy mapping strategies where the robot
    poses need to be obtained first before the map can be estimated. In our formulation, the map is represented as a continuous
    occupancy map where each 2D point in the environment has a corresponding evidence value. The Occupancy-SLAM problem i
  ko: 가우스-뉴턴 변형을 사용하여 2D 레이저 스캔과 주행거리계 정보로부터 로봇 궤적과 연속 점유 지도를 동시에 최적화하는 SLAM 접근법.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- slam
- occupancy_mapping
- laser_scan
- gauss_newton
- pose_estimation
- robot_navigation
- indoor_mapping
- batch_optimization
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.10743v1.
sources:
- id: src_001
  type: paper
  title: 'Occupancy-SLAM: Simultaneously Optimizing Robot Poses and Continuous Occupancy Map'
  url: https://arxiv.org/abs/2405.10743
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## 概述
In this paper, we propose an optimization based SLAM approach to simultaneously optimize the robot trajectory and the occupancy map using 2D laser scans (and odometry) information. The key novelty is that the robot poses and the occupancy map are optimized together, which is significantly different from existing occupancy mapping strategies where the robot poses need to be obtained first before the map can be estimated. In our formulation, the map is represented as a continuous occupancy map where each 2D point in the environment has a corresponding evidence value. The Occupancy-SLAM problem is formulated as an optimization problem where the variables include all the robot poses and the occupancy values at the selected discrete grid cell nodes. We propose a variation of Gauss-Newton method to solve this new formulated problem, obtaining the optimized occupancy map and robot trajectory together with their uncertainties. Our algorithm is an offline approach since it is based on batch optimization and the number of variables involved is large. Evaluations using simulations and publicly available practical 2D laser datasets demonstrate that the proposed approach can estimate the maps and robot trajectories more accurately than the state-of-the-art techniques, when a relatively accurate initial guess is provided to our algorithm. The video shows the convergence process of the proposed Occupancy-SLAM and comparison of results to Cartographer can be found at \url{https://youtu.be/4oLyVEUC4iY}.

## 核心内容
In this paper, we propose an optimization based SLAM approach to simultaneously optimize the robot trajectory and the occupancy map using 2D laser scans (and odometry) information. The key novelty is that the robot poses and the occupancy map are optimized together, which is significantly different from existing occupancy mapping strategies where the robot poses need to be obtained first before the map can be estimated. In our formulation, the map is represented as a continuous occupancy map where each 2D point in the environment has a corresponding evidence value. The Occupancy-SLAM problem is formulated as an optimization problem where the variables include all the robot poses and the occupancy values at the selected discrete grid cell nodes. We propose a variation of Gauss-Newton method to solve this new formulated problem, obtaining the optimized occupancy map and robot trajectory together with their uncertainties. Our algorithm is an offline approach since it is based on batch optimization and the number of variables involved is large. Evaluations using simulations and publicly available practical 2D laser datasets demonstrate that the proposed approach can estimate the maps and robot trajectories more accurately than the state-of-the-art techniques, when a relatively accurate initial guess is provided to our algorithm. The video shows the convergence process of the proposed Occupancy-SLAM and comparison of results to Cartographer can be found at \url{https://youtu.be/4oLyVEUC4iY}.

## 参考
- http://arxiv.org/abs/2405.10743v1

## Overview
In this paper, we propose an optimization based SLAM approach to simultaneously optimize the robot trajectory and the occupancy map using 2D laser scans (and odometry) information. The key novelty is that the robot poses and the occupancy map are optimized together, which is significantly different from existing occupancy mapping strategies where the robot poses need to be obtained first before the map can be estimated. In our formulation, the map is represented as a continuous occupancy map where each 2D point in the environment has a corresponding evidence value. The Occupancy-SLAM problem is formulated as an optimization problem where the variables include all the robot poses and the occupancy values at the selected discrete grid cell nodes. We propose a variation of Gauss-Newton method to solve this new formulated problem, obtaining the optimized occupancy map and robot trajectory together with their uncertainties. Our algorithm is an offline approach since it is based on batch optimization and the number of variables involved is large. Evaluations using simulations and publicly available practical 2D laser datasets demonstrate that the proposed approach can estimate the maps and robot trajectories more accurately than the state-of-the-art techniques, when a relatively accurate initial guess is provided to our algorithm. The video shows the convergence process of the proposed Occupancy-SLAM and comparison of results to Cartographer can be found at \url{https://youtu.be/4oLyVEUC4iY}.

## Content
In this paper, we propose an optimization based SLAM approach to simultaneously optimize the robot trajectory and the occupancy map using 2D laser scans (and odometry) information. The key novelty is that the robot poses and the occupancy map are optimized together, which is significantly different from existing occupancy mapping strategies where the robot poses need to be obtained first before the map can be estimated. In our formulation, the map is represented as a continuous occupancy map where each 2D point in the environment has a corresponding evidence value. The Occupancy-SLAM problem is formulated as an optimization problem where the variables include all the robot poses and the occupancy values at the selected discrete grid cell nodes. We propose a variation of Gauss-Newton method to solve this new formulated problem, obtaining the optimized occupancy map and robot trajectory together with their uncertainties. Our algorithm is an offline approach since it is based on batch optimization and the number of variables involved is large. Evaluations using simulations and publicly available practical 2D laser datasets demonstrate that the proposed approach can estimate the maps and robot trajectories more accurately than the state-of-the-art techniques, when a relatively accurate initial guess is provided to our algorithm. The video shows the convergence process of the proposed Occupancy-SLAM and comparison of results to Cartographer can be found at \url{https://youtu.be/4oLyVEUC4iY}.

## 개요
본 논문에서는 2D 레이저 스캔(및 오도메트리) 정보를 사용하여 로봇 궤적과 점유 지도를 동시에 최적화하는 최적화 기반 SLAM 접근법을 제안합니다. 핵심 혁신은 로봇 자세와 점유 지도가 함께 최적화된다는 점으로, 이는 지도를 추정하기 전에 로봇 자세를 먼저 얻어야 하는 기존 점유 지도 작성 전략과 크게 다릅니다. 본 공식에서 지도는 환경의 각 2D 지점이 해당 증거 값을 갖는 연속 점유 지도로 표현됩니다. 점유-SLAM 문제는 변수에 모든 로봇 자세와 선택된 이산 격자 셀 노드의 점유 값을 포함하는 최적화 문제로 공식화됩니다. 우리는 이 새롭게 공식화된 문제를 해결하기 위해 가우스-뉴턴 방법의 변형을 제안하며, 최적화된 점유 지도와 로봇 궤적 및 그 불확실성을 함께 얻습니다. 본 알고리즘은 배치 최적화를 기반으로 하고 관련 변수 수가 많기 때문에 오프라인 접근법입니다. 시뮬레이션과 공개적으로 이용 가능한 실제 2D 레이저 데이터셋을 사용한 평가는, 상대적으로 정확한 초기 추정치가 제공될 때 제안된 접근법이 최신 기술보다 지도와 로봇 궤적을 더 정확하게 추정할 수 있음을 보여줍니다. 비디오는 제안된 점유-SLAM의 수렴 과정과 Cartographer와의 결과 비교를 보여주며, \url{https://youtu.be/4oLyVEUC4iY}에서 확인할 수 있습니다.

## 핵심 내용
본 논문에서는 2D 레이저 스캔(및 오도메트리) 정보를 사용하여 로봇 궤적과 점유 지도를 동시에 최적화하는 최적화 기반 SLAM 접근법을 제안합니다. 핵심 혁신은 로봇 자세와 점유 지도가 함께 최적화된다는 점으로, 이는 지도를 추정하기 전에 로봇 자세를 먼저 얻어야 하는 기존 점유 지도 작성 전략과 크게 다릅니다. 본 공식에서 지도는 환경의 각 2D 지점이 해당 증거 값을 갖는 연속 점유 지도로 표현됩니다. 점유-SLAM 문제는 변수에 모든 로봇 자세와 선택된 이산 격자 셀 노드의 점유 값을 포함하는 최적화 문제로 공식화됩니다. 우리는 이 새롭게 공식화된 문제를 해결하기 위해 가우스-뉴턴 방법의 변형을 제안하며, 최적화된 점유 지도와 로봇 궤적 및 그 불확실성을 함께 얻습니다. 본 알고리즘은 배치 최적화를 기반으로 하고 관련 변수 수가 많기 때문에 오프라인 접근법입니다. 시뮬레이션과 공개적으로 이용 가능한 실제 2D 레이저 데이터셋을 사용한 평가는, 상대적으로 정확한 초기 추정치가 제공될 때 제안된 접근법이 최신 기술보다 지도와 로봇 궤적을 더 정확하게 추정할 수 있음을 보여줍니다. 비디오는 제안된 점유-SLAM의 수렴 과정과 Cartographer와의 결과 비교를 보여주며, \url{https://youtu.be/4oLyVEUC4iY}에서 확인할 수 있습니다.
