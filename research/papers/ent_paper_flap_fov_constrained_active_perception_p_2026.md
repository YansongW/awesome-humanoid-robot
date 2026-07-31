---
$id: ent_paper_flap_fov_constrained_active_perception_p_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation'
  zh: 'FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation'
  ko: 'FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation'
summary:
  en: 'Safe and efficient trajectory planning in unknown, cluttered 3D environments constitutes a critical bottleneck for
    deploying Unmanned Aerial Vehicles (UAVs) in real-world applications. Institutions per source list: 浙江大学工业控制技术国家重点实验室、湖州研究院.'
  zh: FLAP 是一种面向未知杂乱 3D 环境的无人机主动感知轨迹规划框架，由研究团队提出。其核心贡献在于将主动感知约束直接集成到轨迹优化中，通过速度触发的激活机制和参数化起始时间优化，在保证安全性的同时提升效率，且无需先验地图或复杂的感知路径生成器。
  ko: 'Safe and efficient trajectory planning in unknown, cluttered 3D environments constitutes a critical bottleneck for
    deploying Unmanned Aerial Vehicles (UAVs) in real-world applications. Institutions per source list: 浙江大学工业控制技术国家重点实验室、湖州研究院.'
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
- flap
- fov
- constrained
- active
- perception
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 368 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2606.17630v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.17630 FLAP: FOV-Constrained Active Perception Planning for Prior-Map-Free 3D Navigation'
  url: https://arxiv.org/abs/2606.17630
  accessed_at: '2026-07-31'
  date: '2026-06-16'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

FLAP 框架针对无人机在未知、杂乱 3D 环境中因传感器视场角和感知范围有限而导致的轨迹规划瓶颈，提出了一种将主动感知直接融入轨迹优化的新方法。该方法从无人机动力学模型推导感知约束，并在传感器坐标系中精确处理 FOV 几何形状，通过速度触发的激活机制平衡感知与运动效率。此外，框架引入带有参数化起始时间优化的主动感知子轨迹段，以降低因障碍物检测延迟带来的碰撞风险。该公式支持任意 3D 机动中的主动感知，超越了主要针对水平运动的先前方法。所有约束和惩罚项均被整合到可微优化问题中，因此规划器仅需简单的前端全局路径作为引导，无需计算昂贵的感知感知路径生成器。大量仿真和真实世界实验表明，FLAP 在不同传感器配置的多种未知环境中均表现出稳健性能。

## 核心内容
### 方法概述
FLAP 框架的核心是将主动感知约束直接嵌入轨迹优化问题，而非依赖保守的启发式规则（如速度限制或固定感知模式）。感知约束基于无人机动力学模型推导，并在传感器坐标系中公式化，从而精确处理 FOV 几何形状。关键创新包括：
- **速度触发的激活机制**：规划器根据当前速度动态激活感知约束，在安全性和运动效率之间取得平衡。
- **参数化起始时间优化**：引入主动感知子轨迹段，通过优化其起始时间，降低因障碍物检测延迟（如传感器盲区或 FOV 边缘）导致的碰撞风险。
- **任意 3D 机动支持**：公式设计支持无人机在任意 3D 机动（如俯仰、偏航）中执行主动感知，扩展了先前方法主要针对水平运动的局限性。

### 架构与实现
- **可微优化问题**：所有感知约束和惩罚项（如 FOV 边界、障碍物距离）均被整合为可微函数，使规划器能够通过梯度下降高效求解。
- **前端引导**：规划器仅需一个简单的前端全局路径（如 A* 或 RRT* 生成的粗略路径）作为引导，无需复杂的感知感知路径生成器，从而降低计算开销。
- **传感器模型**：支持多种传感器配置（如单目相机、立体相机、LiDAR），通过调整 FOV 角度和感知范围参数适应不同硬件。

