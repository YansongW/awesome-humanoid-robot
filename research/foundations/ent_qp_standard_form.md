---
$id: ent_qp_standard_form
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: formalism
names:
  en: Standard Quadratic Program (QP)
  zh: 标准二次规划（QP）
  ko: 표준 이차 계획법(QP)
summary:
  en: A convex optimization problem where a quadratic objective is minimized subject to linear equality and inequality constraints.
  zh: 现代 WBC 的主流实现是全身 QP 控制。它把所有任务统一为二次规划问题，同时显式施加动力学、摩擦锥、关节力矩限、关节限位等约束。
  ko: 등식 및 부등식 선형 제약 조건 하에서 이차 목적 함수를 최소화하는 볼록 최적화 문제.
domains:
- 00_foundations
layers:
- foundations
functional_roles:
- knowledge
theoretical_depth:
- formalism
tags:
- optimization
- quadratic_program
- convex_optimization
- wbc
verification:
  status: verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: high
  notes: 'Body backfilled from chapter-08.md#8.4.10.3 基于 QP 的全身控制公式 by scripts/backfill_nonpaper_entries.py. | WP4 trilingual
    backfill 2026-08-10: closed unclosed code fence(s) and removed duplicate stale translation block(s) (pre-existing ingestion
    defect).  [2026-08-12] body upgraded to textbook-grade (.staging/textbook_grade_run/b3): zh 概述/核心内容/参考 rewritten from
    card + graph neighbors + wiki chapters + first-hand sources (number whitelist audit passed); en/ko sections to be regenerated
    by translate pipeline.'
sources:
- id: src_nocedal_wright_2006
  type: other
  title: J. Nocedal and S. J. Wright, Numerical Optimization, 2nd ed., Springer, 2006
  url: https://doi.org/10.1007/978-0-387-40065-5
  date: '2006-01-01'
  accessed_at: '2026-06-25'
---
## 概述

标准二次规划（Standard Quadratic Program, QP）是一类目标函数为二次、约束为线性的凸优化问题，是人形机器人全身控制（Whole-Body Control, WBC）的主流实现形式。它把所有控制任务统一为二次规划问题，同时显式施加动力学、摩擦锥、关节力矩限、关节限位等约束，在满足物理可行性的前提下最小化任务跟踪误差。

## 核心内容

### 是什么：准确定义

二次规划（Quadratic Programming, QP）是数学优化中的一个标准问题类别。其一般形式为：在满足一组线性等式与不等式约束的前提下，最小化一个二次目标函数。当目标函数中的二次项系数矩阵为半正定时，该 QP 为凸问题，具有全局最优解，且可被高效求解。

在人形机器人控制中，QP 被用作**全身控制器**的数学内核。它不再像传统方法那样为每个任务单独设计控制器，而是将所有任务（如质心跟踪、足端位置、躯干姿态）统一放入一个目标函数中，用权重系数调节优先级，同时把机器人动力学、接触约束、执行器限制等物理规律全部编码为约束条件。求解器在每一控制周期内寻找一组最优的广义加速度、关节力矩与接触力，使任务误差加权和最小。

### 为什么存在：痛点与历史定位

在人形机器人控制的发展历程中，研究者长期面临一个核心矛盾：**任务多、约束硬、计算时间短**。早期方法如 ZMP 控制与逆运动学（IK）逐层求解，任务之间缺乏统一协调；而直接求解完整最优控制问题（OCP）又因非线性动力学与实时性要求而难以落地。

QP 的引入改变了这一局面。它真正改变的不是优化理论本身，而是**控制问题的建模方式**——把"该做什么"（任务）与"不能做什么"（约束）分离，让求解器在每一时刻自动寻找可行域内的最优折中。这种"任务加权 + 硬约束"的框架，使得人形机器人能够在行走、操作、受外力扰动等复杂场景下，同时满足稳定性、安全性与任务精度要求。现代 WBC 的主流实现正是全身 QP 控制，它把所有任务统一为二次规划问题，同时显式施加动力学、摩擦锥、关节力矩限、关节限位等约束。

### 原理拆解

**① 优化变量与目标函数**

全身 QP 控制的优化变量通常包括广义加速度 \(\dot{\mathbf{v}}\)、关节力矩 \(\boldsymbol{\tau}\) 与接触力 \(\mathbf{F}_c\)。目标函数为各任务跟踪误差加权和加上正则项：

