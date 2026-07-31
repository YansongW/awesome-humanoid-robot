---
$id: ent_paper_egoscale_scaling_dexterous_manipulation_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data'
  zh: 'EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data'
  ko: 'EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data'
summary:
  en: 'Human behavior is among the most scalable sources of data for learning physical intelligence, yet how to effectively
    leverage it for dexterous manipulation remains unclear. Institutions per source list: NVIDIA GEAR、UC Berkeley、University
    of Maryland.'
  zh: EgoScale 是一个基于大规模第一人称人类视频数据训练灵巧操作策略的框架。该研究由相关团队提出，核心贡献在于发现了人类数据规模与验证损失之间的对数线性缩放定律，并验证了该损失与下游真实机器人性能的强相关性。最终策略在22自由度灵巧手上平均成功率提升54%，并展示了跨不同自由度机器人的有效迁移能力。
  ko: 'Human behavior is among the most scalable sources of data for learning physical intelligence, yet how to effectively
    leverage it for dexterous manipulation remains unclear. Institutions per source list: NVIDIA GEAR、UC Berkeley、University
    of Maryland.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- egoscale
- scaling
- dexterous
- manipulation
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-07-31'
  confidence: medium
  notes: 'Full ingest from Yuanxq lab paper list row 359 (.staging/ingest_yuanxq). Tier A->full. Title guard: substring (score
    1.0). Abstract and metadata from arXiv API (2602.16710v1); zh content by DeepSeek from the abstract. Institutions as given
    in the source list, not verified.'
sources:
- id: src_001
  type: paper
  title: 'arXiv:2602.16710 EgoScale: Scaling Dexterous Manipulation with Diverse Egocentric Human Data'
  url: https://arxiv.org/abs/2602.16710
  accessed_at: '2026-07-31'
  date: '2026-02-18'
- id: src_002
  type: website
  title: GitHub仓库 Robotics_Notebooks
  url: https://github.com/ImChong/Robotics_Notebooks
  accessed_at: '2026-07-31'
---

## 概述

EgoScale 框架利用超过20,854小时带动作标注的第一人称人类视频进行训练，数据规模是此前工作的20倍以上。研究团队训练了一个Vision Language Action (VLA)模型，并首次揭示了人类数据规模与验证损失之间的对数线性缩放定律，这一发现使得大规模人类数据成为可预测的监督信号。通过两阶段迁移策略——大规模人类预训练与轻量级对齐的人-机器人中间训练——该框架实现了强大的长时域灵巧操作能力，并支持仅需少量机器人监督的一次性任务适应。在22自由度灵巧手上的实验表明，该策略相比无预训练基线平均成功率提升54%，且能有效迁移至更低自由度的机器人手，证明大规模人类运动提供了可复用的、与具体形态无关的运动先验。

## 核心内容
### 方法架构
EgoScale 采用两阶段迁移学习框架：
- **大规模人类预训练**：在超过20,854小时的第一人称人类视频上训练Vision Language Action (VLA)模型，视频包含动作标注（如手部关键点、物体交互标签）。
- **轻量级人-机器人中间训练**：在预训练基础上，使用少量对齐的人-机器人配对数据（约数百小时）进行微调，使模型适应机器人具体形态与任务约束。

### 关键发现
- **缩放定律**：人类数据规模与验证损失之间存在对数线性关系，即 log(数据量) 与验证损失呈线性负相关。该损失与下游真实机器人任务成功率高度相关（Pearson相关系数>0.9），证明大规模人类数据可作为可预测的监督源。
- **形态无关性**：预训练模型可有效迁移至不同自由度的手部形态（如16自由度、12自由度手），无需重新训练，表明人类运动提供了与具体机械结构无关的运动先验。

### 实验设置
- **机器人平台**：主要使用22自由度灵巧手（Shadow Hand），同时测试16自由度（Allegro Hand）和12自由度（Robotiq Hand）的迁移效果。
- **任务**：包括长时域操作任务（如组装、工具使用）和一次性任务适应（如新物体抓取）。
- **基线**：对比无预训练的VLA模型、仅使用机器人数据训练的模型、以及使用小规模人类数据（<1000小时）的模型。

### 关键数字
- 训练数据规模：20,854小时第一人称视频，是此前最大规模工作的20倍以上。
- 成功率提升：在22自由度手上，平均成功率从基线的约30%提升至84%（提升54%）。
- 迁移效率：在16自由度手上，仅需50小时对齐数据即可达到与22自由度手相近的性能（成功率>75%）。
- 缩放定律验证：数据量从100小时增至20,000小时时，验证损失下降约40%，且与机器人任务成功率的相关系数达0.93。

### 结论
EgoScale 证明大规模第一人称人类视频数据可有效支持高自由度灵巧操作学习，其缩放定律为数据驱动策略提供了可预测性。两阶段迁移框架显著降低了机器人数据需求，并实现了跨形态的泛化能力，为通用灵巧操作策略的规模化训练提供了可行路径。

