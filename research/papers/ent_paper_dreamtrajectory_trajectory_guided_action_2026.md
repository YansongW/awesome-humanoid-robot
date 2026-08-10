---
$id: ent_paper_dreamtrajectory_trajectory_guided_action_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation'
  zh: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation'
  ko: 'DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment for Mobile Manipulation'
summary:
  en: Mobile manipulation requires a robot to coordinate base and arm motion under continuously changing viewpoints and contact
    conditions, within an action space far larger than that of fixed-base manipulation. Existing Vision-Language-Action (VLA)
    policies are limited in two respects. (i)They map observations directly to whole-body action chunks, searching this large
    action space without an explicit.
  zh: DreamTrajectory 是一个面向移动操作任务的端到端轨迹引导动作生成框架，由作者团队提出。其核心贡献在于：在单一动作专家中联合预测意图级末端执行器轨迹与全身动作块，并引入一个轻量级循环世界模型在测试时对候选动作进行搜索-预测-评分细化，从而同时缓解大动作空间搜索不精确与开环执行误差累积两大问题。
  ko: Mobile manipulation requires a robot to coordinate base and arm motion under continuously changing viewpoints and contact
    conditions, within an action space far larger than that of fixed-base manipulation. Existing Vision-Language-Action (VLA)
    policies are limited in two respects. (i)They map observations directly to whole-body action chunks, searching this large
    action space without an explicit.
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
- dreamtrajectory
- trajectory
- guided
- action
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails. [2026-08-05] experiments section regenerated under programmatic
    number whitelist (guardrail fix: previous numbers unverifiable against full text); en/ko regenerated. 深读+数字白名单复核通过 2026-08-10（补网）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2608.01381 DreamTrajectory: Trajectory-Guided Action Generation with World Model Alignment '
  url: https://arxiv.org/abs/2608.01381
  date: '2026-08-02'
  accessed_at: '2026-08-05'
---



## 概述

DreamTrajectory 是一个面向移动操作任务的端到端轨迹引导动作生成框架，由作者团队提出。其核心贡献在于：在单一动作专家中联合预测意图级末端执行器轨迹与全身动作块，并引入一个轻量级循环世界模型在测试时对候选动作进行搜索-预测-评分细化，从而同时缓解大动作空间搜索不精确与开环执行误差累积两大问题。

## 它改变了什么

移动操作与固定基座操作的本质区别在于，基座与机械臂的协调运动发生在连续变化的视角和接触条件下，其动作空间维度显著更高。现有 VLA 策略直接将观测映射到全身动作块，这隐含了一个强假设：网络能在无显式任务空间运动规划的情况下，从高维动作空间中精确搜索出基座-机械臂的协调解。这个假设在实践中的脆弱性体现在两个层面：一是预测出的动作块在空间上可能不连贯，导致基座与机械臂运动不协调；二是开环执行时，控制误差与未建模接触（如推拉抽屉时的反作用力）会累积成计划运动与实际运动之间的系统性偏差。

DreamTrajectory 真正改变的是“中间表示”的选择与利用方式。它没有抛弃端到端学习，而是在动作生成路径中插入了一个物理上有意义的中间变量——末端执行器轨迹。这个选择的深层动机是：末端执行器轨迹是任务空间中的紧凑描述，其维度远低于全身动作，且直接对应任务目标（如抓取、推拉）。更重要的是，它改变了动作生成的因果结构：动作不再是观测的直接函数，而是以轨迹为条件的生成结果，这迫使基座与机械臂的运动围绕一个统一的意图级计划进行协调。同时，世界模型的引入将“执行后验证”从开环变成了闭环，这是对 VLA 策略“生成即执行”范式的实质性修正。

## 方法拆解

### 轨迹引导动作生成
- **联合预测**：单一动作专家同时输出未来末端执行器轨迹 τ_{t:t+H-1} 与全身动作块 a_{t:t+H-1}，共享水平 H。
- **轨迹表示**：每个路点为 7D 位姿 τ_{t+h} = [p_{t+h}^{B_t}, q_{t+h}^{B_t}] ∈ ℝ⁷，其中位置 p ∈ ℝ³ 与四元数 q ∈ ℝ⁴ 均在块局部坐标系 B_t 中表示，锚定在当前基座位姿并固定在整个预测范围内。这一设计避免了全局坐标系下基座移动导致的轨迹坐标漂移。
- **条件流匹配**：轨迹与动作独立采样高斯噪声 ε_τ, ε_a ~ 𝒩(0, I)，共享流时间 σ ~ 𝒰(0, 1)，插值变量为 τ^σ = σε_τ + (1-σ)τ 和 a^σ = σε_a + (1-σ)a。训练目标为联合流匹配损失 ℒ_VLA = 𝔼[λ_τ‖v_τ - u_τ‖₂² + λ_a‖v_a - u_a‖₂²]，其中 u_τ = ε_τ - τ，u_a = ε_a - a。
- **组因果注意力掩码**：轨迹令牌关注多模态前缀与先前轨迹令牌；动作令牌额外关注完整轨迹流与先前动作令牌。该掩码确保轨迹信息单向流入动作生成，防止动作信息泄漏回轨迹生成，从而保持“轨迹引导动作”的因果方向。

