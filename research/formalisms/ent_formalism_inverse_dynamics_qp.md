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
逆动力学二次规划形式化属于 **formalism** 类型。 所属领域包括：07_ai_models_algorithms, 06_design_engineering。 价值链层级：intelligence, midstream。 一种二次规划形式化，通过最小化任务跟踪误差并受浮动基动力学和物理约束，计算广义加速度、接触力和关节力矩。 英文名称为 *Inverse-Dynamics QP Formulation*。 韩文名称为 *역동역학 QP 공식화*。

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
作为人形机器人产业链中的关键formalism之一，逆动力学二次规划形式化在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Hierarchical QP whole-body control: from theory to practice](https://arxiv.org/abs/1910.13329)

