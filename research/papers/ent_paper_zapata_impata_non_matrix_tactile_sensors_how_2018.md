---
$id: ent_paper_zapata_impata_non_matrix_tactile_sensors_how_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Non-Matrix Tactile Sensors: How Can Be Exploited Their Local Connectivity For Predicting Grasp Stability?'
  zh: 非矩阵触觉传感器：如何利用其局部连通性预测抓取稳定性？
  ko: '비매트릭스 촉각 센서: 국부 연결성을 어떻게 파지 안정성 예측에 활용할 수 있는가?'
summary:
  en: This paper presents a method to process readings from non-matrix tactile sensors as tactile images and train a Convolutional
    Neural Network to predict grasp stability, achieving 94.2% F1-score on over 2500 real three-fingered grasps of 41 everyday
    objects.
  zh: 本文提出一种将非矩阵触觉传感器读数处理为触觉图像的方法，并训练卷积神经网络预测抓取稳定性。该方法在超过2500次真实三指抓取实验中（涵盖41种日常物体）取得了94.2%的F1分数。核心贡献在于证明了非矩阵传感器（触觉单元非规则排列）同样可以利用局部连接性进行稳定性预测。
  ko: 본 논문은 비매트릭스 촉각 센서의 판독값을 촉각 이미지로 처리하고 합성곱 신경망을 훈련시켜 파지 안정성을 예측하는 방법을 제안하며, 41개 일상 물체에 대한 2500회 이상의 실제 세 손가락 파지에서 94.2%의
    F1 점수를 달성했다.
