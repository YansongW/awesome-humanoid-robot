---
$id: ent_paper_active_stereo_camera_outperfor_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Active Stereo-Camera Outperforms Multi-Sensor Setup in ACT Imitation Learning for Humanoid Manipulation
  zh: 在人形操作的ACT模仿学习中，主动立体相机的性能优于多传感器设置
  ko: Active Stereo-Camera Outperforms Multi-Sensor Setup in ACT Imitation Learning for Humanoid Manipulation
summary:
  en: In ACT imitation learning for humanoid manipulation, the performance of active stereo cameras is better than that of
    multi-sensor settings. Camera images/multi-view observations, body state and joint sequences, contact force/tactile signals
    are converted into trackable body targets, and the action chunk/token is finally output through ACT/behavior cloning imitation
    learning, MM-DiT/Transformer action head training or combined whole-body strategies. The key point is to press the demonstration
    trajectory into a supervised action prediction problem, and then reduce timing jitter through action chunk or closed-loop
    execution.
  zh: 在人形操作的ACT模仿学习中，主动立体相机的性能优于多传感器设置 把相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过ACT/行为克隆模仿学习、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出动作
    chunk/token。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。
  ko: 在人形操作的ACT模仿学习中，主动立体相机的性能优于多传感器设置 把相机图像/多视角观测、本体状态与关节序列、接触力/触觉信号转成可跟踪的身体目标，并通过ACT/行为克隆模仿学习、MM-DiT/Transformer 动作头训练或组合全身策略，最终输出动作
    chunk/token。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作 chunk 或闭环执行降低时序抖动。
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
- midstream
functional_roles:
- knowledge
- component
tags:
- act
- deployment
- hardware_platform
- real_world
- sensor_suite
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: low
  notes: 'Imported from WeChat curated list (143). Institution: Imitation Learning for Humanoid Manipulation. Full title:
    Active Stereo-Camera Outperforms Multi-Sensor Setup in ACT Imitation Learning for Humanoid Manipulation. English name/summary
    machine-translated from Chinese by scripts/backfill_en_translations.py. [2026-08-05] body rewritten as full-text six-section
    deep read (.staging/deep_read batch2, DeepSeek deepseek-chat T<=0.3, arXiv HTML full text); en/ko sections regenerated
    by translate pipeline.'
sources:
- id: src_001
  type: website
  title: 在人形操作的ACT模仿学习中，主动立体相机的性能优于多传感器设置 project page
  url: http://github.com/kuehnrobin/
  date: '2026'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---




## 概述

本文针对人形机器人模仿学习（ACT）中传感配置缺乏严格对比的问题，在 Unitree G1 平台上构建统一消融框架（UAF），通过二元掩码在完全同步的训练片段上隔离传感器变量。核心发现是：仅主动立体相机（A）在空间泛化任务上以 87.5% 成功率远超静态相机（10.0%），且添加指尖压力传感器在简单任务上反而造成性能显著下降（94.4%→67.3%），挑战了“多模态即更优”的直觉。

## 它改变了什么

这项工作的真正价值在于终结了“传感器越多越好”的默认假设。此前 Bi-ACT 主张关节力矩、OpenTelevision 强调主动视觉，但各自在不同机器人平台（Dynamixel、Unitree H1）上验证，性能差异无法归因于模态本身还是硬件特性。作者通过单一平台（Unitree G1）+ 统一数据录制（主数据集含全部模态）+ 训练时掩码消融，首次将“操作者技能差异”和“示范质量差异”这两个隐藏变量从比较中剔除——这是此前所有跨论文比较都无法做到的。

它改变的不仅是结论，更是方法论：传统评估需要为每种传感器配置单独录制数据集，这天然引入人为方差；UAF 让所有策略吃同一批同步数据，使传感器贡献的因果归因成为可能。这为社区树立了可复现的基准范式，尤其针对数据有限（≤250 次示范）这一工业落地最关心的场景。

## 方法拆解

### 平台与数据
- 平台：Unitree G1（Edu-U4），三指 Dex3-1 手（7-DoF），代表性价比商用类人机器人
- 数据有限场景：≤250 次示范（任务1：20 episodes；任务2：242 episodes）

