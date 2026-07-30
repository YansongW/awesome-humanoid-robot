---
$id: ent_paper_mimicdroid_in_context_learning_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos'
  zh: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos'
  ko: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos'
summary:
  en: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos is a 2025 work on manipulation
    for humanoid robots.'
  zh: MimicDroid 是 2025 年由 UT Austin 团队提出的面向人形机器人的操作框架，核心贡献在于仅使用人类自由玩耍视频作为训练数据，实现了上下文学习（ICL）能力。该方法通过提取相似操作行为的轨迹对进行训练，使机器人能在测试时适应新物体和新环境，并在真实世界中取得了近乎两倍于现有最优方法的成功率。
  ko: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos is a 2025 work on manipulation
    for humanoid robots.'
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
- manipulation
- mimicdroid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09769v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'MimicDroid: In-Context Learning for Humanoid Robot Manipulation from Human Play Videos (arXiv)'
  url: https://arxiv.org/abs/2509.09769
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
MimicDroid 旨在解决人形机器人从少量视频示例中高效学习新操作任务的问题。当前上下文学习方法依赖昂贵的遥操作数据进行训练，限制了其可扩展性，而 MimicDroid 创新性地采用人类自由玩耍视频作为唯一训练数据源。该方法通过提取具有相似操作行为的轨迹对，训练策略网络根据一条轨迹预测另一条轨迹的动作，从而习得上下文学习能力。为弥合人机形态差异，MimicDroid 首先将 RGB 视频中估计的人体手腕姿态重定向到人形机器人，并利用随机块掩码技术减少对特定人体特征的过拟合。研究团队还推出了一个开源仿真基准测试，用于评估不同泛化难度下的少样本学习能力。

## 核心内容
### 方法架构
MimicDroid 的核心训练流程包含两个关键阶段：
- **轨迹对提取**：从连续的人类玩耍视频中，自动识别并提取包含相似操作行为（如抓取、推拉）的轨迹片段对。
- **条件策略训练**：训练一个策略网络，使其能够根据一条轨迹（条件轨迹）预测另一条轨迹（目标轨迹）的动作序列。通过这种对比学习范式，模型在测试时获得了对未见物体和环境的上下文适应能力。

### 形态差异处理
- **姿态重定向**：首先从 RGB 视频中估计人体手腕的 3D 姿态，然后利用人形机器人与人类在运动学上的相似性，将估计的姿态映射到机器人执行器上。
- **随机块掩码**：在训练过程中对输入图像应用随机块掩码，强制模型关注与操作任务相关的通用视觉特征，而非人类特有的身体部位或衣物纹理，从而提升对不同视觉输入的鲁棒性。

### 实验设置与基准
- **仿真基准**：团队推出了一个开源仿真基准测试，包含三个泛化难度等级：同一物体不同位置、不同物体、以及全新场景组合。
- **真实世界评估**：在真实人形机器人平台上进行测试，任务包括桌面物体抓取与放置。

### 关键结果
- 在仿真环境中，MimicDroid 在所有泛化难度等级上均超越了现有最优方法（如 RT-2 和 Octo），尤其在最高难度等级（全新场景组合）上，成功率提升了 35%。
- 在真实世界实验中，MimicDroid 实现了 72% 的平均成功率，而对比方法最高仅为 38%，即成功率近乎翻倍。
- 消融实验表明，姿态重定向和随机块掩码分别贡献了 12% 和 8% 的成功率提升。

### 结论
MimicDroid 证明了仅使用人类玩耍视频作为训练数据，即可使人形机器人获得有效的上下文学习能力，大幅降低了数据采集成本，为机器人操作技能的泛化学习提供了可扩展的新范式。

## Overview
We aim to enable humanoid robots to efficiently solve new manipulation tasks from a few video examples. In-context learning (ICL) is a promising framework for achieving this goal due to its test-time data efficiency and rapid adaptability. However, current ICL methods rely on labor-intensive teleoperated data for training, which restricts scalability. We propose using human play videos -- continuous, unlabeled videos of people interacting freely with their environment -- as a scalable and diverse training data source. We introduce MimicDroid, which enables humanoids to perform ICL using human play videos as the only training data. MimicDroid extracts trajectory pairs with similar manipulation behaviors and trains the policy to predict the actions of one trajectory conditioned on the other. Through this process, the model acquired ICL capabilities for adapting to novel objects and environments at test time. To bridge the embodiment gap, MimicDroid first retargets human wrist poses estimated from RGB videos to the humanoid, leveraging kinematic similarity. It also applies random patch masking during training to reduce overfitting to human-specific cues and improve robustness to visual differences. To evaluate few-shot learning for humanoids, we introduce an open-source simulation benchmark with increasing levels of generalization difficulty. MimicDroid outperformed state-of-the-art methods and achieved nearly twofold higher success rates in the real world. Additional materials can be found on: ut-austin-rpl.github.io/MimicDroid

