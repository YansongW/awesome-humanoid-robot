---
$id: ent_paper_deep_whole_body_control_unified_policy_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion'
  zh: 'Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion'
  ko: 'Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomotion'
summary:
  en: An attached arm can significantly increase the applicability of legged robots to several mobile manipulation tasks that
    are not possible for the wheeled or tracked counterparts. The standard hierarchical control pipeline for such legged manipulators
    is to decouple the controller into that of manipulation and locomotion. However, this is ineffective. It requires immense
    engineering to support.
  zh: 本文提出一种基于强化学习的统一全身控制策略，在 Unitree Go1 四足机器人搭载 6-DoF WidowX 机械臂的平台上，实现腿臂协同的移动操作。核心贡献在于提出 Regularized Online Adaptation
    解决 Sim2Real 可实现性差距，以及 Advantage Mixing 解决统一策略训练中操作与运动目标的冲突，在真实世界拾取任务中显著优于 MPC+IK 基线。
  ko: An attached arm can significantly increase the applicability of legged robots to several mobile manipulation tasks that
    are not possible for the wheeled or tracked counterparts. The standard hierarchical control pipeline for such legged manipulators
    is to decouple the controller into that of manipulation and locomotion. However, this is ineffective. It requires immense
    engineering to support.
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
- deep
- whole
- body
- control
- unified
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): xiaoze_P042. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. [2026-08-05] guardrail fix: unverifiable numbers corrected to
    full-text-verbatim or marked as computed/未提取 (catchup sweep audit).'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2210.10044 Deep Whole-Body Control: Learning a Unified Policy for Manipulation and Locomoti'
  url: https://arxiv.org/abs/2210.10044
  date: '2022-10-18'
  accessed_at: '2026-08-05'
---

## 概述

本文提出一种基于强化学习的统一全身控制策略，在 Unitree Go1 四足机器人搭载 6-DoF WidowX 机械臂的平台上，实现腿臂协同的移动操作。核心贡献在于提出 Regularized Online Adaptation 解决 Sim2Real 可实现性差距，以及 Advantage Mixing 解决统一策略训练中操作与运动目标的冲突，在真实世界拾取任务中显著优于 MPC+IK 基线。

## 它改变了什么

传统腿臂移动操作采用分层解耦架构（腿部 MPC 运动控制 + 手臂 IK 操作控制），这种设计存在两个根本缺陷：一是模块间错误传播导致运动不自然、不协调；二是缺乏 Bernstein 所强调的肢体运动协同的生物学合理性。现有学习型方法（如 [8]）虽引入学习，但仍保持半耦合分层模型，未真正解决协调问题。

本文真正改变的是将操作与运动从"两个独立优化问题"重构为"一个联合优化问题"。作者指出，直接端到端训练统一策略会陷入局部最优——策略只跟随末端执行器指令而忽略腿部动作空间探索。这一观察揭示了统一策略训练的核心矛盾：操作奖励信号远强于运动奖励，导致腿部退化。本文通过 Advantage Mixing 的课程化优势加权，以及 Regularized Online Adaptation 的单阶段训练范式，使统一策略成为可行方案，而非仅仅是理论上的优雅构想。

## 方法拆解

### Regularized Online Adaptation（单阶段训练）
- 随机初始化特权编码器 μ、适应模块 φ、统一策略 π，初始化空回放缓冲区 D
- 每轮迭代中，当 `itr mod H == 0`（H=20）时用 φ 计算 `z_t^φ = φ(s_{t-10:t-1}, a_{t-11:t-2})`，否则用 μ 计算 `z_t^μ = μ(e_t)`
- 动作 `a_t = π((s_t, a_{t-1}, z_t))`，存储 `((s_t,e_t), a_t, r_t, (s_{t+1},e_{t+1}), z_t^φ, z_t^μ)` 到 D
- 当 `itr mod H == 0` 时优化 `||sg[z_t^μ] - z_t^φ||_2` 更新 θ_φ；否则优化 `-J(θ_π,θ_μ) + λ||z_t^μ - sg[z_t^φ]||_2` 更新 θ_π, θ_μ
- λ 按线性课程从 0 到 1：`λ = min(max((itr-5000)/5000, 0), 1)`
- 关键设计：μ 与策略 π 端到端联合训练，同时正则化 z^μ 避免与 z^φ 偏差过大；φ 通过在线模仿 z^μ 训练。RMA 是本文方法的特例（λ 恒为 0 且 φ 在策略收敛后才训练）

### Advantage Mixing（课程化优势加权）
- 训练目标从 `log(π(a_t^arm|s_t)π(a_t^leg|s_t))(A^manip + A^loco)` 改写为：
  `log π(a_t^arm|s_t)(A^manip + βA^loco) + log π(a_t^leg|s_t)(βA^manip + A^loco)`
