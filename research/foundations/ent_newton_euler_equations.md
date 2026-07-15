---
$id: ent_newton_euler_equations
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: equation
names:
  en: Newton-Euler equations
  zh: 牛顿-欧拉方程
  ko: 뉴턴-오일러 방정식
summary:
  en: A set of coupled force and torque balance equations that describe the motion of a rigid body or articulated multibody
    system.
  zh: '核心内容 ### 牛顿-欧拉方程的定义与定位 牛顿-欧拉方程属于 **equation** 类型。 所属领域包括：00_foundations。 价值链层级：foundations。 描述刚体或铰接多体系统运动的一组耦合的力平衡与力矩平衡方程。
    英文名称为 *Newton-Euler equations*。 韩文名称为 *뉴턴-오일러 방정식*。'
  ko: 강철 또는 관절 연결 다물체 시스템의 운전을 기술하는 결합된 힘 및 토크 평형 방정식 집합.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- dynamics
- rigid_body
- multibody
- newton_euler
- equations_of_motion
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_featherstone_2014
  type: other
  title: R. Featherstone, Rigid Body Dynamics Algorithms, Springer, 2014
  url: https://doi.org/10.1007/978-1-4899-7560-7
  date: '2014-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_lagrangian
  relationship: is_alternative_to
  description:
    en: The Newton-Euler and Lagrangian formalisms are equivalent for rigid-body systems; the former emphasizes force/torque
      balances, the latter emphasizes energy.
    zh: 牛顿-欧拉形式与拉格朗日形式对刚体系统等价；前者强调力/力矩平衡，后者强调能量。
    ko: 뉴턴-오일러 형식과 라그랑지안 형식은 강체 시스템에서 동치입니다. 전자는 힘/토크 균형에, 후자는 에너지에 초점을 맞춥니다.
---

## 概述
描述刚体或铰接多体系统运动的一组耦合的力平衡与力矩平衡方程。

## 核心内容
### 牛顿-欧拉方程的定义与定位
牛顿-欧拉方程属于 **equation** 类型。 所属领域包括：00_foundations。 价值链层级：foundations。 描述刚体或铰接多体系统运动的一组耦合的力平衡与力矩平衡方程。 英文名称为 *Newton-Euler equations*。 韩文名称为 *뉴턴-오일러 방정식*。

### 牛顿-欧拉方程的数学与原理基础
牛顿-欧拉方程建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，牛顿-欧拉方程通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现牛顿-欧拉方程时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
牛顿-欧拉方程可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- dynamics
- rigid_body
- multibody
- newton_euler
- equations_of_motion

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键equation之一，牛顿-欧拉方程在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [R. Featherstone, Rigid Body Dynamics Algorithms, Springer, 2014](https://doi.org/10.1007/978-1-4899-7560-7)


