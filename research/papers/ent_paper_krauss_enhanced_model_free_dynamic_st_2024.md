---
$id: ent_paper_krauss_enhanced_model_free_dynamic_st_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhanced Model-Free Dynamic State Estimation for a Soft Robot Finger Using an Embedded Optical Waveguide Sensor
  zh: 利用嵌入式光波导传感器增强软体机器人手指的无模型动态状态估计
  ko: 내장 광파이드 센서를 이용한 소프트 로봇 손가락의 향상된 모델 프리 동적 상태 추정
summary:
  en: Krauss and Takemura (2024) integrate a semidivided-core stretchable optical waveguide sensor into a two-chamber PneuNet
    soft finger and train NARX neural networks to estimate fingertip position directly from pressure and sensor signals, reducing
    mean end-effector estimation error by 51% compared with pressure-only input.
  zh: Krauss 与 Takemura（2024）将半分割核心可拉伸光波导传感器集成到双腔 PneuNet 软体手指中，训练 NARX 神经网络直接从气压与传感器信号估计指尖位置，相比仅使用气压输入，平均估计误差降低 51%。
  ko: Krauss와 Takemura(2024)는 반분할 코어 신축성 광파이드 센서를 2챔버 PneuNet 소프트 손가락에 통합하고, 공기압 및 센서 신호로부터 최종 위치를 직접 추정하는 NARX 신경망을 훈련시켜
    공기압 입력만 사용했을 때보다 평균 추정 오차를 51% 감소시켰다.
domains:
- 02_components
- 07_ai_models_algorithms
- 06_design_engineering
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- soft_robotics
- pneumatic_finger
- optical_waveguide_sensor
- narx_neural_network
- dynamic_state_estimation
- proprioception
- model_free_control
- soft_gripper
- soft_hand
- pneunet
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.03708v1.
sources:
- id: src_001
  type: paper
  title: Enhanced Model-Free Dynamic State Estimation for a Soft Robot Finger Using an Embedded Optical Waveguide Sensor
  url: https://arxiv.org/abs/2406.03708
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3399590
theoretical_depth:
- method
---
## 概述
In this letter, an advanced stretchable optical waveguide sensor is implemented into a multidirectional PneuNet soft actuator to enhance dynamic state estimation through a NARX neural network. The stretchable waveguide featuring a semidivided core design from previous work is sensitive to multiple strain modes. It is integrated into a soft finger actuator with two pressure chambers that replicates human finger motions. The soft finger, designed for applications in soft robotic grippers or hands, is viewed in isolation under pneumatic actuation controlled by motorized linear stages. The research first characterizes the soft finger's workspace and sensor response. Subsequently, three dynamic state estimators are developed using NARX architecture, differing in the degree of incorporating the optical waveguide sensor response. Evaluation on a testing path reveals that the full sensor response significantly improves end effector position estimation, reducing mean error by 51\% from 5.70 mm to 2.80 mm, compared to only 21\% improvement to 4.53 mm using the estimator representing a single core waveguide design. The letter concludes by discussing the application of these estimators for (open-loop) model-predictive control and recommends future focus on advanced, structured soft (optical) sensors for model-free state estimation and control of soft robots.

## 核心内容
In this letter, an advanced stretchable optical waveguide sensor is implemented into a multidirectional PneuNet soft actuator to enhance dynamic state estimation through a NARX neural network. The stretchable waveguide featuring a semidivided core design from previous work is sensitive to multiple strain modes. It is integrated into a soft finger actuator with two pressure chambers that replicates human finger motions. The soft finger, designed for applications in soft robotic grippers or hands, is viewed in isolation under pneumatic actuation controlled by motorized linear stages. The research first characterizes the soft finger's workspace and sensor response. Subsequently, three dynamic state estimators are developed using NARX architecture, differing in the degree of incorporating the optical waveguide sensor response. Evaluation on a testing path reveals that the full sensor response significantly improves end effector position estimation, reducing mean error by 51\% from 5.70 mm to 2.80 mm, compared to only 21\% improvement to 4.53 mm using the estimator representing a single core waveguide design. The letter concludes by discussing the application of these estimators for (open-loop) model-predictive control and recommends future focus on advanced, structured soft (optical) sensors for model-free state estimation and control of soft robots.

## 参考
- http://arxiv.org/abs/2406.03708v1