- β 从 0 线性增加到 1：`β = min(t/T_mix, 1)`
- 设计理由：先分别将操作回报差异归因于手臂动作、运动回报差异归因于腿部动作，避免统一策略只优化末端执行器指令而忽略腿部探索；随后逐步退火加权优势总和，鼓励学习帮助运动和操作的腿/臂动作

### 策略网络结构
- 多层感知机，输入当前状态 `s_t ∈ ℝ^75` 与环境外在变量 `z_t ∈ ℝ^20` 拼接
- 第一隐藏层 128 维，之后分裂为 2 个头，每个头 2 个隐藏层各 128 维
- 两头的输出拼接，分别输出腿动作 `a_t^leg ∈ ℝ^12` 与臂动作 `a_t^arm ∈ ℝ^6`
- 采用关节空间位置控制（而非操作空间控制），理由：能学习避免自碰撞并减小 Sim-to-Real 差距

### 地形生成与命令采样
- 分形噪声生成地形：octaves=2，lacunarity=2.0，gain=0.25，frequency=10 Hz，amplitude=0.15 m
- 粗糙地形强制足部离地高度，替代平坦地形所需的复杂奖励
- EE 指令球坐标 (l, p, y) 经 `T(S2C[(l,p,y)]) + (p_x^base, p_y^base, p_z^base)` 得到世界坐标；`p_z^base` 设为常数 0.53，T 中 row 和 pitch 设为 0

## 关键创新

1. **Regularized Online Adaptation 的单阶段范式**：不同于 RMA 的两阶段教师-学生方案（先训练教师策略再蒸馏学生），本文让特权编码器 μ 与策略 π 端到端联合训练，并通过 λ 课程正则化强制 z^μ 与 z^φ 对齐。这消除了可实现性差距（realizability gap），使部署时的适应模块与训练时的特权信息编码器行为一致，而非事后逼近。

2. **Advantage Mixing 的课程化优势分解**：将统一策略的联合优势分解为手臂和腿部各自的加权优势，β 从 0 到 1 的课程设计使策略先分别学习操作和运动任务，再逐步合并。这直接解决了统一策略训练中操作奖励主导导致腿部退化的局部最优问题，是端到端全身控制可行的关键机制。

3. **低成本硬件平台的全栈部署**：在 6K USD 的 Unitree Go1 + WidowX 平台上实现完全无束缚的机载推理（策略与适应模块在 Raspberry Pi 4 上 50 Hz 运行），展示了学习型全身控制在学术实验室可复现的硬件成本范围内达到实用性能。

## 实验与结果


### 仿真对比（表4，统一 vs 分离 vs 非协调）
| 指标 | 统一策略 | 分离策略 | 非协调策略 |
|------|---------|---------|-----------|
| 存活率 | 97.1±0.61 | 92.0±0.90 | 94.9±0.61 |
| 基座加速度 | 1.00±0.03 | 1.40±0.04 | 1.03±0.01 |
| 速度误差 | 0.31±0.03 | 0.43±0.07 | 0.33±0.01 |
| EE误差 | 0.63±0.02 | 0.92±0.10 | 0.73±0.02 |
| 总能量 | 50±0.90 | 51±0.30 | 50±0.28 |

统一策略在相同能量消耗下达到最佳性能，EE误差较分离策略降低约 31.5%（0.92→0.63，由表4数值计算）。

### 手臂工作空间与扰动鲁棒性（表5）
| 指标 | 统一策略 | 分离策略 | 非协调策略 |
|------|---------|---------|-----------|
| 工作空间 (m³) | 0.82±0.02 | 0.58±0.10 | 0.65±0.02 |
| 扰动下存活率 | 0.87±0.04 | 0.64±0.06 | 0.77±0.06 |

统一策略工作空间扩大约 41%（0.58→0.82 m³）、扰动存活率提升约 36%（0.64→0.87，均由表5数值计算）。

### OOD 环境 Sim2Real 比较（表6）
| 指标 | 域随机化 | RMA | Regularized OA | 专家(带正则) | 专家(无正则) |
|------|---------|-----|----------------|-------------|-------------|
| 可实现性差距 | - | 0.31±0.01 | 2e-4±0.00 | - | - |
| 存活率 | 95.8±0.2 | 95.2±0.2 | 97.4±0.1 | 97.8±0.2 | 98.3±0.2 |
| EE误差 | 0.40±0.00 | 0.26±0.04 | 0.21±0.00 | 0.21±0.00 | 0.21±0.00 |
| 总能量 | 21.9±0.53 | 27.3±0.95 | 25.9±0.56 | 25.8±0.49 | 25.6±0.30 |

Regularized Online Adaptation 相比 RMA 在 EE 误差上减少 20%，可实现性差距从 0.31 降至 2e-4。

