---
$id: ent_paper_vision_dribbling_humanoid_soccer_privile_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning
  zh: Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning
  ko: Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learning
summary:
  en: Recent advances in humanoid robotics have highlighted the importance of deployable loco-manipulation skills. Dribbling
    a soccer ball while evading active opponents requires simultaneous balance, precise ball control, and awareness of a dynamic
    adversary under onboard sensing and real-time constraints. Existing approaches typically separate perception and motion,
    which can be effective in.
  zh: 本文由罗马大学、CSIC-UPC 和 EPFL 的研究者提出，针对双足人形机器人足球运球任务，采用特权表示学习（Privileged Representation Learning）框架，将感知与控制解耦训练：先在模拟器中以特权状态训练策略，再冻结策略、仅训练视觉编码器从深度图像重建特权潜在表示。核心贡献在于通过课程学习与
    DAgger 正则化，在 Booster T1 人形平台上实现了对静态和动态障碍物的鲁棒运球，动态对手场景下成功率 46%，并公开了代码。
  ko: Recent advances in humanoid robotics have highlighted the importance of deployable loco-manipulation skills. Dribbling
    a soccer ball while evading active opponents requires simultaneous balance, precise ball control, and awareness of a dynamic
    adversary under onboard sensing and real-time constraints. Existing approaches typically separate perception and motion,
    which can be effective in.
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
- vision
- dribbling
- humanoid
- soccer
- privile
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
  title: arXiv:2607.12702 Vision-Based Dribbling for Humanoid Soccer via Privileged Representation Learnin
  url: https://arxiv.org/abs/2607.12702
  date: '2026-07-14'
  accessed_at: '2026-08-05'
---



## 概述

本文由罗马大学、CSIC-UPC 和 EPFL 的研究者提出，针对双足人形机器人足球运球任务，采用特权表示学习（Privileged Representation Learning）框架，将感知与控制解耦训练：先在模拟器中以特权状态训练策略，再冻结策略、仅训练视觉编码器从深度图像重建特权潜在表示。核心贡献在于通过课程学习与 DAgger 正则化，在 Booster T1 人形平台上实现了对静态和动态障碍物的鲁棒运球，动态对手场景下成功率 46%，并公开了代码。

## 它改变了什么

它真正改变的是人形机器人运球任务中“感知-控制”耦合方式的范式。传统模块化方案（如 YOLO 检测 + Kalman 滤波）将感知视为独立于策略的固定模块，其输出表示并未针对下游控制目标优化，因此在遮挡、快速球运动和复杂对手交互下，感知误差会直接传导至控制层，导致任务失败。本文的核心判断是：感知不是为“看得准”服务的，而是为“控得住”服务的——因此必须让感知表示直接对齐策略所需的潜在状态空间。

这一转变的深层意义在于，它把“感知鲁棒性”问题转化为“表示对齐”问题。通过特权学习，策略在训练时获得完美状态，视觉编码器只需学习从高维深度观测中恢复策略所需的低维潜在向量，而非重建完整世界模型。这避免了端到端强化学习中感知与控制耦合训练的高样本复杂度和不稳定性，同时保留了端到端方法“感知服务于控制”的核心优势。对于 RoboCup 这类实时、动态、部分可观测的对抗场景，这种解耦方式在工程上更可控、更易调试。

## 方法拆解

方法分为两个阶段，核心设计是保持策略接口不变，仅替换潜在表示的生成机制。

### 问题形式化
- 建模为 POMDP：ℳ = (𝒮, 𝒪, 𝒜, p, r, γ)
- 状态 𝒮：机器人、球、障碍物的完整世界坐标状态 + 目标命令
- 观测 𝒪：本体感觉（IMU、关节位置/速度）+ 外感受（球/障碍物状态编码为潜在向量 z_t ∈ ℝ⁶⁴）
- 动作 𝒜：21 维身体关节位置向量，头部独立控制

### 阶段 1：特权策略学习
- 演员观测：o_t^actor = [o_t^prop, z_t]，其中 z_t 由小型 MLP 从地面真值球状态和最近障碍物状态（机器人坐标系）映射得到
- 课程学习沿两个轴：阶段（phase）定义 z_t 获取方式，层级（stage）定义障碍物难度
- 四层级课程：
  - 层级 0：无障碍物，球远离，学习接近和运球（普通 PPO）
  - 层级 1：无障碍物，球靠近，精炼目标导向运球
  - 层级 2：静态阻挡物，学习避障和轨迹恢复
  - 层级 3：动态对手与球交互，学习在线反应控制
- 层级 1-3 从上一层级检查点初始化，使用 DAgger 正则化 PPO 目标：
  - ℒ_total = ℒ_PPO + λ_imit 𝔼[||π_θ(a_t|s_t) − π₀(a_t|s_t)||²₂]
  - 模仿项以层级 0 策略为教师，缓解灾难性遗忘，保留标称运动能力

### 阶段 2：视觉适应
- 策略冻结，仅训练视觉编码器从深度观测重建潜在 z_t
- 架构：CNN（每帧深度特征 ℝ⁶⁴）→ GRU（时间聚合 ℝ²⁵⁶）→ 投影头（ℝ⁶⁴）
- 深度帧分辨率 108 × 192，保持原始宽高比
- 训练损失：
  - ℒ_adapt = ℒ_latent + λ_ball^pos ℒ_ball^pos + λ_ball^vel ℒ_ball^vel + λ_obs^pos ℒ_obs^pos + λ_obs^vel ℒ_obs^vel
  - 主项 ℒ_latent = ||z_t^adapt − z_t^priv||²₂，辅助预测头回归球/障碍物状态作为正则化

