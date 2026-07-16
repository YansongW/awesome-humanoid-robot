---
$id: ent_method_thermal_simulation
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Thermal Simulation
  zh: 热仿真
  ko: 열 시뮬레이션
summary:
  en: A computational method that predicts temperature distribution, heat flux, and cooling requirements of electronic and
    mechanical systems under operating loads.
  zh: 1. 建立功耗模型：列出各组件的稳态功耗、峰值功耗和占空比。 2. 构建几何模型：用 CAD 模型或简化几何表示机器人外壳、散热器、风道。 3. 设置材料属性：导热系数、比热容、密度、发射率。 4. 划分网格：对关键区域加密，对远处区域粗化。
    5. 设定边界条件：环境温度、对流系数、风扇曲线、接触热阻。 6. 求解稳态/瞬态温度场：评估关键芯片结温和外壳温度。 7. 迭代优化：调整散热器、风道、TIM、功耗分配，直到满足热目标。
  ko: 전자·기계 시스템의 작동 하중에서 온도 분포·열 유량·냉각 요구량을 예측하는 계산 방법.
domains:
- 02_components
- 08_software_middleware
layers:
- midstream
functional_roles:
- knowledge
tags:
- method
- chapter_6
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-04.md#两节点热网络模型 by scripts/backfill_nonpaper_entries.py. Body backfilled from chapter-06.md
    section '6.7.3 整机功率与热仿真思路' by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---

## 概述
预测电子与机械系统在运行载荷下的温度分布、热流密度与散热需求的计算方法。

## 核心内容
### 6.7.3 整机功率与热仿真思路
整机热仿真通常按以下步骤进行：

1. **建立功耗模型**：列出各组件的稳态功耗、峰值功耗和占空比。
2. **构建几何模型**：用 CAD 模型或简化几何表示机器人外壳、散热器、风道。
3. **设置材料属性**：导热系数、比热容、密度、发射率。
4. **划分网格**：对关键区域加密，对远处区域粗化。
5. **设定边界条件**：环境温度、对流系数、风扇曲线、接触热阻。
6. **求解稳态/瞬态温度场**：评估关键芯片结温和外壳温度。
7. **迭代优化**：调整散热器、风道、TIM、功耗分配，直到满足热目标。

!!! note "术语解释：占空比、CAD、边界条件、网格收敛、风扇曲线"
    - **占空比（duty cycle）**：某组件处于高功耗状态的时间比例。
    - **CAD（Computer-Aided Design）**：计算机辅助设计。
    - **边界条件（boundary condition）**：求解域边界上的物理约束，如温度、热流、对流。
    - **网格收敛（mesh convergence）**：加密网格后结果不再显著变化，说明数值解可信。
    - **风扇曲线（fan curve）**：风扇流量与压降的关系曲线。

### 热仿真在人形机器人中的工程意义
人形机器人集成了计算单元、电机驱动、电池和功率电子，热密度高且空间受限。热仿真用于预判关键芯片结温、电机绕组温升和外壳表面温度，指导散热器、风道、导热界面材料和功耗管理策略的设计，避免过热降频或寿命衰减。通过热-力-电联合仿真，还可以在整机设计早期识别热瓶颈并优化布局。

## 参考
- 项目 Wiki：wiki/docs/chapters/chapter-06.md 第「6.7.3 整机功率与热仿真思路」节
- Wiki extraction

热仿真作为人形机器人产业链中的关键组成部分，其相关理论与工程实践仍在持续发展。深入理解其原理、边界条件与典型应用场景，对于将实验室样机转化为可量产产品具有重要意义。

## Overview
Computational methods for predicting temperature distribution, heat flux density, and heat dissipation requirements of electronic and mechanical systems under operational loads.

## Content
### 6.7.3 System Power and Thermal Simulation Approach
System-level thermal simulation typically follows these steps:

1. **Establish power consumption model**: List the steady-state power, peak power, and duty cycle of each component.
2. **Construct geometric model**: Use CAD models or simplified geometries to represent the robot casing, heat sinks, and air ducts.
3. **Set material properties**: Thermal conductivity, specific heat capacity, density, and emissivity.
4. **Mesh generation**: Refine the mesh in critical regions and coarsen it in distant areas.
5. **Define boundary conditions**: Ambient temperature, convection coefficients, fan curves, and contact thermal resistance.
6. **Solve steady-state/transient temperature field**: Evaluate critical chip junction temperatures and casing temperatures.
7. **Iterative optimization**: Adjust heat sinks, air ducts, TIM (Thermal Interface Material), and power distribution until thermal targets are met.

