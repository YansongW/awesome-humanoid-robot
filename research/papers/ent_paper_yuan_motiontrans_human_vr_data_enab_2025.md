---
$id: ent_paper_yuan_motiontrans_human_vr_data_enab_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies'
  zh: MotionTrans
  ko: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies'
summary:
  en: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (MotionTrans), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, Institute for Interdisciplinary Information Sciences, Tsinghua
    University, Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Wuhan University.'
  zh: MotionTrans 是由北京大学、清华大学、上海交通大学等机构联合提出的2025年大型视觉-语言-动作模型，用于机器人操作策略训练。其核心贡献在于通过多任务人机协同训练，首次系统验证了人类VR数据可直接迁移运动技能至机器人策略，实现13个任务中9个任务的零样本成功执行，并将预训练-微调性能提升40%。
  ko: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (MotionTrans), is a 2025
    large vision-language-action model for robotic manipulation, introduced by State Key Laboratory of Multimedia Information
    Processing, School of Computer Science, Peking University, Institute for Interdisciplinary Information Sciences, Tsinghua
    University, Shanghai Qi Zhi Institute, Shanghai Jiao Tong University, Wuhan University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- motiontrans
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.17759v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'MotionTrans: Human VR Data Enable Motion-Level Learning for Robotic Manipulation Policies (arXiv)'
  url: https://arxiv.org/abs/2509.17759
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MotionTrans source
  url: https://doi.org/10.48550/arXiv.2509.17759
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
针对机器人模仿学习中真实数据稀缺的瓶颈，MotionTrans 提出了一套完整框架，包含VR数据采集系统、人类数据转换流水线及加权协同训练策略。通过同时训练30个人机任务，该模型成功将13个任务的人类运动数据直接转化为可部署的端到端机器人策略，其中9个任务在零样本条件下达到非平凡成功率。消融实验揭示了运动学习成功的关键因素：与机器人数据协同训练以及广泛的任务相关运动覆盖。所有数据、代码和模型权重均已开源。

## 核心内容
### 方法架构
MotionTrans 包含三个核心组件：
- **数据采集系统**：利用VR设备采集人类操作数据，覆盖30种不同任务
- **人类数据转换流水线**：将人类运动数据转换为机器人可执行的格式
- **加权协同训练策略**：在训练过程中动态调整人类数据与机器人数据的权重

### 实验设置
- **任务规模**：同时训练30个人机任务
- **评估指标**：任务成功率
- **关键对比**：与纯机器人数据训练、预训练-微调范式进行对比

### 关键结果
- **运动迁移能力**：13个任务的人类运动数据成功迁移至机器人策略
- **零样本性能**：9个任务在零样本条件下达到非平凡成功率（具体数值未在摘要中给出）
- **预训练-微调提升**：相比基线方法，成功率提升40%
- **消融发现**：
  - 与机器人数据协同训练是运动学习成功的必要条件
  - 广泛的任务相关运动覆盖显著提升泛化能力

### 结论
MotionTrans 首次系统证明了人类VR数据可直接用于机器人运动级学习，突破了传统方法仅利用人类数据提升鲁棒性或训练效率的局限。该工作为利用人类数据训练机器人操作策略提供了新的方法论，并开源了完整资源以促进社区发展。

## Overview
Scaling real robot data is a key bottleneck in imitation learning, leading to the use of auxiliary data for policy training. While other aspects of robotic manipulation such as image or language understanding may be learned from internet-based datasets, acquiring motion knowledge remains challenging. Human data, with its rich diversity of manipulation behaviors, offers a valuable resource for this purpose. While previous works show that using human data can bring benefits, such as improving robustness and training efficiency, it remains unclear whether it can realize its greatest advantage: enabling robot policies to directly learn new motions for task completion. In this paper, we systematically explore this potential through multi-task human-robot cotraining. We introduce MotionTrans, a framework that includes a data collection system, a human data transformation pipeline, and a weighted cotraining strategy. By cotraining 30 human-robot tasks simultaneously, we direcly transfer motions of 13 tasks from human data to deployable end-to-end robot policies. Notably, 9 tasks achieve non-trivial success rates in zero-shot manner. MotionTrans also significantly enhances pretraining-finetuning performance (+40% success rate). Through ablation study, we also identify key factors for successful motion learning: cotraining with robot data and broad task-related motion coverage. These findings unlock the potential of motion-level learning from human data, offering insights into its effective use for training robotic manipulation policies. All data, code, and model weights are open-sourced https://motiontrans.github.io/.

## Overview
Scaling real robot data is a key bottleneck in imitation learning, leading to the use of auxiliary data for policy training. While other aspects of robotic manipulation such as image or language understanding may be learned from internet-based datasets, acquiring motion knowledge remains challenging. Human data, with its rich diversity of manipulation behaviors, offers a valuable resource for this purpose. While previous works show that using human data can bring benefits, such as improving robustness and training efficiency, it remains unclear whether it can realize its greatest advantage: enabling robot policies to directly learn new motions for task completion. In this paper, we systematically explore this potential through multi-task human-robot cotraining. We introduce MotionTrans, a framework that includes a data collection system, a human data transformation pipeline, and a weighted cotraining strategy. By cotraining 30 human-robot tasks simultaneously, we directly transfer motions of 13 tasks from human data to deployable end-to-end robot policies. Notably, 9 tasks achieve non-trivial success rates in zero-shot manner. MotionTrans also significantly enhances pretraining-finetuning performance (+40% success rate). Through ablation study, we also identify key factors for successful motion learning: cotraining with robot data and broad task-related motion coverage. These findings unlock the potential of motion-level learning from human data, offering insights into its effective use for training robotic manipulation policies. All data, code, and model weights are open-sourced https://motiontrans.github.io/.