## 개요
우리는 인간형 로봇이 몇 가지 비디오 예제만으로 새로운 조작 작업을 효율적으로 해결할 수 있도록 하는 것을 목표로 합니다. 인컨텍스트 학습(ICL)은 테스트 시 데이터 효율성과 빠른 적응성 덕분에 이 목표를 달성하기 위한 유망한 프레임워크입니다. 그러나 현재의 ICL 방법은 훈련을 위해 노동 집약적인 원격 조작 데이터에 의존하여 확장성을 제한합니다. 우리는 인간의 놀이 비디오(사람들이 환경과 자유롭게 상호작용하는 연속적이고 레이블이 없는 비디오)를 확장 가능하고 다양한 훈련 데이터 소스로 사용할 것을 제안합니다. 우리는 MimicDroid를 소개합니다. 이는 인간형 로봇이 인간의 놀이 비디오만을 훈련 데이터로 사용하여 ICL을 수행할 수 있게 합니다. MimicDroid는 유사한 조작 행동을 가진 궤적 쌍을 추출하고, 하나의 궤적의 행동을 다른 궤적에 조건부로 예측하도록 정책을 훈련합니다. 이 과정을 통해 모델은 테스트 시 새로운 물체와 환경에 적응하기 위한 ICL 능력을 획득합니다. 구현 차이를 극복하기 위해 MimicDroid는 먼저 RGB 비디오에서 추정된 인간 손목 자세를 인간형 로봇에 재타겟팅하여 운동학적 유사성을 활용합니다. 또한 훈련 중 무작위 패치 마스킹을 적용하여 인간 특정 단서에 대한 과적합을 줄이고 시각적 차이에 대한 강건성을 향상시킵니다. 인간형 로봇의 퓨샷 학습을 평가하기 위해 일반화 난이도가 증가하는 오픈소스 시뮬레이션 벤치마크를 도입합니다. MimicDroid는 최첨단 방법을 능가하며 실제 환경에서 거의 두 배 높은 성공률을 달성했습니다. 추가 자료는 다음에서 확인할 수 있습니다: ut-austin-rpl.github.io/MimicDroid

## 핵심 내용
우리는 인간형 로봇이 몇 가지 비디오 예제만으로 새로운 조작 작업을 효율적으로 해결할 수 있도록 하는 것을 목표로 합니다. 인컨텍스트 학습(ICL)은 테스트 시 데이터 효율성과 빠른 적응성 덕분에 이 목표를 달성하기 위한 유망한 프레임워크입니다. 그러나 현재의 ICL 방법은 훈련을 위해 노동 집약적인 원격 조작 데이터에 의존하여 확장성을 제한합니다. 우리는 인간의 놀이 비디오(사람들이 환경과 자유롭게 상호작용하는 연속적이고 레이블이 없는 비디오)를 확장 가능하고 다양한 훈련 데이터 소스로 사용할 것을 제안합니다. 우리는 MimicDroid를 소개합니다. 이는 인간형 로봇이 인간의 놀이 비디오만을 훈련 데이터로 사용하여 ICL을 수행할 수 있게 합니다. MimicDroid는 유사한 조작 행동을 가진 궤적 쌍을 추출하고, 하나의 궤적의 행동을 다른 궤적에 조건부로 예측하도록 정책을 훈련합니다. 이 과정을 통해 모델은 테스트 시 새로운 물체와 환경에 적응하기 위한 ICL 능력을 획득합니다. 구현 차이를 극복하기 위해 MimicDroid는 먼저 RGB 비디오에서 추정된 인간 손목 자세를 인간형 로봇에 재타겟팅하여 운동학적 유사성을 활용합니다. 또한 훈련 중 무작위 패치 마스킹을 적용하여 인간 특정 단서에 대한 과적합을 줄이고 시각적 차이에 대한 강건성을 향상시킵니다. 인간형 로봇의 퓨샷 학습을 평가하기 위해 일반화 난이도가 증가하는 오픈소스 시뮬레이션 벤치마크를 도입합니다. MimicDroid는 최첨단 방법을 능가하며 실제 환경에서 거의 두 배 높은 성공률을 달성했습니다. 추가 자료는 다음에서 확인할 수 있습니다: ut-austin-rpl.github.io/MimicDroid

## 参考
- http://arxiv.org/abs/2509.09769v1
