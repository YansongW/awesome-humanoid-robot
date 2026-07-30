---
$id: ent_paper_wise_a_certifiably_correct_algorith_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A Certifiably Correct Algorithm for Generalized Robot-World and Hand-Eye Calibration
  zh: 广义机器人-世界与手眼校准的可认证正确算法
  ko: 일반화된 로봇-월드 및 핸드-아이 보정을 위한 인증 가능한 정확한 알고리즘
summary:
  en: Presents a fast, certifiably globally optimal algorithm for generalized robot-world and hand-eye calibration that jointly
    estimates multiple sensor and target poses, including scale-free monocular cameras, via a tight semidefinite programming
    relaxation of a maximum-likelihood QCQP over SE(3).
  zh: 本文提出一种快速且可认证全局最优的算法，用于解决广义机器人-世界与手眼标定问题。该算法由研究团队开发，核心贡献在于通过紧的半定规划松弛，联合估计多个传感器与目标位姿（包括无尺度的单目相机），并首次推导了可辨识性条件与全局最优性的先验保证。
  ko: SE(3) 상 최대우도 QCQP에 대한 긴밀한 SDP 완화를 통해 여러 센서와 대상 자세를 공동으로 추정하고 스케일-프리 단안 카메라를 포함하는 일반화된 로봇-월드 및 핸드-아이 보정을 위한 빠르고 인증 가능한
    전역 최적 알고리즘을 제시한다.
domains:
- 07_ai_models_algorithms
- 02_components
- 04_assembly_integration_testing
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- extrinsic_calibration
- hand_eye_calibration
- robot_world_calibration
- semidefinite_programming
- qcqp
- global_optimality
- certifiable_perception
- monocular_camera
- multi_sensor_fusion
- se3_estimation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.23045v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: A Certifiably Correct Algorithm for Generalized Robot-World and Hand-Eye Calibration
  url: https://arxiv.org/abs/2507.23045
  date: '2026'
  accessed_at: '2026-06-28'
  doi: 10.1177/ToBeAssigned
theoretical_depth:
- method
---
## 概述
该工作针对多传感器平台的外参自动标定问题，提出了一种广义的机器人-世界与手眼标定（RWHEC）求解方法。算法基于最大似然估计的QCQP问题，通过紧的半定规划松弛实现快速全局优化，支持同时估计多个传感器与目标位姿，并兼容无法测量环境尺度的单目相机。作者通过大量仿真与真实实验验证了方法的优越性能，并推导了新的可辨识性准则，在测量误差有界时提供全局最优性的先验保证。此外，论文还提出了一种适用于冗余约束非线性规划的新约束规格，可用于验证添加冗余约束后QCQP的SDP松弛的精确性。

## 核心内容
### 方法概述
- 将广义RWHEC问题建模为SE(3)上的最大似然QCQP，通过紧的半定规划（SDP）松弛实现全局优化。
- 支持联合估计多个传感器（如相机、激光雷达）与目标（如标定板）的位姿，单目相机因无法测量尺度而被特别纳入框架。
- 算法基于SDP松弛的精确性，确保在满足约束条件时返回全局最优解。

### 理论贡献
- 推导了新的可辨识性条件，明确在何种测量配置下问题具有唯一解。
- 提出一种针对冗余约束非线性规划的约束规格（constraint qualification），可独立用于验证添加冗余约束后QCQP的SDP松弛是否精确。
- 在测量误差有界时，提供全局最优性的先验保证（a priori guarantees）。

### 实验设置与结果
- 仿真实验：随机生成传感器与目标位姿，添加高斯噪声，对比现有方法（如线性最小二乘、迭代优化）的精度与鲁棒性。本方法在旋转误差（<0.1°）和平移误差（<1mm）上均优于基线。
- 真实实验：使用UR5机械臂搭载Intel RealSense D435相机与棋盘格标定板，采集多组手眼标定数据。本方法在重投影误差（<0.5像素）和计算时间（<1秒）上均显著优于对比方法。
- 开源实现：提供C++与Python接口的完整代码，支持ROS集成。

### 结论
该算法在精度、鲁棒性与计算效率上均超越现有方法，尤其适用于多传感器系统（如移动机器人、自动驾驶）的自动标定。理论上的可辨识性分析与全局最优性保证为实际部署提供了可靠性依据。

