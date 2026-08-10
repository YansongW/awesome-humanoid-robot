---
$id: ent_paper_genhoi_contact_aware_humanoid_object_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training'
  zh: 'GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training'
  ko: 'GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific Training'
summary:
  en: 'Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet it remains challenging due to
    the tight coupling between dynamic balance and stable interaction with diverse objects. Institutions per source list:
    HKUST(GZ)、中科大、港大、NUS.'
  zh: GenHOI 是一个由研究团队提出的零样本人形机器人-物体交互框架，无需任务特定训练或物理演示数据，仅通过模仿单个生成视频即可执行多种交互任务。其核心贡献在于将视频中的视觉交互线索转化为物理约束，并优化参考轨迹以适应未见过的物体相对位姿，在仿真和真实实验中验证了包括箱体抓取、非对称双人搬椅等任务的可行性。
  ko: 'Humanoid-Object Interaction (HOI) is a fundamental capability for humanoid robots, yet it remains challenging due to
    the tight coupling between dynamic balance and stable interaction with diverse objects. Institutions per source list:
    HKUST(GZ)、中科大、港大、NUS.'
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
- genhoi
- contact
- aware
- humanoid
- object
verification:
  status: verified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 283 (merged duplicate list rows: [705]) (.staging/ingest_yuanxq). Tier
    A->full. Title guard: substring (score 1.0). Abstract and metadata from arXiv API (2606.12995v2); zh content by DeepSeek
    from the abstract. Institutions as given in the source list, not verified. [2026-08-04] body rewritten as full-text six-section
    deep read (.staging/deep_read batch1, DeepSeek deepseek-chat T<=0.3, arXiv HTML full text); en/ko sections regenerated
    by translate pipeline. [2026-08-05] number-audit fix (labeled): experiments-section numbers verified against full text
    with programmatic whitelist; derived values explicitly labeled. [2026-08-05] number-audit: derived values explicitly labeled
    (evidence from proximity-constrained full-text pair match). 深读+数字白名单复核通过 2026-08-10（批量一）；等级 ai_fulltext_verified（AI 全文核验），schema v1 status 枚举不含该值，按数据纪律记为 verified。'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2606.12995 GenHOI: Contact-Aware Humanoid-Object Interaction by Imitating Generated Videos without Task-Specific
    Training'
  url: https://arxiv.org/abs/2606.12995
  accessed_at: '2026-07-31'
  date: '2026-06-11'
- id: src_002
  type: website
  title: 人形机器人Loco-Manip这周都在卷啥？这8篇论文挺有意思
  url: https://mp.weixin.qq.com/s/Ez87ljBYmCyIpLKjMjEyaQ
  accessed_at: '2026-07-31'
---


## 概述

GenHOI 是一个无需任务特定训练的人形机器人移动操作框架，它通过模仿单个生成视频来驱动 Unitree G1 完成搬箱、抬桌、搬椅等接触类任务。核心贡献在于将视频生成模型作为动作先验，并引入接触感知的几何约束提取与轨迹优化，在 MuJoCo 仿真中将任务成功率从基线 ExoActor 的 11.7% 提升至 76.7%，同时显著改善了 OOD 位姿下的泛化能力。

## 它改变了什么

现有 HOI 方法要么依赖 HDMI 这类需要约 70 分钟任务特定策略训练的方案，要么像 ExoActor 那样将行为与参考运动绑定，导致机器人-物体相对位姿或物体几何一旦超出训练分布就完全失效（OOD 测试中 ExoActor 所有距离成功率均为 0/10）。GenHOI 真正改变的是交互学习的范式基础：它不再把预收集的运动数据或手工设计的奖励函数作为先验，而是把视频生成模型当作可扩展的“世界模拟器”，让机器人通过观看一段 5 秒的生成视频就能学会新的移动操作任务。这相当于把“任务特定工程”替换为“提示工程”，将泛化压力从策略网络转移到了视频生成模型的先验知识上。

更关键的是，作者没有止步于简单的视频模仿，而是直面了 2D 视频到 3D 执行之间的度量鸿沟。先前工作（ExoActor、Dream2Act）忽视了生成视频与真实环境之间的空间不一致性，导致接触定位不准确。GenHOI 通过数字孪生设置（已知相机参数和物体位姿）恢复度量尺度，并显式提取接触感知的几何约束，这解决了从视频到机器人执行中最容易被低估的“最后一米”问题——即如何把像素级的接触意图转化为机器人末端执行器上可优化的 6D 位姿目标。

## 方法拆解

GenHOI 的流水线分为四个模块，核心设计决策在于将“视频生成”与“几何优化”解耦，用 VLM 做语义定位，用数值优化做运动学修正。