### 测试时搜索-预测-评分细化
- **候选扰动**：保留原始动作块 â，独立采样 N-1 个扰动块 ε_i，每个动作维度遵循独立 AR(1) 高斯过程，边际标准差 σ=0.05，滞后一相关 ρ=0.9，N=30。
- **世界模型预测**：轻量级循环世界模型 W_φ(o_t, s_t, a_{t:t+H-1}) 预测候选动作块会诱导的轨迹 τ̃(a) ∈ ℝ^{H×7}。该模型从交互数据学习而非解析推导，因为命令与实现运动之间的偏差源于接触、自碰撞与低层跟踪误差。
- **评分与选择**：并行评估所有候选，选择最大化 [λS_traj(a) + (1-λ)ηS_smooth(a)] 的候选，其中 λ=0.5，η=10⁻³。S_traj 衡量预测轨迹与 VLA 生成轨迹的一致性，S_smooth 惩罚动作抖动。

### 两阶段训练
- **阶段一**：用 π_0.5 预训练权重初始化 VLA 骨干，在专家演示上微调。
- **阶段二**：用包含成功与失败试验的额外机器人-环境交互数据集训练轨迹世界模型。使用滑动窗口构建密集训练样本，动作与轨迹维度用训练集统计独立标准化。训练数据构造中，对记录的平面基座速度通道积分，将记录的末端执行器位姿从瞬时机器人基座坐标系变换到以时间 t 基座位姿为锚的块局部坐标系，并使用一步时间偏移使目标路点对应执行动作 a_{t+h} 后观测到的位姿。

## 关键创新

1. **轨迹作为显式中间表示的因果引导**：不同于以往将轨迹视为隐式潜在变量或辅助预测头，DreamTrajectory 通过组因果注意力掩码在架构层面强制轨迹信息单向引导动作生成。这一设计使得“意图级规划”与“全身执行”在单一网络中解耦又耦合，既保留了端到端学习的可微性，又为动作生成提供了任务空间约束。其新颖性在于将因果方向作为归纳偏置写入注意力机制，而非依赖损失权重或后处理。

2. **动作条件轨迹世界模型**：现有 VLA 工作要么完全开环执行，要么依赖解析运动学模型进行闭环修正。DreamTrajectory 学习一个从动作块到实际诱导轨迹的映射，且该映射是从包含失败试验的交互数据中习得的。这使其能够隐式建模接触、自碰撞与低层跟踪误差等解析模型难以刻画的因素。世界模型作为即插即用模块，可附加到任意轨迹引导策略上，无需重新训练 VLA，这在实际部署中具有显著工程价值。

3. **测试时搜索-预测-评分范式**：将生成问题转化为“生成-验证-选择”的闭环过程。通过 AR(1) 高斯过程在动作空间中进行结构化扰动（而非无差别噪声），保留了动作的时间相关性；通过世界模型并行评分 30 个候选，将计算开销控制在单张 RTX 4090 上仅增加 11.75 ms 延迟。这一范式在保持实时性的同时，将开环执行误差的修正从“预测更准”转向“选择更优”，是策略优化思路的转变。

## 实验与结果


## 实验与结果

**对照设置。** 我们在仿真与真实世界两个层面评估 DreamTrajectory（DT）。仿真采用 ManiSkill-HAB（MS-HAB）benchmark 的 set_table 套件，使用 Fetch 移动操作机器人，覆盖 6 个子任务（pick apple、pick bowl、open fridge、close fridge、open counter、close counter），每个方法每任务评估 100 个 episode，共 600 episodes/方法。基线包括 ACT、Diffusion Policy、RDT-1B、GR00T N1 与 π₀.₅。消融变体包括：DT w/o trajectory guidance（直接预测全身动作，等价于 π₀.₅ 基线）、DT w/o refiner（保留轨迹引导但直接执行初始动作块）、完整 DT（每个重规划步对 30 个候选进行轨迹世界模型精炼）。真实世界采用 ARX LIFT 移动操作机器人，覆盖 3 个任务（水果抓取放置、开抽屉、关抽屉），每个方法每任务 20 个 episode。世界模型架构消融在 4,096 条轨迹上比较 Analytical FK（开环）、Diffusion、One-shot Transformer、Cross Attention 与 GRU（DT 采用），指标包括 xyz ADE (m)、xyz FDE (m)、Angular ADE (°) 与 Geodesic ADE。计算效率在单张 RTX 4090、BF16 精度下测量。

**关键结果（MS-HAB 仿真平均成功率，%）。**

| 方法 | Avg. |
|------|------|
| ACT | 28.0 |
| Diffusion Policy | 27.7 |
| RDT-1B | 8.7 |
| GR00T N1 | 21.2 |
| π₀.₅ | 32.3 |
| DT w/o trajectory guidance | 32.3 |
| DT w/o refiner | 47.5 |
| DT（完整） | 54.8 |

**结果含义要点。**

- **轨迹引导是主要增益来源，且集中在接触丰富任务上。** 轨迹引导将平均成功率从 32.3 提升至 47.5，其中 open fridge 从 5.0 提升至 44.0、close counter 从 38.0 提升至 72.0，说明轨迹引导主要惠及需要精确全身接触协调的任务；但在 pick apple 与 open counter 上的轻微下降表明其并非对所有任务都有益。相对 action-only 基线的 22.5 点总增益中，15.2 点来自轨迹引导，7.3 点来自精炼，证明两个组件互补。

- **世界模型精炼在强基线上仍能纠正残余误差。** 精炼将平均成功率从 47.5 进一步提升至 54.8，且改善了全部 6 个子任务；即使在初始策略已较强的 close counter 上仍从 72.0 提升至 80.0，说明精炼在执行前有效纠正了残余的计划—执行偏差。

