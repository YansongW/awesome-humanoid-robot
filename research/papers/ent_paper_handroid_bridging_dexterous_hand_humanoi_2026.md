---
$id: ent_paper_handroid_bridging_dexterous_hand_humanoi_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Handroid: Bridging Dexterous Hand and Humanoid'
  zh: 'Handroid: Bridging Dexterous Hand and Humanoid'
  ko: 'Handroid: Bridging Dexterous Hand and Humanoid'
summary:
  en: 'Dexterous hands and humanoid robots are typically developed as distinct embodiments: the former enable contact-rich
    manipulation at the object scale, whereas the latter provide mobility and whole-body interaction in human-centered environments.
    We introduce \textbf{Handroid}, a desktop-scale dual-embodiment robot that integrates both capabilities within a single
    reconfigurable platform. Handroid.'
  zh: Handroid 是一个 27-DoF 的桌面级双实体机器人系统，可在灵巧手（20 DoF）与桌面人形（25 DoF）之间通过棱柱关节重构，由加州大学团队开发。其核心贡献在于提出"形态复用"理念——同一物理本体通过重构承担操作与移动两种角色，并配套了从遥操作、扩散策略抓取到
    RL 全身运动控制的完整算法栈，为跨形态机器人学习提供了统一研究平台。
  ko: 'Dexterous hands and humanoid robots are typically developed as distinct embodiments: the former enable contact-rich
    manipulation at the object scale, whereas the latter provide mobility and whole-body interaction in human-centered environments.
    We introduce \textbf{Handroid}, a desktop-scale dual-embodiment robot that integrates both capabilities within a single
    reconfigurable platform. Handroid.'
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
- handroid
- bridging
- dexterous
- hand
- humanoi
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-08-05'
  confidence: medium
  notes: 'Catch-up sweep 2026-08-05, source channel(s): arxiv_scan. Full text from arXiv (HTML or PDF); zh six-section interpretation
    by DeepSeek (deepseek-chat, T<=0.3) with fact guardrails.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2607.16187 Handroid: Bridging Dexterous Hand and Humanoid'
  url: https://arxiv.org/abs/2607.16187
  date: '2026-07-17'
  accessed_at: '2026-08-05'
---

## 概述

Handroid 是一个 27-DoF 的桌面级双实体机器人系统，可在灵巧手（20 DoF）与桌面人形（25 DoF）之间通过棱柱关节重构，由加州大学团队开发。其核心贡献在于提出"形态复用"理念——同一物理本体通过重构承担操作与移动两种角色，并配套了从遥操作、扩散策略抓取到 RL 全身运动控制的完整算法栈，为跨形态机器人学习提供了统一研究平台。

## 它改变了什么

移动性与灵巧性在机器人领域长期被割裂对待：灵巧手安装在固定基座上追求接触精度，人形机器人则优先保证运动稳定性而牺牲手部功能。这种"形态即功能"的固化思维导致两个子领域各自为政，缺乏统一的物理平台来研究跨形态的技能迁移与协调控制。Handroid 真正改变的是这一范式——它用一套可重构硬件证明，手指和腿在关节布置、接触几何、驱动方式上存在深层结构同构性，同一模块在不同实体中承担不同功能角色是可行的。

这一设计决策的深层意义在于：它把"形态"从固定属性变成了可操作变量。研究者可以在同一物理系统上对比灵巧操作与全身运动控制，甚至探索跨实体策略迁移——这在以往需要两套完全不同的硬件才能实现。同时，桌面级尺寸（0.33 m，2.05 kg）和商用 Dynamixel 执行器大幅降低了复现门槛，使双实体机器人学习从"实验室奢侈品"变为可广泛开展的研究方向。

## 方法拆解

### 硬件重构机制
- 关节 9 和 26 为棱柱关节，采用齿条-小齿轮传动，将旋转转换为沿刚性直线导轨的平移
- 从人形切换到灵巧手时，模块 II 和 V 向下平移至手配置位置，分别作为食指和小指模块
- 切换仅需受控模块重定位，无需更换硬件