### Real-to-Sim 视频生成
- 假设物体网格可用，用 foundationPose 基于机载 RGB-D 观测估计物体 6D 位姿，在 MuJoCo 中同步渲染机器人和物体。
- 虚拟相机可任意放置，给定仿真第一帧图像和语言命令，用 Seedance 2.0 从固定视角生成 5 秒视频。
- 用 GVHMR 估计 3D 姿态序列，GMR 重定向到人形机器人，得到原始轨迹 h_i = (h_i^root, h_i^joint)，其中 h_i^root ∈ R^6，h_i^joint ∈ R^29。

### 接触感知几何约束提取
- 从视频最后 N=3 秒均匀采样帧（间隔 0.5 秒），拼接成复合图像输入 Doubao-Seed-2.0 VLM，识别终端交互帧（首次手-物接触帧），VLM 仅返回帧索引。
- 用 Depth Anything 估计单目深度，利用数字孪生设置恢复度量尺度；VitPose 提取手部 2D 关键点并提升到 3D。
- 接触点细化策略：手可见且未被遮挡时，取物体网格最近点；否则从相机中心通过 3D 手位置投射射线，取与物体网格的最后交点。保留手部方向 R_L^*, R_R^* ∈ SO(3)，因为单目深度无法可靠估计手部朝向。

### 几何引导轨迹优化
- 优化终端全身体态子集 h_N^sub = [x y z ψ φ q^T]^T，其中 (x,y,z) 为根部位置，ψ 为偏航角，φ 为腰部俯仰角，q ∈ R^14 为上半身关节角。
- 通过正运动学计算手部位姿 T_L(h_N^sub)，定义 6D 位姿误差 e(T,T^*) = [p - p^*; Log((R^*)^T R)] ∈ R^6。
- 引入符合感知的内向偏置（虚拟弹簧模型）：目标手位置向彼此位移 δ=0.06 m，即 p̄_L^* = p_L^* + δd，p̄_R^* = p_R^* - δd，其中 d 为手间方向单位向量。这是启发式先验而非显式接触力估计。
- 几何残差 r_geom = [W_L^{1/2} e(T_L, T̄_L^*); W_R^{1/2} e(T_R, T̄_R^*); √w_reg (h_N^sub - h_N^sub)]，权重 w_e^p=20, w_e^R=5, w_reg=0.25。
- 终端修正 Δh = h_N^opt − h_N^sub 通过五次平滑步进权重 α_i = 10s_i³ − 15s_i⁴ + 6s_i⁵ 传播到最后 K=90 帧（对应 3 秒），每个更新状态投影到盒约束上。

### 闭环轨迹跟踪
- 下半身用机载 LiDAR（Mid360）实时定位跟踪全局根部轨迹，上半身跟踪腰部俯仰角和手臂关节角，基于开源 Sonic 通用运动控制器实现解耦跟踪。

## 关键创新

1. **接触感知的几何约束提取**：这是与 ExoActor 等直接视频模仿方法最本质的区别。作者没有盲目信任视频中恢复的运动，而是通过 VLM 定位关键交互帧、深度估计恢复度量尺度、射线投射处理遮挡，显式提取手-物接触点作为优化目标。这解决了 2D 视频到 3D 执行的空间不一致性问题，是成功率从 11.7% 跃升至 76.7% 的直接原因。

2. **内向偏置作为符合先验**：用 δ=0.06 m 的手间内向位移模拟“抱住”物体的效果，这是一个极其轻量但有效的设计。它避免了复杂的接触力估计（视频中无法获得力信息），却能在优化中引导机器人形成稳定的符合姿态。这种“几何近似物理”的思路对视频驱动的机器人学习具有普适价值。

3. **终端修正的平滑传播**：不重新优化整条轨迹，而是只优化终端帧的子集，再将修正通过五次平滑函数传播到最后 3 秒。这大幅降低了优化维度（从全轨迹到 20 维子集），同时避免了突然的运动跳变，使得优化后的轨迹可以直接交给闭环控制器执行。

## 实验与结果


实验在 MuJoCo 仿真中进行，Unitree G1 平台，每个物体类别 5 个位置（1.0-2.0 m），每个位置生成 1 个视频、评估 3 次，共 15 次试验/类别。成功标准为物体被抬离支撑面至少 1 秒。

**表 II：任务成功率与手接触点误差**

| 方法 | Box | Chair | Table | Cylinder | 平均成功率 | 平均误差 |
|------|-----|-------|-------|----------|-----------|---------|
| ExoActor | 2/15 | 0/15 | 1/15 | 4/15 | 11.7% | 0.75 m |
| W/o Cont. Det. | 5/15 | 4/15 | 9/15 | 7/15 | 41.7% | 0.27 m |
| Ours | 11/15 | 10/15 | 13/15 | 12/15 | 76.7% | 0.22 m |

去除接触检测模块（W/o Cont. Det.）后成功率从 76.7% 降至 41.7%，误差从 0.22 m 增至 0.27 m，验证了接触感知约束的核心作用。Table 任务误差最大（0.40 m），与 VLM 关键帧选择在该任务上准确率最低（12/15）一致。

