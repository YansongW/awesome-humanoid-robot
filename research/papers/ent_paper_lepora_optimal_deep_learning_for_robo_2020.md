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
  en: This 2020 survey and methods paper applies deep learning, specifically ConvNet
    regression (PoseNet), to estimate the 3D pose of surfaces and edges from optical
    tactile sensor images, using unlabelled shear augmentation and Bayesian hyperparameter
    optimization to achieve robustness and accuracy.
  zh: 这篇2020年的综述与方法论文将深度学习（特别是ConvNet回归/PoseNet）应用于光学触觉传感器图像，以估计表面和边缘的三维位姿，通过未标记剪切增强和贝叶斯超参数优化实现鲁棒性与准确性。
  ko: 이 2020년 설문조사 및 방법론 논문은 딥러닝(특히 ConvNet 회귀/PoseNet)을 광학 촉각 센서 이미지에 적용하여 표면과 모서리의
    3D 자세를 추정하고, 레이블 없는 전단(shear) 증강과 베이지안 초모수 최적화를 통해 강건성과 정확도를 달성한다.
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
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from metadata and abstract; full-text review needed to confirm
    section-level citations and exact experimental claims.
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

## Overview

This article surveys the application of deep learning to robot touch, with emphasis on optical tactile sensors that bridge vision-based deep learning to touch. It then presents a method for training ConvNet regression models, referred to as PoseNet, to estimate the 3D pose of surfaces and edges in contact with a soft optical tactile sensor. The method incorporates unlabelled shear perturbations into the training data to make pose estimates insensitive to motion-dependent shear, and applies Bayesian optimization (HyperOpt's Tree-structured Parzen Estimator) to select network architecture and training hyperparameters. The resulting models are evaluated on controlled geometries and demonstrated in closed-loop 3D surface and edge following on complex objects.

The work connects tactile sensing to broader humanoid manipulation by treating pose estimation from touch as a fundamental capability for safe and precise physical interaction. Optical tactile sensors such as TacTip, GelSight, and GelSlim provide high-resolution contact images, enabling convolutional networks to regress pose directly from tactile appearance. The proposed training pipeline addresses nuisance variables—particularly shear caused by contact motion—by augmenting labelled data with unlabelled motion perturbations rather than requiring explicit shear labels.

## Key Contributions

- Demonstrates deep learning for accurate 3D pose estimation from optical tactile images.
- Develops pose models that are robust to motion-dependent shear by including unlabelled shear perturbations in training data.
- Introduces systematic Bayesian optimization of network architecture and training hyperparameters for tactile sensing.
- Demonstrates closed-loop 3D surface and edge following on complex objects using the trained pose models.

## Relevance to Humanoid Robotics

Accurate tactile pose estimation is a core enabling capability for humanoid robot hands, which must control physical contact safely and precisely during dexterous manipulation and object exploration in unstructured environments. By estimating the 3D pose of contacted surfaces and edges, humanoid systems can close the loop on contact geometry, supporting tasks such as grasp adjustment, sliding, and probing. The use of optical tactile sensors and deep learning aligns with the need for compact, high-resolution, and data-driven tactile perception in anthropomorphic end-effectors.