- **世界模型架构选择有据可依。** 所有学习模型均大幅优于 Analytical FK（0.241 xyz ADE、0.345 xyz FDE、27.0 Angular ADE、0.057 Geodesic ADE），后者无法捕捉接触与控制器误差等超出名义运动学的执行偏差。GRU 在整体轨迹预测精度上最优（0.028 xyz ADE、0.035 xyz FDE、6.2 Angular ADE、0.014 Geodesic ADE），因此被 DT 采用；Diffusion 在 Geodesic ADE 上与 GRU 持平（均为 0.014）但位置与角度误差更大。

- **计算开销可控，真实世界增益显著。** 完整 DT 框架引入 49.04M 额外参数（1.40%）与 11.75 ms 每重规划步延迟，其中轨迹头参数开销可忽略（0.017M、3.65 ms），世界模型为 3.5B 参数 VLA 的 1.40%。真实世界中，轨迹引导将平均成功率从 63.3 提升至 81.7，精炼进一步至 90.0；其中 fruit pick-and-place 从 45.0 提升至 80.0、drawer opening 从 60.0 提升至 90.0，而轨迹引导在 drawer closing 上已达到 100.0。

## 边界与局限

论文未明确提及训练数据量、训练配置细节（学习率、批次大小、轮数）与推理频率。作者承认未来预测 VLA 被排除在定量比较之外，因其固定基座形态与 MS-HAB 不兼容，仅做了定性比较，这意味着与最先进的多模态 VLA 的对比可能不够全面。轨迹引导在 pick apple 和 open counter 上有轻微下降，表明该机制并非对所有任务类型都无代价——对于基座运动需求较低或接触协调要求不高的任务，轨迹引导可能引入不必要的约束。世界模型在仿真与真实平台上的泛化能力未做跨平台验证，其训练数据依赖特定机器人的交互数据，迁移到新形态时可能需要重新采集。此外，测试时搜索的候选扰动参数（σ=0.05, ρ=0.9, N=30）是否对任务类型敏感未做系统分析。

## 工程启示

复现时首先核对轨迹坐标系的锚定方式：块局部坐标系 B_t 锚定在当前基座位姿并固定在整个预测范围内，这是轨迹表示正确性的关键，若误用全局坐标系将导致基座移动时轨迹坐标漂移。其次，组因果注意力掩码的实现必须严格保证动作令牌不能影响轨迹令牌，否则轨迹引导的因果方向会被破坏，消融实验显示这会导致 15.2 个百分点的性能损失。世界模型训练数据的构造中，一步时间偏移（目标路点对应执行动作 a_{t+h} 后观测到的位姿）是容易出错的环节，需确保动作与观测轨迹的时间对齐。测试时搜索的 AR(1) 扰动参数（σ=0.05, ρ=0.9）对结果敏感，建议在目标任务上先做小规模网格搜索。世界模型作为即插即用模块，可先附加到现有轨迹引导策略上验证收益，再决定是否投入训练成本。计算开销方面，完整 DT 仅增加 11.75 ms 延迟，在 RTX 4090 上可满足实时性要求，但需注意世界模型的 49M 参数在显存受限设备上的部署成本。

## 参考
- https://arxiv.org/abs/2608.01381

## Overview

DreamTrajectory is an end-to-end trajectory-guided action generation framework for mobile manipulation tasks, proposed by the author team. Its core contribution lies in jointly predicting intent-level end-effector trajectories and whole-body action chunks within a single action expert, and introducing a lightweight recurrent world model to perform search-predict-score refinement on candidate actions at test time, thereby simultaneously mitigating two major issues: imprecise search in large action spaces and error accumulation during open-loop execution.

## What It Changes

The fundamental difference between mobile manipulation and fixed-base manipulation is that the coordinated motion of the base and robotic arm occurs under continuously changing viewpoints and contact conditions, resulting in a significantly higher-dimensional action space. Existing VLA policies directly map observations to whole-body action chunks, which implicitly assumes that the network can precisely search for base-arm coordinated solutions from a high-dimensional action space without explicit task-space motion planning. The fragility of this assumption in practice manifests at two levels: first, the predicted action chunks may be spatially incoherent, leading to uncoordinated base and arm movements; second, during open-loop execution, control errors and unmodeled contacts (such as reaction forces when pushing or pulling drawers) accumulate into systematic deviations between planned and actual motion.

What DreamTrajectory truly changes is the choice and utilization of the "intermediate representation." It does not abandon end-to-end learning but instead inserts a physically meaningful intermediate variable—the end-effector trajectory—into the action generation pathway. The deeper motivation for this choice is that the end-effector trajectory is a compact description in task space, with far lower dimensionality than whole-body actions, and it directly corresponds to task objectives (e.g., grasping, pushing, pulling). More importantly, it changes the causal structure of action generation: actions are no longer a direct function of observations but are generated conditioned on trajectories, which forces the base and arm motions to coordinate around a unified intent-level plan. Meanwhile, the introduction of the world model transforms "post-execution verification" from open-loop to closed-loop, representing a substantive correction to the "generate-and-execute" paradigm of VLA policies.

## Method Breakdown