### 关键设计决策
- 保持两个阶段演员接口完全一致，仅改变潜在生成机制，策略架构不变——这保证了阶段 2 训练时策略无需重新调整
- 任务目标 g^w ∈ ℝ² 在世界坐标系中围绕球位置采样，避免每步重新采样速度，减少非平稳性
- 奖励函数包含 26 项，覆盖球控（速度跟踪、航向）、姿态（摆动相、支撑相）、安全（碰撞、摔倒）等多个维度

## 关键创新

1. **特权表示学习用于人形机器人运球**：将 DribbleBot 等四足平台的特权学习思想扩展到双足人形，解决了动态平衡与高自由度带来的额外挑战。其新颖性在于课程学习与 DAgger 正则化的结合——层级 0 的标称策略作为教师，防止后续层级学习时遗忘基础运球能力，这是四足工作中未见的。

2. **感知-控制接口的稳定设计**：通过固定潜在向量维度（ℝ⁶⁴）和演员观测结构，阶段 2 的视觉适应完全独立于策略优化。这使得视觉编码器可以在策略冻结的情况下训练，大幅降低训练复杂度，同时保证部署时策略行为与模拟一致。

3. **阻塞时间步的细粒度诊断**：引入“阻塞”（blocked）时间步定义（障碍物在球-目标方向前向 2.0 m 内、距球-目标线 0.75 m 内），将评估细分为未阻塞/阻塞子条件。这揭示了动态对手场景下性能下降的主因是闭环控制而非感知失败——阻塞时角度误差从 34.27° 升至 43.00°，但球位置误差仅从 0.05 m 升至 0.08 m。

## 实验与结果


## 实验与结果

**对照设置。** 我们在仿真环境（mjlab 框架，Booster T1 人形机器人，平坦地面）中评估最终策略，设置三种条件：无障碍物、静态障碍物（单个静止障碍物置于球到目标走廊附近）、球攻击者（单个移动障碍物以固定速度追逐球，速度采样范围 `[0.1, 0.4] m/s`）。终止条件为成功到达目标（球-目标距离 `≤ 0.75 m`）、超时（`30 s`）、机器人摔倒、球丢失（机器人-球距离超过 `2.0 m`）；障碍物碰撞不终止试验，仅记录为安全指标。评估规模为 5 个随机种子、每条件每种子 10 次试验（每条件共 50 次试验）。无外部基线，主要对比三种条件间的表现差异及课程阶段消融。指标包括成功率（SR）、到达时间（T2T/T2T-C）、摔倒率（FR）、丢球率（LR）、机器人-障碍物碰撞率（RCR）与每试验接触次数（RC/t）、球-障碍物碰撞率（BCR）与每试验接触次数（BC/t）、最小球-障碍物净距（MBC），以及速度诊断（`e_vec`、`e_spd`、`e_ang`）和感知指标（`e_ball,pos`、`e_ball,vel`、`e_obs,pos`、`e_obs,vel`、`c_fov`）。训练采用两阶段框架：Phase 1 特权编码器 + 四阶段课程（Stage 0 无障碍球远、Stage 1 无障碍球近、Stage 2 单个静态阻挡、Stage 3 单个动态对手）；Phase 2 冻结策略，训练视觉编码器（CNN + GRU）从深度观测（尺寸 `108 × 192`）预测潜变量。

**关键数字（Table 2–5）。**

