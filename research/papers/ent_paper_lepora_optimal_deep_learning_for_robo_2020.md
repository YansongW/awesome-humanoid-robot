---
$id: ent_paper_lepora_optimal_deep_learning_for_robo_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Optimal Deep Learning for Robot Touch
  zh: 面向机器人触觉的最优深度学习
  ko: 로봇 촉각을 위한 최적 딥러닝
summary:
  en: This 2020 survey and methods paper applies deep learning, specifically ConvNet regression (PoseNet), to estimate the
    3D pose of surfaces and edges from optical tactile sensor images, using unlabelled shear augmentation and Bayesian hyperparameter
    optimization to achieve robustness and accuracy.
  zh: 这篇2020年的综述与方法论文将深度学习（特别是ConvNet回归/PoseNet）应用于光学触觉传感器图像，以估计表面和边缘的三维位姿，通过未标记剪切增强和贝叶斯超参数优化实现鲁棒性与准确性。
  ko: 이 2020년 설문조사 및 방법론 논문은 딥러닝(특히 ConvNet 회귀/PoseNet)을 광학 촉각 센서 이미지에 적용하여 표면과 모서리의 3D 자세를 추정하고, 레이블 없는 전단(shear) 증강과 베이지안
    초모수 최적화를 통해 강건성과 정확도를 달성한다.
domains:
- 02_components
- 07_ai_models_algorithms
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- tactile_sensing
- optical_tactile_sensor
- deep_learning
- pose_estimation
- convnet
- bayesian_optimization
- shear_invariance
- dexterous_manipulation
- robot_touch
- soft_robotics
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2003.01916v2.
sources:
- id: src_001
  type: paper
  title: Optimal Deep Learning for Robot Touch
  url: https://arxiv.org/abs/2003.01916
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---
## 概述
This article illustrates the application of deep learning to robot touch by considering a basic yet fundamental capability: estimating the relative pose of part of an object in contact with a tactile sensor. We begin by surveying deep learning applied to tactile robotics, focussing on optical tactile sensors, which help bridge from deep learning for vision to touch. We then show how deep learning can be used to train accurate pose models of 3D surfaces and edges that are insensitive to nuisance variables such as motion-dependent shear. This involves including representative motions as unlabelled perturbations of the training data and using Bayesian optimization of the network and training hyperparameters to find the most accurate models. Accurate estimation of pose from touch will enable robots to safely and precisely control their physical interactions, underlying a wide range of object exploration and manipulation tasks.

## 核心内容
This article illustrates the application of deep learning to robot touch by considering a basic yet fundamental capability: estimating the relative pose of part of an object in contact with a tactile sensor. We begin by surveying deep learning applied to tactile robotics, focussing on optical tactile sensors, which help bridge from deep learning for vision to touch. We then show how deep learning can be used to train accurate pose models of 3D surfaces and edges that are insensitive to nuisance variables such as motion-dependent shear. This involves including representative motions as unlabelled perturbations of the training data and using Bayesian optimization of the network and training hyperparameters to find the most accurate models. Accurate estimation of pose from touch will enable robots to safely and precisely control their physical interactions, underlying a wide range of object exploration and manipulation tasks.

## 参考
- http://arxiv.org/abs/2003.01916v2

## Overview
This article illustrates the application of deep learning to robot touch by considering a basic yet fundamental capability: estimating the relative pose of part of an object in contact with a tactile sensor. We begin by surveying deep learning applied to tactile robotics, focussing on optical tactile sensors, which help bridge from deep learning for vision to touch. We then show how deep learning can be used to train accurate pose models of 3D surfaces and edges that are insensitive to nuisance variables such as motion-dependent shear. This involves including representative motions as unlabelled perturbations of the training data and using Bayesian optimization of the network and training hyperparameters to find the most accurate models. Accurate estimation of pose from touch will enable robots to safely and precisely control their physical interactions, underlying a wide range of object exploration and manipulation tasks.

## Content
This article illustrates the application of deep learning to robot touch by considering a basic yet fundamental capability: estimating the relative pose of part of an object in contact with a tactile sensor. We begin by surveying deep learning applied to tactile robotics, focussing on optical tactile sensors, which help bridge from deep learning for vision to touch. We then show how deep learning can be used to train accurate pose models of 3D surfaces and edges that are insensitive to nuisance variables such as motion-dependent shear. This involves including representative motions as unlabelled perturbations of the training data and using Bayesian optimization of the network and training hyperparameters to find the most accurate models. Accurate estimation of pose from touch will enable robots to safely and precisely control their physical interactions, underlying a wide range of object exploration and manipulation tasks.

## 개요
본 논문은 로봇 촉각에 딥러닝을 적용하는 방법을, 촉각 센서와 접촉하는 물체 일부의 상대적 자세를 추정하는 기본적이면서도 핵심적인 능력을 통해 설명합니다. 먼저 촉각 로봇공학에 적용된 딥러닝을 조사하며, 특히 시각 딥러닝과 촉각을 연결하는 광학 촉각 센서에 초점을 맞춥니다. 그런 다음 딥러닝을 사용하여 움직임에 따른 전단력과 같은 방해 변수에 영향을 받지 않는 3D 표면 및 모서리의 정확한 자세 모델을 훈련하는 방법을 보여줍니다. 여기에는 대표적인 움직임을 훈련 데이터의 레이블이 없는 섭동으로 포함시키고, 네트워크 및 훈련 하이퍼파라미터의 베이지안 최적화를 통해 가장 정확한 모델을 찾는 과정이 포함됩니다. 촉각을 통한 정확한 자세 추정은 로봇이 물리적 상호작용을 안전하고 정밀하게 제어할 수 있게 하여, 다양한 물체 탐색 및 조작 작업의 기반이 됩니다.

## 핵심 내용
본 논문은 로봇 촉각에 딥러닝을 적용하는 방법을, 촉각 센서와 접촉하는 물체 일부의 상대적 자세를 추정하는 기본적이면서도 핵심적인 능력을 통해 설명합니다. 먼저 촉각 로봇공학에 적용된 딥러닝을 조사하며, 특히 시각 딥러닝과 촉각을 연결하는 광학 촉각 센서에 초점을 맞춥니다. 그런 다음 딥러닝을 사용하여 움직임에 따른 전단력과 같은 방해 변수에 영향을 받지 않는 3D 표면 및 모서리의 정확한 자세 모델을 훈련하는 방법을 보여줍니다. 여기에는 대표적인 움직임을 훈련 데이터의 레이블이 없는 섭동으로 포함시키고, 네트워크 및 훈련 하이퍼파라미터의 베이지안 최적화를 통해 가장 정확한 모델을 찾는 과정이 포함됩니다. 촉각을 통한 정확한 자세 추정은 로봇이 물리적 상호작용을 안전하고 정밀하게 제어할 수 있게 하여, 다양한 물체 탐색 및 조작 작업의 기반이 됩니다.
