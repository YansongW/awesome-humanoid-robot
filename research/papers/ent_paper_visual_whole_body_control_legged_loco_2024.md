---
$id: ent_paper_visual_whole_body_control_legged_loco_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Visual Whole-Body Control for Legged Loco-Manipulation
  zh: Visual Whole-Body Control for Legged Loco-Manipulation
  ko: Visual Whole-Body Control for Legged Loco-Manipulation
summary:
  en: We study the problem of mobile manipulation using legged robots equipped with an arm, namely legged loco-manipulation.
    The robot legs, while usually utilized for mobility, offer an opportunity to amplify the manipulation capabilities by
    conducting whole-body control. That is, the robot can control the legs and the arm at the same time to extend its workspace.
    We propose a framework that can.
  zh: 本文提出 Visual Whole-Body Control (VBC)，一个用于四足机器人移动操作的分层学习框架，由低层全身目标到达策略和高层视觉任务规划策略组成。作者在仿真中通过三阶段训练（RL 低层、RL 特权教师、DAgger
    蒸馏学生）实现完全自主的视觉抓取，并直接部署到 Unitree B1 + Z1 真实平台。核心贡献在于证明了分层架构结合全身行为（而非固定基座）能显著扩展操作工作空间，并实现了无需真实世界微调的 Sim2Real 迁移。
  ko: We study the problem of mobile manipulation using legged robots equipped with an arm, namely legged loco-manipulation.
    The robot legs, while usually utilized for mobility, offer an opportunity to amplify the manipulation capabilities by
    conducting whole-body control. That is, the robot can control the legs and the arm at the same time to extend its workspace.
    We propose a framework that can.
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
- visual
- whole
- body
- control
- legged
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): xiaoze_P043. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: arXiv:2403.16967 Visual Whole-Body Control for Legged Loco-Manipulation
  url: https://arxiv.org/abs/2403.16967
  date: '2024-03-25'
  accessed_at: '2026-08-05'
---

## 概述

本文提出 Visual Whole-Body Control (VBC)，一个用于四足机器人移动操作的分层学习框架，由低层全身目标到达策略和高层视觉任务规划策略组成。作者在仿真中通过三阶段训练（RL 低层、RL 特权教师、DAgger 蒸馏学生）实现完全自主的视觉抓取，并直接部署到 Unitree B1 + Z1 真实平台。核心贡献在于证明了分层架构结合全身行为（而非固定基座）能显著扩展操作工作空间，并实现了无需真实世界微调的 Sim2Real 迁移。

## 它改变了什么

这项工作的真正改变在于将四足机器人的腿部从“移动执行器”重新定义为“全身操作执行器”的一部分。此前基于学习的四足工作（如视觉避障、爬楼梯）只关注 locomotion，而移动操作系统（Zhang et al., Yokoyama et al.）均使用默认低层控制器，机器人身体高度固定，无法适应不同高度的物体。VBC 通过训练一个能跟踪任意末端执行器目标并同时调整身体姿态的低层策略，打破了这一限制——机器人可以弯曲前腿去捡地面物体，也可以站直去够桌面物体，这是对“操作工作空间”的实质性扩展。

另一个关键改变是证明了端到端学习在此任务上不可行（Non-Hierarchical 基线成功率 0.0%），而分层训练（低层 RL + 高层 RL + 蒸馏）是可行路径。这为后续四足操作研究提供了重要的架构选择依据：与其强行端到端，不如将问题分解为“如何到达”和“去哪里”两个可独立优化的子问题。

## 方法拆解

### 低层策略：全身目标到达
- **命令空间**：$\mathbf{b}_t = [\mathbf{p}^{\text{cmd}}, \mathbf{o}^{\text{cmd}}, v_{\text{lin}}^{\text{cmd}}, \omega_{\text{yaw}}^{\text{cmd}}]$，其中末端执行器位置命令在高度不变坐标系中采样，确保轨迹位于球面上，避免受机器人高度影响。
- **观测**：90 维向量，包含基座状态、手臂/腿部关节状态、上一步动作、环境潜变量 $z_t \in \mathbb{R}^{20}$、步态时序参考。
- **动作**：输出 12 个腿部关节目标角（PD 控制），手臂通过 IK 求解器 $\Delta\theta = J^T(JJ^T)^{-1}e$ 跟踪末端位姿。
- **训练**：PPO + 正则化在线适应 (ROA)。损失函数为：
$$L = -L^{PPO} + \lambda\|z^\mu - \text{sg}[z^\phi]\|_2 + \|\text{sg}[z^\mu] - z^\phi\|_2$$
其中 $\lambda$ 通过对偶梯度下降优化，RMA 是 $\lambda=0$ 的特例。适应模块 $\phi$ 仅在策略和编码器收敛后开始训练。
- **奖励**：命令跟随（速度跟踪权重 1.0，偏航 0.5）、能量惩罚（关节力矩 -0.00002）、存活奖励、相位奖励（摆动相跟踪位置/速度权重 ±0.2）。

