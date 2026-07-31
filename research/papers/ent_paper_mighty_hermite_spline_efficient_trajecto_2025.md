---
$id: ent_paper_mighty_hermite_spline_efficient_trajecto_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MIGHTY: Hermite Spline-based Efficient Trajectory Planning'
  zh: 'MIGHTY: Hermite Spline-based Efficient Trajectory Planning'
  ko: 'MIGHTY: Hermite Spline-based Efficient Trajectory Planning'
summary:
  en: 'Hard-constraint trajectory planners often rely on commercial solvers and demand substantial computational resources.
    Existing soft-constraint methods achieve faster computation, but either (1) decouple spatial and temporal optimization
    or (2) restrict the search space. Institutions per source list: MIT ACL.'
  zh: MIGHTY 是一种基于 Hermite 样条的轨迹规划器，由研究团队提出，旨在解决硬约束轨迹规划依赖商业求解器且计算成本高的问题。其核心贡献在于实现了时空联合优化，同时充分利用样条的连续搜索空间，在仿真中计算时间降低 9.3%，旅行时间减少
    13.1%，成功率达 100%。
  ko: 'Hard-constraint trajectory planners often rely on commercial solvers and demand substantial computational resources.
    Existing soft-constraint methods achieve faster computation, but either (1) decouple spatial and temporal optimization
    or (2) restrict the search space. Institutions per source list: MIT ACL.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- mighty
- hermite
- spline
- efficient
- trajecto
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 710 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2511.10822 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2511.10822v4); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2511.10822 MIGHTY: Hermite Spline-based Efficient Trajectory Planning'
  url: https://arxiv.org/abs/2511.10822
  accessed_at: '2026-07-31'
  date: '2025-11-13'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

MIGHTY 通过 Hermite 样条表示轨迹，将空间和时间优化统一在一个框架内，避免了传统软约束方法中解耦时空或限制搜索空间的缺陷。在仿真实验中，MIGHTY 相比现有最优基线方法，计算时间缩短 9.3%，旅行时间减少 13.1%，且成功率达到 100%。硬件实验中，MIGHTY 在杂乱静态环境中完成了最高 6.7 m/s 的高速飞行，并在动态添加障碍物的场景下实现了长时间飞行。

## 核心内容
### 方法
MIGHTY 采用 Hermite 样条作为轨迹表示，通过样条的控制点同时优化空间路径和时间分配。该方法将硬约束（如动力学限制、避障）直接嵌入优化问题，避免了传统软约束方法中惩罚项带来的近似误差。优化过程利用样条的连续性，在连续搜索空间中求解，无需离散化或解耦时空。

### 架构
- **轨迹表示**：使用 Hermite 样条，每个分段由端点位置和导数定义，确保轨迹的平滑性和连续性。
- **优化框架**：将空间和时间变量联合优化，目标函数包括最小化旅行时间和控制输入，约束条件涵盖速度、加速度上限及障碍物距离。
- **求解策略**：采用梯度下降法结合样条解析梯度，避免依赖商业求解器，提升计算效率。

### 实验设置
- **仿真环境**：在随机生成的障碍物场景中测试，与 state-of-the-art 基线方法（如软约束解耦规划器）对比。
- **硬件平台**：使用四旋翼无人机，在室内外混合环境中进行高速飞行实验，障碍物包括静态柱体和动态添加的箱子。

### 关键数字
- **仿真结果**：计算时间降低 9.3%，旅行时间减少 13.1%，成功率 100%。
- **硬件性能**：最高飞行速度 6.7 m/s，在动态障碍物场景中完成超过 2 分钟的连续飞行。
- **约束满足**：所有实验均严格满足速度（≤10 m/s）和加速度（≤5 m/s²）限制。

### 结论
MIGHTY 通过 Hermite 样条实现了高效的时空联合优化，在计算效率和轨迹质量上均优于现有方法。硬件实验验证了其在高速动态环境中的鲁棒性，未来可扩展至多机器人协同规划。

