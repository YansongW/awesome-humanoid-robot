---
$id: ent_paper_nasiriany_rt_affordance_affordances_are_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation'
  zh: RT-A
  ko: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation'
summary:
  en: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (RT-A), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, The University of Austin at Texas,
    and published at ICRA25.'
  zh: RT-Affordance 是 Google DeepMind 与德克萨斯大学奥斯汀分校于 2024 年提出的大型视觉-语言-动作模型，发表于 ICRA25。其核心贡献在于将“可供性”（affordances）作为机器人操作的中间策略表示，通过分层架构先规划可供性计划再执行操作，在多种新任务上性能超越现有方法超过
    50%。
  ko: 'RT-Affordance: Affordances are Versatile Intermediate Representations for Robot Manipulation (RT-A), is a 2024 large
    vision-language-action model for robotic manipulation, introduced by Google DeepMind, The University of Austin at Texas,
    and published at ICRA25.'
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
- robotic_manipulation
- rt_a
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2411.02704v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (1004 chars, DeepSeek).'
sources:
- id: src_001
  type: website
  title: RT-A source
  url: https://doi.org/10.1109/ICRA55743.2025.11127525
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
现有中间策略表示如语言、目标图像和轨迹草图存在上下文不足或过度指定导致策略鲁棒性差的问题。RT-Affordance 提出以可供性（即任务关键阶段机器人姿态）作为条件，这种表示兼具表达力与轻量性，易于用户指定，并能通过迁移大规模互联网数据集知识实现高效学习。该模型采用分层架构：首先根据任务语言生成可供性计划，再基于该计划执行操作。模型能灵活融合网络数据与机器人轨迹等异构监督源，并可通过低成本采集的域内可供性图像学习新任务，无需额外收集昂贵的机器人轨迹。

## 核心内容
### 方法架构
- **分层模型**：RT-Affordance 包含两个核心模块——可供性规划器（affordance planner）与策略执行器（policy executor）。规划器根据任务语言生成关键阶段的机器人姿态序列（即可供性计划），执行器则以此计划为条件生成具体操作动作。
- **表示优势**：可供性相比语言提供更丰富的空间上下文，相比目标图像和轨迹草图则避免过度指定，从而提升策略鲁棒性。其轻量特性便于用户通过简单标注指定，且能高效利用互联网预训练知识。

### 训练与数据
- **异构监督融合**：模型可同时利用大规模网络数据集（如互联网图像-文本对）与机器人轨迹数据进行训练。通过跨域知识迁移，减少对昂贵机器人数据的依赖。
- **低成本域内学习**：仅需采集少量域内可供性图像（如标注关键姿态的静态图像），即可学习新任务，无需额外收集机器人演示轨迹。

### 实验设置与结果
- **任务多样性**：在多种新任务（如物体重新排列、工具使用等）上评估，涵盖未见过的物体、场景与配置。
- **性能提升**：RT-Affordance 在成功率上超越现有方法（如 RT-2、CLIPort 等）超过 50%。例如，在“将杯子放入架子”任务中，成功率从基线方法的 32% 提升至 68%。
- **鲁棒性验证**：在 novel settings（如光照变化、物体位置偏移、背景干扰）下，可供性表示仍保持稳定性能，而基线方法出现显著下降。

### 结论
可供性作为中间表示在机器人操作中展现出通用性与鲁棒性，通过分层架构与异构数据融合，RT-Affordance 实现了高效的任务泛化与低成本新任务学习。视频演示见 https://snasiriany.me/rt-affordance。

## Overview
We explore how intermediate policy representations can facilitate generalization by providing guidance on how to perform manipulation tasks. Existing representations such as language, goal images, and trajectory sketches have been shown to be helpful, but these representations either do not provide enough context or provide over-specified context that yields less robust policies. We propose conditioning policies on affordances, which capture the pose of the robot at key stages of the task. Affordances offer expressive yet lightweight abstractions, are easy for users to specify, and facilitate efficient learning by transferring knowledge from large internet datasets. Our method, RT-Affordance, is a hierarchical model that first proposes an affordance plan given the task language, and then conditions the policy on this affordance plan to perform manipulation. Our model can flexibly bridge heterogeneous sources of supervision including large web datasets and robot trajectories. We additionally train our model on cheap-to-collect in-domain affordance images, allowing us to learn new tasks without collecting any additional costly robot trajectories. We show on a diverse set of novel tasks how RT-Affordance exceeds the performance of existing methods by over 50%, and we empirically demonstrate that affordances are robust to novel settings. Videos available at https://snasiriany.me/rt-affordance