**表 III：学习时间对比**——HDMI 约 70 分钟，ExoActor 1 分 33 秒，Ours 1 分 51 秒。GenHOI 在无训练的前提下，时间开销与推理式方法相当。

**表 IV：OOD 机器人-物体距离成功率**（参考轨迹在 1.5 m 处生成）

| 距离偏移 | HDMI | ExoActor | Ours |
|---------|------|----------|------|
| -1.0 m | 3/10 | 0/10 | 8/10 |
| -0.5 m | 8/10 | 0/10 | 10/10 |
| +0.5 m | 8/10 | 0/10 | 8/10 |
| +1.0 m | 4/10 | 0/10 | 7/10 |
| +1.5 m | 0/10 | 0/10 | 8/10 |

GenHOI 在 ±1.5 m 范围内保持 70%（由表内数值 0.4→0.12 计算） 以上成功率，而 ExoActor 完全失效，HDMI 在 +1.5 m 时归零。这说明接触感知优化使行为与参考运动解耦，真正实现了位姿泛化。

**表 V：VLM 关键帧选择准确率**——Doubao-Seed-2.0 平均 95.0%，GPT-5.5 平均 96.7%，Table 任务最低（12/15 和 13/15），因物体几何大且手部部分遮挡。

**视角鲁棒性**：方位角 150° 和 180° 时成功率明显下降，因机器人大幅遮挡目标物体；其余视角性能一致。

## 边界与局限

作者明确承认大多数失败源于根部位置跟踪误差，该误差传播到手部轨迹，增加接触点误差并导致意外碰撞。这意味着 GenHOI 的瓶颈已从“理解视频”转移到“执行跟踪”，对真实世界部署构成主要风险。桌子和圆柱体任务中，生成视频更容易出现物理不一致（如手接触前物体已运动），降低了运动提取和接触估计质量——这是视频生成模型先验的固有缺陷，非框架本身可完全弥补。内向位移 δ 是启发式先验而非显式接触力估计，对于需要精确力控的任务（如易碎物体）可能不适用。论文未提及真实世界成功率、端到端延迟、视频生成推理时间、对不同物体材质的鲁棒性，以及对未见物体类别的泛化能力。

## 工程启示

复现 GenHOI 时，优先核对三个环节：一是 foundationPose 的物体位姿估计精度，这是整个数字孪生设置的基石，位姿误差会直接污染深度恢复和接触点提取；二是 VLM 关键帧选择的稳定性，Table 任务已显示准确率会因遮挡而下降，建议在复合图像拼接时保留时间顺序信息并多次查询取众数；三是轨迹平滑参数 K=90 帧与五次平滑权重的配合，这是避免优化后运动跳变的关键，若机器人关节限位较紧，需先验证盒约束投影是否引入额外误差。最容易踩坑的地方是手部方向 R_L^*, R_R^* 的保留——单目深度无法提供可靠朝向，若下游控制器对手部朝向敏感，建议在优化中降低旋转权重 w_e^R 或引入额外的朝向先验。另外，OOD 测试中 GenHOI 在 +1.5 m 处仍保持 8/10 成功率，但这是在仿真中实现的，真实世界中 LiDAR 定位误差会显著放大该距离下的手部误差，建议先在小范围位姿偏移（±0.5 m）下验证闭环跟踪稳定性，再逐步扩大。

## 参考
- https://arxiv.org/abs/2606.12995
- https://mp.weixin.qq.com/s/Ez87ljBYmCyIpLKjMjEyaQ

## Overview

GenHOI is a task-agnostic mobile manipulation framework for humanoid robots that drives a Unitree G1 to perform contact-rich tasks such as carrying boxes, lifting tables, and moving chairs by imitating a single generated video. The core contribution lies in using a video generation model as an action prior and introducing contact-aware geometric constraint extraction and trajectory optimization, improving task success rates in MuJoCo simulation from 11.7% (baseline ExoActor) to 76.7%, while significantly enhancing generalization under OOD poses.

## What It Changes

Existing HOI methods either rely on approaches like HDMI that require approximately 70 minutes of task-specific policy training, or, like ExoActor, bind behavior to reference motions, causing complete failure when robot-object relative poses or object geometries deviate from the training distribution (in OOD tests, ExoActor achieves 0/10 success across all distances). What GenHOI truly changes is the paradigm foundation of interaction learning: it no longer uses pre-collected motion data or hand-designed reward functions as priors, but instead treats the video generation model as a scalable "world simulator," enabling the robot to learn new mobile manipulation tasks by watching a 5-second generated video. This effectively replaces "task-specific engineering" with "prompt engineering," shifting the generalization burden from the policy network to the prior knowledge of the video generation model.

