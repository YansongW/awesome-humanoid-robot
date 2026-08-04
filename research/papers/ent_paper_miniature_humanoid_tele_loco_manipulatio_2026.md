---
$id: ent_paper_miniature_humanoid_tele_loco_manipulatio_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning
  zh: Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning
  ko: Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Reinforcement Learning
summary:
  en: Full-sized humanoid robot capabilities have grown exponentially in recent years, aiming towards general-purpose deployment
    in human environments. A popular control method used by manufacturers utilizes Virtual Reality for upper-body teleoperation
    and Reinforcement Learning for lower-body balance and locomotion control. As a result, a single remote operator can see,
    manipulate, and navigate about.
  zh: 本文提出了一套面向微型人形机器人 ROBOTIS OP3 的柔顺全身遥临场控制栈，将 VR 上半身遥操作与 RL 下半身行走/平衡控制解耦，通过 PD 阻抗控制实现双臂操纵与双腿行走的协同。系统在真实机器人上完成了行走、拾取与搬运任务，验证了低成本微型平台执行
    loco-manipulation 的可行性，并公开了完整的软硬件实现细节。
  ko: Full-sized humanoid robot capabilities have grown exponentially in recent years, aiming towards general-purpose deployment
    in human environments. A popular control method used by manufacturers utilizes Virtual Reality for upper-body teleoperation
    and Reinforcement Learning for lower-body balance and locomotion control. As a result, a single remote operator can see,
    manipulate, and navigate about.
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
- miniature
- humanoid
- tele
- loco
- manipulatio
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
  title: arXiv:2607.20399 Towards Miniature Humanoid Tele-Loco-Manipulation Using Virtual Reality and Rein
  url: https://arxiv.org/abs/2607.20399
  date: '2026-07-22'
  accessed_at: '2026-08-05'
---



## 概述

本文提出了一套面向微型人形机器人 ROBOTIS OP3 的柔顺全身遥临场控制栈，将 VR 上半身遥操作与 RL 下半身行走/平衡控制解耦，通过 PD 阻抗控制实现双臂操纵与双腿行走的协同。系统在真实机器人上完成了行走、拾取与搬运任务，验证了低成本微型平台执行 loco-manipulation 的可行性，并公开了完整的软硬件实现细节。

## 它改变了什么

全尺寸人形机器人的 VR+RL 控制栈（如 HOMIE、Mobile-TeleVision）虽然功能强大，但硬件成本高、操作门槛大，导致研究社区难以复现和积累数据。微型人形机器人（如 OP3）价格亲民、易于获取，却因自由度少、传感器简陋、执行器非线性强，长期缺乏一套完整的全身控制方案——现有工作要么只做上半身遥操作，要么只做下半身行走，鲜有将两者结合并验证真实搬运任务的。

本文真正改变的是：它证明了在 20 个自由度、无关节力矩传感器、仅靠电流开环扭矩控制的微型平台上，通过"VR 遥操作（上半身）+ RL 策略（下半身）+ 全身 PD 阻抗"的分层架构，可以构建出可用的 loco-manipulation 系统。这为低成本人形机器人研究提供了一个可复现的基线，而非仅仅展示一个昂贵的演示。其意义在于把"全身遥操作"从全尺寸平台的专利变成了微型平台的现实选项。

## 方法拆解

### 系统架构
- **分层控制**：VR 遥操作负责双臂（3 DoF/臂）与颈部（2 DoF），RL 策略负责双腿（6 DoF/腿），两者通过全身 PD 阻抗控制（式 1）在关节层面融合。
- **硬件**：ROBOTIS OP3（20 DoF，DYNAMIXEL XM430-W350-R 舵机），摄像头替换为 VR180 双鱼眼（3840×1080@60Hz），主机为 i9+RTX 4090，VR 为 VIVE Pro 2 + 4 基站。

### 上半身遥操作
- **运动重定向**：多目标 IK 求解器 [28] 跟踪 VR 控制器位置，内置梯形速度曲线约束关节最大速度/加速度；VIVE 扳机作为开关，释放时归零 IK 限制，按下时经 EMA 滤波缓慢恢复。
- **扭矩控制**：自定义 PD 控制器（式 1），200 Hz 运行（受 TTL 限制）；DYNAMIXEL 舵机通过硬件电流控制开环实现扭矩，假设电流-扭矩线性（电机常数由堵转扭矩/电流确定），静态测试台验证线性行为。
- **接触力估计（式 2）**：F = −Kx（x 为虚拟与半透明模型末端执行器间矢量距离），低于阈值时假设误差由机械延迟引起，不依赖完整动力学模型。
- **视频流**：UDP + GStreamer，GPU 加速 H.265 转码，玻璃到玻璃延迟约 100 ms，码率 <4 Mbps；颈部机械延迟通过反向旋转显示球体掩蔽，EMA 滤波平滑。