### 灵巧操作算法栈
- **遥操作**：Apple Vision Pro 捕获 22 个手部关键点，经 AnyTeleop 重定向框架和 DexPilot 风格目标函数映射到 Handroid 和 Franka Research 3，组合循环稳定运行在 20 Hz 以上
- **灵巧抓取**：物体条件扩散策略，PointNet++ 编码物体点云（512 点），MLP 编码本体感觉历史，U-Net 骨干生成动作块（n_obs=2, n_action=8），部署时用时间集成平滑
- **手内重定向**：IsaacLab + PPO 训练，策略观察手部关节位置和命令历史，输出 PD 目标；Sim-to-real 随机化接触摩擦、执行器参数、物体质量和尺度

### 人形全身运动控制
- **ZMP 步态规划**：固定高度 LIPM 模型 p_zmp = c_xy − (h_com/g)·c̈_xy，LQR 预览控制器权衡 ZMP 跟踪与 CoM 加速度代价；单支撑/双支撑阶段交替，脚和 CoM 轨迹遵循相同相位调度
- **Mink 差分 IK**：每帧求解加权差分 IK（CoM、双脚位姿、躯干稳定、姿态正则化），支撑脚权重高于摆动脚，每帧从上一帧热启动，12 次迭代细化
- **RL 跟踪策略**：actor 接收参考关节状态 + 实测基座角速度 + 五步历史，critic 额外接收特权观测（锚点偏移、仿真基座速度）；奖励核宽度：根位置 0.03 m、根姿态 0.15 rad、身体线速度 0.25 m/s、身体角速度 0.60 rad/s
- **无参考速度控制**：直接以指令平面 CoM 速度和偏航角速率为条件，不调用 ZMP 规划器或 Mink；非对称 actor-critic，critic 接收仿真特权观测（接触状态、脚高度、接触力）；速度跟踪权重 w_v=2, w_ω=2，核宽度 σ_v=0.16 m/s, σ_ω=0.50 rad/s
- **关键帧运动控制**：Viser 编辑器生成关节空间关键帧序列，分段线性插值生成密集轨迹；两条路径——直接硬件执行（Dynamixel 位置指令）或转换为跟踪参考供 RL 训练

## 关键创新

1. **形态可重构的双实体设计**：这是首个在桌面级尺度上实现灵巧手与人形之间无缝重构的系统。27-DoF 中 20 DoF 用于手、25 DoF 用于人形，通过棱柱关节平移实现形态切换，无需更换硬件。这一设计将"形态"从固定属性变为可操作变量，为跨形态技能迁移研究提供了前所未有的实验平台。

2. **统一跟踪管线的多源运动融合**：Handroid 将规划器生成（ZMP+IK）、关键帧作者创作、RL 从零学习三种运动生成方式统一到同一跟踪策略中。所有参考运动共享时间索引序列表示（关节位置/速度、身体位姿/速度），以髋关节连杆为锚点，使不同来源的运动能被同一套闭环策略执行。这消除了传统方法中"每种运动来源需要专用控制器"的碎片化问题。

3. **无参考速度控制与跟踪控制的互补架构**：速度策略直接以运动指令为条件，不依赖时间索引参考，训练和推理时不调用 ZMP 规划器或 Mink；而跟踪策略保留对参考的依赖以利用规划器和关键帧生成的运动。这种双轨设计同时满足"响应式控制"与"参考引导控制"两种需求，且非对称 actor-critic 确保部署时无需特权观测。

## 实验与结果

### 灵巧抓取成功率（表 1，每物体 10 次尝试）

| 物体 | 成功率 |
|------|--------|
| Apple | 8/10 |
| Band Aid | 6/10 |
| Canister | 8/10 |
| Chip Tube | 9/10 |
| Cocoa Box | 7/10 |
| Earphone | 6/10 |
| Glove Box | 7/10 |
| Sheep | 9/10 |
| Sprayer | 5/10 |
| WD-40 | 7/10 |
| **平均** | **72%** |