### 高层策略：任务规划
- **特权教师**：观测 1094 维，包含 PointNet++ 预训练的物体形状特征 $z_{\text{shape}} \in \mathbb{R}^{1024}$、物体相对位姿、本体感觉、基座速度。动作 $\mathbf{a}_t = [\mathbf{p}^{\text{cmd}}, \mathbf{v}^{\text{cmd}}, p_{\text{gripper}}] \in \mathbb{R}^9$。
- **奖励**：三阶段（接近、进展、完成）+ 辅助奖励。接近奖励 $r_{\text{approach}} = \min(d_{\text{closest}} - d, 0)$，进展奖励 $r_{\text{progress}} = \min(d - d_{\text{highest}}, 0)$，完成奖励 $r_{\text{completion}} = 1$（物体抬升超过阈值）。辅助奖励包括动作平滑、关节加速度惩罚、身体/夹爪朝向物体。
- **课程**：逐步添加奖励、使用上一步动作命令低层（模拟延迟）、裁剪高层动作输出。

### 视觉学生策略
- **观测**：分割深度图像 + 本体感觉 + 上一步动作。仅用深度而非 RGB，因真实世界 RGB 与仿真差异大。
- **架构**：两层 CNN（核 5 和 3）+ 64 维潜在 + GRU（128 隐藏）+ 两层 MLP（64 隐藏）。
- **训练**：DAgger 在线模仿，先用教师采样初始化（类似 BC），再用学生采样并请求教师纠正。

### 真实世界部署
- 硬件：Unitree B1 + Z1 臂 + 夹爪，两个 RealSense D435，板载 + Jetson Orin。
- 频率：低层 50Hz，高层 10Hz，手臂 >500Hz。
- Sim2Real：随机化相机位置/旋转，深度裁剪最小 0.2m，归一化，TrackingSAM 提供实时分割掩码。

## 关键创新

1. **全身行为作为低层原语**：训练一个通用的全身目标到达策略，而非针对特定任务优化。这使得高层策略可以专注于“去哪里”，而低层负责“如何到达”，包括弯曲腿部、调整身体高度等。这是对现有固定基座方法（Floating Base）的实质性改进，仿真中在 7 类物体上平均成功率提升约 30 个百分点。

2. **高度不变坐标系采样**：在采样末端执行器目标时，以机器人基座为原点、高度不变，确保采样轨迹始终位于球面上。这一设计避免了四足机器人高度变化对采样分布的影响，保证了低层策略在不同身体姿态下的泛化能力。这是一个看似简单但对训练稳定性至关重要的细节。

3. **预训练物体形状特征**：在教师策略中使用 PointNet++ 编码物体点云，提供 1024 维形状特征。消融实验显示，移除该特征后，碗类物体成功率从 74.16% 降至 17.95%，钻类从 56.70% 降至 9.04%，说明形状理解对抓取不同几何物体至关重要。

## 实验与结果

### 仿真结果（表 I，成功率 %，34 个物体，7 类，每类 300 episodes，3 个种子）

| 方法 | 球 | 长盒 | 方盒 | 瓶 | 杯 | 碗 | 钻 |
|------|------|------|------|------|------|------|------|
| **VBC (Ours)** | **70.51** | **51.40** | **76.53** | **69.79** | **81.22** | **74.16** | **56.70** |
| VBC w.o. Shape Feature | 68.44 | 33.88 | 77.72 | 54.18 | 65.42 | 17.95 | 9.04 |
| Floating Base | 49.75 | 32.71 | 56.38 | 45.37 | 25.36 | 27.18 | 12.62 |
| Non-Hierarchical | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

- VBC 在 7 类物体上均优于 Floating Base，尤其在杯（81.22% vs 25.36%）和碗（74.16% vs 27.18%）上差距显著，说明全身行为对低矮/不规则物体的抓取至关重要。
- 移除形状特征后，碗和钻类成功率大幅下降，表明 PointNet++ 特征对几何复杂物体不可或缺。
- Non-Hierarchical 完全失败（0.0%），验证了分层架构的必要性。
- 高度测试（图 10）：VBC 在 0.0m 至 0.6m 七个高度上均优于固定高度浮基基线，且优势在低高度（地面）时最明显。