### Trajectory-Guided Action Generation
- **Joint Prediction**: A single action expert simultaneously outputs future end-effector trajectories τ_{t:t+H-1} and whole-body action chunks a_{t:t+H-1}, sharing the same horizon H.
- **Trajectory Representation**: Each waypoint is a 7D pose τ_{t+h} = [p_{t+h}^{B_t}, q_{t+h}^{B_t}] ∈ ℝ⁷, where the position p ∈ ℝ³ and quaternion q ∈ ℝ⁴ are both expressed in the chunk-local coordinate frame B_t, anchored at the current base pose and fixed throughout the prediction horizon. This design avoids trajectory coordinate drift caused by base movement in a global coordinate frame.
- **Conditional Flow Matching**: Trajectories and actions are independently sampled with Gaussian noise ε_τ, ε_a ~ 𝒩(0, I), sharing flow time σ ~ 𝒰(0, 1), with interpolated variables τ^σ = σε_τ + (1-σ)τ and a^σ = σε_a + (1-σ)a. The training objective is the joint flow matching loss ℒ_VLA = 𝔼[λ_τ‖v_τ - u_τ‖₂² + λ_a‖v_a - u_a‖₂²], where u_τ = ε_τ - τ and u_a = ε_a - a.
- **Group Causal Attention Mask**: Trajectory tokens attend to multimodal prefixes and previous trajectory tokens; action tokens additionally attend to the full trajectory stream and previous action tokens. This mask ensures trajectory information flows unidirectionally into action generation, preventing action information from leaking back into trajectory generation, thereby maintaining the causal direction of "trajectory-guided actions."

### Test-Time Search-Predict-Score Refinement
- **Candidate Perturbation**: The original action chunk â is retained, and N-1 perturbed chunks ε_i are independently sampled, with each action dimension following an independent AR(1) Gaussian process, marginal standard deviation σ=0.05, lag-one correlation ρ=0.9, N=30.
- **World Model Prediction**: A lightweight recurrent world model W_φ(o_t, s_t, a_{t:t+H-1}) predicts the trajectory τ̃(a) ∈ ℝ^{H×7} that a candidate action chunk would induce. This model is learned from interaction data rather than derived analytically, because deviations between commanded and realized motion arise from contacts, self-collisions, and low-level tracking errors.
- **Scoring and Selection**: All candidates are evaluated in parallel, and the candidate maximizing [λS_traj(a) + (1-λ)ηS_smooth(a)] is selected, where λ=0.5 and η=10⁻³. S_traj measures the consistency between the predicted trajectory and the VLA-generated trajectory, while S_smooth penalizes action jitter.

### Two-Stage Training
- **Stage One**: The VLA backbone is initialized with π₀.₅ pretrained weights and fine-tuned on expert demonstrations.
- **Stage Two**: A trajectory world model is trained on an additional robot-environment interaction dataset containing both successful and failed trials. Dense training samples are constructed using a sliding window, with action and trajectory dimensions independently standardized using training set statistics. During training data construction, the recorded planar base velocity channels are integrated, and recorded end-effector poses are transformed from the instantaneous robot base frame to a chunk-local frame anchored at the time-t base pose, using a one-step temporal offset so that target waypoints correspond to poses observed after executing action a_{t+h}.

## Key Innovations

1. **Causal Guidance via Trajectory as Explicit Intermediate Representation**: Unlike prior work treating trajectories as implicit latent variables or auxiliary prediction heads, DreamTrajectory enforces unidirectional trajectory-guided action generation at the architectural level through a group causal attention mask. This design decouples and recouples "intent-level planning" and "whole-body execution" within a single network, preserving the differentiability of end-to-end learning while providing task-space constraints for action generation. Its novelty lies in encoding causal direction as an inductive bias into the attention mechanism, rather than relying on loss weights or post-processing.

2. **Action-Conditioned Trajectory World Model**: Existing VLA work either executes entirely open-loop or relies on analytical kinematic models for closed-loop correction. DreamTrajectory learns a mapping from action chunks to actual induced trajectories, and this mapping is learned from interaction data including failed trials. This enables implicit modeling of contacts, self-collisions, and low-level tracking errors that are difficult to capture with analytical models. The world model serves as a plug-and-play module that can be attached to any trajectory-guided policy without retraining the VLA, offering significant engineering value in practical deployment.

3. **Test-Time Search-Predict-Score Paradigm**: This transforms the generation problem into a closed-loop "generate-verify-select" process. Structured perturbation via AR(1) Gaussian processes in action space (rather than undifferentiated noise) preserves temporal correlations in actions; parallel scoring of 30 candidates via the world model keeps computational overhead to just 11.75 ms additional latency on a single RTX 4090. This paradigm shifts open-loop execution error correction from "predicting more accurately" to "selecting better," representing a fundamental change in policy optimization philosophy.

## Experiments and Results

**Comparison Setup.** We evaluate DreamTrajectory (DT) at both simulation and real-world levels. Simulation uses the set_table suite from the ManiSkill-HAB (MS-HAB) benchmark with a Fetch mobile manipulation robot, covering 6 subtasks (pick apple, pick bowl, open fridge, close fridge, open counter, close counter), with 100 episodes evaluated per method per task, totaling 600 episodes/method. Baselines include ACT, Diffusion Policy, RDT-1B, GR00T N1, and π₀.₅. Ablation variants include: DT w/o trajectory guidance (direct whole-body action prediction, equivalent to the π₀.₅ baseline), DT w/o refiner (retains trajectory guidance but directly executes the initial action chunk), and full DT (trajectory world model refinement over 30 candidates at each replanning step). Real-world evaluation uses the ARX LIFT mobile manipulation robot across 3 tasks (fruit pick-and-place, drawer opening, drawer closing), with 20 episodes per method per task. World model architecture ablations compare Analytical FK (open-loop), Diffusion, One-shot Transformer, Cross Attention, and GRU (adopted by DT) on 4,096 trajectories, with metrics including xyz ADE (m), xyz FDE (m), Angular ADE (°), and Geodesic ADE. Computational efficiency is measured on a single RTX 4090 with BF16 precision.

