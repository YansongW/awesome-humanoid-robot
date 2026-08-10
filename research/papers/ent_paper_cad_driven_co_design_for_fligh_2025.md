---
$id: ent_paper_cad_driven_co_design_for_fligh_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids
  zh: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids
  ko: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids
summary:
  en: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids is a 2025 work on hardware design for humanoid robots.
  zh: 本文提出了一种基于CAD驱动的协同设计框架，用于优化喷气动力空中人形机器人，使其能够执行动态约束轨迹。该工作以iRonCub-Mk3模型为起点，通过实验设计方法生成5000种几何变体，并利用K-means聚类和NSGA-II多目标优化算法，联合优化设计参数与控制参数，最终输出一组具备飞行能力的人形机器人配置。
  ko: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids is a 2025 work on hardware design for humanoid robots.
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- cad_driven_co_design_for_fligh
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14935v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (910 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: CAD-Driven Co-Design for Flight-Ready Jet-Powered Humanoids (arXiv)
  url: https://arxiv.org/abs/2509.14935
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对喷气动力空中人形机器人的硬件设计问题，提出了一种CAD驱动的协同设计框架。框架从iRonCub-Mk3模型出发，通过修改肢体尺寸、喷气接口几何参数（如角度和偏移量）以及整体质量分布，采用实验设计方法生成了5000种几何各异且机械可行的设计方案。每个模型均通过CAD装配构建以确保结构有效性，并兼容仿真工具。为降低计算成本并实现参数敏感性分析，模型通过K-means聚类选取代表性中心点进行评估。飞行性能评估采用最小加加速度轨迹，为基于动量的线性化模型预测控制策略提供位置和速度参考。最终，利用NSGA-II算法进行多目标优化，联合探索设计中心点与MPC增益参数空间，以最小化轨迹跟踪误差和机械能耗为目标。

## 核心内容
### 方法概述
- **设计空间生成**：以iRonCub-Mk3为基准模型，采用实验设计方法系统修改肢体尺寸、喷气接口几何参数（角度和偏移量）及质量分布，生成5000种几何变体。
- **CAD装配与验证**：每个设计通过CAD装配构建，确保结构有效性与仿真工具兼容性。
- **聚类与降维**：使用K-means算法对5000个模型进行聚类，选取代表性中心点进行评估，以降低计算成本并支持参数敏感性分析。
- **轨迹与控制**：采用最小加加速度轨迹作为飞行性能评估基准，为基于动量的线性化模型预测控制策略提供位置和速度参考。
- **多目标优化**：利用NSGA-II算法联合优化设计中心点与MPC增益参数，目标函数为最小化轨迹跟踪误差与机械能耗。

### 实验设置
- **设计变量**：包括肢体长度、喷气接口角度与偏移量、质量分布等几何与物理参数。
- **控制参数**：MPC增益参数作为优化变量之一。
- **评估指标**：轨迹跟踪误差与机械能耗。

### 关键结果
- 框架输出一组飞行就绪的人形机器人配置，并附带验证后的控制参数。
- 提供了一种结构化方法，用于选择并实现可行的空中人形机器人设计。

### 结论
该CAD驱动协同设计框架有效整合了硬件设计与控制优化，为喷气动力空中人形机器人的开发提供了系统化工具，显著提升了设计可行性与飞行性能。

## Overview
This paper presents a CAD-driven co-design framework for optimizing jet-powered aerial humanoid robots to execute dynamically constrained trajectories. Starting from the iRonCub-Mk3 model, a Design of Experiments (DoE) approach is used to generate 5,000 geometrically varied and mechanically feasible designs by modifying limb dimensions, jet interface geometry (e.g., angle and offset), and overall mass distribution. Each model is constructed through CAD assemblies to ensure structural validity and compatibility with simulation tools. To reduce computational cost and enable parameter sensitivity analysis, the models are clustered using K-means, with representative centroids selected for evaluation. A minimum-jerk trajectory is used to assess flight performance, providing position and velocity references for a momentum-based linearized Model Predictive Control (MPC) strategy. A multi-objective optimization is then conducted using the NSGA-II algorithm, jointly exploring the space of design centroids and MPC gain parameters. The objectives are to minimize trajectory tracking error and mechanical energy expenditure. The framework outputs a set of flight-ready humanoid configurations with validated control parameters, offering a structured method for selecting and implementing feasible aerial humanoid designs.

## 参考
- http://arxiv.org/abs/2509.14935v1

## 개요
이 연구는 제트 추진 공중 휴머노이드 로봇의 하드웨어 설계 문제를 해결하기 위해 CAD 기반 공동 설계 프레임워크를 제안한다. 프레임워크는 iRonCub-Mk3 모델에서 출발하여, 팔다리 치수, 제트 인터페이스 기하 파라미터(예: 각도 및 오프셋), 그리고 전체 질량 분포를 수정하고, 실험 설계 방법을 사용하여 5000개의 기하학적으로 다양하고 기계적으로 실현 가능한 설계안을 생성한다. 각 모델은 구조적 유효성을 보장하고 시뮬레이션 도구와 호환되도록 CAD 어셈블리를 통해 구축된다. 계산 비용을 줄이고 파라미터 민감도 분석을 가능하게 하기 위해, 모델은 K-means 클러스터링을 통해 대표 중심점을 선택하여 평가한다. 비행 성능 평가는 최소 가속도 궤적을 사용하며, 이는 모멘텀 기반 선형화 모델 예측 제어 전략에 위치 및 속도 참조를 제공한다. 마지막으로, NSGA-II 알고리즘을 사용한 다중 목표 최적화를 통해 설계 중심점과 MPC 게인 파라미터 공간을 공동으로 탐색하여 궤적 추적 오차와 기계적 에너지 소비를 최소화한다.

## 핵심 내용
### 방법 개요
- **설계 공간 생성**: iRonCub-Mk3를 기준 모델로 사용하여, 실험 설계 방법을 통해 팔다리 치수, 제트 인터페이스 기하 파라미터(각도 및 오프셋) 및 질량 분포를 체계적으로 수정하여 5000개의 기하 변형을 생성한다.
- **CAD 어셈블리 및 검증**: 각 설계는 CAD 어셈블리를 통해 구축되어 구조적 유효성과 시뮬레이션 도구 호환성을 보장한다.
- **클러스터링 및 차원 축소**: K-means 알고리즘을 사용하여 5000개의 모델을 클러스터링하고, 대표 중심점을 선택하여 평가함으로써 계산 비용을 줄이고 파라미터 민감도 분석을 지원한다.
- **궤적 및 제어**: 최소 가속도 궤적을 비행 성능 평가 기준으로 사용하며, 이는 모멘텀 기반 선형화 모델 예측 제어 전략에 위치 및 속도 참조를 제공한다.
- **다중 목표 최적화**: NSGA-II 알고리즘을 사용하여 설계 중심점과 MPC 게인 파라미터를 공동으로 최적화하며, 목표 함수는 궤적 추적 오차와 기계적 에너지 소비를 최소화하는 것이다.

### 실험 설정
- **설계 변수**: 팔다리 길이, 제트 인터페이스 각도 및 오프셋, 질량 분포 등의 기하 및 물리 파라미터를 포함한다.
- **제어 파라미터**: MPC 게인 파라미터가 최적화 변수 중 하나로 포함된다.
- **평가 지표**: 궤적 추적 오차와 기계적 에너지 소비.

### 주요 결과
- 프레임워크는 검증된 제어 파라미터와 함께 비행 준비가 완료된 휴머노이드 로봇 구성 세트를 출력한다.
- 실현 가능한 공중 휴머노이드 로봇 설계를 선택하고 구현하기 위한 구조화된 방법을 제공한다.

### 결론
이 CAD 기반 공동 설계 프레임워크는 하드웨어 설계와 제어 최적화를 효과적으로 통합하여, 제트 추진 공중 휴머노이드 로봇 개발을 위한 체계적인 도구를 제공하며, 설계 실현 가능성과 비행 성능을 크게 향상시킨다.