### 下半身 RL 行走
- **MDP 形式化**：最大化折扣回报 G_t = Σ γᵏR(S_{t+k}, A_{t+k})，最优策略 π* 同时最大化状态条件与状态-动作条件期望回报。
- **观测空间**：5 项（角速度、投影重力、用户命令、关节位置、上一动作），每项叠加前 9 步历史，组成 330×1 向量；关节速度由模型推断，不在观测中。
- **奖励设计**：步态奖励（双支撑/单支撑）、足部朝向惩罚（投影重力 xy 分量）、足部离地奖励、动作平滑度惩罚等，权重见表 III。
- **域随机化**：足部摩擦 (0.5, 0.9)、重力缩放 (0.95, 1.3)、连杆质量 (0.7, 1.3)、身体速度/位置/朝向加性噪声、关节位置/速度缩放；推挤事件每 (10, 15) 秒随机添加身体线速度。
- **执行器辨识**：BAM 方法基于摆锤测试台，参数 armature=0.045、friction loss=0.03、effort limit=3.6，在 Isaac Sim 中验证。

### 触控板映射
- VIVE 2D 触控板映射为差速驱动式速度命令（一个角速度、一个线速度），发送至下半身 RL 策略。

## 关键创新

1. **微型平台全身控制栈的首次完整实现**：此前 VR 遥操作与 RL 行走分别在微型平台上独立验证，本文首次将两者在 OP3 上融合，并完成真实搬运任务，填补了低成本平台 loco-manipulation 研究的空白。
2. **无需关节力矩传感器的柔顺控制**：利用 DYNAMIXEL 舵机电流-扭矩线性关系实现开环扭矩控制，配合自定义 PD 增益（手臂低、腿部高），在无力矩传感器条件下获得柔顺操纵能力，降低了硬件门槛。
3. **基于虚拟误差的接触力估计**：式 2 不依赖机械臂动力学模型，仅用虚拟与半透明模型间的距离误差估计接触力，比 Jacobian 方法更简单实用，适合传感器匮乏的微型平台。

## 实验与结果


## 实验与结果

为验证系统整体性能，作者在 ROBOTIS OP3 微型人形机器人（20 个旋转自由度）上开展了三组实验：遥操作验证（双臂画圆）、运动验证（随机全身速度指令下的双足稳定性）以及遥-运动-操作综合实验（行走、拾取并搬运 3D 打印 PLA 立方体）。遥操作硬件采用 VIVE Pro 2 HMD、VIVE 控制器、4 个 SteamVR Basestation 2.0 与 KAT Walk C2+ VR 跑步机，控制频率为 200 Hz，视频系统为 VR180 双鱼眼 USB 相机（3840 × 1080 水平并排图像，60 Hz，H.265 转码，玻璃到玻璃延迟约 100 ms）。运动策略基于域随机化（足部摩擦 (0.5, 0.9)、重力缩放 (0.95, 1.3)、连杆质量缩放 (0.7, 1.3) 等）与观测噪声注入（角速度 0.2、投影重力 0.1、关节位置 0.05）训练，观测空间为 330 × 1 向量。综合实验中，操作员在 10 mins 内完成十次试验，每次行走约 5 m 并尝试搬运 40 g 立方体。

| 指标 | 数值 |
|------|------|
| 遥操作运动延迟（y 方向） | 220 ms |
| 右手 x 方向位置跟踪 MAE / RMSE | 8.76 / 12.35 |
| 右手 y 方向位置跟踪 MAE / RMSE | 10.58 / 15.07 |
| 右手 z 方向位置跟踪 MAE / RMSE | 8.68 / 11.17 |
| 综合实验成功搬运方块数 | 2 out of 6 |
| 综合实验平均行走速度 | 0.35 m/s |
| 行走速度上限（摘要） | 0.45 m/s |

**结果含义：**

