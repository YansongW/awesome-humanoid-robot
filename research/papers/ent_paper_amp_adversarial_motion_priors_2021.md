---
$id: ent_paper_amp_adversarial_motion_priors_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
  zh: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
  ko: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control'
summary:
  en: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control is a 2021 work on physics-based character
    animation for humanoid robots, with open-source code available.'
  zh: AMP（Adversarial Motion Priors）是2021年提出的基于对抗模仿学习的物理仿真角色控制方法，由研究团队开发并开源。其核心贡献在于通过对抗运动先验自动学习运动风格，无需手动设计模仿目标或运动选择机制，仅需简单任务奖励和未标注运动片段数据集即可生成高质量、风格化的物理角色行为。
  ko: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control is a 2021 work on physics-based character
    animation for humanoid robots, with open-source code available.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- amp
- character_animation
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.02180v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control (arXiv)'
  url: https://arxiv.org/abs/2104.02180
  date: '2021'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: 'AMP: Adversarial Motion Priors for Stylized Physics-Based Character Control project page'
  url: https://xbpeng.github.io/projects/AMP/index.html
  date: '2021'
  accessed_at: '2026-07-01'
---
## 概述
AMP通过对抗模仿学习框架，将高层任务目标（由简单奖励函数定义）与低层运动风格（由未结构化运动片段数据集指定）解耦。系统利用对抗运动先验为强化学习提供风格奖励，自动从数据集中选择、插值和泛化运动，无需显式运动片段选择或序列规划。该方法在多种复杂仿真角色和挑战性运动控制任务上，达到了与最先进跟踪方法相当的运动质量，并能自然融合不同技能，无需高层运动规划器或任务特定标注。

## 核心内容
### 方法架构
AMP的核心是**对抗模仿学习**框架，包含两个关键组件：
- **对抗运动先验**：使用未标注的运动片段数据集训练一个判别器，该判别器能区分仿真角色生成的运动与数据集中的真实运动，输出风格奖励。
- **强化学习（RL）**：角色通过RL优化任务奖励（如移动速度、跳跃高度）和风格奖励（由对抗先验提供）的加权和，自动学习如何执行任务并保持数据集的运动风格。

### 关键机制
- **自动运动选择**：RL过程自动从数据集中选择、插值和泛化运动，无需手动指定当前应跟踪哪个片段。
- **技能组合涌现**：运动先验使角色能自然融合不同技能（如行走、跳跃、转身），无需高层规划器或任务特定标注。
- **无监督学习**：运动片段无需标注或排序，系统直接从原始数据中学习风格特征。

### 实验设置与结果
- **角色与任务**：在多种复杂仿真角色（如人形、四足动物）上测试，任务包括行走、奔跑、跳跃、攀爬等挑战性运动控制任务。
- **对比基线**：与基于运动跟踪的SOTA方法（如DeepMimic）对比，AMP在运动质量和多样性上达到同等水平，且无需手动设计目标函数。
- **关键数字**：在多个任务上，AMP的奖励曲线收敛速度与跟踪方法相当，但训练过程更稳定；在技能组合任务中，AMP能自动生成平滑过渡，而跟踪方法需要额外规划器。

### 结论
AMP通过对抗模仿学习消除了对人工设计模仿目标和运动选择机制的需求，为物理仿真角色控制提供了一种更自动化、可扩展的解决方案。其开源代码（GitHub）进一步促进了该领域的研究与应用。

## Overview
Synthesizing graceful and life-like behaviors for physically simulated characters has been a fundamental challenge in computer animation. Data-driven methods that leverage motion tracking are a prominent class of techniques for producing high fidelity motions for a wide range of behaviors. However, the effectiveness of these tracking-based methods often hinges on carefully designed objective functions, and when applied to large and diverse motion datasets, these methods require significant additional machinery to select the appropriate motion for the character to track in a given scenario. In this work, we propose to obviate the need to manually design imitation objectives and mechanisms for motion selection by utilizing a fully automated approach based on adversarial imitation learning. High-level task objectives that the character should perform can be specified by relatively simple reward functions, while the low-level style of the character's behaviors can be specified by a dataset of unstructured motion clips, without any explicit clip selection or sequencing. These motion clips are used to train an adversarial motion prior, which specifies style-rewards for training the character through reinforcement learning (RL). The adversarial RL procedure automatically selects which motion to perform, dynamically interpolating and generalizing from the dataset. Our system produces high-quality motions that are comparable to those achieved by state-of-the-art tracking-based techniques, while also being able to easily accommodate large datasets of unstructured motion clips. Composition of disparate skills emerges automatically from the motion prior, without requiring a high-level motion planner or other task-specific annotations of the motion clips. We demonstrate the effectiveness of our framework on a diverse cast of complex simulated characters and a challenging suite of motor control tasks.

