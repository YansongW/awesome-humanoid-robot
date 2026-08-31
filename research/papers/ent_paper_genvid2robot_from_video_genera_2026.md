---
$id: ent_paper_genvid2robot_from_video_genera_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency'
  zh: 'GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency'
  ko: 'GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency'
summary:
  en: 'arXiv:2607.09191v1 Announce Type: new Abstract: Generated videos provide useful visual motion priors for robot manipulation,
    but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry,
    grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable
    in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated
    video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction,
    GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated
    video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse
    relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct
    robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is
    then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution
    trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution
    mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation
    module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate
    that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with
    sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.'
  zh: GenVid2Robot 是一个将生成视频中的运动转化为真实机器人可执行操作轨迹的框架，由研究团队提出。其核心贡献在于通过刚体几何一致性约束，将生成视频视为不确定的视觉运动假设而非直接演示，仅转移几何一致的运动，并结合掩码约束抓取与有界深度补偿模块，显著提升了视频引导操作的真实世界可靠性。
  ko: 'arXiv:2607.09191v1 Announce Type: new Abstract: Generated videos provide useful visual motion priors for robot manipulation,
    but their visual plausibility does not imply physical executability. A generated video usually lacks metric geometry,
    grasp grounding, robot kinematic feasibility, and execution-time feedback, which makes direct trajectory replay unreliable
    in real-world manipulation. This paper presents GenVid2Robot, a rigid-geometric consistency framework that converts generated
    video motion into executable real-robot manipulation trajectories. Given an initial RGB-D observation and a task instruction,
    GenVid2Robot samples task-relevant semantic anchors from the real first frame, tracks these anchors through generated
    video candidates, and verifies whether the resulting 2D motion can be explained by first-frame RGB-D anchors under a sparse
    relative $SE(3)$ model. In this way, generated videos are treated as uncertain visual motion hypotheses rather than direct
    robot demonstrations. Only geometrically consistent motion is transferred to the robot. The accepted relative motion is
    then applied to the real grasp-time TCP pose selected by mask-constrained grasping, producing a grasp-conditioned execution
    trajectory that is consistent with both the visual motion prior and the physical grasp configuration. To reduce execution
    mismatch caused by RGB-D noise, calibration residuals, and small contact-induced displacement, a bounded depth-compensation
    module corrects local depth-direction errors without assuming full online replanning. Real-robot experiments demonstrate
    that GenVid2Robot improves the reliability of generated-video-guided manipulation by grounding visual motion priors with
    sparse metric geometry, grasp constraints, robot feasibility checking, and bounded execution feedback.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- genvid2robot
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.09191v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (939 chars, DeepSeek). [2026-08-28] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'GenVid2Robot: From Video Generation to Robot Manipulation via Rigid-Geometric Consistency (arXiv)'
  url: https://arxiv.org/abs/2607.09191
  date: '2026'
  accessed_at: '2026-07-14'
---
## 概述

GenVid2Robot 提出一种将生成视频转化为可执行机器人操作轨迹的框架，由 GenVid2Robot 团队完成。其核心贡献在于将生成视频视为不确定的二维运动假设，通过第一帧 RGB-D 观测构建语义锚点，并利用稀疏刚性 SE(3) 一致性验证筛选出几何上可信的运动，再结合抓取条件 TCP 归纳与有界深度补偿，实现无需对象 CAD 模型或预收集演示的真实操作。

## 它改变了什么

该工作真正改变的是“生成视频到机器人操作”这一范式的信任基础。此前方法（如 RIGVid、NovaFlow）默认生成视频中的视觉运动可直接映射为机器人动作，但视觉合理性掩盖了物理不可行性——漂移对应、非刚性伪影、不一致深度演化等问题导致直接轨迹重放在真实操作中频繁失败。GenVid2Robot 将问题重新定义为：生成视频只是提供运动假设的“提案”，必须经过几何与物理的验证关卡才能被采纳。