- **遥操作精度受延迟主导**：尽管部分手臂定位误差的 RMSE 或 MAE 超过 15（论文未明确），但大部分瞬时误差可归因于约 220 ms 的运动延迟；上肢能够清晰复现操作员要求的画圆运动，表明遥操作映射在延迟补偿后具备可用精度。
- **运动策略在剧烈指令下保持稳定**：归一化投影重力保持在期望值 -1 附近，表明 RL 策略在随机且剧烈的行走速度指令变化下仍能正确维持稳定的躯干姿态，验证了域随机化训练的有效性。
- **综合任务性能受操作难度与挫败感制约**：系统在 10 mins 内仅成功搬运 2 out of 6 个方块，平均行走速度 0.35 m/s。作者指出性能瓶颈主要来自三方面：RL 策略行走时抬脚高度不足、用户需交叉手臂才能产生足够力量抬起立方体、有线供电连接带来的运动挑战。系统缺乏重力与摩擦补偿项导致需使用较高 PD 增益，进一步降低了柔顺性。

## 边界与局限

- **搬运性能有限**：平均仅搬运 2/6 个立方体，归因于 RL 行走策略抬脚不够高、用户需交叉手臂产生足够握持力、系绳供电阻碍行走。
- **柔顺性与力控制矛盾**：缺少重力/摩擦补偿，需较高 PD 增益，牺牲柔顺性；建议加入补偿项但需准确动态模型。
- **执行器模型粗糙**：需过度域随机化应对 sim2real 差距，可能影响策略在真实环境的上限。
- **未做之事**：未集成 VR treadmill（KAT Walk C2+）、未实现无系绳操作、未使用更困难地形、未加真实夹爪/末端力传感器、未处理腰部自由度缺失（OP3 无腰部 DoF，用户躯干旋转无法映射）。
- **训练细节缺失**：论文未明确训练步数、并行环境数、学习率、网络结构、推理频率等关键复现参数。

## 工程启示

- **复现优先级**：先核对执行器辨识参数（armature=0.045、friction loss=0.03、effort limit=3.6）是否适用于你的舵机型号；DYNAMIXEL 电流-扭矩线性假设是关键前提，务必在静态测试台上验证线性度，否则 PD 控制会失真。
- **最容易踩坑**：① 200 Hz 控制频率受 TTL 通信限制，若改用更高带宽总线需重新调 PD 增益；② 接触力估计（式 2）的阈值 x_threshold 需根据机械延迟实测调整，否则误判接触；③ 视频延迟掩蔽依赖 EMA 滤波参数，需与颈部机械延迟精确匹配，否则操作者会晕眩。
- **下游团队指导**：若目标任务是精细操纵，建议优先加入重力/摩擦补偿以降低 PD 增益、提升柔顺性；若目标是行走鲁棒性，可参考表 I 的域随机化范围，但需注意过度随机化可能降低操纵精度。搬运任务中，真实夹爪或末端力传感器是提升成功率的直接手段。
- **数据价值**：该系统可作为微型人形机器人 loco-manipulation 数据采集平台，但需先解决系绳和抬脚高度问题，否则采集的数据质量受限。

## 参考
- https://arxiv.org/abs/2607.20399

## Overview

This paper presents a compliant whole-body telepresence control stack for the miniature humanoid robot ROBOTIS OP3, decoupling VR upper-body teleoperation from RL lower-body walking/balance control, and achieving coordinated dual-arm manipulation and bipedal locomotion through PD impedance control. The system completes walking, picking, and carrying tasks on a real robot, validating the feasibility of loco-manipulation on a low-cost miniature platform, and releases complete software and hardware implementation details.

## What It Changes

While VR+RL control stacks for full-sized humanoid robots (e.g., HOMIE, Mobile-TeleVision) are powerful, their high hardware costs and steep operational barriers make them difficult for the research community to reproduce and accumulate data. Miniature humanoids (e.g., OP3) are affordable and accessible, but suffer from fewer degrees of freedom, rudimentary sensors, and highly nonlinear actuators, leaving a long-standing gap in a complete whole-body control solution—existing work either focuses solely on upper-body teleoperation or lower-body walking, with few combining both and validating real carrying tasks.

What this paper truly changes is this: it demonstrates that on a miniature platform with 20 DoF, no joint torque sensors, and only open-loop current-based torque control, a usable loco-manipulation system can be built through a hierarchical architecture of "VR teleoperation (upper body) + RL policy (lower body) + whole-body PD impedance." This provides a reproducible baseline for low-cost humanoid research, rather than merely showcasing an expensive demonstration. Its significance lies in turning "whole-body teleoperation" from a privilege of full-sized platforms into a realistic option for miniature ones.

## Method Breakdown

