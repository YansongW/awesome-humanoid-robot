---
$id: ent_paper_amo_adaptive_motion_optimizati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
  zh: AMO｜超灵巧人形全身控制的自适应运动优化
  ko: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
summary:
  en: 'Humanoid robots derive much of their dexterity from hyper-dexterous whole-body movements, enabling tasks that require
    a large operational workspace: such as picking objects off the ground. However, achieving these capabilities on real humanoids
    remains challenging due to their high degrees of freedom (DoF) and nonlinear dynamics. We propose Adaptive Motion Optimization
    (AMO), a framework that integrates sim-to-real reinforcement learning (RL) with trajectory optimization for real-time,
    adaptive whole-body control. To mitigate distribution bias in motion imitation RL, we construct a hybrid AMO dataset and
    train a network capable of robust, on-demand adaptation to potentially O.O.D. commands. We validate AMO in simulation
    and on a 29-DoF Unitree G1 humanoid robot, demonstrating superior stab'
  zh: AMO（Adaptive Motion Optimization）是一个将仿真到现实强化学习与轨迹优化相结合的框架，用于实现人形机器人的实时自适应全身控制。该框架由研究团队提出，通过构建混合AMO数据集来缓解运动模仿强化学习中的分布偏差，并在29自由度的Unitree
    G1人形机器人上验证了其优越的稳定性和扩展的工作空间。
  ko: AMO 把本体状态与关节序列、仿真交互数据、接触力/触觉信号转成可跟踪的身体目标，并通过PPO/RL 策略训练、ACT/行为克隆模仿学习、全身控制器/WBC/MPC训练或组合全身策略，最终输出全身轨迹/动作序列、低层控制器目标。关键点是把示范轨迹压成可监督的动作预测问题，再通过动作
    chunk 或闭环执行降低时序抖动。
domains:
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- midstream
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- amo
- manipulation_interface
- mobile_manipulation
- upper_body_control
- whole_body_control
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: low
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from Semantic Scholar search: AMO: Adaptive Motion Optimization
    for Hyper-Dexterous Humanoid Whole-Body Control. [2026-07-29] zh content backfilled from English abstract via scripts/sinicize_english_cards.py'
sources:
- id: src_001
  type: website
  title: AMO project page
  url: https://amo-humanoid.github.io/
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
人形机器人通过高度灵巧的全身运动实现大操作空间的任务（如从地面拾取物体），但高自由度与非线性动力学使得在真实机器人上实现这些能力充满挑战。AMO框架创新性地融合了仿真到现实强化学习与轨迹优化，实现了实时自适应的全身控制。为解决运动模仿强化学习中的分布偏差问题，研究团队构建了混合AMO数据集，训练出的网络能够对潜在的分布外指令进行鲁棒的按需适应。在仿真和29自由度的Unitree G1人形机器人上的实验表明，AMO相比强基线方法展现出更优的稳定性和更大的工作空间。

## 核心内容
### 方法
AMO框架的核心是将仿真到现实强化学习与轨迹优化相结合，实现实时自适应全身控制。具体而言：
- **混合AMO数据集**：为缓解运动模仿强化学习中的分布偏差，构建了包含多种运动模式的混合数据集。
- **网络训练**：基于该数据集训练网络，使其能够对潜在的分布外（O.O.D.）指令进行鲁棒的按需适应。

### 实验设置
- **平台**：29自由度的Unitree G1人形机器人。
- **验证方式**：在仿真环境和真实机器人上分别进行验证。
- **对比基线**：与强基线方法进行对比。

### 关键结果
- **稳定性**：AMO在真实机器人上展现出更优的稳定性。
- **工作空间**：相比强基线方法，AMO实现了更大的操作工作空间。
- **任务执行**：AMO的一致性能支持通过模仿学习进行自主任务执行，证明了系统的多功能性和鲁棒性。

### 结论
AMO框架通过融合仿真到现实强化学习与轨迹优化，有效解决了高自由度人形机器人在实时全身控制中的挑战，为灵巧操作任务提供了可靠的解决方案。

## Overview
Humanoid robots derive much of their dexterity from hyper-dexterous whole-body movements, enabling tasks that require a large operational workspace: such as picking objects off the ground. However, achieving these capabilities on real humanoids remains challenging due to their high degrees of freedom (DoF) and nonlinear dynamics. We propose Adaptive Motion Optimization (AMO), a framework that integrates sim-to-real reinforcement learning (RL) with trajectory optimization for real-time, adaptive whole-body control. To mitigate distribution bias in motion imitation RL, we construct a hybrid AMO dataset and train a network capable of robust, on-demand adaptation to potentially O.O.D. commands. We validate AMO in simulation and on a 29-DoF Unitree G1 humanoid robot, demonstrating superior stability and an expanded workspace compared to strong baselines. Finally, we show that AMO's consistent performance supports autonomous task execution via imitation learning, underscoring the system's versatility and robustness.

## 개요
휴머노이드 로봇은 초정밀 전신 움직임을 통해 대부분의 손재주를 얻으며, 이는 넓은 작업 공간을 요구하는 작업(예: 바닥에서 물체 집기)을 가능하게 합니다. 그러나 높은 자유도(DoF)와 비선형 동역학으로 인해 실제 휴머노이드에서 이러한 능력을 구현하는 것은 여전히 어려운 과제입니다. 본 연구에서는 시뮬레이션-실제 강화 학습(RL)과 궤적 최적화를 통합하여 실시간 적응형 전신 제어를 가능하게 하는 Adaptive Motion Optimization(AMO) 프레임워크를 제안합니다. 모션 모방 RL의 분포 편향을 완화하기 위해 하이브리드 AMO 데이터셋을 구축하고, 잠재적인 O.O.D. 명령에 대해 강건하고 요구 기반 적응이 가능한 네트워크를 학습시킵니다. AMO는 시뮬레이션과 29-DoF Unitree G1 휴머노이드 로봇에서 검증되었으며, 강력한 기준선 대비 우수한 안정성과 확장된 작업 공간을 입증했습니다. 마지막으로, AMO의 일관된 성능이 모방 학습을 통한 자율 작업 실행을 지원함을 보여주며, 시스템의 다재다능함과 강건성을 강조합니다.

## 핵심 내용
휴머노이드 로봇은 초정밀 전신 움직임을 통해 대부분의 손재주를 얻으며, 이는 넓은 작업 공간을 요구하는 작업(예: 바닥에서 물체 집기)을 가능하게 합니다. 그러나 높은 자유도(DoF)와 비선형 동역학으로 인해 실제 휴머노이드에서 이러한 능력을 구현하는 것은 여전히 어려운 과제입니다. 본 연구에서는 시뮬레이션-실제 강화 학습(RL)과 궤적 최적화를 통합하여 실시간 적응형 전신 제어를 가능하게 하는 Adaptive Motion Optimization(AMO) 프레임워크를 제안합니다. 모션 모방 RL의 분포 편향을 완화하기 위해 하이브리드 AMO 데이터셋을 구축하고, 잠재적인 O.O.D. 명령에 대해 강건하고 요구 기반 적응이 가능한 네트워크를 학습시킵니다. AMO는 시뮬레이션과 29-DoF Unitree G1 휴머노이드 로봇에서 검증되었으며, 강력한 기준선 대비 우수한 안정성과 확장된 작업 공간을 입증했습니다. 마지막으로, AMO의 일관된 성능이 모방 학습을 통한 자율 작업 실행을 지원함을 보여주며, 시스템의 다재다능함과 강건성을 강조합니다.

## 参考
- Semantic Scholar search: AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control
