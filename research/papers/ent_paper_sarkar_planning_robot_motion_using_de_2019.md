---
$id: ent_paper_sarkar_planning_robot_motion_using_de_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Planning Robot Motion using Deep Visual Prediction
  zh: 利用深度视觉预测规划机器人运动
  ko: 딥 비주얼 예측을 이용한 로봇 동작 계획
summary:
  en: Introduces PROM-Net, a lightweight unsupervised encoder-decoder convolutional
    LSTM network that predicts up to 10 future frames from raw video, and proposes
    integrating these predictions into a model predictive controller for robot motion
    planning in dynamic environments.
  zh: 提出了PROM-Net，一种轻量级无监督编码器-解码器卷积LSTM网络，可从原始视频预测多达10帧未来画面，并建议将这些预测集成到模型预测控制器中，用于动态环境中的机器人运动规划。
  ko: 원시 비디오에서 최대 10프레임의 미래를 예측하는 경량 비지도 인코더-디코더 컨볼루션 LSTM 네트워크인 PROM-Net을 소개하고, 동적
    환경에서 로봇 동작 계획을 위해 이러한 예측을 모델 예측 제어기에 통합하는 프레임워크를 제안한다.
domains:
- 07_ai_models_algorithms
- 11_applications_markets
- 02_components
layers:
- intelligence
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
tags:
- visual_prediction
- motion_prediction
- unsupervised_learning
- conv_lstm
- encoder_decoder
- model_predictive_control
- dynamic_environments
- mobile_robotics
- lego_mindstorms
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided paper metadata and abstract; full-text verification
    needed before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Planning Robot Motion using Deep Visual Prediction
  url: https://arxiv.org/abs/1906.10182
  date: '2019'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Sarkar, Pradhan, and Ghose (2019) address robot path planning in unknown dynamic environments by predicting the future motion of obstacles and agents directly from raw video frames. They propose PROM-Net (PROposal-based Motion prediction Network), a lightweight encoder-decoder convolutional LSTM architecture trained in a completely unsupervised manner. Once trained, the network can forecast up to ten future frames while remaining compact enough (~5 MB, ~6 million parameters) for deployment on mobile platforms with limited computing resources.

The authors created the Actual Robot Motion (ARM) dataset to support this work. ARM captures LEGO Mindstorms robots moving along diverse trajectories in three different environments under varying lighting conditions, filmed from a first-person robot perspective using a GoPro Hero 5 Black camera. The dataset is complemented by a ROS-Gazebo simulated Turtlebot dataset. The paper evaluates prediction quality using standard image metrics (PSNR and SSIM) and outlines a planning framework in which PROM-Net's predicted frames are fed into a model predictive controller (MPC) to navigate dynamic scenes with moving obstacles.

Although the full vision-based MPC integration is proposed rather than experimentally validated, the work demonstrates that unsupervised future-frame prediction can be made sufficiently lightweight and accurate for real-time robotic applications.

## Key Contributions

- PROM-Net: a lightweight unsupervised motion prediction network that forecasts up to 10 future frames from raw video.
- A compact architecture (~5 MB, ~6M parameters) suitable for mobile and GPU-constrained platforms.
- Creation of the Actual Robot Motion (ARM) dataset, the first dataset to capture robot motion from a first-person robot perspective using LEGO Mindstorms.
- A framework for feeding predicted frames into a model predictive controller for motion planning in dynamic environments with moving obstacles.

## Relevance to Humanoid Robotics

Humanoid robots operating in human-centered environments must perceive, anticipate, and react to dynamic obstacles in real time, often under tight onboard compute budgets. PROM-Net's lightweight unsupervised visual prediction pipeline directly supports this need by enabling future-frame forecasting without requiring large supervised datasets or powerful GPUs. The proposed coupling with model predictive control is also directly applicable to humanoid locomotion and manipulation planning, where anticipating the motion of people and objects is essential for safe interaction.