### 真实世界拾取任务（表7/10，10次试验平均）
| 任务 | 方法 | 成功率 | TTC (s) | IK失败率 | 自碰撞率 |
|------|------|--------|---------|---------|---------|
| 简单(3点) | Ours | 0.8 | 5.0 | - | 0 |
| 简单(3点) | MPC+IK | 0.3 | 17 | 0.4 | 0.3 |
| 困难(5点) | Ours | 0.8 | 5.6 | - | 0 |
| 困难(5点) | MPC+IK | 0.1 | 22.0 | 0.2 | 0.5 |

本方法成功率较 MPC+IK 提升约 2.7–8 倍、任务完成时间缩短约 71–75%（均由表7数值计算得出），自碰撞率为零。

### 训练规模
- 10000 次迭代/训练批次，即 20 亿样本（2 billions）和 20 万次梯度更新
- PPO：clip range 0.2，学习率 2e-4，折扣因子 0.99，GAE λ 0.95，环境数 5000
- 每 episode 最多 1000 步，策略控制频率 50 Hz，仿真频率 200 Hz

## 边界与局限

- 夹爪开合不包含在策略内（"EE gripper closing and opening are not a part of the policy"），遥操作中由摇杆直接控制，视觉追踪中由脚本策略控制，限制了策略的完全自主性
- 视觉估计不是本工作重点，失败试验主要源于 AprilTag 位置与实际物体位置不匹配，未处理遮挡和软物体等通用物体交互
- 论文仅提供若干未来方向的第一步（"provides a first step towards several of such future directions"），具体局限未在片段中详述
- 未实现从躯干和手臂安装的以自我为中心的相机学习基于视觉的策略，也未利用前腿攀爬障碍物拾取高处物体
- 训练规模庞大（20 亿样本），对计算资源要求高，可能限制学术实验室复现

## 工程启示

- **复现优先级**：先核对 Advantage Mixing 的 β 课程实现——这是统一策略训练不陷入局部最优的关键，β 从 0 到 1 的线性增长需与训练迭代数对齐（T_mix 具体值论文未明确，需自行调参）
- **最易踩坑点**：Regularized Online Adaptation 中 λ 的课程调度（`λ = min(max((itr-5000)/5000, 0), 1)`）和 H=20 的交替优化周期必须严格遵循，否则 μ 与 φ 的对齐会失败；停止梯度算子 sg 的位置不能出错
- **硬件部署注意**：策略与适应模块推理在 Raspberry Pi 4 上 50 Hz 运行，WidowX 软件栈在 Nvidia TX2 上，Pi 与 TX2 之间使用 UDP 通信——需确认通信延迟是否影响 50 Hz 控制频率的稳定性
- **地形生成参数**：分形噪声参数（octaves=2，lacunarity=2.0，gain=0.25，frequency=10 Hz，amplitude=0.15 m）是强制足部离地的关键，替代复杂奖励设计，复现时不可随意更改
- **训练规模预期**：20 亿样本和 20 万次梯度更新是达到表 4-6 性能的必要条件，缩减训练规模可能导致统一策略退化到非协调策略水平
- **基线对比**：MPC+IK 基线在真实世界任务中 IK 失败率高达 0.2-0.4，自碰撞率 0.3-0.5——若你的基线表现更好，需重新评估本方法的相对优势

## 参考
- https://arxiv.org/abs/2210.10044

## Overview

This paper proposes a unified whole-body control policy based on reinforcement learning, achieving coordinated leg-arm mobile manipulation on a Unitree Go1 quadruped robot equipped with a 6-DoF WidowX robotic arm. The core contributions lie in proposing Regularized Online Adaptation to address the Sim2Real realizability gap, and Advantage Mixing to resolve the conflict between manipulation and locomotion objectives in unified policy training, significantly outperforming the MPC+IK baseline in real-world pick-and-place tasks.

## What It Changes

Traditional leg-arm mobile manipulation adopts a hierarchical decoupled architecture (leg MPC locomotion control + arm IK manipulation control), which suffers from two fundamental flaws: first, error propagation between modules leads to unnatural and uncoordinated motion; second, it lacks the biological plausibility of limb motion coordination emphasized by Bernstein. Existing learning-based methods (e.g., [8]) introduce learning but still maintain a semi-coupled hierarchical model without truly solving the coordination problem.

What this paper truly changes is reframing manipulation and locomotion from "two independent optimization problems" into "one joint optimization problem." The authors point out that directly training a unified policy end-to-end falls into local optima—the policy only follows end-effector commands while ignoring leg action-space exploration. This observation reveals the core contradiction in unified policy training: manipulation reward signals are far stronger than locomotion rewards, causing leg degradation. Through the curriculum-based advantage weighting of Advantage Mixing and the single-stage training paradigm of Regularized Online Adaptation, this paper makes the unified policy a viable solution rather than merely an elegant theoretical construct.

## Method Breakdown

