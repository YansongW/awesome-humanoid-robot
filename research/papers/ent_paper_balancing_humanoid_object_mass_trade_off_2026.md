---
$id: ent_paper_balancing_humanoid_object_mass_trade_off_2026
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
    dynamics with distributed.
  zh: 本文提出一种将物体质量参数显式纳入全身动力学与平衡稳定盆地（BSB）框架的严格公式化方法，用于定量分析人形机器人负载操作中物体质量对平衡稳定性的非线性权衡关系，并将BSB作为显式约束用于稳定举升控制的轨迹优化。作者在ROBOTIS-OP3人形机器人上通过仿真和实验验证了该方法在lift-and-hold与lift-and-release任务中的有效性，并揭示了临界质量与转变质量等关键设计参数。
  ko: The demand for humanoid loco-manipulation tasks with an object has recently increased, and most existing control approaches
    for stability in such tasks rely on heuristics or machine-learning techniques. This study rigorously analyzes and exploits
    the dynamic effects of the object mass on balance stability. By formulating the object mass parameters in the whole-body
    dynamics with distributed.
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
- balancing
- humanoid
- object
- mass
- trade
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. [2026-08-05] experiments section regenerated under programmatic
    number whitelist (guardrail fix: previous numbers unverifiable against full text); en/ko regenerated.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.29625 Balancing of Humanoid with Object Mass: Trade-off Analyses and Lifting Control'
  url: https://arxiv.org/abs/2607.29625
  date: '2026-07-31'
  accessed_at: '2026-08-05'
---



## 概述

本文提出一种将物体质量参数显式纳入全身动力学与平衡稳定盆地（BSB）框架的严格公式化方法，用于定量分析人形机器人负载操作中物体质量对平衡稳定性的非线性权衡关系，并将BSB作为显式约束用于稳定举升控制的轨迹优化。作者在ROBOTIS-OP3人形机器人上通过仿真和实验验证了该方法在lift-and-hold与lift-and-release任务中的有效性，并揭示了临界质量与转变质量等关键设计参数。

## 它改变了什么

这项工作的核心改变在于将“物体质量”从负载操作控制中的被动参数提升为主动的平衡稳定性设计变量。现有方法要么依赖CoP/ZMP等参考点判据（既不充分也不必要），要么采用倒立摆等降阶模型（缺乏全身属性），都无法系统量化物体质量对全身动力学平衡的耦合影响。作者通过严格公式化，首次建立了物体质量与平衡能力之间的非线性权衡关系，并给出了“临界质量”和“转变质量”的解析定义——这为机器人设计者提供了超越“别拿太重”这一直觉的定量设计准则。

更重要的是，作者将BSB从离线分析工具转化为在线轨迹优化的显式约束。这一转变解决了现有轨迹优化方法（MPC、RL等）中平衡约束要么过于保守（CoP裕度）要么无法保证安全（无约束）的根本矛盾。通过证明“若当前状态在变化后系统的BSB内，则所有先前状态在给定接触下均平衡”的充分条件，作者为质量突变场景（如瞬时释放）提供了理论上的安全保证，这是此前任何方法都未能提供的。

## 方法拆解

### 全身动力学公式化
- 将物体质量参数（m_object, I_object）显式纳入关节空间动力学：M(q)q̈ + h(q,q̇) = τ_gen + c_stance(q)·γ + c_other(q)·γ，其中广义坐标q ∈ ℝ^(n+6)包含关节与浮动基座。
- 线性动量与角动量方程分别引入物体质量项：ΣF_p = m_robot·r̈_robot + m_object·r̈_object + (m_robot + m_object)g。
- 接触力/CoP分布通过非维度参数向量α ∈ ℝ⁶参数化，解决双支撑相的力学不确定性（法向力分配、摩擦力方向、CoP局部坐标等）。

### 权衡关系与关键量定义
- **临界质量**：系统平衡能力（CoM X-速度扰动幅度）最大时的物体质量。
- **转变质量**：m_obj,trans = τ_UB/(0.5·BoS_x·g) − m₁ − m₂，用于分类限制因素：
  - m_object < m_obj,trans：BoS维度限制（驱动容量未充分利用）
  - m_object = m_obj,trans：两约束同时激活
  - m_object > m_obj,trans：驱动容量限制（CoP无法利用BoS全范围）

### BSB构建与轨迹优化
- 对离散化全身姿态域求解约束非线性优化问题，最大化ṙ_x(0)，约束包括全身动力学、系统/接触约束、初始/终末条件、平衡保持和任务要求。
- 优化变量：三阶B样条控制顶点v + 非维度变量α；求解算法为SQP配合直接配点法，使用解析梯度和可行初始解。
- 举升任务分两阶段：蹲到站阶段最小化控制努力，稳定阶段求可行解实现最终静态平衡。
- BSB约束施加：lift-and-hold用含物体质量的BSB（式24），lift-and-release用零物体质量BSB（式25）。

## 关键创新