### 人形运动控制（模拟）
- RL 跟踪：关节位置跟踪误差 **0.12 rad**，身体位置跟踪误差 **0.0019 m**
- RL 速度控制：前向速度 0.20 m/s 指令下，速度跟踪误差 **0.052 m/s**；学习步态表现出相对较短的步幅和高步频

### 真实机器人演示
- 关键帧运动：6 个手动编写关键帧构建行走循环，相邻间隔 0.045 s；演示了俯卧撑、引体向上、拾放任务、前进/后退行走、转身和侧步
- 长时程任务：完整流程包括灵巧手→人形切换、人形绕过障碍推盒、切换回灵巧手抓取瓶子放入盒子，电磁法兰提供约 180 N 保持力

### 关键观察
- 72% 的抓取成功率在 10 物体、姿态随机化条件下表现合理，但 Sprayer（5/10）和 Band Aid/Earphone（6/10）等小物体成功率偏低，反映接触几何对抓取鲁棒性的影响
- 模拟中 RL 跟踪误差远小于速度控制误差（0.0019 m vs 0.052 m/s），说明参考引导控制精度更高，但速度控制无需规划器，响应更直接

## 边界与局限

论文未明确列出作者承认的局限性，但从方法描述可推断以下边界：

- **真实人形 RL 策略未部署**：RL 跟踪和速度控制仅在模拟中评估（MuJoCo），真实人形实体上未验证闭环运动控制效果，Sim-to-real 差距未知
- **手内重定向仅定性评估**：真实机器人上手内重定向策略无成功率定量指标，仅演示了立方体朝向匹配
- **无跨实体策略迁移实验**：未验证灵巧手训练的策略能否迁移到人形实体（或反之），这是"形态复用"理念的核心假设之一
- **速度控制步态质量有限**：学习步态步幅短、步频高，与自然行走有差距，可能限制其在复杂地形上的适用性
- **关键帧直接执行无闭环反馈**：硬件直接执行路径不经过 RL 策略，对扰动和地形变化无自适应能力

## 工程启示

复现或基于 Handroid 开展研究时，以下工程细节最值得关注：

1. **先核对关节命令接口缩放因子**：式 3 中 s_j = 0.25 对所有受控下肢关节，这一缩放直接影响 RL 策略输出的有效动作范围。若更换执行器或关节配置，需重新标定该参数，否则策略输出可能超出执行器物理极限。

2. **跟踪奖励核宽度是调参核心**：根位置 0.03 m、根姿态 0.15 rad、身体线速度 0.25 m/s、身体角速度 0.60 rad/s 这些值决定了跟踪精度与动作平滑度的权衡。若目标运动速度更快或振幅更大，需相应放宽核宽度，否则策略会因过度惩罚而收敛到保守行为。

3. **速度控制策略的终止条件需谨慎设置**：倾斜超过 70° 即终止回合，这一阈值对桌面级机器人可能过于宽松——0.33 m 高的机器人倾斜 70° 时重心已严重偏移，可能导致不可恢复的姿态。建议根据实际硬件重心高度重新计算安全倾斜角。

4. **关键帧时间间隔是行走质量的关键**：行走用 0.045 s 间隔，这一值决定了插值轨迹的平滑度和执行速度。间隔过短会导致执行器跟踪滞后，过长则运动生硬。建议根据执行器带宽（Dynamixel XC330 系列）和关节负载实测调整。

5. **电磁法兰保持力（180 N）是长时程任务的瓶颈**：该力值足以支撑抓取和推盒，但若任务涉及较大冲击载荷（如快速转身或跌倒恢复），需验证法兰连接可靠性。建议在任务设计中避免对法兰施加剪切力。

6. **最易踩坑处：Sim-to-real 随机化参数未公开**：论文未给出接触摩擦、执行器参数、物体质量/尺度的具体随机化范围。复现手内重定向策略时，这些参数直接影响迁移成功率，建议从较窄范围（±10%）开始逐步扩大。

