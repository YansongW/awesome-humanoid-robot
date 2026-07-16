---
$id: ent_paper_jallet_proxnlp_a_primal_dual_augmente_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ProxNLP: a primal-dual augmented Lagrangian solver for nonlinear programming in Robotics and beyond'
  zh: ProxNLP：面向机器人及更广领域的非线性规划原始-对偶增广拉格朗日求解器
  ko: 'ProxNLP: 로보틱스 및 그 이상의 비선형 프로그래밍을 위한 primal-dual augmented Lagrangian 솔버'
summary:
  en: This paper presents a primal-dual augmented Lagrangian method for inequality-constrained nonlinear programs on manifolds
    and introduces proxnlp, an open-source C++ implementation with Eigen, Pinocchio, and CasADi bindings, validated on robot
    examples including Talos pose generation.
  zh: 本文提出了一种流形上不等式约束非线性规划的原始-对偶增广拉格朗日方法，并介绍了开源C++实现proxnlp，该实现具有Eigen、Pinocchio和CasADi绑定，并在包括Talos姿态生成在内的机器人示例上进行了验证。
  ko: 본 논문은 다양체 상에서 부등식 제약이 있는 비선형 계획을 위한 primal-dual augmented Lagrangian 방법을 제시하고, Eigen, Pinocchio, CasADi 바인딩을 갖춘 오픈소스
    C++ 구현체인 proxnlp를 소개하며, Talos 자세 생성을 포함한 로봇 예제에서 검증한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- proxnlp
- augmented_lagrangian
- primal_dual
- nonlinear_programming
- manifold_optimization
- lie_groups
- optimization_solver
- talos
- humanoid_pose_generation
- trajectory_optimization
- inverse_geometry
- pinocchio
- casadi
- eigen
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.02109v1.
sources:
- id: src_001
  type: paper
  title: 'ProxNLP: a primal-dual augmented Lagrangian solver for nonlinear programming in Robotics and beyond'
  url: https://arxiv.org/abs/2210.02109
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
Mathematical optimization is the workhorse behind several aspects of modern robotics and control. In these applications, the focus is on constrained optimization, and the ability to work on manifolds (such as the classical matrix Lie groups), along with a specific requirement for robustness and speed. In recent years, augmented Lagrangian methods have seen a resurgence due to their robustness and flexibility, their connections to (inexact) proximal-point methods, and their interoperability with Newton or semismooth Newton methods. In the sequel, we present primal-dual augmented Lagrangian method for inequality-constrained problems on manifolds, which we introduced in our recent work, as well as an efficient C++ implementation suitable for use in robotics applications and beyond.

## 核心内容
Mathematical optimization is the workhorse behind several aspects of modern robotics and control. In these applications, the focus is on constrained optimization, and the ability to work on manifolds (such as the classical matrix Lie groups), along with a specific requirement for robustness and speed. In recent years, augmented Lagrangian methods have seen a resurgence due to their robustness and flexibility, their connections to (inexact) proximal-point methods, and their interoperability with Newton or semismooth Newton methods. In the sequel, we present primal-dual augmented Lagrangian method for inequality-constrained problems on manifolds, which we introduced in our recent work, as well as an efficient C++ implementation suitable for use in robotics applications and beyond.

## 参考
- http://arxiv.org/abs/2210.02109v1

## Overview
Mathematical optimization is the workhorse behind several aspects of modern robotics and control. In these applications, the focus is on constrained optimization, and the ability to work on manifolds (such as the classical matrix Lie groups), along with a specific requirement for robustness and speed. In recent years, augmented Lagrangian methods have seen a resurgence due to their robustness and flexibility, their connections to (inexact) proximal-point methods, and their interoperability with Newton or semismooth Newton methods. In the sequel, we present primal-dual augmented Lagrangian method for inequality-constrained problems on manifolds, which we introduced in our recent work, as well as an efficient C++ implementation suitable for use in robotics applications and beyond.

## Content
Mathematical optimization is the workhorse behind several aspects of modern robotics and control. In these applications, the focus is on constrained optimization, and the ability to work on manifolds (such as the classical matrix Lie groups), along with a specific requirement for robustness and speed. In recent years, augmented Lagrangian methods have seen a resurgence due to their robustness and flexibility, their connections to (inexact) proximal-point methods, and their interoperability with Newton or semismooth Newton methods. In the sequel, we present primal-dual augmented Lagrangian method for inequality-constrained problems on manifolds, which we introduced in our recent work, as well as an efficient C++ implementation suitable for use in robotics applications and beyond.

## 개요
수학적 최적화는 현대 로봇공학 및 제어의 여러 측면을 뒷받침하는 핵심 도구입니다. 이러한 응용 분야에서는 제약 조건이 있는 최적화, 다양체(예: 고전적인 행렬 리 군)에서 작업할 수 있는 능력, 그리고 견고성과 속도에 대한 특정 요구 사항이 중점적으로 다루어집니다. 최근 몇 년간, 증강 라그랑주 방법은 그 견고성과 유연성, (부정확한) 근접점 방법과의 연결성, 그리고 뉴턴 방법 또는 반평활 뉴턴 방법과의 상호 운용성 덕분에 다시 주목받고 있습니다. 이어서, 우리는 최근 연구에서 소개한 다양체 상의 부등식 제약 문제를 위한 원시-쌍대 증강 라그랑주 방법과 로봇공학 응용 및 그 이상에 적합한 효율적인 C++ 구현을 제시합니다.

## 핵심 내용
수학적 최적화는 현대 로봇공학 및 제어의 여러 측면을 뒷받침하는 핵심 도구입니다. 이러한 응용 분야에서는 제약 조건이 있는 최적화, 다양체(예: 고전적인 행렬 리 군)에서 작업할 수 있는 능력, 그리고 견고성과 속도에 대한 특정 요구 사항이 중점적으로 다루어집니다. 최근 몇 년간, 증강 라그랑주 방법은 그 견고성과 유연성, (부정확한) 근접점 방법과의 연결성, 그리고 뉴턴 방법 또는 반평활 뉴턴 방법과의 상호 운용성 덕분에 다시 주목받고 있습니다. 이어서, 우리는 최근 연구에서 소개한 다양체 상의 부등식 제약 문제를 위한 원시-쌍대 증강 라그랑주 방법과 로봇공학 응용 및 그 이상에 적합한 효율적인 C++ 구현을 제시합니다.