1. **物体质量的显式平衡量化**：首次将物体质量参数严格纳入全身动力学与BSB框架，建立了平衡能力随质量增加先增后减的非线性权衡关系，并给出临界质量与转变质量的解析定义。这超越了此前“附加质量有益”的启发式发现，提供了可计算的定量设计准则。

2. **BSB作为轨迹优化的显式约束**：通过证明质量属性变化下的充分条件（当前状态在变化后系统BSB内⇒所有先前状态平衡），将BSB从离线分析工具转化为在线轨迹优化的安全约束。这解决了CoP裕度约束过保守、无约束方法不安全的核心矛盾，尤其适用于质量突变场景。

3. **限制因素分类的解析洞察**：通过转变质量将系统限制因素明确分为BoS主导与驱动容量主导两类，揭示了为何在某些条件下增加BoS宽度反而降低临界质量（如τ_ref^UB + 2BoS_ref时mobj,trans降至0.9 kg），为机械设计（足部尺寸、关节选型）提供了反直觉但可解释的指导。

## 实验与结果


## 实验与结果

### 对照设置

为验证 BSB 约束的有效性，作者在两类平台上开展实验：一是 2 自由度降阶机构（支撑连杆上的集中质量系统），用于解析可处理的参数化分析；二是 ROBOTIS-OP3 全尺寸人形机器人（质量 **3.5 kg**，直立高度 **0.51 m**，脚长 **0.127 m**），在 Webots 仿真与实物中执行矢状面双支撑相的物体举升任务。任务包括 lift-and-hold（举升并保持）与 lift-and-release（举升并释放）。基线对比条件为带裕度的 CoP（ZMP）约束，替代 BSB 约束；优化采用直接配点法与 SQP 求解，控制为 PID 加比例调整项。降阶机构中，连杆参数 l1 = **0.2 m**、l2 = **0.13 m**，质量 m1 = **1.74 kg**、m2 = **0.23 kg**，物体质量扫描范围 **0** 至 **5.85 kg**（步长 **0.05 kg**），扭矩上限缩放 **0.2–2.0** 倍 τ_ref^UB，BoS 缩放 **0.5、1.0、2.0** 倍 BoS_ref，终端时间 T = **0.8 s**。人形机器人实验中，物体质量范围 **0** 至 **1.5 kg**（占机器人质量的 **42.86%**），CoM Y 位置在髋关节高度 **0.12 m** 至 **0.19 m** 间取 **21** 个等间距值，BoS 维度为 fl（sl = **0**）与 **1.5**fl（sl = **0.5**fl），终端时间分别为 T = **0.95 s** 与 T = **1.0 s**。

### 关键数字

| 平台 | 条件 | mobj,trans (kg) | 最大 ṙx(0) (m/s) | 最大可行 mobject (kg) |
|---|---|---|---|---|
| 降阶机构 | 0.2 τ_ref^UB, BoS_ref | **0** | **0.26** | **0.35** |
| 降阶机构 | 0.3 τ_ref^UB, BoS_ref | — | **0.42** | **0.7** |
| 降阶机构 | 0.5 τ_ref^UB, BoS_ref | — | **0.9** | **1.2** |
| 降阶机构 | τ_ref^UB, BoS_ref | **2.15** | **0.45** | **2.8** |
| 降阶机构 | 2 τ_ref^UB, BoS_ref | **4.85** | **0.46** | **5.5** |
| 降阶机构 | τ_ref^UB, 0.5BoS_ref | **2.4** | **0.24** | **2.65** |
| 降阶机构 | τ_ref^UB, 2BoS_ref | **0.9** | **0.81** | **2.8** |
| 降阶机构 | 2 τ_ref^UB, 2BoS_ref | **3.75** | **0.83** | **5.85** |
| 人形机器人 | fl BoS | — | — | **1.2**（临界质量，占 **34.28%**） |
| 人形机器人 | 1.5fl BoS | — | — | **0.6**（临界质量，占 **17.14%**） |

### 结果含义

- **物体质量对平衡能力呈非线性权衡**：在无约束条件下，更大物体质量通过增加可用动量提升平衡能力（类似走钢丝的平衡杆效应），但关节力矩上限、BoS 尺寸与摩擦锥等约束会限制这一收益。降阶机构中，最大可行物体质量在 τ_ref^UB 与 BoS_ref 条件下解析近似为 **2.6 kg**、数值优化为 **2.8 kg**；当 mobject < mobj,trans 时 BoS 是限制因素，mobject = mobj,trans 时两种约束同时激活，mobject > mobj,trans 时力矩上限成为限制因素且平衡能力随质量增加而下降。人形机器人中，fl BoS 的临界质量为 **1.2 kg**，1.5fl BoS 时为 **0.6 kg**，验证了该权衡关系。

- **BoS 与扭矩极限具有非对称效应**：增大 BoS（如从 BoS_ref 到 **2**BoS_ref）可提升给定物体质量下的 BSB（最大 ṙx(0) 从 **0.45** 增至 **0.81 m/s**），但对可行域几乎无影响（最大可行质量仍为 **2.8 kg**）；增大扭矩极限（如从 τ_ref^UB 到 **2**τ_ref^UB）则显著扩展可行域（最大可行质量从 **2.8** 增至 **5.5 kg**），但对临界质量以下的 BSB 几乎无影响（最大 ṙx(0) 仅从 **0.45** 变为 **0.46 m/s**），呈现饱和效应。

