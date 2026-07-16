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
  en: Introduces PROM-Net, a lightweight unsupervised encoder-decoder convolutional LSTM network that predicts up to 10 future
    frames from raw video, and proposes integrating these predictions into a model predictive controller for robot motion
    planning in dynamic environments.
  zh: 提出了PROM-Net，一种轻量级无监督编码器-解码器卷积LSTM网络，可从原始视频预测多达10帧未来画面，并建议将这些预测集成到模型预测控制器中，用于动态环境中的机器人运动规划。
  ko: 원시 비디오에서 최대 10프레임의 미래를 예측하는 경량 비지도 인코더-디코더 컨볼루션 LSTM 네트워크인 PROM-Net을 소개하고, 동적 환경에서 로봇 동작 계획을 위해 이러한 예측을 모델 예측 제어기에 통합하는
    프레임워크를 제안한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1906.10182v1.
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
## 概述
In this paper, we introduce a novel framework that can learn to make visual predictions about the motion of a robotic agent from raw video frames. Our proposed motion prediction network (PROM-Net) can learn in a completely unsupervised manner and efficiently predict up to 10 frames in the future. Moreover, unlike any other motion prediction models, it is lightweight and once trained it can be easily implemented on mobile platforms that have very limited computing capabilities. We have created a new robotic data set comprising LEGO Mindstorms moving along various trajectories in three different environments under different lighting conditions for testing and training the network. Finally, we introduce a framework that would use the predicted frames from the network as an input to a model predictive controller for motion planning in unknown dynamic environments with moving obstacles.

## 核心内容
In this paper, we introduce a novel framework that can learn to make visual predictions about the motion of a robotic agent from raw video frames. Our proposed motion prediction network (PROM-Net) can learn in a completely unsupervised manner and efficiently predict up to 10 frames in the future. Moreover, unlike any other motion prediction models, it is lightweight and once trained it can be easily implemented on mobile platforms that have very limited computing capabilities. We have created a new robotic data set comprising LEGO Mindstorms moving along various trajectories in three different environments under different lighting conditions for testing and training the network. Finally, we introduce a framework that would use the predicted frames from the network as an input to a model predictive controller for motion planning in unknown dynamic environments with moving obstacles.

## 参考
- http://arxiv.org/abs/1906.10182v1

## Overview
In this paper, we introduce a novel framework that can learn to make visual predictions about the motion of a robotic agent from raw video frames. Our proposed motion prediction network (PROM-Net) can learn in a completely unsupervised manner and efficiently predict up to 10 frames in the future. Moreover, unlike any other motion prediction models, it is lightweight and once trained it can be easily implemented on mobile platforms that have very limited computing capabilities. We have created a new robotic data set comprising LEGO Mindstorms moving along various trajectories in three different environments under different lighting conditions for testing and training the network. Finally, we introduce a framework that would use the predicted frames from the network as an input to a model predictive controller for motion planning in unknown dynamic environments with moving obstacles.

## Content
In this paper, we introduce a novel framework that can learn to make visual predictions about the motion of a robotic agent from raw video frames. Our proposed motion prediction network (PROM-Net) can learn in a completely unsupervised manner and efficiently predict up to 10 frames in the future. Moreover, unlike any other motion prediction models, it is lightweight and once trained it can be easily implemented on mobile platforms that have very limited computing capabilities. We have created a new robotic data set comprising LEGO Mindstorms moving along various trajectories in three different environments under different lighting conditions for testing and training the network. Finally, we introduce a framework that would use the predicted frames from the network as an input to a model predictive controller for motion planning in unknown dynamic environments with moving obstacles.

## 개요
본 논문에서는 로봇 에이전트의 움직임에 대한 시각적 예측을 원시 비디오 프레임으로부터 학습할 수 있는 새로운 프레임워크를 소개합니다. 제안된 움직임 예측 네트워크(PROM-Net)는 완전히 비지도 방식으로 학습할 수 있으며, 최대 10프레임까지 효율적으로 예측할 수 있습니다. 또한 다른 움직임 예측 모델과 달리 경량화되어 있어, 학습 후에는 컴퓨팅 성능이 매우 제한된 모바일 플랫폼에서도 쉽게 구현할 수 있습니다. 우리는 네트워크의 테스트 및 학습을 위해 세 가지 다른 환경에서 다양한 조명 조건 하에 다양한 궤적으로 움직이는 LEGO Mindstorms로 구성된 새로운 로봇 데이터 세트를 생성했습니다. 마지막으로, 네트워크에서 예측된 프레임을 입력으로 사용하여 움직이는 장애물이 있는 알려지지 않은 동적 환경에서 모션 플래닝을 위한 모델 예측 제어기로 활용하는 프레임워크를 소개합니다.

## 핵심 내용
본 논문에서는 로봇 에이전트의 움직임에 대한 시각적 예측을 원시 비디오 프레임으로부터 학습할 수 있는 새로운 프레임워크를 소개합니다. 제안된 움직임 예측 네트워크(PROM-Net)는 완전히 비지도 방식으로 학습할 수 있으며, 최대 10프레임까지 효율적으로 예측할 수 있습니다. 또한 다른 움직임 예측 모델과 달리 경량화되어 있어, 학습 후에는 컴퓨팅 성능이 매우 제한된 모바일 플랫폼에서도 쉽게 구현할 수 있습니다. 우리는 네트워크의 테스트 및 학습을 위해 세 가지 다른 환경에서 다양한 조명 조건 하에 다양한 궤적으로 움직이는 LEGO Mindstorms로 구성된 새로운 로봇 데이터 세트를 생성했습니다. 마지막으로, 네트워크에서 예측된 프레임을 입력으로 사용하여 움직이는 장애물이 있는 알려지지 않은 동적 환경에서 모션 플래닝을 위한 모델 예측 제어기로 활용하는 프레임워크를 소개합니다.