### 真实世界结果（图 11，14 个物体，3 个高度，每高度 5 次重置）
- VBC 在所有高度设置上优于基线（固定腿部 + 遥操作到达）。
- 基线在 0.0m 和 0.3m 完全失败（默认控制器固定机器人高度，无法够到地面物体），在 0.5m 时 VBC 仍普遍更好。
- 成功定义为物体被抬起高于放置平面 0.1m。

## 边界与局限

作者承认的局限包括：分层管线的复合误差（各模块需连贯精确）、RGBD 相机在反光物体上深度估计不精确、Unitree Z1 夹爪为喙状而非平行夹爪（易推开物体）、TrackingSAM 可能因相机偏移或遮挡丢失跟踪。论文未提及长期部署测试、其他机器人平台验证、室外复杂地形实验（仅在仿真中随机化地形类型），也未报告具体训练步数、学习率、批量大小等超参数。推理频率（低层 50Hz、高层 10Hz）已给出，但未说明端到端延迟对任务成功率的影响。

## 工程启示

复现时需优先核对以下关键点：

1. **低层策略的泛化能力是基础**：先验证低层策略能否在仿真中跟踪任意末端执行器目标（包括地面和桌面高度），再训练高层。若低层失败，高层无论如何优化都无法成功。建议先复现低层奖励权重（速度跟踪 1.0、偏航 0.5、基座高度 -5.0）并确认机器人能稳定小跑。

2. **高度不变坐标系采样是低层训练的关键细节**：若直接在世界坐标系采样目标，机器人高度变化会导致采样分布偏移，训练可能不收敛。务必实现球面采样逻辑。

3. **ROA 的 $\lambda$ 调节**：RMA（$\lambda=0$）是特例，但 ROA 通过拉格朗日乘子动态调节适应模块的约束强度。复现时建议先跑通 RMA 再引入 ROA，否则难以判断性能差异来源。

4. **形状特征不可省略**：若省略 PointNet++ 特征，碗和钻类成功率会从 74%/57% 暴跌至 18%/9%。确保预训练特征在教师训练期间固定（不更新梯度）。

5. **真实世界部署最易踩坑**：深度图像裁剪最小 0.2m（避免近距离低质量数据）、TrackingSAM 的掩码质量直接影响学生策略输入。建议先离线录制真实深度图像，验证分割掩码的稳定性再上机。夹爪为喙状，抓取圆柱形物体时需额外注意姿态控制。

6. **计算资源**：高层学生训练仅 240 个并行环境（因渲染视觉观测需大量 GPU 内存），若资源有限可考虑降低图像分辨率或减少环境数，但需注意可能影响策略泛化。

## Overview
We study the problem of mobile manipulation using legged robots equipped with an arm, namely legged loco-manipulation. The robot legs, while usually utilized for mobility, offer an opportunity to amplify the manipulation capabilities by conducting whole-body control. That is, the robot can control the legs and the arm at the same time to extend its workspace. We propose a framework that can conduct the whole-body control autonomously with visual observations. Our approach, namely Visual Whole-Body Control(VBC), is composed of a low-level policy using all degrees of freedom to track the body velocities along with the end-effector position, and a high-level policy proposing the velocities and end-effector position based on visual inputs. We train both levels of policies in simulation and perform Sim2Real transfer for real robot deployment. We perform extensive experiments and show significant improvements over baselines in picking up diverse objects in different configurations (heights, locations, orientations) and environments.

## 参考
- https://arxiv.org/abs/2403.16967

## 개요

본 논문은 Visual Whole-Body Control (VBC)을 제안한다. 이는 네 발 달린 로봇의 이동 조작을 위한 계층적 학습 프레임워크로, 저수준 전신 목표 도달 정책과 고수준 시각 작업 계획 정책으로 구성된다. 저자들은 시뮬레이션에서 3단계 훈련(저수준 RL, 특권 교사, DAgger 증류 학생)을 통해 완전 자율적인 시각 파지를 구현하고, 이를 Unitree B1 + Z1 실제 플랫폼에 직접 배포한다. 핵심 기여는 계층적 아키텍처가 고정 기반이 아닌 전신 동작과 결합하여 조작 작업 공간을 크게 확장할 수 있음을 입증하고, 실제 세계 미세 조정 없이 Sim2Real 전이를 달성했다는 점이다.