- **CoP 裕度约束不足以作为精确稳定性阈值**：在 lift-and-hold 实验中（sl = **0**，mobject = **0.6 kg**），BSB 约束下代价函数值为 **4.481 N²m²s**，机器人成功完成举升；CoP 裕度约束下代价函数值为 **4.784 N²m²s**，其实际 CoP 范围（**–0.44** 至 **–0.019 m**）远在约束边界（**–0.058** 至 **0.058**，对应 BoS 维度的 **91.34%**）内，但机器人仍摔倒。这说明平衡能力受限于系统/接触约束与当前关节状态，而非单纯的 CoP 位置。lift-and-release 实验中（蹲到站阶段代价函数值 **6.036 N²m²s**），释放后 CoM 状态保持在 BSB(0 kg) 内，成功达到最终静态平衡，验证了 BSB 作为充分条件的有效性。

## 边界与局限

- 所有分析限于2D矢状面、双支撑相（DS）场景，未扩展到3D任意方向、跨步恢复、滑倒/绊倒等扰动。
- 物体简化为点质量（m_object），惯性张量I_object虽在公式中但未独立变化验证。
- 未与现有控制方法（MPC、RL等）进行定量性能对比，也未在多种人形机器人平台上基准测试。
- 真实应用中物体质量参数需外部估计（引用相关文献），本文未实现未知质量估计。
- 优化计算成本高，虽提出离线计算+参数延拓缓解，但未给出在线实时运行的推理频率数据。

## 工程启示

复现时首先核对**转变质量公式**的适用条件：m_obj,trans = τ_UB/(0.5·BoS_x·g) − m₁ − m₂需满足τ_UB ≥ (m₂ + m_object)·g·l₂，否则该解析值不成立。最容易踩坑的是**BSB约束施加的有效性**——必须确保BSB构建所用的q_sampled与轨迹优化中的中间条件一致，否则充分条件不成立，约束形同虚设。

工程选型上，若关节驱动容量有限（τ_ref^UB较小），增大BoS（如加长脚掌）反而可能降低临界质量（见τ_ref^UB + 2BoS_ref案例），应先通过降阶机构模型估算mobj,trans再决定机械设计方向。对于下游团队，建议将BSB离线计算并存储，在线查询时利用物体质量的线性动力学特性做参数延拓，避免实时求解非线性优化。实验验证时注意：CoP裕度约束即使轨迹完全在边界内也可能摔倒（举升-保持实验已证明），因此不要用CoP裕度作为安全验证的替代指标。

## 参考
- https://arxiv.org/abs/2607.29625

## Overview

This paper proposes a rigorous formulation that explicitly incorporates object mass parameters into a whole-body dynamics and Balance Stability Basin (BSB) framework, enabling quantitative analysis of the nonlinear trade-off between object mass and balance stability during humanoid robot load manipulation. The BSB is further employed as an explicit constraint in trajectory optimization for stable lifting control. The authors validate the method through simulations and experiments on the ROBOTIS-OP3 humanoid robot in lift-and-hold and lift-and-release tasks, revealing key design parameters such as critical mass and transition mass.

## What It Changes

The core shift of this work lies in elevating "object mass" from a passive parameter in load manipulation control to an active design variable for balance stability. Existing methods either rely on reference-point criteria such as CoP/ZMP (which are neither sufficient nor necessary) or employ reduced-order models like the inverted pendulum (lacking whole-body properties), none of which can systematically quantify the coupled impact of object mass on whole-body dynamic balance. Through rigorous formulation, the authors establish, for the first time, a nonlinear trade-off relationship between object mass and balance capability, providing analytical definitions of "critical mass" and "transition mass"—offering robot designers quantitative design guidelines that go beyond the intuitive rule of "don't lift anything too heavy."

More importantly, the authors transform the BSB from an offline analysis tool into an explicit constraint for online trajectory optimization. This shift resolves the fundamental contradiction in existing trajectory optimization methods (MPC, RL, etc.), where balance constraints are either overly conservative (CoP margins) or unable to guarantee safety (unconstrained). By proving the sufficient condition that "if the current state lies within the BSB of the changed system, then all prior states are balanced under the given contacts," the authors provide theoretical safety guarantees for mass-change scenarios (e.g., instantaneous release)—something no prior method has offered.

## Method Breakdown

### Whole-Body Dynamics Formulation
- Object mass parameters (m_object, I_object) are explicitly incorporated into joint-space dynamics: M(q)q̈ + h(q,q̇) = τ_gen + c_stance(q)·γ + c_other(q)·γ, where generalized coordinates q ∈ ℝ^(n+6) include joints and the floating base.
- Linear and angular momentum equations introduce object mass terms respectively: ΣF_p = m_robot·r̈_robot + m_object·r̈_object + (m_robot + m_object)g.
- Contact force/CoP distribution is parameterized via a non-dimensional parameter vector α ∈ ℝ⁶, resolving mechanical indeterminacy in double-support phases (normal force distribution, friction direction, local CoP coordinates, etc.).