### Regularized Online Adaptation (Single-Stage Training)
- Randomly initialize privileged encoder μ, adaptation module φ, unified policy π, and an empty replay buffer D
- In each iteration, when `itr mod H == 0` (H=20), compute `z_t^φ = φ(s_{t-10:t-1}, a_{t-11:t-2})` using φ; otherwise compute `z_t^μ = μ(e_t)` using μ
- Action `a_t = π((s_t, a_{t-1}, z_t))`, store `((s_t,e_t), a_t, r_t, (s_{t+1},e_{t+1}), z_t^φ, z_t^μ)` into D
- When `itr mod H == 0`, optimize `||sg[z_t^μ] - z_t^φ||_2` to update θ_φ; otherwise optimize `-J(θ_π,θ_μ) + λ||z_t^μ - sg[z_t^φ]||_2` to update θ_π, θ_μ
- λ follows a linear curriculum from 0 to 1: `λ = min(max((itr-5000)/5000, 0), 1)`
- Key design: μ is trained end-to-end jointly with policy π, while regularizing z^μ to avoid excessive deviation from z^φ; φ is trained via online imitation of z^μ. RMA is a special case of this method (λ is always 0 and φ is trained only after policy convergence)

### Advantage Mixing (Curriculum-Based Advantage Weighting)
- Training objective rewritten from `log(π(a_t^arm|s_t)π(a_t^leg|s_t))(A^manip + A^loco)` to:
  `log π(a_t^arm|s_t)(A^manip + βA^loco) + log π(a_t^leg|s_t)(βA^manip + A^loco)`
- β increases linearly from 0 to 1: `β = min(t/T_mix, 1)`
- Design rationale: first attribute manipulation return differences to arm actions and locomotion return differences to leg actions separately, avoiding the unified policy optimizing only end-effector commands while ignoring leg exploration; then gradually anneal the weighted advantage sum to encourage leg/arm actions that benefit both locomotion and manipulation

### Policy Network Architecture
- Multilayer perceptron, input is the concatenation of current state `s_t ∈ ℝ^75` and environment extrinsic variable `z_t ∈ ℝ^20`
- First hidden layer has 128 dimensions, then splits into 2 heads, each with 2 hidden layers of 128 dimensions
- Outputs of the two heads are concatenated, producing leg actions `a_t^leg ∈ ℝ^12` and arm actions `a_t^arm ∈ ℝ^6` respectively
- Uses joint-space position control (rather than operational-space control), with the rationale: it enables learning to avoid self-collision and reduces the Sim-to-Real gap

### Terrain Generation and Command Sampling
- Fractal noise terrain generation: octaves=2, lacunarity=2.0, gain=0.25, frequency=10 Hz, amplitude=0.15 m
- Rough terrain enforces foot clearance height, replacing the complex rewards needed for flat terrain
- EE command spherical coordinates (l, p, y) transformed via `T(S2C[(l,p,y)]) + (p_x^base, p_y^base, p_z^base)` to world coordinates; `p_z^base` is set to constant 0.53, and row and pitch in T are set to 0

## Key Innovations

1. **Single-stage paradigm of Regularized Online Adaptation**: Unlike RMA's two-stage teacher-student scheme (first train teacher policy, then distill student), this paper trains privileged encoder μ end-to-end jointly with policy π, and enforces alignment between z^μ and z^φ through a λ curriculum regularization. This eliminates the realizability gap, making the deployed adaptation module behave consistently with the training-time privileged information encoder, rather than approximating it post hoc.

2. **Curriculum-based advantage decomposition of Advantage Mixing**: The joint advantage of the unified policy is decomposed into weighted advantages for arm and leg respectively, with a β curriculum from 0 to 1 enabling the policy to first learn manipulation and locomotion tasks separately, then gradually merge them. This directly solves the local optimum problem where manipulation reward dominance causes leg degradation in unified policy training, and is the key mechanism making end-to-end whole-body control feasible.

3. **Full-stack deployment on low-cost hardware platform**: Fully untethered onboard inference on a 6K USD Unitree Go1 + WidowX platform (policy and adaptation module running at 50 Hz on Raspberry Pi 4), demonstrating that learning-based whole-body control achieves practical performance within hardware costs reproducible in academic laboratories.

## Experiments and Results

### Simulation Comparison (Table 4, Unified vs Separated vs Uncoordinated)
| Metric | Unified Policy | Separated Policy | Uncoordinated Policy |
|--------|---------------|-----------------|---------------------|
| Survival Rate | 97.1±0.61 | 92.0±0.90 | 94.9±0.61 |
| Base Acceleration | 1.00±0.03 | 1.40±0.04 | 1.03±0.01 |
| Velocity Error | 0.31±0.03 | 0.43±0.07 | 0.33±0.01 |
| EE Error | 0.63±0.02 | 0.92±0.10 | 0.73±0.02 |
| Total Energy | 50±0.90 | 51±0.30 | 50±0.28 |

The unified policy achieves the best performance at the same energy consumption, with EE error reduced by approximately 31.5% compared to the separated policy (0.92→0.63, computed from Table 4 values).