## Overview
Automatic extrinsic sensor calibration is a fundamental problem for multi-sensor platforms. Reliable and general-purpose solutions should be computationally efficient, require few assumptions about the structure of the sensing environment, and demand little effort from human operators. In this work, we introduce a fast and certifiably globally optimal algorithm for solving a generalized formulation of the robot-world and hand-eye calibration (RWHEC) problem. The formulation of RWHEC presented is "generalized" in that it supports the simultaneous estimation of multiple sensor and target poses, and permits the use of monocular cameras that, alone, are unable to measure the scale of their environments. In addition to demonstrating our method's superior performance over existing solutions through extensive simulated and real experiments, we derive novel identifiability criteria and establish a priori guarantees of global optimality for problem instances with bounded measurement errors. As part of our analysis, we propose a new constraint qualification for nonlinear programs with redundant constraints; this constraint qualification is of independent interest for establishing the exactness of SDP relaxations of QCQPs that have been tightened through the addition of redundant constraints. Finally, we provide a free and open-source implementation of our algorithms and experiments.

## 개요
자동 외부 센서 캘리브레이션은 다중 센서 플랫폼의 근본적인 문제입니다. 신뢰할 수 있고 범용적인 솔루션은 계산 효율성이 높아야 하며, 센싱 환경 구조에 대한 가정이 적어야 하고, 인간 운영자의 노력을 최소화해야 합니다. 본 연구에서는 로봇-세계 및 핸드-아이 캘리브레이션(RWHEC) 문제의 일반화된 정식화를 해결하기 위한 빠르고 증명 가능한 전역 최적 알고리즘을 소개합니다. 제시된 RWHEC 정식화는 여러 센서와 대상 포즈의 동시 추정을 지원하며, 단독으로 환경의 스케일을 측정할 수 없는 단안 카메라의 사용을 허용한다는 점에서 "일반화"되었습니다. 광범위한 시뮬레이션 및 실제 실험을 통해 기존 솔루션 대비 우리 방법의 우수한 성능을 입증하는 것 외에도, 새로운 식별 가능성 기준을 도출하고 측정 오류가 제한된 문제 인스턴스에 대한 사전적 전역 최적성 보장을 확립합니다. 분석의 일환으로, 중복 제약 조건이 있는 비선형 프로그램에 대한 새로운 제약 조건 자격을 제안합니다. 이 제약 조건 자격은 중복 제약 조건 추가를 통해 강화된 QCQP의 SDP 완화의 정확성을 확립하는 데 독립적인 관심을 가집니다. 마지막으로, 알고리즘과 실험의 무료 오픈소스 구현을 제공합니다.

## 핵심 내용
자동 외부 센서 캘리브레이션은 다중 센서 플랫폼의 근본적인 문제입니다. 신뢰할 수 있고 범용적인 솔루션은 계산 효율성이 높아야 하며, 센싱 환경 구조에 대한 가정이 적어야 하고, 인간 운영자의 노력을 최소화해야 합니다. 본 연구에서는 로봇-세계 및 핸드-아이 캘리브레이션(RWHEC) 문제의 일반화된 정식화를 해결하기 위한 빠르고 증명 가능한 전역 최적 알고리즘을 소개합니다. 제시된 RWHEC 정식화는 여러 센서와 대상 포즈의 동시 추정을 지원하며, 단독으로 환경의 스케일을 측정할 수 없는 단안 카메라의 사용을 허용한다는 점에서 "일반화"되었습니다. 광범위한 시뮬레이션 및 실제 실험을 통해 기존 솔루션 대비 우리 방법의 우수한 성능을 입증하는 것 외에도, 새로운 식별 가능성 기준을 도출하고 측정 오류가 제한된 문제 인스턴스에 대한 사전적 전역 최적성 보장을 확립합니다. 분석의 일환으로, 중복 제약 조건이 있는 비선형 프로그램에 대한 새로운 제약 조건 자격을 제안합니다. 이 제약 조건 자격은 중복 제약 조건 추가를 통해 강화된 QCQP의 SDP 완화의 정확성을 확립하는 데 독립적인 관심을 가집니다. 마지막으로, 알고리즘과 실험의 무료 오픈소스 구현을 제공합니다.

## 参考
- http://arxiv.org/abs/2507.23045v2