### Trade-off Relationship and Key Quantity Definitions
- **Critical mass**: The object mass at which the system's balance capability (CoM X-velocity perturbation magnitude) is maximized.
- **Transition mass**: m_obj,trans = τ_UB/(0.5·BoS_x·g) − m₁ − m₂, used to classify limiting factors:
  - m_object < m_obj,trans: BoS dimension limited (actuator capacity underutilized)
  - m_object = m_obj,trans: both constraints activated simultaneously
  - m_object > m_obj,trans: actuator capacity limited (CoP cannot utilize the full BoS range)

### BSB Construction and Trajectory Optimization
- A constrained nonlinear optimization problem is solved over a discretized whole-body posture domain to maximize ṙ_x(0), with constraints including whole-body dynamics, system/contact constraints, initial/terminal conditions, balance maintenance, and task requirements.
- Optimization variables: cubic B-spline control vertices v + non-dimensional variables α; solved via SQP with direct collocation, using analytical gradients and feasible initial guesses.
- Lifting tasks are divided into two phases: a squat-to-stand phase minimizing control effort, and a stabilization phase finding feasible solutions for final static balance.
- BSB constraint application: lift-and-hold uses the BSB with object mass (Eq. 24), lift-and-release uses the zero-object-mass BSB (Eq. 25).

## Key Innovations

1. **Explicit balance quantification of object mass**: For the first time, object mass parameters are rigorously incorporated into the whole-body dynamics and BSB framework, establishing a nonlinear trade-off where balance capability first increases then decreases with mass, along with analytical definitions of critical mass and transition mass. This surpasses prior heuristic findings of "added mass is beneficial," providing computable quantitative design guidelines.