### Arm Workspace and Disturbance Robustness (Table 5)
| Metric | Unified Policy | Separated Policy | Uncoordinated Policy |
|--------|---------------|-----------------|---------------------|
| Workspace (m³) | 0.82±0.02 | 0.58±0.10 | 0.65±0.02 |
| Survival Rate under Disturbance | 0.87±0.04 | 0.64±0.06 | 0.77±0.06 |

The unified policy expands workspace by approximately 41% (0.58→0.82 m³) and improves disturbance survival rate by approximately 36% (0.64→0.87, both computed from Table 5 values).

### OOD Environment Sim2Real Comparison (Table 6)
| Metric | Domain Randomization | RMA | Regularized OA | Expert (with Reg.) | Expert (without Reg.) |
|--------|---------------------|-----|----------------|-------------------|----------------------|
| Realizability Gap | - | 0.31±0.01 | 2e-4±0.00 | - | - |
| Survival Rate | 95.8±0.2 | 95.2±0.2 | 97.4±0.1 | 97.8±0.2 | 98.3±0.2 |
| EE Error | 0.40±0.00 | 0.26±0.04 | 0.21±0.00 | 0.21±0.00 | 0.21±0.00 |
| Total Energy | 21.9±0.53 | 27.3±0.95 | 25.9±0.56 | 25.8±0.49 | 25.6±0.30 |

Regularized Online Adaptation reduces EE error by 20% compared to RMA, and the realizability gap drops from 0.31 to 2e-4.

### Real-World Pick-and-Place Task (Table 7/10, average of 10 trials)
| Task | Method | Success Rate | TTC (s) | IK Failure Rate | Self-Collision Rate |
|------|--------|-------------|---------|-----------------|---------------------|
| Simple (3 points) | Ours | 0.8 | 5.0 | - | 0 |
| Simple (3 points) | MPC+IK | 0.3 | 17 | 0.4 | 0.3 |
| Difficult (5 points) | Ours | 0.8 | 5.6 | - | 0 |
| Difficult (5 points) | MPC+IK | 0.1 | 22.0 | 0.2 | 0.5 |

This method improves success rate by approximately 2.7–8 times over MPC+IK and reduces task completion time by approximately 71–75% (both computed from Table 7 values), with zero self-collision rate.

### Training Scale
- 10000 iterations/training batches, i.e., 2 billion samples and 200,000 gradient updates
- PPO: clip range 0.2, learning rate 2e-4, discount factor 0.99, GAE λ 0.95, 5000 environments
- Maximum 1000 steps per episode, policy control frequency 50 Hz, simulation frequency 200 Hz

## Boundaries and Limitations

- Gripper opening/closing is not included in the policy ("EE gripper closing and opening are not a part of the policy"), controlled directly by joystick in teleoperation and by scripted policy in visual tracking, limiting the policy's full autonomy
- Visual estimation is not the focus of this work; failed trials mainly stem from mismatch between AprilTag positions and actual object positions, without handling occlusion and generic object interaction such as soft objects
- The paper only provides a first step towards several future directions ("provides a first step towards several of such future directions"), with specific limitations not detailed in the excerpt
- Does not implement vision-based policies learned from ego-centric cameras mounted on the torso and arm, nor does it utilize front legs for climbing obstacles to pick up high objects
- Training scale is massive (2 billion samples), demanding significant computational resources, potentially limiting reproduction in academic laboratories

## Engineering Insights

- **Reproduction priority**: First verify the β curriculum implementation of Advantage Mixing—this is key to preventing the unified policy from falling into local optima; the linear growth of β from 0 to 1 needs to be aligned with training iteration count (the specific value of T_mix is not explicitly stated in the paper and requires self-tuning)
- **Most likely pitfall**: The λ curriculum scheduling in Regularized Online Adaptation (`λ = min(max((itr-5000)/5000, 0), 1)`) and the alternating optimization period of H=20 must be strictly followed, otherwise the alignment between μ and φ will fail; the placement of the stop-gradient operator sg must not be erroneous
- **Hardware deployment notes**: Policy and adaptation module inference runs at 50 Hz on Raspberry Pi 4, the WidowX software stack runs on Nvidia TX2, with UDP communication between Pi and TX2—communication latency must be verified to ensure stability of the 50 Hz control frequency
- **Terrain generation parameters**: Fractal noise parameters (octaves=2, lacunarity=2.0, gain=0.25, frequency=10 Hz, amplitude=0.15 m) are key to enforcing foot clearance, replacing complex reward design; they must not be arbitrarily modified during reproduction
- **Training scale expectations**: 2 billion samples and 200,000 gradient updates are necessary conditions for achieving the performance in Tables 4-6; reducing training scale may cause the unified policy to degrade to the level of the uncoordinated policy
- **Baseline comparison**: The MPC+IK baseline exhibits IK failure rates as high as 0.2-0.4 and self-collision rates of 0.3-0.5 in real-world tasks—if your baseline performs better, the relative advantages of this method need to be reassessed

