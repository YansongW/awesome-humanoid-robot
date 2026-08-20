---
$id: ent_paper_abot_m05_unified_mobility_and_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model'
  zh: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model'
  ko: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model'
summary:
  en: 'arXiv:2607.00678v1 Announce Type: cross Abstract: Mobile manipulation is a key capability for general-purpose robots,
    yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world
    modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation:
    they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under
    supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics,
    suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new
    WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space,
    and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local
    visual state transitions and serve as an bridging action space between video latents and embodiment-specific controls.
    To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations
    and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose
    the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test
    alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation
    benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained
    control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent
    world-action modeling.'
  zh: ABot-M0.5 是一个面向移动操作任务的统一世界动作模型（WAM），由研究团队提出。其核心贡献在于从时间粒度、动作空间和推理一致性三个层面实现对齐，通过引入中间潜在动作、双级 Mixture-of-Transformers 架构和
    dream-forcing 训练策略，显著提升了长程任务成功率和精细控制精度。
  ko: 'arXiv:2607.00678v1 Announce Type: cross Abstract: Mobile manipulation is a key capability for general-purpose robots,
    yet remains challenging for current embodied learning methods. VLA policies are typically reactive and lack explicit world
    modeling, while existing World Action Models (WAMs) are still poorly aligned with the structure of mobile manipulation:
    they operate on coarse video chunks, model entangled navigation-manipulation actions, and train inverse dynamics under
    supervision that does not match autoregressive inference. As a result, they often miss fine-grained contact dynamics,
    suffer from action-distribution conflicts, and accumulate errors over long-horizon rollouts. We propose ABot-M0.5, a new
    WAM built on the insight that mobile manipulation requires alignment at three levels: temporal granularity, action space,
    and train-test consistency. To align temporal granularity, we introduce intermediate latent actions that capture local
    visual state transitions and serve as an bridging action space between video latents and embodiment-specific controls.
    To align action space, we design a dual-level Mixture-of-Transformers architecture that disentangles both modality representations
    and heterogeneous action subspaces such as base movement and arm manipulation. To align inference conditions, we propose
    the dream-forcing training strategy that progressively trains inverse dynamics on model-predicted videos, improving train-test
    alignment and robustness during autoregressive prediction. Experiments on challenging mobile and fine-grained manipulation
    benchmarks demonstrate that ABot-M0.5 achieves state-of-the-art performance in both long-horizon task success and finegrained
    control accuracy. These results highlight the critical importance of granularity-aligned, action-disentangled, and inference-consistent
    world-action modeling.'
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
- abot_m05
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.00678v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1049 chars, DeepSeek). [2026-08-20] body rewritten as full-text six-section deep
    read (scripts/deep_read_cards.py, DeepSeek deepseek-chat T<=0.3, arXiv full text; number whitelist enforced at generation);
    en/ko sections regenerated by translate pipeline.'
sources:
- id: src_001
  type: paper
  title: 'ABot-M0.5: Unified Mobility-and-Manipulation World Action Model (arXiv)'
  url: https://arxiv.org/abs/2607.00678
  date: '2026'
  accessed_at: '2026-07-03'
---
## 概述

ABot-M0.5 是一套基于 3D 打印双臂外骨骼与低成本网络摄像头的跨平台遥操作系统，由论文作者团队提出。其核心贡献在于以约 0.6k 美元成本实现了对拟人手、夹爪、人形与四足等多平台的统一高精度遥操作与模仿学习数据采集，并在目标到达与真实任务模仿学习实验中显著优于 GELLO 基线。

## 它改变了什么

现有遥操作系统（ALOHA、GELLO、AnyTeleop、DexCap）的痛点在于“一平台一硬件”的定制化路径：要么成本高昂（ALOHA 20k、Mobile-ALOHA 32k），要么仅支持单一末端执行器类型，且跨平台迁移时需重新设计机械结构与校准流程。这导致模仿学习数据采集的规模化被硬件碎片化所阻塞——研究者每换一个机器人平台，就要重造一套遥操作设备。