## 무엇을 바꾸었는가

이 작업의 진정한 변화는 네 발 달린 로봇의 다리를 "이동 액추에이터"에서 "전신 조작 액추에이터"의 일부로 재정의한 것이다. 이전의 학습 기반 네 발 달린 연구(예: 시각 장애물 회피, 계단 오르기)는 locomotion에만 초점을 맞췄지만, 이동 조작 시스템(Zhang et al., Yokoyama et al.)은 모두 기본 저수준 컨트롤러를 사용하여 로봇의 몸체 높이가 고정되어 다양한 높이의 물체에 적응할 수 없었다. VBC는 임의의 엔드 이펙터 목표를 추적하면서 동시에 몸체 자세를 조정할 수 있는 저수준 정책을 훈련함으로써 이 제약을 깨뜨린다. 로봇은 앞다리를 구부려 바닥의 물체를 집거나, 몸을 곧게 세워 테이블 위 물체에 닿을 수 있으며, 이는 "조작 작업 공간"의 실질적인 확장이다.

또 다른 핵심 변화는 이 작업에서 종단 간 학습이 불가능하다는 것(Non-Hierarchical 기준 성공률 0.0%)과 계층적 훈련(저수준 RL + 고수준 RL + 증류)이 실행 가능한 경로임을 입증한 것이다. 이는 이후 네 발 달린 조작 연구에 중요한 아키텍처 선택 근거를 제공한다. 즉, 억지로 종단 간으로 가기보다는 문제를 "어떻게 도달할 것인가"와 "어디로 갈 것인가"라는 두 개의 독립적으로 최적화 가능한 하위 문제로 분해하는 것이 낫다.

## 방법 분해

### 저수준 정책: 전신 목표 도달
- **명령 공간**: $\mathbf{b}_t = [\mathbf{p}^{\text{cmd}}, \mathbf{o}^{\text{cmd}}, v_{\text{lin}}^{\text{cmd}}, \omega_{\text{yaw}}^{\text{cmd}}]$, 여기서 엔드 이펙터 위치 명령은 높이 불변 좌표계에서 샘플링되어 궤적이 항상 구면 위에 있도록 보장하며, 로봇 높이의 영향을 받지 않는다.
- **관측**: 90차원 벡터로, 기반 상태, 팔/다리 관절 상태, 이전 단계 동작, 환경 잠재 변수 $z_t \in \mathbb{R}^{20}$, 보행 타이밍 참조를 포함한다.
- **동작**: 12개의 다리 관절 목표 각도(PD 제어)를 출력하고, 팔은 IK 솔버 $\Delta\theta = J^T(JJ^T)^{-1}e$를 통해 엔드 포즈를 추적한다.
- **훈련**: PPO + 정규화 온라인 적응(ROA). 손실 함수는 다음과 같다:
$$L = -L^{PPO} + \lambda\|z^\mu - \text{sg}[z^\phi]\|_2 + \|\text{sg}[z^\mu] - z^\phi\|_2$$
여기서 $\lambda$는 쌍대 경사 하강법으로 최적화되며, RMA는 $\lambda=0$의 특수한 경우이다. 적응 모듈 $\phi$는 정책과 인코더가 수렴한 후에만 훈련을 시작한다.
- **보상**: 명령 추종(속도 추종 가중치 1.0, 요 각도 0.5), 에너지 패널티(관절 토크 -0.00002), 생존 보상, 위상 보상(스윙 위상 위치/속도 추종 가중치 ±0.2).

### 고수준 정책: 작업 계획
- **특권 교사**: 관측 1094차원으로, PointNet++ 사전 훈련된 물체 형상 특징 $z_{\text{shape}} \in \mathbb{R}^{1024}$, 물체 상대 포즈, 고유 감각, 기반 속도를 포함한다. 동작 $\mathbf{a}_t = [\mathbf{p}^{\text{cmd}}, \mathbf{v}^{\text{cmd}}, p_{\text{gripper}}] \in \mathbb{R}^9$.
- **보상**: 3단계(접근, 진행, 완료) + 보조 보상. 접근 보상 $r_{\text{approach}} = \min(d_{\text{closest}} - d, 0)$, 진행 보상 $r_{\text{progress}} = \min(d - d_{\text{highest}}, 0)$, 완료 보상 $r_{\text{completion}} = 1$(물체가 임계값 이상 들어 올려짐). 보조 보상에는 동작 평활화, 관절 가속도 패널티, 몸체/그리퍼가 물체를 향함이 포함된다.
- **커리큘럼**: 보상을 점진적으로 추가하고, 이전 단계 동작 명령을 저수준에 사용(시뮬레이션 지연), 고수준 동작 출력을 클리핑한다.