$$
\min_{\dot{\mathbf{v}}, \boldsymbol{\tau}, \mathbf{F}_c} \quad \sum_i w_i \left\| \mathbf{J}_i \dot{\mathbf{v}} + \dot{\mathbf{J}}_i \mathbf{v} - \ddot{\mathbf{x}}_i^* \right\|^2 + w_{\tau}\|\boldsymbol{\tau}\|^2 + w_{f}\|\mathbf{F}_c\|^2
$$

其中 \(\mathbf{J}_i\) 为第 \(i\) 个任务的 Jacobian 矩阵，\(\ddot{\mathbf{x}}_i^*\) 为期望的任务空间加速度。权重 \(w_i\) 决定任务优先级，正则项 \(w_{\tau}\|\boldsymbol{\tau}\|^2\) 与 \(w_{f}\|\mathbf{F}_c\|^2\) 用于抑制过大的力矩与接触力。

**② 约束条件：物理可行性的数学编码**

QP 的强大之处在于约束的显式表达。人形机器人控制中的核心约束包括：

**动力学约束**（浮动基刚体动力学方程）：

$$
\mathbf{M}\dot{\mathbf{v}} + \mathbf{C}\mathbf{v} + \mathbf{g} = \mathbf{S}^T \boldsymbol{\tau} + \sum_c \mathbf{J}_{c}^T \mathbf{F}_c
$$

其中 \(\mathbf{M}\) 为质量矩阵，\(\mathbf{C}\) 为科氏力/离心力项，\(\mathbf{g}\) 为重力项，\(\mathbf{S}\) 为选择矩阵，\(\mathbf{J}_c\) 为接触点 Jacobian。该等式保证求解出的加速度、力矩与接触力满足物理定律。

**摩擦锥约束**（防止接触点滑动）：

$$
\mathbf{F}_c \in \mathcal{C}(\mu)
$$

其中 \(\mathcal{C}(\mu)\) 为以摩擦系数 \(\mu\) 定义的锥形可行域。实际求解中通常用线性化的多边形近似。

**关节力矩限**（执行器物理极限）：

$$
\boldsymbol{\tau}_{\min} \leq \boldsymbol{\tau} \leq \boldsymbol{\tau}_{\max}
$$

**关节限位（速度级）**（防止关节超限）：

$$
\mathbf{q}_{\min} \leq \mathbf{q} + \Delta t \, \dot{\mathbf{q}} \leq \mathbf{q}_{\max}
$$

### 关键参数与规格

全身 QP 控制器的关键参数包括：

| 参数 | 含义 | 典型取值/说明 |
|------|------|---------------|
| \(w_i\) | 任务权重 | 需按任务优先级整定，质心任务通常权重最高 |
| \(w_{\tau}\) | 力矩正则权重 | 较小值（如 \(10^{-4}\) 量级），仅用于数值稳定 |
| \(\mu\) | 摩擦系数 | 依据接触面材料确定，通常取 0.5–1.0 |
| \(\Delta t\) | 控制周期 | 典型值 1–5 ms，需与求解器速度匹配 |
| 求解器 | QP 求解算法 | 常用 OSQP、qpOASES、ProxQP 等实时求解器 |

### 横向对比

| 方法 | 约束处理 | 任务协调 | 计算开销 | 适用场景 |
|------|----------|----------|----------|----------|
| 逆运动学（IK）+ 独立 PID | 隐式 | 弱 | 低 | 简单操作任务 |
| ZMP 控制 + 预览控制 | 仅 ZMP 约束 | 中 | 低 | 平地行走 |
| 全身 QP 控制 | 显式、完整 | 强（加权） | 中 | 动态行走、操作、受扰 |
| 模型预测控制（MPC） | 显式、前瞻 | 强（时域） | 高 | 复杂动态场景 |

QP 与 MPC 的核心区别在于：QP 是单步优化（当前时刻），MPC 是滚动时域优化（未来 N 步）。MPC 内部通常也嵌套 QP 求解器。

### 谁在用·应用案例

全身 QP 控制已成为现代人形机器人控制器的标准组件。典型应用包括：

- **动态行走与平衡**：在行走过程中实时求解全身关节力矩，同时满足 ZMP 约束与摩擦锥约束。
- **全身操作**：如乒乓球对打（HITTER 系统）中，低层控制器通过 WBC 或 MPC 实现关节级别的精确跟踪。
- **分层规划中的低层跟踪**：在"高层规划 footsteps 与躯干运动，中层规划四肢关节轨迹，低层用 QP 或 MPC 实时跟踪"的分层架构中，QP 承担实时全身运动生成的角色。

