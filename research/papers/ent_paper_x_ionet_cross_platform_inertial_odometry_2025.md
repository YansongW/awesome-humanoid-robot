---
$id: ent_paper_x_ionet_cross_platform_inertial_odometry_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'X-IONet: Cross-Platform Inertial Odometry Network for Pedestrian and Legged Robot'
  zh: 'X-IONet: Cross-Platform Inertial Odometry Network for Pedestrian and Legged Robot'
  ko: 'X-IONet: Cross-Platform Inertial Odometry Network for Pedestrian and Legged Robot'
summary:
  en: 'Learning-based inertial odometry has achieved remarkable progress in pedestrian navigation. However, extending these
    methods to quadruped robots remains challenging due to their distinct and highly dynamic motion patterns. Institutions
    per source list: 香港科技大学（广州）智能交通 Thrust、HKUST 新兴交叉学科部.'
  zh: X-IONet 是一个跨平台惯性里程计框架，由研究团队提出，仅使用单个 IMU 即可在行人与四足机器人平台上实现高精度导航。其核心贡献在于引入基于规则的专家选择模块与双阶段注意力架构，并结合 Extended Kalman Filter
    (EKF) 进行鲁棒状态估计，在多个数据集上显著降低了轨迹误差。
  ko: 'Learning-based inertial odometry has achieved remarkable progress in pedestrian navigation. However, extending these
    methods to quadruped robots remains challenging due to their distinct and highly dynamic motion patterns. Institutions
    per source list: 香港科技大学（广州）智能交通 Thrust、HKUST 新兴交叉学科部.'
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
- x
- ionet
- cross
- platform
- inertial
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 833 (.staging/ingest_yuanxq). Tier C->full. arXiv id 2511.08277 recovered
    programmatically (strict title match/page scan). Title guard: substring (score 1.0). Abstract and metadata from arXiv
    API (2511.08277v2); zh content by DeepSeek from the abstract. Institutions as given in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2511.08277 X-IONet: Cross-Platform Inertial Odometry Network for Pedestrian and Legged Robot'
  url: https://arxiv.org/abs/2511.08277
  accessed_at: '2026-07-31'
  date: '2025-11-11'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

X-IONet 针对现有惯性里程计方法难以泛化至四足机器人高动态运动模式的问题，设计了一种跨平台解决方案。该框架通过规则驱动的专家选择模块自动识别运动平台类型，并将 IMU 序列路由至对应的专家网络。位移预测网络采用双阶段注意力机制，同时建模长程时间依赖与轴间相关性，输出位移及其不确定性。这些输出随后通过 Extended Kalman Filter (EKF) 融合，实现鲁棒的状态估计。在 RoNIN、GrandTour 及自采集 Go2 数据集上的实验表明，X-IONet 在绝对轨迹误差 (ATE) 和相对轨迹误差 (RTE) 上均达到最优性能。

## 核心内容
### 方法架构
X-IONet 的核心设计包含三个关键模块：
- **规则驱动的专家选择模块**：基于 IMU 序列的统计特征（如加速度方差）自动分类运动平台（行人或四足机器人），并将数据路由至对应的专家网络。
- **双阶段注意力位移预测网络**：
  - 第一阶段：使用 Transformer 编码器建模长程时间依赖关系。
  - 第二阶段：通过跨轴注意力机制捕捉三轴加速度与角速度之间的相关性。
  - 输出：位移向量及其不确定性（方差）。
- **Extended Kalman Filter (EKF) 融合**：将位移预测与不确定性作为观测输入，结合 IMU 原始测量进行状态估计，提升鲁棒性。

### 实验设置
- **数据集**：
  - 行人：RoNIN 公开数据集（包含多种手持与口袋放置场景）。
  - 四足机器人：GrandTour 公开数据集（多种地形）及自采集 Go2 数据集（包含跳跃、奔跑等高动态动作）。
- **基线方法**：对比了 IONet、RoNIN、TLIO 等主流惯性里程计方法。
- **评估指标**：绝对轨迹误差 (ATE) 与相对轨迹误差 (RTE)。

### 关键结果
- **RoNIN 数据集**：ATE 降低 14.3%，RTE 降低 11.4%。
- **GrandTour 数据集**：ATE 降低 11.8%，RTE 降低 9.7%。
- **Go2 数据集**：ATE 降低 52.8%，RTE 降低 41.3%。
- 消融实验验证了专家选择模块与双阶段注意力机制的有效性，移除任一模块均导致性能显著下降。

### 结论
X-IONet 通过跨平台专家路由与双阶段注意力机制，首次实现了单一模型在行人与四足机器人上的高精度惯性导航，尤其在高动态场景下优势显著。未来工作可扩展至更多运动平台（如轮式机器人）及多传感器融合场景。

