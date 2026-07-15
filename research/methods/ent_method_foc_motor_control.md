---
$id: ent_method_foc_motor_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Field-Oriented Control (FOC)
  zh: 磁场定向控制（FOC）
  ko: 자장 지향 제어(FOC)
summary:
  en: A motor-control method that transforms three-phase currents into a rotating dq reference frame to enable independent
    control of torque and flux, similar to a DC machine.
  zh: 将三相电流变换到旋转的dq坐标系，分别控制转矩与磁通，使交流电机获得类似直流电机的调速性能。
  ko: 삼상 전류를 회전하는 dq 좌표계로 변환하여 토크와 자속을 독립 제어하는 모터 제어 방식.
domains:
- 02_components
layers:
- midstream
functional_roles:
- knowledge
tags:
- method
- chapter_4
- wiki_gap
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: Body backfilled from chapter-04.md#4.5.2 磁场定向控制（FOC）的数学结构 by scripts/backfill_nonpaper_entries.py. Body backfilled
    from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_wiki_extraction
  type: other
  title: Wiki extraction
  date: '2026-07-09'
  accessed_at: '2026-07-09'
---
## 概述
将三相电流变换到旋转的dq坐标系，分别控制转矩与磁通，使交流电机获得类似直流电机的调速性能。

## 核心内容
### 磁场定向控制（FOC）的定义与定位
磁场定向控制（FOC）属于 **method** 类型。 所属领域包括：02_components。 价值链层级：midstream。 将三相电流变换到旋转的dq坐标系，分别控制转矩与磁通，使交流电机获得类似直流电机的调速性能。 英文名称为 *Field-Oriented Control (FOC)*。 韩文名称为 *자장 지향 제어(FOC)*。

### 磁场定向控制（FOC）的数学与原理基础
磁场定向控制（FOC）建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，磁场定向控制（FOC）通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现磁场定向控制（FOC）时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
磁场定向控制（FOC）可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- method
- chapter_4
- wiki_gap

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键method之一，磁场定向控制（FOC）在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- Wiki extraction