2. **BSB as an explicit constraint in trajectory optimization**: By proving the sufficient condition under mass property changes (current state within the changed system's BSB ⇒ all prior states balanced), the BSB is transformed from an offline analysis tool into a safety constraint for online trajectory optimization. This resolves the core contradiction between overly conservative CoP margin constraints and unsafe unconstrained methods, particularly for mass-change scenarios.

3. **Analytical insight into limiting-factor classification**: Through the transition mass, system limiting factors are clearly classified into BoS-dominated and actuator-capacity-dominated categories, revealing why increasing BoS width can paradoxically lower critical mass under certain conditions (e.g., mobj,trans drops to 0.9 kg at τ_ref^UB + 2BoS_ref), providing counterintuitive yet explainable guidance for mechanical design (foot dimensions, joint selection).

## Experiments and Results

### Comparison Setup

To validate the effectiveness of the BSB constraint, the authors conducted experiments on two platforms: a 2-DOF reduced-order mechanism (a lumped-mass system on a support link) for analytically tractable parametric analysis, and the full-scale ROBOTIS-OP3 humanoid robot (mass **3.5 kg**, standing height **0.51 m**, foot length **0.127 m**), performing sagittal-plane double-support object lifting tasks in both Webots simulation and physical experiments. Tasks included lift-and-hold and lift-and-release. The baseline comparison condition used CoP (ZMP) constraints with margins, replacing the BSB constraint; optimization employed direct collocation with SQP, and control used PID with proportional adjustment terms. In the reduced-order mechanism, link parameters were l1 = **0.2 m**, l2 = **0.13 m**, masses m1 = **1.74 kg**, m2 = **0.23 kg**, object mass swept from **0** to **5.85 kg** (step **0.05 kg**), torque limits scaled by **0.2–2.0**× τ_ref^UB, BoS scaled by **0.5, 1.0, 2.0**× BoS_ref, and terminal time T = **0.8 s**. In humanoid experiments, object mass ranged from **0** to **1.5 kg** (**42.86%** of robot mass), CoM Y positions spanned **21** equally spaced values between hip height **0.12 m** and **0.19 m**, BoS dimensions were fl (sl = **0**) and **1.5**fl (sl = **0.5**fl), with terminal times T = **0.95 s** and T = **1.0 s**, respectively.

### Key Numbers

| Platform | Condition | mobj,trans (kg) | Max ṙx(0) (m/s) | Max feasible mobject (kg) |
|---|---|---|---|---|
| Reduced-order | 0.2 τ_ref^UB, BoS_ref | **0** | **0.26** | **0.35** |
| Reduced-order | 0.3 τ_ref^UB, BoS_ref | — | **0.42** | **0.7** |
| Reduced-order | 0.5 τ_ref^UB, BoS_ref | — | **0.9** | **1.2** |
| Reduced-order | τ_ref^UB, BoS_ref | **2.15** | **0.45** | **2.8** |
| Reduced-order | 2 τ_ref^UB, BoS_ref | **4.85** | **0.46** | **5.5** |
| Reduced-order | τ_ref^UB, 0.5BoS_ref | **2.4** | **0.24** | **2.65** |
| Reduced-order | τ_ref^UB, 2BoS_ref | **0.9** | **0.81** | **2.8** |
| Reduced-order | 2 τ_ref^UB, 2BoS_ref | **3.75** | **0.83** | **5.85** |
| Humanoid | fl BoS | — | — | **1.2** (critical mass, **34.28%**) |
| Humanoid | 1.5fl BoS | — | — | **0.6** (critical mass, **17.14%**) |

### Implications of Results

- **Object mass exhibits a nonlinear trade-off with balance capability**: Under unconstrained conditions, larger object mass enhances balance capability by increasing available momentum (similar to a tightrope walker's balance pole effect), but joint torque limits, BoS dimensions, and friction cones constrain this benefit. In the reduced-order mechanism, the maximum feasible object mass under τ_ref^UB and BoS_ref conditions was analytically approximated as **2.6 kg** and numerically optimized to **2.8 kg**; when mobject < mobj,trans, BoS is the limiting factor; at mobject = mobj,trans, both constraints activate simultaneously; when mobject > mobj,trans, torque limits become the limiting factor and balance capability decreases with increasing mass. In the humanoid, the critical mass was **1.2 kg** for fl BoS and **0.6 kg** for 1.5fl BoS, validating this trade-off relationship.

- **BoS and torque limits exhibit asymmetric effects**: Increasing BoS (e.g., from BoS_ref to **2**BoS_ref) improves the BSB for a given object mass (max ṙx(0) increases from **0.45** to **0.81 m/s**) but has almost no effect on the feasible region (max feasible mass remains **2.8 kg**); increasing torque limits (e.g., from τ_ref^UB to **2**τ_ref^UB) significantly expands the feasible region (max feasible mass increases from **2.8** to **5.5 kg**) but has almost no effect on the BSB below critical mass (max ṙx(0) changes only from **0.45** to **0.46 m/s**), exhibiting a saturation effect.

- **CoP margin constraints are insufficient as precise stability thresholds**: In the lift-and-hold experiment (sl = **0**, mobject = **0.6 kg**), the cost function value under the BSB constraint was **4.481 N²m²s** and the robot successfully completed the lift; under the CoP margin constraint, the cost function value was **4.784 N²m²s**, with the actual CoP range (**–0.44** to **–0.019 m**) well within the constraint boundaries (**–0.058** to **0.058**, corresponding to **91.34%** of the BoS dimension), yet the robot still fell. This demonstrates that balance capability is limited by system/contact constraints and current joint states, not merely CoP position. In the lift-and-release experiment (squat-to-stand phase cost function value **6.036 N²m²s**), the CoM state remained within BSB(0 kg) after release, successfully achieving final static balance, validating the effectiveness of the BSB as a sufficient condition.

## Boundaries and Limitations

- All analyses are limited to 2D sagittal-plane, double-support (DS) scenarios, without extension to 3D arbitrary directions, stepping recovery, or disturbances such as slips/trips.
- The object is simplified as a point mass (m_object); although the inertia tensor I_object appears in the formulation, it was not independently varied for validation.
- No quantitative performance comparison was conducted against existing control methods (MPC, RL, etc.), nor was benchmarking performed across multiple humanoid platforms.
- In real applications, object mass parameters require external estimation (referencing related literature); this paper does not implement unknown-mass estimation.
- Optimization computational cost is high; although offline computation with parameter continuation is proposed as mitigation, no inference frequency data for online real-time operation is provided.

## Engineering Insights

When reproducing, first verify the applicability conditions of the **transition mass formula**: m_obj,trans = τ_UB/(0.5·BoS_x·g) − m₁ − m₂ requires τ_UB ≥ (m₂ + m_object)·g·l₂; otherwise, this analytical value is invalid. The most common pitfall is the **effectiveness of BSB constraint application**—one must ensure that the q_sampled used in BSB construction is consistent with the intermediate conditions in trajectory optimization; otherwise, the sufficient condition fails and the constraint becomes ineffective.

For engineering design, if actuator capacity is limited (small τ_ref^UB), increasing BoS (e.g., lengthening the foot) may paradoxically lower critical mass (see the τ_ref^UB + 2BoS_ref case); one should first estimate mobj,trans using the reduced-order mechanism model before deciding on mechanical design direction. For downstream teams, it is recommended to compute and store the BSB offline, then use the linear dynamic characteristics of object mass for parameter continuation during online queries, avoiding real-time nonlinear optimization. During experimental validation, note that CoP margin constraints can still lead to falls even when trajectories remain entirely within boundaries (as demonstrated by the lift-and-hold experiment), so CoP margins should not be used as a substitute metric for safety verification.

## 개요

본 논문은 물체 질량 매개변수를 전신 동역학 및 균형 안정성 유역(BSB) 프레임워크에 명시적으로 포함하는 엄밀한 공식화 방법을 제안하여, 휴머노이드 로봇의 물체 들어올리기 작업에서 물체 질량이 균형 안정성에 미치는 비선형적 상충 관계를 정량적으로 분석하고, BSB를 명시적 제약 조건으로 사용하여 안정적인 들어올리기 제어를 위한 궤적 최적화를 수행한다. 저자들은 ROBOTIS-OP3 휴머노이드 로봇에서 시뮬레이션과 실험을 통해 이 방법의 lift-and-hold 및 lift-and-release 작업에서의 효용성을 검증하고, 임계 질량과 전이 질량과 같은 핵심 설계 매개변수를 규명했다.

## 무엇을 바꾸었는가

이 연구의 핵심 변화는 "물체 질량"을 부하 작업 제어의 수동적 매개변수에서 능동적 균형 안정성 설계 변수로 승격시킨 것이다. 기존 방법은 CoP/ZMP와 같은 기준점 판정(충분하지도 필요하지도 않음)에 의존하거나, 역진자와 같은 축소 차수 모델(전신 특성 부족)을 사용하여 물체 질량이 전신 동역학 균형에 미치는 결합 영향을 체계적으로 정량화하지 못했다. 저자들은 엄밀한 공식화를 통해 물체 질량과 균형 능력 사이의 비선형적 상충 관계를 최초로 확립하고, "임계 질량"과 "전이 질량"의 해석적 정의를 제시했다. 이는 로봇 설계자에게 "너무 무겁게 들지 말라"는 직관을 넘어선 정량적 설계 기준을 제공한다.

더 중요하게, 저자들은 BSB를 오프라인 분석 도구에서 온라인 궤적 최적화의 명시적 제약 조건으로 전환했다. 이 전환은 기존 궤적 최적화 방법(MPC, RL 등)에서 균형 제약이 너무 보수적이거나(CoP 마진) 안전성을 보장할 수 없는(무제약) 근본적 모순을 해결한다. "현재 상태가 변화 후 시스템의 BSB 내에 있으면, 모든 이전 상태는 주어진 접촉 하에서 균형을 이룬다"는 충분 조건을 증명함으로써, 저자들은 질량 급변 시나리오(예: 순간 방출)에 대해 이전 어떤 방법도 제공하지 못한 이론적 안전 보장을 제공한다.

## 방법 분해

### 전신 동역학 공식화
- 물체 질량 매개변수(m_object, I_object)를 관절 공간 동역학에 명시적으로 포함: M(q)q̈ + h(q,q̇) = τ_gen + c_stance(q)·γ + c_other(q)·γ, 여기서 일반화 좌표 q ∈ ℝ^(n+6)는 관절과 부동 기저부를 포함한다.
- 선형 운동량 및 각운동량 방정식에 각각 물체 질량 항을 도입: ΣF_p = m_robot·r̈_robot + m_object·r̈_object + (m_robot + m_object)g.
- 접촉력/CoP 분포는 비차원 매개변수 벡터 α ∈ ℝ⁶로 매개변수화하여 이중 지지상의 역학적 불확정성(법선력 분배, 마찰력 방향, CoP 국소 좌표 등)을 해결한다.

### 상충 관계 및 핵심량 정의
- **임계 질량**: 시스템 균형 능력(CoM X-속도 교란 진폭)이 최대가 되는 물체 질량.
- **전이 질량**: m_obj,trans = τ_UB/(0.5·BoS_x·g) − m₁ − m₂, 제한 요인 분류에 사용:
  - m_object < m_obj,trans: BoS 차원 제한(구동 용량 미활용)
  - m_object = m_obj,trans: 두 제약 동시 활성화
  - m_object > m_obj,trans: 구동 용량 제한(CoP가 BoS 전체 범위를 활용할 수 없음)

### BSB 구축 및 궤적 최적화
- 이산화된 전신 자세 영역에 대해 제약 비선형 최적화 문제를 풀어 ṙ_x(0)를 최대화하며, 제약 조건에는 전신 동역학, 시스템/접촉 제약, 초기/최종 조건, 균형 유지 및 작업 요구사항이 포함된다.
- 최적화 변수: 3차 B-스플라인 제어 정점 v + 비차원 변수 α; 해법 알고리즘은 직접 배치법을 사용한 SQP이며, 해석적 기울기와 실행 가능한 초기 해를 사용한다.
- 들어올리기 작업은 두 단계로 나뉜다: 스쿼트-투-스탠드 단계는 제어 노력을 최소화하고, 안정화 단계는 최종 정적 균형을 달성하기 위한 실행 가능한 해를 찾는다.
- BSB 제약 적용: lift-and-hold는 물체 질량을 포함한 BSB(식 24)를, lift-and-release는 물체 질량이 0인 BSB(식 25)를 사용한다.

## 핵심 혁신

1. **물체 질량의 명시적 균형 정량화**: 물체 질량 매개변수를 전신 동역학 및 BSB 프레임워크에 엄밀하게 포함하여, 질량 증가에 따라 균형 능력이 먼저 증가한 후 감소하는 비선형적 상충 관계를 최초로 확립하고, 임계 질량과 전이 질량의 해석적 정의를 제시했다. 이는 기존의 "추가 질량이 유익하다"는 발견적 지식을 넘어 계산 가능한 정량적 설계 기준을 제공한다.

2. **궤적 최적화의 명시적 제약으로서의 BSB**: 질량 속성 변화 하의 충분 조건(현재 상태가 변화 후 시스템 BSB 내에 있음 ⇒ 모든 이전 상태가 균형)을 증명함으로써, BSB를 오프라인 분석 도구에서 온라인 궤적 최적화의 안전 제약으로 전환했다. 이는 CoP 마진 제약의 과도한 보수성과 무제약 방법의 불안전성이라는 핵심 모순을 해결하며, 특히 질량 급변 시나리오에 적합하다.

3. **제한 요인 분류의 해석적 통찰**: 전이 질량을 통해 시스템 제한 요인을 BoS 지배형과 구동 용량 지배형으로 명확히 분류하고, 특정 조건에서 BoS 폭을 늘리면 오히려 임계 질량이 감소하는 이유(예: τ_ref^UB + 2BoS_ref에서 mobj,trans가 0.9 kg으로 감소)를 밝혀, 기계 설계(발 크기, 관절 선정)에 반직관적이지만 설명 가능한 지침을 제공한다.

## 실험 및 결과

### 대조 설정

BSB 제약의 효용성을 검증하기 위해 저자들은 두 가지 플랫폼에서 실험을 수행했다: 첫째는 해석적으로 다루기 쉬운 매개변수 분석을 위한 2자유도 축소 기구(지지 링크의 집중 질량 시스템), 둘째는 ROBOTIS-OP3 전신 휴머노이드 로봇(질량 **3.5 kg**, 직립 높이 **0.51 m**, 발 길이 **0.127 m**)으로, Webots 시뮬레이션과 실물에서 시상면 이중 지지상의 물체 들어올리기 작업을 수행했다. 작업에는 lift-and-hold(들어올려 유지)와 lift-and-release(들어올려 방출)가 포함된다. 기준 대조 조건은 BSB 제약을 대체하는 마진이 있는 CoP(ZMP) 제약이며, 최적화는 직접 배치법과 SQP로 해결하고 제어는 PID에 비례 조정 항을 더한 방식이다. 축소 기구에서 링크 매개변수는 l1 = **0.2 m**, l2 = **0.13 m**, 질량 m1 = **1.74 kg**, m2 = **0.23 kg**, 물체 질량 스캔 범위는 **0** ~ **5.85 kg**(간격 **0.05 kg**), 토크 상한 스케일은 **0.2–2.0**배 τ_ref^UB, BoS 스케일은 **0.5, 1.0, 2.0**배 BoS_ref, 종료 시간 T = **0.8 s**이다. 휴머노이드 로봇 실험에서 물체 질량 범위는 **0** ~ **1.5 kg**(로봇 질량의 **42.86%**), CoM Y 위치는 엉덩이 높이 **0.12 m** ~ **0.19 m** 사이에서 **21**개의 등간격 값, BoS 차원은 fl(sl = **0**)과 **1.5**fl(sl = **0.5**fl), 종료 시간은 각각 T = **0.95 s**와 T = **1.0 s**이다.

### 핵심 수치

| 플랫폼 | 조건 | mobj,trans (kg) | 최대 ṙx(0) (m/s) | 최대 실행 가능 mobject (kg) |
|---|---|---|---|---|
| 축소 기구 | 0.2 τ_ref^UB, BoS_ref | **0** | **0.26** | **0.35** |
| 축소 기구 | 0.3 τ_ref^UB, BoS_ref | — | **0.42** | **0.7** |
| 축소 기구 | 0.5 τ_ref^UB, BoS_ref | — | **0.9** | **1.2** |
| 축소 기구 | τ_ref^UB, BoS_ref | **2.15** | **0.45** | **2.8** |
| 축소 기구 | 2 τ_ref^UB, BoS_ref | **4.85** | **0.46** | **5.5** |
| 축소 기구 | τ_ref^UB, 0.5BoS_ref | **2.4** | **0.24** | **2.65** |
| 축소 기구 | τ_ref^UB, 2BoS_ref | **0.9** | **0.81** | **2.8** |
| 축소 기구 | 2 τ_ref^UB, 2BoS_ref | **3.75** | **0.83** | **5.85** |
| 휴머노이드 로봇 | fl BoS | — | — | **1.2**(임계 질량, **34.28%** 비율) |
| 휴머노이드 로봇 | 1.5fl BoS | — | — | **0.6**(임계 질량, **17.14%** 비율) |

### 결과 의미

- **물체 질량은 균형 능력에 비선형적 상충 관계를 보인다**: 무제약 조건에서 더 큰 물체 질량은 사용 가능한 운동량을 증가시켜 균형 능력을 향상시키지만(줄타기 균형 막대 효과와 유사), 관절 토크 상한, BoS 크기 및 마찰 원뿔과 같은 제약이 이 이득을 제한한다. 축소 기구에서 최대 실행 가능 물체 질량은 τ_ref^UB 및 BoS_ref 조건에서 해석적으로 약 **2.6 kg**, 수치 최적화로 **2.8 kg**이다; mobject < mobj,trans일 때 BoS가 제한 요인이고, mobject = mobj,trans일 때 두 제약이 동시에 활성화되며, mobject > mobj,trans일 때 토크 상한이 제한 요인이 되어 균형 능력이 질량 증가에 따라 감소한다. 휴머노이드 로봇에서 fl BoS의 임계 질량은 **1.2 kg**, 1.5fl BoS에서는 **0.6 kg**으로 이 상충 관계를 검증한다.

- **BoS와 토크 한계는 비대칭적 효과를 가진다**: BoS를 늘리면(예: BoS_ref에서 **2**BoS_ref로) 주어진 물체 질량에서 BSB가 향상되지만(최대 ṙx(0)가 **0.45**에서 **0.81 m/s**로 증가), 실행 가능 영역에는 거의 영향을 미치지 않는다(최대 실행 가능 질량은 여전히 **2.8 kg**); 토크 한계를 늘리면(예: τ_ref^UB에서 **2**τ_ref^UB로) 실행 가능 영역이 크게 확장되지만(최대 실행 가능 질량이 **2.8**에서 **5.5 kg**로 증가), 임계 질량 이하의 BSB에는 거의 영향을 미치지 않으며(최대 ṙx(0)가 **0.45**에서 **0.46 m/s**로만 변화), 포화 효과를 보인다.

- **CoP 마진 제약은 정밀한 안정성 임계값으로 충분하지 않다**: lift-and-hold 실험(sl = **0**, mobject = **0.6 kg**)에서 BSB 제약 하의 비용 함수 값은 **4.481 N²m²s**이고 로봇은 들어올리기를 성공적으로 완료했다; CoP 마진 제약 하의 비용 함수 값은 **4.784 N²m²s**이며, 실제 CoP 범위(**–0.44** ~ **–0.019 m**)는 제약 경계(**–0.058** ~ **0.058**, BoS 차원의 **91.34%**에 해당) 내에 훨씬 있지만 로봇은 여전히 넘어졌다. 이는 균형 능력이 단순한 CoP 위치가 아닌 시스템/접촉 제약과 현재 관절 상태에 의해 제한됨을 시사한다. lift-and-release 실험(스쿼트-투-스탠드 단계 비용 함수 값 **6.036 N²m²s**)에서 방출 후 CoM 상태가 BSB(0 kg) 내에 유지되어 최종 정적 균형을 성공적으로 달성했으며, 이는 BSB가 충분 조건으로서의 효용성을 검증한다.

## 경계 및 한계

- 모든 분석은 2D 시상면, 이중 지지상(DS) 시나리오로 제한되며, 3D 임의 방향, 보폭 회복, 미끄러짐/걸림과 같은 교란으로 확장되지 않았다.
- 물체는 점 질량(m_object)으로 단순화되었으며, 관성 텐서 I_object는 공식에 포함되지만 독립적으로 변화시켜 검증되지는 않았다.
- 기존 제어 방법(MPC, RL 등)과의 정량적 성능 비교가 수행되지 않았고, 다양한 휴머노이드 플랫폼에서의 벤치마크 테스트도 없다.
- 실제 응용에서 물체 질량 매개변수는 외부 추정이 필요하며(관련 문헌 인용), 본 논문은 미지 질량 추정을 구현하지 않았다.
- 최적화 계산 비용이 높으며, 오프라인 계산과 매개변수 연속법으로 완화했지만 온라인 실시간 실행의 추론 빈도 데이터는 제공되지 않았다.

## 공학적 시사점

재현 시 먼저 **전이 질량 공식**의 적용 조건을 확인해야 한다: m_obj,trans = τ_UB/(0.5·BoS_x·g) − m₁ − m₂는 τ_UB ≥ (m₂ + m_object)·g·l₂를 충족해야 하며, 그렇지 않으면 이 해석 값이 성립하지 않는다. 가장 쉽게 실수하는 부분은 **BSB 제약 적용의 유효성**이다 — BSB 구축에 사용된 q_sampled가 궤적 최적화의 중간 조건과 일치하는지 반드시 확인해야 하며, 그렇지 않으면 충분 조건이 성립하지 않아 제약이 무의미해진다.

공학적 선정 측면에서, 관절 구동 용량이 제한적이라면(τ_ref^UB가 작음), BoS를 늘리는 것(예: 발바닥 연장)이 오히려 임계 질량을 낮출 수 있으므로(τ_ref^UB + 2BoS_ref 사례 참조), 먼저 축소 기구 모델로 mobj,trans를 추정한 후 기계 설계 방향을 결정해야 한다. 하류 팀에게는 BSB를 오프라인으로 계산하여 저장하고, 온라인 조회 시 물체 질량의 선형 동역학 특성을 활용한 매개변수 연속법을 사용하여 실시간 비선형 최적화를 피할 것을 권장한다. 실험 검증 시 주의할 점: CoP 마진 제약은 궤적이 완전히 경계 내에 있더라도 넘어질 수 있으므로(들어올리기-유지 실험에서 입증됨), CoP 마진을 안전 검증의 대체 지표로 사용하지 말아야 한다.
