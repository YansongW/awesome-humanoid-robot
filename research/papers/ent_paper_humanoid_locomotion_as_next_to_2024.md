---
$id: ent_paper_humanoid_locomotion_as_next_to_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Humanoid Locomotion as Next Token Prediction
  zh: Humanoid Locomotion as Next Token Prediction
  ko: Humanoid Locomotion as Next Token Prediction
summary:
  en: Humanoid Locomotion as Next Token Prediction is a 2024 work on locomotion for humanoid robots.
  zh: Humanoid Locomotion as Next Token Prediction 是2024年提出的人形机器人运动控制方法，由研究团队将现实世界的人形机器人控制建模为类似语言模型的下一个词预测问题。核心贡献在于使用因果Transformer对传感器-运动轨迹进行自回归预测，通过模态对齐的预测方式处理多模态数据，并成功让全尺寸人形机器人在旧金山实现零样本行走。
  ko: Humanoid Locomotion as Next Token Prediction is a 2024 work on locomotion for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- humanoid_locomotion_as_next_to
- locomotion
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2402.19469v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (604 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Humanoid Locomotion as Next Token Prediction (arXiv)
  url: https://arxiv.org/abs/2402.19469
  date: '2024'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Humanoid Locomotion as Next Token Prediction project page
  url: https://humanoid-next-token-prediction.github.io/
  date: '2024'
  accessed_at: '2026-07-01'
---
## 概述
该方法将人形机器人控制转化为下一个token预测任务，采用因果Transformer架构对传感器-运动轨迹进行自回归预测。为适应多模态数据特性，模型采用模态对齐的预测方式，即每个输入token仅预测同一模态的下一个token。这种通用框架允许利用缺失模态的数据（如无动作标签的视频轨迹）。训练数据来自模拟环境中的神经网络策略、基于模型的控制器、动作捕捉数据以及YouTube人类行走视频。实验表明，仅用27小时行走数据训练的模型即可实现真实世界迁移，并能泛化到未见过的指令（如倒走）。

## 核心内容
### 方法架构
- 将人形机器人控制建模为下一个token预测问题，类似于语言模型预测下一个词
- 采用因果Transformer架构，对传感器-运动轨迹进行自回归预测
- 实现模态对齐的预测方式：每个输入token仅预测同一模态的下一个token
- 这种设计允许利用缺失模态的数据（如无动作标签的视频轨迹）

### 训练数据
- 模拟环境中的神经网络策略生成轨迹
- 基于模型的控制器产生的轨迹
- 动作捕捉数据
- YouTube人类行走视频

### 实验设置与结果
- 全尺寸人形机器人在旧金山实现零样本行走
- 仅用27小时行走数据训练即可实现真实世界迁移
- 能泛化到训练中未见的指令，如倒走
- 结果表明通过生成式建模传感器-运动轨迹，可以学习具有挑战性的真实世界控制任务

## Overview
We cast real-world humanoid control as a next token prediction problem, akin to predicting the next word in language. Our model is a causal transformer trained via autoregressive prediction of sensorimotor trajectories. To account for the multi-modal nature of the data, we perform prediction in a modality-aligned way, and for each input token predict the next token from the same modality. This general formulation enables us to leverage data with missing modalities, like video trajectories without actions. We train our model on a collection of simulated trajectories coming from prior neural network policies, model-based controllers, motion capture data, and YouTube videos of humans. We show that our model enables a full-sized humanoid to walk in San Francisco zero-shot. Our model can transfer to the real world even when trained on only 27 hours of walking data, and can generalize to commands not seen during training like walking backward. These findings suggest a promising path toward learning challenging real-world control tasks by generative modeling of sensorimotor trajectories.

## 参考
- http://arxiv.org/abs/2402.19469v1

## 개요
이 방법은 휴머노이드 로봇 제어를 다음 토큰 예측 작업으로 변환하며, 인과적 Transformer 아키텍처를 사용하여 센서-운동 궤적을 자기회귀적으로 예측합니다. 다중 모달 데이터 특성에 적응하기 위해 모델은 모달 정렬 예측 방식을 채택하며, 각 입력 토큰은 동일한 모달의 다음 토큰만 예측합니다. 이러한 일반적인 프레임워크는 누락된 모달의 데이터(예: 동작 레이블이 없는 비디오 궤적)를 활용할 수 있게 합니다. 훈련 데이터는 시뮬레이션 환경의 신경망 정책, 모델 기반 제어기, 모션 캡처 데이터 및 YouTube 인간 보행 비디오에서 비롯됩니다. 실험에 따르면 단 27시간의 보행 데이터로 훈련된 모델만으로도 실제 세계 전이가 가능하며, 훈련 중 보지 못한 명령(예: 뒤로 걷기)에도 일반화할 수 있습니다.

## 핵심 내용
### 방법 아키텍처
- 휴머노이드 로봇 제어를 다음 토큰 예측 문제로 모델링하며, 이는 언어 모델이 다음 단어를 예측하는 것과 유사합니다.
- 인과적 Transformer 아키텍처를 채택하여 센서-운동 궤적을 자기회귀적으로 예측합니다.
- 모달 정렬 예측 방식을 구현합니다: 각 입력 토큰은 동일한 모달의 다음 토큰만 예측합니다.
- 이러한 설계는 누락된 모달의 데이터(예: 동작 레이블이 없는 비디오 궤적)를 활용할 수 있게 합니다.

### 훈련 데이터
- 시뮬레이션 환경의 신경망 정책이 생성한 궤적
- 모델 기반 제어기가 생성한 궤적
- 모션 캡처 데이터
- YouTube 인간 보행 비디오

### 실험 설정 및 결과
- 전체 크기 휴머노이드 로봇이 샌프란시스코에서 제로샷 보행을 구현했습니다.
- 단 27시간의 보행 데이터로 훈련된 모델만으로도 실제 세계 전이가 가능합니다.
- 훈련 중 보지 못한 명령(예: 뒤로 걷기)에도 일반화할 수 있습니다.
- 결과는 센서-운동 궤적을 생성적으로 모델링함으로써 도전적인 실제 세계 제어 작업을 학습할 수 있음을 보여줍니다.