## Overview
Dexterous hands and humanoid robots are typically developed as distinct embodiments: the former enable contact-rich manipulation at the object scale, whereas the latter provide mobility and whole-body interaction in human-centered environments. We introduce \textbf{Handroid}, a desktop-scale dual-embodiment robot that integrates both capabilities within a single reconfigurable platform. Handroid reuses one 27-DoF electromechanical body as either a dexterous hand or a desktop humanoid, measuring 0.33 m in height and 2.05 kg in weight. In the dexterous hand embodiment, 20 DoFs form an anthropomorphic hand closely matching the kinematic structure of the human hand. In the humanoid embodiment, the same articulated modules are reconfigured into a humanoid with a head, arms, and legs, including a 12-DoF lower-limb structure for locomotion and whole-body motion. Handroid further provides a unified control and learning framework supporting hand teleoperation, dexterous grasping, in-hand manipulation, humanoid locomotion, gait generation, and interactive motion authoring. We validate the platform through real-world dexterous manipulation, reinforcement-learning-based locomotion, keyframe motion deployment, and a long-horizon task involving embodiment reconfiguration, locomotion, docking, and dexterous pick-and-place. These results position Handroid as a compact and reproducible platform for advancing morphology-reconfigurable robotics and cross-embodiment robot learning.

## 参考
- https://arxiv.org/abs/2607.16187

## 개요

Handroid는 27-DoF 데스크톱급 이중 실체 로봇 시스템으로, 정교한 손(20 DoF)과 데스크톱 휴머노이드(25 DoF) 사이를 프리즘 관절을 통해 재구성할 수 있으며, 캘리포니아 대학 팀이 개발했습니다. 핵심 기여는 "형태 재사용" 개념을 제안한 것입니다—동일한 물리적 본체가 재구성을 통해 조작과 이동이라는 두 가지 역할을 수행하며, 원격 조작, 확산 정책 파지부터 RL 전신 운동 제어까지의 완전한 알고리즘 스택을 갖추어, 교차 형태 로봇 학습을 위한 통합 연구 플랫폼을 제공합니다.

## 무엇을 바꾸었는가

이동성과 정교함은 로봇 분야에서 오랫동안 분리되어 취급되어 왔습니다: 정교한 손은 고정 기반 위에 장착되어 접촉 정밀도를 추구하고, 휴머노이드 로봇은 운동 안정성을 우선시하여 손 기능을 희생합니다. 이러한 "형태가 곧 기능"이라는 고정 관념은 두 하위 분야가 각자 독립적으로 운영되게 하여, 교차 형태 기술 전이와 조정 제어를 연구할 통일된 물리적 플랫폼이 부재했습니다. Handroid가 실제로 바꾼 것은 바로 이 패러다임입니다—재구성 가능한 하드웨어 한 세트로 손가락과 다리가 관절 배치, 접촉 기하학, 구동 방식에서 깊은 구조적 동형성을 가지며, 동일한 모듈이 다른 실체에서 다른 기능적 역할을 수행할 수 있음을 증명했습니다.

이 설계 결정의 심층적 의미는 "형태"를 고정 속성에서 조작 가능한 변수로 바꾼 것입니다. 연구자는 동일한 물리적 시스템에서 정교한 조작과 전신 운동 제어를 비교할 수 있으며, 심지어 교차 실체 정책 전이를 탐구할 수 있습니다—이는 이전에는 두 세트의 완전히 다른 하드웨어가 필요했던 것입니다. 동시에 데스크톱급 크기(0.33 m, 2.05 kg)와 상용 Dynamixel 액추에이터는 재현 장벽을 크게 낮추어, 이중 실체 로봇 학습을 "실험실 사치품"에서 널리 수행 가능한 연구 방향으로 전환했습니다.

## 방법 분석