### 统一消融框架（UAF）
1. **主数据集录制**：所有示范同时记录 Active Cam、Static Cam、Wrist Cams、关节位置 q、速度 q̇、力矩 τ、指尖压力 f_pres
2. **训练时掩码**：自定义数据加载器对观测向量施加二元掩码，动态省略被排除的传感器流
3. **关键设计**：所有策略使用完全同步的训练片段，消除人类示范方差——这是与传统“分别录制数据集”的本质区别

### ACT 架构
- 基于 LeRobot 的 Unitree wrapper，CVAE 预测动作序列 a_{t:t+k}
- 状态向量扩展：s_t = [q, q̇, τ, f_pres]，经可学习线性层投影到 transformer 嵌入维度
- 超参数沿用 OpenTelevision，视觉骨干 ResNet18，每策略训练 80,000 步

### 遥操作与主动感知
- Meta Quest 3 VR 遥操作，操作者通过机器人主动立体相机观察环境
- 头部运动与视觉观察形成因果联系，使策略能从示范中学习主动感知（如视觉搜索）
- 手部重定向采用修改版 DexPilot

### 策略命名
- 相机：A=Active、S=Static、W=Wrist；本体感觉：P=Pressure、V=Velocity、T=Torque
- 例：WA-P = Wrist + Active 相机 + 压力传感器

## 关键创新

1. **UAF 掩码消融范式**：这是首个在完全同步数据上隔离传感器贡献的框架。此前所有对比要么跨论文（平台不同），要么独立录制（人为方差），UAF 通过训练时掩码让同一批示范服务所有配置，使因果归因首次成立。

2. **主动视觉的压倒性优势量化**：在空间泛化任务（Cube in Box）中，仅主动立体相机（A）达到 87.5% 成功率，而静态相机（S）仅 10.0%——这不是渐进改进，而是数量级的差距。这为“主动感知是类人操作刚需”提供了迄今最有力的单变量证据。

3. **触觉模态的负面效应发现**：在简单任务（Sort Cans）中，给主动相机添加压力传感器（A→A-P）导致成功率从 94.4% 暴跌至 67.3%。这挑战了“触觉总有益”的直觉，提示低保真压力传感器（Unitree G1 趋向二值）在数据有限时可能成为噪声源而非信息源。

## 实验与结果

### 任务1（Sort Cans，20 episodes，N=10 试验/策略）

| 策略 | 训练时间 (h) | 成功率 (%) | 执行时间 (min) |
|------|-------------|-----------|---------------|
| A（仅主动相机） | 7.35 | 94.4 | 3.9（最快） |
| A-P | 7.40 | 67.3 | - |
| WA-P（最佳） | 19.35 | 97.6 | 4.8 |
| WA | 20.58 | 93.6 | 5.8 |

### 任务2（Cube in Box，242 episodes，N=15 试验/策略）

| 策略 | 训练时间 (h) | 成功率 (%) | 执行时间 (min) |
|------|-------------|-----------|---------------|
| A（最佳） | 11.51 | 87.5 | 0.4（最快） |
| S（仅静态相机） | 9.56 | 10.0 | - |
| WA | - | 72.7 | 0.7 |
| WA-PV_AT_A | 15.35 | 82.5 | 0.9 |

### 关键对比
- **主动 vs 静态**：任务2中 A（87.5%）vs S（10.0%）
- **压力传感器负面效应**：任务1中 A→A-P 成功率从 94.4% 降至 67.3%
- **与 OpenTelevision 基线**：其 Sort Cans 类任务报 83% 抓取/50% 放置（N=5），本工作 WA-P 达 97.6% 总体成功率，作者归因于双倍训练数据量
- **失败模式**：任务1出现模式平均（轨迹间插值导致碰撞）；任务2中主动+静态广角组合触发悬停/振荡，大幅增加执行时间

## 边界与局限