**Key Results (MS-HAB Simulation Average Success Rate, %).**

| Method | Avg. |
|--------|------|
| ACT | 28.0 |
| Diffusion Policy | 27.7 |
| RDT-1B | 8.7 |
| GR00T N1 | 21.2 |
| π₀.₅ | 32.3 |
| DT w/o trajectory guidance | 32.3 |
| DT w/o refiner | 47.5 |
| DT (full) | 54.8 |

**Key Implications of Results.**

- **Trajectory guidance is the primary source of gains, concentrated on contact-rich tasks.** Trajectory guidance improves average success from 32.3 to 47.5, with open fridge rising from 5.0 to 44.0 and close counter from 38.0 to 72.0, indicating that trajectory guidance primarily benefits tasks requiring precise whole-body contact coordination; however, slight decreases on pick apple and open counter suggest it is not universally beneficial. Of the 22.5-point total gain over the action-only baseline, 15.2 points come from trajectory guidance and 7.3 from refinement, demonstrating the complementarity of the two components.

- **World model refinement corrects residual errors even on strong baselines.** Refinement further improves average success from 47.5 to 54.8, with improvements across all 6 subtasks; even on close counter, where the initial policy is already strong, it improves from 72.0 to 80.0, indicating that refinement effectively corrects residual plan-execution deviations before execution.

- **World model architecture choice is well-justified.** All learned models substantially outperform Analytical FK (0.241 xyz ADE, 0.345 xyz FDE, 27.0 Angular ADE, 0.057 Geodesic ADE), which cannot capture execution deviations beyond nominal kinematics such as contacts and controller errors. GRU achieves the best overall trajectory prediction accuracy (0.028 xyz ADE, 0.035 xyz FDE, 6.2 Angular ADE, 0.014 Geodesic ADE) and is therefore adopted by DT; Diffusion matches GRU on Geodesic ADE (both 0.014) but exhibits larger position and angular errors.

- **Computational overhead is manageable, with significant real-world gains.** The full DT framework introduces 49.04M additional parameters (1.40%) and 11.75 ms per replanning step, with the trajectory head's parameter overhead negligible (0.017M, 3.65 ms), and the world model accounting for 1.40% of the 3.5B-parameter VLA. In the real world, trajectory guidance improves average success from 63.3 to 81.7, with refinement further increasing it to 90.0; fruit pick-and-place rises from 45.0 to 80.0 and drawer opening from 60.0 to 90.0, while trajectory guidance already achieves 100.0 on drawer closing.

## Boundaries and Limitations

The paper does not explicitly mention training data volume, training configuration details (learning rate, batch size, epochs), or inference frequency. The authors acknowledge that future-predicting VLAs are excluded from quantitative comparison due to their fixed-base morphology being incompatible with MS-HAB, with only qualitative comparison performed, meaning the comparison against state-of-the-art multimodal VLAs may not be fully comprehensive. Trajectory guidance shows slight decreases on pick apple and open counter, indicating that the mechanism is not cost-free for all task types—for tasks with low base-motion requirements or low contact-coordination demands, trajectory guidance may introduce unnecessary constraints. The world model's generalization across simulation and real-world platforms has not been validated cross-platform, and its training data depends on robot-specific interaction data, potentially requiring re-collection when transferring to new morphologies. Additionally, whether the test-time search candidate perturbation parameters (σ=0.05, ρ=0.9, N=30) are sensitive to task type has not been systematically analyzed.

## Engineering Insights

When reproducing, first verify the anchoring of the trajectory coordinate frame: the chunk-local coordinate frame B_t is anchored at the current base pose and fixed throughout the prediction horizon—this is critical for trajectory representation correctness, and misusing a global coordinate frame will cause trajectory coordinate drift during base movement. Second, the implementation of the group causal attention mask must strictly ensure that action tokens cannot influence trajectory tokens; otherwise, the causal direction of trajectory guidance will be broken, and ablation experiments show this leads to a 15.2-percentage-point performance loss. In world model training data construction, the one-step temporal offset (target waypoints corresponding to poses observed after executing action a_{t+h}) is an error-prone step, and temporal alignment between actions and observed trajectories must be ensured. The AR(1) perturbation parameters for test-time search (σ=0.05, ρ=0.9) are sensitive to results, so a small-scale grid search on the target task is recommended. The world model, as a plug-and-play module, can first be attached to an existing trajectory-guided policy to validate benefits before committing to training costs. Regarding computational overhead, the full DT adds only 11.75 ms latency, meeting real-time requirements on an RTX 4090, but the deployment cost of the world model's 49M parameters on memory-constrained devices should be noted.

## 개요

DreamTrajectory는 저자 팀이 제안한, 이동 조작 작업을 위한 엔드투엔드 궤적 유도 동작 생성 프레임워크입니다. 핵심 기여는 단일 동작 전문가에서 의도 수준의 엔드이펙터 궤적과 전신 동작 블록을 공동으로 예측하고, 경량 순환 세계 모델을 도입하여 테스트 시 후보 동작에 대한 탐색-예측-점수화 정제를 수행함으로써, 큰 동작 공간 탐색의 부정확성과 개루프 실행 오류 누적이라는 두 가지 문제를 동시에 완화한다는 점입니다.

## 무엇을 바꾸었는가