这一转变的深层意义在于，它把“视频生成质量”与“机器人执行可行性”解耦。系统不再被动接受生成结果，而是主动用真实观测的度量几何去检验假设，拒绝那些视觉上合理但物理上不可解释的运动。这种“验证优先”的设计哲学，使得系统对生成模型的误差具有鲁棒性，而非依赖生成模型的完美性，这是从“生成即执行”到“生成需验证”的关键范式跃迁。

## 方法拆解

### 阶段 1：语义锚点采样与视频运动假设
- 使用 VLM（如 GPT-4V）提出任务相关部件级提示（如倾倒任务的 handle、body、spout），SAM 分割产生部件掩码。
- 深度感知特征：φ(u,v) = [u/W, v/H, D₀(u,v)/dₛ]ᵀ，其中 D₀ 为第一帧深度，dₛ 为归一化常数。
- 每掩码执行 K-Means 聚类（K_m=5），锚点选为距聚类中心最近的合法像素，抑制邻近重复。
- 锚点反投影至第一帧相机坐标系，形成稀疏度量参考 P_c⁰，不依赖 CAD 定义的规范坐标系。
- 使用 Kling 1.6 生成 5 个候选视频，VLM 语义筛选去除对象身份/形状/运动方向不一致者，CoTracker 传播锚点得到 2D 轨迹与置信度。

### 阶段 2：刚性几何一致性验证
- 过滤低置信度、出图像、无效关联锚点，要求至少 4 个有效锚点且第一帧 3D 点非共线。
- 使用 OpenCV solvePnPRansac 估计帧间相对运动，RANSAC 内点阈值约 8 像素。
- 重投影残差 e_{n,t} = 内点上平均‖q - q̂‖₂，接受条件：ē_n < 5 px，e_max < 12 px，r_valid > η_v，L_invalid < L_max。
- 多候选通过时，选择最低组合分数 C_n = ē_n + λ_max·e_max - λ_v·r_valid + λ_s·E_smooth。
- 接受的运动序列执行前平滑：平移用移动窗口或 Savitzky–Golay 滤波，旋转在符号对齐后用单位四元数平滑；短无效区间仅在候选级接受后通过 SE(3) 插值填充。

### 阶段 3：抓取选择与 TCP 归纳
- AnyGrasp 从真实 RGB-D 点云生成 6-DoF 抓取候选，接触区域落在任务相关掩码外的被移除。
- 抓取选择分数：S_j = s_j - λ_m·E_m(j) - λ_r·E_r(j) - λ_c·E_c(j)，其中 E_m 为掩码不一致惩罚，E_r 为可达性/近奇异惩罚，E_c 为碰撞惩罚。
- 名义 TCP 轨迹：T̃_tcp^(t) = ΔT̄_b^(t)·T_tcp^(0)，将验证的相对运动施加到选定抓取位姿。
- PyBullet IK 检查（RM75 URDF），每帧从上一关节解初始化，可行性阈值：位置 0.01 m，方向 0.40 rad；关节轨迹经 CubicSpline 插值和 Savitzky–Golay 滤波后 FK 回检。

### 阶段 4：有界深度补偿
- 深度误差：e_d(t) = d_rs(t) - d_exp(t)，d_rs 为对象掩码或抓取邻域中值有效深度。
- 修正：p_cmd(t) = p̄_tcp(t) + clip(λ_d·e_d(t), -d_max, d_max)·r_b，仅沿相机深度方向修正，保持名义方向。
- 参数：λ_d ∈ [0.3, 0.5]，d_max ∈ [0.005, 0.01] m；无可靠局部深度时修正项为零。

## 关键创新

1. **刚性几何一致性作为验证关卡**：将生成视频的运动假设与第一帧真实 RGB-D 度量几何对齐，通过稀疏 SE(3) 模型检验其物理可解释性。这是首次将“几何验证”而非“语义相似性”作为视频到机器人运动转移的核心筛选标准，直接过滤掉视觉合理但物理漂移的候选。