- **算法特异性**：仅验证 ACT；Diffusion Policy 等对多模态动作分布和噪声鲁棒性可能不同
- **遥操作延迟**：VR 设置引入 0.5–1.0 秒运动到光子延迟，虽恒定但可能在训练数据中引入停顿伪影
- **任务范围**：仅桌面操作；动态任务（locomotion、全身举升）的最优传感器集可能完全不同
- **数据范围**：仅 ≤250 次示范；触觉等模态的收益可能在更大数据集下才显现
- **硬件保真度绑定**：结论与 Unitree G1 的传感器质量强相关（基于电流的力矩估计、趋向二值的压力传感器）；高保真平台（如 DLR TORO）上本体感觉可能更有益
- **未做之事**：未测试 ViT（如 DINOv3）对视觉干扰的敏感性；未确定触觉从噪声变信息的数据集阈值；未验证 Diffusion Policies 或 VLA 模型

## 工程启示

- **复现优先核对**：UAF 代码在 https://github.com/kuehnrobin/UAF_lerobot ，数据集在 Hugging Face（Sort Cans revision eefeb43，Cube in Box revision ba5d998）；训练硬件为单张 RTX 4090，每策略 80,000 步，任务1约 7–21 小时、任务2约 10–25 小时——先跑通 A 配置（最快收敛）再扩展其他配置。

- **最容易踩坑**：① 压力传感器在低保真平台上是负资产，别盲目堆模态；② 主动+静态广角组合会触发悬停/振荡（任务2中 WA-PV_AT_A 执行时间从 0.4 min 增至 2.4 min），若必须多相机，优先保证主动视图主导；③ 训练时间随传感器配置差异巨大（7.3→20.6 小时），预算规划需按最慢配置预留。

- **下游团队选型建议**：若目标是空间泛化（如随机抓取），仅主动立体相机（A）是最优性价比——训练最快、成功率最高、执行最快；若任务简单且位置可预测（如分拣），WA-P 可冲最高绝对性能（97.6%），但需接受 2.6 倍训练时间。对数据有限场景，先砍触觉和力矩，把钱花在主动视觉上。

## 参考
- http://github.com/kuehnrobin/

## Overview

This paper addresses the lack of rigorous sensor configuration comparisons in humanoid robot imitation learning (ACT). It builds a Unified Ablation Framework (UAF) on the Unitree G1 platform, isolating sensor variables through binary masks on fully synchronized training episodes. The core finding is that the active stereo camera alone (A) achieves a 87.5% success rate on spatial generalization tasks, far surpassing the static camera (10.0%), and that adding fingertip pressure sensors actually causes significant performance degradation on simple tasks (94.4%→67.3%), challenging the intuition that "more modalities are better."

## What It Changes

The true value of this work lies in ending the default assumption that "more sensors are better." Previously, Bi-ACT advocated for joint torque, and OpenTelevision emphasized active vision, but each was validated on different robot platforms (Dynamixel, Unitree H1), making it impossible to attribute performance differences to the modality itself versus hardware characteristics. By using a single platform (Unitree G1) + unified data recording (master dataset containing all modalities) + training-time mask ablation, the authors for the first time eliminate the two hidden variables of "operator skill differences" and "demonstration quality differences" from comparisons—something no previous cross-paper comparison could achieve.

What it changes is not just the conclusion but the methodology: traditional evaluation requires separately recording datasets for each sensor configuration, which inherently introduces human variance; UAF allows all policies to consume the same synchronized data, making causal attribution of sensor contributions possible. This establishes a reproducible benchmark paradigm for the community, especially for the data-limited scenario (≤250 demonstrations) most relevant to industrial deployment.

## Method Breakdown

### Platform and Data
- Platform: Unitree G1 (Edu-U4), three-finger Dex3-1 hand (7-DoF), representing a cost-effective commercial humanoid robot
- Data-limited scenario: ≤250 demonstrations (Task 1: 20 episodes; Task 2: 242 episodes)

### Unified Ablation Framework (UAF)
1. **Master dataset recording**: All demonstrations simultaneously record Active Cam, Static Cam, Wrist Cams, joint positions q, velocities q̇, torques τ, and fingertip pressure f_pres
2. **Training-time masking**: A custom data loader applies binary masks to observation vectors, dynamically omitting excluded sensor streams
3. **Key design**: All policies use fully synchronized training episodes, eliminating human demonstration variance—this is the fundamental difference from traditional "separately recorded datasets"

