---
$id: ent_paper_thirugnanam_duality_based_convex_optimizat_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Duality-based Convex Optimization for Real-time Obstacle Avoidance between Polytopes with Control Barrier Functions
  zh: 基于对偶的凸优化控制障碍函数实时多面体避障
  ko: 제어 장벽 함수를 이용한 다면체 간 실시간 장애물 회피를 위한 이중성 기반 볼록 최적화
summary:
  en: Proposes a duality-based nonsmooth control barrier function framework that reformulates minimum-distance constraints
    between polytopes into a convex quadratic program, enabling real-time safety-critical obstacle avoidance for control-affine
    nonlinear systems.
  zh: 本文提出一种基于对偶的非光滑控制屏障函数框架，将多面体间最小距离约束重构为凸二次规划问题，实现控制仿射非线性系统的实时安全关键避障。该方法由团队提出，核心贡献在于将传统离线优化问题转化为可实时求解的QP形式，并通过L形（沙发形）机器人在走廊环境中的实验验证了非保守机动能力。
  ko: 제어 아핀 비선형 시스템을 위해 다면체 간 최소 거리 제약을 볼록 이차 계획법으로 재구성하는 이중성 기반 비연속 제어 장벽 함수 프레임워크를 제안하여 실시간 안전 필수 장애물 회피를 가능하게 함.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- intelligence
- knowledge
tags:
- control_barrier_function
- nonsmooth_cbf
- quadratic_programming
- obstacle_avoidance
- polytope
- real_time_control
- safety_critical_control
- nonlinear_control
- motion_planning
- moving_sofa_problem
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2107.08360v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (536 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Duality-based Convex Optimization for Real-time Obstacle Avoidance between Polytopes with Control Barrier Functions
  url: https://arxiv.org/abs/2107.08360
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
针对多面体间避障这一导航难题，传统方法仅能进行离线优化。本文创新性地引入对偶优化问题表示多面体间最小距离，并利用对偶形式的拉格朗日函数构建控制屏障函数，从而将避障约束转化为可实时求解的凸二次规划。该方法在具有非线性动力学的移动沙发（钢琴）问题上实现了紧贴障碍物的非保守机动，并在走廊环境中对L形受控机器人进行了验证。

## 核心内容
### 方法架构
- 提出基于对偶的非光滑控制屏障函数（CBF）框架，将多面体间最小距离约束转化为凸二次规划（QP）问题
- 通过引入对偶优化问题表示多面体间最小距离，利用对偶形式的拉格朗日函数构造CBF
- 将传统离线优化问题转化为实时可解的QP形式，适用于控制仿射非线性系统

### 实验设置
- 验证场景：走廊环境中的L形（沙发形）受控机器人
- 测试任务：移动沙发（钢琴）问题，涉及非线性动力学
- 关键指标：实时性、非保守机动能力

### 关键结果
- 成功实现实时紧贴障碍物的避障控制
- 在非线性动力学条件下完成非保守机动，避免传统方法的保守性
- 通过QP求解器实现实时优化，满足安全关键控制需求

### 结论
该对偶框架有效解决了多面体间实时避障的优化难题，为导航系统提供了可在线部署的安全保障方案。

## Overview
Developing controllers for obstacle avoidance between polytopes is a challenging and necessary problem for navigation in tight spaces. Traditional approaches can only formulate the obstacle avoidance problem as an offline optimization problem. To address these challenges, we propose a duality-based safety-critical optimal control using nonsmooth control barrier functions for obstacle avoidance between polytopes, which can be solved in real-time with a QP-based optimization problem. A dual optimization problem is introduced to represent the minimum distance between polytopes and the Lagrangian function for the dual form is applied to construct a control barrier function. We validate the obstacle avoidance with the proposed dual formulation for L-shaped (sofa-shaped) controlled robot in a corridor environment. We demonstrate real-time tight obstacle avoidance with non-conservative maneuvers on a moving sofa (piano) problem with nonlinear dynamics.

## 参考
- http://arxiv.org/abs/2107.08360v4

## 개요
다면체 간 장애물 회피라는 내비게이션 난제에 대해, 기존 방법은 오프라인 최적화만 가능했습니다. 본 논문은 혁신적으로 쌍대 최적화 문제를 도입하여 다면체 간 최소 거리를 표현하고, 쌍대 형식의 라그랑주 함수를 활용해 제어 장벽 함수를 구축함으로써, 장애물 회피 제약을 실시간으로 풀 수 있는 볼록 2차 계획법으로 변환합니다. 이 방법은 비선형 동역학을 가진 이동 소파(피아노) 문제에서 장애물에 밀착된 비보수적 기동을 구현했으며, 복도 환경에서 L자형 제어 로봇으로 검증되었습니다.

## 핵심 내용
### 방법 구조
- 다면체 간 최소 거리 제약을 볼록 2차 계획법(QP) 문제로 변환하는, 쌍대 기반의 비매끄러운 제어 장벽 함수(CBF) 프레임워크 제안
- 쌍대 최적화 문제를 도입하여 다면체 간 최소 거리를 표현하고, 쌍대 형식의 라그랑주 함수를 활용해 CBF를 구성
- 기존 오프라인 최적화 문제를 실시간으로 풀 수 있는 QP 형태로 변환하여, 제어 아핀 비선형 시스템에 적용 가능

### 실험 설정
- 검증 환경: 복도 환경에서의 L자형(소파형) 제어 로봇
- 테스트 과제: 비선형 동역학을 포함한 이동 소파(피아노) 문제
- 핵심 지표: 실시간성, 비보수적 기동 능력

### 주요 결과
- 장애물에 밀착된 실시간 회피 제어를 성공적으로 구현
- 비선형 동역학 조건에서 비보수적 기동을 완수하여 기존 방법의 보수성을 극복
- QP 솔버를 통한 실시간 최적화로 안전 필수 제어 요구를 충족

### 결론
본 쌍대 프레임워크는 다면체 간 실시간 장애물 회피의 최적화 난제를 효과적으로 해결하며, 내비게이션 시스템에 온라인 배포 가능한 안전 보장 방안을 제공합니다.
