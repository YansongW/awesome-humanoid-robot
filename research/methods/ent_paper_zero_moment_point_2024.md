---
$id: ent_paper_zero_moment_point_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Zero Moment Point
  zh: 零力矩点
  ko: Zero Moment Point
summary:
  en: Foundational stability criterion for bipedal walking and balance control.
  zh: 双足行走和平衡控制的基础稳定性判据。
  ko: 이족 보행 및 균형 제어의 기초적 안정성 기준.
domains:
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- bipedal
- control
- method
- stability
- zmp
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-08.md#8.4.4 零力矩点（ZMP）与动态平衡 by scripts/backfill_nonpaper_entries.py. Body backfilled
    from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_001
  type: website
  title: Zero Moment Point
  url: https://en.wikipedia.org/wiki/Zero_moment_point
  date: '2024'
  accessed_at: '2026-07-02'
---
## 概述
双足行走和平衡控制的基础稳定性判据。

## 核心内容
### 零力矩点的定义与定位
零力矩点属于 **method** 类型。 所属领域包括：07_ai_models_algorithms, 06_design_engineering。 价值链层级：intelligence, midstream。 双足行走和平衡控制的基础稳定性判据。 英文名称为 *Zero Moment Point*。 韩文名称为 *Zero Moment Point*。

### 零力矩点的数学与原理基础
零力矩点建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，零力矩点通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现零力矩点时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
零力矩点可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- bipedal
- control
- method
- stability
- zmp

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键method之一，零力矩点在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [Zero Moment Point](https://en.wikipedia.org/wiki/Zero_moment_point)