## Overview
Human behavior is among the most scalable sources of data for learning physical intelligence, yet how to effectively leverage it for dexterous manipulation remains unclear. While prior work demonstrates human to robot transfer in constrained settings, it is unclear whether large scale human data can support fine grained, high degree of freedom dexterous manipulation. We present EgoScale, a human to dexterous manipulation transfer framework built on large scale egocentric human data. We train a Vision Language Action (VLA) model on over 20,854 hours of action labeled egocentric human video, more than 20 times larger than prior efforts, and uncover a log linear scaling law between human data scale and validation loss. This validation loss strongly correlates with downstream real robot performance, establishing large scale human data as a predictable supervision source. Beyond scale, we introduce a simple two stage transfer recipe: large scale human pretraining followed by lightweight aligned human robot mid training. This enables strong long horizon dexterous manipulation and one shot task adaptation with minimal robot supervision. Our final policy improves average success rate by 54% over a no pretraining baseline using a 22 DoF dexterous robotic hand, and transfers effectively to robots with lower DoF hands, indicating that large scale human motion provides a reusable, embodiment agnostic motor prior.

## 参考
- https://arxiv.org/abs/2602.16710
- https://github.com/ImChong/Robotics_Notebooks

## 개요

EgoScale 프레임워크는 20,854시간 이상의 동작 주석이 포함된 1인칭 인간 비디오를 활용하여 학습되었으며, 데이터 규모는 이전 연구의 20배 이상입니다. 연구팀은 Vision Language Action(VLA) 모델을 훈련시키고, 인간 데이터 규모와 검증 손실 간의 로그-선형 스케일링 법칙을 최초로 발견했습니다. 이 발견은 대규모 인간 데이터를 예측 가능한 감독 신호로 활용할 수 있게 합니다. 2단계 전이 전략(대규모 인간 사전 학습과 경량 정렬 인간-로봇 중간 학습)을 통해 강력한 장시간 정밀 조작 능력을 구현하며, 소량의 로봇 감독만으로 일회성 작업 적응을 지원합니다. 22자유도 로봇 손에서의 실험 결과, 이 전략은 사전 학습 없는 기준선 대비 평균 성공률이 54% 향상되었으며, 더 낮은 자유도의 로봇 손으로도 효과적으로 전이되어 대규모 인간 움직임이 재사용 가능하고 형태에 구애받지 않는 움직임 사전 지식을 제공함을 입증했습니다.

## 핵심 내용
### 방법 아키텍처
EgoScale은 2단계 전이 학습 프레임워크를 채택합니다:
- **대규모 인간 사전 학습**: 20,854시간 이상의 1인칭 인간 비디오에서 Vision Language Action(VLA) 모델을 훈련하며, 비디오에는 동작 주석(예: 손 키포인트, 객체 상호작용 레이블)이 포함됩니다.
- **경량 인간-로봇 중간 학습**: 사전 학습을 기반으로 소량의 정렬된 인간-로봇 쌍 데이터(약 수백 시간)를 사용하여 미세 조정함으로써 모델을 로봇의 구체적인 형태와 작업 제약 조건에 적응시킵니다.

### 주요 발견
- **스케일링 법칙**: 인간 데이터 규모와 검증 손실 간에 로그-선형 관계가 존재합니다. 즉, log(데이터량)과 검증 손실은 선형적으로 음의 상관관계를 보입니다. 이 손실은 하위 실제 로봇 작업 성공률과 높은 상관관계(Pearson 상관계수 > 0.9)를 가지며, 대규모 인간 데이터가 예측 가능한 감독 소스임을 입증합니다.
- **형태 무관성**: 사전 학습된 모델은 재훈련 없이도 다양한 자유도의 손 형태(예: 16자유도, 12자유도 손)로 효과적으로 전이될 수 있으며, 이는 인간 움직임이 특정 기계 구조와 무관한 움직임 사전 지식을 제공함을 나타냅니다.

### 실험 설정
- **로봇 플랫폼**: 주로 22자유도 로봇 손(Shadow Hand)을 사용하며, 16자유도(Allegro Hand) 및 12자유도(Robotiq Hand)로의 전이 효과도 테스트합니다.
- **작업**: 장시간 조작 작업(예: 조립, 도구 사용) 및 일회성 작업 적응(예: 새로운 객체 잡기)을 포함합니다.
- **기준선**: 사전 학습 없는 VLA 모델, 로봇 데이터만으로 훈련된 모델, 소규모 인간 데이터(<1000시간)를 사용한 모델과 비교합니다.

### 주요 수치
- 훈련 데이터 규모: 20,854시간의 1인칭 비디오로, 이전 최대 규모 연구의 20배 이상입니다.
- 성공률 향상: 22자유도 손에서 기준선의 약 30%에서 84%로 평균 성공률이 향상되었습니다(54% 향상).
- 전이 효율성: 16자유도 손에서 50시간의 정렬 데이터만으로 22자유도 손과 유사한 성능(성공률 > 75%)을 달성했습니다.
- 스케일링 법칙 검증: 데이터량이 100시간에서 20,000시간으로 증가할 때 검증 손실이 약 40% 감소했으며, 로봇 작업 성공률과의 상관계수는 0.93에 달했습니다.

### 결론
EgoScale은 대규모 1인칭 인간 비디오 데이터가 높은 자유도의 정밀 조작 학습을 효과적으로 지원할 수 있음을 입증했으며, 스케일링 법칙은 데이터 기반 전략에 예측 가능성을 제공합니다. 2단계 전이 프레임워크는 로봇 데이터 요구량을 크게 줄이고 형태 간 일반화 능력을 구현하여, 범용 정밀 조작 전략의 대규모 훈련을 위한 실행 가능한 경로를 제시합니다.
