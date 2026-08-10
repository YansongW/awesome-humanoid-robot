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
  zh: Occupancy-SLAM 是一种基于优化的同步定位与建图方法，由研究团队提出，核心创新在于同时优化机器人轨迹与连续占据地图，而非传统方法中先定位后建图的顺序。该方法采用 Gauss-Newton 变体求解，在仿真和公开 2D 激光数据集上，当提供较准确的初始位姿估计时，能比
    Cartographer 等现有技术更精确地估计地图与轨迹。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.10743v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (844 chars, DeepSeek).'
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
Occupancy-SLAM 将机器人位姿与占据地图的联合优化建模为一个大规模批处理优化问题，其中地图表示为连续占据场，每个 2D 点对应一个证据值。变量包括所有机器人位姿和选定离散网格节点的占据值，通过提出的 Gauss-Newton 变体求解，同时输出优化后的地图、轨迹及其不确定性。该方法属于离线算法，适用于需要高精度地图与轨迹的场合，在仿真与真实激光数据集上均优于现有技术。

## 核心内容
### 方法
- 核心创新：将机器人位姿与占据地图作为联合优化变量，打破传统 SLAM 中先定位后建图的顺序依赖。
- 地图表示：采用连续占据地图，环境中每个 2D 点对应一个连续的占据证据值，而非离散的网格概率。
- 优化问题：变量包括所有机器人位姿（pose）和选定离散网格节点（grid cell nodes）的占据值，目标函数基于激光扫描与里程计观测。

### 架构与求解
- 求解器：提出一种 Gauss-Newton 方法的变体，用于求解大规模联合优化问题，同时输出优化后的地图、轨迹及其不确定性（uncertainty）。
- 离线特性：由于采用批处理优化且变量数量庞大，算法为离线方法，适用于后处理场景。

### 实验设置
- 数据来源：仿真环境与公开可用的 2D 激光数据集（practical 2D laser datasets）。
- 初始条件：算法需要提供相对准确的初始位姿估计（initial guess）才能获得最优性能。
- 对比基准：与 Cartographer 等现有技术进行对比。

### 关键数字与结论
- 精度提升：在仿真与真实数据集上，Occupancy-SLAM 估计的地图与轨迹精度均优于现有技术。
- 收敛过程：视频展示了算法的收敛过程及与 Cartographer 的结果对比（视频链接：https://youtu.be/4oLyVEUC4iY）。
- 局限性：依赖较好的初始估计，且为离线方法，不适用于实时在线应用。

## Overview
In this paper, we propose an optimization based SLAM approach to simultaneously optimize the robot trajectory and the occupancy map using 2D laser scans (and odometry) information. The key novelty is that the robot poses and the occupancy map are optimized together, which is significantly different from existing occupancy mapping strategies where the robot poses need to be obtained first before the map can be estimated. In our formulation, the map is represented as a continuous occupancy map where each 2D point in the environment has a corresponding evidence value. The Occupancy-SLAM problem is formulated as an optimization problem where the variables include all the robot poses and the occupancy values at the selected discrete grid cell nodes. We propose a variation of Gauss-Newton method to solve this new formulated problem, obtaining the optimized occupancy map and robot trajectory together with their uncertainties. Our algorithm is an offline approach since it is based on batch optimization and the number of variables involved is large. Evaluations using simulations and publicly available practical 2D laser datasets demonstrate that the proposed approach can estimate the maps and robot trajectories more accurately than the state-of-the-art techniques, when a relatively accurate initial guess is provided to our algorithm. The video shows the convergence process of the proposed Occupancy-SLAM and comparison of results to Cartographer can be found at \url{https://youtu.be/4oLyVEUC4iY}.

## 参考
- http://arxiv.org/abs/2405.10743v1

## 개요
Occupancy-SLAM은 로봇 포즈와 점유 맵의 결합 최적화를 대규모 배치 최적화 문제로 모델링하며, 맵은 연속 점유 필드로 표현되어 각 2D 포인트가 증거 값에 대응합니다. 변수에는 모든 로봇 포즈와 선택된 이산 그리드 노드의 점유 값이 포함되며, 제안된 Gauss-Newton 변형을 통해 해결되어 최적화된 맵, 궤적 및 그 불확실성을 동시에 출력합니다. 이 방법은 오프라인 알고리즘에 속하며, 고정밀 맵과 궤적이 필요한 상황에 적합하고, 시뮬레이션 및 실제 레이저 데이터셋에서 기존 기술보다 우수합니다.

## 핵심 내용
### 방법
- 핵심 혁신: 로봇 포즈와 점유 맵을 공동 최적화 변수로 설정하여 기존 SLAM의 위치 추정 후 맵 구축 순서 의존성을 깨뜨립니다.
- 맵 표현: 연속 점유 맵을 사용하며, 환경의 각 2D 포인트는 이산 그리드 확률이 아닌 연속 점유 증거 값에 대응합니다.
- 최적화 문제: 변수에는 모든 로봇 포즈와 선택된 이산 그리드 셀 노드의 점유 값이 포함되며, 목적 함수는 레이저 스캔과 오도메트리 관측을 기반으로 합니다.

### 아키텍처 및 해법
- 솔버: 대규모 공동 최적화 문제를 해결하기 위해 Gauss-Newton 방법의 변형을 제안하며, 최적화된 맵, 궤적 및 그 불확실성을 동시에 출력합니다.
- 오프라인 특성: 배치 최적화를 사용하고 변수 수가 방대하므로, 알고리즘은 오프라인 방법으로 후처리 시나리오에 적합합니다.

### 실험 설정
- 데이터 출처: 시뮬레이션 환경과 공개적으로 사용 가능한 2D 레이저 데이터셋.
- 초기 조건: 알고리즘은 최적 성능을 위해 상대적으로 정확한 초기 포즈 추정이 필요합니다.
- 비교 기준: Cartographer 등 기존 기술과 비교합니다.

### 주요 수치 및 결론
- 정밀도 향상: 시뮬레이션 및 실제 데이터셋에서 Occupancy-SLAM이 추정한 맵과 궤적의 정밀도가 기존 기술보다 우수합니다.
- 수렴 과정: 비디오는 알고리즘의 수렴 과정과 Cartographer와의 결과 비교를 보여줍니다 (비디오 링크: https://youtu.be/4oLyVEUC4iY).
- 한계: 좋은 초기 추정에 의존하며, 오프라인 방법이므로 실시간 온라인 응용에는 적합하지 않습니다.