이동 조작과 고정 베이스 조작의 본질적 차이는 베이스와 로봇 팔의 협조 운동이 연속적으로 변화하는 시점과 접촉 조건에서 발생하며, 동작 공간의 차원이 훨씬 높다는 점입니다. 기존 VLA 정책은 관측을 전신 동작 블록에 직접 매핑하는데, 이는 네트워크가 명시적 작업 공간 운동 계획 없이 고차원 동작 공간에서 베이스-팔 협조 해를 정밀하게 탐색할 수 있다는 강한 가정을 내포합니다. 이 가정의 취약성은 실제로 두 가지 측면에서 드러납니다. 첫째, 예측된 동작 블록이 공간적으로 불연속적일 수 있어 베이스와 팔의 운동이 부자연스러워집니다. 둘째, 개루프 실행 시 제어 오류와 모델링되지 않은 접촉(예: 서랍을 밀고 당길 때의 반작용)이 계획된 운동과 실제 운동 사이의 체계적 편차로 누적됩니다.

DreamTrajectory가 실제로 바꾼 것은 '중간 표현'의 선택과 활용 방식입니다. 엔드투엔드 학습을 버리지 않으면서, 동작 생성 경로에 물리적으로 의미 있는 중간 변수인 엔드이펙터 궤적을 삽입했습니다. 이 선택의 심층적 동기는 엔드이펙터 궤적이 작업 공간의 간결한 설명으로, 전신 동작보다 차원이 훨씬 낮고 작업 목표(예: 파지, 밀고 당기기)에 직접 대응한다는 점입니다. 더 중요하게는, 이는 동작 생성의 인과 구조를 바꿉니다. 동작은 더 이상 관측의 직접 함수가 아니라 궤적을 조건으로 하는 생성 결과가 되며, 이는 베이스와 팔의 운동이 통일된 의도 수준 계획을 중심으로 협조하도록 강제합니다. 동시에 세계 모델의 도입은 '실행 후 검증'을 개루프에서 폐루프로 바꾸었으며, 이는 VLA 정책의 '생성 즉 실행' 패러다임에 대한 실질적 수정입니다.

## 방법 분해

### 궤적 유도 동작 생성
- **공동 예측**: 단일 동작 전문가가 미래 엔드이펙터 궤적 τ_{t:t+H-1}과 전신 동작 블록 a_{t:t+H-1}을 동시에 출력하며, 수평선 H를 공유합니다.
- **궤적 표현**: 각 웨이포인트는 7D 포즈 τ_{t+h} = [p_{t+h}^{B_t}, q_{t+h}^{B_t}] ∈ ℝ⁷이며, 위치 p ∈ ℝ³와 쿼터니언 q ∈ ℝ⁴ 모두 블록 로컬 좌표계 B_t에서 표현되고, 현재 베이스 포즈에 고정되어 전체 예측 범위 동안 유지됩니다. 이 설계는 전역 좌표계에서 베이스 이동으로 인한 궤적 좌표 드리프트를 피합니다.
- **조건부 흐름 매칭**: 궤적과 동작은 독립적으로 가우시안 노이즈 ε_τ, ε_a ~ 𝒩(0, I)를 샘플링하고, 공유 흐름 시간 σ ~ 𝒰(0, 1)을 사용하며, 보간 변수는 τ^σ = σε_τ + (1-σ)τ 및 a^σ = σε_a + (1-σ)a입니다. 훈련 목표는 결합 흐름 매칭 손실 ℒ_VLA = 𝔼[λ_τ‖v_τ - u_τ‖₂² + λ_a‖v_a - u_a‖₂²]이며, 여기서 u_τ = ε_τ - τ, u_a = ε_a - a입니다.
- **그룹 인과 주의 마스크**: 궤적 토큰은 다중 모드 프리픽스와 이전 궤적 토큰에 주의를 기울입니다. 동작 토큰은 추가로 전체 궤적 흐름과 이전 동작 토큰에 주의를 기울입니다. 이 마스크는 궤적 정보가 동작 생성으로 단방향으로 흐르도록 보장하고, 동작 정보가 궤적 생성으로 누출되는 것을 방지하여 '궤적 유도 동작'의 인과 방향을 유지합니다.

### 테스트 시 탐색-예측-점수화 정제
- **후보 섭동**: 원래 동작 블록 â를 유지하고, N-1개의 섭동 블록 ε_i를 독립적으로 샘플링합니다. 각 동작 차원은 독립적인 AR(1) 가우시안 프로세스를 따르며, 한계 표준 편차 σ=0.05, 지연 1 상관 ρ=0.9, N=30입니다.
- **세계 모델 예측**: 경량 순환 세계 모델 W_φ(o_t, s_t, a_{t:t+H-1})이 후보 동작 블록이 유도할 궤적 τ̃(a) ∈ ℝ^{H×7}을 예측합니다. 이 모델은 해석적 유도가 아닌 상호작용 데이터에서 학습됩니다. 명령과 구현 운동 사이의 편차가 접촉, 자체 충돌 및 저수준 추적 오류에서 비롯되기 때문입니다.
- **점수화 및 선택**: 모든 후보를 병렬로 평가하고, [λS_traj(a) + (1-λ)ηS_smooth(a)]를 최대화하는 후보를 선택합니다. 여기서 λ=0.5, η=10⁻³입니다. S_traj는 예측 궤적과 VLA 생성 궤적의 일치도를 측정하고, S_smooth는 동작 떨림을 페널티합니다.

