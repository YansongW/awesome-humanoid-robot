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
  zh: 本文提出了一种用于流形上不等式约束非线性规划的原对偶增广拉格朗日方法，并介绍了开源C++实现proxNLP，该实现集成了Eigen、Pinocchio和CasADi绑定。通过在Talos机器人姿态生成等实例上的验证，展示了其在机器人学中的鲁棒性和高效性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.02109v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该工作聚焦于机器人学与控制领域中的约束优化问题，特别强调在流形（如经典矩阵李群）上操作的能力，以及对鲁棒性和速度的特定需求。作者提出了一种原对偶增广拉格朗日方法，用于处理流形上的不等式约束非线性规划，该方法与（不精确）近端点方法及牛顿或半光滑牛顿方法紧密相关。此外，他们开发了开源C++实现proxNLP，该实现利用Eigen、Pinocchio和CasADi库，并通过Talos机器人姿态生成等实例验证了其有效性。

## 核心内容
### 方法核心
- 提出一种**原对偶增广拉格朗日方法**，专门针对流形上的不等式约束非线性规划问题。
- 该方法结合了增广拉格朗日法的鲁棒性与原对偶框架的灵活性，并利用（不精确）近端点方法及牛顿或半光滑牛顿方法进行求解。

### 实现细节
- 开源C++实现**proxNLP**，依赖以下库：
  - **Eigen**：用于线性代数运算。
  - **Pinocchio**：用于机器人运动学与动力学计算。
  - **CasADi**：用于自动微分与优化求解。
- 支持流形上的约束优化，适用于机器人学中的复杂问题。

### 实验验证
- 在**Talos机器人**的**姿态生成**任务上进行验证，展示了该方法在真实机器人场景中的有效性。
- 实验结果表明，该方法在鲁棒性和计算速度上均具有优势，适用于实时控制应用。

### 结论
- 该工作为机器人学中的非线性约束优化提供了一种高效且鲁棒的求解器，其开源实现proxNLP可广泛应用于机器人学及其他领域。

## Overview
Mathematical optimization is the workhorse behind several aspects of modern robotics and control. In these applications, the focus is on constrained optimization, and the ability to work on manifolds (such as the classical matrix Lie groups), along with a specific requirement for robustness and speed. In recent years, augmented Lagrangian methods have seen a resurgence due to their robustness and flexibility, their connections to (inexact) proximal-point methods, and their interoperability with Newton or semismooth Newton methods. In the sequel, we present primal-dual augmented Lagrangian method for inequality-constrained problems on manifolds, which we introduced in our recent work, as well as an efficient C++ implementation suitable for use in robotics applications and beyond.

## 개요
수학적 최적화는 현대 로봇공학 및 제어의 여러 측면을 뒷받침하는 핵심 도구입니다. 이러한 응용 분야에서는 제약 조건이 있는 최적화, 다양체(예: 고전적인 행렬 리 군)에서 작업할 수 있는 능력, 그리고 견고성과 속도에 대한 특정 요구 사항이 중점적으로 다루어집니다. 최근 몇 년간, 증강 라그랑주 방법은 그 견고성과 유연성, (부정확한) 근접점 방법과의 연결성, 그리고 뉴턴 방법 또는 반평활 뉴턴 방법과의 상호 운용성 덕분에 다시 주목받고 있습니다. 이어서, 우리는 최근 연구에서 소개한 다양체 상의 부등식 제약 문제를 위한 원시-쌍대 증강 라그랑주 방법과 로봇공학 응용 및 그 이상에 적합한 효율적인 C++ 구현을 제시합니다.

## 핵심 내용
수학적 최적화는 현대 로봇공학 및 제어의 여러 측면을 뒷받침하는 핵심 도구입니다. 이러한 응용 분야에서는 제약 조건이 있는 최적화, 다양체(예: 고전적인 행렬 리 군)에서 작업할 수 있는 능력, 그리고 견고성과 속도에 대한 특정 요구 사항이 중점적으로 다루어집니다. 최근 몇 년간, 증강 라그랑주 방법은 그 견고성과 유연성, (부정확한) 근접점 방법과의 연결성, 그리고 뉴턴 방법 또는 반평활 뉴턴 방법과의 상호 운용성 덕분에 다시 주목받고 있습니다. 이어서, 우리는 최근 연구에서 소개한 다양체 상의 부등식 제약 문제를 위한 원시-쌍대 증강 라그랑주 방법과 로봇공학 응용 및 그 이상에 적합한 효율적인 C++ 구현을 제시합니다.

## 参考
- http://arxiv.org/abs/2210.02109v1
