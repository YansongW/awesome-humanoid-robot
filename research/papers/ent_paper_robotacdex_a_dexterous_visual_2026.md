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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31836v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
로봇 학습 분야에서 대규모의 다양한 시연 궤적은 로봇 조작 능력을 향상시키는 기본 토대를 제공합니다. 본 논문에서는 휴머노이드 로봇으로 수행된 정교한 조작 행동에 대한 대규모의 다중 모달 및 다양한 데이터셋인 RoboTacDex를 소개합니다. 공개적으로 접근 가능한 휴머노이드 로봇 Unitree G1을 기반으로 구축된 RoboTacDex는 19개 작업, 23개 기술, 22개 객체와의 상호작용을 포괄하는 6,000개의 궤적으로 구성됩니다. RoboTacDex는 다중 시점 RGB 및 깊이 정보, 촉각 피드백, 상세한 의미론적 주석을 포함한 포괄적인 기록을 제공합니다. 또한, 데이터셋은 인간과 유사한 조작 논리를 모방하고 실제 세계의 조작 복잡성을 시뮬레이션하기 위해 양팔과 정교한 손으로만 완료할 수 있는 다양한 상대적으로 어려운 작업을 특징으로 합니다. 데이터 수집 품질을 보장하기 위해 밀리초 단위의 데이터 동기화 및 모달리티 기록을 가능하게 하는 개선된 다중 카메라 동기화 시스템을 개발했습니다. 실험에서는 데이터셋에서 세 가지 대표적인 모방 학습 모델을 평가하여 다양한 작업 범주에서의 성능과 각각의 강점 및 한계를 분석했습니다. 일련의 작업에 걸친 성공적인 시험 결과와 적절한 수준의 일반화 능력은 수집된 데이터셋의 효과성과 다양성을 나타냅니다. 본 데이터셋은 곧 오픈소스로 공개될 예정입니다.

## 핵심 내용
로봇 학습 분야에서 대규모의 다양한 시연 궤적은 로봇 조작 능력을 향상시키는 기본 토대를 제공합니다. 본 논문에서는 휴머노이드 로봇으로 수행된 정교한 조작 행동에 대한 대규모의 다중 모달 및 다양한 데이터셋인 RoboTacDex를 소개합니다. 공개적으로 접근 가능한 휴머노이드 로봇 Unitree G1을 기반으로 구축된 RoboTacDex는 19개 작업, 23개 기술, 22개 객체와의 상호작용을 포괄하는 6,000개의 궤적으로 구성됩니다. RoboTacDex는 다중 시점 RGB 및 깊이 정보, 촉각 피드백, 상세한 의미론적 주석을 포함한 포괄적인 기록을 제공합니다. 또한, 데이터셋은 인간과 유사한 조작 논리를 모방하고 실제 세계의 조작 복잡성을 시뮬레이션하기 위해 양팔과 정교한 손으로만 완료할 수 있는 다양한 상대적으로 어려운 작업을 특징으로 합니다. 데이터 수집 품질을 보장하기 위해 밀리초 단위의 데이터 동기화 및 모달리티 기록을 가능하게 하는 개선된 다중 카메라 동기화 시스템을 개발했습니다. 실험에서는 데이터셋에서 세 가지 대표적인 모방 학습 모델을 평가하여 다양한 작업 범주에서의 성능과 각각의 강점 및 한계를 분석했습니다. 일련의 작업에 걸친 성공적인 시험 결과와 적절한 수준의 일반화 능력은 수집된 데이터셋의 효과성과 다양성을 나타냅니다. 본 데이터셋은 곧 오픈소스로 공개될 예정입니다.

## 参考
- http://arxiv.org/abs/2606.31836v1
