---
$id: ent_paper_robust_humanoid_walking_on_com_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL
  zh: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL
  ko: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL
summary:
  en: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL is a 2025 work on locomotion for humanoid robots.
  zh: 本文提出一种基于 sim-to-real 深度强化学习的方法，用于人形机器人在柔顺和不平坦地形上的稳健行走。核心贡献在于通过简单的训练课程让 RL 智能体在仿真中接触随机化地形，仅利用本体感受反馈即可实现真实机器人上的稳健行走。此外，通过允许机器人展现非周期性运动并调整步频，进一步提升了行走策略的鲁棒性。
  ko: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL is a 2025 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- locomotion
- robust_humanoid_walking_on_com
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2504.13619v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Robust Humanoid Walking on Compliant and Uneven Terrain with Deep RL (arXiv)
  url: https://arxiv.org/abs/2504.13619
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
该研究针对腿式机器人在真实环境中部署时面临的挑战，即地形可能具有意外变形和不规则性。作者探索了 sim-to-real 深度强化学习在双足行走控制器设计中的应用，核心创新是提出一种训练课程，使 RL 智能体在仿真中暴露于随机化地形，从而仅依赖本体感受反馈就能在真实 HRP-5P 人形机器人上实现稳健行走。实验在实验室内外多种困难地形上进行了广泛验证。此外，论文提出通过允许机器人展现非周期性运动并调整步频来增强行走策略的鲁棒性，具体通过修改时钟信号实现自适应步频，并在仿真中验证了该策略在控制摆动和支撑持续时间方面的有效性。

## 核心内容
### 方法
- 采用 sim-to-real 深度强化学习框架，训练端到端双足行走策略。
- 关键创新在于训练课程：在仿真中随机化地形属性（如柔顺性和不规则性），使策略学会适应真实世界的未知地形。
- 仅使用本体感受反馈（如关节角度、角速度、IMU 数据），无需外部感知输入。

### 架构
- 策略网络直接输出关节目标位置或扭矩，实现从感知到动作的端到端控制。
- 提出一种新的控制策略，允许修改观测到的时钟信号，从而根据地形和指令速度自适应调整步频。
- 通过控制摆动相和支撑相的持续时间，使机器人能够展现非周期性运动，提升在挑战性地形上的行走能力。

### 实验设置
- 真实机器人平台：HRP-5P 人形机器人。
- 测试环境：实验室内部及外部的多种困难地形，包括柔顺地面（如泡沫垫）和不规则表面（如碎石路）。
- 仿真实验用于验证自适应步频策略的有效性。

### 关键数字
- 在真实机器人上成功演示了多种困难地形的稳健行走。
- 仿真实验表明，自适应步频策略在挑战性地形上显著提升了行走性能。

### 结论
- 简单的训练课程结合 sim-to-real 迁移，足以让双足机器人仅靠本体感受反馈实现稳健行走。
- 允许非周期性运动和可变步频是提升双足行走策略鲁棒性的有效手段。
- 代码和演示视频已公开，便于复现和进一步研究。

## Overview
For the deployment of legged robots in real-world environments, it is essential to develop robust locomotion control methods for challenging terrains that may exhibit unexpected deformability and irregularity. In this paper, we explore the application of sim-to-real deep reinforcement learning (RL) for the design of bipedal locomotion controllers for humanoid robots on compliant and uneven terrains. Our key contribution is to show that a simple training curriculum for exposing the RL agent to randomized terrains in simulation can achieve robust walking on a real humanoid robot using only proprioceptive feedback. We train an end-to-end bipedal locomotion policy using the proposed approach, and show extensive real-robot demonstration on the HRP-5P humanoid over several difficult terrains inside and outside the lab environment. Further, we argue that the robustness of a bipedal walking policy can be improved if the robot is allowed to exhibit aperiodic motion with variable stepping frequency. We propose a new control policy to enable modification of the observed clock signal, leading to adaptive gait frequencies depending on the terrain and command velocity. Through simulation experiments, we show the effectiveness of this policy specifically for walking over challenging terrains by controlling swing and stance durations. The code for training and evaluation is available online at https://github.com/rohanpsingh/LearningHumanoidWalking. Demo video is available at https://www.youtube.com/watch?v=ZgfNzGAkk2Q.