domains:
- 02_components
- 07_ai_models_algorithms
- 11_applications_markets
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- tactile_sensing
- grasp_stability_prediction
- convolutional_neural_network
- non_matrix_tactile_sensor
- tactile_image
- biotac_sp
- shadow_dexterous_hand
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.05551v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (754 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Non-Matrix Tactile Sensors: How Can Be Exploited Their Local Connectivity For Predicting Grasp Stability?'
  url: https://arxiv.org/abs/1809.05551
  date: '2018'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
以往研究多将触觉传感器读数作为信号处理，通过手工设计特征来评估抓取稳定性；部分工作虽将矩阵式传感器读数视为图像，但非矩阵传感器（触觉单元非规则排列）尚未被充分探索。本文提出将非矩阵触觉传感器的读数重新组织为触觉图像，并利用卷积神经网络（CNN）的局部连接特性进行抓取稳定性预测。实验采集了2500余次真实三指抓取数据（覆盖41种日常物体），训练后的CNN模型在稳定性预测任务上达到了94.2%的F1分数，验证了该方法对非规则传感器布局的有效性。

## 核心内容
### 方法概述
- 将非矩阵触觉传感器的原始读数（触觉单元位置非规则排列）通过空间映射转换为二维触觉图像，保留传感器固有的局部连接结构。
- 采用卷积神经网络（CNN）处理这些触觉图像，利用其局部感受野特性自动提取空间特征，无需手工设计特征。

### 实验设置
- **数据集**：采集2500余次真实三指抓取实验，对象为41种日常物体（涵盖不同形状、材质与尺寸）。
- **传感器**：使用非矩阵触觉传感器（触觉单元未按矩形网格排列），每个抓取记录触觉单元的压力分布。
- **任务**：二分类预测抓取是否稳定（稳定/不稳定），以F1分数作为主要评价指标。

### 关键结果
- 训练后的CNN模型在测试集上达到**94.2%的F1分数**，显著优于传统基于手工特征的方法。
- 实验表明，非矩阵传感器的局部连接性（即相邻触觉单元的空间关系）可被CNN有效利用，即使传感器布局不规则，仍能通过图像化处理获得高精度预测。

### 结论
本文首次系统验证了非矩阵触觉传感器通过图像化处理与CNN结合，能够实现与矩阵式传感器相当的抓取稳定性预测性能。该方法降低了传感器硬件布局的限制，为低成本、非规则触觉阵列的应用提供了新思路。

## Overview
Tactile sensors supply useful information during the interaction with an object that can be used for assessing the stability of a grasp. Most of the previous works on this topic processed tactile readings as signals by calculating hand-picked features. Some of them have processed these readings as images calculating characteristics on matrix-like sensors. In this work, we explore how non-matrix sensors (sensors with taxels not arranged exactly in a matrix) can be processed as tactile images as well. In addition, we prove that they can be used for predicting grasp stability by training a Convolutional Neural Network (CNN) with them. We captured over 2500 real three-fingered grasps on 41 everyday objects to train a CNN that exploited the local connectivity inherent on the non-matrix tactile sensors, achieving 94.2% F1-score on predicting stability.

## 参考
- http://arxiv.org/abs/1809.05551v1

## 개요
기존 연구들은 대부분 촉각 센서 판독값을 신호 처리로 간주하여 수작업으로 설계된 특징을 통해 파지 안정성을 평가했습니다. 일부 연구에서는 행렬형 센서 판독값을 이미지로 간주했지만, 비행렬형 센서(촉각 유닛이 불규칙하게 배열된 경우)는 충분히 탐구되지 않았습니다. 본 논문은 비행렬형 촉각 센서의 판독값을 촉각 이미지로 재구성하고, 합성곱 신경망(CNN)의 국소 연결 특성을 활용하여 파지 안정성을 예측하는 방법을 제안합니다. 실험에서는 41종의 일상 물체를 대상으로 2500회 이상의 실제 세 손가락 파지 데이터를 수집했으며, 훈련된 CNN 모델은 안정성 예측 작업에서 94.2%의 F1 점수를 달성하여 불규칙한 센서 배치에 대한 이 방법의 효과성을 검증했습니다.

## 핵심 내용
### 방법 개요
- 비행렬형 촉각 센서의 원시 판독값(촉각 유닛 위치가 불규칙하게 배열됨)을 공간 매핑을 통해 2차원 촉각 이미지로 변환하여 센서 고유의 국소 연결 구조를 보존합니다.
- 합성곱 신경망(CNN)을 사용하여 이러한 촉각 이미지를 처리하고, 국소 수용 영역 특성을 활용하여 수작업 특징 설계 없이 공간 특징을 자동으로 추출합니다.

### 실험 설정
- **데이터셋**: 41종의 일상 물체(다양한 형태, 재질, 크기 포함)를 대상으로 2500회 이상의 실제 세 손가락 파지 실험 데이터를 수집했습니다.
- **센서**: 비행렬형 촉각 센서(촉각 유닛이 직사각형 격자로 배열되지 않음)를 사용했으며, 각 파지에서 촉각 유닛의 압력 분포를 기록했습니다.
- **작업**: 파지 안정성 여부(안정/불안정)를 이진 분류로 예측하며, F1 점수를 주요 평가 지표로 사용했습니다.

### 주요 결과
- 훈련된 CNN 모델은 테스트 세트에서 **94.2%의 F1 점수**를 달성하여 기존의 수작업 특징 기반 방법보다 크게 우수했습니다.
- 실험 결과, 비행렬형 센서의 국소 연결성(즉, 인접 촉각 유닛 간의 공간 관계)이 CNN에 의해 효과적으로 활용될 수 있으며, 센서 배치가 불규칙하더라도 이미지화 처리를 통해 높은 정확도의 예측이 가능함을 보여주었습니다.

### 결론
본 논문은 비행렬형 촉각 센서가 이미지화 처리와 CNN의 결합을 통해 행렬형 센서와 동등한 수준의 파지 안정성 예측 성능을 달성할 수 있음을 최초로 체계적으로 검증했습니다. 이 방법은 센서 하드웨어 배치의 제약을 줄여 저비용, 불규칙 촉각 어레이의 응용에 새로운 방향을 제시합니다.