2. **抓取条件 TCP 归纳**：不直接重放物体轨迹，而是将验证的相对运动施加到选定的真实抓取位姿上，使 TCP 轨迹与物体轨迹解耦。这一设计避免了物体中心路径与 TCP 路径的固定偏移假设，对抓取位置误差和物体形状差异具有天然鲁棒性。

3. **有界深度补偿作为执行时反馈**：在离线验证的名义轨迹上叠加单轴、有界的深度修正，而非全在线视觉伺服。这种“轻量级闭环”在保持系统稳定性的同时，补偿了 RGB-D 噪声和接触引起的位移，是实用性与鲁棒性的折中。

## 实验与结果

实验在 RM75 机械臂、平行夹爪、RealSense RGB-D 相机上进行，覆盖 4 个桌面任务（Pouring、Lifting、Tool Delivery、Sweeping），每任务 20 次真实试验。基线为三种复现变体（ReKep 风格、RIGVid 风格、NovaFlow 风格），共享相同抓取源、IK 检查器和执行接口。

| 指标 | Pouring | Lifting | Tool Delivery | Sweeping |
|------|---------|---------|---------------|----------|
| 成功率（GenVid2Robot） | 90% | 90% | 85% | 80% |
| 成功率（w/o filter） | 75% | 80% | 70% | 60% |
| 平均生成样本数 | 2.1 | 1.6 | 1.9 | 2.4 |
| 通过率 | 61% | 74% | 68% | 55% |
| 平均重投影误差 (px) | 3.4 | 2.8 | 3.1 | 4.0 |

| 锚点策略 | 存活率 | 有效 PnP | 重投影误差 (px) |
|----------|--------|----------|-----------------|
| Random points | 72.4% | 68.1% | 6.7 |
| Uniform mask points | 81.6% | 78.9% | 5.1 |
| Semantic anchors | 91.8% | 90.5% | 3.6 |

| 模块 | 耗时 (s) |
|------|----------|
| 视频生成/预处理 | 185.5 |
| 锚点生成 | 224.8 |
| CoTracker | 7.41 |
| PnP/RANSAC | 0.204 |
| AnyGrasp | 2.1 |
| IK+平滑 | 0.5 |
| 总延迟 | 420.5 |

消融显示，刚性过滤在 Sweeping 上提升最大（60%→80%），印证长时程漂移场景下验证机制的价值。语义锚点相比随机/均匀采样在存活率（91.8% vs 72.4%）和重投影误差（3.6 px vs 6.7 px）上显著更优。失败分析：80 次试验中 11 次失败，包括 8 次工作空间极限、2 次关键点过度丢失、1 次抓取执行错误。

## 边界与局限

论文明确承认以下边界：深度补偿不处理相机 X–Y 平面内的横向位移，若对象在执行中大幅移动（尤其图像平面内），轨迹视为无效需重新初始化；有界深度反馈不是全在线视觉伺服或任务级重规划。此外，稀疏 PnP 对无纹理、对称或锚点分布不佳区域可能不稳定，且依赖生成视频质量——对严重变形、错误任务语义或强遮挡的序列可能拒绝或失败。论文未明确提及对 VLM/生成模型质量的定量依赖、锚点数量固定的敏感性分析，以及多任务泛化到非桌面场景的表现。

## 工程启示

复现或采用此框架时，优先核对以下环节：**锚点质量是系统命脉**——语义锚点的存活率（91.8%）与重投影误差（3.6 px）直接决定验证通过率，建议先验证 VLM 提示与 SAM 分割在目标对象上的稳定性，再投入完整流程。**PnP 的 RANSAC 内点阈值（约 8 像素）与接受阈值（ē_n < 5 px）需根据相机内参和深度噪声标定**，过严会拒绝有效运动，过松则引入漂移。**IK 检查的阈值（位置 0.01 m，方向 0.40 rad）对 RM75 的 URDF 精度敏感**，建议先用仿真验证关节解连续性。最易踩坑的是**深度补偿的 λ_d 与 d_max 调节**——λ_d ∈ [0.3, 0.5] 范围看似宽，但实际需按对象尺寸和相机距离微调，过大易振荡，过小则补偿失效。总延迟 420.5 s 中锚点生成占 224.8 s，若需实时性，应优先优化此模块（如并行化 VLM 调用或减少候选视频数）。