### System Architecture
- **Hierarchical Control**: VR teleoperation handles the arms (3 DoF/arm) and neck (2 DoF), while the RL policy handles the legs (6 DoF/leg), fused at the joint level via whole-body PD impedance control (Eq. 1).
- **Hardware**: ROBOTIS OP3 (20 DoF, DYNAMIXEL XM430-W350-R servos), camera replaced with a VR180 dual-fisheye (3840×1080@60Hz), host machine with i9+RTX 4090, VR setup with VIVE Pro 2 + 4 base stations.

### Upper-Body Teleoperation
- **Motion Retargeting**: A multi-objective IK solver [28] tracks VR controller positions, with built-in trapezoidal velocity profiles constraining joint maximum velocity/acceleration; the VIVE trigger acts as a switch—when released, IK limits reset to zero; when pressed, they slowly recover via EMA filtering.
- **Torque Control**: Custom PD controller (Eq. 1) running at 200 Hz (limited by TTL); DYNAMIXEL servos achieve torque through hardware current control in open loop, assuming current-torque linearity (motor constant determined from stall torque/current), with linear behavior verified on a static test bench.
- **Contact Force Estimation (Eq. 2)**: F = −Kx (x is the vector distance between the virtual and semi-transparent model end-effectors), with errors below a threshold attributed to mechanical delay, without relying on a full dynamics model.
- **Video Streaming**: UDP + GStreamer, GPU-accelerated H.265 transcoding, glass-to-glass latency of approximately 100 ms, bitrate <4 Mbps; neck mechanical delay is masked by counter-rotating a displayed sphere, with EMA filtering for smoothing.

### Lower-Body RL Walking
- **MDP Formulation**: Maximize discounted return G_t = Σ γᵏR(S_{t+k}, A_{t+k}), with the optimal policy π* maximizing both state-conditioned and state-action-conditioned expected returns.
- **Observation Space**: 5 terms (angular velocity, projected gravity, user commands, joint positions, previous actions), each stacked with the previous 9 steps of history, forming a 330×1 vector; joint velocities are inferred by the model and not included in observations.
- **Reward Design**: Gait rewards (double support/single support), foot orientation penalty (xy components of projected gravity), foot lift-off reward, action smoothness penalty, etc., with weights listed in Table III.
- **Domain Randomization**: Foot friction (0.5, 0.9), gravity scaling (0.95, 1.3), link mass (0.7, 1.3), additive noise on body velocity/position/orientation, joint position/velocity scaling; push events randomly add body linear velocity every (10, 15) seconds.
- **Actuator Identification**: BAM method based on a pendulum test bench, with parameters armature=0.045, friction loss=0.03, effort limit=3.6, validated in Isaac Sim.

### Touchpad Mapping
- The VIVE 2D touchpad maps to differential-drive-style velocity commands (one angular velocity, one linear velocity), sent to the lower-body RL policy.

## Key Innovations

1. **First Complete Whole-Body Control Stack on a Miniature Platform**: Previously, VR teleoperation and RL walking were independently validated on miniature platforms; this paper is the first to fuse both on the OP3 and complete real carrying tasks, filling the gap in low-cost platform loco-manipulation research.
2. **Compliant Control Without Joint Torque Sensors**: Leverages the DYNAMIXEL servo current-torque linearity for open-loop torque control, paired with custom PD gains (low for arms, high for legs), achieving compliant manipulation without torque sensors and lowering the hardware barrier.
3. **Virtual-Error-Based Contact Force Estimation**: Eq. 2 does not rely on a manipulator dynamics model, using only the distance error between virtual and semi-transparent models to estimate contact force—simpler and more practical than Jacobian methods, suitable for sensor-deprived miniature platforms.

## Experiments and Results

To validate overall system performance, the authors conducted three sets of experiments on the ROBOTIS OP3 miniature humanoid robot (20 rotary DoF): teleoperation validation (drawing circles with both arms), locomotion validation (bipedal stability under random whole-body velocity commands), and combined tele-locomotion-manipulation experiments (walking, picking up, and carrying a 3D-printed PLA cube). Teleoperation hardware included the VIVE Pro 2 HMD, VIVE controllers, 4 SteamVR Basestation 2.0, and a KAT Walk C2+ VR treadmill, with a control frequency of 200 Hz. The video system used a VR180 dual-fisheye USB camera (3840 × 1080 side-by-side images, 60 Hz, H.265 transcoding, glass-to-glass latency of approximately 100 ms). The locomotion policy was trained with domain randomization (foot friction (0.5, 0.9), gravity scaling (0.95, 1.3), link mass scaling (0.7, 1.3), etc.) and observation noise injection (angular velocity 0.2, projected gravity 0.1, joint position 0.05), with an observation space of 330 × 1. In the combined experiments, the operator completed ten trials within 10 mins, walking approximately 5 m each time and attempting to carry a 40 g cube.

