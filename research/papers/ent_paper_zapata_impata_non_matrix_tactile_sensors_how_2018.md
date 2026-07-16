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
  zh: Tactile sensors supply useful information during the interaction with an object that can be used for assessing the stability
    of a grasp. Most of the previous works on this topic processed tactile readings as signals by calculating hand-picked
    features. Some of them have processed these readings as images calculating characteristics on matrix-like sensors. In
    this work, we explore how non-matrix sensors (sensors with taxels not arranged exactly in a matrix) can be processed as
    tactile images as well. In addition, we prove that they can be used for predicting grasp stability by training a Convol
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.05551v1.
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
Tactile sensors supply useful information during the interaction with an object that can be used for assessing the stability of a grasp. Most of the previous works on this topic processed tactile readings as signals by calculating hand-picked features. Some of them have processed these readings as images calculating characteristics on matrix-like sensors. In this work, we explore how non-matrix sensors (sensors with taxels not arranged exactly in a matrix) can be processed as tactile images as well. In addition, we prove that they can be used for predicting grasp stability by training a Convolutional Neural Network (CNN) with them. We captured over 2500 real three-fingered grasps on 41 everyday objects to train a CNN that exploited the local connectivity inherent on the non-matrix tactile sensors, achieving 94.2% F1-score on predicting stability.

## 核心内容
Tactile sensors supply useful information during the interaction with an object that can be used for assessing the stability of a grasp. Most of the previous works on this topic processed tactile readings as signals by calculating hand-picked features. Some of them have processed these readings as images calculating characteristics on matrix-like sensors. In this work, we explore how non-matrix sensors (sensors with taxels not arranged exactly in a matrix) can be processed as tactile images as well. In addition, we prove that they can be used for predicting grasp stability by training a Convolutional Neural Network (CNN) with them. We captured over 2500 real three-fingered grasps on 41 everyday objects to train a CNN that exploited the local connectivity inherent on the non-matrix tactile sensors, achieving 94.2% F1-score on predicting stability.

## 参考
- http://arxiv.org/abs/1809.05551v1

## Overview
Tactile sensors supply useful information during the interaction with an object that can be used for assessing the stability of a grasp. Most of the previous works on this topic processed tactile readings as signals by calculating hand-picked features. Some of them have processed these readings as images calculating characteristics on matrix-like sensors. In this work, we explore how non-matrix sensors (sensors with taxels not arranged exactly in a matrix) can be processed as tactile images as well. In addition, we prove that they can be used for predicting grasp stability by training a Convolutional Neural Network (CNN) with them. We captured over 2500 real three-fingered grasps on 41 everyday objects to train a CNN that exploited the local connectivity inherent on the non-matrix tactile sensors, achieving 94.2% F1-score on predicting stability.

## Content
Tactile sensors supply useful information during the interaction with an object that can be used for assessing the stability of a grasp. Most of the previous works on this topic processed tactile readings as signals by calculating hand-picked features. Some of them have processed these readings as images calculating characteristics on matrix-like sensors. In this work, we explore how non-matrix sensors (sensors with taxels not arranged exactly in a matrix) can be processed as tactile images as well. In addition, we prove that they can be used for predicting grasp stability by training a Convolutional Neural Network (CNN) with them. We captured over 2500 real three-fingered grasps on 41 everyday objects to train a CNN that exploited the local connectivity inherent on the non-matrix tactile sensors, achieving 94.2% F1-score on predicting stability.

## 개요
촉각 센서는 물체와의 상호작용 중 유용한 정보를 제공하며, 이를 통해 파지 안정성을 평가할 수 있습니다. 이 주제에 대한 대부분의 이전 연구들은 수동으로 선택된 특징을 계산하여 촉각 데이터를 신호로 처리했습니다. 일부 연구에서는 이러한 데이터를 이미지로 처리하여 매트릭스 형태의 센서에서 특성을 계산했습니다. 본 연구에서는 비매트릭스 센서(택셀이 정확히 매트릭스 형태로 배열되지 않은 센서)도 촉각 이미지로 처리할 수 있는 방법을 탐구합니다. 또한, 합성곱 신경망(CNN)을 학습시켜 이를 파지 안정성 예측에 사용할 수 있음을 입증합니다. 우리는 41개의 일상 물체에 대해 2500회 이상의 실제 세 손가락 파지를 수집하여, 비매트릭스 촉각 센서에 내재된 국소 연결성을 활용한 CNN을 학습시켰고, 안정성 예측에서 94.2%의 F1 점수를 달성했습니다.

## 핵심 내용
촉각 센서는 물체와의 상호작용 중 유용한 정보를 제공하며, 이를 통해 파지 안정성을 평가할 수 있습니다. 이 주제에 대한 대부분의 이전 연구들은 수동으로 선택된 특징을 계산하여 촉각 데이터를 신호로 처리했습니다. 일부 연구에서는 이러한 데이터를 이미지로 처리하여 매트릭스 형태의 센서에서 특성을 계산했습니다. 본 연구에서는 비매트릭스 센서(택셀이 정확히 매트릭스 형태로 배열되지 않은 센서)도 촉각 이미지로 처리할 수 있는 방법을 탐구합니다. 또한, 합성곱 신경망(CNN)을 학습시켜 이를 파지 안정성 예측에 사용할 수 있음을 입증합니다. 우리는 41개의 일상 물체에 대해 2500회 이상의 실제 세 손가락 파지를 수집하여, 비매트릭스 촉각 센서에 내재된 국소 연결성을 활용한 CNN을 학습시켰고, 안정성 예측에서 94.2%의 F1 점수를 달성했습니다.