## 개요
실제 환경에서 보행 로봇을 배치하려면 예상치 못한 변형성과 불규칙성을 보일 수 있는 까다로운 지형에 대한 강건한 보행 제어 방법을 개발하는 것이 필수적입니다. 본 논문에서는 시뮬레이션-실제 심층 강화 학습(RL)을 적용하여 유연하고 고르지 않은 지형에서 휴머노이드 로봇의 이족 보행 제어기를 설계하는 방법을 탐구합니다. 주요 기여는 시뮬레이션에서 RL 에이전트를 무작위 지형에 노출시키는 간단한 훈련 커리큘럼이 고유 감각 피드백만을 사용하여 실제 휴머노이드 로봇에서 강건한 보행을 달성할 수 있음을 보여주는 것입니다. 제안된 접근 방식을 사용하여 종단 간 이족 보행 정책을 훈련하고, 실험실 내외의 여러 까다로운 지형에서 HRP-5P 휴머노이드를 통해 광범위한 실제 로봇 시연을 보여줍니다. 또한, 로봇이 가변 보폭 주파수를 가진 비주기적 움직임을 보일 수 있도록 허용하면 이족 보행 정책의 강건성이 향상될 수 있다고 주장합니다. 관찰된 클록 신호를 수정할 수 있는 새로운 제어 정책을 제안하여 지형과 명령 속도에 따라 적응형 보행 주파수를 구현합니다. 시뮬레이션 실험을 통해 스윙 및 스탠스 지속 시간을 제어함으로써 까다로운 지형에서의 보행에 특히 효과적인 이 정책의 효용성을 입증합니다. 훈련 및 평가를 위한 코드는 https://github.com/rohanpsingh/LearningHumanoidWalking 에서 온라인으로 제공됩니다. 데모 비디오는 https://www.youtube.com/watch?v=ZgfNzGAkk2Q 에서 확인할 수 있습니다.

## 핵심 내용
실제 환경에서 보행 로봇을 배치하려면 예상치 못한 변형성과 불규칙성을 보일 수 있는 까다로운 지형에 대한 강건한 보행 제어 방법을 개발하는 것이 필수적입니다. 본 논문에서는 시뮬레이션-실제 심층 강화 학습(RL)을 적용하여 유연하고 고르지 않은 지형에서 휴머노이드 로봇의 이족 보행 제어기를 설계하는 방법을 탐구합니다. 주요 기여는 시뮬레이션에서 RL 에이전트를 무작위 지형에 노출시키는 간단한 훈련 커리큘럼이 고유 감각 피드백만을 사용하여 실제 휴머노이드 로봇에서 강건한 보행을 달성할 수 있음을 보여주는 것입니다. 제안된 접근 방식을 사용하여 종단 간 이족 보행 정책을 훈련하고, 실험실 내외의 여러 까다로운 지형에서 HRP-5P 휴머노이드를 통해 광범위한 실제 로봇 시연을 보여줍니다. 또한, 로봇이 가변 보폭 주파수를 가진 비주기적 움직임을 보일 수 있도록 허용하면 이족 보행 정책의 강건성이 향상될 수 있다고 주장합니다. 관찰된 클록 신호를 수정할 수 있는 새로운 제어 정책을 제안하여 지형과 명령 속도에 따라 적응형 보행 주파수를 구현합니다. 시뮬레이션 실험을 통해 스윙 및 스탠스 지속 시간을 제어함으로써 까다로운 지형에서의 보행에 특히 효과적인 이 정책의 효용성을 입증합니다. 훈련 및 평가를 위한 코드는 https://github.com/rohanpsingh/LearningHumanoidWalking 에서 온라인으로 제공됩니다. 데모 비디오는 https://www.youtube.com/watch?v=ZgfNzGAkk2Q 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2504.13619v1
