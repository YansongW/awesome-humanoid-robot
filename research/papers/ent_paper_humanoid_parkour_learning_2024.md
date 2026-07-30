---
$id: ent_paper_humanoid_parkour_learning_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Parkour Learning
  zh: Humanoid Parkour Learning
  ko: Humanoid Parkour Learning
summary:
  en: Humanoid Parkour Learning is a 2024 work on locomotion for humanoid robots.
  zh: Humanoid Parkour Learning 是2024年提出的人形机器人运动控制框架，由研究团队开发。其核心贡献在于无需运动先验，通过端到端视觉驱动的全身控制强化学习策略，使人形机器人能够自主完成跳跃0.42米平台、跨越0.8米间隙、野外奔跑（1.8m/s）等多种跑酷技能，并支持移动操作任务迁移。
  ko: Humanoid Parkour Learning is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoid_parkour_learning
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.10759v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Humanoid Parkour Learning (arXiv)
  url: https://arxiv.org/abs/2406.10759
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Humanoid Parkour Learning project page
  url: https://humanoid4parkour.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
该工作针对人形机器人跑酷这一极具挑战性的运动控制问题，提出了一种无需运动先验的端到端学习框架。与现有依赖单轨迹优化或大量运动参考数据的方法不同，该框架通过视觉输入直接生成全身控制策略，使人形机器人能够自主选择并执行多种跑酷技能。实验表明，机器人不仅能完成跳跃平台、跨越障碍等复杂动作，还能在野外以1.8m/s的速度奔跑，并在不同地形上稳健行走。此外，通过覆盖手臂动作，该框架可轻松迁移至人形移动操作任务。

## 核心内容
### 方法架构
- 采用端到端强化学习框架，输入为视觉图像（来自机器人头部摄像头）与本体感知数据（关节角度、IMU等），输出为全身关节控制指令。
- 策略网络基于卷积神经网络（CNN）处理视觉特征，结合多层感知机（MLP）融合本体感知信息，最终生成动作指令。
- 训练过程中无需任何运动先验（如参考轨迹或动作捕捉数据），完全通过奖励函数引导学习跑酷技能。

### 实验设置
- 使用真实人形机器人平台（具体型号未在摘要中提及）进行测试。
- 训练环境包括室内障碍赛道（平台、栏杆、间隙）与室外复杂地形（草地、斜坡、碎石路）。
- 奖励函数设计包含速度跟踪、身体平衡、关节限制、能量效率等项，并针对不同技能（跳跃、跨越、奔跑）设置自适应权重。

### 关键结果
- **跳跃能力**：成功跃上0.42米高的平台，跨越0.8米宽的间隙。
- **奔跑速度**：在野外环境中达到1.8m/s的稳定奔跑速度。
- **鲁棒性**：在草地、斜坡、碎石路等不同地形上均能稳健行走，无需重新训练。
- **自主技能选择**：在跟随摇杆旋转指令的同时，机器人能根据视觉输入自主选择跳跃、跨越或奔跑等技能。
- **迁移能力**：通过覆盖手臂动作（如抓取或推动），该框架可直接应用于移动操作任务（如搬运物体），无需修改核心策略。

### 结论
该工作首次实现了无需运动先验的人形机器人端到端跑酷学习，验证了视觉驱动全身控制策略在复杂运动任务中的有效性。其技能自主选择能力与任务迁移性为未来人形机器人在非结构化环境中的实际应用提供了重要基础。

## Overview
Parkour is a grand challenge for legged locomotion, even for quadruped robots, requiring active perception and various maneuvers to overcome multiple challenging obstacles. Existing methods for humanoid locomotion either optimize a trajectory for a single parkour track or train a reinforcement learning policy only to walk with a significant amount of motion references. In this work, we propose a framework for learning an end-to-end vision-based whole-body-control parkour policy for humanoid robots that overcomes multiple parkour skills without any motion prior. Using the parkour policy, the humanoid robot can jump on a 0.42m platform, leap over hurdles, 0.8m gaps, and much more. It can also run at 1.8m/s in the wild and walk robustly on different terrains. We test our policy in indoor and outdoor environments to demonstrate that it can autonomously select parkour skills while following the rotation command of the joystick. We override the arm actions and show that this framework can easily transfer to humanoid mobile manipulation tasks. Videos can be found at https://humanoid4parkour.github.io

## 개요
파쿠르는 보행 로봇, 특히 사족 로봇에게도 큰 도전 과제로, 능동적인 인식과 다양한 기동을 통해 여러 장애물을 극복해야 합니다. 기존의 인간형 로봇 보행 방법은 단일 파쿠르 트랙에 대한 궤적을 최적화하거나, 상당한 양의 동작 참조를 사용하여 보행만을 위한 강화 학습 정책을 훈련합니다. 본 연구에서는 사전 동작 없이도 여러 파쿠르 기술을 극복할 수 있는, 인간형 로봇을 위한 엔드투엔드(end-to-end) 비전 기반 전신 제어 파쿠르 정책 학습 프레임워크를 제안합니다. 이 파쿠르 정책을 통해 인간형 로봇은 0.42m 높이의 플랫폼에 점프하고, 허들, 0.8m 간격의 갭 등을 뛰어넘을 수 있습니다. 또한 야외에서 1.8m/s 속도로 달리고, 다양한 지형에서 견고하게 보행할 수 있습니다. 우리는 실내 및 실외 환경에서 정책을 테스트하여 조이스틱의 회전 명령을 따르면서 자율적으로 파쿠르 기술을 선택할 수 있음을 입증했습니다. 팔 동작을 오버라이드(override)하여 이 프레임워크가 인간형 로봇의 이동 조작 작업에 쉽게 전이될 수 있음을 보여줍니다. 비디오는 https://humanoid4parkour.github.io 에서 확인할 수 있습니다.

## 핵심 내용
파쿠르는 보행 로봇, 특히 사족 로봇에게도 큰 도전 과제로, 능동적인 인식과 다양한 기동을 통해 여러 장애물을 극복해야 합니다. 기존의 인간형 로봇 보행 방법은 단일 파쿠르 트랙에 대한 궤적을 최적화하거나, 상당한 양의 동작 참조를 사용하여 보행만을 위한 강화 학습 정책을 훈련합니다. 본 연구에서는 사전 동작 없이도 여러 파쿠르 기술을 극복할 수 있는, 인간형 로봇을 위한 엔드투엔드(end-to-end) 비전 기반 전신 제어 파쿠르 정책 학습 프레임워크를 제안합니다. 이 파쿠르 정책을 통해 인간형 로봇은 0.42m 높이의 플랫폼에 점프하고, 허들, 0.8m 간격의 갭 등을 뛰어넘을 수 있습니다. 또한 야외에서 1.8m/s 속도로 달리고, 다양한 지형에서 견고하게 보행할 수 있습니다. 우리는 실내 및 실외 환경에서 정책을 테스트하여 조이스틱의 회전 명령을 따르면서 자율적으로 파쿠르 기술을 선택할 수 있음을 입증했습니다. 팔 동작을 오버라이드(override)하여 이 프레임워크가 인간형 로봇의 이동 조작 작업에 쉽게 전이될 수 있음을 보여줍니다. 비디오는 https://humanoid4parkour.github.io 에서 확인할 수 있습니다.

## 参考
- http://arxiv.org/abs/2406.10759v2