### 2단계 훈련
- **1단계**: π_0.5 사전 훈련 가중치로 VLA 백본을 초기화하고 전문가 시연에서 미세 조정합니다.
- **2단계**: 성공 및 실패 시험을 포함한 추가 로봇-환경 상호작용 데이터셋으로 궤적 세계 모델을 훈련합니다. 슬라이딩 윈도우를 사용하여 밀집 훈련 샘플을 구성하고, 동작 및 궤적 차원은 훈련 세트 통계로 독립적으로 표준화합니다. 훈련 데이터 구성에서 기록된 평면 베이스 속도 채널을 적분하고, 기록된 엔드이펙터 포즈를 순간 로봇 베이스 좌표계에서 시간 t 베이스 포즈를 기준으로 하는 블록 로컬 좌표계로 변환하며, 1단계 시간 오프셋을 사용하여 목표 웨이포인트가 실행 동작 a_{t+h} 후 관측된 포즈에 대응하도록 합니다.

## 핵심 혁신

1. **명시적 중간 표현으로서 궤적의 인과 유도**: 이전 연구가 궤적을 암시적 잠재 변수나 보조 예측 헤드로 취급한 것과 달리, DreamTrajectory는 그룹 인과 주의 마스크를 통해 아키텍처 수준에서 궤적 정보가 동작 생성을 단방향으로 유도하도록 강제합니다. 이 설계는 '의도 수준 계획'과 '전신 실행'을 단일 네트워크에서 분리하면서도 결합하여, 엔드투엔드 학습의 미분 가능성을 유지하면서 동작 생성에 작업 공간 제약을 제공합니다. 그 참신함은 인과 방향을 손실 가중치나 후처리에 의존하지 않고 주의 메커니즘에 귀납적 편향으로 작성한 점입니다.

2. **동작 조건 궤적 세계 모델**: 기존 VLA 연구는 완전히 개루프로 실행하거나 해석적 운동학 모델에 의존하여 폐루프 수정을 수행합니다. DreamTrajectory는 동작 블록에서 실제 유도 궤적으로의 매핑을 학습하며, 이 매핑은 실패 시험을 포함한 상호작용 데이터에서 학습됩니다. 이를 통해 해석적 모델이 설명하기 어려운 접촉, 자체 충돌 및 저수준 추적 오류와 같은 요소를 암시적으로 모델링할 수 있습니다. 세계 모델은 플러그 앤 플레이 모듈로, VLA를 재훈련하지 않고도 임의의 궤적 유도 정책에 부착할 수 있어 실제 배포에서 상당한 엔지니어링 가치가 있습니다.

3. **테스트 시 탐색-예측-점수화 패러다임**: 생성 문제를 '생성-검증-선택'의 폐루프 프로세스로 변환합니다. AR(1) 가우시안 프로세스를 통해 동작 공간에서 구조화된 섭동(무차별 노이즈가 아닌)을 수행하여 동작의 시간 상관성을 유지하고, 세계 모델로 30개 후보를 병렬 점수화하여 계산 비용을 단일 RTX 4090에서 11.75ms 지연 증가로 제한합니다. 이 패러다임은 실시간성을 유지하면서 개루프 실행 오류 수정을 '더 정확한 예측'에서 '더 나은 선택'으로 전환하여, 정책 최적화 접근 방식의 변화를 나타냅니다.

## 실험 및 결과

**비교 설정.** 우리는 시뮬레이션과 실제 세계 두 수준에서 DreamTrajectory(DT)를 평가합니다. 시뮬레이션은 ManiSkill-HAB(MS-HAB) 벤치마크의 set_table 스위트를 사용하며, Fetch 이동 조작 로봇을 사용하여 6개의 하위 작업(pick apple, pick bowl, open fridge, close fridge, open counter, close counter)을 다룹니다. 각 방법은 작업당 100개 에피소드, 총 600 에피소드/방법으로 평가됩니다. 기준선에는 ACT, Diffusion Policy, RDT-1B, GR00T N1 및 π₀.₅가 포함됩니다. 절제 변형에는 DT w/o trajectory guidance(전신 동작 직접 예측, π₀.₅ 기준선과 동일), DT w/o refiner(궤적 유도 유지하지만 초기 동작 블록 직접 실행), 전체 DT(각 재계획 단계에서 30개 후보에 대해 궤적 세계 모델 정제)가 포함됩니다. 실제 세계는 ARX LIFT 이동 조작 로봇을 사용하여 3개 작업(과일 파지 배치, 서랍 열기, 서랍 닫기)을 다루며, 각 방법은 작업당 20개 에피소드입니다. 세계 모델 아키텍처 절제는 4,096개 궤적에서 Analytical FK(개루프), Diffusion, One-shot Transformer, Cross Attention 및 GRU(DT 채택)를 비교하며, 지표는 xyz ADE(m), xyz FDE(m), Angular ADE(°) 및 Geodesic ADE를 포함합니다. 계산 효율성은 단일 RTX 4090, BF16 정밀도에서 측정됩니다.

**핵심 결과(MS-HAB 시뮬레이션 평균 성공률, %).**

| 방법 | 평균 |
|------|------|
| ACT | 28.0 |
| Diffusion Policy | 27.7 |
| RDT-1B | 8.7 |
| GR00T N1 | 21.2 |
| π₀.₅ | 32.3 |
| DT w/o trajectory guidance | 32.3 |
| DT w/o refiner | 47.5 |
| DT(전체) | 54.8 |

**결과 의미 요점.**

- **궤적 유도는 주요 이득 원천이며 접촉이 많은 작업에 집중됩니다.** 궤적 유도는 평균 성공률을 32.3에서 47.5로 향상시켰으며, open fridge는 5.0에서 44.0으로, close counter는 38.0에서 72.0으로 향상되어 궤적 유도가 주로 정밀한 전신 접촉 협조가 필요한 작업에 혜택을 준다는 것을 보여줍니다. 그러나 pick apple과 open counter에서의 약간의 하락은 모든 작업 유형에 유익한 것은 아님을 시사합니다. 동작 전용 기준선 대비 22.5포인트의 총 이득 중 15.2포인트는 궤적 유도에서, 7.3포인트는 정제에서 발생하여 두 구성 요소가 상호 보완적임을 증명합니다.