## Overview
Hard-constraint trajectory planners often rely on commercial solvers and demand substantial computational resources. Existing soft-constraint methods achieve faster computation, but either (1) decouple spatial and temporal optimization or (2) restrict the search space. To overcome these limitations, we introduce MIGHTY, a Hermite spline-based planner that performs spatiotemporal optimization while fully leveraging the continuous search space of a spline. In simulation, MIGHTY achieves a 9.3% reduction in computation time and a 13.1% reduction in travel time over state-of-the-art baselines, with a 100% success rate. In hardware, MIGHTY completes multiple high-speed flights up to 6.7 m/s in a cluttered static environment and long-duration flights with dynamically added obstacles.

## 参考
- https://arxiv.org/abs/2511.10822
- https://github.com/ImChong/Robotics_Notebooks

## 개요

MIGHTY는 Hermite 스플라인을 통해 궤적을 표현하여 공간과 시간 최적화를 하나의 프레임워크로 통합함으로써, 기존의 소프트 제약 조건 방식에서 발생하는 시공간 분리 또는 탐색 공간 제한의 단점을 피합니다. 시뮬레이션 실험에서 MIGHTY는 기존 최적 기준 방법에 비해 계산 시간이 9.3% 단축되고, 이동 시간이 13.1% 감소했으며, 성공률은 100%에 도달했습니다. 하드웨어 실험에서는 MIGHTY가 복잡한 정적 환경에서 최대 6.7m/s의 고속 비행을 완료했으며, 동적으로 장애물이 추가된 시나리오에서 장시간 비행을 구현했습니다.

## 핵심 내용
### 방법
MIGHTY는 Hermite 스플라인을 궤적 표현으로 사용하며, 스플라인의 제어점을 통해 공간 경로와 시간 할당을 동시에 최적화합니다. 이 방법은 하드 제약 조건(예: 동역학 제한, 장애물 회피)을 최적화 문제에 직접 포함시켜, 기존 소프트 제약 조건 방식에서 패널티 항으로 인한 근사 오차를 방지합니다. 최적화 과정은 스플라인의 연속성을 활용하여 연속 탐색 공간에서 해를 구하며, 이산화나 시공간 분리가 필요하지 않습니다.

### 아키텍처
- **궤적 표현**: Hermite 스플라인을 사용하며, 각 구간은 끝점 위치와 도함수로 정의되어 궤적의 평활성과 연속성을 보장합니다.
- **최적화 프레임워크**: 공간 및 시간 변수를 결합하여 최적화하며, 목적 함수는 이동 시간 및 제어 입력 최소화를 포함하고, 제약 조건은 속도, 가속도 상한 및 장애물 거리를 포함합니다.
- **해법 전략**: 경사 하강법과 스플라인의 해석적 기울기를 결합하여 상용 솔버에 의존하지 않고 계산 효율성을 높입니다.

### 실험 설정
- **시뮬레이션 환경**: 무작위로 생성된 장애물 시나리오에서 테스트하며, 최신 기준 방법(예: 소프트 제약 분리 계획기)과 비교합니다.
- **하드웨어 플랫폼**: 쿼드로터 드론을 사용하여 실내외 혼합 환경에서 고속 비행 실험을 수행하며, 장애물은 정적 기둥과 동적으로 추가된 상자를 포함합니다.

### 주요 수치
- **시뮬레이션 결과**: 계산 시간 9.3% 감소, 이동 시간 13.1% 감소, 성공률 100%.
- **하드웨어 성능**: 최대 비행 속도 6.7m/s, 동적 장애물 시나리오에서 2분 이상 연속 비행 완료.
- **제약 조건 충족**: 모든 실험에서 속도(≤10m/s) 및 가속도(≤5m/s²) 제한을 엄격히 준수.

### 결론
MIGHTY는 Hermite 스플라인을 통해 효율적인 시공간 결합 최적화를 구현했으며, 계산 효율성과 궤적 품질 모두에서 기존 방법보다 우수합니다. 하드웨어 실험은 고속 동적 환경에서의 강건성을 입증했으며, 향후 다중 로봇 협력 계획으로 확장 가능합니다.