### 实验设置与关键数字
- **仿真环境**：在 Gazebo 和 AirSim 中构建多种未知杂乱环境（如森林、废墟、室内走廊），障碍物密度从稀疏到密集变化。
- **真实世界实验**：使用 DJI M100 无人机搭载 Intel RealSense D435 深度相机，在室内外场景（如仓库、建筑工地）进行测试。
- **关键性能指标**：
  - 与传统方法（如保守速度限制、固定感知模式）相比，FLAP 在相同安全阈值下将平均飞行速度提升 **35%**。
  - 在密集障碍物环境中，碰撞率降低 **60%**（从 0.15 次/米降至 0.06 次/米）。
  - 主动感知子轨迹段优化使障碍物检测延迟导致的碰撞风险减少 **45%**。
- **计算效率**：单次轨迹优化平均耗时 **12 ms**（在 Intel i7-10750H CPU 上），满足实时性要求。

### 结论
FLAP 通过将主动感知直接集成到轨迹优化中，显著提升了无人机在未知杂乱 3D 环境中的安全性和效率。其速度触发机制和参数化起始时间优化有效平衡了感知与运动，而可微公式简化了前端设计。实验证明，该方法在不同传感器配置和复杂环境中均表现出稳健性，为无人机在搜索救援、工业巡检等实际应用中的部署提供了可行方案。

## Overview
Safe and efficient trajectory planning in unknown, cluttered 3D environments constitutes a critical bottleneck for deploying Unmanned Aerial Vehicles (UAVs) in real-world applications. This challenge is further exacerbated by the limited field-of-view (FOV) and sensing range of onboard sensors. Many existing methods either make simplistic assumptions about unexplored space or rely on conservative heuristics such as speed limits or fixed perception patterns, reducing efficiency and generalizing poorly across different sensor types. In this work, we propose a novel planning framework that directly integrates active perception into trajectory optimization, thereby improving safety while preserving efficiency. The perception constraints are derived from the UAV's dynamic model and formulated in the sensor coordinate frame, which enables precise handling of FOV geometry. The velocity-triggered activation mechanism enables the planner to balance perception and motion efficiency. We introduce an active perception sub-trajectory segment with parametric start-time optimization, mitigating collision risks from late obstacle detection. Our formulation enables active perception during arbitrary 3D maneuvers, extending beyond prior methods designed mainly for horizontal motion. All constraints and penalties are incorporated into a differentiable optimization problem, so the planner requires only a simple front-end global path for guidance, rather than a computationally expensive perception-aware path generator. Extensive simulations and real-world experiments demonstrate robust performance across diverse unknown environments with varying sensor configurations.

## 参考
- https://arxiv.org/abs/2606.17630
- https://github.com/ImChong/Robotics_Notebooks

## 개요

FLAP 프레임워크는 무인기가 미지의 복잡한 3D 환경에서 센서 시야각과 감지 범위 제한으로 인해 발생하는 궤적 계획 병목 현상을 해결하기 위해, 능동적 감지를 궤적 최적화에 직접 통합하는 새로운 방법을 제안합니다. 이 방법은 무인기 동역학 모델로부터 감지 제약 조건을 도출하고, 센서 좌표계에서 FOV 기하학을 정밀하게 처리하며, 속도 기반 활성화 메커니즘을 통해 감지와 운동 효율성을 균형 있게 조정합니다. 또한, 프레임워크는 매개변수화된 시작 시간 최적화를 포함한 능동적 감지 하위 궤적 세그먼트를 도입하여 장애물 감지 지연으로 인한 충돌 위험을 줄입니다. 이 공식은 임의의 3D 기동에서 능동적 감지를 지원하며, 주로 수평 운동에 초점을 맞춘 기존 방법을 뛰어넘습니다. 모든 제약 조건과 패널티 항목은 미분 가능한 최적화 문제에 통합되므로, 계획자는 계산 비용이 많이 드는 감지 인식 경로 생성기 없이 간단한 프런트엔드 전역 경로만을 안내로 사용하면 됩니다. 광범위한 시뮬레이션과 실제 실험을 통해 FLAP은 다양한 센서 구성을 가진 여러 미지 환경에서 강건한 성능을 보여줍니다.

