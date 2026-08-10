---
$id: ent_paper_robotacdex_a_dexterous_visual_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation'
  zh: 'RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation'
  ko: 'RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation'
summary:
  en: 'arXiv:2606.31836v1 Announce Type: new Abstract: In the field of robot learning, large-scale and diverse demonstration
    trajectories provide the fundamental basis for enhancing robotic manipulation ability. We introduce RoboTacDex, a large,
    multi-modal, and diverse dataset of dexterous manipulation behaviors performed with a humanoid robot. Built on the publicly
    accessible humanoid robot Unitree G1, RoboTacDex consists of 6k trajectories covering 19 tasks, 23 skills, and interactions
    with 22 objects. RoboTacDex provides comprehensive records including multi-view RGB and depth information, tactile feedback,
    and detailed semantic annotations. Furthermore, the dataset features a variety of relatively challenging tasks that can
    only be completed by dual arms and dexterous hands, aiming to mimic human-like operational logic and simulate real-world
    manipulation complexity. To ensure data collection quality, we develop an improved multi-camera synchronization system
    to enable millisecond data synchronization and recording of modalities. In our experiments, we evaluate three representative
    imitation learning models on our dataset, analyzing their performance as well as their respective strengths and limitations
    across different task categories. Successful trial results and a moderate level of generalization capabilities across
    a suite of tasks indicate the effectiveness and diversity of the collected dataset. Our dataset will be open-sourced soon.'
  zh: RoboTacDex 是一个面向人形机器人灵巧操作的大规模多模态数据集，由研究团队基于 Unitree G1 机器人构建。该数据集包含 6000 条轨迹，覆盖 19 个任务、23 种技能和 22 种物体交互，并提供多视角 RGB-D、触觉反馈及语义标注。其核心贡献在于通过改进的多相机同步系统实现毫秒级数据采集，并验证了三种模仿学习模型在复杂双手机器人任务上的有效性。
  ko: 'arXiv:2606.31836v1 Announce Type: new Abstract: In the field of robot learning, large-scale and diverse demonstration
    trajectories provide the fundamental basis for enhancing robotic manipulation ability. We introduce RoboTacDex, a large,
    multi-modal, and diverse dataset of dexterous manipulation behaviors performed with a humanoid robot. Built on the publicly
    accessible humanoid robot Unitree G1, RoboTacDex consists of 6k trajectories covering 19 tasks, 23 skills, and interactions
    with 22 objects. RoboTacDex provides comprehensive records including multi-view RGB and depth information, tactile feedback,
    and detailed semantic annotations. Furthermore, the dataset features a variety of relatively challenging tasks that can
    only be completed by dual arms and dexterous hands, aiming to mimic human-like operational logic and simulate real-world
    manipulation complexity. To ensure data collection quality, we develop an improved multi-camera synchronization system
    to enable millisecond data synchronization and recording of modalities. In our experiments, we evaluate three representative
    imitation learning models on our dataset, analyzing their performance as well as their respective strengths and limitations
    across different task categories. Successful trial results and a moderate level of generalization capabilities across
    a suite of tasks indicate the effectiveness and diversity of the collected dataset. Our dataset will be open-sourced soon.'
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
- robotacdex
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31836v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (910 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'RoboTacDex: A Dexterous Visual-Tactile-Action Dataset for Humanoid Manipulation'
  url: https://arxiv.org/abs/2606.31836
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
RoboTacDex 数据集旨在解决机器人学习中大规模多样化演示轨迹的稀缺问题，专门针对人形机器人的灵巧操作行为设计。它基于公开可用的 Unitree G1 人形机器人平台，记录了 6000 条包含多视角 RGB 与深度图像、触觉反馈以及详细语义标注的轨迹数据。数据集涵盖了 19 个任务、23 种技能和 22 种物体交互，其中包含许多仅能通过双臂和灵巧手完成的挑战性任务，以模拟人类操作逻辑和真实世界的操作复杂性。为确保数据质量，团队开发了改进的多相机同步系统，实现了毫秒级的数据同步与模态记录。实验部分评估了三种代表性模仿学习模型，结果表明该数据集在任务成功率与泛化能力上均表现良好，验证了其有效性与多样性。

## 核心内容
### 数据集构建
- **平台与规模**：基于 Unitree G1 人形机器人，采集 6000 条演示轨迹，涵盖 19 个任务、23 种技能，与 22 种物体交互。
- **模态记录**：提供多视角 RGB 与深度图像、触觉反馈（tactile feedback）以及详细的语义标注（semantic annotations）。
- **任务特点**：包含仅能通过双臂与灵巧手完成的挑战性任务，旨在模仿人类操作逻辑并模拟真实世界的操作复杂性。

### 数据采集系统
- **同步技术**：开发了改进的多相机同步系统，实现毫秒级（millisecond）数据同步与多模态记录。
- **质量保障**：通过高精度同步确保各模态数据的时间对齐，为后续模型训练提供可靠基础。

### 实验设置与结果
- **模型评估**：在数据集上测试了三种代表性模仿学习模型（imitation learning models），分析其在不同任务类别中的性能、优势与局限。
- **关键指标**：成功试验结果（successful trial results）表明模型在任务执行上表现良好；跨任务套件的泛化能力（generalization capabilities）达到中等水平，验证了数据集的多样性与有效性。
- **开源计划**：数据集即将开源（open-sourced soon）。

## Overview
In the field of robot learning, large-scale and diverse demonstration trajectories provide the fundamental basis for enhancing robotic manipulation ability. We introduce RoboTacDex, a large, multi-modal, and diverse dataset of dexterous manipulation behaviors performed with a humanoid robot. Built on the publicly accessible humanoid robot Unitree G1, RoboTacDex consists of 6k trajectories covering 19 tasks, 23 skills, and interactions with 22 objects. RoboTacDex provides comprehensive records including multi-view RGB and depth information, tactile feedback, and detailed semantic annotations. Furthermore, the dataset features a variety of relatively challenging tasks that can only be completed by dual arms and dexterous hands, aiming to mimic human-like operational logic and simulate real-world manipulation complexity. To ensure data collection quality, we develop an improved multi-camera synchronization system to enable millisecond data synchronization and recording of modalities. In our experiments, we evaluate three representative imitation learning models on our dataset,   analyzing their performance as well as their respective strengths and limitations across different task categories. Successful trial results and a moderate level of generalization capabilities across a suite of tasks indicate the effectiveness and diversity of the collected dataset. Our dataset will be open-sourced soon.

## Overview
In the field of robot learning, large-scale and diverse demonstration trajectories provide the fundamental basis for enhancing robotic manipulation ability. We introduce RoboTacDex, a large, multi-modal, and diverse dataset of dexterous manipulation behaviors performed with a humanoid robot. Built on the publicly accessible humanoid robot Unitree G1, RoboTacDex consists of 6k trajectories covering 19 tasks, 23 skills, and interactions with 22 objects. RoboTacDex provides comprehensive records including multi-view RGB and depth information, tactile feedback, and detailed semantic annotations. Furthermore, the dataset features a variety of relatively challenging tasks that can only be completed by dual arms and dexterous hands, aiming to mimic human-like operational logic and simulate real-world manipulation complexity. To ensure data collection quality, we develop an improved multi-camera synchronization system to enable millisecond data synchronization and recording of modalities. In our experiments, we evaluate three representative imitation learning models on our dataset, analyzing their performance as well as their respective strengths and limitations across different task categories. Successful trial results and a moderate level of generalization capabilities across a suite of tasks indicate the effectiveness and diversity of the collected dataset. Our dataset will be open-sourced soon.

## Content
In the field of robot learning, large-scale and diverse demonstration trajectories provide the fundamental basis for enhancing robotic manipulation ability. We introduce RoboTacDex, a large, multi-modal, and diverse dataset of dexterous manipulation behaviors performed with a humanoid robot. Built on the publicly accessible humanoid robot Unitree G1, RoboTacDex consists of 6k trajectories covering 19 tasks, 23 skills, and interactions with 22 objects. RoboTacDex provides comprehensive records including multi-view RGB and depth information, tactile feedback, and detailed semantic annotations. Furthermore, the dataset features a variety of relatively challenging tasks that can only be completed by dual arms and dexterous hands, aiming to mimic human-like operational logic and simulate real-world manipulation complexity. To ensure data collection quality, we develop an improved multi-camera synchronization system to enable millisecond data synchronization and recording of modalities. In our experiments, we evaluate three representative imitation learning models on our dataset, analyzing their performance as well as their respective strengths and limitations across different task categories. Successful trial results and a moderate level of generalization capabilities across a suite of tasks indicate the effectiveness and diversity of the collected dataset. Our dataset will be open-sourced soon.

## 参考
- http://arxiv.org/abs/2606.31836v1

## 개요
RoboTacDex 데이터셋은 로봇 학습에서 대규모 다양화된 시연 궤적의 부족 문제를 해결하기 위해 설계되었으며, 특히 휴머노이드 로봇의 손재주 있는 조작 행동에 초점을 맞추고 있습니다. 공개적으로 사용 가능한 Unitree G1 휴머노이드 로봇 플랫폼을 기반으로, 다중 시점 RGB 및 깊이 이미지, 촉각 피드백, 상세한 의미론적 주석을 포함한 6000개의 궤적 데이터를 기록했습니다. 데이터셋은 19개의 작업, 23개의 기술, 22개의 객체 상호작용을 포함하며, 그중에는 양팔과 손재주 있는 손으로만 완료할 수 있는 도전적인 작업이 많이 포함되어 인간의 조작 논리와 실제 세계의 조작 복잡성을 모방합니다. 데이터 품질을 보장하기 위해 팀은 개선된 다중 카메라 동기화 시스템을 개발하여 밀리초 단위의 데이터 동기화와 모달리티 기록을 구현했습니다. 실험 부분에서는 세 가지 대표적인 모방 학습 모델을 평가했으며, 결과는 데이터셋이 작업 성공률과 일반화 능력 모두에서 우수한 성능을 보여 그 효과성과 다양성을 검증했습니다.

## 핵심 내용
### 데이터셋 구축
- **플랫폼 및 규모**: Unitree G1 휴머노이드 로봇을 기반으로 6000개의 시연 궤적을 수집하며, 19개의 작업, 23개의 기술, 22개의 객체 상호작용을 포함합니다.
- **모달리티 기록**: 다중 시점 RGB 및 깊이 이미지, 촉각 피드백(tactile feedback), 상세한 의미론적 주석(semantic annotations)을 제공합니다.
- **작업 특성**: 양팔과 손재주 있는 손으로만 완료할 수 있는 도전적인 작업을 포함하며, 인간의 조작 논리를 모방하고 실제 세계의 조작 복잡성을 시뮬레이션하는 것을 목표로 합니다.

### 데이터 수집 시스템
- **동기화 기술**: 개선된 다중 카메라 동기화 시스템을 개발하여 밀리초(millisecond) 단위의 데이터 동기화와 다중 모달리티 기록을 구현했습니다.
- **품질 보장**: 고정밀 동기화를 통해 각 모달리티 데이터의 시간 정렬을 보장하며, 후속 모델 훈련을 위한 신뢰할 수 있는 기반을 제공합니다.

### 실험 설정 및 결과
- **모델 평가**: 데이터셋에서 세 가지 대표적인 모방 학습 모델(imitation learning models)을 테스트하고, 다양한 작업 범주에서의 성능, 장점, 한계를 분석했습니다.
- **핵심 지표**: 성공적인 시험 결과(successful trial results)는 모델이 작업 실행에서 우수한 성능을 보임을 나타냅니다; 교차 작업 스위트에서의 일반화 능력(generalization capabilities)은 중간 수준에 도달하여 데이터셋의 다양성과 효과성을 검증했습니다.
- **오픈소스 계획**: 데이터셋은 곧 오픈소스로 공개될 예정입니다(open-sourced soon).