- **세계 모델 정제는 강한 기준선에서도 잔여 오류를 수정할 수 있습니다.** 정제는 평균 성공률을 47.5에서 54.8로 추가 향상시키고 6개 하위 작업 모두를 개선합니다. 초기 정책이 이미 강한 close counter에서도 72.0에서 80.0으로 향상되어, 정제가 실행 전에 잔여 계획-실행 편차를 효과적으로 수정함을 보여줍니다.

- **세계 모델 아키텍처 선택에는 근거가 있습니다.** 모든 학습 모델은 Analytical FK(0.241 xyz ADE, 0.345 xyz FDE, 27.0 Angular ADE, 0.057 Geodesic ADE)를 크게 능가하며, 후자는 명목 운동학을 넘어서는 접촉 및 제어기 오류와 같은 실행 편차를 포착할 수 없습니다. GRU는 전체 궤적 예측 정확도에서 최적(0.028 xyz ADE, 0.035 xyz FDE, 6.2 Angular ADE, 0.014 Geodesic ADE)이므로 DT에서 채택되었습니다. Diffusion은 Geodesic ADE에서 GRU와 동률(둘 다 0.014)이지만 위치 및 각도 오류가 더 큽니다.

- **계산 비용은 통제 가능하며 실제 세계 이득이 상당합니다.** 전체 DT 프레임워크는 49.04M 추가 파라미터(1.40%)와 재계획 단계당 11.75ms 지연을 도입하며, 궤적 헤드 파라미터 비용은 무시할 수 있습니다(0.017M, 3.65ms). 세계 모델은 3.5B 파라미터 VLA의 1.40%입니다. 실제 세계에서 궤적 유도는 평균 성공률을 63.3에서 81.7로 향상시키고, 정제는 90.0으로 추가 향상시킵니다. fruit pick-and-place는 45.0에서 80.0으로, drawer opening은 60.0에서 90.0으로 향상되었으며, 궤적 유도는 drawer closing에서 이미 100.0에 도달했습니다.

## 경계 및 한계

논문은 훈련 데이터 양, 훈련 구성 세부 사항(학습률, 배치 크기, 에폭 수) 및 추론 빈도를 명시적으로 언급하지 않습니다. 저자는 미래 예측 VLA가 정량적 비교에서 제외되었음을 인정하는데, 이는 고정 베이스 형태가 MS-HAB와 호환되지 않아 정성적 비교만 수행했기 때문이며, 이는 최첨단 다중 모드 VLA와의 비교가 충분히 포괄적이지 않을 수 있음을 의미합니다. 궤적 유도는 pick apple과 open counter에서 약간의 하락을 보여, 이 메커니즘이 모든 작업 유형에 무비용이 아님을 시사합니다. 베이스 운동 요구가 낮거나 접촉 협조 요구가 높지 않은 작업의 경우 궤적 유도가 불필요한 제약을 도입할 수 있습니다. 세계 모델의 시뮬레이션 및 실제 플랫폼 간 일반화 능력은 교차 플랫폼 검증되지 않았으며, 훈련 데이터는 특정 로봇의 상호작용 데이터에 의존하므로 새 형태로 전이할 때 재수집이 필요할 수 있습니다. 또한 테스트 시 탐색의 후보 섭동 파라미터(σ=0.05, ρ=0.9, N=30)가 작업 유형에 민감한지에 대한 체계적 분석은 수행되지 않았습니다.

## 엔지니어링 시사점

재현 시 먼저 궤적 좌표계의 고정 방식을 확인해야 합니다. 블록 로컬 좌표계 B_t는 현재 베이스 포즈에 고정되고 전체 예측 범위 동안 유지되며, 이는 궤적 표현의 정확성에 핵심입니다. 전역 좌표계를 잘못 사용하면 베이스 이동 시 궤적 좌표 드리프트가 발생합니다. 둘째, 그룹 인과 주의 마스크 구현은 동작 토큰이 궤적 토큰에 영향을 미칠 수 없음을 엄격히 보장해야 합니다. 그렇지 않으면 궤적 유도의 인과 방향이 파괴되며, 절제 실험에 따르면 이는 15.2포인트의 성능 손실을 초래합니다. 세계 모델 훈련 데이터 구성에서 1단계 시간 오프셋(목표 웨이포인트가 실행 동작 a_{t+h} 후 관측된 포즈에 대응)은 오류가 발생하기 쉬운 부분이므로 동작과 관측 궤적의 시간 정렬을 보장해야 합니다. 테스트 시 탐색의 AR(1) 섭동 파라미터(σ=0.05, ρ=0.9)는 결과에 민감하므로, 목표 작업에서 먼저 소규모 그리드 탐색을 수행하는 것이 좋습니다. 세계 모델은 플러그 앤 플레이 모듈이므로, 먼저 기존 궤적 유도 정책에 부착하여 이득을 검증한 후 훈련 비용 투자 여부를 결정할 수 있습니다. 계산 비용 측면에서 전체 DT는 11.75ms 지연만 추가하므로 RTX 4090에서 실시간 요구 사항을 충족할 수 있지만, 세계 모델의 49M 파라미터가 메모리 제한 장치에서의 배포 비용에 미치는 영향을 고려해야 합니다.