!!! note "Terminology: Duty Cycle, CAD, Boundary Conditions, Mesh Convergence, Fan Curve"
    - **Duty cycle**: The proportion of time a component operates at high power.
    - **CAD (Computer-Aided Design)**: Computer-aided design.
    - **Boundary condition**: Physical constraints on the boundaries of the solution domain, such as temperature, heat flux, and convection.
    - **Mesh convergence**: When results no longer change significantly after mesh refinement, indicating the numerical solution is reliable.
    - **Fan curve**: The relationship between fan flow rate and pressure drop.

### Engineering Significance of Thermal Simulation in Humanoid Robots
Humanoid robots integrate computing units, motor drives, batteries, and power electronics, resulting in high heat density within confined spaces. Thermal simulation is used to predict critical chip junction temperatures, motor winding temperature rises, and casing surface temperatures, guiding the design of heat sinks, air ducts, thermal interface materials, and power management strategies to avoid overheating-induced throttling or lifespan degradation. Through thermal-mechanical-electrical co-simulation, thermal bottlenecks can be identified and layout optimized early in the system design phase.

## 개요
전자 및 기계 시스템이 작동 하중 하에서 온도 분포, 열유속 밀도 및 방열 요구량을 예측하는 계산 방법.

## 핵심 내용
### 6.7.3 전체 기기 전력 및 열 시뮬레이션 접근법
전체 기기 열 시뮬레이션은 일반적으로 다음 단계로 진행됩니다:

1. **소비 전력 모델 구축**: 각 구성 요소의 정상 상태 소비 전력, 최대 소비 전력 및 듀티 사이클을 나열합니다.
2. **기하학적 모델 구축**: CAD 모델 또는 단순화된 형상을 사용하여 로봇 외부 케이스, 방열판, 공기 덕트를 표현합니다.
3. **재료 특성 설정**: 열전도율, 비열 용량, 밀도, 방사율을 설정합니다.
4. **메쉬 분할**: 주요 영역은 세밀하게, 원거리 영역은 거칠게 분할합니다.
5. **경계 조건 설정**: 주변 온도, 대류 계수, 팬 곡선, 접촉 열 저항을 설정합니다.
6. **정상/과도 온도장 해석**: 주요 칩의 접합 온도와 외부 케이스 온도를 평가합니다.
7. **반복 최적화**: 방열판, 공기 덕트, TIM, 전력 분배를 조정하여 열 목표를 충족할 때까지 반복합니다.

!!! note "용어 설명: 듀티 사이클, CAD, 경계 조건, 메쉬 수렴, 팬 곡선"
    - **듀티 사이클(duty cycle)**: 특정 구성 요소가 높은 소비 전력 상태에 있는 시간 비율.
    - **CAD(Computer-Aided Design)**: 컴퓨터 지원 설계.
    - **경계 조건(boundary condition)**: 해석 영역 경계에서의 물리적 제약 조건(예: 온도, 열유속, 대류).
    - **메쉬 수렴(mesh convergence)**: 메쉬를 세밀화한 후 결과가 더 이상 크게 변하지 않아 수치 해석이 신뢰할 수 있음을 나타냄.
    - **팬 곡선(fan curve)**: 팬 유량과 압력 강하 간의 관계 곡선.

### 인간형 로봇에서 열 시뮬레이션의 공학적 의의
인간형 로봇은 연산 장치, 모터 드라이브, 배터리 및 전력 전자 장치를 통합하며, 열 밀도가 높고 공간이 제한적입니다. 열 시뮬레이션은 주요 칩의 접합 온도, 모터 권선 온도 상승 및 외부 케이스 표면 온도를 예측하여 방열판, 공기 덕트, 열 인터페이스 재료 및 전력 관리 전략의 설계를 안내하고, 과열로 인한 성능 저하 또는 수명 감소를 방지하는 데 사용됩니다. 열-구조-전기 연합 시뮬레이션을 통해 전체 기기 설계 초기 단계에서 열 병목 현상을 식별하고 배치를 최적화할 수 있습니다.
