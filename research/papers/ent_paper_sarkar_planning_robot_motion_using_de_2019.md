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