| Metric | Value |
|------|------|
| Teleoperation motion latency (y-direction) | 220 ms |
| Right-hand x-direction position tracking MAE / RMSE | 8.76 / 12.35 |
| Right-hand y-direction position tracking MAE / RMSE | 10.58 / 15.07 |
| Right-hand z-direction position tracking MAE / RMSE | 8.68 / 11.17 |
| Cubes successfully carried in combined experiments | 2 out of 6 |
| Average walking speed in combined experiments | 0.35 m/s |
| Maximum walking speed (abstract) | 0.45 m/s |

**Interpretation of Results:**

- **Teleoperation accuracy is dominated by latency**: Although some arm positioning errors have RMSE or MAE exceeding 15 (not explicitly stated in the paper), most instantaneous errors can be attributed to the approximately 220 ms motion latency; the upper limbs clearly reproduce the operator's requested circular motions, indicating that the teleoperation mapping achieves usable accuracy after latency compensation.
- **Locomotion policy remains stable under aggressive commands**: The normalized projected gravity stays near the desired value of -1, indicating that the RL policy correctly maintains stable torso posture under random and aggressive walking speed command changes, validating the effectiveness of domain-randomized training.
- **Combined task performance is constrained by operational difficulty and frustration**: The system successfully carried only 2 out of 6 cubes within 10 mins, with an average walking speed of 0.35 m/s. The authors attribute the performance bottleneck to three factors: insufficient foot lift height in the RL walking policy, the need for users to cross their arms to generate enough force to lift the cube, and movement challenges posed by the tethered power connection. The lack of gravity and friction compensation terms necessitates higher PD gains, further reducing compliance.

## Boundaries and Limitations

- **Limited carrying performance**: Only 2/6 cubes carried on average, attributed to insufficient foot lift in the RL walking policy, the need for users to cross arms to generate sufficient grip force, and tether power supply hindering walking.
- **Conflict between compliance and force control**: The absence of gravity/friction compensation requires higher PD gains, sacrificing compliance; adding compensation terms is suggested but requires an accurate dynamics model.
- **Coarse actuator model**: Excessive domain randomization is needed to bridge the sim2real gap, potentially limiting the policy's upper bound in real environments.
- **What was not done**: No integration of the VR treadmill (KAT Walk C2+), no untethered operation, no more challenging terrain, no real grippers/end-effector force sensors, and no handling of the missing waist DoF (OP3 has no waist DoF, so user torso rotation cannot be mapped).
- **Missing training details**: The paper does not specify training steps, number of parallel environments, learning rate, network architecture, inference frequency, or other key reproduction parameters.

## Engineering Insights

- **Reproduction priority**: First verify whether the actuator identification parameters (armature=0.045, friction loss=0.03, effort limit=3.6) apply to your servo model; the DYNAMIXEL current-torque linearity assumption is a critical prerequisite—validate linearity on a static test bench, otherwise PD control will be distorted.
- **Most common pitfalls**: ① The 200 Hz control frequency is limited by TTL communication; switching to a higher-bandwidth bus requires retuning PD gains; ② The threshold x_threshold in contact force estimation (Eq. 2) must be adjusted based on measured mechanical delay, otherwise contact is misjudged; ③ Video latency masking relies on EMA filter parameters that must precisely match neck mechanical delay, otherwise the operator experiences dizziness.
- **Guidance for downstream teams**: If the target task is fine manipulation, prioritize adding gravity/friction compensation to lower PD gains and improve compliance; if the goal is walking robustness, refer to the domain randomization ranges in Table I, but note that excessive randomization may reduce manipulation precision. For carrying tasks, real grippers or end-effector force sensors are a direct means to improve success rates.
- **Data value**: This system can serve as a data collection platform for miniature humanoid loco-manipulation, but tethering and foot lift height issues must first be resolved, otherwise the quality of collected data will be limited.

## 개요

본 논문은 소형 휴머노이드 로봇 ROBOTIS OP3를 위한 순응형 전신 원격현장 제어 스택을 제안한다. VR 상반신 원격 조작과 RL 하반신 보행/균형 제어를 분리하고, PD 임피던스 제어를 통해 양팔 조작과 양다리 보행의 협력을 구현한다. 시스템은 실제 로봇에서 보행, 집기, 운반 작업을 완료하여 저비용 소형 플랫폼의 loco-manipulation 실행 가능성을 검증하고, 완전한 소프트웨어/하드웨어 구현 세부 사항을 공개한다.

