---
$id: ent_algorithm_active_set_method
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: algorithm
names:
  en: Active-Set Method for Quadratic Programming
  zh: 二次规划的积极集法
  ko: 이차 계획법의 활성 집합법
summary:
  en: An iterative algorithm for solving QPs that maintains a working set of active constraints and solves equality-constrained
    subproblems until optimality conditions are satisfied.
  zh: 一种求解二次规划的迭代算法，维护一个活动约束工作集，并求解等式约束子问题直到满足最优性条件。
  ko: 활성 제약 조건의 작업 집합을 유지하고 최적성 조건이 만족될 때까지 등식 제약 하위 문제를 푸는 QP를 위한 반복 알고리즘이다.
domains:
- 07_ai_models_algorithms
- 00_foundations
layers:
- intelligence
- foundations
functional_roles:
- knowledge
tags:
- active_set
- quadratic_programming
- optimization_algorithm
- kkt_conditions
- humanoid_control
theoretical_depth:
- method
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: high
  notes: Standard QP algorithm. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: paper
  title: Nocedal and Wright, Numerical Optimization
  url: https://link.springer.com/book/10.1007/978-0-387-40065-5
  date: '2006'
  accessed_at: '2026-06-26'
related_entities:
- id: ent_foundation_convex_optimization
  relationship: has_prerequisite
  description:
    en: Active-set methods rely on convex QP theory and KKT conditions.
    zh: 积极集法依赖于凸 QP 理论与 KKT 条件。
    ko: 활성 집합법은 볼록 QP 이론과 KKT 조건에 의존한다.
- id: ent_formalism_inverse_dynamics_qp
  relationship: solves
  description:
    en: Active-set methods can solve the inverse-dynamics QP formulation.
    zh: 积极集法可用于求解逆动力学 QP 形式化。
    ko: 활성 집합법은 역동역학 QP 공식화를 풀 수 있다.
---
## 概述
一种求解二次规划的迭代算法，维护一个活动约束工作集，并求解等式约束子问题直到满足最优性条件。

## 核心内容
### 二次规划的积极集法的定义与定位
二次规划的积极集法属于 **algorithm** 类型。 所属领域包括：07_ai_models_algorithms, 00_foundations。 价值链层级：intelligence, foundations。 一种求解二次规划的迭代算法，维护一个活动约束工作集，并求解等式约束子问题直到满足最优性条件。 英文名称为 *Active-Set Method for Quadratic Programming*。 韩文名称为 *이차 계획법의 활성 집합법*。

### 二次规划的积极集法的数学与原理基础
二次规划的积极集法建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，二次规划的积极集法通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现二次规划的积极集法时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
二次规划的积极集法可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- active_set
- quadratic_programming
- optimization_algorithm
- kkt_conditions
- humanoid_control

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键algorithm之一，二次规划的积极集法在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Nocedal and Wright, Numerical Optimization](https://link.springer.com/book/10.1007/978-0-387-40065-5)

