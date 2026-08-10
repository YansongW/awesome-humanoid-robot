---
$id: ent_paper_chen_modal_based_kinematics_and_con_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Modal-based Kinematics and Contact Detection of Soft Robots
  zh: 基于模态的软体机器人运动学与接触检测
  ko: 모달 기반 소프트 로봇 운동학 및 접촉 감지
summary:
  en: Proposes modal-based forward and instantaneous kinematics for a 1-DoF pneumatic bellow soft actuator and uses fixed
    centrode deviation with nonlinear least-squares optimization to detect external contacts and estimate their location along
    the backbone.
  zh: 本文提出了一种基于模态的1自由度气动波纹管软体执行器正运动学与瞬时运动学建模方法，并利用固定瞬心偏差结合非线性最小二乘优化，实现了对外部接触的检测及其沿骨架位置的估计。
  ko: 1자유도 공기압 벨로우 연성 액츄에이터의 모달 기반 정운동학 및 순간운동학을 제안하고, 고정 중심선 편차법과 비선형 최소자승 최적화를 사용하여 외부 접촉을 감지하고 백본 상의 접촉 위치를 추정한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- soft_robotics
- pneumatic_bellow_actuator
- contact_detection
- modal_kinematics
- fixed_centrode_deviation
- nonlinear_least_squares
- compliant_actuator
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1906.11654v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (561 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Modal-based Kinematics and Contact Detection of Soft Robots
  url: https://arxiv.org/abs/1906.11654
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
该研究聚焦于构成复杂多自由度软体机器人的基础单元——1自由度气动波纹管弯曲执行器。通过空间曲线的积分表示对软体机器人进行建模，并采用模态方法显式计算其正运动学与瞬时运动学。为应对外部接触导致的形变与动力学变化，研究引入固定瞬心偏差方法，通过求解非线性最小二乘优化问题，在仿真中实现了接触位置的准确估计。

## 核心内容
### 研究背景与目标
软体机器人凭借其柔顺特性，可在受限空间中安全操作，但外部接触力易导致形变，影响运动学与动力学性能。准确检测接触并估计其位置，对建模、控制与任务完成至关重要。

### 方法与架构
- **研究对象**：1自由度气动波纹管弯曲执行器，作为构建多自由度软体机器人的基础组件。
- **运动学建模**：采用空间曲线的积分表示，通过模态方法显式计算正运动学与瞬时运动学。
- **接触检测与定位**：提出固定瞬心偏差方法，通过比较理论运动与实际运动之间的偏差来检测外部接触。

### 实验设置与关键结果
- **优化求解**：将接触位置估计转化为非线性最小二乘优化问题。
- **仿真验证**：结果表明，该方法能够准确估计接触位置，验证了模型与算法的有效性。

### 结论
本文为软体机器人的接触感知提供了一种基于运动学偏差的解决方案，为后续控制与轨迹规划奠定了基础。

## Overview
Soft robots offer an alternative approach to manipulate inside the constrained space while maintaining the safe interaction with the external environment. Due to its adaptable compliance characteristic, external contact force can easily deform the robot shapes and lead to undesired robot kinematic and dynamic properties. Accurate contact detection and contact position estimation are of critical importance for soft robot modeling, control, trajectory planning, and eventually affect the success of task completion. In this paper, we focus on the study of 1-DoF soft pneumatic bellow bending actuator, which is one of the fundamental components to construct complex, multi-DoF soft robots. This 1-DoF soft robot is modeled through the integral representation of the spacial curve. The direct and instantaneous kinematics are calculated explicitly through a modal method. The fixed centrode deviation (FCD) method is used to to detect the external contact and estimate contact location. Simulation results indicate that the contact location can be accurately estimated by solving a nonlinear least square optimization problem.

## Overview
Soft robots offer an alternative approach to manipulate inside the constrained space while maintaining the safe interaction with the external environment. Due to its adaptable compliance characteristic, external contact force can easily deform the robot shapes and lead to undesired robot kinematic and dynamic properties. Accurate contact detection and contact position estimation are of critical importance for soft robot modeling, control, trajectory planning, and eventually affect the success of task completion. In this paper, we focus on the study of 1-DoF soft pneumatic bellow bending actuator, which is one of the fundamental components to construct complex, multi-DoF soft robots. This 1-DoF soft robot is modeled through the integral representation of the spacial curve. The direct and instantaneous kinematics are calculated explicitly through a modal method. The fixed centrode deviation (FCD) method is used to detect the external contact and estimate contact location. Simulation results indicate that the contact location can be accurately estimated by solving a nonlinear least square optimization problem.

## Content
Soft robots offer an alternative approach to manipulate inside the constrained space while maintaining the safe interaction with the external environment. Due to its adaptable compliance characteristic, external contact force can easily deform the robot shapes and lead to undesired robot kinematic and dynamic properties. Accurate contact detection and contact position estimation are of critical importance for soft robot modeling, control, trajectory planning, and eventually affect the success of task completion. In this paper, we focus on the study of 1-DoF soft pneumatic bellow bending actuator, which is one of the fundamental components to construct complex, multi-DoF soft robots. This 1-DoF soft robot is modeled through the integral representation of the spacial curve. The direct and instantaneous kinematics are calculated explicitly through a modal method. The fixed centrode deviation (FCD) method is used to detect the external contact and estimate contact location. Simulation results indicate that the contact location can be accurately estimated by solving a nonlinear least square optimization problem.

## 参考
- http://arxiv.org/abs/1906.11654v1

## 개요
본 연구는 복잡한 다자유도 소프트 로봇을 구성하는 기본 단위인 1자유도 공압 벨로우즈 굽힘 액추에이터에 초점을 맞춘다. 공간 곡선의 적분 표현을 통해 소프트 로봇을 모델링하고, 모드 방법을 사용하여 정기구학 및 순간기구학을 명시적으로 계산한다. 외부 접촉으로 인한 변형 및 동역학 변화에 대응하기 위해, 연구는 고정 순간 중심 편차 방법을 도입하고, 비선형 최소제곱 최적화 문제를 해결하여 시뮬레이션에서 접촉 위치의 정확한 추정을 달성한다.

## 핵심 내용
### 연구 배경 및 목표
소프트 로봇은 유연한 특성 덕분에 제한된 공간에서 안전하게 작동할 수 있지만, 외부 접촉력은 변형을 쉽게 유발하여 기구학 및 동역학 성능에 영향을 미친다. 접촉을 정확히 감지하고 위치를 추정하는 것은 모델링, 제어 및 작업 완료에至关重要하다.

### 방법 및 아키텍처
- **연구 대상**: 다자유도 소프트 로봇을 구축하기 위한 기본 구성 요소로서의 1자유도 공압 벨로우즈 굽힘 액추에이터.
- **기구학 모델링**: 공간 곡선의 적분 표현을 사용하고, 모드 방법을 통해 정기구학 및 순간기구학을 명시적으로 계산.
- **접촉 감지 및 위치 추정**: 이론적 운동과 실제 운동 간의 편차를 비교하여 외부 접촉을 감지하는 고정 순간 중심 편차 방법을 제안.

### 실험 설정 및 주요 결과
- **최적화 해법**: 접촉 위치 추정을 비선형 최소제곱 최적화 문제로 변환.
- **시뮬레이션 검증**: 결과는 이 방법이 접촉 위치를 정확히 추정할 수 있음을 보여주며, 모델과 알고리즘의 유효성을 검증.

### 결론
본 논문은 소프트 로봇의 접촉 인식을 위한 기구학 편차 기반 솔루션을 제공하며, 후속 제어 및 궤적 계획을 위한 기초를 마련한다.