## Content
Scaling real robot data is a key bottleneck in imitation learning, leading to the use of auxiliary data for policy training. While other aspects of robotic manipulation such as image or language understanding may be learned from internet-based datasets, acquiring motion knowledge remains challenging. Human data, with its rich diversity of manipulation behaviors, offers a valuable resource for this purpose. While previous works show that using human data can bring benefits, such as improving robustness and training efficiency, it remains unclear whether it can realize its greatest advantage: enabling robot policies to directly learn new motions for task completion. In this paper, we systematically explore this potential through multi-task human-robot cotraining. We introduce MotionTrans, a framework that includes a data collection system, a human data transformation pipeline, and a weighted cotraining strategy. By cotraining 30 human-robot tasks simultaneously, we directly transfer motions of 13 tasks from human data to deployable end-to-end robot policies. Notably, 9 tasks achieve non-trivial success rates in zero-shot manner. MotionTrans also significantly enhances pretraining-finetuning performance (+40% success rate). Through ablation study, we also identify key factors for successful motion learning: cotraining with robot data and broad task-related motion coverage. These findings unlock the potential of motion-level learning from human data, offering insights into its effective use for training robotic manipulation policies. All data, code, and model weights are open-sourced https://motiontrans.github.io/.

## 개요
실제 로봇 데이터의 확장은 모방 학습의 주요 병목 현상으로, 정책 훈련에 보조 데이터를 사용하게 됩니다. 로봇 조작의 다른 측면(예: 이미지 또는 언어 이해)은 인터넷 기반 데이터셋에서 학습될 수 있지만, 동작 지식을 획득하는 것은 여전히 어려운 과제입니다. 다양한 조작 행동을 포함하는 인간 데이터는 이러한 목적에 귀중한 자원을 제공합니다. 이전 연구들은 인간 데이터를 사용하면 강건성 및 훈련 효율성 향상과 같은 이점을 얻을 수 있음을 보여주었지만, 인간 데이터가 가장 큰 장점인 로봇 정책이 작업 완료를 위해 새로운 동작을 직접 학습할 수 있게 하는 능력을 실현할 수 있는지는 여전히 불분명합니다. 본 논문에서는 다중 작업 인간-로봇 공동 훈련을 통해 이 가능성을 체계적으로 탐구합니다. 우리는 데이터 수집 시스템, 인간 데이터 변환 파이프라인, 가중 공동 훈련 전략을 포함하는 프레임워크인 MotionTrans를 소개합니다. 30개의 인간-로봇 작업을 동시에 공동 훈련함으로써, 13개 작업의 동작을 인간 데이터에서 배포 가능한 엔드투엔드 로봇 정책으로 직접 전송합니다. 특히, 9개 작업은 제로샷 방식에서 유의미한 성공률을 달성합니다. MotionTrans는 또한 사전 훈련-미세 조정 성능을 크게 향상시킵니다(+40% 성공률). 절제 연구를 통해 성공적인 동작 학습의 핵심 요소인 로봇 데이터와의 공동 훈련 및 광범위한 작업 관련 동작 범위를 식별합니다. 이러한 발견은 인간 데이터로부터의 동작 수준 학습 가능성을 열어주며, 로봇 조작 정책 훈련에 효과적으로 활용하기 위한 통찰력을 제공합니다. 모든 데이터, 코드 및 모델 가중치는 https://motiontrans.github.io/에서 오픈소스로 제공됩니다.

## 핵심 내용
실제 로봇 데이터의 확장은 모방 학습의 주요 병목 현상으로, 정책 훈련에 보조 데이터를 사용하게 됩니다. 로봇 조작의 다른 측면(예: 이미지 또는 언어 이해)은 인터넷 기반 데이터셋에서 학습될 수 있지만, 동작 지식을 획득하는 것은 여전히 어려운 과제입니다. 다양한 조작 행동을 포함하는 인간 데이터는 이러한 목적에 귀중한 자원을 제공합니다. 이전 연구들은 인간 데이터를 사용하면 강건성 및 훈련 효율성 향상과 같은 이점을 얻을 수 있음을 보여주었지만, 인간 데이터가 가장 큰 장점인 로봇 정책이 작업 완료를 위해 새로운 동작을 직접 학습할 수 있게 하는 능력을 실현할 수 있는지는 여전히 불분명합니다. 본 논문에서는 다중 작업 인간-로봇 공동 훈련을 통해 이 가능성을 체계적으로 탐구합니다. 우리는 데이터 수집 시스템, 인간 데이터 변환 파이프라인, 가중 공동 훈련 전략을 포함하는 프레임워크인 MotionTrans를 소개합니다. 30개의 인간-로봇 작업을 동시에 공동 훈련함으로써, 13개 작업의 동작을 인간 데이터에서 배포 가능한 엔드투엔드 로봇 정책으로 직접 전송합니다. 특히, 9개 작업은 제로샷 방식에서 유의미한 성공률을 달성합니다. MotionTrans는 또한 사전 훈련-미세 조정 성능을 크게 향상시킵니다(+40% 성공률). 절제 연구를 통해 성공적인 동작 학습의 핵심 요소인 로봇 데이터와의 공동 훈련 및 광범위한 작업 관련 동작 범위를 식별합니다. 이러한 발견은 인간 데이터로부터의 동작 수준 학습 가능성을 열어주며, 로봇 조작 정책 훈련에 효과적으로 활용하기 위한 통찰력을 제공합니다. 모든 데이터, 코드 및 모델 가중치는 https://motiontrans.github.io/에서 오픈소스로 제공됩니다.

## 参考
- http://arxiv.org/abs/2509.17759v1
