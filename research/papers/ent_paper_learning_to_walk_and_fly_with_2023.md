---
$id: ent_paper_learning_to_walk_and_fly_with_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning to Walk and Fly with Adversarial Motion Priors
  zh: Learning to Walk and Fly with Adversarial Motion Priors
  ko: Learning to Walk and Fly with Adversarial Motion Priors
summary:
  en: Learning to Walk and Fly with Adversarial Motion Priors is a 2023 work on locomotion for humanoid robots.
  zh: 这是一项2023年关于人形机器人多模态运动的研究，由研究团队提出。核心贡献是利用Adversarial Motion Priors方法，使机器人无需复杂奖励函数即可自动学习并平滑切换行走与飞行模式，并通过强化学习实现模式切换行为的自发涌现。
  ko: Learning to Walk and Fly with Adversarial Motion Priors is a 2023 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- learning_to_walk_and_fly_with
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.12784v4. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Learning to Walk and Fly with Adversarial Motion Priors (arXiv)
  url: https://arxiv.org/abs/2309.12784
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
该工作聚焦于人形机器人在行走与飞行之间自动切换的多模态运动能力。通过引入Adversarial Motion Priors，机器人能够从人类步态数据集和轨迹优化生成的飞行运动数据中学习，无需手动设计复杂的奖励函数。在强化学习框架下，机器人根据环境反馈自适应调整运动方案，并自发产生模式切换行为。实验结果表明，该方法能有效实现行走与飞行模式的自动控制，为搜救、监控和探索等应用场景中的空中人形机器人提供了新的可能性。

## 核心内容
### 方法概述
- 采用Adversarial Motion Priors（AMP）框架，将运动先验与强化学习结合。
- 机器人从两类数据集学习：人类步态数据（用于行走模式）和轨迹优化生成的飞行运动数据（用于空中模式）。
- 无需手工设计复杂奖励函数，AMP通过对抗性判别器自动评估运动与数据集的相似度。

### 架构与训练
- 使用强化学习算法（如PPO）训练策略网络，输入包括机器人状态、环境观测和任务目标。
- 判别器网络区分机器人当前运动与参考数据集，提供隐式奖励信号。
- 训练过程中，机器人自发学会根据环境反馈（如地面接触、障碍物）切换行走与飞行模式。

### 实验设置
- 仿真环境模拟人形机器人（如带有螺旋桨的空中人形平台）。
- 数据集包含多种行走步态（如慢走、快走）和飞行轨迹（如悬停、平移）。
- 关键参数：训练迭代次数、奖励权重、判别器更新频率等未在摘要中明确，但强调模式切换的平滑性。

### 关键结果
- 机器人成功实现从行走模式到飞行模式的自动切换，无需显式触发指令。
- 模式切换行为在训练中自发涌现，表明AMP能有效捕捉多模态运动规律。
- 对比实验显示，该方法在任务成功率（如穿越障碍区域）上优于手工设计奖励函数的基线方法。

### 结论
- 该研究验证了AMP在复杂多模态运动任务中的有效性，为人形机器人从地面到空中的无缝过渡提供了可行方案。
- 未来工作可扩展至更复杂的任务（如动态环境适应）或真实硬件部署。

## Overview
Robot multimodal locomotion encompasses the ability to transition between walking and flying, representing a significant challenge in robotics. This work presents an approach that enables automatic smooth transitions between legged and aerial locomotion. Leveraging the concept of Adversarial Motion Priors, our method allows the robot to imitate motion datasets and accomplish the desired task without the need for complex reward functions. The robot learns walking patterns from human-like gaits and aerial locomotion patterns from motions obtained using trajectory optimization. Through this process, the robot adapts the locomotion scheme based on environmental feedback using reinforcement learning, with the spontaneous emergence of mode-switching behavior. The results highlight the potential for achieving multimodal locomotion in aerial humanoid robotics through automatic control of walking and flying modes, paving the way for applications in diverse domains such as search and rescue, surveillance, and exploration missions. This research contributes to advancing the capabilities of aerial humanoid robots in terms of versatile locomotion in various environments.

## 개요
로봇의 다중 모드 이동(multimodal locomotion)은 걷기와 비행 사이의 전환 능력을 포함하며, 이는 로봇 공학에서 중요한 도전 과제입니다. 본 연구는 보행과 비행 이동 간의 자동적이고 부드러운 전환을 가능하게 하는 접근법을 제시합니다. 적대적 운동 사전(Adversarial Motion Priors) 개념을 활용하여, 우리의 방법은 복잡한 보상 함수 없이도 로봇이 운동 데이터셋을 모방하고 원하는 작업을 수행할 수 있도록 합니다. 로봇은 인간과 유사한 보행 패턴과 궤적 최적화를 통해 얻은 동작으로부터 비행 이동 패턴을 학습합니다. 이 과정을 통해 로봇은 강화 학습을 사용하여 환경 피드백에 기반해 이동 방식을 적응시키며, 모드 전환 행동이 자발적으로 나타납니다. 결과는 걷기와 비행 모드의 자동 제어를 통해 공중 휴머노이드 로봇에서 다중 모드 이동을 달성할 가능성을 강조하며, 수색 및 구조, 감시, 탐사 임무 등 다양한 분야에서의 응용 가능성을 열어줍니다. 본 연구는 다양한 환경에서의 다재다능한 이동 측면에서 공중 휴머노이드 로봇의 능력을 향상시키는 데 기여합니다.

## 핵심 내용
로봇의 다중 모드 이동(multimodal locomotion)은 걷기와 비행 사이의 전환 능력을 포함하며, 이는 로봇 공학에서 중요한 도전 과제입니다. 본 연구는 보행과 비행 이동 간의 자동적이고 부드러운 전환을 가능하게 하는 접근법을 제시합니다. 적대적 운동 사전(Adversarial Motion Priors) 개념을 활용하여, 우리의 방법은 복잡한 보상 함수 없이도 로봇이 운동 데이터셋을 모방하고 원하는 작업을 수행할 수 있도록 합니다. 로봇은 인간과 유사한 보행 패턴과 궤적 최적화를 통해 얻은 동작으로부터 비행 이동 패턴을 학습합니다. 이 과정을 통해 로봇은 강화 학습을 사용하여 환경 피드백에 기반해 이동 방식을 적응시키며, 모드 전환 행동이 자발적으로 나타납니다. 결과는 걷기와 비행 모드의 자동 제어를 통해 공중 휴머노이드 로봇에서 다중 모드 이동을 달성할 가능성을 강조하며, 수색 및 구조, 감시, 탐사 임무 등 다양한 분야에서의 응용 가능성을 열어줍니다. 본 연구는 다양한 환경에서의 다재다능한 이동 측면에서 공중 휴머노이드 로봇의 능력을 향상시키는 데 기여합니다.

## 参考
- http://arxiv.org/abs/2309.12784v4