## 개요

본 논문은 강화 학습 기반의 통합 전신 제어 정책을 제안하며, Unitree Go1 4족 보행 로봇에 6-DoF WidowX 로봇 팔을 장착한 플랫폼에서 다리-팔 협력 이동 조작을 구현합니다. 핵심 기여는 Sim2Real 실현 가능성 격차를 해결하는 Regularized Online Adaptation과 통합 정책 훈련에서 조작 및 운동 목표의 충돌을 해결하는 Advantage Mixing을 제안한 것이며, 실제 세계 물체 집기 작업에서 MPC+IK 기준선보다 현저히 우수한 성능을 보입니다.

## 무엇을 변화시켰는가

기존의 다리-팔 이동 조작은 계층적 분리 아키텍처(다리 MPC 운동 제어 + 팔 IK 조작 제어)를 채택했으며, 이러한 설계에는 두 가지 근본적인 결함이 있습니다: 첫째, 모듈 간 오류 전파로 인해 부자연스럽고 비협조적인 움직임이 발생합니다; 둘째, Bernstein이 강조한 사지 운동 협조의 생물학적 타당성이 부족합니다. 기존의 학습 기반 방법(예: [8])은 학습을 도입했지만 여전히 반결합 계층 모델을 유지하여 협조 문제를 진정으로 해결하지 못했습니다.

본 논문이 진정으로 변화시킨 것은 조작과 운동을 "두 개의 독립적인 최적화 문제"에서 "하나의 결합 최적화 문제"로 재구성한 것입니다. 저자들은 직접적인 엔드투엔드 훈련 통합 정책이 국소 최적해에 빠질 수 있음을 지적합니다——정책이 말단 실행기 명령만 따르고 다리 동작 공간 탐색을 무시합니다. 이러한 관찰은 통합 정책 훈련의 핵심 모순을 드러냅니다: 조작 보상 신호가 운동 보상보다 훨씬 강하여 다리 퇴화를 초래합니다. 본 논문은 Advantage Mixing의 커리큘럼 기반 이점 가중치와 Regularized Online Adaptation의 단일 단계 훈련 패러다임을 통해 통합 정책을 이론적으로 우아한 구상에 그치지 않고 실현 가능한 방안으로 만듭니다.

## 방법 분석

### Regularized Online Adaptation (단일 단계 훈련)
- 특권 인코더 μ, 적응 모듈 φ, 통합 정책 π를 무작위 초기화하고 빈 리플레이 버퍼 D를 초기화
- 각 반복에서 `itr mod H == 0`(H=20)일 때 φ로 `z_t^φ = φ(s_{t-10:t-1}, a_{t-11:t-2})`를 계산하고, 그 외에는 μ로 `z_t^μ = μ(e_t)`를 계산
- 동작 `a_t = π((s_t, a_{t-1}, z_t))`, 저장 `((s_t,e_t), a_t, r_t, (s_{t+1},e_{t+1}), z_t^φ, z_t^μ)`을 D에 저장
- `itr mod H == 0`일 때 `||sg[z_t^μ] - z_t^φ||_2`를 최적화하여 θ_φ를 업데이트; 그 외에는 `-J(θ_π,θ_μ) + λ||z_t^μ - sg[z_t^φ]||_2`를 최적화하여 θ_π, θ_μ를 업데이트
- λ는 선형 커리큘럼으로 0에서 1까지: `λ = min(max((itr-5000)/5000, 0), 1)`
- 핵심 설계: μ는 정책 π와 엔드투엔드로 결합 훈련되며, 동시에 z^μ가 z^φ와 너무 크게 편향되지 않도록 정규화; φ는 온라인 모방을 통해 z^μ를 학습. RMA는 본 방법의 특수한 경우입니다(λ가 항상 0이고 φ는 정책 수렴 후에만 훈련)

### Advantage Mixing (커리큘럼 기반 이점 가중치)
- 훈련 목표를 `log(π(a_t^arm|s_t)π(a_t^leg|s_t))(A^manip + A^loco)`에서 다음과 같이 변경:
  `log π(a_t^arm|s_t)(A^manip + βA^loco) + log π(a_t^leg|s_t)(βA^manip + A^loco)`
- β는 0에서 1로 선형 증가: `β = min(t/T_mix, 1)`
- 설계 근거: 먼저 조작 보상 차이를 팔 동작에, 운동 보상 차이를 다리 동작에 각각 귀속시켜 통합 정책이 말단 실행기 명령만 최적화하고 다리 탐색을 무시하는 것을 방지; 이후 점진적으로 가중 이점 합계를 감쇠하여 운동과 조작을 돕는 다리/팔 동작 학습을 장려