ABot-M0.5 真正改变的是“硬件通用性”与“控制抽象层”的绑定关系。它通过将腕部姿态解耦为外骨骼正运动学计算、手部姿态解耦为视觉关键点检测，使同一套外骨骼硬件能通过软件层面的工作空间映射与模式切换，适配从桌面夹爪到人形手的多种平台。这意味着遥操作系统的成本与复杂度不再随平台数量线性增长，而是收敛为一次性硬件投入加可复用的控制软件栈。

## 方法拆解

### 硬件架构
- 双臂外骨骼：每臂 7 连杆、6 自由度，配腕部与摄像头支架，3D 打印制造。
- 驱动与传感：DYNAMIXEL XL330-M288-T 伺服电机（12 位编码器），UCB2Dynamixel (U2D2) 控制器。
- 视觉：两个低成本网络摄像头，MediaPipe 检测 21 个手部关键点，CPU 实时运行。
- 模块化：磁性连接，穿戴 <30 秒；腕部尺寸即时调整，上下臂长度调整 <2 分钟；同一臂可切换桌面/移动底座，无需重新校准。

### 姿态估计与控制映射
- 腕部姿态：外骨骼编码器读数经正运动学计算，平均误差约 1 mm。
- 手部姿态：MediaPipe 输出 21 关键点，跟踪频率约 27 Hz（可提升至 100 Hz）。
- 位置映射公式：\( \mathbf{x}_{e} = \gamma(\mathbf{x}_{h} - \mathbf{c}_{h}) + \mathbf{c}_{t} \)，其中 \( \gamma \) 为控制比例，\( \mathbf{c}_{h} \) 为人工作空间中心，\( \mathbf{c}_{t} \) 为任务工作空间中心。

### 控制模式
- **Normal Mode**：直接传递末端位置，\( \gamma \) 为机器人与人类工作空间半径比。
- **Mirror Mode**：\( \mathbf{x}_{e}^{mirror} = -\gamma_{e}^{mirror}(\mathbf{x}_{h} - \mathbf{c}_{h}) + \mathbf{c}_{t} \)，用于大型机器人面对面操作。
- **Bimanual Mode**：调整 \( \gamma \) 与 \( \mathbf{c}_{t} \) 使左右手工作空间对齐，避免摄像头碰撞。
- **Gripper Mode**：拇指尖与食指尖距离线性映射到 0 到 1。
- **Hand Mode**：手和指尖运动重定向到机器人手。

### 关键设计决策
- 采用正运动学+逆运动学而非直接关节匹配，以解决工作空间不匹配与控制比例可变性问题。
- 伺服电机绝对零位反馈，一次性校准无需拆卸。
- 集成 gRPC 管道，便于扩展到其他平台（如 Vision Pro）。

## 关键创新

1. **硬件-软件解耦的跨平台架构**：以往系统（如 GELLO）的硬件设计紧密绑定特定机器人构型，而 ABot-M0.5 通过将“腕部姿态”与“手部姿态”分离为独立传感通道，使同一外骨骼可通过软件映射适配人形手、夹爪、四足等多种末端，这是架构层面的创新而非参数调整。

2. **低成本与高精度的平衡**：在约 0.6k 美元成本下实现平均 1 mm 正运动学误差与 3 mm 累积遥操作误差（卷尺延伸任务），打破了“低成本必然低精度”的行业惯性。其关键在于使用 12 位编码器伺服电机配合正运动学计算，而非依赖高成本力传感器或光学动捕。

3. **多模式工作空间映射**：通过 Normal、Mirror、Bimanual、Gripper、Hand 五种模式，将人类操作空间灵活映射到不同机器人工作空间，特别是 Bimanual Mode 中对左右手工作空间的对齐调整，解决了双臂操作中常见的摄像头碰撞与空间冲突问题。

## 实验与结果