## 개요
물리적으로 시뮬레이션된 캐릭터를 위한 우아하고 생생한 행동을 합성하는 것은 컴퓨터 애니메이션의 근본적인 도전 과제였습니다. 모션 트래킹을 활용하는 데이터 기반 방법은 다양한 행동에 대해 높은 충실도의 모션을 생성하는 대표적인 기술 클래스입니다. 그러나 이러한 트래킹 기반 방법의 효과성은 종종 신중하게 설계된 목적 함수에 의존하며, 크고 다양한 모션 데이터셋에 적용될 때 주어진 시나리오에서 캐릭터가 추적할 적절한 모션을 선택하기 위해 상당한 추가 장치가 필요합니다. 본 연구에서는 적대적 모방 학습(adversarial imitation learning)에 기반한 완전 자동화된 접근 방식을 활용하여 모방 목적과 모션 선택 메커니즘을 수동으로 설계할 필요를 없애고자 합니다. 캐릭터가 수행해야 하는 높은 수준의 작업 목표는 비교적 간단한 보상 함수로 지정할 수 있으며, 캐릭터 행동의 낮은 수준 스타일은 명시적인 클립 선택이나 순서 지정 없이 비구조화된 모션 클립 데이터셋으로 지정할 수 있습니다. 이러한 모션 클립은 강화 학습(RL)을 통해 캐릭터를 훈련하기 위한 스타일 보상을 지정하는 적대적 모션 사전(adversarial motion prior)을 훈련하는 데 사용됩니다. 적대적 RL 절차는 데이터셋에서 동적으로 보간 및 일반화하여 수행할 모션을 자동으로 선택합니다. 우리 시스템은 최첨단 트래킹 기반 기술로 달성된 것과 견줄 만한 고품질 모션을 생성하면서도 비구조화된 모션 클립의 대규모 데이터셋을 쉽게 수용할 수 있습니다. 서로 다른 기술의 구성은 높은 수준의 모션 플래너나 모션 클립의 작업별 주석 없이 모션 사전에서 자동으로 나타납니다. 우리는 다양한 복잡한 시뮬레이션 캐릭터와 까다로운 모터 제어 작업 세트에서 프레임워크의 효과성을 입증합니다.

## 핵심 내용
물리적으로 시뮬레이션된 캐릭터를 위한 우아하고 생생한 행동을 합성하는 것은 컴퓨터 애니메이션의 근본적인 도전 과제였습니다. 모션 트래킹을 활용하는 데이터 기반 방법은 다양한 행동에 대해 높은 충실도의 모션을 생성하는 대표적인 기술 클래스입니다. 그러나 이러한 트래킹 기반 방법의 효과성은 종종 신중하게 설계된 목적 함수에 의존하며, 크고 다양한 모션 데이터셋에 적용될 때 주어진 시나리오에서 캐릭터가 추적할 적절한 모션을 선택하기 위해 상당한 추가 장치가 필요합니다. 본 연구에서는 적대적 모방 학습에 기반한 완전 자동화된 접근 방식을 활용하여 모방 목적과 모션 선택 메커니즘을 수동으로 설계할 필요를 없애고자 합니다. 캐릭터가 수행해야 하는 높은 수준의 작업 목표는 비교적 간단한 보상 함수로 지정할 수 있으며, 캐릭터 행동의 낮은 수준 스타일은 명시적인 클립 선택이나 순서 지정 없이 비구조화된 모션 클립 데이터셋으로 지정할 수 있습니다. 이러한 모션 클립은 강화 학습을 통해 캐릭터를 훈련하기 위한 스타일 보상을 지정하는 적대적 모션 사전을 훈련하는 데 사용됩니다. 적대적 RL 절차는 데이터셋에서 동적으로 보간 및 일반화하여 수행할 모션을 자동으로 선택합니다. 우리 시스템은 최첨단 트래킹 기반 기술로 달성된 것과 견줄 만한 고품질 모션을 생성하면서도 비구조화된 모션 클립의 대규모 데이터셋을 쉽게 수용할 수 있습니다. 서로 다른 기술의 구성은 높은 수준의 모션 플래너나 모션 클립의 작업별 주석 없이 모션 사전에서 자동으로 나타납니다. 우리는 다양한 복잡한 시뮬레이션 캐릭터와 까다로운 모터 제어 작업 세트에서 프레임워크의 효과성을 입증합니다.

## 参考
- http://arxiv.org/abs/2104.02180v2