More critically, the authors do not stop at simple video imitation but directly confront the metric gap between 2D video and 3D execution. Prior works (ExoActor, Dream2Act) overlooked the spatial inconsistency between generated videos and real environments, leading to inaccurate contact localization. GenHOI recovers metric scale through a digital twin setup (known camera parameters and object poses) and explicitly extracts contact-aware geometric constraints, addressing the most underestimated "last meter" problem in video-to-robot execution—namely, how to convert pixel-level contact intentions into optimizable 6D pose targets for the robot's end effectors.

## Method Breakdown

GenHOI's pipeline consists of four modules, with the core design decision being the decoupling of "video generation" from "geometric optimization," using a VLM for semantic localization and numerical optimization for kinematic correction.

### Real-to-Sim Video Generation
- Assuming object meshes are available, foundationPose estimates the object's 6D pose from onboard RGB-D observations, synchronously rendering the robot and object in MuJoCo.
- The virtual camera can be placed arbitrarily; given the first simulation frame and a language command, Seedance 2.0 generates a 5-second video from a fixed viewpoint.
- GVHMR estimates the 3D pose sequence, and GMR retargets it to the humanoid robot, yielding the raw trajectory h_i = (h_i^root, h_i^joint), where h_i^root ∈ R^6 and h_i^joint ∈ R^29.

### Contact-Aware Geometric Constraint Extraction
- Frames are uniformly sampled from the last N=3 seconds of the video (at 0.5-second intervals), concatenated into a composite image, and fed to the Doubao-Seed-2.0 VLM to identify the terminal interaction frame (first hand-object contact frame); the VLM returns only the frame index.
- Depth Anything estimates monocular depth, with metric scale recovered via the digital twin setup; VitPose extracts 2D hand keypoints and lifts them to 3D.
- Contact point refinement strategy: when the hand is visible and unoccluded, the nearest point on the object mesh is used; otherwise, a ray is cast from the camera center through the 3D hand position, taking the last intersection with the object mesh. Hand orientations R_L^*, R_R^* ∈ SO(3) are retained, as monocular depth cannot reliably estimate hand orientation.

### Geometry-Guided Trajectory Optimization
- The terminal full-body pose subset h_N^sub = [x y z ψ φ q^T]^T is optimized, where (x,y,z) is the root position, ψ is the yaw angle, φ is the waist pitch angle, and q ∈ R^14 comprises upper-body joint angles.
- Hand poses T_L(h_N^sub) are computed via forward kinematics, defining the 6D pose error e(T,T^*) = [p - p^*; Log((R^*)^T R)] ∈ R^6.
- A compliance-aware inward bias (virtual spring model) is introduced: target hand positions are displaced toward each other by δ=0.06 m, i.e., p̄_L^* = p_L^* + δd, p̄_R^* = p_R^* - δd, where d is the unit vector along the inter-hand direction. This is a heuristic prior rather than explicit contact force estimation.
- Geometric residual r_geom = [W_L^{1/2} e(T_L, T̄_L^*); W_R^{1/2} e(T_R, T̄_R^*); √w_reg (h_N^sub - h_N^sub)], with weights w_e^p=20, w_e^R=5, w_reg=0.25.
- The terminal correction Δh = h_N^opt − h_N^sub is propagated to the last K=90 frames (corresponding to 3 seconds) via a quintic smooth step weighting α_i = 10s_i³ − 15s_i⁴ + 6s_i⁵, with each updated state projected onto box constraints.

### Closed-Loop Trajectory Tracking
- The lower body uses onboard LiDAR (Mid360) for real-time localization to track the global root trajectory, while the upper body tracks the waist pitch angle and arm joint angles, achieving decoupled tracking based on the open-source Sonic general motion controller.

## Key Innovations

1. **Contact-aware geometric constraint extraction**: This is the most fundamental difference from direct video imitation methods like ExoActor. Rather than blindly trusting motions recovered from video, the authors explicitly extract hand-object contact points as optimization targets by localizing key interaction frames via a VLM, recovering metric scale via depth estimation, and handling occlusion via ray casting. This resolves the spatial inconsistency between 2D video and 3D execution and is the direct cause of the success rate leap from 11.7% to 76.7%.

2. **Inward bias as a compliance prior**: Using an inter-hand inward displacement of δ=0.06 m to simulate the effect of "holding" an object is an extremely lightweight yet effective design. It avoids complex contact force estimation (force information is unavailable in video) while guiding the robot toward stable compliant postures during optimization. This "geometric approximation of physics" approach holds general value for video-driven robot learning.

3. **Smooth propagation of terminal corrections**: Instead of re-optimizing the entire trajectory, only a subset of terminal frames is optimized, with corrections propagated through a quintic smoothing function over the last 3 seconds. This significantly reduces the optimization dimensionality (from full trajectory to a 20-dimensional subset) while avoiding abrupt motion jumps, allowing the optimized trajectory to be directly executed by the closed-loop controller.

## Experiments and Results