### 하드웨어 재구성 메커니즘
- 관절 9와 26은 프리즘 관절로, 랙-피니언 변속을 사용하여 회전을 강체 직선 레일을 따른 병진으로 변환합니다
- 휴머노이드에서 정교한 손으로 전환할 때, 모듈 II와 V가 아래로 손 구성 위치로 병진하여 각각 검지와 소지 모듈로 작동합니다
- 전환은 제어된 모듈 재배치만 필요하며 하드웨어 교체가 필요 없습니다

### 정교한 조작 알고리즘 스택
- **원격 조작**: Apple Vision Pro가 22개 손 키포인트를 캡처하고, AnyTeleop 리타겟팅 프레임워크와 DexPilot 스타일 목적 함수를 통해 Handroid와 Franka Research 3에 매핑하며, 결합 루프가 20 Hz 이상에서 안정적으로 작동합니다
- **정교한 파지**: 객체 조건 확산 정책, PointNet++가 객체 포인트 클라우드(512 포인트)를 인코딩하고, MLP가 고유 수용 감각 이력을 인코딩하며, U-Net 백본이 액션 블록(n_obs=2, n_action=8)을 생성하고, 배포 시 시간 통합으로 평활화합니다
- **손 내부 리타겟팅**: IsaacLab + PPO 훈련, 정책이 손 관절 위치와 명령 이력을 관찰하고 PD 목표를 출력합니다; Sim-to-real은 접촉 마찰, 액추에이터 파라미터, 객체 질량과 스케일을 무작위화합니다

### 휴머노이드 전신 운동 제어
- **ZMP 보행 계획**: 고정 높이 LIPM 모델 p_zmp = c_xy − (h_com/g)·c̈_xy, LQR 예측 제어기가 ZMP 추적과 CoM 가속도 비용을 절충합니다; 단일 지지/이중 지지 단계가 교대하고, 발과 CoM 궤적이 동일한 위상 스케줄을 따릅니다
- **Mink 차분 IK**: 매 프레임 가중 차분 IK(CoM, 양발 자세, 몸통 안정화, 자세 정규화)를 해결하고, 지지 발 가중치가 스윙 발보다 높으며, 매 프레임 이전 프레임에서 웜 스타트하고 12회 반복으로 정제합니다
- **RL 추적 정책**: actor가 참조 관절 상태 + 측정된 베이스 각속도 + 5단계 이력을 수신하고, critic은 추가로 특권 관찰(앵커 오프셋, 시뮬레이션 베이스 속도)을 수신합니다; 보상 커널 폭: 루트 위치 0.03 m, 루트 자세 0.15 rad, 몸체 선속도 0.25 m/s, 몸체 각속도 0.60 rad/s
- **무참조 속도 제어**: 명령된 평면 CoM 속도와 요 각속도에 직접 조건화하고, ZMP 계획기나 Mink를 호출하지 않습니다; 비대칭 actor-critic, critic은 시뮬레이션 특권 관찰(접촉 상태, 발 높이, 접촉 힘)을 수신합니다; 속도 추적 가중치 w_v=2, w_ω=2, 커널 폭 σ_v=0.16 m/s, σ_ω=0.50 rad/s
- **키프레임 운동 제어**: Viser 편집기가 관절 공간 키프레임 시퀀스를 생성하고, 조각별 선형 보간으로 밀집 궤적을 생성합니다; 두 가지 경로—직접 하드웨어 실행(Dynamixel 위치 명령) 또는 RL 훈련용 추적 참조로 변환

## 핵심 혁신

1. **형태 재구성 가능한 이중 실체 설계**: 데스크톱급 스케일에서 정교한 손과 휴머노이드 사이의 원활한 재구성을 실현한 최초의 시스템입니다. 27-DoF 중 20 DoF는 손에, 25 DoF는 휴머노이드에 사용되며, 프리즘 관절 병진을 통해 형태 전환을 수행하고 하드웨어 교체가 필요 없습니다. 이 설계는 "형태"를 고정 속성에서 조작 가능한 변수로 바꾸어, 교차 형태 기술 전이 연구에 전례 없는 실험 플랫폼을 제공합니다.