### 系统对比（Table 1）
| 系统 | 成本 | 末端执行器支持 | EE 跟踪 |
|------|------|----------------|---------|
| ALOHA | 20k | 夹爪 | 关节 |
| Mobile-ALOHA | 32k | 夹爪 | 关节 |
| GELLO | 0.6k | 夹爪 | 关节 |
| AnyTeleop | 0.3k | 夹爪 | 视觉 |
| DexCap | 4k | 拟人手 | 视觉+IMU |
| ACE | 0.6k | Both | Vision + FK |

### 目标到达实验（Table 2，六名操作员）
| 场景 | 指标 | GELLO | ACE |
|------|------|-------|-----|
| Small/Small | 平均到达时间 | 13.6 s | 4.69 s |
| Small/Small | 成功率 | 47.6% | 97.1% |
| Medium/Small | 平均到达时间 | 6.52 s | 4.54 s |
| Medium/Small | 成功率 | 73.8% | 91.4% |
| Medium/Medium | 平均到达时间 | 3.65 s | 4.05 s |
| Medium/Medium | 成功率 | 93.8% | 87.5% |
| Large/Large | 平均到达时间 | 6.52 s | 5.17 s |
| Large/Large | 成功率 | 68.7% | 78.6% |

ACE 在小工作空间优势显著（成功率 97.1% vs 47.6%），但在 Medium/Medium 场景成功率略低于 GELLO（87.5% vs 93.8%），表明其优势主要集中在需要精细控制的小空间任务。

### 模仿学习（Table 3，每任务 10 回合）
| 任务 | 平台 | 数据收集成功率 | 关键步骤成功率 |
|------|------|----------------|----------------|
| Vacuum Keyboard | xArm7+Ability | 30/38 | Grasp 1，Activate 0.6，Clean 0.6，Place 0.5 |
| Serve Candies | xArm7+Ability | 45/53 | Grasp 0.9，Open 0.6，Throw Cap 0.5，Pour 0.4 |
| Wipe Whiteboard | xArm7+Ability | 30/37 | Grasp 1，Wipe 0.7 |
| Grasp Dolls | xArm7+Ability | 120/123 | Grasp 0.9，Place 0.8 |
| Put in Tennis | H1+Inspire | 25/29 | Grasp 0.9，Put in 0.9 |
| Grasp Dolls | H1+Inspire | 62/66 | Grasp 0.9，Place 0.9 |

Grasp Dolls 泛化测试：训练 9 种小型+2 种大型玩偶，测试 15 种小型+3 种大型玩偶，成功率保持 0.9，表明数据质量足以支撑一定程度的泛化。

## 边界与局限

- 摄像头支架阻止穿戴者双手靠近，并因增加的力矩臂加重旋转运动的负担；虽通过缩放控制器在功能上解决，但某些操作不够直观。
- 论文未明确大规模数据集收集、长期稳定性测试、不同操作员体型适配的详细评估、力反馈集成、延迟量化分析。
- 手部跟踪频率约 27 Hz 可能限制高速动态任务的采集质量，提升至 100 Hz 需更换更高频率摄像头。
- 模仿学习算法依赖平台（xArm 用 3D 扩散策略，H1 用 ACT），跨平台算法迁移性未验证。

## 工程启示

- **复现优先级**：先核对 DYNAMIXEL XL330-M288-T 伺服电机的 12 位编码器精度是否满足 1 mm 正运动学误差要求，这是整个系统精度的基石。
- **易踩坑点**：摄像头支架的力矩臂问题在长时间操作中会显著影响操作员舒适度，建议在复现时考虑轻量化支架或调整摄像头安装位置；Bimanual Mode 的工作空间对齐参数（\( \gamma \) 与 \( \mathbf{c}_{t} \)）需针对具体机器人构型重新标定，不可直接沿用论文数值。
- **下游团队选型**：若任务以小型精细操作为主（如桌面装配），ACE 的 Small/Small 场景优势（成功率 97.1%）值得优先考虑；若任务涉及大型工作空间（如人形全身操作），需评估 Medium/Medium 场景中 ACE 成功率低于 GELLO（87.5% vs 93.8%）的潜在影响。
- **数据采集建议**：Grasp Dolls 任务数据收集成功率高达 120/123，表明该系统在抓取类任务中数据质量稳定，适合作为模仿学习数据采集的首选场景；但 Serve Candies 的 Throw Cap 与 Pour 步骤成功率仅 0.5 与 0.4，提示涉及抛掷或倾倒的动态操作仍是当前瓶颈。