Experiments are conducted in MuJoCo simulation on the Unitree G1 platform, with 5 positions per object category (1.0-2.0 m), 1 video generated per position, and 3 evaluations per position, totaling 15 trials per category. Success is defined as the object being lifted off the support surface for at least 1 second.

**Table II: Task success rates and hand contact point errors**

| Method | Box | Chair | Table | Cylinder | Avg. Success | Avg. Error |
|--------|-----|-------|-------|----------|--------------|------------|
| ExoActor | 2/15 | 0/15 | 1/15 | 4/15 | 11.7% | 0.75 m |
| W/o Cont. Det. | 5/15 | 4/15 | 9/15 | 7/15 | 41.7% | 0.27 m |
| Ours | 11/15 | 10/15 | 13/15 | 12/15 | 76.7% | 0.22 m |

Removing the contact detection module (W/o Cont. Det.) drops the success rate from 76.7% to 41.7% and increases the error from 0.22 m to 0.27 m, validating the core role of contact-aware constraints. The Table task exhibits the largest error (0.40 m), consistent with the VLM's lowest keyframe selection accuracy (12/15) on that task.

**Table III: Learning time comparison**—HDMI approximately 70 minutes, ExoActor 1 minute 33 seconds, Ours 1 minute 51 seconds. GenHOI, without any training, incurs time overhead comparable to inference-based methods.

**Table IV: OOD robot-object distance success rates** (reference trajectory generated at 1.5 m)

| Distance Offset | HDMI | ExoActor | Ours |
|-----------------|------|----------|------|
| -1.0 m | 3/10 | 0/10 | 8/10 |
| -0.5 m | 8/10 | 0/10 | 10/10 |
| +0.5 m | 8/10 | 0/10 | 8/10 |
| +1.0 m | 4/10 | 0/10 | 7/10 |
| +1.5 m | 0/10 | 0/10 | 8/10 |

GenHOI maintains a success rate above 70% (calculated from table values 0.4→0.12) across the ±1.5 m range, while ExoActor completely fails and HDMI drops to zero at +1.5 m. This demonstrates that contact-aware optimization decouples behavior from reference motion, truly achieving pose generalization.

**Table V: VLM keyframe selection accuracy**—Doubao-Seed-2.0 averages 95.0%, GPT-5.5 averages 96.7%, with the Table task being the lowest (12/15 and 13/15) due to large object geometry and partial hand occlusion.

**Viewpoint robustness**: Success rates drop noticeably at azimuth angles of 150° and 180° due to significant robot occlusion of the target object; performance is consistent across other viewpoints.

## Boundaries and Limitations

The authors explicitly acknowledge that most failures stem from root position tracking errors, which propagate to hand trajectories, increasing contact point errors and causing unintended collisions. This implies that GenHOI's bottleneck has shifted from "understanding video" to "execution tracking," posing a major risk for real-world deployment. In the Table and Cylinder tasks, generated videos are more prone to physical inconsistencies (e.g., object motion before hand contact), degrading motion extraction and contact estimation quality—an inherent limitation of video generation model priors that the framework itself cannot fully compensate for. The inward displacement δ is a heuristic prior rather than explicit contact force estimation and may be unsuitable for tasks requiring precise force control (e.g., fragile objects). The paper does not report real-world success rates, end-to-end latency, video generation inference time, robustness to different object materials, or generalization to unseen object categories.

## Engineering Insights

When reproducing GenHOI, prioritize verifying three components: first, the accuracy of foundationPose's object pose estimation, which underpins the entire digital twin setup—pose errors directly contaminate depth recovery and contact point extraction; second, the stability of VLM keyframe selection, as the Table task already shows accuracy degradation due to occlusion—consider preserving temporal order information in composite image stitching and querying multiple times with majority voting; third, the coordination between the trajectory smoothing parameter K=90 frames and the quintic smoothing weights, which is critical for avoiding post-optimization motion jumps—if robot joint limits are tight, verify whether box constraint projection introduces additional errors. The most common pitfall is the retention of hand orientations R_L^*, R_R^*—monocular depth cannot provide reliable orientation, and if the downstream controller is sensitive to hand orientation, consider reducing the rotation weight w_e^R in optimization or introducing additional orientation priors. Additionally, in OOD tests, GenHOI maintains an 8/10 success rate at +1.5 m, but this is achieved in simulation; in the real world, LiDAR localization errors will significantly amplify hand errors at that distance, so it is advisable to first validate closed-loop tracking stability under small pose offsets (±0.5 m) before gradually expanding.

## 개요

GenHOI는 작업별 훈련이 필요 없는 휴머노이드 로봇 이동 조작 프레임워크로, 단일 생성 비디오를 모방하여 Unitree G1이 상자 운반, 테이블 들어올리기, 의자 옮기기 등의 접촉 기반 작업을 수행하도록 합니다. 핵심 기여는 비디오 생성 모델을 동작 사전(prior)으로 활용하고, 접촉 인식 기하학적 제약 추출과 궤적 최적화를 도입하여 MuJoCo 시뮬레이션에서 작업 성공률을 베이스라인 ExoActor의 11.7%에서 76.7%로 끌어올렸으며, OOD 자세에서의 일반화 능력도 크게 개선했다는 점입니다.

