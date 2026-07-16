---
$id: ent_formalism_inverse_dynamics_qp
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Inverse-Dynamics QP Formulation
  zh: 逆动力学二次规划形式化
  ko: 역동역학 QP 공식화
summary:
  en: A quadratic-program formulation that computes generalized accelerations, contact forces, and joint torques by minimizing
    task-tracking errors subject to floating-base dynamics and physical constraints.
  zh: 一种二次规划形式化，通过最小化任务跟踪误差并受浮动基动力学和物理约束，计算广义加速度、接触力和关节力矩。
  ko: 부유 기반 동역학과 물리적 제약 조건 하에서 작업 추종 오차를 최소화하여 일반화 가속도, 접촉력, 관절 토크를 계산하는 이차 계획법 공식화이다.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- intelligence
- knowledge
tags:
- inverse_dynamics
- quadratic_programming
- qp_formulation
- floating_base
- humanoid_control
theoretical_depth:
- formalism
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard formulation in WBC literature. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: paper
  title: 'Hierarchical QP whole-body control: from theory to practice'
  url: https://arxiv.org/abs/1910.13329
  date: '2019'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_equation_weighted_task_error_objective
  relationship: includes
  description:
    en: The QP objective includes a weighted sum of task errors.
    zh: QP 目标包含任务误差的加权和。
    ko: QP 목적 함수는 작업 오차의 가중합을 포함한다.
- id: ent_principle_newton_euler_equations
  relationship: derived_from
  description:
    en: The equality constraints encode the Newton-Euler floating-base dynamics.
    zh: 等式约束编码了牛顿-欧拉浮动基动力学。
    ko: 등식 제약은 뉴턴-오일러 부유 기반 동역학을 인코딩한다.
---

## 概述
一种二次规划形式化，通过最小化任务跟踪误差并受浮动基动力学和物理约束，计算广义加速度、接触力和关节力矩。

## 核心内容
### 逆动力学二次规划形式化的定义与定位
逆动力学二次规划形式化属于 **形式化方法** 类型。 所属领域包括：AI 模型与算法, 设计工程。 价值链层级：智能层, midstream。 一种二次规划形式化，通过最小化任务跟踪误差并受浮动基动力学和物理约束，计算广义加速度、接触力和关节力矩。 英文名称为 *Inverse-Dynamics QP Formulation*。 韩文名称为 *역동역학 QP 공식화*。

### 逆动力学二次规划形式化的数学与原理基础
逆动力学二次规划形式化建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，逆动力学二次规划形式化通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现逆动力学二次规划形式化时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
逆动力学二次规划形式化可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- inverse_dynamics
- quadratic_programming
- qp_formulation
- floating_base
- humanoid_control

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键形式化方法之一，逆动力学二次规划形式化在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Hierarchical QP whole-body control: from theory to practice](https://arxiv.org/abs/1910.13329)

## Overview
A quadratic programming formulation that computes generalized accelerations, contact forces, and joint torques by minimizing task tracking errors while subject to floating-base dynamics and physical constraints.

## Content
### Definition and Positioning of the Inverse-Dynamics QP Formulation
The inverse-dynamics quadratic programming formulation belongs to the **formal method** category. Its domains include: AI models and algorithms, design engineering. Value chain level: intelligence layer, midstream. A quadratic programming formulation that computes generalized accelerations, contact forces, and joint torques by minimizing task tracking errors while subject to floating-base dynamics and physical constraints. The English name is *Inverse-Dynamics QP Formulation*. The Korean name is *역동역학 QP 공식화*.

### Mathematical and Theoretical Foundations of the Inverse-Dynamics QP Formulation
The inverse-dynamics quadratic programming formulation is built upon relevant mathematical theories and physical laws. Understanding its assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention should be paid to its input space, output space, objective function, and guarantees of convergence or stability.
In humanoid robots—high-dimensional, underactuated, and strongly coupled systems—the inverse-dynamics QP formulation typically requires a balance between real-time performance, accuracy, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing the inverse-dynamics QP formulation in practice, it is necessary to clarify initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable operation of the algorithm on real platforms.

### Typical Applications and Limitations
The inverse-dynamics QP formulation can be applied to multiple aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptability remain key issues to address in practical deployment.

### Related Tags
- inverse_dynamics
- quadratic_programming
- qp_formulation
- floating_base
- humanoid_control

### Role in Humanoid Robot Systems
As one of the key formal methods in the humanoid robot industry chain, the inverse-dynamics QP formulation plays an important role in system design, performance optimization, and industrial application. It couples with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall machine performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
이차 계획법 정식화의 한 형태로, 부동 기반 동역학과 물리적 제약 조건을 따르면서 작업 추적 오차를 최소화하여 일반화 가속도, 접촉력 및 관절 토크를 계산합니다.

## 핵심 내용
### 역동역학 이차 계획법 정식화의 정의와 위치
역동역학 이차 계획법 정식화는 **형식적 방법** 유형에 속합니다. 관련 분야로는 AI 모델 및 알고리즘, 설계 공학이 있습니다. 가치 사슬 계층은 지능 계층, 중류(midstream)입니다. 작업 추적 오차를 최소화하고 부동 기반 동역학과 물리적 제약 조건을 따르면서 일반화 가속도, 접촉력 및 관절 토크를 계산하는 이차 계획법 정식화입니다. 영어 명칭은 *Inverse-Dynamics QP Formulation*이며, 한국어 명칭은 *역동역학 QP 공식화*입니다.

### 역동역학 이차 계획법 정식화의 수학적 및 원리적 기초
역동역학 이차 계획법 정식화는 관련 수학 이론과 물리 법칙에 기반합니다. 그 전제 조건, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수, 그리고 수렴성 또는 안정성 보장에 주목해야 합니다.
고차원, 저구동, 강결합 시스템인 휴머노이드 로봇에서 역동역학 이차 계획법 정식화는 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 맞춰야 합니다.

### 알고리즘 단계와 구현 요점
역동역학 이차 계획법 정식화를 실제로 구현할 때는 초기화 조건, 반복 규칙, 중단 기준 및 매개변수 최적화 전략을 명확히 해야 합니다.
수치적 방법, 선형 대수 솔버 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 잡음 및 액추에이터 포화와 같은 공학적 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 해야 합니다.

### 전형적인 응용과 한계
역동역학 이차 계획법 정식화는 휴머노이드 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- inverse_dynamics
- quadratic_programming
- qp_formulation
- floating_base
- humanoid_control

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인에서 핵심적인 형식적 방법 중 하나로서, 역동역학 이차 계획법 정식화는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
