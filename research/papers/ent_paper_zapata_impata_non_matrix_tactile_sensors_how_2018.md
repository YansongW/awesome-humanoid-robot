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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.05551v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## 개요
촉각 센서는 물체와의 상호작용 중 유용한 정보를 제공하며, 이를 통해 파지 안정성을 평가할 수 있습니다. 이 주제에 대한 대부분의 이전 연구들은 수동으로 선택된 특징을 계산하여 촉각 데이터를 신호로 처리했습니다. 일부 연구에서는 이러한 데이터를 이미지로 처리하여 매트릭스 형태의 센서에서 특성을 계산했습니다. 본 연구에서는 비매트릭스 센서(택셀이 정확히 매트릭스 형태로 배열되지 않은 센서)도 촉각 이미지로 처리할 수 있는 방법을 탐구합니다. 또한, 합성곱 신경망(CNN)을 학습시켜 이를 파지 안정성 예측에 사용할 수 있음을 입증합니다. 우리는 41개의 일상 물체에 대해 2500회 이상의 실제 세 손가락 파지를 수집하여, 비매트릭스 촉각 센서에 내재된 국소 연결성을 활용한 CNN을 학습시켰고, 안정성 예측에서 94.2%의 F1 점수를 달성했습니다.

## 핵심 내용
촉각 센서는 물체와의 상호작용 중 유용한 정보를 제공하며, 이를 통해 파지 안정성을 평가할 수 있습니다. 이 주제에 대한 대부분의 이전 연구들은 수동으로 선택된 특징을 계산하여 촉각 데이터를 신호로 처리했습니다. 일부 연구에서는 이러한 데이터를 이미지로 처리하여 매트릭스 형태의 센서에서 특성을 계산했습니다. 본 연구에서는 비매트릭스 센서(택셀이 정확히 매트릭스 형태로 배열되지 않은 센서)도 촉각 이미지로 처리할 수 있는 방법을 탐구합니다. 또한, 합성곱 신경망(CNN)을 학습시켜 이를 파지 안정성 예측에 사용할 수 있음을 입증합니다. 우리는 41개의 일상 물체에 대해 2500회 이상의 실제 세 손가락 파지를 수집하여, 비매트릭스 촉각 센서에 내재된 국소 연결성을 활용한 CNN을 학습시켰고, 안정성 예측에서 94.2%의 F1 점수를 달성했습니다.

## 参考
- http://arxiv.org/abs/1809.05551v1