### 시각 학생 정책
- **관측**: 분할 깊이 이미지 + 고유 감각 + 이전 단계 동작. 실제 세계 RGB와 시뮬레이션의 차이가 크므로 RGB가 아닌 깊이만 사용한다.
- **아키텍처**: 2계층 CNN(커널 5 및 3) + 64차원 잠재 + GRU(128 은닉) + 2계층 MLP(64 은닉).
- **훈련**: DAgger 온라인 모방으로, 먼저 교사 샘플링으로 초기화(BC와 유사)한 후 학생 샘플링으로 교사 수정을 요청한다.

### 실제 세계 배포
- 하드웨어: Unitree B1 + Z1 팔 + 그리퍼, RealSense D435 2개, 온보드 + Jetson Orin.
- 주파수: 저수준 50Hz, 고수준 10Hz, 팔 >500Hz.
- Sim2Real: 카메라 위치/회전 무작위화, 깊이 클리핑 최소 0.2m, 정규화, TrackingSAM이 실시간 분할 마스크 제공.

## 핵심 혁신

1. **전신 동작을 저수준 원시 동작으로**: 특정 작업에 최적화된 것이 아닌 범용 전신 목표 도달 정책을 훈련한다. 이를 통해 고수준 정책은 "어디로 갈 것인가"에 집중하고, 저수준은 "어떻게 도달할 것인가"(다리 구부리기, 몸체 높이 조정 등)를 담당한다. 이는 기존 고정 기반 방법(Floating Base)에 대한 실질적인 개선으로, 시뮬레이션에서 7개 물체 유형에 대해 평균 성공률이 약 30% 포인트 향상되었다.

2. **높이 불변 좌표계 샘플링**: 엔드 이펙터 목표를 샘플링할 때 로봇 기반을 원점으로 하고 높이를 불변으로 유지하여 샘플링 궤적이 항상 구면 위에 있도록 보장한다. 이 설계는 네 발 달린 로봇의 높이 변화가 샘플링 분포에 미치는 영향을 피하고, 다양한 몸체 자세에서 저수준 정책의 일반화 능력을 보장한다. 이는 단순해 보이지만 훈련 안정성에 매우 중요한 세부 사항이다.

3. **사전 훈련된 물체 형상 특징**: 교사 정책에서 PointNet++를 사용하여 물체 포인트 클라우드를 인코딩하고 1024차원 형상 특징을 제공한다. 절제 실험에서 이 특징을 제거하면 그릇 유형의 성공률이 74.16%에서 17.95%로, 드릴 유형이 56.70%에서 9.04%로 감소하여, 다양한 기하학적 물체를 파지하는 데 형상 이해가 중요함을 보여준다.

## 실험 및 결과

### 시뮬레이션 결과(표 I, 성공률 %, 34개 물체, 7개 유형, 유형당 300 에피소드, 3개 시드)

| 방법 | 공 | 긴 상자 | 정사각형 상자 | 병 | 컵 | 그릇 | 드릴 |
|------|------|------|------|------|------|------|------|
| **VBC (Ours)** | **70.51** | **51.40** | **76.53** | **69.79** | **81.22** | **74.16** | **56.70** |
| VBC w.o. Shape Feature | 68.44 | 33.88 | 77.72 | 54.18 | 65.42 | 17.95 | 9.04 |
| Floating Base | 49.75 | 32.71 | 56.38 | 45.37 | 25.36 | 27.18 | 12.62 |
| Non-Hierarchical | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 |

- VBC는 7개 물체 유형 모두에서 Floating Base보다 우수하며, 특히 컵(81.22% vs 25.36%)과 그릇(74.16% vs 27.18%)에서 차이가 크다. 이는 전신 동작이 낮거나 불규칙한 물체의 파지에 중요함을 보여준다.
- 형상 특징을 제거하면 그릇과 드릴 유형의 성공률이 크게 감소하여, PointNet++ 특징이 기하학적으로 복잡한 물체에 필수적임을 나타낸다.
- Non-Hierarchical은 완전히 실패(0.0%)하여 계층적 아키텍처의 필요성을 검증한다.
- 높이 테스트(그림 10): VBC는 0.0m에서 0.6m의 7개 높이 모두에서 고정 높이 부유 기반 기준선보다 우수하며, 낮은 높이(바닥)에서 그 차이가 가장 두드러진다.