## 그것이 바꾼 것

전신 휴머노이드 로봇의 VR+RL 제어 스택(예: HOMIE, Mobile-TeleVision)은 강력하지만 하드웨어 비용이 높고 조작 장벽이 커서 연구 커뮤니티가 재현하고 데이터를 축적하기 어렵다. 소형 휴머노이드 로봇(예: OP3)은 가격이 저렴하고 접근이 용이하지만, 자유도가 적고 센서가 단순하며 액추에이터 비선형성이 강해 오랫동안 완전한 전신 제어 솔루션이 부재했다. 기존 연구는 상반신 원격 조작만 하거나 하반신 보행만 다루었으며, 둘을 결합하고 실제 운반 작업을 검증한 사례는 드물었다.

본 논문이 실제로 바꾼 것은: 20자유도, 관절 토크 센서 없음, 전류 개루프 토크 제어만 가능한 소형 플랫폼에서 "VR 원격 조작(상반신) + RL 정책(하반신) + 전신 PD 임피던스"의 계층적 아키텍처를 통해 사용 가능한 loco-manipulation 시스템을 구축할 수 있음을 증명한 것이다. 이는 값비싼 데모를 보여주는 것이 아니라 저비용 휴머노이드 로봇 연구를 위한 재현 가능한 기준선을 제공한다. 그 의미는 "전신 원격 조작"을 전신 플랫폼의 전유물에서 소형 플랫폼의 현실적 선택지로 바꾼 것이다.

## 방법 분해

### 시스템 아키텍처
- **계층적 제어**: VR 원격 조작은 양팔(팔당 3 DoF)과 목(2 DoF)을 담당하고, RL 정책은 양다리(다리당 6 DoF)를 담당하며, 둘은 전신 PD 임피던스 제어(식 1)를 통해 관절 수준에서 융합된다.
- **하드웨어**: ROBOTIS OP3(20 DoF, DYNAMIXEL XM430-W350-R 서보), 카메라는 VR180 듀얼 어안(3840×1080@60Hz)으로 교체, 호스트는 i9+RTX 4090, VR은 VIVE Pro 2 + 4 베이스스테이션.

### 상반신 원격 조작
- **모션 리타겟팅**: 다중 목표 IK 솔버 [28]가 VR 컨트롤러 위치를 추적하며, 내장 사다리꼴 속도 프로파일이 관절 최대 속도/가속도를 제한한다. VIVE 트리거가 스위치 역할을 하며, 해제 시 IK 제한을 0으로 만들고, 누를 때 EMA 필터를 통해 천천히 복구한다.
- **토크 제어**: 맞춤형 PD 컨트롤러(식 1), 200 Hz에서 실행(TTL 제한). DYNAMIXEL 서보는 하드웨어 전류 제어를 통한 개루프 토크를 구현하며, 전류-토크 선형성을 가정한다(모터 상수는 락 토크/전류로 결정). 정적 테스트 벤치에서 선형 동작을 검증한다.
- **접촉력 추정(식 2)**: F = −Kx(x는 가상 모델과 반투명 모델 엔드 이펙터 간 벡터 거리), 임계값 미만일 때 오차가 기계적 지연에 의한 것으로 가정하며 완전한 동역학 모델에 의존하지 않는다.
- **비디오 스트리밍**: UDP + GStreamer, GPU 가속 H.265 트랜스코딩, 글래스-투-글래스 지연 약 100 ms, 비트레이트 <4 Mbps. 목 기계적 지연은 디스플레이 구체를 역회전시켜 마스킹하고, EMA 필터로 평활화한다.

