---
$id: ent_method_field_oriented_control
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: method
names:
  en: Field-Oriented Control
  zh: 磁场定向控制
  ko: 전계 지향 제어
summary:
  en: A motor control technique that transforms three-phase stator currents into a rotating d-q reference frame aligned with
    the rotor flux, enabling independent torque and flux control.
  zh: 一种电机控制技术，将三相定子电流变换到与转子磁链对齐的旋转 d-q 坐标系，实现转矩与磁链的解耦控制。
  ko: 3상 정자 전류를 회전자 자속에 맞춘 d-q 좌표계로 변환하여 토크와 자속을 독립적으로 제어하는 모터 제어 기법.
domains:
- 02_components
- 07_ai_models_algorithms
layers:
- upstream
functional_roles:
- knowledge
theoretical_depth:
- method
tags:
- motor
- pmsm
- bldc
- servo
- current_control
- actuator
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Body backfilled from chapter-04.md#4.5.2 磁场定向控制（FOC）的数学结构 by scripts/backfill_nonpaper_entries.py. Body backfilled
    from entity metadata by scripts/backfill_critical_entities.py.
sources:
- id: src_mohan_2003
  type: other
  title: 'N. Mohan, Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink, Wiley, 2013'
  url: https://doi.org/10.1002/9781118704810
  date: '2013-01-01'
  accessed_at: '2026-07-09'
- id: src_krause_wasynczuk_sudhoff_2013
  type: other
  title: P. C. Krause, O. Wasynczuk, and S. D. Sudhoff, Analysis of Electric Machinery and Drive Systems, 3rd ed., IEEE Press/Wiley,
    2013
  url: https://doi.org/10.1002/9781118526030
  date: '2013-01-01'
  accessed_at: '2026-07-09'
related_entities:
- id: ent_component_rotary_actuator_2024
  relationship: applies_to
  description:
    en: FOC is widely used inside rotary actuator servo drives for PMSM/BLDC motors in humanoid joints.
    zh: FOC 广泛用于人形机器人关节旋转执行器中的 PMSM/BLDC 伺服驱动。
- id: ent_method_pid_control
  relationship: requires
  description:
    en: FOC typically uses PI/PID current controllers in the d-q frame to regulate flux and torque currents.
    zh: FOC 通常在 d-q 坐标系中使用 PI/PID 电流控制器调节磁链电流与转矩电流。
---

## 概述
一种电机控制技术，将三相定子电流变换到与转子磁链对齐的旋转 d-q 坐标系，实现转矩与磁链的解耦控制。

## 核心内容
### 磁场定向控制的定义与定位
磁场定向控制属于 **方法** 类型。 所属领域包括：零部件, AI 模型与算法。 价值链层级：上游。 一种电机控制技术，将三相定子电流变换到与转子磁链对齐的旋转 d-q 坐标系，实现转矩与磁链的解耦控制。 英文名称为 *Field-Oriented Control*。 韩文名称为 *전계 지향 제어*。

### 磁场定向控制的数学与原理基础
磁场定向控制建立在相关数学理论与物理规律之上。理解其前提假设、约束条件与推导过程，是正确应用该方法的前提。
具体而言，需要关注其输入空间、输出空间、目标函数以及收敛性或稳定性保证。
在人形机器人这一高维、欠驱动、强耦合系统中，磁场定向控制通常需要在实时性、精度与鲁棒性之间取得平衡。

### 算法步骤与实现要点
在实际实现磁场定向控制时，需要明确初始化条件、迭代规则、停止准则以及参数调优策略。
合理选择数值方法、线性代数求解器与并行计算策略，能够显著提升计算效率与稳定性。
同时，应充分考虑模型误差、传感器噪声与执行器饱和等工程约束，确保算法在真实平台上可靠运行。

### 典型应用与局限性
磁场定向控制可应用于人形机器人的运动规划、控制优化、状态估计与学习算法等多个环节。
然而，其计算复杂度、对模型精度的依赖以及在线适应能力仍是实际部署中需要重点解决的问题。

### 相关标签
- motor
- pmsm
- bldc
- servo
- current_control
- actuator

### 在人形机器人系统中的作用
作为人形机器人产业链中的关键方法之一，磁场定向控制在系统设计、性能优化和产业化应用中扮演着重要角色。它与感知、决策、执行、能源、结构与验证等多个子系统相互耦合，共同决定了整机性能。相关研究与应用正在持续推进，以进一步提升其在实际场景中的可靠性、效率和经济性。

## 参考
- [N. Mohan, Advanced Electric Drives: Analysis, Control, and Modeling Using MATLAB/Simulink, Wiley, 2013](https://doi.org/10.1002/9781118704810)
- [P. C. Krause, O. Wasynczuk, and S. D. Sudhoff, Analysis of Electric Machinery and Drive Systems, 3rd ed., IEEE Press/Wiley, 2013](https://doi.org/10.1002/9781118526030)