## 参考
- http://arxiv.org/abs/2607.00678v2

## 개요
ABot-M0.5는 기존 세계 행동 모델이 이동 조작에서 가지는 한계를 해결하기 위해 3단계 정렬 방안을 제안한다. 이는 중간 잠재 행동을 통해 국부적 시각 상태 변화를 포착하여, 비디오 잠재 표현과 구체적 제어 사이의 다리 역할을 수행한다. 또한 이중 수준 Mixture-of-Transformers 아키텍처를 채택하여 베이스 이동과 로봇 팔 조작과 같은 이질적 행동 부분 공간을 분리하고, dream-forcing 훈련 전략을 통해 모델이 예측한 비디오에서 역동역학을 점진적으로 훈련하여 자기회귀 추론 시 강건성을 강화한다. 여러 이동 및 정밀 조작 벤치마크에서 ABot-M0.5는 선도적인 성능을 달성했다.

## 핵심 내용
### 방법 개요
ABot-M0.5는 이동 조작 작업에서 시간 입자 크기가 거칠고, 행동 공간이 결합되며, 훈련과 추론이 일치하지 않는 문제를 해결하기 위한 통합 세계 행동 모델이다. 그 설계는 세 가지 핵심 정렬 목표를 중심으로 전개된다:

- **시간 입자 정렬**: 중간 잠재 행동(intermediate latent actions)을 도입하여 인접 비디오 프레임 간의 국부적 시각 상태 변화를 포착하며, 이는 비디오 잠재 표현과 구체적 로봇 제어 신호 사이의 다리 역할을 한다. 이를 통해 거친 비디오 블록을 직접 조작할 때 발생하는 접촉 역학 손실을 방지한다.
- **행동 공간 정렬**: 이중 수준 Mixture-of-Transformers 아키텍처를 채택하여, 첫 번째 수준은 시각과 행동 같은 서로 다른 양식의 표현을 분리하고, 두 번째 수준은 베이스 이동(base movement)과 로봇 팔 조작(arm manipulation)을 분리하는 등 이질적 행동 부분 공간을 추가로 분리하여 행동 분포 충돌을 제거한다.
- **추론 조건 정렬**: dream-forcing 훈련 전략을 제안하여 실제 비디오에만 의존하지 않고 모델이 예측한 비디오 시퀀스에서 역동역학 모델을 점진적으로 훈련한다. 이를 통해 훈련 시 감독 신호와 자기회귀 추론 시 입력 분포가 더 잘 일치하여 장기 rollout에서 오류 누적을 줄인다.

### 실험 설정 및 주요 결과
- **벤치마크 테스트**: 장기 계획이 필요한 작업과 정밀한 접촉 역학이 필요한 작업을 포함한 여러 도전적인 이동 조작 벤치마크에서 평가된다.
- **성능**: ABot-M0.5는 장기 작업 성공률(long-horizon task success)과 정밀 제어 정확도(fine-grained control accuracy) 두 지표 모두에서 state-of-the-art 수준에 도달했다.
- **주요 수치**: 구체적인 값은 요약에 제시되지 않았지만, 실험은 특히 내비게이션과 조작 행동을 분리해야 하는 시나리오에서 기존 WAM 방법보다 현저히 우수함을 보여준다.

### 결론
ABot-M0.5는 이동 조작에서 시간 입자 정렬, 행동 분리, 추론 일관성 모델링의 중요성을 검증한다. 그 설계는 더 강건하고 정밀한 범용 로봇 세계 모델을 구축하는 새로운 방향을 제시한다.