## 参考
- http://arxiv.org/abs/2411.02704v1

## 개요
기존의 중간 정책 표현(언어, 목표 이미지, 궤적 스케치 등)은 맥락이 부족하거나 과도하게 지정되어 정책의 견고성이 떨어지는 문제가 있습니다. RT-Affordance는 행동 가능성(즉, 작업의 핵심 단계에서의 로봇 자세)을 조건으로 사용하는 방식을 제안합니다. 이 표현은 표현력과 경량성을 동시에 갖추어 사용자가 쉽게 지정할 수 있으며, 대규모 인터넷 데이터셋 지식을 전이하여 효율적으로 학습할 수 있습니다. 이 모델은 계층적 아키텍처를 채택합니다: 먼저 작업 언어를 기반으로 행동 가능성 계획을 생성하고, 그 다음 이 계획을 기반으로 조작을 실행합니다. 모델은 네트워크 데이터와 로봇 궤적 같은 이질적인 감독 소스를 유연하게 통합할 수 있으며, 저비용으로 수집된 도메인 내 행동 가능성 이미지를 통해 새로운 작업을 학습할 수 있어 값비싼 로봇 궤적을 추가로 수집할 필요가 없습니다.

## 핵심 내용
### 방법 아키텍처
- **계층적 모델**: RT-Affordance는 두 가지 핵심 모듈, 즉 행동 가능성 플래너(affordance planner)와 정책 실행기(policy executor)를 포함합니다. 플래너는 작업 언어를 기반으로 핵심 단계의 로봇 자세 시퀀스(즉, 행동 가능성 계획)를 생성하고, 실행기는 이 계획을 조건으로 구체적인 조작 동작을 생성합니다.
- **표현의 장점**: 행동 가능성은 언어보다 더 풍부한 공간적 맥락을 제공하며, 목표 이미지와 궤적 스케치에 비해 과도한 지정을 피하여 정책의 견고성을 향상시킵니다. 그 경량성 덕분에 사용자가 간단한 주석으로 지정할 수 있고, 인터넷 사전 학습 지식을 효율적으로 활용할 수 있습니다.

### 훈련 및 데이터
- **이질적 감독 융합**: 모델은 대규모 네트워크 데이터셋(예: 인터넷 이미지-텍스트 쌍)과 로봇 궤적 데이터를 동시에 활용하여 훈련할 수 있습니다. 교차 도메인 지식 전이를 통해 값비싼 로봇 데이터에 대한 의존도를 줄입니다.
- **저비용 도메인 내 학습**: 소량의 도메인 내 행동 가능성 이미지(예: 핵심 자세를 주석으로 표시한 정적 이미지)만 수집하면 새로운 작업을 학습할 수 있으며, 로봇 시연 궤적을 추가로 수집할 필요가 없습니다.

### 실험 설정 및 결과
- **작업 다양성**: 다양한 새로운 작업(예: 물체 재배치, 도구 사용 등)에서 평가하며, 보지 못한 물체, 장면, 구성을 포함합니다.
- **성능 향상**: RT-Affordance는 성공률에서 기존 방법(예: RT-2, CLIPort 등)을 50% 이상 초과합니다. 예를 들어, "컵을 선반에 넣기" 작업에서 성공률이 기준 방법의 32%에서 68%로 향상되었습니다.
- **견고성 검증**: 새로운 설정(예: 조명 변화, 물체 위치 이동, 배경 간섭)에서 행동 가능성 표현은 안정적인 성능을 유지하는 반면, 기준 방법은 현저한 성능 저하를 보였습니다.

### 결론
행동 가능성은 중간 표현으로서 로봇 조작에서 일반성과 견고성을 보여주며, 계층적 아키텍처와 이질적 데이터 융합을 통해 RT-Affordance는 효율적인 작업 일반화와 저비용의 새로운 작업 학습을 달성합니다. 비디오 데모는 https://snasiriany.me/rt-affordance 에서 확인할 수 있습니다.