### 하반신 RL 보행
- **MDP 정식화**: 할인된 보상 G_t = Σ γᵏR(S_{t+k}, A_{t+k})를 최대화하고, 최적 정책 π*는 상태 조건 및 상태-행동 조건 기대 보상을 동시에 최대화한다.
- **관측 공간**: 5개 항목(각속도, 투영 중력, 사용자 명령, 관절 위치, 이전 행동), 각 항목에 이전 9단계 히스토리를叠加하여 330×1 벡터를 구성한다. 관절 속도는 모델이 추론하며 관측에 포함되지 않는다.
- **보상 설계**: 보행 보상(이중 지지/단일 지지), 발 방향 페널티(투영 중력 xy 성분), 발 지면 이탈 보상, 행동 평활도 페널티 등, 가중치는 표 III 참조.
- **도메인 무작위화**: 발 마찰 (0.5, 0.9), 중력 스케일 (0.95, 1.3), 링크 질량 (0.7, 1.3), 신체 속도/위치/방향 가산 잡음, 관절 위치/속도 스케일링. 밀기 이벤트는 (10, 15)초마다 무작위로 신체 선속도를 추가한다.
- **액추에이터 식별**: BAM 방법은 진자 테스트 벤치 기반, 파라미터 armature=0.045, friction loss=0.03, effort limit=3.6, Isaac Sim에서 검증.

### 터치패드 매핑
- VIVE 2D 터치패드는 차동 구동식 속도 명령(각속도 1개, 선속도 1개)으로 매핑되어 하반신 RL 정책으로 전송된다.

## 핵심 혁신

1. **소형 플랫폼 전신 제어 스택의 최초 완전 구현**: 이전에는 VR 원격 조작과 RL 보행이 각각 소형 플랫폼에서 독립적으로 검증되었지만, 본 논문은 처음으로 둘을 OP3에서 융합하고 실제 운반 작업을 완료하여 저비용 플랫폼 loco-manipulation 연구의 공백을 메웠다.
2. **관절 토크 센서가 필요 없는 순응 제어**: DYNAMIXEL 서보의 전류-토크 선형 관계를 활용한 개루프 토크 제어와 맞춤형 PD 게인(팔은 낮게, 다리는 높게)을 통해 토크 센서 없이 순응 조작 능력을 확보하여 하드웨어 장벽을 낮췄다.
3. **가상 오차 기반 접촉력 추정**: 식 2는 로봇 팔 동역학 모델에 의존하지 않고 가상 모델과 반투명 모델 간의 거리 오차만으로 접촉력을 추정하여, Jacobian 방법보다 간단하고 실용적이며 센서가 부족한 소형 플랫폼에 적합하다.

## 실험 및 결과

시스템 전체 성능을 검증하기 위해 저자는 ROBOTIS OP3 소형 휴머노이드 로봇(20개 회전 자유도)에서 세 가지 실험을 수행했다: 원격 조작 검증(양팔 원 그리기), 운동 검증(무작위 전신 속도 명령 하의 이족 안정성), 원격-운동-조작 통합 실험(보행, 3D 프린팅 PLA 큐브 집기 및 운반). 원격 조작 하드웨어는 VIVE Pro 2 HMD, VIVE 컨트롤러, 4개 SteamVR Basestation 2.0 및 KAT Walk C2+ VR 트레드밀을 사용하며, 제어 주파수는 200 Hz, 비디오 시스템은 VR180 듀얼 어안 USB 카메라(3840 × 1080 수평 나란히 이미지, 60 Hz, H.265 트랜스코딩, 글래스-투-글래스 지연 약 100 ms)이다. 운동 정책은 도메인 무작위화(발 마찰 (0.5, 0.9), 중력 스케일 (0.95, 1.3), 링크 질량 스케일 (0.7, 1.3) 등)와 관측 잡음 주입(각속도 0.2, 투영 중력 0.1, 관절 위치 0.05)으로 훈련되었으며, 관측 공간은 330 × 1 벡터이다. 통합 실험에서 조작자는 10분 내에 10회 시도를 완료했으며, 각 시도는 약 5m를 보행하고 40g 큐브 운반을 시도했다.

| 지표 | 값 |
|------|------|
| 원격 조작 운동 지연(y 방향) | 220 ms |
| 오른손 x 방향 위치 추적 MAE / RMSE | 8.76 / 12.35 |
| 오른손 y 방향 위치 추적 MAE / RMSE | 10.58 / 15.07 |
| 오른손 z 방향 위치 추적 MAE / RMSE | 8.68 / 11.17 |
| 통합 실험 성공적 큐브 운반 수 | 6개 중 2개 |
| 통합 실험 평균 보행 속도 | 0.35 m/s |
| 보행 속도 상한(요약) | 0.45 m/s |

**결과 의미:**