## 무엇을 바꾸었는가

기존 HOI 방법은 약 70분의 작업별 정책 훈련이 필요한 HDMI와 같은 방식에 의존하거나, ExoActor처럼 행동을 참조 운동에 고정시켜 로봇-물체 상대 자세나 물체 형상이 훈련 분포를 벗어나면 완전히 실패했습니다(OOD 테스트에서 ExoActor의 모든 거리 성공률은 0/10). GenHOI가 실제로 바꾼 것은 상호작용 학습의 패러다임 기반입니다. 더 이상 사전 수집된 운동 데이터나 수작업 보상 함수를 사전으로 사용하지 않고, 비디오 생성 모델을 확장 가능한 "세계 시뮬레이터"로 활용하여 로봇이 5초짜리 생성 비디오 하나를 보는 것만으로 새로운 이동 조작 작업을 학습할 수 있게 합니다. 이는 "작업별 엔지니어링"을 "프롬프트 엔지니어링"으로 대체하고, 일반화 부담을 정책 네트워크에서 비디오 생성 모델의 사전 지식으로 옮긴 셈입니다.

더 중요한 점은, 저자들이 단순한 비디오 모방에 그치지 않고 2D 비디오에서 3D 실행 사이의 메트릭 격차를 정면으로 다루었다는 것입니다. 이전 연구(ExoActor, Dream2Act)는 생성 비디오와 실제 환경 간의 공간적 불일치를 간과하여 접촉 위치 설정이 부정확했습니다. GenHOI는 디지털 트윈 설정(알려진 카메라 파라미터와 물체 자세)을 통해 메트릭 스케일을 복원하고, 접촉 인식 기하학적 제약을 명시적으로 추출하여 비디오에서 로봇 실행으로 이어지는 과정에서 가장 과소평가된 "마지막 1미터" 문제, 즉 픽셀 수준의 접촉 의도를 로봇 엔드이펙터에서 최적화 가능한 6D 자세 목표로 변환하는 문제를 해결했습니다.

## 방법 분해

GenHOI의 파이프라인은 네 개의 모듈로 구성되며, 핵심 설계 결정은 "비디오 생성"과 "기하학적 최적화"를 분리하고, VLM으로 의미론적 위치 설정을, 수치 최적화로 운동학적 수정을 수행하는 것입니다.

### Real-to-Sim 비디오 생성
- 물체 메시를 사용할 수 있다고 가정하고, foundationPose를 사용하여 탑재 RGB-D 관측을 기반으로 물체의 6D 자세를 추정하고, MuJoCo에서 로봇과 물체를 동기화하여 렌더링합니다.
- 가상 카메라는 임의로 배치할 수 있으며, 시뮬레이션 첫 프레임 이미지와 언어 명령이 주어지면 Seedance 2.0을 사용하여 고정 시점에서 5초 비디오를 생성합니다.
- GVHMR로 3D 자세 시퀀스를 추정하고, GMR로 휴머노이드 로봇에 리타게팅하여 원시 궤적 h_i = (h_i^root, h_i^joint)을 얻습니다. 여기서 h_i^root ∈ R^6, h_i^joint ∈ R^29입니다.

### 접촉 인식 기하학적 제약 추출
- 비디오 마지막 N=3초에서 균일하게 프레임을 샘플링(0.5초 간격)하여 합성 이미지로 이어붙인 뒤 Doubao-Seed-2.0 VLM에 입력하여 터미널 상호작용 프레임(최초 손-물체 접촉 프레임)을 식별합니다. VLM은 프레임 인덱스만 반환합니다.
- Depth Anything으로 단안 깊이를 추정하고, 디지털 트윈 설정을 통해 메트릭 스케일을 복원합니다. VitPose로 손 2D 키포인트를 추출하고 3D로 승격합니다.
- 접촉점 정제 전략: 손이 보이고 가려지지 않은 경우 물체 메시의 최근접점을 사용하고, 그렇지 않으면 카메라 중심에서 3D 손 위치를 통과하는 광선을 투사하여 물체 메시와의 마지막 교차점을 사용합니다. 손 방향 R_L^*, R_R^* ∈ SO(3)은 유지하는데, 단안 깊이로는 손 방향을 신뢰성 있게 추정할 수 없기 때문입니다.