## 参考
- http://arxiv.org/abs/2607.09191v1

## 개요
비디오 생성은 로봇 조작을 위한 시각적 운동 사전을 제공할 수 있지만, 시각적 합리성이 물리적 실행 가능성을 보장하지는 않습니다. 비디오에는 측정 기하학, 파지 접지, 로봇 운동학적 실현 가능성 및 실행 중 피드백이 부족하기 때문입니다. GenVid2Robot은 실제 첫 프레임 RGB-D 관측에서 작업 관련 의미론적 앵커를 샘플링하고, 생성된 비디오 후보 프레임에서 이러한 앵커를 추적하며, 희소 상대 SE(3) 모델을 사용하여 2D 운동이 첫 프레임 RGB-D 앵커로 설명될 수 있는지 검증함으로써 기하학적으로 일관된 운동을 선별합니다. 수용된 상대 운동은 이후 마스크 제약 파지로 선택된 실제 파지 시점의 TCP 포즈에 적용되어, 시각적 운동 사전 및 물리적 파지 구성과 일치하는 파지 조건 실행 궤적을 생성합니다. RGB-D 노이즈, 캘리브레이션 잔차 및 접촉 변위로 인한 실행 편차를 줄이기 위해, 프레임워크는 완전한 온라인 재계획에 의존하지 않고 국소 깊이 방향 오류를 수정하는 유계 깊이 보상 모듈을 도입합니다.

## 핵심 내용
### 방법 개요
GenVid2Robot의 핵심 아이디어는 생성된 비디오를 직접적인 시연이 아닌 불확실한 시각적 운동 가설로 간주하는 것입니다. 그 흐름은 다음과 같습니다:
- **의미론적 앵커 샘플링**: 실제 첫 프레임 RGB-D 관측에서 작업 지시에 따라 작업 관련 의미론적 앵커(예: 객체 키포인트)를 샘플링합니다.
- **앵커 추적 및 기하학적 검증**: 생성된 비디오 후보 프레임에서 이러한 앵커를 추적하고, 희소 상대 SE(3) 모델을 통해 2D 운동이 첫 프레임 RGB-D 앵커와 기하학적으로 일관되는지 검증합니다. 검증을 통과한 운동만 로봇으로 전송됩니다.
- **파지 조건 궤적 생성**: 수용된 상대 운동은 마스크 제약 파지로 선택된 실제 파지 시점의 TCP 포즈에 적용되어, 궤적이 시각적 운동 사전과 물리적 파지 구성 모두에 부합하도록 보장합니다.

### 핵심 모듈
- **마스크 제약 파지**: 객체 마스크를 사용하여 파지 지점 선택을 제약하고, 파지 포즈가 객체 기하학과 정렬되도록 보장합니다.
- **유계 깊이 보상 모듈**: RGB-D 노이즈, 캘리브레이션 잔차 및 접촉 변위로 인한 깊이 방향 오류를 대상으로, 이 모듈은 완전한 온라인 재계획 없이 국소 범위에서 깊이 오류를 수정합니다.

### 실험 설정 및 결과
- **실험 플랫폼**: 다양한 객체와 작업 지시를 포함하는 실제 로봇 조작 시나리오.
- **핵심 지표**: GenVid2Robot은 시각적 운동 사전을 희소 측정 기하학, 파지 제약, 로봇 실현 가능성 검사 및 유계 실행 피드백과 결합하여, 생성 비디오 기반 조작의 성공률과 신뢰성을 크게 향상시켰습니다. 실험에 따르면 직접 궤적 재생은 기하학적 일관성 부족으로 실패율이 높은 반면, GenVid2Robot의 기하학적 검증 및 보상 메커니즘은 실행 편차를 효과적으로 줄였습니다.