### 정책 네트워크 구조
- 다층 퍼셉트론, 입력은 현재 상태 `s_t ∈ ℝ^75`와 환경 외생 변수 `z_t ∈ ℝ^20`을 연결
- 첫 번째 은닉층은 128차원, 이후 2개의 헤드로 분할되며 각 헤드는 128차원의 2개 은닉층을 가짐
- 두 헤드의 출력을 연결하여 다리 동작 `a_t^leg ∈ ℝ^12`와 팔 동작 `a_t^arm ∈ ℝ^6`을 각각 출력
- 관절 공간 위치 제어(조작 공간 제어가 아닌)를 채택, 이유: 자체 충돌을 학습하고 Sim-to-Real 격차를 줄일 수 있음

### 지형 생성 및 명령 샘플링
- 프랙탈 노이즈로 지형 생성: octaves=2, lacunarity=2.0, gain=0.25, frequency=10 Hz, amplitude=0.15 m
- 거친 지형은 발의 지면 이탈 높이를 강제하여 평평한 지형에 필요한 복잡한 보상을 대체
- EE 명령 구면 좌표 (l, p, y)는 `T(S2C[(l,p,y)]) + (p_x^base, p_y^base, p_z^base)`를 통해 세계 좌표로 변환; `p_z^base`는 상수 0.53으로 설정, T의 row와 pitch는 0으로 설정

## 핵심 혁신

1. **Regularized Online Adaptation의 단일 단계 패러다임**: RMA의 2단계 교사-학생 방식(먼저 교사 정책 훈련 후 학생 증류)과 달리, 본 논문은 특권 인코더 μ와 정책 π를 엔드투엔드로 결합 훈련하고 λ 커리큘럼 정규화를 통해 z^μ와 z^φ의 정렬을 강제합니다. 이는 실현 가능성 격차(realizability gap)를 제거하여 배포 시 적응 모듈이 훈련 시 특권 정보 인코더와 일관된 동작을 하도록 만들며, 사후 근사가 아닙니다.

2. **Advantage Mixing의 커리큘럼 기반 이점 분해**: 통합 정책의 결합 이점을 팔과 다리의 각각 가중 이점으로 분해하고, β가 0에서 1로 증가하는 커리큘럼 설계를 통해 정책이 먼저 조작 및 운동 작업을 각각 학습한 후 점진적으로 병합합니다. 이는 통합 정책 훈련에서 조작 보상이 지배하여 다리가 퇴화하는 국소 최적해 문제를 직접 해결하며, 엔드투엔드 전신 제어를 실현 가능하게 만드는 핵심 메커니즘입니다.

3. **저비용 하드웨어 플랫폼의 풀스택 배포**: 6K USD의 Unitree Go1 + WidowX 플랫폼에서 완전한 무구속 온보드 추론(정책 및 적응 모듈이 Raspberry Pi 4에서 50 Hz로 실행)을 구현하여 학습 기반 전신 제어가 학술 연구실에서 재현 가능한 하드웨어 비용 범위 내에서 실용적 성능에 도달함을 보여줍니다.

## 실험 및 결과

### 시뮬레이션 비교 (표4, 통합 vs 분리 vs 비협조)
| 지표 | 통합 정책 | 분리 정책 | 비협조 정책 |
|------|---------|---------|-----------|
| 생존율 | 97.1±0.61 | 92.0±0.90 | 94.9±0.61 |
| 베이스 가속도 | 1.00±0.03 | 1.40±0.04 | 1.03±0.01 |
| 속도 오차 | 0.31±0.03 | 0.43±0.07 | 0.33±0.01 |
| EE 오차 | 0.63±0.02 | 0.92±0.10 | 0.73±0.02 |
| 총 에너지 | 50±0.90 | 51±0.30 | 50±0.28 |

통합 정책은 동일한 에너지 소비에서 최고 성능을 달성하며, EE 오차는 분리 정책 대비 약 31.5% 감소(0.92→0.63, 표4 수치 계산).

### 팔 작업 공간 및 교란 강건성 (표5)
| 지표 | 통합 정책 | 분리 정책 | 비협조 정책 |
|------|---------|---------|-----------|
| 작업 공간 (m³) | 0.82±0.02 | 0.58±0.10 | 0.65±0.02 |
| 교란 하 생존율 | 0.87±0.04 | 0.64±0.06 | 0.77±0.06 |

통합 정책의 작업 공간은 약 41% 확대(0.58→0.82 m³), 교란 생존율은 약 36% 향상(0.64→0.87, 모두 표5 수치 계산).

### OOD 환경 Sim2Real 비교 (표6)
| 지표 | 도메인 무작위화 | RMA | Regularized OA | 전문가(정규화 포함) | 전문가(정규화 없음) |
|------|---------|-----|----------------|-------------|-------------|
| 실현 가능성 격차 | - | 0.31±0.01 | 2e-4±0.00 | - | - |
| 생존율 | 95.8±0.2 | 95.2±0.2 | 97.4±0.1 | 97.8±0.2 | 98.3±0.2 |
| EE 오차 | 0.40±0.00 | 0.26±0.04 | 0.21±0.00 | 0.21±0.00 | 0.21±0.00 |
| 총 에너지 | 21.9±0.53 | 27.3±0.95 | 25.9±0.56 | 25.8±0.49 | 25.6±0.30 |