### ACT Architecture
- Based on LeRobot's Unitree wrapper, CVAE predicts action sequences a_{t:t+k}
- State vector extension: s_t = [q, q̇, τ, f_pres], projected via learnable linear layers to transformer embedding dimensions
- Hyperparameters follow OpenTelevision, visual backbone ResNet18, each policy trained for 80,000 steps

### Teleoperation and Active Perception
- Meta Quest 3 VR teleoperation, operator observes the environment through the robot's active stereo camera
- Head movement and visual observation form a causal link, enabling policies to learn active perception (e.g., visual search) from demonstrations
- Hand retargeting uses a modified version of DexPilot

### Policy Naming
- Cameras: A=Active, S=Static, W=Wrist; Proprioception: P=Pressure, V=Velocity, T=Torque
- Example: WA-P = Wrist + Active camera + Pressure sensor

## Key Innovations

1. **UAF mask ablation paradigm**: This is the first framework to isolate sensor contributions on fully synchronized data. All previous comparisons were either cross-paper (different platforms) or independently recorded (human variance). UAF uses training-time masks so the same demonstrations serve all configurations, making causal attribution valid for the first time.

2. **Quantification of active vision's overwhelming advantage**: In the spatial generalization task (Cube in Box), the active stereo camera alone (A) achieves 87.5% success, while the static camera (S) reaches only 10.0%—this is not incremental improvement but an order-of-magnitude gap. This provides the strongest single-variable evidence to date that "active perception is essential for humanoid manipulation."

3. **Discovery of negative effects from tactile modality**: In the simple task (Sort Cans), adding pressure sensors to the active camera (A→A-P) causes success rate to plummet from 94.4% to 67.3%. This challenges the intuition that "touch is always beneficial," suggesting that low-fidelity pressure sensors (Unitree G1 tends toward binary) may act as a noise source rather than an information source under data-limited conditions.

## Experiments and Results

### Task 1 (Sort Cans, 20 episodes, N=10 trials/policy)

| Policy | Training Time (h) | Success Rate (%) | Execution Time (min) |
|--------|-------------------|------------------|----------------------|
| A (active camera only) | 7.35 | 94.4 | 3.9 (fastest) |
| A-P | 7.40 | 67.3 | - |
| WA-P (best) | 19.35 | 97.6 | 4.8 |
| WA | 20.58 | 93.6 | 5.8 |

### Task 2 (Cube in Box, 242 episodes, N=15 trials/policy)

| Policy | Training Time (h) | Success Rate (%) | Execution Time (min) |
|--------|-------------------|------------------|----------------------|
| A (best) | 11.51 | 87.5 | 0.4 (fastest) |
| S (static camera only) | 9.56 | 10.0 | - |
| WA | - | 72.7 | 0.7 |
| WA-PV_AT_A | 15.35 | 82.5 | 0.9 |

### Key Comparisons
- **Active vs. static**: Task 2 A (87.5%) vs. S (10.0%)
- **Negative effect of pressure sensors**: Task 1 A→A-P success rate drops from 94.4% to 67.3%
- **vs. OpenTelevision baseline**: Its Sort Cans-type task reports 83% grasp/50% place (N=5); this work's WA-P achieves 97.6% overall success, attributed by the authors to double the training data volume
- **Failure modes**: Task 1 exhibits mode averaging (trajectory interpolation causing collisions); in Task 2, the active + static wide-angle combination triggers hovering/oscillation, significantly increasing execution time

## Boundaries and Limitations

- **Algorithm specificity**: Only ACT is validated; Diffusion Policy and others may respond differently to multimodal action distributions and noise robustness
- **Teleoperation latency**: The VR setup introduces 0.5–1.0 seconds of motion-to-photon delay, which is constant but may introduce pause artifacts in training data
- **Task scope**: Only tabletop manipulation; optimal sensor sets for dynamic tasks (locomotion, whole-body lifting) may be entirely different
- **Data scope**: Only ≤250 demonstrations; benefits of modalities like touch may only emerge with larger datasets
- **Hardware fidelity binding**: Conclusions are strongly tied to Unitree G1's sensor quality (current-based torque estimation, pressure sensors tending toward binary); proprioception may be more beneficial on high-fidelity platforms (e.g., DLR TORO)
- **What was not done**: ViT (e.g., DINOv3) sensitivity to visual disturbances was not tested; the dataset threshold at which touch transitions from noise to information was not determined; Diffusion Policies or VLA models were not validated