### 실제 세계 결과(그림 11, 14개 물체, 3개 높이, 높이당 5회 재설정)
- VBC는 모든 높이 설정에서 기준선(고정 다리 + 원격 조작 도달)보다 우수하다.
- 기준선은 0.0m와 0.3m에서 완전히 실패(기본 컨트롤러가 로봇 높이를 고정하여 바닥 물체에 닿을 수 없음)하며, 0.5m에서도 VBC가 일반적으로 더 우수하다.
- 성공은 물체가 놓인 평면보다 0.1m 이상 들어 올려진 것으로 정의된다.

## 경계 및 한계

저자들이 인정한 한계는 다음과 같다: 계층적 파이프라인의 복합 오류(각 모듈이 일관되고 정밀해야 함), 반사 물체에서 RGBD 카메라의 깊이 추정 부정확성, Unitree Z1 그리퍼가 평행 그리퍼가 아닌 부리 모양(물체를 밀어내기 쉬움), TrackingSAM이 카메라 오프셋이나 가림으로 인해 추적을 잃을 수 있음. 논문은 장기 배포 테스트, 다른 로봇 플랫폼 검증, 실외 복잡 지형 실험(시뮬레이션에서만 지형 유형 무작위화)을 언급하지 않았으며, 구체적인 훈련 스텝 수, 학습률, 배치 크기 등의 하이퍼파라미터도 보고하지 않았다. 추론 주파수(저수준 50Hz, 고수준 10Hz)는 제공되었지만, 종단 간 지연이 작업 성공률에 미치는 영향은 설명되지 않았다.

## 공학적 시사점

재현 시 다음 핵심 사항을 우선적으로 확인해야 한다:

1. **저수준 정책의 일반화 능력이 기초**: 먼저 저수준 정책이 시뮬레이션에서 임의의 엔드 이펙터 목표(바닥 및 테이블 높이 포함)를 추적할 수 있는지 검증한 후 고수준을 훈련한다. 저수준이 실패하면 고수준이 아무리 최적화해도 성공할 수 없다. 저수준 보상 가중치(속도 추종 1.0, 요 각도 0.5, 기반 높이 -5.0)를 먼저 재현하고 로봇이 안정적으로 조깅할 수 있는지 확인하는 것이 좋다.

2. **높이 불변 좌표계 샘플링은 저수준 훈련의 핵심 세부 사항**: 세계 좌표계에서 목표를 직접 샘플링하면 로봇 높이 변화로 인해 샘플링 분포가 이동하여 훈련이 수렴하지 않을 수 있다. 반드시 구면 샘플링 로직을 구현해야 한다.

3. **ROA의 $\lambda$ 조정**: RMA($\lambda=0$)는 특수한 경우이지만, ROA는 라그랑주 승수를 통해 적응 모듈의 제약 강도를 동적으로 조정한다. 재현 시 먼저 RMA를 실행한 후 ROA를 도입하는 것이 좋다. 그렇지 않으면 성능 차이의 원인을 판단하기 어렵다.

4. **형상 특징은 생략할 수 없다**: PointNet++ 특징을 생략하면 그릇과 드릴 유형의 성공률이 74%/57%에서 18%/9%로 급락한다. 교사 훈련 중 사전 훈련된 특징이 고정(그래디언트 업데이트 없음)되도록 보장해야 한다.

5. **실제 세계 배포에서 가장 함정에 빠지기 쉬운 부분**: 깊이 이미지 클리핑 최소 0.2m(근거리 저품질 데이터 방지), TrackingSAM의 마스크 품질이 학생 정책 입력에 직접 영향을 미친다. 먼저 오프라인으로 실제 깊이 이미지를 녹화하고 분할 마스크의 안정성을 검증한 후 로봇에 적용하는 것이 좋다. 그리퍼가 부리 모양이므로 원통형 물체를 파지할 때 자세 제어에 추가 주의가 필요하다.

6. **계산 자원**: 고수준 학생 훈련은 시각 관측 렌더링에 많은 GPU 메모리가 필요하므로 병렬 환경이 240개에 불과하다. 자원이 제한된 경우 이미지 해상도를 낮추거나 환경 수를 줄일 수 있지만, 정책 일반화에 영향을 줄 수 있음에 유의해야 한다.