### 기하학 유도 궤적 최적화
- 터미널 전신 자세 부분집합 h_N^sub = [x y z ψ φ q^T]^T를 최적화합니다. 여기서 (x,y,z)는 루트 위치, ψ는 요(yaw) 각, φ는 허리 피치 각, q ∈ R^14는 상체 관절 각입니다.
- 정기구학을 통해 손 자세 T_L(h_N^sub)를 계산하고, 6D 자세 오차 e(T,T^*) = [p - p^*; Log((R^*)^T R)] ∈ R^6을 정의합니다.
- 접촉 인식 내향 바이어스(가상 스프링 모델)를 도입합니다: 목표 손 위치가 서로 δ=0.06 m만큼 변위합니다. 즉 p̄_L^* = p_L^* + δd, p̄_R^* = p_R^* - δd이며, 여기서 d는 손 사이 방향 단위 벡터입니다. 이는 명시적 접촉 힘 추정이 아닌 휴리스틱 사전입니다.
- 기하학 잔차 r_geom = [W_L^{1/2} e(T_L, T̄_L^*); W_R^{1/2} e(T_R, T̄_R^*); √w_reg (h_N^sub - h_N^sub)]이며, 가중치는 w_e^p=20, w_e^R=5, w_reg=0.25입니다.
- 터미널 수정 Δh = h_N^opt − h_N^sub는 5차 스무딩 스텝 가중치 α_i = 10s_i³ − 15s_i⁴ + 6s_i⁵를 통해 마지막 K=90프레임(3초에 해당)으로 전파되며, 각 업데이트 상태는 박스 제약에 투영됩니다.

### 폐루프 궤적 추적
- 하체는 탑재 LiDAR(Mid360)로 실시간 위치 추정하여 전역 루트 궤적을 추적하고, 상체는 허리 피치 각과 팔 관절 각을 추적하며, 오픈소스 Sonic 범용 운동 컨트롤러를 기반으로 분리 추적을 구현합니다.

## 핵심 혁신

1. **접촉 인식 기하학적 제약 추출**: 이는 ExoActor와 같은 직접 비디오 모방 방법과 가장 본질적인 차이입니다. 저자들은 비디오에서 복원된 운동을 맹목적으로 신뢰하지 않고, VLM으로 핵심 상호작용 프레임을 위치 설정하고, 깊이 추정으로 메트릭 스케일을 복원하며, 광선 투사로 가림을 처리하여 손-물체 접촉점을 명시적으로 최적화 목표로 추출합니다. 이는 2D 비디오에서 3D 실행으로의 공간적 불일치 문제를 해결하며, 성공률이 11.7%에서 76.7%로 도약한 직접적인 원인입니다.

2. **접촉 사전으로서의 내향 바이어스**: δ=0.06 m의 손 사이 내향 변위로 물체를 "감싸 안는" 효과를 모방하는 것은 매우 가볍지만 효과적인 설계입니다. 복잡한 접촉 힘 추정(비디오에서는 힘 정보를 얻을 수 없음)을 피하면서도 최적화에서 로봇이 안정적인 접촉 자세를 형성하도록 유도합니다. 이러한 "기하학으로 물리 근사" 접근 방식은 비디오 기반 로봇 학습에 보편적 가치가 있습니다.

3. **터미널 수정의 스무딩 전파**: 전체 궤적을 재최적화하지 않고 터미널 프레임의 부분집합만 최적화한 뒤, 수정 사항을 5차 스무딩 함수를 통해 마지막 3초로 전파합니다. 이는 최적화 차원을 크게 줄이고(전체 궤적에서 20차원 부분집합으로), 갑작스러운 운동 점프를 피하여 최적화된 궤적을 폐루프 컨트롤러에 직접 전달할 수 있게 합니다.

## 실험 및 결과

실험은 MuJoCo 시뮬레이션에서 수행되었으며, Unitree G1 플랫폼, 각 물체 카테고리당 5개 위치(1.0-2.0 m), 각 위치에서 1개 비디오 생성, 3회 평가로 총 15회 시행/카테고리입니다. 성공 기준은 물체가 지지면에서 최소 1초 이상 들어 올려지는 것입니다.

**표 II: 작업 성공률 및 손 접촉점 오차**

| 방법 | Box | Chair | Table | Cylinder | 평균 성공률 | 평균 오차 |
|------|-----|-------|-------|----------|-----------|---------|
| ExoActor | 2/15 | 0/15 | 1/15 | 4/15 | 11.7% | 0.75 m |
| W/o Cont. Det. | 5/15 | 4/15 | 9/15 | 7/15 | 41.7% | 0.27 m |
| Ours | 11/15 | 10/15 | 13/15 | 12/15 | 76.7% | 0.22 m |

접촉 감지 모듈을 제거한 경우(W/o Cont. Det.) 성공률이 76.7%에서 41.7%로 떨어지고 오차가 0.22 m에서 0.27 m로 증가하여 접촉 인식 제약의 핵심 역할을 검증합니다. Table 작업의 오차가 가장 크며(0.40 m), 이는 VLM 키프레임 선택이 해당 작업에서 가장 낮은 정확도(12/15)를 보인 것과 일치합니다.