## Engineering Insights

- **Reproduction priority checklist**: UAF code is at https://github.com/kuehnrobin/UAF_lerobot , datasets on Hugging Face (Sort Cans revision eefeb43, Cube in Box revision ba5d998); training hardware is a single RTX 4090, 80,000 steps per policy, Task 1 approximately 7–21 hours, Task 2 approximately 10–25 hours—start with the A configuration (fastest convergence) before expanding to other configurations.

- **Most common pitfalls**: ① Pressure sensors are a liability on low-fidelity platforms—don't blindly stack modalities; ② The active + static wide-angle combination triggers hovering/oscillation (Task 2 WA-PV_AT_A execution time increases from 0.4 min to 2.4 min); if multiple cameras are necessary, prioritize active view dominance; ③ Training time varies dramatically with sensor configuration (7.3→20.6 hours), so budget planning should reserve for the slowest configuration.

- **Downstream team selection recommendations**: If the goal is spatial generalization (e.g., random grasping), the active stereo camera alone (A) offers the best cost-performance—fastest training, highest success rate, fastest execution; if the task is simple with predictable positions (e.g., sorting), WA-P can achieve the highest absolute performance (97.6%) but requires accepting 2.6× training time. For data-limited scenarios, cut touch and torque first, and invest in active vision.

## 개요

본 논문은 휴머노이드 로봇 모방 학습(ACT)에서 센서 구성에 대한 엄격한 비교가 부재한 문제를 해결하기 위해, Unitree G1 플랫폼에서 통합 소거 프레임워크(UAF)를 구축하고, 이진 마스크를 통해 완전히 동기화된 훈련 세그먼트에서 센서 변수를 격리한다. 핵심 발견은 다음과 같다: 능동 스테레오 카메라(A)만 사용했을 때 공간 일반화 작업에서 87.5%의 성공률로 정적 카메라(10.0%)를 크게 능가했으며, 손끝 압력 센서를 추가하면 오히려 간단한 작업에서 성능이 현저히 저하되어(94.4%→67.3%) '다중 모달이 곧 더 우수하다'는 직관에 도전한다.

## 그것이 바꾸는 것

이 작업의 진정한 가치는 '센서가 많을수록 좋다'는 기본 가정을 종식시킨 데 있다. 이전에는 Bi-ACT가 관절 토크를 주장하고 OpenTelevision이 능동 비전을 강조했지만, 각각 다른 로봇 플랫폼(Dynamixel, Unitree H1)에서 검증되어 성능 차이를 모달리티 자체 때문인지 하드웨어 특성 때문인지 귀인할 수 없었다. 저자들은 단일 플랫폼(Unitree G1) + 통합 데이터 녹화(마스터 데이터셋에 모든 모달리티 포함) + 훈련 시 마스크 소거를 통해 '조작자 기술 차이'와 '시연 품질 차이'라는 두 가지 숨은 변수를 비교에서 처음으로 제거했다—이는 이전의 모든 논문 간 비교에서 불가능했던 것이다.

이것이 바꾸는 것은 결론뿐만 아니라 방법론이다: 기존 평가는 각 센서 구성에 대해 별도로 데이터셋을 녹화해야 했으며, 이는 자연스럽게 인간의 분산을 도입했다; UAF는 모든 정책이 동일한 동기화 데이터를 사용하게 하여 센서 기여에 대한 인과적 귀인을 가능하게 한다. 이는 특히 데이터가 제한된(≤250회 시연) 산업 현장 적용에서 가장 중요한 시나리오에 대해 커뮤니티에 재현 가능한 벤치마크 패러다임을 제시한다.

## 방법 분석

