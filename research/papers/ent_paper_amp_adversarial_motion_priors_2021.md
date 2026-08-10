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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2104.02180v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (881 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2104.02180v2

## 개요
AMP는 적대적 모방 학습 프레임워크를 통해 고수준 작업 목표(간단한 보상 함수로 정의)와 저수준 동작 스타일(구조화되지 않은 모션 클립 데이터셋으로 지정)을 분리한다. 시스템은 적대적 동작 사전을 활용해 강화 학습에 스타일 보상을 제공하며, 명시적인 모션 클립 선택이나 시퀀스 계획 없이 데이터셋에서 자동으로 동작을 선택, 보간 및 일반화한다. 이 방법은 다양한 복잡한 시뮬레이션 캐릭터와 도전적인 운동 제어 작업에서 최신 추적 방법과 동등한 동작 품질을 달성하며, 고수준 동작 계획기나 작업별 주석 없이도 다양한 기술을 자연스럽게 융합할 수 있다.

## 핵심 내용
### 방법 아키텍처
AMP의 핵심은 **적대적 모방 학습** 프레임워크로, 두 가지 주요 구성 요소를 포함한다:
- **적대적 동작 사전**: 주석이 없는 모션 클립 데이터셋을 사용해 판별기를 훈련하며, 이 판별기는 시뮬레이션 캐릭터가 생성한 동작과 데이터셋의 실제 동작을 구분하여 스타일 보상을 출력한다.
- **강화 학습(RL)**: 캐릭터는 RL을 통해 작업 보상(예: 이동 속도, 점프 높이)과 스타일 보상(적대적 사전에서 제공)의 가중 합을 최적화하며, 작업 수행 방법과 데이터셋의 동작 스타일 유지를 자동으로 학습한다.

### 핵심 메커니즘
- **자동 동작 선택**: RL 과정은 현재 추적해야 할 클립을 수동으로 지정할 필요 없이 데이터셋에서 자동으로 동작을 선택, 보간 및 일반화한다.
- **기술 조합의 창발**: 동작 사전은 캐릭터가 걷기, 점프, 회전과 같은 다양한 기술을 고수준 계획기나 작업별 주석 없이 자연스럽게 융합할 수 있게 한다.
- **비지도 학습**: 모션 클립은 주석이나 정렬이 필요 없으며, 시스템은 원시 데이터에서 직접 스타일 특징을 학습한다.

### 실험 설정 및 결과
- **캐릭터 및 작업**: 다양한 복잡한 시뮬레이션 캐릭터(예: 휴머노이드, 사족 동물)에서 테스트했으며, 작업에는 걷기, 달리기, 점프, 등반 등 도전적인 운동 제어 작업이 포함된다.
- **비교 기준**: 동작 추적 기반의 최신 방법(예: DeepMimic)과 비교했을 때, AMP는 동작 품질과 다양성에서 동등한 수준을 달성하며 수동 목표 함수 설계가 필요 없다.
- **핵심 수치**: 여러 작업에서 AMP의 보상 곡선 수렴 속도는 추적 방법과 유사하지만 훈련 과정은 더 안정적이다. 기술 조합 작업에서 AMP는 자동으로 매끄러운 전환을 생성하는 반면, 추적 방법은 추가 계획기가 필요하다.

### 결론
AMP는 적대적 모방 학습을 통해 수동으로 설계된 모방 목표와 동작 선택 메커니즘의 필요성을 제거하여, 물리 시뮬레이션 캐릭터 제어를 위한 더 자동화되고 확장 가능한 솔루션을 제공한다. 오픈소스 코드(GitHub)는 이 분야의 연구와 응용을 더욱 촉진한다.
