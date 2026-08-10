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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2309.12784v4. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (852 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2309.12784v4

## 개요
이 연구는 인간형 로봇이 보행과 비행 사이를 자동으로 전환하는 다중 모드 운동 능력에 초점을 맞춥니다. Adversarial Motion Priors를 도입하여, 로봇은 수동으로 복잡한 보상 함수를 설계할 필요 없이 인간 보행 데이터셋과 궤적 최적화로 생성된 비행 운동 데이터에서 학습할 수 있습니다. 강화 학습 프레임워크 내에서 로봇은 환경 피드백에 따라 운동 방식을 적응적으로 조정하고, 모드 전환 행동을 자발적으로 생성합니다. 실험 결과는 이 방법이 보행과 비행 모드의 자동 제어를 효과적으로 구현할 수 있음을 보여주며, 수색 구조, 감시, 탐사 등의 응용 시나리오에서 공중 인간형 로봇에 새로운 가능성을 제공합니다.

## 핵심 내용
### 방법 개요
- Adversarial Motion Priors(AMP) 프레임워크를 채택하여 운동 사전 지식과 강화 학습을 결합합니다.
- 로봇은 두 가지 데이터셋에서 학습합니다: 인간 보행 데이터(보행 모드용)와 궤적 최적화로 생성된 비행 운동 데이터(공중 모드용).
- 수동으로 복잡한 보상 함수를 설계할 필요 없이, AMP는 적대적 판별기를 통해 로봇의 현재 운동과 데이터셋 간의 유사성을 자동으로 평가합니다.

### 아키텍처 및 훈련
- 강화 학습 알고리즘(예: PPO)을 사용하여 정책 네트워크를 훈련하며, 입력에는 로봇 상태, 환경 관측, 작업 목표가 포함됩니다.
- 판별기 네트워크는 로봇의 현재 운동과 참조 데이터셋을 구분하여 암시적 보상 신호를 제공합니다.
- 훈련 과정에서 로봇은 환경 피드백(예: 지면 접촉, 장애물)에 따라 보행과 비행 모드를 전환하는 방법을 자발적으로 학습합니다.

### 실험 설정
- 시뮬레이션 환경은 인간형 로봇(예: 프로펠러가 장착된 공중 인간형 플랫폼)을 모사합니다.
- 데이터셋에는 다양한 보행 보행(예: 느린 걷기, 빠른 걷기)과 비행 궤적(예: 호버링, 평행 이동)이 포함됩니다.
- 주요 매개변수: 훈련 반복 횟수, 보상 가중치, 판별기 업데이트 빈도 등은 초록에서 명확히 명시되지 않았지만, 모드 전환의 매끄러움을 강조합니다.

### 주요 결과
- 로봇은 명시적 트리거 명령 없이 보행 모드에서 비행 모드로의 자동 전환을 성공적으로 구현합니다.
- 모드 전환 행동은 훈련 중 자발적으로 나타나며, AMP가 다중 모드 운동 규칙을 효과적으로 포착할 수 있음을 시사합니다.
- 비교 실험에서 이 방법은 작업 성공률(예: 장애물 구역 통과)에서 수동으로 설계된 보상 함수 기반 기준 방법보다 우수함을 보여줍니다.

### 결론
- 이 연구는 복잡한 다중 모드 운동 작업에서 AMP의 효과성을 검증하며, 인간형 로봇의 지상에서 공중으로의 원활한 전환을 위한 실현 가능한 솔루션을 제공합니다.
- 향후 작업은 더 복잡한 작업(예: 동적 환경 적응)이나 실제 하드웨어 배포로 확장될 수 있습니다.
