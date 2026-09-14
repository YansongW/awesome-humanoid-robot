---
$id: ent_paper_song_balancing_of_humanoid_with_obj_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Balancing of Humanoid with Object Mass: Trade-off Analyses and Lifting Control'
  zh: 'Balancing of Humanoid with Object Mass: Trade-off Analyses and Lifting Control'
  ko: 'Balancing of Humanoid with Object Mass: Trade-off Analyses and Lifting Control'
summary:
  en: The demand for humanoid loco-manipulation tasks with an object has recently increased, and most existing control approaches
    for stability in such tasks rely on heuristics or machine-learning techniques. This study rigorously analyzes and exploits
    the dynamic effects of the object mass on balance stability. By formulating the object mass parameters in the whole-body
    dynamics with distributed ...
  zh: 本研究由Hyunjong Song、William Z. Peng和Joo H. Kim共同完成，发表于arXiv（cs.RO），系统分析了物体质量对人形机器人平衡稳定性的动态影响。通过将物体质量参数纳入全身动力学，构建了平衡状态盆地（BSB），并引入临界质量和过渡质量两个关键量，以刻画平衡能力与限制因素间的权衡关系。该方法被应用于全身轨迹优化，实现了稳定物体举升控制，并通过仿真和实验验证了举升-保持与举升-释放任务。
  ko: The demand for humanoid loco-manipulation tasks with an object has recently increased, and most existing control approaches
    for stability in such tasks rely on heuristics or machine-learning techniques. This study rigorously analyzes and exploits
    the dynamic effects of the object mass on balance stability. By formulating the object mass parameters in the whole-body
    dynamics with distributed ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_balancing
- whole_body_control
- loco_manipulation
- trajectory_optimization
- center_of_mass
- object_manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-04'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-08-04). Bibliographic metadata from arXiv API (2607.29625);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.29625 Balancing of Humanoid with Object Mass: Trade-off Analyses and Lifting Control'
  url: https://arxiv.org/abs/2607.29625
  date: '2026-07-31'
  accessed_at: '2026-08-04'
---

## 概述

该研究针对人形机器人携带物体进行移动操作任务中稳定性控制的挑战，摒弃了传统启发式或机器学习方法，而是从动力学角度严格分析物体质量对平衡的影响。作者在全身动力学中显式建模物体质量参数，结合分布式接触力和支撑接触处的压力中心，量化了其对系统动量和约束的非线性效应。通过构建平衡状态盆地（BSB）作为质心状态空间的划分，系统分析了支撑基底、驱动能力和姿态等不同条件下的平衡能力变化。研究引入临界质量和过渡质量两个新概念，揭示了动量调节与平衡限制因素之间的权衡关系，并将BSB作为显式阈值约束集成到全身轨迹优化中，成功实现了人形机器人的稳定物体举升控制。

## 核心内容

### 问题背景
人形机器人执行物体移动操作（loco-manipulation）任务的需求日益增长，但现有稳定性控制方法多依赖启发式规则或机器学习技术，缺乏对物体质量动态影响的严格分析。本研究旨在从第一性原理出发，量化物体质量对双足系统平衡稳定性的作用。

### 方法
- **动力学建模**：将物体质量参数显式纳入全身动力学，模型包含分布式接触力和支撑接触处的压力中心（centers of pressure），从而精确描述系统动量和约束条件。
- **平衡状态盆地（BSB）构建**：基于上述动力学模型，构建BSB作为双足系统在期望接触下维持平衡的质心状态空间划分。BSB用于预测和控制系统行为。
- **关键量定义**：引入两个新量——临界质量（critical mass），即系统平衡能力达到最大值时的物体质量；过渡质量（transition mass），即触发不同平衡限制因素切换的质量阈值。
- **轨迹优化集成**：建立将平衡状态施加于轨迹的充分条件，并将BSB作为显式阈值约束嵌入全身轨迹优化框架，用于稳定物体举升控制。

### 实验设置与结果
- **分析工具**：使用人形机器人和一个解析可处理的降阶机构进行验证，比较不同支撑基底、驱动能力和姿态条件下的BSB，系统分析物体质量对平衡能力的影响。
- **任务验证**：在仿真和实验中演示了举升-保持（lift-and-hold）和举升-释放（lift-and-release）两种任务，物体具有不同的质量属性。
- **关键结果**：BSB分析揭示了动量调节与平衡限制因素（如驱动能力、支撑范围）之间的权衡关系；临界质量和过渡质量为系统设计提供了量化指导。轨迹优化结合BSB约束后，成功实现了稳定举升控制，验证了方法的有效性。

### 结论
该研究为物体质量影响下人形机器人平衡控制提供了严格的动力学分析框架，BSB及其衍生量（临界质量、过渡质量）可作为通用工具，用于预测平衡能力、指导控制器设计和优化操作任务。

## Overview

The demand for humanoid loco-manipulation tasks with an object has recently increased, and most existing control approaches for stability in such tasks rely on heuristics or machine-learning techniques. This study rigorously analyzes and exploits the dynamic effects of the object mass on balance stability. By formulating the object mass parameters in the whole-body dynamics with distributed contact wrenches and centers of pressure at the stance contacts, their nonlinear effects on the system momenta and constraints are quantified. The dynamic models and constraints are incorporated into the construction of the balanced state basin/boundary (BSB), a partition of the center-of-mass state space for a biped system to maintain balance in its desired contacts. The implications of the BSB for prediction and control are highlighted using a humanoid robot and an analytically tractable reduced-order mechanism. The BSBs under different conditions of base of support, actuation capacity, and pose provide systematic analyses of the effects of object mass on the balancing capability of a system. In particular, the trade-off relationships between momentum regulation and limiting factors in balancing are characterized, introducing two key quantities of the object: the critical mass, at which the system's balancing capability is maximum, and the transition mass, which activates different limiting factors. In addition, sufficient conditions for imposing balanced states on a trajectory are established and implemented with BSBs as explicit threshold constraints in the whole-body trajectory optimization for stable object-lifting control of the humanoid, demonstrating the lift-and-hold and lift-and-release tasks with distinct mass properties in simulations and experiments.

## 参考
- https://arxiv.org/abs/2607.29625