### 플랫폼 및 데이터
- 플랫폼: Unitree G1 (Edu-U4), 3손가락 Dex3-1 핸드(7-DoF), 가성비 상용 휴머노이드 로봇 대표
- 데이터 제한 시나리오: ≤250회 시연 (작업1: 20 episodes; 작업2: 242 episodes)

### 통합 소거 프레임워크 (UAF)
1. **마스터 데이터셋 녹화**: 모든 시연에서 Active Cam, Static Cam, Wrist Cams, 관절 위치 q, 속도 q̇, 토크 τ, 손끝 압력 f_pres를 동시에 기록
2. **훈련 시 마스크**: 맞춤형 데이터 로더가 관측 벡터에 이진 마스크를 적용하여 제외된 센서 스트림을 동적으로 생략
3. **핵심 설계**: 모든 정책이 완전히 동기화된 훈련 세그먼트를 사용하여 인간 시연 분산을 제거—이는 기존의 '별도 데이터셋 녹화'와의 본질적 차이

### ACT 아키텍처
- LeRobot 기반 Unitree 래퍼, CVAE가 동작 시퀀스 a_{t:t+k} 예측
- 상태 벡터 확장: s_t = [q, q̇, τ, f_pres], 학습 가능한 선형 레이어를 통해 transformer 임베딩 차원으로 투영
- 하이퍼파라미터는 OpenTelevision을 따르며, 비주얼 백본 ResNet18, 정책당 80,000 스텝 훈련

### 원격 조작 및 능동 인지
- Meta Quest 3 VR 원격 조작, 조작자는 로봇의 능동 스테레오 카메라를 통해 환경 관찰
- 머리 움직임과 시각적 관찰이 인과적 연결을 형성하여 정책이 시연에서 능동 인지(예: 시각 검색)를 학습할 수 있게 함
- 손 재지정은 수정된 DexPilot 사용

### 정책 명명
- 카메라: A=Active, S=Static, W=Wrist; 고유수용감각: P=Pressure, V=Velocity, T=Torque
- 예: WA-P = Wrist + Active 카메라 + 압력 센서

## 핵심 혁신

1. **UAF 마스크 소거 패러다임**: 완전히 동기화된 데이터에서 센서 기여를 격리하는 최초의 프레임워크. 이전의 모든 비교는 논문 간(플랫폼 상이) 또는 독립 녹화(인간 분산)였으며, UAF는 훈련 시 마스크를 통해 동일한 시연이 모든 구성에 서비스되도록 하여 인과적 귀인이 처음으로 성립한다.

2. **능동 비전의 압도적 우위 정량화**: 공간 일반화 작업(Cube in Box)에서 능동 스테레오 카메라(A)만으로 87.5% 성공률을 달성한 반면, 정적 카메라(S)는 10.0%에 불과—이는 점진적 개선이 아니라 규모의 차이다. 이는 '능동 인지가 휴머노이드 조작의 필수 요소'라는 주장에迄今为止 가장 강력한 단일 변수 증거를 제공한다.

3. **촉각 모달리티의 부정적 효과 발견**: 간단한 작업(Sort Cans)에서 능동 카메라에 압력 센서를 추가(A→A-P)하면 성공률이 94.4%에서 67.3%로 급락한다. 이는 '촉각이 항상 유익하다'는 직관에 도전하며, 저충실도 압력 센서(Unitree G1은 이진에 가까움)가 데이터가 제한된 상황에서 정보원이 아닌 노이즈원이 될 수 있음을 시사한다.

## 실험 및 결과

### 작업1 (Sort Cans, 20 episodes, N=10 시험/정책)

| 정책 | 훈련 시간 (h) | 성공률 (%) | 실행 시간 (min) |
|------|-------------|-----------|---------------|
| A (능동 카메라만) | 7.35 | 94.4 | 3.9 (가장 빠름) |
| A-P | 7.40 | 67.3 | - |
| WA-P (최고) | 19.35 | 97.6 | 4.8 |
| WA | 20.58 | 93.6 | 5.8 |

### 작업2 (Cube in Box, 242 episodes, N=15 시험/정책)

