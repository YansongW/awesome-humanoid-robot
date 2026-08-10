---
$id: ent_paper_mckay_learning_the_p2d_model_for_lit_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Learning the P2D Model for Lithium-Ion Batteries with SOH Detection
  zh: 具有SOH检测的锂离子电池P2D模型学习
  ko: SOH 감지를 위한 리튬 이온 배터리 P2D 모델 학습
summary:
  en: This paper proposes a Convolutional Neural Network surrogate trained on synthetic P2D battery simulations to replace
    the computationally expensive Pseudo Two Dimensional electrochemical model for 100-second-ahead state prediction, and
    introduces a single-parameter State of Health adjustment estimated by voltage-discrepancy grid search.
  zh: 本文提出用卷积神经网络（CNN）替代计算昂贵的P2D电化学模型，实现锂离子电池100秒前的状态预测，并通过电压差异网格搜索引入单参数健康状态（SOH）调整机制。
  ko: 본 논문은 합성 P2D 배터리 시뮬레이션 데이터로 학습된 컨볼루션 신경망 서로게이트 모델을 제안하여, 계산 비용이 높은 의사이차원 전기화학 모델을 대체하고 100초 선행 상태 예측을 수행하며, 전압 불일치 그리드
    서치를 통해 추정되는 단일 매개변수 SOH 조정을 도입한다.
domains:
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- battery_management_system
- state_of_health_estimation
- convolutional_neural_network
- surrogate_model
- electrochemical_model
- power_system
- lithium_ion_battery
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2502.14147v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (517 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Learning the P2D Model for Lithium-Ion Batteries with SOH Detection
  url: https://arxiv.org/abs/2502.14147
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究针对电池管理系统中电化学模型计算复杂的问题，利用合成P2D电池仿真数据训练CNN代理模型。实验证明CNN能精确捕捉锂离子浓度分布特征，在随机驾驶循环数据上实现高效预测。同时提出基于电压差异网格搜索的单参数SOH调整方法，使神经网络模型能适应电池老化状态的变化。

## 核心内容
### 方法架构
- 使用P2D电化学模型生成合成训练数据，覆盖随机驾驶循环场景
- 构建CNN代理模型替代原始P2D模型，实现100秒前状态预测
- 提出单参数SOH调整机制，通过电压差异网格搜索估计老化参数

### 实验设置
- 训练数据：基于P2D模型仿真的随机驾驶循环数据集
- 模型架构：CNN被证明是捕捉锂离子浓度分布的最优选择
- 评估指标：对比CNN代理模型与原始P2D模型的预测精度

### 关键发现
- CNN代理模型在保持预测精度的同时显著降低计算成本
- 单参数SOH调整方法能有效反映电池老化状态变化
- 该方法适用于电池管理系统中的实时预测需求

### 结论
该研究证明数据驱动的CNN模型可以替代复杂的电化学模型，为电池管理系统提供高效准确的预测工具，同时SOH调整机制增强了模型对电池老化的适应性。

## Overview
Lithium ion batteries are widely used in many applications. Battery management systems control their optimal use and charging and predict when the battery will cease to deliver the required output on a planned duty or driving cycle. Such systems use a simulation of a mathematical model of battery performance. These models can be electrochemical or data-driven. Electrochemical models for batteries running at high currents are mathematically and computationally complex. In this work, we show that a well-regarded electrochemical model, the Pseudo Two Dimensional (P2D) model, can be replaced by a computationally efficient Convolutional Neural Network (CNN) surrogate model fit to accurately simulated data from a class of random driving cycles. We demonstrate that a CNN is an ideal choice for accurately capturing Lithium ion concentration profiles. Additionally, we show how the neural network model can be adjusted to correspond to battery changes in State of Health (SOH).

## 参考
- http://arxiv.org/abs/2502.14147v1

## 개요
본 연구는 배터리 관리 시스템에서 전기화학 모델의 계산 복잡성 문제를 해결하기 위해, 합성 P2D 배터리 시뮬레이션 데이터를 활용하여 CNN 대리 모델을 훈련시켰습니다. 실험을 통해 CNN이 리튬 이온 농도 분포 특성을 정밀하게 포착할 수 있으며, 무작위 주행 사이클 데이터에서 효율적인 예측을 구현함을 입증했습니다. 또한 전압 차이 그리드 탐색 기반의 단일 파라미터 SOH 조정 방법을 제안하여, 신경망 모델이 배터리 노화 상태 변화에 적응할 수 있도록 했습니다.

## 핵심 내용
### 방법 아키텍처
- P2D 전기화학 모델을 사용하여 무작위 주행 사이클 시나리오를 포괄하는 합성 훈련 데이터 생성
- 원래 P2D 모델을 대체하는 CNN 대리 모델 구축, 100초 전 상태 예측 구현
- 전압 차이 그리드 탐색을 통해 노화 파라미터를 추정하는 단일 파라미터 SOH 조정 메커니즘 제안

### 실험 설정
- 훈련 데이터: P2D 모델 시뮬레이션 기반 무작위 주행 사이클 데이터셋
- 모델 아키텍처: CNN이 리튬 이온 농도 분포를 포착하는 최적의 선택임이 입증됨
- 평가 지표: CNN 대리 모델과 원래 P2D 모델의 예측 정확도 비교

### 주요 발견
- CNN 대리 모델은 예측 정확도를 유지하면서 계산 비용을 크게 절감
- 단일 파라미터 SOH 조정 방법이 배터리 노화 상태 변화를 효과적으로 반영
- 이 방법은 배터리 관리 시스템의 실시간 예측 요구에 적합

### 결론
본 연구는 데이터 기반 CNN 모델이 복잡한 전기화학 모델을 대체할 수 있음을 입증하여, 배터리 관리 시스템에 효율적이고 정확한 예측 도구를 제공하며, SOH 조정 메커니즘은 모델의 배터리 노화 적응성을 강화합니다.