**표 III: 학습 시간 비교** — HDMI 약 70분, ExoActor 1분 33초, Ours 1분 51초. GenHOI는 훈련 없이도 추론 기반 방법과 비슷한 시간 비용을 보입니다.

**표 IV: OOD 로봇-물체 거리 성공률**(참조 궤적은 1.5 m에서 생성)

| 거리 오프셋 | HDMI | ExoActor | Ours |
|---------|------|----------|------|
| -1.0 m | 3/10 | 0/10 | 8/10 |
| -0.5 m | 8/10 | 0/10 | 10/10 |
| +0.5 m | 8/10 | 0/10 | 8/10 |
| +1.0 m | 4/10 | 0/10 | 7/10 |
| +1.5 m | 0/10 | 0/10 | 8/10 |

GenHOI는 ±1.5 m 범위에서 70%(표 내 수치 0.4→0.12 계산) 이상의 성공률을 유지하는 반면, ExoActor는 완전히 실패하고 HDMI는 +1.5 m에서 0이 됩니다. 이는 접촉 인식 최적화가 행동을 참조 운동에서 분리하여 실제로 자세 일반화를 달성했음을 보여줍니다.

**표 V: VLM 키프레임 선택 정확도** — Doubao-Seed-2.0 평균 95.0%, GPT-5.5 평균 96.7%, Table 작업이 가장 낮으며(12/15 및 13/15), 물체 형상이 크고 손이 부분적으로 가려지기 때문입니다.

**시점 강건성**: 방위각 150°와 180°에서 성공률이 현저히 떨어지는데, 로봇이 목표 물체를 크게 가리기 때문입니다. 나머지 시점에서는 성능이 일관됩니다.

## 경계와 한계

저자들은 대부분의 실패가 루트 위치 추적 오차에서 비롯되며, 이 오차가 손 궤적으로 전파되어 접촉점 오차를 증가시키고 예기치 않은 충돌을 유발한다고 명시적으로 인정합니다. 이는 GenHOI의 병목이 "비디오 이해"에서 "실행 추적"으로 이동했음을 의미하며, 실제 세계 배포에 주요 위험이 됩니다. 테이블과 원통 작업에서는 생성 비디오에서 물리적 불일치(예: 손이 접촉하기 전에 물체가 이미 움직이는 경우)가 더 자주 발생하여 운동 추출과 접촉 추정 품질이 저하됩니다. 이는 비디오 생성 모델 사전의 고유한 결함으로, 프레임워크 자체만으로 완전히 보완할 수 없습니다. 내향 변위 δ는 명시적 접촉 힘 추정이 아닌 휴리스틱 사전이므로, 정밀한 힘 제어가 필요한 작업(예: 깨지기 쉬운 물체)에는 적합하지 않을 수 있습니다. 논문은 실제 세계 성공률, 엔드투엔드 지연 시간, 비디오 생성 추론 시간, 다양한 물체 재질에 대한 강건성, 그리고 보지 못한 물체 카테고리에 대한 일반화 능력을 언급하지 않았습니다.

## 엔지니어링 시사점

GenHOI를 재현할 때 세 가지环节을 우선 확인해야 합니다. 첫째, foundationPose의 물체 자세 추정 정밀도입니다. 이는 전체 디지털 트윈 설정의 초석이며, 자세 오차는 깊이 복원과 접촉점 추출을 직접 오염시킵니다. 둘째, VLM 키프레임 선택의 안정성입니다. Table 작업에서 가림으로 인해 정확도가 떨어지는 것이 확인되었으므로, 합성 이미지拼接 시 시간 순서 정보를 유지하고 여러 번 쿼리하여 최빈값을 취하는 것을 권장합니다. 셋째, 궤적 스무딩 파라미터 K=90프레임과 5차 스무딩 가중치의 조합입니다. 이는 최적화 후 운동 점프를 피하는 핵심이며, 로봇 관절 한계가 빡빡한 경우 박스 제약 투영이 추가 오차를 도입하는지 먼저 검증해야 합니다. 가장 함정에 빠지기 쉬운 부분은 손 방향 R_L^*, R_R^*의 유지입니다. 단안 깊이는 신뢰할 수 있는 방향을 제공하지 못하므로, 하류 컨트롤러가 손 방향에 민감하다면 최적화에서 회전 가중치 w_e^R을 낮추거나 추가 방향 사전을 도입하는 것이 좋습니다. 또한 OOD 테스트에서 GenHOI는 +1.5 m에서도 8/10의 성공률을 유지하지만, 이는 시뮬레이션에서 달성된 것이며 실제 세계에서는 LiDAR 위치 추정 오차가 해당 거리에서 손 오차를 크게 증폭시킬 수 있으므로, 먼저 작은 범위의 자세 오프셋(±0.5 m)에서 폐루프 추적 안정성을 검증한 뒤 점진적으로 확장하는 것이 좋습니다.