2. **통합 추적 파이프라인의 다중 소스 운동 융합**: Handroid는 계획기 생성(ZMP+IK), 키프레임 저작, RL 처음부터 학습이라는 세 가지 운동 생성 방식을 동일한 추적 정책으로 통합합니다. 모든 참조 운동은 시간 인덱스 시퀀스 표현(관절 위치/속도, 몸체 자세/속도)을 공유하고, 엉덩이 링크를 앵커로 사용하여 서로 다른 소스의 운동이 동일한 폐루프 정책으로 실행될 수 있게 합니다. 이는 기존 방식의 "각 운동 소스마다 전용 컨트롤러 필요"라는 파편화 문제를 제거합니다.

3. **무참조 속도 제어와 추적 제어의 상보적 아키텍처**: 속도 정책은 운동 명령에 직접 조건화하고 시간 인덱스 참조에 의존하지 않으며, 훈련 및 추론 시 ZMP 계획기나 Mink를 호출하지 않습니다; 반면 추적 정책은 계획기와 키프레임이 생성한 운동을 활용하기 위해 참조에 대한 의존성을 유지합니다. 이러한 이중 트랙 설계는 "반응형 제어"와 "참조 유도 제어"라는 두 가지 요구를 동시에 충족하며, 비대칭 actor-critic은 배포 시 특권 관찰이 필요 없음을 보장합니다.

## 실험과 결과

### 정교한 파지 성공률 (표 1, 객체당 10회 시도)

| 객체 | 성공률 |
|------|--------|
| Apple | 8/10 |
| Band Aid | 6/10 |
| Canister | 8/10 |
| Chip Tube | 9/10 |
| Cocoa Box | 7/10 |
| Earphone | 6/10 |
| Glove Box | 7/10 |
| Sheep | 9/10 |
| Sprayer | 5/10 |
| WD-40 | 7/10 |
| **평균** | **72%** |

### 휴머노이드 운동 제어 (시뮬레이션)
- RL 추적: 관절 위치 추적 오차 **0.12 rad**, 몸체 위치 추적 오차 **0.0019 m**
- RL 속도 제어: 전방 속도 0.20 m/s 명령에서 속도 추적 오차 **0.052 m/s**; 학습된 보행은 상대적으로 짧은 보폭과 높은 보행 빈도를 보임

### 실제 로봇 데모
- 키프레임 운동: 6개의 수동 작성 키프레임으로 보행 루프 구성, 인접 간격 0.045 s; 팔굽혀펴기, 턱걸이, 집기-놓기 작업, 전진/후진 보행, 회전 및 옆걸음 데모
- 장시간 작업: 전체 흐름은 정교한 손→휴머노이드 전환, 휴머노이드가 장애물을 우회하여 상자 밀기, 정교한 손으로 전환하여 병을 집어 상자에 넣기, 전자기 플랜지가 약 180 N 유지력을 제공

### 핵심 관찰
- 10개 객체, 자세 무작위화 조건에서 72% 파지 성공률은 합리적이지만, Sprayer(5/10)와 Band Aid/Earphone(6/10) 같은 작은 객체는 성공률이 낮아 접촉 기하학이 파지 견고성에 미치는 영향을 반영합니다
- 시뮬레이션에서 RL 추적 오차는 속도 제어 오차보다 훨씬 작아(0.0019 m vs 0.052 m/s), 참조 유도 제어의 정밀도가 더 높지만, 속도 제어는 계획기가 필요 없어 응답이 더 직접적임을 보여줍니다

## 경계와 한계

논문은 저자가 인정한 한계를 명시적으로 나열하지 않았지만, 방법 설명에서 다음 경계를 추론할 수 있습니다:

- **실제 휴머노이드 RL 정책 미배포**: RL 추적과 속도 제어는 시뮬레이션(MuJoCo)에서만 평가되었고, 실제 휴머노이드 실체에서 폐루프 운동 제어 효과가 검증되지 않아 Sim-to-real 격차가 알려지지 않았습니다
- **손 내부 리타겟팅은 정성적 평가만**: 실제 로봇에서 손 내부 리타겟팅 정책은 성공률 정량 지표가 없고, 큐브 방향 정합 데모만 수행되었습니다
- **교차 실체 정책 전이 실험 없음**: 정교한 손에서 훈련된 정책이 휴머노이드 실체로 전이될 수 있는지(또는 그 반대) 검증되지 않았으며, 이는 "형태 재사용" 개념의 핵심 가정 중 하나입니다
- **속도 제어 보행 품질 제한**: 학습된 보행은 보폭이 짧고 보행 빈도가 높아 자연스러운 보행과 차이가 있으며, 복잡한 지형에서의 적용 가능성을 제한할 수 있습니다
- **키프레임 직접 실행은 폐루프 피드백 없음**: 하드웨어 직접 실행 경로는 RL 정책을 거치지 않아 교란과 지형 변화에 대한 적응 능력이 없습니다

## 공학적 시사점

Handroid를 재현하거나 기반으로 연구를 수행할 때 다음 공학적 세부 사항이 가장 주목할 가치가 있습니다:

1. **관절 명령 인터페이스 스케일링 팩터 먼저 확인**: 식 3의 s_j = 0.25는 모든 제어되는 하지 관절에 적용되며, 이 스케일링은 RL 정책 출력의 유효 동작 범위에 직접 영향을 미칩니다. 액추에이터나 관절 구성을 변경하면 이 파라미터를 다시 보정해야 하며, 그렇지 않으면 정책 출력이 액추에이터 물리적 한계를 초과할 수 있습니다.

2. **추적 보상 커널 폭이 튜닝의 핵심**: 루트 위치 0.03 m, 루트 자세 0.15 rad, 몸체 선속도 0.25 m/s, 몸체 각속도 0.60 rad/s 값은 추적 정밀도와 동작 평활도의 절충을 결정합니다. 목표 운동 속도가 더 빠르거나 진폭이 더 크면 커널 폭을 상응하게 완화해야 하며, 그렇지 않으면 정책이 과도한 페널티로 인해 보수적 행동으로 수렴합니다.

3. **속도 제어 정책의 종료 조건을 신중히 설정**: 기울기가 70°를 초과하면 에피소드가 종료되는데, 이 임계값은 데스크톱급 로봇에 너무 관대할 수 있습니다—0.33 m 높이의 로봇이 70° 기울면 무게 중심이 심각하게 편향되어 회복 불가능한 자세가 될 수 있습니다. 실제 하드웨어 무게 중심 높이를 기준으로 안전 기울기 각도를 다시 계산하는 것이 좋습니다.

4. **키프레임 시간 간격이 보행 품질의 핵심**: 보행에 0.045 s 간격을 사용하며, 이 값은 보간 궤적의 평활도와 실행 속도를 결정합니다. 간격이 너무 짧으면 액추에이터 추적 지연이 발생하고, 너무 길면 운동이 뻣뻣해집니다. 액추에이터 대역폭(Dynamixel XC330 시리즈)과 관절 부하 실측을 기반으로 조정하는 것이 좋습니다.

5. **전자기 플랜지 유지력(180 N)이 장시간 작업의 병목**: 이 힘 값은 파지와 상자 밀기에 충분하지만, 작업이 큰 충격 하중(빠른 회전이나 낙하 회복 등)을 포함하면 플랜지 연결 신뢰성을 검증해야 합니다. 작업 설계에서 플랜지에 전단력을 가하지 않도록 하는 것이 좋습니다.

6. **가장 함정에 빠지기 쉬운 부분: Sim-to-real 무작위화 파라미터 미공개**: 논문은 접촉 마찰, 액추에이터 파라미터, 객체 질량/스케일의 구체적 무작위화 범위를 제공하지 않습니다. 손 내부 리타겟팅 정책을 재현할 때 이러한 파라미터는 전이 성공률에 직접 영향을 미치므로, 좁은 범위(±10%)에서 시작하여 점진적으로 확대하는 것이 좋습니다.