- **원격 조작 정밀도는 지연에 의해 지배됨**: 일부 팔 위치 오차의 RMSE 또는 MAE가 15를 초과하지만(논문에서 명확히 밝히지 않음), 대부분의 순간 오차는 약 220 ms의 운동 지연에 기인한다. 상지는 조작자가 요구한 원 그리기 동작을 명확히 재현할 수 있어, 지연 보상 후 원격 조작 매핑이 사용 가능한 정밀도를 가짐을 보여준다.
- **운동 정책은 급격한 명령 하에서도 안정성을 유지**: 정규화된 투영 중력이 기대값 -1 근처에 유지되어, RL 정책이 무작위하고 급격한 보행 속도 명령 변화 하에서도 올바르게 안정적인 몸통 자세를 유지함을 보여주며, 도메인 무작위화 훈련의 효과를 검증한다.
- **통합 작업 성능은 조작 난이도와 좌절감에 의해 제약됨**: 시스템은 10분 내에 6개 중 2개의 큐브만 성공적으로 운반했으며, 평균 보행 속도는 0.35 m/s이다. 저자는 성능 병목이 주로 세 가지 측면에서 비롯된다고 지적한다: RL 정책 보행 시 발 들기 높이 부족, 사용자가 큐브를 들어 올릴 충분한 힘을 내기 위해 팔을 교차해야 함, 유선 전원 연결로 인한 운동 도전. 시스템에 중력 및 마찰 보상 항목이 없어 높은 PD 게인을 사용해야 하며, 이는 순응성을 더욱 저하시킨다.

## 경계 및 한계

- **운반 성능 제한적**: 평균 6개 중 2개의 큐브만 운반했으며, RL 보행 정책의 발 들기 높이 부족, 사용자가 충분한 파지력을 내기 위해 팔을 교차해야 함, 케이블 전원 공급이 보행을 방해함에 기인한다.
- **순응성과 힘 제어의 모순**: 중력/마찰 보상 부재로 높은 PD 게인이 필요하며, 순응성을 희생한다. 보상 항목 추가를 권장하지만 정확한 동역학 모델이 필요하다.
- **액추에이터 모델 조잡함**: sim2real 격차에 대응하기 위해 과도한 도메인 무작위화가 필요하며, 이는 실제 환경에서 정책의 상한 성능에 영향을 줄 수 있다.
- **수행하지 않은 것**: VR 트레드밀(KAT Walk C2+) 통합 미구현, 무선 조작 미구현, 더 어려운 지형 미사용, 실제 그리퍼/엔드 이펙터 힘 센서 미추가, 허리 자유도 부재 처리 미수행(OP3에는 허리 DoF가 없어 사용자 몸통 회전을 매핑할 수 없음).
- **훈련 세부 사항 누락**: 논문은 훈련 스텝 수, 병렬 환경 수, 학습률, 네트워크 구조, 추론 빈도 등 핵심 재현 파라미터를 명확히 밝히지 않았다.

## 공학적 시사점

- **재현 우선순위**: 먼저 액추에이터 식별 파라미터(armature=0.045, friction loss=0.03, effort limit=3.6)가 사용 중인 서보 모델에 적용되는지 확인하라. DYNAMIXEL 전류-토크 선형 가정은 핵심 전제이므로 반드시 정적 테스트 벤치에서 선형성을 검증해야 하며, 그렇지 않으면 PD 제어가 왜곡된다.
- **가장 쉽게 빠지는 함정**: ① 200 Hz 제어 주파수는 TTL 통신 제한에 기인하므로, 더 높은 대역폭 버스로 변경하면 PD 게인을 다시 조정해야 한다. ② 접촉력 추정(식 2)의 임계값 x_threshold는 기계적 지연 실측에 따라 조정해야 하며, 그렇지 않으면 접촉을 오판한다. ③ 비디오 지연 마스킹은 EMA 필터 파라미터에 의존하므로 목 기계적 지연과 정확히 일치해야 하며, 그렇지 않으면 조작자가 어지러움을 느낀다.
- **하위 팀 지침**: 목표 작업이 정밀 조작이라면 중력/마찰 보상을 우선 추가하여 PD 게인을 낮추고 순응성을 높이는 것이 좋다. 목표가 보행 견고성이라면 표 I의 도메인 무작위화 범위를 참조할 수 있지만, 과도한 무작위화가 조작 정밀도를 저하시킬 수 있음에 주의하라. 운반 작업에서 실제 그리퍼 또는 엔드 이펙터 힘 센서는 성공률을 높이는 직접적인 수단이다.
- **데이터 가치**: 이 시스템은 소형 휴머노이드 로봇 loco-manipulation 데이터 수집 플랫폼으로 사용될 수 있지만, 먼저 케이블 문제와 발 들기 높이 문제를 해결해야 하며, 그렇지 않으면 수집된 데이터 품질이 제한된다.
