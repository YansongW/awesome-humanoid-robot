---
$id: ent_method_hierarchical_qp_wbc
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Hierarchical QP Whole-Body Control
  zh: 分层二次规划全身控制
  ko: 계층적 QP 전신 제어
summary:
  en: A whole-body control method that stacks multiple tasks by priority and solves them as a cascade of quadratic programs,
    ensuring higher-priority tasks are fulfilled before lower-priority ones.
  zh: 一种按优先级堆叠多个任务并通过级联二次规划求解的全身控制方法，确保高优先级任务优先满足。
  ko: 여러 작업을 우선순위에 따라 쌓아 올리고 연속된 이차 계획법으로 풀어 높은 우선순위 작업을 먼저 만족시키는 전신 제어 방법이다.
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
- whole_body_control
- hierarchical_qp
- stack_of_tasks
- quadratic_programming
- humanoid_robot
theoretical_depth:
- method
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Based on de Lasa et al. 2010, Herzog et al. 2016, and Kim et al. 2019. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: paper
  title: 'Hierarchical QP whole-body control: from theory to practice'
  url: https://arxiv.org/abs/1910.13329
  date: '2019'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_formalism_inverse_dynamics_qp
  relationship: formalizes
  description:
    en: Hierarchical QP WBC instantiates the inverse-dynamics QP formulation.
    zh: 分层 QP WBC 实例化了逆动力学 QP 形式化。
    ko: 계층적 QP WBC는 역동역학 QP 공식화를 구현한다.
- id: ent_operator_task_jacobian
  relationship: uses
  description:
    en: Each task in the hierarchy is expressed through its task Jacobian.
    zh: 层级中的每个任务都通过其任务 Jacobian 表达。
    ko: 계층의 각 작업은 작업 Jacobian을 통해 표현된다.
---

## 概述
一种按优先级堆叠多个任务并通过级联二次规划求解的全身控制方法，确保高优先级任务优先满足。

## 核心内容
### 分层二次规划全身控制的定义与定位
分层二次规划全身控制属于 **方法** 类型。 所属领域包括：AI 模型与算法, 设计工程。 价值链层级：智能层, midstream。 一种按优先级堆叠多个任务并通过级联二次规划求解的全身控制方法，确保高优先级任务优先满足。 英文名称为 *Hierarchical QP Whole-Body Control*。 韩文名称为 *계층적 QP 전신 제어*。

