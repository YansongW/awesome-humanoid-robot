---
$id: ent_paper_li_amo_adaptive_motion_optimizati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
  zh: AMO：面向超灵巧人形机器人全身控制的自适应运动优化
  ko: 'AMO: 초민첩한 인간형 로봇 전신 제어를 위한 적응형 동작 최적화'
summary:
  en: Proposes Adaptive Motion Optimization (AMO), a framework that combines sim-to-real reinforcement learning with trajectory
    optimization to enable real-time, hyper-dexterous whole-body control on a 29-DoF Unitree G1 humanoid robot, validated
    on tasks such as picking objects from the ground.
  zh: AMO（Adaptive Motion Optimization）是一个结合仿真到现实强化学习与轨迹优化的框架，由研究团队提出，用于实现29自由度Unitree G1人形机器人的实时、高灵巧全身控制。其核心贡献在于通过混合数据集训练网络，解决运动模仿中的分布偏差问题，并在地面拾取物体等任务中验证了稳定性和扩展工作空间。
  ko: sim-to-real 강화학습과 궤적 최적화를 결합하여 29-DoF Unitree G1 인간형 로봇에서 실시간 초민첩 전신 제어를 가능하게 하는 AMO(Adaptive Motion Optimization) 프레임워크를
    제안하고, 지면에서 물체를 집는 작업 등으로 검증함.
domains:
- 07_ai_models_algorithms
- 02_components
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- whole_body_control
- sim_to_real
- reinforcement_learning
- trajectory_optimization
- motion_imitation
- loco_manipulation
- unitree_g1
- humanoid_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.03738v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'AMO: Adaptive Motion Optimization for Hyper-Dexterous Humanoid Whole-Body Control'
  url: https://arxiv.org/abs/2505.03738
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- method
---
## 概述
AMO框架通过整合仿真到现实强化学习与轨迹优化，解决了高自由度人形机器人非线性动力学带来的控制挑战。它构建了一个混合AMO数据集，用于训练网络，使其能够对潜在的分布外命令进行鲁棒、按需的适应。在仿真和29自由度Unitree G1人形机器人上的实验表明，AMO相比强基线方法展现出更优的稳定性和更大的工作空间。此外，AMO的一致性能支持通过模仿学习实现自主任务执行，突显了系统的多功能性和鲁棒性。

## 核心内容
### 方法
AMO框架的核心是结合仿真到现实强化学习与轨迹优化，以实现实时、自适应的全身控制。为了缓解运动模仿强化学习中的分布偏差，研究团队构建了一个混合AMO数据集，并训练了一个网络，使其能够对潜在的分布外命令进行鲁棒、按需的适应。

### 架构
AMO采用了一种集成架构，其中强化学习策略与轨迹优化器协同工作。强化学习部分负责从仿真环境中学习基础运动技能，而轨迹优化器则用于在线调整运动轨迹，以应对现实世界中的动态变化。这种设计使得系统能够在保持实时性的同时，适应复杂的任务需求。

### 实验设置
实验在仿真环境和29自由度Unitree G1人形机器人上进行了验证。任务包括从地面拾取物体等需要大工作空间的操作。对比的基线方法包括传统的全身控制方法和纯强化学习方法。

### 关键数字
- 机器人自由度：29 DoF
- 验证任务：地面拾取物体
- 性能提升：相比强基线方法，AMO在稳定性上显著提升，并扩展了工作空间

### 结论
AMO框架通过结合仿真到现实强化学习与轨迹优化，成功实现了高灵巧人形机器人的实时全身控制。其一致性能支持通过模仿学习进行自主任务执行，证明了系统的多功能性和鲁棒性。未来工作可进一步探索在更复杂环境中的应用。

## Overview
Humanoid robots derive much of their dexterity from hyper-dexterous whole-body movements, enabling tasks that require a large operational workspace: such as picking objects off the ground. However, achieving these capabilities on real humanoids remains challenging due to their high degrees of freedom (DoF) and nonlinear dynamics. We propose Adaptive Motion Optimization (AMO), a framework that integrates sim-to-real reinforcement learning (RL) with trajectory optimization for real-time, adaptive whole-body control. To mitigate distribution bias in motion imitation RL, we construct a hybrid AMO dataset and train a network capable of robust, on-demand adaptation to potentially O.O.D. commands. We validate AMO in simulation and on a 29-DoF Unitree G1 humanoid robot, demonstrating superior stability and an expanded workspace compared to strong baselines. Finally, we show that AMO's consistent performance supports autonomous task execution via imitation learning, underscoring the system's versatility and robustness.

## 개요
휴머노이드 로봇은 초정밀 전신 움직임을 통해 대부분의 기민함을 얻으며, 이는 넓은 작업 공간을 필요로 하는 작업(예: 바닥에서 물체 집기)을 가능하게 합니다. 그러나 높은 자유도(DoF)와 비선형 동역학으로 인해 실제 휴머노이드에서 이러한 능력을 구현하는 것은 여전히 어려운 과제입니다. 본 연구에서는 시뮬레이션-실제 강화 학습(sim-to-real RL)과 궤적 최적화를 통합하여 실시간 적응형 전신 제어를 가능하게 하는 Adaptive Motion Optimization (AMO) 프레임워크를 제안합니다. 모션 모방 강화 학습에서의 분포 편향을 완화하기 위해 하이브리드 AMO 데이터셋을 구축하고, 잠재적으로 O.O.D. 명령에 대해 강건하고 요구 기반 적응이 가능한 네트워크를 학습시킵니다. AMO를 시뮬레이션과 29-DoF Unitree G1 휴머노이드 로봇에서 검증하여, 강력한 기준선 대비 우수한 안정성과 확장된 작업 공간을 입증합니다. 마지막으로, AMO의 일관된 성능이 모방 학습을 통한 자율 작업 실행을 지원함을 보여주며, 시스템의 다재다능함과 강건성을 강조합니다.

## 핵심 내용
휴머노이드 로봇은 초정밀 전신 움직임을 통해 대부분의 기민함을 얻으며, 이는 넓은 작업 공간을 필요로 하는 작업(예: 바닥에서 물체 집기)을 가능하게 합니다. 그러나 높은 자유도(DoF)와 비선형 동역학으로 인해 실제 휴머노이드에서 이러한 능력을 구현하는 것은 여전히 어려운 과제입니다. 본 연구에서는 시뮬레이션-실제 강화 학습(sim-to-real RL)과 궤적 최적화를 통합하여 실시간 적응형 전신 제어를 가능하게 하는 Adaptive Motion Optimization (AMO) 프레임워크를 제안합니다. 모션 모방 강화 학습에서의 분포 편향을 완화하기 위해 하이브리드 AMO 데이터셋을 구축하고, 잠재적으로 O.O.D. 명령에 대해 강건하고 요구 기반 적응이 가능한 네트워크를 학습시킵니다. AMO를 시뮬레이션과 29-DoF Unitree G1 휴머노이드 로봇에서 검증하여, 강력한 기준선 대비 우수한 안정성과 확장된 작업 공간을 입증합니다. 마지막으로, AMO의 일관된 성능이 모방 학습을 통한 자율 작업 실행을 지원함을 보여주며, 시스템의 다재다능함과 강건성을 강조합니다.

## 参考
- http://arxiv.org/abs/2505.03738v1
