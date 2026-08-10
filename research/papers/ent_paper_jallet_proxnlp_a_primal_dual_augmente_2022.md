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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2210.02109v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (661 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2210.02109v1

## Overview
This work focuses on constrained optimization problems in robotics and control, with particular emphasis on the ability to operate on manifolds (such as classical matrix Lie groups), as well as specific requirements for robustness and speed. The authors propose a primal-dual augmented Lagrangian method for handling inequality-constrained nonlinear programming on manifolds, which is closely related to (inexact) proximal point methods and Newton or semi-smooth Newton methods. Additionally, they develop an open-source C++ implementation called proxNLP, which leverages the Eigen, Pinocchio, and CasADi libraries, and validate its effectiveness through examples such as pose generation for the Talos robot.

## Content
### Method Core
- Proposes a **primal-dual augmented Lagrangian method**, specifically designed for inequality-constrained nonlinear programming problems on manifolds.
- This method combines the robustness of augmented Lagrangian methods with the flexibility of the primal-dual framework, and utilizes (inexact) proximal point methods along with Newton or semi-smooth Newton methods for solving.

### Implementation Details
- Open-source C++ implementation **proxNLP**, relying on the following libraries:
  - **Eigen**: for linear algebra operations.
  - **Pinocchio**: for robot kinematics and dynamics computations.
  - **CasADi**: for automatic differentiation and optimization solving.
- Supports constrained optimization on manifolds, suitable for complex problems in robotics.

### Experimental Validation
- Validated on **pose generation** tasks for the **Talos robot**, demonstrating the method's effectiveness in real robotic scenarios.
- Experimental results indicate advantages in both robustness and computational speed, making it suitable for real-time control applications.

### Conclusion
- This work provides an efficient and robust solver for nonlinear constrained optimization in robotics, and its open-source implementation proxNLP can be widely applied in robotics and other fields.

## 개요
이 연구는 로봇공학 및 제어 분야의 제약 최적화 문제에 초점을 맞추며, 특히 다양체(예: 고전 행렬 리 군)에서의 연산 능력과 강건성 및 속도에 대한 특정 요구를 강조합니다. 저자들은 다양체 상의 부등식 제약 비선형 계획법을 처리하기 위한 원-이중 증강 라그랑주 방법을 제안하며, 이 방법은 (부정확한) 근접 점 방법 및 뉴턴 또는 반평활 뉴턴 방법과 밀접하게 관련됩니다. 또한, 그들은 Eigen, Pinocchio 및 CasADi 라이브러리를 활용하는 오픈소스 C++ 구현인 proxNLP를 개발했으며, Talos 로봇의 자세 생성과 같은 사례를 통해 그 효과를 검증했습니다.

## 핵심 내용
### 방법의 핵심
- 다양체 상의 부등식 제약 비선형 계획법 문제를专门 처리하는 **원-이중 증강 라그랑주 방법**을 제안합니다.
- 이 방법은 증강 라그랑주법의 강건성과 원-이중 프레임워크의 유연성을 결합하며, (부정확한) 근접 점 방법 및 뉴턴 또는 반평활 뉴턴 방법을 활용하여 해를 구합니다.

### 구현 세부 사항
- 오픈소스 C++ 구현인 **proxNLP**는 다음 라이브러리에 의존합니다:
  - **Eigen**: 선형 대수 연산용.
  - **Pinocchio**: 로봇 운동학 및 동역학 계산용.
  - **CasADi**: 자동 미분 및 최적화 해석용.
- 다양체 상의 제약 최적화를 지원하며, 로봇공학의 복잡한 문제에 적합합니다.

### 실험 검증
- **Talos 로봇**의 **자세 생성** 작업에서 검증되어 실제 로봇 시나리오에서의 효과를 입증했습니다.
- 실험 결과, 이 방법은 강건성과 계산 속도 모두에서 장점을 보여 실시간 제어 응용에 적합합니다.

### 결론
- 이 연구는 로봇공학의 비선형 제약 최적화를 위한 효율적이고 강건한 솔버를 제공하며, 오픈소스 구현인 proxNLP는 로봇공학 및 기타 분야에 널리 적용될 수 있습니다.
