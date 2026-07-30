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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14935v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
본 논문은 제트 추진 방식의 비행 인간형 로봇이 동적으로 제약된 궤적을 실행할 수 있도록 최적화하는 CAD 기반 공동 설계 프레임워크를 제시합니다. iRonCub-Mk3 모델을 기반으로 실험 계획법(DoE) 접근 방식을 사용하여, 팔다리 치수, 제트 인터페이스 형상(예: 각도 및 오프셋), 전체 질량 분포를 수정함으로써 기하학적으로 다양하고 기계적으로 실현 가능한 5,000개의 설계를 생성합니다. 각 모델은 CAD 어셈블리를 통해 구축되어 구조적 타당성과 시뮬레이션 도구와의 호환성을 보장합니다. 계산 비용을 줄이고 매개변수 민감도 분석을 가능하게 하기 위해, 모델은 K-평균을 사용하여 클러스터링되며, 평가를 위해 대표적인 중심점이 선택됩니다. 비행 성능을 평가하기 위해 최소 저크 궤적이 사용되며, 운동량 기반 선형화된 모델 예측 제어(MPC) 전략에 대한 위치 및 속도 참조를 제공합니다. 그런 다음 NSGA-II 알고리즘을 사용하여 다중 목적 최적화가 수행되며, 설계 중심점과 MPC 게인 매개변수의 공간을 공동으로 탐색합니다. 목표는 궤적 추적 오차와 기계적 에너지 소비를 최소화하는 것입니다. 프레임워크는 검증된 제어 매개변수를 갖춘 비행 가능한 인간형 구성을 출력하며, 실현 가능한 비행 인간형 설계를 선택하고 구현하기 위한 체계적인 방법을 제공합니다.

## 핵심 내용
본 논문은 제트 추진 방식의 비행 인간형 로봇이 동적으로 제약된 궤적을 실행할 수 있도록 최적화하는 CAD 기반 공동 설계 프레임워크를 제시합니다. iRonCub-Mk3 모델을 기반으로 실험 계획법(DoE) 접근 방식을 사용하여, 팔다리 치수, 제트 인터페이스 형상(예: 각도 및 오프셋), 전체 질량 분포를 수정함으로써 기하학적으로 다양하고 기계적으로 실현 가능한 5,000개의 설계를 생성합니다. 각 모델은 CAD 어셈블리를 통해 구축되어 구조적 타당성과 시뮬레이션 도구와의 호환성을 보장합니다. 계산 비용을 줄이고 매개변수 민감도 분석을 가능하게 하기 위해, 모델은 K-평균을 사용하여 클러스터링되며, 평가를 위해 대표적인 중심점이 선택됩니다. 비행 성능을 평가하기 위해 최소 저크 궤적이 사용되며, 운동량 기반 선형화된 모델 예측 제어(MPC) 전략에 대한 위치 및 속도 참조를 제공합니다. 그런 다음 NSGA-II 알고리즘을 사용하여 다중 목적 최적화가 수행되며, 설계 중심점과 MPC 게인 매개변수의 공간을 공동으로 탐색합니다. 목표는 궤적 추적 오차와 기계적 에너지 소비를 최소화하는 것입니다. 프레임워크는 검증된 제어 매개변수를 갖춘 비행 가능한 인간형 구성을 출력하며, 실현 가능한 비행 인간형 설계를 선택하고 구현하기 위한 체계적인 방법을 제공합니다.

## 参考
- http://arxiv.org/abs/2509.14935v1
