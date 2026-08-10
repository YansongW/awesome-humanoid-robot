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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.09769v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1073 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.09769v1

## 개요
MimicDroid는 인간형 로봇이 소량의 비디오 예시만으로 새로운 조작 작업을 효율적으로 학습하는 문제를 해결하는 것을 목표로 합니다. 현재의 맥락 학습 방법은 고가의 원격 조작 데이터를 학습에 의존하여 확장성을 제한하는 반면, MimicDroid는 인간의 자유로운 놀이 비디오를 유일한 학습 데이터 소스로 혁신적으로 사용합니다. 이 방법은 유사한 조작 행동을 가진 궤적 쌍을 추출하여, 정책 네트워크가 한 궤적을 기반으로 다른 궤적의 동작을 예측하도록 학습시켜 맥락 학습 능력을 습득합니다. 인간-로봇 형태 차이를 극복하기 위해, MimicDroid는 먼저 RGB 비디오에서 추정된 인간 손목 자세를 인간형 로봇에 재지정하고, 무작위 블록 마스킹 기법을 사용하여 특정 인간 특징에 대한 과적합을 줄입니다. 연구팀은 또한 다양한 일반화 난이도에서의 소수 샷 학습 능력을 평가하기 위한 오픈소스 시뮬레이션 벤치마크를 공개했습니다.

## 핵심 내용
### 방법 아키텍처
MimicDroid의 핵심 학습 프로세스는 두 가지 주요 단계를 포함합니다:
- **궤적 쌍 추출**: 연속적인 인간 놀이 비디오에서 유사한 조작 행동(예: 잡기, 밀기/당기기)을 포함하는 궤적 세그먼트 쌍을 자동으로 식별하고 추출합니다.
- **조건부 정책 학습**: 한 궤적(조건 궤적)을 기반으로 다른 궤적(목표 궤적)의 동작 시퀀스를 예측할 수 있는 정책 네트워크를 학습합니다. 이러한 대조 학습 패러다임을 통해, 모델은 테스트 시 보지 못한 객체와 환경에 대한 맥락 적응 능력을 획득합니다.

### 형태 차이 처리
- **자세 재지정**: 먼저 RGB 비디오에서 인간 손목의 3D 자세를 추정한 다음, 인간형 로봇과 인간의 운동학적 유사성을 활용하여 추정된 자세를 로봇 액추에이터에 매핑합니다.
- **무작위 블록 마스킹**: 학습 과정에서 입력 이미지에 무작위 블록 마스킹을 적용하여, 모델이 인간 특유의 신체 부위나 의복 질감보다는 조작 작업과 관련된 일반적인 시각적 특징에 집중하도록 강제함으로써 다양한 시각적 입력에 대한 강건성을 향상시킵니다.

### 실험 설정 및 벤치마크
- **시뮬레이션 벤치마크**: 연구팀은 세 가지 일반화 난이도 수준(동일 객체의 다른 위치, 다른 객체, 완전히 새로운 장면 조합)을 포함하는 오픈소스 시뮬레이션 벤치마크를 공개했습니다.
- **실제 환경 평가**: 실제 인간형 로봇 플랫폼에서 테스트를 수행하며, 작업에는 테이블 위 객체 잡기 및 배치가 포함됩니다.

### 주요 결과
- 시뮬레이션 환경에서 MimicDroid는 모든 일반화 난이도 수준에서 기존 최고 성능 방법(예: RT-2 및 Octo)을 능가했으며, 특히 최고 난이도 수준(완전히 새로운 장면 조합)에서 성공률이 35% 향상되었습니다.
- 실제 실험에서 MimicDroid는 평균 성공률 72%를 달성했으며, 비교 방법의 최고 성능은 38%에 불과하여 성공률이 거의 두 배로 증가했습니다.
- 절제 실험에 따르면 자세 재지정과 무작위 블록 마스킹은 각각 12%와 8%의 성공률 향상에 기여했습니다.

### 결론
MimicDroid는 인간 놀이 비디오만을 학습 데이터로 사용하여 인간형 로봇이 효과적인 맥락 학습 능력을 획득할 수 있음을 입증했으며, 데이터 수집 비용을 크게 줄이고 로봇 조작 기술의 일반화 학습을 위한 확장 가능한 새로운 패러다임을 제공합니다.