| 条件 | SR [%] | T2T [s] | T2T-C [s] | FR [%] | LR [%] | RCR [%] | RC/t [#/trial] | BCR [%] | BC/t [#/trial] | MBC [m] |
|---|---|---|---|---|---|---|---|---|---|---|
| 无障碍物 | `100.00` | `11.45` | `11.45` | `0.00` | `0.00` | – | – | – | – | – |
| 静态障碍物 | `96.00` | `13.29` | `13.95` | `4.00` | `0.00` | `8.00` | `0.08` | `4.00` | `0.10` | `1.73` |
| 球攻击者 | `46.00` | `11.82` | `21.64` | `52.00` | `2.00` | `68.00` | `0.72` | `40.00` | `0.70` | `1.36` |

速度诊断（Table 3）：无障碍物全部时间步 `e_vec=0.71`、`e_spd=0.62`、`e_ang=28.39`；静态障碍物未阻塞/阻塞分别为 `0.74/0.74`、`0.62/0.60`、`35.62/33.96`；球攻击者未阻塞/阻塞分别为 `0.74/0.79`、`0.61/0.60`、`34.27/43.00`。感知指标（Table 4）：无障碍物 `e_ball,pos=0.05`、`e_ball,vel=0.25`、`c_fov=75.43`；静态障碍物 `0.05/0.24/1.26/0.21/76.74`；球攻击者 `0.08/0.26/1.26/0.13/78.39`。课程消融成功率（Table 5，%）：无障碍物 Stage 1/2/3 为 `100/68/90`；静态障碍物为 `24/42/88`；球攻击者为 `2/2/46`。

**结果含义。**

- **名义带球被可靠保留，静态障碍物可有效处理。** 无障碍条件达到 `100.00 %` 成功率且零失败（FR、LR 均为 `0.00`）；静态障碍物条件下成功率保持 `96.00 %`，到达时间仅适度增加（T2T `13.29 s` vs 无障碍 `11.45 s`），碰撞率低（RCR `8.00 %`、BCR `4.00 %`），表明策略能应对单个静止障碍物而不显著牺牲任务表现。
- **主动移动对手仍是开放问题。** 球攻击者条件下成功率骤降至 `46.00 %`，摔倒率（`52.00 %`）与碰撞率（RCR `68.00 %`、BCR `40.00 %`）大幅上升，超时截尾到达时间（T2T-C `21.64 s`）明显高于成功试验到达时间（T2T `11.82 s`），说明对主动追逐者的鲁棒带球尚未解决。
- **感知并非主要瓶颈，闭环控制难度是限制因素。** 感知指标在各条件间相对稳定（球位置误差 `0.05–0.08 m`，障碍物位置误差均为 `1.26 m`），球攻击者条件下阻塞时间步呈现最大角度误差（`e_ang=43.00`）与向量误差（`e_vec=0.79`），表明偏离名义指令主要源于对移动对手的闭环控制困难，而非严重感知失败。
- **课程策略有效提升障碍物回避能力。** Stage 1（仅无障碍球近）在存在障碍物时表现极差（静态 `24 %`、球攻击者 `2 %`），而 Stage 3 后静态条件达 `88 %`、球攻击者达 `46 %`，验证了逐步增加难度使策略获得障碍物回避能力的有效性。

## 边界与局限

作者明确承认的局限包括：动态对手场景成功率仅 46%，对主动移动对手的鲁棒运球仍是开放问题；主要限制不是感知失败而是对移动对手的闭环控制难度。所有实验均在模拟中进行，未进行真实世界（sim-to-real）部署实验，仅概述了原则性路线图。此外，独立训练策略数量少（5 种子），统计功效有限。论文未明确提及训练/推理频率、硬件配置、PPO 超参数等复现细节，也未讨论视觉编码器在球完全移出视野时的处理策略（评估中仅在地面真值球位置可用时计算感知指标）。

## 工程启示

对复现和下游团队的工程启示：

1. **先核对课程学习的关键超参数**：层级间初始化与 DAgger 正则化权重 λ_imit 是方法核心，但论文未给出具体值。复现时建议从 λ_imit = 0.1 起步，观察层级 1-2 是否出现灾难性遗忘（可参考表 5 中层级 1 在静态障碍物下仅 24% 的退化现象）。

2. **最容易踩坑的是“阻塞”判定逻辑**：阻塞时间步定义（前向 2.0 m、距线 0.75 m）直接影响诊断指标的可比性。若下游任务中障碍物速度或尺寸不同，需重新校准这些阈值，否则 e_ang 等指标会失真。

3. **视觉编码器的 GRU 时间窗口是感知鲁棒性的关键**：球在近距离运球时频繁移出视野（c_fov 仅 75-78%），GRU 的时间聚合是维持状态估计的核心。复现时建议优先验证 GRU 隐藏维度 256 是否足够，以及深度帧 108×192 分辨率在真实相机上的迁移效果。

4. **动态对手场景的瓶颈在控制而非感知**：若你的团队目标是提升对抗鲁棒性，应优先改进策略对障碍物运动的预测与反应，而非优化视觉编码器。表 4 显示感知误差已足够小（球位置误差 0.08 m），但 SR 仍仅 46%。

5. **奖励函数中安全项权重需谨慎调整**：机器人-障碍物碰撞和球-障碍物碰撞均为 −10.0，但动态场景下 RCR 仍达 68%，说明策略在“避碰”与“推进”之间存在权衡。若下游任务更看重安全，可尝试提高碰撞惩罚或引入安全约束。

## 参考
- https://arxiv.org/abs/2607.12702

## Overview

This paper, proposed by researchers from Sapienza University, CSIC-UPC, and EPFL, addresses the task of bipedal humanoid robot soccer dribbling using a Privileged Representation Learning framework. It decouples perception and control training: first, a policy is trained with privileged states in simulation, then the policy is frozen and only a visual encoder is trained to reconstruct the privileged latent representation from depth images. The core contribution lies in combining curriculum learning with DAgger regularization to achieve robust dribbling against static and dynamic obstacles on the Booster T1 humanoid platform, reaching a 46% success rate in dynamic opponent scenarios, with code released publicly.

## What It Changes

What it truly changes is the paradigm of the "perception-control" coupling in humanoid robot dribbling tasks. Traditional modular approaches (e.g., YOLO detection + Kalman filtering) treat perception as a fixed module independent of the policy, whose output representation is not optimized for downstream control objectives. Consequently, under occlusion, fast ball motion, and complex opponent interactions, perception errors propagate directly to the control layer, causing task failure. The core judgment of this paper is that perception does not serve "seeing accurately" but rather "controlling effectively"—therefore, the perceptual representation must be directly aligned with the latent state space required by the policy.

The deeper significance of this shift is that it transforms the "perceptual robustness" problem into a "representation alignment" problem. Through privileged learning, the policy obtains perfect states during training, and the visual encoder only needs to learn to recover the low-dimensional latent vector required by the policy from high-dimensional depth observations, rather than reconstructing a complete world model. This avoids the high sample complexity and instability of coupled perception-control training in end-to-end reinforcement learning, while retaining the core advantage of end-to-end methods where "perception serves control." For real-time, dynamic, partially observable adversarial scenarios like RoboCup, this decoupling is more controllable and easier to debug from an engineering perspective.

## Method Breakdown

The method consists of two phases, with the core design being to keep the policy interface unchanged and only replace the mechanism for generating the latent representation.

### Problem Formulation
- Modeled as a POMDP: ℳ = (𝒮, 𝒪, 𝒜, p, r, γ)
- State 𝒮: complete world-coordinate states of the robot, ball, and obstacles + goal command
- Observation 𝒪: proprioception (IMU, joint positions/velocities) + exteroception (ball/obstacle states encoded as latent vector z_t ∈ ℝ⁶⁴)
- Action 𝒜: 21-dimensional body joint position vector, with independent head control

### Phase 1: Privileged Policy Learning
- Actor observation: o_t^actor = [o_t^prop, z_t], where z_t is mapped by a small MLP from ground-truth ball state and nearest obstacle state (in robot coordinates)
- Curriculum learning along two axes: phase defines how z_t is obtained, stage defines obstacle difficulty
- Four-stage curriculum:
  - Stage 0: no obstacles, ball far away, learning approach and dribbling (standard PPO)
  - Stage 1: no obstacles, ball close, refining goal-directed dribbling
  - Stage 2: static blockers, learning obstacle avoidance and trajectory recovery
  - Stage 3: dynamic opponents interacting with the ball, learning online reactive control
- Stages 1–3 initialize from the checkpoint of the previous stage, using DAgger-regularized PPO objective:
  - ℒ_total = ℒ_PPO + λ_imit 𝔼[||π_θ(a_t|s_t) − π₀(a_t|s_t)||²₂]
  - The imitation term uses the Stage 0 policy as teacher, mitigating catastrophic forgetting and preserving nominal locomotion capabilities

### Phase 2: Visual Adaptation
- Policy frozen, only the visual encoder is trained to reconstruct the latent z_t from depth observations
- Architecture: CNN (per-frame depth features ℝ⁶⁴) → GRU (temporal aggregation ℝ²⁵⁶) → projection head (ℝ⁶⁴)
- Depth frame resolution 108 × 192, preserving original aspect ratio
- Training loss:
  - ℒ_adapt = ℒ_latent + λ_ball^pos ℒ_ball^pos + λ_ball^vel ℒ_ball^vel + λ_obs^pos ℒ_obs^pos + λ_obs^vel ℒ_obs^vel
  - Main term ℒ_latent = ||z_t^adapt − z_t^priv||²₂, with auxiliary prediction heads regressing ball/obstacle states as regularization

### Key Design Decisions
- Keeping the actor interface identical across both phases, only changing the latent generation mechanism, with the policy architecture unchanged—this ensures the policy requires no re-tuning during Phase 2 training
- Task goal g^w ∈ ℝ² is sampled in world coordinates around the ball position, avoiding per-step resampling of velocity and reducing non-stationarity
- The reward function includes 26 terms covering ball control (velocity tracking, heading), posture (swing phase, stance phase), and safety (collisions, falls)

## Key Innovations

1. **Privileged representation learning for humanoid robot dribbling**: Extends privileged learning ideas from quadruped platforms like DribbleBot to bipedal humanoids, addressing the additional challenges of dynamic balance and high degrees of freedom. The novelty lies in the combination of curriculum learning with DAgger regularization—the Stage 0 nominal policy serves as a teacher, preventing forgetting of basic dribbling skills during later stages, which is absent in quadruped work.

2. **Stable perception-control interface design**: By fixing the latent vector dimension (ℝ⁶⁴) and actor observation structure, Phase 2 visual adaptation is completely independent of policy optimization. This allows the visual encoder to be trained with the policy frozen, greatly reducing training complexity while ensuring deployed policy behavior matches simulation.

3. **Fine-grained diagnostics for blocked time steps**: Introduces a "blocked" time-step definition (obstacle within 2.0 m forward of the ball-goal direction and within 0.75 m of the ball-goal line), splitting evaluation into unblocked/blocked sub-conditions. This reveals that performance degradation in dynamic opponent scenarios stems primarily from closed-loop control rather than perception failure—blocked angular error rises from 34.27° to 43.00°, but ball position error only increases from 0.05 m to 0.08 m.

## Experiments and Results

**Comparison setup.** We evaluate the final policy in simulation (mjlab framework, Booster T1 humanoid robot, flat ground) under three conditions: no obstacles, static obstacles (a single stationary obstacle placed near the ball-to-goal corridor), and ball attacker (a single moving obstacle chasing the ball at a fixed speed, sampled from `[0.1, 0.4] m/s`). Termination conditions are successful goal arrival (ball-goal distance `≤ 0.75 m`), timeout (`30 s`), robot fall, and ball loss (robot-ball distance exceeding `2.0 m`); obstacle collisions do not terminate trials and are only recorded as safety metrics. Evaluation scale is 5 random seeds with 10 trials per condition per seed (50 trials per condition total). No external baselines; the primary comparisons are performance differences across conditions and curriculum stage ablations. Metrics include success rate (SR), time-to-target (T2T/T2T-C), fall rate (FR), ball loss rate (LR), robot-obstacle collision rate (RCR) with contacts per trial (RC/t), ball-obstacle collision rate (BCR) with contacts per trial (BC/t), minimum ball-obstacle clearance (MBC), as well as velocity diagnostics (`e_vec`, `e_spd`, `e_ang`) and perception metrics (`e_ball,pos`, `e_ball,vel`, `e_obs,pos`, `e_obs,vel`, `c_fov`). Training uses a two-phase framework: Phase 1 privileged encoder with a four-stage curriculum (Stage 0 no obstacles with ball far, Stage 1 no obstacles with ball close, Stage 2 single static blocker, Stage 3 single dynamic opponent); Phase 2 freezes the policy and trains a visual encoder (CNN + GRU) to predict latent variables from depth observations (size `108 × 192`).

**Key numbers (Tables 2–5).**

| Condition | SR [%] | T2T [s] | T2T-C [s] | FR [%] | LR [%] | RCR [%] | RC/t [#/trial] | BCR [%] | BC/t [#/trial] | MBC [m] |
|---|---|---|---|---|---|---|---|---|---|---|
| No obstacles | `100.00` | `11.45` | `11.45` | `0.00` | `0.00` | – | – | – | – | – |
| Static obstacles | `96.00` | `13.29` | `13.95` | `4.00` | `0.00` | `8.00` | `0.08` | `4.00` | `0.10` | `1.73` |
| Ball attacker | `46.00` | `11.82` | `21.64` | `52.00` | `2.00` | `68.00` | `0.72` | `40.00` | `0.70` | `1.36` |

Velocity diagnostics (Table 3): no obstacles all time steps `e_vec=0.71`, `e_spd=0.62`, `e_ang=28.39`; static obstacles unblocked/blocked are `0.74/0.74`, `0.62/0.60`, `35.62/33.96`; ball attacker unblocked/blocked are `0.74/0.79`, `0.61/0.60`, `34.27/43.00`. Perception metrics (Table 4): no obstacles `e_ball,pos=0.05`, `e_ball,vel=0.25`, `c_fov=75.43`; static obstacles `0.05/0.24/1.26/0.21/76.74`; ball attacker `0.08/0.26/1.26/0.13/78.39`. Curriculum ablation success rates (Table 5, %): no obstacles Stage 1/2/3 are `100/68/90`; static obstacles are `24/42/88`; ball attacker is `2/2/46`.

**Interpretation of results.**

- **Nominal ball carrying is reliably preserved, and static obstacles are handled effectively.** The no-obstacle condition achieves `100.00 %` success with zero failures (FR and LR both `0.00`); the static obstacle condition maintains `96.00 %` success with only a moderate increase in time-to-target (T2T `13.29 s` vs. `11.45 s` without obstacles) and low collision rates (RCR `8.00 %`, BCR `4.00 %`), indicating the policy can handle a single stationary obstacle without significantly sacrificing task performance.
- **Active moving opponents remain an open problem.** Under the ball attacker condition, success drops sharply to `46.00 %`, with fall rate (`52.00 %`) and collision rates (RCR `68.00 %`, BCR `40.00 %`) rising substantially; the timeout-truncated time-to-target (T2T-C `21.64 s`) is notably higher than the success-trial time-to-target (T2T `11.82 s`), indicating that robust dribbling against active pursuers is not yet solved.
- **Perception is not the primary bottleneck; closed-loop control difficulty is the limiting factor.** Perception metrics remain relatively stable across conditions (ball position error `0.05–0.08 m`, obstacle position error `1.26 m` in all cases), and blocked time steps under the ball attacker condition show the largest angular error (`e_ang=43.00`) and vector error (`e_vec=0.79`), suggesting that deviation from nominal commands stems mainly from closed-loop control difficulties against moving opponents rather than severe perception failures.
- **The curriculum strategy effectively improves obstacle avoidance capability.** Stage 1 (no obstacles, ball close only) performs poorly in the presence of obstacles (static `24 %`, ball attacker `2 %`), whereas after Stage 3, static conditions reach `88 %` and ball attacker `46 %`, validating that gradually increasing difficulty equips the policy with obstacle avoidance skills.

## Boundaries and Limitations

Limitations explicitly acknowledged by the authors include: the dynamic opponent scenario success rate is only 46%, and robust dribbling against actively moving opponents remains an open problem; the main limitation is not perception failure but closed-loop control difficulty against moving opponents. All experiments were conducted in simulation without real-world (sim-to-real) deployment experiments, with only a principled roadmap outlined. Additionally, the number of independently trained policies is small (5 seeds), limiting statistical power. The paper does not explicitly mention reproduction details such as training/inference frequency, hardware configuration, or PPO hyperparameters, nor does it discuss the visual encoder's handling strategy when the ball completely leaves the field of view (perception metrics are only computed when ground-truth ball positions are available in evaluation).

## Engineering Insights

Engineering insights for reproduction and downstream teams:

1. **First verify key curriculum hyperparameters**: inter-stage initialization and the DAgger regularization weight λ_imit are central to the method, but the paper does not provide specific values. For reproduction, we recommend starting with λ_imit = 0.1 and monitoring whether catastrophic forgetting occurs in Stages 1–2 (refer to the degradation observed in Table 5 where Stage 1 achieves only 24% under static obstacles).

2. **The most likely pitfall is the "blocked" determination logic**: the blocked time-step definition (2.0 m forward, 0.75 m from the line) directly affects the comparability of diagnostic metrics. If obstacle speeds or sizes differ in downstream tasks, these thresholds need recalibration; otherwise, metrics like e_ang will be distorted.

3. **The GRU temporal window of the visual encoder is key to perceptual robustness**: the ball frequently leaves the field of view during close-range dribbling (c_fov only 75–78%), and GRU temporal aggregation is central to maintaining state estimation. For reproduction, we recommend first verifying whether a GRU hidden dimension of 256 is sufficient, and how well the 108×192 depth frame resolution transfers to real cameras.

4. **The bottleneck in dynamic opponent scenarios is control, not perception**: if your team's goal is to improve adversarial robustness, prioritize improving the policy's prediction and reaction to obstacle motion rather than optimizing the visual encoder. Table 4 shows perception errors are already sufficiently small (ball position error 0.08 m), yet SR remains only 46%.

5. **Safety term weights in the reward function require careful tuning**: robot-obstacle and ball-obstacle collisions are both −10.0, yet RCR still reaches 68% in dynamic scenarios, indicating a trade-off between "collision avoidance" and "advancement." If downstream tasks prioritize safety, consider increasing collision penalties or introducing safety constraints.

## 개요

본 논문은 로마 대학, CSIC-UPC 및 EPFL의 연구자들이 제안한 것으로, 이족 보행 휴머노이드 로봇 축구 드리블 작업을 위해 특권 표현 학습(Privileged Representation Learning) 프레임워크를 사용하여 인식과 제어를 분리하여 훈련한다: 먼저 시뮬레이터에서 특권 상태로 정책을 훈련한 다음, 정책을 동결하고 시각 인코더만 훈련하여 깊이 이미지에서 특권 잠재 표현을 재구성한다. 핵심 기여는 커리큘럼 학습과 DAgger 정규화를 통해 Booster T1 휴머노이드 플랫폼에서 정적 및 동적 장애물에 대한 강건한 드리블을 구현했으며, 동적 상대 시나리오에서 성공률 46%를 달성하고 코드를 공개한 것이다.

## 무엇을 바꾸었는가

진정으로 바꾼 것은 휴머노이드 로봇 드리블 작업에서 '인식-제어' 결합 방식의 패러다임이다. 기존 모듈식 접근법(예: YOLO 감지 + Kalman 필터)은 인식을 정책과 독립적인 고정 모듈로 간주하며, 그 출력 표현은 하위 제어 목표에 맞게 최적화되지 않았다. 따라서 폐색, 빠른 볼 움직임 및 복잡한 상대 상호작용 하에서 인식 오류가 제어 계층으로 직접 전달되어 작업 실패를 초래한다. 본 논문의 핵심 판단은 인식이 '정확히 보기' 위한 것이 아니라 '안정적으로 제어하기' 위한 것이라는 점이다 — 따라서 인식 표현이 정책이 필요로 하는 잠재 상태 공간에 직접 정렬되어야 한다.

이러한 전환의 심층적 의미는 '인식 강건성' 문제를 '표현 정렬' 문제로 변환한다는 것이다. 특권 학습을 통해 정책은 훈련 중 완벽한 상태를 얻고, 시각 인코더는 고차원 깊이 관측에서 정책이 필요로 하는 저차원 잠재 벡터를 복구하는 방법만 학습하면 되며, 완전한 세계 모델을 재구성할 필요가 없다. 이는 엔드투엔드 강화 학습에서 인식과 제어의 결합 훈련으로 인한 높은 샘플 복잡성과 불안정성을 피하면서, 엔드투엔드 방식의 '인식이 제어를 위한 서비스'라는 핵심 장점을 유지한다. RoboCup과 같은 실시간, 동적, 부분 관측 가능한 대항 시나리오에서 이러한 분리 방식은 공학적으로 더 제어 가능하고 디버깅이 용이하다.

## 방법 분석

방법은 두 단계로 구성되며, 핵심 설계는 정책 인터페이스를 유지하면서 잠재 표현 생성 메커니즘만 교체하는 것이다.

### 문제 정식화
- POMDP로 모델링: ℳ = (𝒮, 𝒪, 𝒜, p, r, γ)
- 상태 𝒮: 로봇, 볼, 장애물의 완전한 세계 좌표 상태 + 목표 명령
- 관측 𝒪: 고유 감각(IMU, 관절 위치/속도) + 외부 감각(볼/장애물 상태를 잠재 벡터 z_t ∈ ℝ⁶⁴로 인코딩)
- 행동 𝒜: 21차원 신체 관절 위치 벡터, 머리는 독립적으로 제어

### 1단계: 특권 정책 학습
- 행위자 관측: o_t^actor = [o_t^prop, z_t], 여기서 z_t는 소형 MLP가 지상 실측 볼 상태와 최근 장애물 상태(로봇 좌표계)에서 매핑
- 커리큘럼 학습은 두 축을 따라 진행: 단계(phase)는 z_t 획득 방식을 정의하고, 수준(stage)은 장애물 난이도를 정의
- 4단계 커리큘럼:
  - 수준 0: 장애물 없음, 볼이 멀리 있음, 접근 및 드리블 학습(일반 PPO)
  - 수준 1: 장애물 없음, 볼이 가까이 있음, 목표 지향 드리블 정교화
  - 수준 2: 정적 차단물, 장애물 회피 및 궤적 복구 학습
  - 수준 3: 동적 상대와 볼 상호작용, 온라인 반응 제어 학습
- 수준 1-3은 이전 수준 체크포인트에서 초기화되며, DAgger 정규화 PPO 목표 사용:
  - ℒ_total = ℒ_PPO + λ_imit 𝔼[||π_θ(a_t|s_t) − π₀(a_t|s_t)||²₂]
  - 모방 항은 수준 0 정책을 교사로 사용하여 파국적 망각을 완화하고 명목 운동 능력을 보존

### 2단계: 시각 적응
- 정책 동결, 시각 인코더만 깊이 관측에서 잠재 z_t 재구성 훈련
- 아키텍처: CNN(프레임당 깊이 특징 ℝ⁶⁴) → GRU(시간 집계 ℝ²⁵⁶) → 프로젝션 헤드(ℝ⁶⁴)
- 깊이 프레임 해상도 108 × 192, 원본 종횡비 유지
- 훈련 손실:
  - ℒ_adapt = ℒ_latent + λ_ball^pos ℒ_ball^pos + λ_ball^vel ℒ_ball^vel + λ_obs^pos ℒ_obs^pos + λ_obs^vel ℒ_obs^vel
  - 주요 항 ℒ_latent = ||z_t^adapt − z_t^priv||²₂, 보조 예측 헤드가 볼/장애물 상태를 회귀하여 정규화 역할

### 핵심 설계 결정
- 두 단계의 행위자 인터페이스를 완전히 동일하게 유지하고 잠재 생성 메커니즘만 변경 — 이는 2단계 훈련 시 정책을 재조정할 필요가 없음을 보장
- 작업 목표 g^w ∈ ℝ²는 세계 좌표계에서 볼 위치 주변에 샘플링되어 매 단계 속도 재샘플링을 피하고 비정상성을 줄임
- 보상 함수는 26개 항목을 포함하며 볼 제어(속도 추적, 방향), 자세(스윙 위상, 지지 위상), 안전(충돌, 낙상) 등 여러 차원을 포괄

## 핵심 혁신

1. **휴머노이드 로봇 드리블을 위한 특권 표현 학습**: DribbleBot과 같은 사족 플랫폼의 특권 학습 개념을 이족 보행 휴머노이드로 확장하여 동적 균형과 높은 자유도가 가져오는 추가 도전을 해결. 참신성은 커리큘럼 학습과 DAgger 정규화의 결합 — 수준 0의 명목 정책이 교사 역할을 하여 후속 수준 학습 시 기본 드리블 능력의 망각을 방지하며, 이는 사족 연구에서는 볼 수 없었던 것이다.

2. **인식-제어 인터페이스의 안정적 설계**: 잠재 벡터 차원(ℝ⁶⁴)과 행위자 관측 구조를 고정함으로써 2단계의 시각 적응이 정책 최적화와 완전히 독립적이다. 이는 시각 인코더가 정책 동결 상태에서 훈련될 수 있게 하여 훈련 복잡성을 크게 줄이고, 배포 시 정책 동작이 시뮬레이션과 일치함을 보장한다.

3. **차단 시간 단계의 세밀한 진단**: '차단'(blocked) 시간 단계 정의(장애물이 볼-목표 방향 전방 2.0 m 이내, 볼-목표 선에서 0.75 m 이내)를 도입하여 평가를 비차단/차단 하위 조건으로 세분화. 이는 동적 상대 시나리오에서 성능 저하의 주요 원인이 인식 실패가 아닌 폐루프 제어임을 밝혀냈다 — 차단 시 각도 오류가 34.27°에서 43.00°로 증가했지만 볼 위치 오류는 0.05 m에서 0.08 m로만 증가.

## 실험 및 결과

**비교 설정.** 시뮬레이션 환경(mjlab 프레임워크, Booster T1 휴머노이드 로봇, 평평한 지면)에서 최종 정책을 평가하며, 세 가지 조건을 설정: 장애물 없음, 정적 장애물(단일 정지 장애물을 볼-목표 회랑 근처에 배치), 볼 공격자(단일 이동 장애물이 고정 속도로 볼을 추적, 속도 샘플링 범위 `[0.1, 0.4] m/s`). 종료 조건은 목표 도달 성공(볼-목표 거리 `≤ 0.75 m`), 시간 초과(`30 s`), 로봇 낙상, 볼 분실(로봇-볼 거리 `2.0 m` 초과); 장애물 충돌은 시험을 종료하지 않고 안전 지표로만 기록. 평가 규모는 5개 무작위 시드, 조건당 시드당 10회 시험(조건당 총 50회 시험). 외부 기준선 없음, 주로 세 조건 간 성능 차이 및 커리큘럼 단계 소거를 비교. 지표는 성공률(SR), 도달 시간(T2T/T2T-C), 낙상률(FR), 볼 분실률(LR), 로봇-장애물 충돌률(RCR) 및 시험당 접촉 횟수(RC/t), 볼-장애물 충돌률(BCR) 및 시험당 접촉 횟수(BC/t), 최소 볼-장애물 순거리(MBC), 속도 진단(`e_vec`, `e_spd`, `e_ang`) 및 인식 지표(`e_ball,pos`, `e_ball,vel`, `e_obs,pos`, `e_obs,vel`, `c_fov`). 훈련은 2단계 프레임워크 사용: 1단계 특권 인코더 + 4단계 커리큘럼(0단계 장애물 없음 볼 원거리, 1단계 장애물 없음 볼 근거리, 2단계 단일 정적 차단, 3단계 단일 동적 상대); 2단계 정책 동결, 시각 인코더(CNN + GRU)를 깊이 관측(크기 `108 × 192`)에서 잠재 변수 예측으로 훈련.

**핵심 수치(Table 2–5).**

| 조건 | SR [%] | T2T [s] | T2T-C [s] | FR [%] | LR [%] | RCR [%] | RC/t [#/trial] | BCR [%] | BC/t [#/trial] | MBC [m] |
|---|---|---|---|---|---|---|---|---|---|---|
| 장애물 없음 | `100.00` | `11.45` | `11.45` | `0.00` | `0.00` | – | – | – | – | – |
| 정적 장애물 | `96.00` | `13.29` | `13.95` | `4.00` | `0.00` | `8.00` | `0.08` | `4.00` | `0.10` | `1.73` |
| 볼 공격자 | `46.00` | `11.82` | `21.64` | `52.00` | `2.00` | `68.00` | `0.72` | `40.00` | `0.70` | `1.36` |

속도 진단(Table 3): 장애물 없음 전체 시간 단계 `e_vec=0.71`, `e_spd=0.62`, `e_ang=28.39`; 정적 장애물 비차단/차단 각각 `0.74/0.74`, `0.62/0.60`, `35.62/33.96`; 볼 공격자 비차단/차단 각각 `0.74/0.79`, `0.61/0.60`, `34.27/43.00`. 인식 지표(Table 4): 장애물 없음 `e_ball,pos=0.05`, `e_ball,vel=0.25`, `c_fov=75.43`; 정적 장애물 `0.05/0.24/1.26/0.21/76.74`; 볼 공격자 `0.08/0.26/1.26/0.13/78.39`. 커리큘럼 소거 성공률(Table 5, %): 장애물 없음 1/2/3단계 `100/68/90`; 정적 장애물 `24/42/88`; 볼 공격자 `2/2/46`.

**결과 의미.**

- **명목 볼 운반이 안정적으로 유지되고 정적 장애물을 효과적으로 처리.** 장애물 없음 조건에서 `100.00 %` 성공률과 제로 실패(FR, LR 모두 `0.00`); 정적 장애물 조건에서 성공률 `96.00 %` 유지, 도달 시간은 적절히만 증가(T2T `13.29 s` vs 장애물 없음 `11.45 s`), 충돌률 낮음(RCR `8.00 %`, BCR `4.00 %`), 정책이 단일 정지 장애물을 작업 성능을 크게 희생하지 않고 대응할 수 있음을 나타냄.
- **능동적 이동 상대는 여전히 미해결 문제.** 볼 공격자 조건에서 성공률이 `46.00 %`로 급감, 낙상률(`52.00 %`)과 충돌률(RCR `68.00 %`, BCR `40.00 %`)이 크게 증가, 시간 초과 절단 도달 시간(T2T-C `21.64 s`)이 성공 시험 도달 시간(T2T `11.82 s`)보다 현저히 높음, 능동적 추적자에 대한 강건한 볼 운반이 아직 해결되지 않았음을 시사.
- **인식이 주요 병목이 아니며, 폐루프 제어 난이도가 제한 요소.** 인식 지표는 조건 간 상대적으로 안정적(볼 위치 오류 `0.05–0.08 m`, 장애물 위치 오류 모두 `1.26 m`), 볼 공격자 조건의 차단 시간 단계에서 최대 각도 오류(`e_ang=43.00`)와 벡터 오류(`e_vec=0.79`)를 보임, 명목 명령 이탈이 주로 이동 상대에 대한 폐루프 제어 어려움에서 비롯되며 심각한 인식 실패가 아님을 시사.
- **커리큘럼 정책이 장애물 회피 능력을 효과적으로 향상.** 1단계(장애물 없음 볼 근거리만)는 장애물 존재 시 매우 낮은 성능(정적 `24 %`, 볼 공격자 `2 %`), 3단계 후 정적 조건 `88 %`, 볼 공격자 `46 %` 달성, 점진적 난이도 증가가 정책에 장애물 회피 능력을 부여하는 효과를 검증.

## 경계 및 한계

저자가 명시적으로 인정한 한계는 다음과 같다: 동적 상대 시나리오 성공률 46%에 불과, 능동적 이동 상대에 대한 강건한 드리블은 여전히 미해결 문제; 주요 제한은 인식 실패가 아닌 이동 상대에 대한 폐루프 제어 난이도. 모든 실험은 시뮬레이션에서 수행되었으며 실제 세계(sim-to-real) 배포 실험은 없었고, 원칙적 로드맵만 개요로 제시. 또한 독립 훈련 정책 수가 적고(5개 시드), 통계적 검정력이 제한적. 논문은 훈련/추론 빈도, 하드웨어 구성, PPO 하이퍼파라미터 등의 재현 세부 사항을 명시적으로 언급하지 않았으며, 볼이 완전히 시야에서 벗어날 때 시각 인코더의 처리 전략도 논의하지 않음(평가에서는 지상 실측 볼 위치가 사용 가능할 때만 인식 지표 계산).

## 공학적 시사점

재현 및 하위 팀을 위한 공학적 시사점:

1. **커리큘럼 학습의 핵심 하이퍼파라미터를 먼저 확인**: 수준 간 초기화와 DAgger 정규화 가중치 λ_imit는 방법의 핵심이지만 논문에서 구체적인 값을 제시하지 않음. 재현 시 λ_imit = 0.1에서 시작하여 수준 1-2에서 파국적 망각이 발생하는지 관찰하는 것을 권장(Table 5에서 수준 1이 정적 장애물 하에서 24%에 불과한 퇴화 현상 참조).

2. **가장 함정에 빠지기 쉬운 것은 '차단' 판정 로직**: 차단 시간 단계 정의(전방 2.0 m, 선에서 0.75 m)는 진단 지표의 비교 가능성에 직접 영향을 미침. 하위 작업에서 장애물 속도나 크기가 다르면 이러한 임계값을 재보정해야 하며, 그렇지 않으면 e_ang 등의 지표가 왜곡됨.

3. **시각 인코더의 GRU 시간 창은 인식 강건성의 핵심**: 볼이 근거리 드리블 중 자주 시야에서 벗어나며(c_fov 75-78%에 불과), GRU의 시간 집계가 상태 추정 유지의 핵심. 재현 시 GRU 은닉 차원 256이 충분한지, 깊이 프레임 108×192 해상도의 실제 카메라 전이 효과를 우선 검증할 것을 권장.

4. **동적 상대 시나리오의 병목은 제어가 아닌 인식**: 팀의 목표가 대항 강건성 향상이라면 시각 인코더 최적화보다 정책의 장애물 움직임 예측 및 반응 개선을 우선해야 함. Table 4는 인식 오류가 이미 충분히 작지만(볼 위치 오류 0.08 m) SR이 여전히 46%에 불과함을 보여줌.

5. **보상 함수의 안전 항목 가중치를 신중히 조정**: 로봇-장애물 충돌과 볼-장애물 충돌 모두 −10.0이지만 동적 시나리오에서 RCR이 여전히 68%에 달함, 정책이 '충돌 회피'와 '전진' 사이에서 절충하고 있음을 시사. 하위 작업이 안전을 더 중시한다면 충돌 페널티를 높이거나 안전 제약을 도입할 수 있음.