### 分层二次规划全身控制的数学与原理基础
分层二次规划全身控制建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，分层二次规划全身控制通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现分层二次规划全身控制时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
分层二次规划全身控制可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- whole_body_control
- hierarchical_qp
- stack_of_tasks
- quadratic_programming
- humanoid_robot

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，分层二次规划全身控制在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Hierarchical QP whole-body control: from theory to practice](https://arxiv.org/abs/1910.13329)

## Overview
A whole-body control method that stacks multiple tasks by priority and solves them through cascaded quadratic programming, ensuring that high-priority tasks are satisfied first.

## Content
### Definition and Positioning of Hierarchical Quadratic Programming Whole-Body Control
Hierarchical quadratic programming whole-body control belongs to the **method** type. Its domains include: AI models and algorithms, design engineering. Value chain level: intelligence layer, midstream. A whole-body control method that stacks multiple tasks by priority and solves them through cascaded quadratic programming, ensuring that high-priority tasks are satisfied first. Its English name is *Hierarchical QP Whole-Body Control*. Its Korean name is *계층적 QP 전신 제어*.

### Mathematical and Theoretical Foundations of Hierarchical Quadratic Programming Whole-Body Control
Hierarchical quadratic programming whole-body control is built upon relevant mathematical theories and physical laws. Understanding its assumptions, constraints, and derivation process is a prerequisite for correctly applying this method.
Specifically, attention must be paid to its input space, output space, objective function, and convergence or stability guarantees.
In humanoid robots, which are high-dimensional, underactuated, and strongly coupled systems, hierarchical quadratic programming whole-body control typically requires a balance between real-time performance, precision, and robustness.

### Algorithm Steps and Implementation Key Points
When implementing hierarchical quadratic programming whole-body control in practice, it is necessary to define initialization conditions, iteration rules, stopping criteria, and parameter tuning strategies.
Choosing appropriate numerical methods, linear algebra solvers, and parallel computing strategies can significantly improve computational efficiency and stability.
At the same time, engineering constraints such as model errors, sensor noise, and actuator saturation should be fully considered to ensure reliable algorithm operation on real platforms.

### Typical Applications and Limitations
Hierarchical quadratic programming whole-body control can be applied to various aspects of humanoid robots, including motion planning, control optimization, state estimation, and learning algorithms.
However, its computational complexity, dependence on model accuracy, and online adaptation capability remain key issues to address in practical deployment.

### Related Tags
- whole_body_control
- hierarchical_qp
- stack_of_tasks
- quadratic_programming
- humanoid_robot

### Role in Humanoid Robot Systems
As one of the key methods in the humanoid robot industry chain, hierarchical quadratic programming whole-body control plays an important role in system design, performance optimization, and industrial application. It interacts with multiple subsystems such as perception, decision-making, actuation, energy, structure, and verification, collectively determining overall robot performance. Related research and applications are continuously advancing to further improve its reliability, efficiency, and cost-effectiveness in real-world scenarios.

## 개요
우선순위에 따라 여러 작업을 스택으로 쌓고, 계층적 2차 계획법을 통해 해를 구하는 전신 제어 방법으로, 높은 우선순위의 작업이 먼저 충족되도록 보장합니다.

## 핵심 내용
### 계층적 2차 계획법 전신 제어의 정의와 위치
계층적 2차 계획법 전신 제어는 **방법** 유형에 속합니다. 관련 분야로는 AI 모델 및 알고리즘, 설계 공학이 있습니다. 가치 사슬 계층은 지능 계층, 중류(midstream)에 해당합니다. 우선순위에 따라 여러 작업을 스택으로 쌓고, 계층적 2차 계획법을 통해 해를 구하는 전신 제어 방법으로, 높은 우선순위의 작업이 먼저 충족되도록 보장합니다. 영어 명칭은 *Hierarchical QP Whole-Body Control*입니다. 한국어 명칭은 *계층적 QP 전신 제어*입니다.

### 계층적 2차 계획법 전신 제어의 수학적 및 원리적 기초
계층적 2차 계획법 전신 제어는 관련 수학 이론과 물리 법칙에 기반합니다. 그 전제 가정, 제약 조건 및 유도 과정을 이해하는 것이 이 방법을 올바르게 적용하기 위한 전제입니다.
구체적으로는 입력 공간, 출력 공간, 목적 함수, 그리고 수렴성 또는 안정성 보장에 주목해야 합니다.
고차원, 저구동, 강결합 시스템인 휴머노이드 로봇에서 계층적 2차 계획법 전신 제어는 일반적으로 실시간성, 정밀도 및 강건성 사이에서 균형을 유지해야 합니다.

### 알고리즘 단계와 구현 요점
계층적 2차 계획법 전신 제어를 실제로 구현할 때는 초기화 조건, 반복 규칙, 중단 기준 및 매개변수 튜닝 전략을 명확히 해야 합니다.
수치 방법, 선형 대수 해석기 및 병렬 계산 전략을 합리적으로 선택하면 계산 효율성과 안정성을 크게 향상시킬 수 있습니다.
동시에 모델 오차, 센서 노이즈 및 액추에이터 포화와 같은 공학적 제약을 충분히 고려하여 알고리즘이 실제 플랫폼에서 안정적으로 작동하도록 보장해야 합니다.

### 대표적인 응용과 한계
계층적 2차 계획법 전신 제어는 휴머노이드 로봇의 운동 계획, 제어 최적화, 상태 추정 및 학습 알고리즘 등 여러 단계에 적용될 수 있습니다.
그러나 계산 복잡성, 모델 정밀도에 대한 의존성 및 온라인 적응 능력은 실제 배치에서 중점적으로 해결해야 할 문제입니다.

### 관련 태그
- whole_body_control
- hierarchical_qp
- stack_of_tasks
- quadratic_programming
- humanoid_robot

### 휴머노이드 로봇 시스템에서의 역할
휴머노이드 로봇 산업 체인에서 핵심 방법 중 하나로서, 계층적 2차 계획법 전신 제어는 시스템 설계, 성능 최적화 및 산업화 응용에서 중요한 역할을 합니다. 이는 인식, 의사 결정, 실행, 에너지, 구조 및 검증 등 여러 하위 시스템과 상호 결합되어 전체 기계 성능을 결정합니다. 관련 연구와 응용은 실제 시나리오에서의 신뢰성, 효율성 및 경제성을 더욱 향상시키기 위해 지속적으로 추진되고 있습니다.