## Overview
Learning-based inertial odometry has achieved remarkable progress in pedestrian navigation. However, extending these methods to quadruped robots remains challenging due to their distinct and highly dynamic motion patterns. Models that perform well on pedestrian data often experience severe degradation when deployed on legged platforms. To tackle this challenge, we introduce X-IONet, a cross-platform inertial odometry framework that operates solely using a single Inertial Measurement Unit (IMU). X-IONet incorporates a rule-based expert selection module to classify motion platforms and route IMU sequences to platform-specific expert networks. The displacement prediction network features a dual-stage attention architecture that jointly models long-range temporal dependencies and inter-axis correlations, enabling accurate motion representation. It outputs both displacement and associated uncertainty, which are further fused through an Extended Kalman Filter (EKF) for robust state estimation. Extensive experiments on the public RoNIN pedestrian dataset, the GrandTour quadruped dataset, and a self-collected Go2 quadruped dataset demonstrate that X-IONet achieves state-of-the-art performance, reducing ATE and RTE by 14.3% and 11.4% on RoNIN, 11.8% and 9.7% on GrandTour, and 52.8% and 41.3% on Go2. These results highlight X-IONet's effectiveness for accurate and robust inertial navigation across both human and legged robot platforms.

## 参考
- https://arxiv.org/abs/2511.08277
- https://github.com/ImChong/Robotics_Notebooks

## 개요

X-IONet은 기존 관성 측위 방법이 사족 로봇의 고동적 운동 패턴에 일반화되기 어려운 문제를 해결하기 위해, 크로스 플랫폼 솔루션을 설계했습니다. 이 프레임워크는 규칙 기반 전문가 선택 모듈을 통해 운동 플랫폼 유형을 자동으로 식별하고, IMU 시퀀스를 해당 전문가 네트워크로 라우팅합니다. 변위 예측 네트워크는 이중 단계 주의 메커니즘을 채택하여 장기 시간 의존성과 축 간 상관성을 동시에 모델링하고, 변위 및 불확실성을 출력합니다. 이러한 출력은 이후 Extended Kalman Filter (EKF)를 통해 융합되어 강건한 상태 추정을 구현합니다. RoNIN, GrandTour 및 자체 수집 Go2 데이터셋에서의 실험은 X-IONet이 절대 궤적 오차(ATE)와 상대 궤적 오차(RTE) 모두에서 최적 성능을 달성함을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
X-IONet의 핵심 설계는 세 가지 주요 모듈로 구성됩니다:
- **규칙 기반 전문가 선택 모듈**: IMU 시퀀스의 통계적 특징(예: 가속도 분산)을 기반으로 운동 플랫폼(보행자 또는 사족 로봇)을 자동 분류하고, 데이터를 해당 전문가 네트워크로 라우팅합니다.
- **이중 단계 주의 변위 예측 네트워크**:
  - 첫 번째 단계: Transformer 인코더를 사용하여 장기 시간 의존성을 모델링합니다.
  - 두 번째 단계: 교차 축 주의 메커니즘을 통해 3축 가속도와 각속도 간의 상관성을 포착합니다.
  - 출력: 변위 벡터 및 불확실성(분산).
- **Extended Kalman Filter (EKF) 융합**: 변위 예측과 불확실성을 관측 입력으로 사용하고, IMU 원시 측정값과 결합하여 상태 추정을 수행하여 강건성을 향상시킵니다.

### 실험 설정
- **데이터셋**:
  - 보행자: RoNIN 공개 데이터셋(다양한 휴대 및 주머니 배치 시나리오 포함).
  - 사족 로봇: GrandTour 공개 데이터셋(다양한 지형) 및 자체 수집 Go2 데이터셋(점프, 달리기 등 고동적 동작 포함).
- **기준 방법**: IONet, RoNIN, TLIO 등 주요 관성 측위 방법과 비교했습니다.
- **평가 지표**: 절대 궤적 오차(ATE) 및 상대 궤적 오차(RTE).

### 주요 결과
- **RoNIN 데이터셋**: ATE 14.3% 감소, RTE 11.4% 감소.
- **GrandTour 데이터셋**: ATE 11.8% 감소, RTE 9.7% 감소.
- **Go2 데이터셋**: ATE 52.8% 감소, RTE 41.3% 감소.
- 절제 실험은 전문가 선택 모듈과 이중 단계 주의 메커니즘의 효과를 검증했으며, 어느 하나의 모듈을 제거해도 성능이 크게 저하되었습니다.

### 결론
X-IONet은 크로스 플랫폼 전문가 라우팅과 이중 단계 주의 메커니즘을 통해 단일 모델로 보행자와 사족 로봇에서 고정밀 관성 항법을 최초로 구현했으며, 특히 고동적 시나리오에서 뚜렷한 이점을 보여줍니다. 향후 작업은 더 많은 운동 플랫폼(예: 바퀴형 로봇) 및 다중 센서 융합 시나리오로 확장할 수 있습니다.