| 정책 | 훈련 시간 (h) | 성공률 (%) | 실행 시간 (min) |
|------|-------------|-----------|---------------|
| A (최고) | 11.51 | 87.5 | 0.4 (가장 빠름) |
| S (정적 카메라만) | 9.56 | 10.0 | - |
| WA | - | 72.7 | 0.7 |
| WA-PV_AT_A | 15.35 | 82.5 | 0.9 |

### 핵심 비교
- **능동 vs 정적**: 작업2에서 A (87.5%) vs S (10.0%)
- **압력 센서 부정적 효과**: 작업1에서 A→A-P 성공률이 94.4%에서 67.3%로 하락
- **OpenTelevision 베이스라인과 비교**: 해당 작업의 Sort Cans 유사 작업은 83% 그립/50% 배치(N=5)를 보고했으며, 본 연구의 WA-P는 97.6% 전체 성공률을 달성—저자들은 두 배의 훈련 데이터 양에 기인한다고 분석
- **실패 모드**: 작업1에서 모드 평균(궤적 간 보간으로 인한 충돌) 발생; 작업2에서 능동+정적 광각 조합이 호버링/진동을 유발하여 실행 시간을 크게 증가

## 경계 및 한계

- **알고리즘 특이성**: ACT만 검증; Diffusion Policy 등은 다중 모달 동작 분포 및 노이즈에 대한 강건성이 다를 수 있음
- **원격 조작 지연**: VR 설정이 0.5–1.0초의 모션-투-포톤 지연을 도입하며, 일정하지만 훈련 데이터에 일시 정지 아티팩트를 도입할 수 있음
- **작업 범위**: 데스크톱 조작만 해당; 동적 작업(locomotion, 전신 리프팅)의 최적 센서 세트는 완전히 다를 수 있음
- **데이터 범위**: ≤250회 시연만 해당; 촉각 등의 모달리티 이점은 더 큰 데이터셋에서 나타날 수 있음
- **하드웨어 충실도 의존성**: 결론은 Unitree G1의 센서 품질(전류 기반 토크 추정, 이진에 가까운 압력 센서)과 강하게 연관됨; 고충실도 플랫폼(예: DLR TORO)에서는 고유수용감각이 더 유익할 수 있음
- **수행하지 않은 것**: ViT(예: DINOv3)의 시각적 교란 민감도 테스트 미수행; 촉각이 노이즈에서 정보로 전환되는 데이터셋 임계값 미확정; Diffusion Policies 또는 VLA 모델 검증 미수행

## 엔지니어링 시사점

- **재현 우선 확인 사항**: UAF 코드는 https://github.com/kuehnrobin/UAF_lerobot , 데이터셋은 Hugging Face(Sort Cans revision eefeb43, Cube in Box revision ba5d998)에 있음; 훈련 하드웨어는 단일 RTX 4090, 정책당 80,000 스텝, 작업1 약 7–21시간, 작업2 약 10–25시간—A 구성(가장 빠른 수렴)을 먼저 실행한 후 다른 구성을 확장할 것.

- **가장 흔한 함정**: ① 압력 센서는 저충실도 플랫폼에서 부정적 자산이므로 모달리티를 무분별하게 추가하지 말 것; ② 능동+정적 광각 조합은 호버링/진동을 유발하며(작업2에서 WA-PV_AT_A 실행 시간이 0.4 min에서 2.4 min으로 증가), 다중 카메라가 필요하면 능동 뷰가 주도하도록 우선 보장할 것; ③ 훈련 시간은 센서 구성에 따라 크게 다르므로(7.3→20.6시간), 예산 계획은 가장 느린 구성 기준으로 예비할 것.

- **다운스트림 팀 선택 제안**: 목표가 공간 일반화(예: 무작위 그립)라면 능동 스테레오 카메라(A)만이 최적의 가성비—훈련이 가장 빠르고, 성공률이 가장 높으며, 실행이 가장 빠름; 작업이 간단하고 위치가 예측 가능하다면(예: 분류), WA-P가 최고 절대 성능(97.6%)을 달성할 수 있지만 2.6배의 훈련 시간을 수용해야 함. 데이터 제한 시나리오에서는 촉각과 토크를 먼저 제거하고 능동 비전에 투자할 것.