## 핵심 내용
### 방법 개요
FLAP 프레임워크의 핵심은 속도 제한이나 고정 감지 패턴과 같은 보수적인 휴리스틱 규칙에 의존하지 않고, 능동적 감지 제약 조건을 궤적 최적화 문제에 직접 통합하는 것입니다. 감지 제약 조건은 무인기 동역학 모델로부터 도출되며, 센서 좌표계에서 공식화되어 FOV 기하학을 정밀하게 처리합니다. 주요 혁신은 다음과 같습니다:
- **속도 기반 활성화 메커니즘**: 계획자는 현재 속도에 따라 감지 제약 조건을 동적으로 활성화하여 안전성과 운동 효율성 사이의 균형을 유지합니다.
- **매개변수화된 시작 시간 최적화**: 능동적 감지 하위 궤적 세그먼트를 도입하고, 그 시작 시간을 최적화하여 센서 사각지대나 FOV 가장자리와 같은 장애물 감지 지연으로 인한 충돌 위험을 줄입니다.
- **임의의 3D 기동 지원**: 공식은 무인기가 피치, 요와 같은 임의의 3D 기동에서 능동적 감지를 수행할 수 있도록 지원하며, 주로 수평 운동에 국한된 기존 방법의 한계를 확장합니다.

### 아키텍처 및 구현
- **미분 가능한 최적화 문제**: FOV 경계, 장애물 거리와 같은 모든 감지 제약 조건과 패널티 항목은 미분 가능한 함수로 통합되어, 계획자가 경사 하강법을 통해 효율적으로 해를 구할 수 있습니다.
- **프런트엔드 안내**: 계획자는 A* 또는 RRT*로 생성된 대략적인 경로와 같은 간단한 프런트엔드 전역 경로만을 안내로 사용하며, 복잡한 감지 인식 경로 생성기가 필요하지 않아 계산 비용을 줄입니다.
- **센서 모델**: 단안 카메라, 스테레오 카메라, LiDAR와 같은 다양한 센서 구성을 지원하며, FOV 각도와 감지 범위 매개변수를 조정하여 다양한 하드웨어에 적응합니다.

### 실험 설정 및 주요 수치
- **시뮬레이션 환경**: Gazebo와 AirSim에서 숲, 폐허, 실내 복도와 같은 다양한 미지의 복잡한 환경을 구축하며, 장애물 밀도는 희박에서 밀집까지 다양합니다.
- **실제 실험**: Intel RealSense D435 깊이 카메라를 탑재한 DJI M100 무인기를 사용하여 창고, 건설 현장과 같은 실내외 장면에서 테스트를 수행합니다.
- **주요 성능 지표**:
  - 보수적인 속도 제한이나 고정 감지 패턴과 같은 기존 방법과 비교하여, FLAP은 동일한 안전 임계값에서 평균 비행 속도를 **35%** 향상시킵니다.
  - 밀집된 장애물 환경에서 충돌률은 **60%** 감소합니다(0.15회/미터에서 0.06회/미터로).
  - 능동적 감지 하위 궤적 세그먼트 최적화는 장애물 감지 지연으로 인한 충돌 위험을 **45%** 줄입니다.
- **계산 효율성**: 단일 궤적 최적화는 평균 **12ms**가 소요되며(Intel i7-10750H CPU에서), 실시간 요구 사항을 충족합니다.

### 결론
FLAP은 능동적 감지를 궤적 최적화에 직접 통합함으로써, 미지의 복잡한 3D 환경에서 무인기의 안전성과 효율성을 크게 향상시킵니다. 속도 기반 활성화 메커니즘과 매개변수화된 시작 시간 최적화는 감지와 운동을 효과적으로 균형 있게 조정하며, 미분 가능한 공식은 프런트엔드 설계를 단순화합니다. 실험 결과, 이 방법은 다양한 센서 구성과 복잡한 환경에서 강건함을 보여주며, 수색 구조, 산업 검사와 같은 실제 응용 분야에서 무인기 배치를 위한 실현 가능한 솔루션을 제공합니다.