一个典型的概念演示算例（来自项目 Wiki 第 8 章）使用 SLSQP 求解器，优化变量为关节加速度、关节力矩与接触力，目标函数为末端加速度跟踪误差，约束包括动力学等式、摩擦锥不等式与力矩限。该算例仅为概念演示：真实 WBC 需要完整的浮动基动力学、多个任务、多个接触点以及实时 QP 求解器（如 OSQP、qpOASES、ProxQP）。但其核心结构——任务跟踪目标 + 动力学等式 + 摩擦锥不等式 + 力矩限——与现代人形机器人控制器完全一致。

### 局限与边界

1. **线性化近似**：QP 要求约束为线性，而真实机器人动力学为非线性。动力学约束中的质量矩阵 \(\mathbf{M}\) 与科氏项 \(\mathbf{C}\) 需在当前状态处线性化，这限制了 QP 在高速高动态场景下的精度。
2. **任务权重整定困难**：权重 \(w_i\) 的选取依赖经验，不当的权重可能导致任务间冲突或抖动。
3. **接触力假设**：摩擦锥约束通常用线性多边形近似，对接触点数量多、接触面复杂的情况需谨慎处理。
4. **计算实时性**：虽然 QP 可高效求解，但全身 QP 的变量维度高（广义加速度 + 力矩 + 接触力），对求解器性能有较高要求。工程判断：在典型 1 kHz 控制频率下，需选用 OSQP 等专用实时求解器。
5. **模型依赖**：QP 控制效果依赖模型精度，模型误差会直接导致控制性能下降。

### 常见误区

1. **"QP 就是 MPC"**——错。MPC 是滚动时域最优控制框架，其内部可能嵌套 QP 求解器，但 QP 本身是单步优化问题。MPC 的"前瞻性"来自多步预测，而非 QP 本身。
2. **"权重越大任务越优先"**——不完全对。权重影响目标函数中的相对重要性，但硬约束（如摩擦锥、力矩限）不可违反，权重再大也不能突破硬约束。
3. **"QP 能处理任意非线性约束"**——错。标准 QP 只允许线性约束，非线性约束需线性化或改用非线性规划（NLP）。
4. **"全身 QP 不需要模型"**——错。动力学约束、Jacobian 计算都依赖精确的机器人模型，模型误差是 QP 控制的主要误差来源之一。

### 相关知识

- `ent_method_model_predictive_control` — MPC 是 QP 的"时域扩展"，在滚动时域内反复求解 QP 子问题，实现前瞻性约束处理。
- `ent_paper_hitter_a_humanoid_table_tennis_2025` — HITTER 系统的低层控制器使用 WBC/MPC 实现关节级跟踪，是 QP 控制的典型应用场景。
- `ent_paper_agile_a_comprehensive_workflow_2026` — AGILE 工作流中，WBC 与 MPC 作为低层控制组件，与高层技能路由协同。
- `ent_paper_amo_adaptive_motion_optimizati_2025` — AMO 框架用轨迹优化离线生成参考数据，低层 RL 策略与 WBC 类方法形成对比。

## 参考