Regularized Online Adaptation은 RMA 대비 EE 오차가 20% 감소하고, 실현 가능성 격차가 0.31에서 2e-4로 감소합니다.

### 실제 세계 물체 집기 작업 (표7/10, 10회 시행 평균)
| 작업 | 방법 | 성공률 | TTC (s) | IK 실패율 | 자체 충돌률 |
|------|------|--------|---------|---------|---------|
| 단순(3점) | Ours | 0.8 | 5.0 | - | 0 |
| 단순(3점) | MPC+IK | 0.3 | 17 | 0.4 | 0.3 |
| 어려움(5점) | Ours | 0.8 | 5.6 | - | 0 |
| 어려움(5점) | MPC+IK | 0.1 | 22.0 | 0.2 | 0.5 |

본 방법의 성공률은 MPC+IK 대비 약 2.7–8배 향상, 작업 완료 시간은 약 71–75% 단축(모두 표7 수치 계산), 자체 충돌률은 0입니다.

### 훈련 규모
- 10000회 반복/훈련 배치, 즉 20억 샘플(2 billions) 및 20만 회 경사 업데이트
- PPO: clip range 0.2, 학습률 2e-4, 할인 계수 0.99, GAE λ 0.95, 환경 수 5000
- 각 에피소드는 최대 1000단계, 정책 제어 주파수 50 Hz, 시뮬레이션 주파수 200 Hz

## 경계 및 한계

- 그리퍼 개폐는 정책에 포함되지 않음("EE gripper closing and opening are not a part of the policy"), 원격 조작에서는 조이스틱으로 직접 제어되고, 시각 추적에서는 스크립트 정책으로 제어되어 정책의 완전한 자율성이 제한됨
- 시각 추정은 본 연구의 핵심이 아니며, 실패 시행은 주로 AprilTag 위치와 실제 물체 위치의 불일치에서 발생, 폐색 및 연성 물체와 같은 일반적인 물체 상호작용은 처리하지 않음
- 논문은 여러 미래 방향에 대한 첫 단계만 제공("provides a first step towards several of such future directions"), 구체적인 한계는 본문에서 자세히 설명되지 않음
- 몸통 및 팔에 장착된 자기 중심 카메라로부터 시각 기반 정책을 학습하지 않았으며, 앞다리로 장애물을 기어올라 높은 물체를 집는 것도 활용하지 않음
- 훈련 규모가 방대(20억 샘플)하여 계산 자원 요구가 높아 학술 연구실의 재현을 제한할 수 있음

## 공학적 시사점

- **재현 우선순위**: 먼저 Advantage Mixing의 β 커리큘럼 구현을 확인——이는 통합 정책 훈련이 국소 최적해에 빠지지 않도록 하는 핵심이며, β의 0에서 1로의 선형 증가는 훈련 반복 수와 정렬되어야 함(T_mix 구체적 값은 논문에 명시되지 않아 자체 튜닝 필요)
- **가장 실수하기 쉬운 지점**: Regularized Online Adaptation에서 λ의 커리큘럼 스케줄(`λ = min(max((itr-5000)/5000, 0), 1)`)과 H=20의 교대 최적화 주기를 엄격히 따라야 하며, 그렇지 않으면 μ와 φ의 정렬이 실패; 정지 경사 연산자 sg의 위치를 잘못 두면 안 됨
- **하드웨어 배포 주의**: 정책 및 적응 모듈 추론은 Raspberry Pi 4에서 50 Hz로 실행되고, WidowX 소프트웨어 스택은 Nvidia TX2에 있으며, Pi와 TX2 사이는 UDP 통신 사용——통신 지연이 50 Hz 제어 주파수의 안정성에 영향을 미치는지 확인 필요
- **지형 생성 매개변수**: 프랙탈 노이즈 매개변수(octaves=2, lacunarity=2.0, gain=0.25, frequency=10 Hz, amplitude=0.15 m)는 발의 지면 이탈을 강제하는 핵심으로 복잡한 보상 설계를 대체하므로 재현 시 임의로 변경할 수 없음
- **훈련 규모 기대**: 20억 샘플과 20만 회 경사 업데이트는 표 4-6의 성능을 달성하기 위한 필요 조건이며, 훈련 규모를 축소하면 통합 정책이 비협조 정책 수준으로 퇴화할 수 있음
- **기준선 비교**: MPC+IK 기준선은 실제 세계 작업에서 IK 실패율이 0.2-0.4, 자체 충돌률이 0.3-0.5에 달함——기준선이 더 우수하다면 본 방법의 상대적 이점을 재평가해야 함
