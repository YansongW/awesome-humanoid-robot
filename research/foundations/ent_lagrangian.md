---
$id: ent_lagrangian
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Lagrangian
  zh: 拉格朗日量
  ko: 라그랑지안
summary:
  en: A scalar function that encodes the dynamics of a system through the difference (or generalized combination) of kinetic
    and potential energy, from which equations of motion follow via a variational principle.
  zh: 通过动能与势能之差（或更一般组合）刻画系统动力学，并由变分原理导出运动方程的标量函数。
  ko: 울성 및 위치 에너지의 차이(또는 일반화된 조합)로 시스템 역학을 기술하고 변분 원리로부터 운 동 방정식을 유도하는 스칼라 함수.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- mechanics
- classical_mechanics
- variational_principle
- lagrangian
- energy
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: high
  notes: Standard foundational knowledge; reviewed against standard references. Body backfilled from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_goldstein_poole_safko_2002
  type: other
  title: H. Goldstein, C. Poole, and J. Safko, Classical Mechanics, 3rd ed., Addison-Wesley, 2002
  url: https://doi.org/10.2307/2522307
  date: '2002-01-01'
  accessed_at: '2026-06-25'
related_entities:
- id: ent_newton_euler_equations
  relationship: is_alternative_to
  description:
    en: Newton-Euler equations give the same dynamics as the Lagrangian formalism for rigid-body systems, but via force and
      torque balances.
    zh: 牛顿-欧拉方程与拉格朗日形式对刚体系统给出相同动力学，但直接通过力与力矩平衡列写。
    ko: 뉴턴-오일러 방정식은 강체 시스템에 대해 라그랑지안 형식과 동일한 역학을 주지만 힘과 토크 균형을 통해 직접 유도합니다.
---
## 概述
通过动能与势能之差（或更一般组合）刻画系统动力学，并由变分原理导出运动方程的标量函数。

## 核心内容
### 拉格朗日量的定义与定位
拉格朗日量属于 **formalism** 类型。 所属领域包括：00_foundations。 价值链层级：foundations。 通过动能与势能之差（或更一般组合）刻画系统动力学，并由变分原理导出运动方程的标量函数。 英文名称为 *Lagrangian*。 韩文名称为 *라그랑지안*。

### 拉格朗日量的数学与原理基础
拉格朗日量建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，拉格朗日量通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现拉格朗日量时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
拉格朗日量可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- mechanics
- classical_mechanics
- variational_principle
- lagrangian
- energy

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键formalism之一，拉格朗日量在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [H. Goldstein, C. Poole, and J. Safko, Classical Mechanics, 3rd ed., Addison-Wesley, 2002](https://doi.org/10.2307/2522307)