- [Numerical Optimization (Nocedal & Wright, 2006)](https://doi.org/10.1007/978-0-387-40065-5)
- [项目 Wiki 第 8 章：人形机器人设计开发全流程](https://github.com/YansongW/awesome-humanoid-robot/tree/main/wiki/docs/chapters/chapter-08.md)
- [项目 Wiki 第 14 章：控制与软件设计](https://github.com/YansongW/awesome-humanoid-robot/tree/main/wiki/docs/chapters/chapter-14.md)

## Overview

Standard Quadratic Programming (QP) is a class of convex optimization problems with a quadratic objective function and linear constraints, and it is the mainstream implementation form for Whole-Body Control (WBC) of humanoid robots. It unifies all control tasks into a quadratic programming problem while explicitly imposing constraints such as dynamics, friction cones, joint torque limits, and joint position limits, minimizing task tracking errors under the premise of physical feasibility.

## Content

### What It Is: Precise Definition

Quadratic Programming (QP) is a standard problem category in mathematical optimization. Its general form is: minimize a quadratic objective function subject to a set of linear equality and inequality constraints. When the quadratic coefficient matrix in the objective function is positive semidefinite, the QP is convex, has a globally optimal solution, and can be solved efficiently.

In humanoid robot control, QP serves as the mathematical core of **whole-body controllers**. Unlike traditional methods that design a separate controller for each task, it unifies all tasks (such as centroid tracking, foot position, torso orientation) into a single objective function, using weight coefficients to adjust priorities, while encoding all physical laws—robot dynamics, contact constraints, actuator limits—as constraints. The solver finds an optimal set of generalized accelerations, joint torques, and contact forces in each control cycle to minimize the weighted sum of task errors.

### Why It Exists: Pain Points and Historical Positioning

In the development of humanoid robot control, researchers have long faced a core contradiction: **many tasks, hard constraints, and short computation time**. Early methods such as ZMP control and inverse kinematics (IK) solved problems layer by layer, lacking unified coordination between tasks; meanwhile, directly solving the full optimal control problem (OCP) was difficult to implement due to nonlinear dynamics and real-time requirements.

The introduction of QP changed this situation. What it truly changed was not optimization theory itself, but the **modeling approach of control problems**—separating "what to do" (tasks) from "what cannot be done" (constraints), allowing the solver to automatically find the optimal compromise within the feasible region at each instant. This "task weighting + hard constraints" framework enables humanoid robots to simultaneously satisfy stability, safety, and task accuracy requirements in complex scenarios such as walking, manipulation, and external disturbances. The mainstream implementation of modern WBC is whole-body QP control, which unifies all tasks into a quadratic programming problem while explicitly imposing dynamics, friction cone, joint torque limit, and joint position limit constraints.

### Principle Breakdown

**① Optimization Variables and Objective Function**

The optimization variables of whole-body QP control typically include generalized accelerations \(\dot{\mathbf{v}}\), joint torques \(\boldsymbol{\tau}\), and contact forces \(\mathbf{F}_c\). The objective function is the weighted sum of task tracking errors plus regularization terms:

$$
\min_{\dot{\mathbf{v}}, \boldsymbol{\tau}, \mathbf{F}_c} \quad \sum_i w_i \left\| \mathbf{J}_i \dot{\mathbf{v}} + \dot{\mathbf{J}}_i \mathbf{v} - \ddot{\mathbf{x}}_i^* \right\|^2 + w_{\tau}\|\boldsymbol{\tau}\|^2 + w_{f}\|\mathbf{F}_c\|^2
$$

where \(\mathbf{J}_i\) is the Jacobian matrix of the \(i\)-th task, and \(\ddot{\mathbf{x}}_i^*\) is the desired task-space acceleration. The weights \(w_i\) determine task priorities, and the regularization terms \(w_{\tau}\|\boldsymbol{\tau}\|^2\) and \(w_{f}\|\mathbf{F}_c\|^2\) suppress excessively large torques and contact forces.

**② Constraints: Mathematical Encoding of Physical Feasibility**

The power of QP lies in the explicit expression of constraints. The core constraints in humanoid robot control include:

**Dynamics constraints** (floating-base rigid-body dynamics equations):

$$
\mathbf{M}\dot{\mathbf{v}} + \mathbf{C}\mathbf{v} + \mathbf{g} = \mathbf{S}^T \boldsymbol{\tau} + \sum_c \mathbf{J}_{c}^T \mathbf{F}_c
$$

where \(\mathbf{M}\) is the mass matrix, \(\mathbf{C}\) is the Coriolis/centrifugal term, \(\mathbf{g}\) is the gravity term, \(\mathbf{S}\) is the selection matrix, and \(\mathbf{J}_c\) is the contact point Jacobian. This equality ensures that the solved accelerations, torques, and contact forces satisfy physical laws.

**Friction cone constraints** (preventing contact point sliding):

$$
\mathbf{F}_c \in \mathcal{C}(\mu)
$$

where \(\mathcal{C}(\mu)\) is the conical feasible region defined by the friction coefficient \(\mu\). In practice, a linearized polygonal approximation is typically used.

**Joint torque limits** (actuator physical limits):

$$
\boldsymbol{\tau}_{\min} \leq \boldsymbol{\tau} \leq \boldsymbol{\tau}_{\max}
$$

**Joint position limits (velocity level)** (preventing joint limit violations):

$$
\mathbf{q}_{\min} \leq \mathbf{q} + \Delta t \, \dot{\mathbf{q}} \leq \mathbf{q}_{\max}
$$

### Key Parameters and Specifications

The key parameters of a whole-body QP controller include:

| Parameter | Meaning | Typical Value/Description |
|-----------|---------|---------------------------|
| \(w_i\) | Task weight | Tuned according to task priority; centroid tasks usually have the highest weight |
| \(w_{\tau}\) | Torque regularization weight | Small value (e.g., on the order of \(10^{-4}\)), used only for numerical stability |
| \(\mu\) | Friction coefficient | Determined by contact surface material, typically 0.5–1.0 |
| \(\Delta t\) | Control period | Typical value 1–5 ms, must match solver speed |
| Solver | QP solving algorithm | Common real-time solvers: OSQP, qpOASES, ProxQP |

### Horizontal Comparison

| Method | Constraint Handling | Task Coordination | Computational Cost | Applicable Scenarios |
|--------|---------------------|-------------------|--------------------|----------------------|
| Inverse Kinematics (IK) + Independent PID | Implicit | Weak | Low | Simple manipulation tasks |
| ZMP Control + Preview Control | ZMP constraints only | Medium | Low | Flat-ground walking |
| Whole-body QP Control | Explicit, complete | Strong (weighted) | Medium | Dynamic walking, manipulation, disturbances |
| Model Predictive Control (MPC) | Explicit, look-ahead | Strong (time domain) | High | Complex dynamic scenarios |

The core difference between QP and MPC is: QP is single-step optimization (current instant), while MPC is receding-horizon optimization (future N steps). MPC typically embeds a QP solver internally.

### Who Uses It: Application Cases

Whole-body QP control has become a standard component of modern humanoid robot controllers. Typical applications include:

- **Dynamic walking and balancing**: Solving whole-body joint torques in real time during walking while satisfying ZMP constraints and friction cone constraints.
- **Whole-body manipulation**: For example, in table tennis play (HITTER system), the low-level controller uses WBC or MPC to achieve joint-level precise tracking.
- **Low-level tracking in hierarchical planning**: In the hierarchical architecture of "high-level planning of footsteps and torso motion, mid-level planning of limb joint trajectories, and low-level real-time tracking with QP or MPC," QP handles real-time whole-body motion generation.

A typical conceptual demonstration example (from Chapter 8 of the project Wiki) uses the SLSQP solver, with optimization variables of joint accelerations, joint torques, and contact forces, an objective function of end-effector acceleration tracking error, and constraints including dynamics equalities, friction cone inequalities, and torque limits. This example is only a conceptual demonstration: real WBC requires complete floating-base dynamics, multiple tasks, multiple contact points, and real-time QP solvers (such as OSQP, qpOASES, ProxQP). However, its core structure—task tracking objective + dynamics equalities + friction cone inequalities + torque limits—is fully consistent with modern humanoid robot controllers.

### Limitations and Boundaries

1. **Linearization approximation**: QP requires linear constraints, while real robot dynamics are nonlinear. The mass matrix \(\mathbf{M}\) and Coriolis term \(\mathbf{C}\) in the dynamics constraints must be linearized at the current state, which limits the accuracy of QP in high-speed, highly dynamic scenarios.
2. **Difficulty in task weight tuning**: The selection of weights \(w_i\) relies on experience; improper weights may lead to conflicts between tasks or oscillations.
3. **Contact force assumptions**: Friction cone constraints are typically approximated by linear polygons, requiring careful handling for scenarios with many contact points or complex contact surfaces.
4. **Computational real-time performance**: Although QP can be solved efficiently, whole-body QP has high variable dimensionality (generalized accelerations + torques + contact forces), imposing high demands on solver performance. Engineering judgment: at typical 1 kHz control frequencies, dedicated real-time solvers such as OSQP must be used.
5. **Model dependence**: The control performance of QP depends on model accuracy; model errors directly degrade control performance.

### Common Misconceptions

1. **"QP is MPC"**—Wrong. MPC is a receding-horizon optimal control framework that may embed a QP solver internally, but QP itself is a single-step optimization problem. The "look-ahead" property of MPC comes from multi-step prediction, not from QP itself.
2. **"Larger weight means higher task priority"**—Not entirely correct. Weights affect relative importance in the objective function, but hard constraints (such as friction cones and torque limits) cannot be violated; no matter how large the weight, hard constraints cannot be broken.
3. **"QP can handle arbitrary nonlinear constraints"**—Wrong. Standard QP only allows linear constraints; nonlinear constraints require linearization or switching to nonlinear programming (NLP).
4. **"Whole-body QP does not require a model"**—Wrong. Dynamics constraints and Jacobian computations all depend on an accurate robot model; model errors are one of the main error sources in QP control.

### Related Knowledge

- `ent_method_model_predictive_control` — MPC is the "time-domain extension" of QP, repeatedly solving QP subproblems within a receding horizon to achieve look-ahead constraint handling.
- `ent_paper_hitter_a_humanoid_table_tennis_2025` — The low-level controller of the HITTER system uses WBC/MPC for joint-level tracking, a typical application scenario of QP control.
- `ent_paper_agile_a_comprehensive_workflow_2026` — In the AGILE workflow, WBC and MPC serve as low-level control components, coordinating with high-level skill routing.
- `ent_paper_amo_adaptive_motion_optimizati_2025` — The AMO framework uses trajectory optimization to generate reference data offline, with low-level RL policies contrasting with WBC-type methods.

## 개요

표준 이차 계획법(Standard Quadratic Program, QP)은 목적 함수가 이차식이고 제약 조건이 선형인 볼록 최적화 문제의 한 종류로, 휴머노이드 로봇의 전신 제어(Whole-Body Control, WBC)의 주류 구현 형태입니다. 모든 제어 작업을 이차 계획법 문제로 통합하면서 동역학, 마찰 원뿔, 관절 토크 한계, 관절 한계 등의 제약 조건을 명시적으로 적용하여 물리적 실현 가능성을 충족시키는 동시에 작업 추적 오차를 최소화합니다.

## 핵심 내용

### 무엇인가: 정확한 정의

이차 계획법(Quadratic Programming, QP)은 수학적 최적화의 표준 문제 범주입니다. 일반적인 형태는 다음과 같습니다: 일련의 선형 등식 및 부등식 제약 조건을 충족시키면서 이차 목적 함수를 최소화하는 것입니다. 목적 함수의 이차 항 계수 행렬이 반양정치(半正定値)일 때, 해당 QP는 볼록 문제로 전역 최적해를 가지며 효율적으로 풀 수 있습니다.

휴머노이드 로봇 제어에서 QP는 **전신 제어기**의 수학적 핵심으로 사용됩니다. 기존 방식처럼 각 작업에 대해 개별적으로 제어기를 설계하는 대신, 모든 작업(질량 중심 추적, 발끝 위치, 몸통 자세 등)을 하나의 목적 함수에 통합하고 가중치 계수로 우선순위를 조정하며, 로봇 동역학, 접촉 제약, 액추에이터 제한 등의 물리적 법칙을 모두 제약 조건으로 인코딩합니다. 솔버는 각 제어 주기마다 최적의 일반화 가속도, 관절 토크 및 접촉력을 찾아 작업 오차의 가중 합을 최소화합니다.

### 왜 존재하는가:痛点과 역사적 위치

휴머노이드 로봇 제어의 발전 과정에서 연구자들은 오랫동안 핵심 모순에 직면해 왔습니다: **작업이 많고, 제약이 엄격하며, 계산 시간이 짧다**. 초기 방법인 ZMP 제어와 역기구학(IK)은 계층적으로 풀었으며 작업 간의 통일된 조정이 부족했습니다. 반면 완전한 최적 제어 문제(OCP)를 직접 푸는 것은 비선형 동역학과 실시간 요구 사항 때문에 실용화가 어려웠습니다.

QP의 도입은 이러한 상황을 바꾸었습니다. QP가 실제로 바꾼 것은 최적화 이론 자체가 아니라 **제어 문제의 모델링 방식**입니다 — "무엇을 해야 하는가"(작업)와 "무엇을 할 수 없는가"(제약)를 분리하여 솔버가 매 순간 실현 가능 영역 내에서 최적의 절충안을 자동으로 찾도록 합니다. 이러한 "작업 가중치 + 하드 제약" 프레임워크는 휴머노이드 로봇이 보행, 조작, 외부 교란 등의 복잡한 시나리오에서 안정성, 안전성 및 작업 정밀도를 동시에 충족시킬 수 있게 합니다. 현대 WBC의 주류 구현은 바로 전신 QP 제어로, 모든 작업을 이차 계획법 문제로 통합하면서 동역학, 마찰 원뿔, 관절 토크 한계, 관절 한계 등의 제약 조건을 명시적으로 적용합니다.

### 원리 분석

**① 최적화 변수와 목적 함수**

전신 QP 제어의 최적화 변수는 일반적으로 일반화 가속도 \(\dot{\mathbf{v}}\), 관절 토크 \(\boldsymbol{\tau}\) 및 접촉력 \(\mathbf{F}_c\)를 포함합니다. 목적 함수는 각 작업 추적 오차의 가중 합에 정규화 항을 더한 것입니다:

$$
\min_{\dot{\mathbf{v}}, \boldsymbol{\tau}, \mathbf{F}_c} \quad \sum_i w_i \left\| \mathbf{J}_i \dot{\mathbf{v}} + \dot{\mathbf{J}}_i \mathbf{v} - \ddot{\mathbf{x}}_i^* \right\|^2 + w_{\tau}\|\boldsymbol{\tau}\|^2 + w_{f}\|\mathbf{F}_c\|^2
$$

여기서 \(\mathbf{J}_i\)는 \(i\)번째 작업의 Jacobian 행렬이고, \(\ddot{\mathbf{x}}_i^*\)는 기대 작업 공간 가속도입니다. 가중치 \(w_i\)는 작업 우선순위를 결정하며, 정규화 항 \(w_{\tau}\|\boldsymbol{\tau}\|^2\)와 \(w_{f}\|\mathbf{F}_c\|^2\)는 과도한 토크와 접촉력을 억제하는 데 사용됩니다.

**② 제약 조건: 물리적 실현 가능성의 수학적 인코딩**

QP의 강점은 제약 조건의 명시적 표현에 있습니다. 휴머노이드 로봇 제어의 핵심 제약 조건은 다음과 같습니다:

**동역학 제약**(부유 기반 강체 동역학 방정식):

$$
\mathbf{M}\dot{\mathbf{v}} + \mathbf{C}\mathbf{v} + \mathbf{g} = \mathbf{S}^T \boldsymbol{\tau} + \sum_c \mathbf{J}_{c}^T \mathbf{F}_c
$$

여기서 \(\mathbf{M}\)은 질량 행렬, \(\mathbf{C}\)는 코리올리/원심력 항, \(\mathbf{g}\)는 중력 항, \(\mathbf{S}\)는 선택 행렬, \(\mathbf{J}_c\)는 접촉점 Jacobian입니다. 이 등식은 계산된 가속도, 토크 및 접촉력이 물리 법칙을 충족함을 보장합니다.

**마찰 원뿔 제약**(접촉점 미끄러짐 방지):

$$
\mathbf{F}_c \in \mathcal{C}(\mu)
$$

여기서 \(\mathcal{C}(\mu)\)는 마찰 계수 \(\mu\)로 정의된 원뿔형 실현 가능 영역입니다. 실제 해석에서는 일반적으로 선형화된 다각형 근사를 사용합니다.

**관절 토크 한계**(액추에이터 물리적 한계):

$$
\boldsymbol{\tau}_{\min} \leq \boldsymbol{\tau} \leq \boldsymbol{\tau}_{\max}
$$

**관절 한계(속도 수준)**(관절 초과 방지):

$$
\mathbf{q}_{\min} \leq \mathbf{q} + \Delta t \, \dot{\mathbf{q}} \leq \mathbf{q}_{\max}
$$

### 주요 매개변수와 사양

전신 QP 제어기의 주요 매개변수는 다음과 같습니다:

| 매개변수 | 의미 | 일반적인 값/설명 |
|------|------|---------------|
| \(w_i\) | 작업 가중치 | 작업 우선순위에 따라 조정 필요, 질량 중심 작업이 일반적으로 가장 높은 가중치 |
| \(w_{\tau}\) | 토크 정규화 가중치 | 작은 값(예: \(10^{-4}\) 수준), 수치적 안정성에만 사용 |
| \(\mu\) | 마찰 계수 | 접촉면 재질에 따라 결정, 일반적으로 0.5–1.0 |
| \(\Delta t\) | 제어 주기 | 일반적인 값 1–5 ms, 솔버 속도와 일치해야 함 |
| 솔버 | QP 해석 알고리즘 | 일반적으로 OSQP, qpOASES, ProxQP 등의 실시간 솔버 사용 |

### 수평 비교

| 방법 | 제약 처리 | 작업 조정 | 계산 비용 | 적용 시나리오 |
|------|----------|----------|----------|----------|
| 역기구학(IK) + 독립 PID | 암시적 | 약함 | 낮음 | 단순 조작 작업 |
| ZMP 제어 + 미리보기 제어 | ZMP 제약만 | 중간 | 낮음 | 평지 보행 |
| 전신 QP 제어 | 명시적, 완전 | 강함(가중치) | 중간 | 동적 보행, 조작, 교란 |
| 모델 예측 제어(MPC) | 명시적, 예측 | 강함(시간 영역) | 높음 | 복잡한 동적 시나리오 |

QP와 MPC의 핵심 차이점은: QP는 단일 단계 최적화(현재 시점)이고, MPC는 롤링 시간 영역 최적화(미래 N단계)입니다. MPC 내부에는 일반적으로 QP 솔버가 중첩되어 있습니다.

### 누가 사용하는가·응용 사례

전신 QP 제어는 현대 휴머노이드 로봇 제어기의 표준 구성 요소가 되었습니다. 일반적인 응용 사례는 다음과 같습니다:

- **동적 보행 및 균형**: 보행 중 전신 관절 토크를 실시간으로 계산하면서 ZMP 제약과 마찰 원뿔 제약을 동시에 충족.
- **전신 조작**: 탁구 대전(HITTER 시스템)과 같은 경우, 저수준 제어기가 WBC 또는 MPC를 통해 관절 수준의 정밀 추적을 구현.
- **계층적 계획의 저수준 추적**: "고수준 계획이 footsteps와 몸통 운동을, 중수준 계획이 사지 관절 궤적을, 저수준이 QP 또는 MPC로 실시간 추적"하는 계층 구조에서 QP는 실시간 전신 운동 생성을 담당.

프로젝트 Wiki 8장의 일반적인 개념 데모 예제는 SLSQP 솔버를 사용하며, 최적화 변수는 관절 가속도, 관절 토크 및 접촉력이고, 목적 함수는 말단 가속도 추적 오차이며, 제약 조건은 동역학 등식, 마찰 원뿔 부등식 및 토크 한계를 포함합니다. 이 예제는 개념 데모일 뿐입니다: 실제 WBC는 완전한 부유 기반 동역학, 여러 작업, 여러 접촉점 및 실시간 QP 솔버(예: OSQP, qpOASES, ProxQP)가 필요합니다. 그러나 핵심 구조 — 작업 추적 목표 + 동역학 등식 + 마찰 원뿔 부등식 + 토크 한계 — 는 현대 휴머노이드 로봇 제어기와 완전히 일치합니다.

### 한계와 경계

1. **선형화 근사**: QP는 제약 조건이 선형이어야 하지만 실제 로봇 동역학은 비선형입니다. 동역학 제약의 질량 행렬 \(\mathbf{M}\)과 코리올리 항 \(\mathbf{C}\)는 현재 상태에서 선형화해야 하므로, 고속 고동적 시나리오에서 QP의 정밀도가 제한됩니다.
2. **작업 가중치 조정의 어려움**: 가중치 \(w_i\)의 선택은 경험에 의존하며, 부적절한 가중치는 작업 간 충돌이나 떨림을 유발할 수 있습니다.
3. **접촉력 가정**: 마찰 원뿔 제약은 일반적으로 선형 다각형으로 근사되며, 접촉점 수가 많고 접촉면이 복잡한 경우 주의가 필요합니다.
4. **계산 실시간성**: QP는 효율적으로 풀 수 있지만, 전신 QP의 변수 차원이 높아(일반화 가속도 + 토크 + 접촉력) 솔버 성능에 대한 요구가 높습니다. 공학적 판단: 일반적인 1 kHz 제어 주파수에서 OSQP와 같은 전용 실시간 솔버를 선택해야 합니다.
5. **모델 의존성**: QP 제어 효과는 모델 정밀도에 의존하며, 모델 오차는 제어 성능 저하를 직접 초래합니다.

### 일반적인 오해

1. **"QP는 MPC다"** — 틀림. MPC는 롤링 시간 영역 최적 제어 프레임워크로, 내부에 QP 솔버가 중첩될 수 있지만 QP 자체는 단일 단계 최적화 문제입니다. MPC의 "예측성"은 다단계 예측에서 오는 것이지 QP 자체에서 오는 것이 아닙니다.
2. **"가중치가 클수록 작업 우선순위가 높다"** — 완전히 맞지는 않음. 가중치는 목적 함수의 상대적 중요성에 영향을 주지만, 하드 제약(예: 마찰 원뿔, 토크 한계)은 위반할 수 없으며 가중치가 아무리 커도 하드 제약을 돌파할 수 없습니다.
3. **"QP는 임의의 비선형 제약을 처리할 수 있다"** — 틀림. 표준 QP는 선형 제약만 허용하며, 비선형 제약은 선형화하거나 비선형 계획법(NLP)으로 전환해야 합니다.
4. **"전신 QP는 모델이 필요 없다"** — 틀림. 동역학 제약, Jacobian 계산은 모두 정밀한 로봇 모델에 의존하며, 모델 오차는 QP 제어의 주요 오차 원인 중 하나입니다.

### 관련 지식

- `ent_method_model_predictive_control` — MPC는 QP의 "시간 영역 확장"으로, 롤링 시간 영역에서 QP 하위 문제를 반복적으로 풀어 예측적 제약 처리를 구현합니다.
- `ent_paper_hitter_a_humanoid_table_tennis_2025` — HITTER 시스템의 저수준 제어기는 WBC/MPC를 사용하여 관절 수준 추적을 구현하며, QP 제어의 전형적인 응용 시나리오입니다.
- `ent_paper_agile_a_comprehensive_workflow_2026` — AGILE 워크플로우에서 WBC와 MPC는 저수준 제어 구성 요소로 고수준 스킬 라우팅과 협력합니다.
- `ent_paper_amo_adaptive_motion_optimizati_2025` — AMO 프레임워크는 궤적 최적화로 오프라인 참조 데이터를 생성하며, 저수준 RL 정책과 WBC 유사 방법이 대조를 이룹니다.
