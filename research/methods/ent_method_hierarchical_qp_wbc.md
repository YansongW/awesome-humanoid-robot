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
分层二次规划全身控制属于 **method** 类型。 所属领域包括：07_ai_models_algorithms, 06_design_engineering。 价值链层级：intelligence, midstream。 一种按优先级堆叠多个任务并通过级联二次规划求解的全身控制方法，确保高优先级任务优先满足。 英文名称为 *Hierarchical QP Whole-Body Control*。 韩文名称为 *계층적 QP 전신 제어*。

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
作为人形机器人产业链中的关键method之一，分层二次规划全身控制在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Hierarchical QP whole-body control: from theory to practice](https://arxiv.org/abs/1910.13329)

