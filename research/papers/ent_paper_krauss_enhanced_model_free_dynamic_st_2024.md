---
$id: ent_paper_krauss_enhanced_model_free_dynamic_st_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Enhanced Model-Free Dynamic State Estimation for a Soft Robot Finger Using an
    Embedded Optical Waveguide Sensor
  zh: 利用嵌入式光波导传感器增强软体机器人手指的无模型动态状态估计
  ko: 내장 광파이드 센서를 이용한 소프트 로봇 손가락의 향상된 모델 프리 동적 상태 추정
summary:
  en: Krauss and Takemura (2024) integrate a semidivided-core stretchable optical
    waveguide sensor into a two-chamber PneuNet soft finger and train NARX neural
    networks to estimate fingertip position directly from pressure and sensor signals,
    reducing mean end-effector estimation error by 51% compared with pressure-only
    input.
  zh: Krauss 与 Takemura（2024）将半分割核心可拉伸光波导传感器集成到双腔 PneuNet 软体手指中，训练 NARX 神经网络直接从气压与传感器信号估计指尖位置，相比仅使用气压输入，平均估计误差降低
    51%。
  ko: Krauss와 Takemura(2024)는 반분할 코어 신축성 광파이드 센서를 2챔버 PneuNet 소프트 손가락에 통합하고, 공기압 및
    센서 신호로부터 최종 위치를 직접 추정하는 NARX 신경망을 훈련시켜 공기압 입력만 사용했을 때보다 평균 추정 오차를 51% 감소시켰다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the paper abstract and supplied metadata; detailed architecture,
    training protocol, and full experimental conditions should be verified against
    the complete text.
sources:
- id: src_001
  type: paper
  title: Enhanced Model-Free Dynamic State Estimation for a Soft Robot Finger Using
    an Embedded Optical Waveguide Sensor
  url: https://arxiv.org/abs/2406.03708
  date: '2024'
  accessed_at: '2026-06-27'
  doi: 10.1109/LRA.2024.3399590
theoretical_depth:
- method
---

## Overview

This 2024 RA-L paper by Henrik Krauss and Kenjiro Takemura presents a soft pneumatic finger that embeds a stretchable optical waveguide sensor with a semidivided core. The finger has two pressure chambers and is designed to reproduce human finger motions such as flexion and abduction/adduction, targeting soft robotic grippers or prosthetic hands. Actuation is delivered through motorized linear stages regulated by a position controller, while an Arduino Mega 2560 handles low-level sensing and an LM358N amplifier conditions the phototransistor outputs. The authors first characterize the workspace and sensor response, then build three dynamic state estimators based on the NARX architecture.

The estimators differ in how much they incorporate the waveguide sensor response: a pressure-only baseline, an estimator using a single averaged waveguide signal, and an estimator using the full two-output waveguide response. The comparison is performed on dynamic test paths over 120 s. The full-sensor NARX estimator reduces mean end-effector position error by 51% compared with the pressure-only case, whereas the averaged-waveguide estimator reduces it by only 21%. The work is conducted on the isolated finger without closed-loop control; the authors frame the results as enabling future model-free state estimation and open-loop model-predictive control of soft robots.

Key materials include Elastosil M4601, Clear Flex 30, and Ecoflex 00-30 for molding, with a Kingbright 880 nm LED and Osram SFH 309 FA phototransistors as the optical pair. The sensor output is fed directly to the NARX network, bypassing the need for explicit strain-mode decoupling. Evaluation is reported at 25 Hz on CPU.

## Key Contributions

- Integration of a semidivided-core stretchable optical waveguide sensor into a custom two-chamber PneuNet soft finger.
- Model-free dynamic state estimation using a NARX neural network without manual decoupling of strain modes.
- Empirical demonstration that the full two-output waveguide response reduces end-effector estimation error by 51% versus pressure-only input.
- Evaluation of open-loop and self-loop prediction stability over 120 s dynamic test paths.
- Discussion of applicability to open-loop model-predictive control and recommendations for advanced multimodal soft optical sensors.

## Relevance to Humanoid Robotics

Soft pneumatic fingers that mimic human digits are fundamental building blocks for compliant robotic and prosthetic hands, which are increasingly relevant as humanoid end-effectors. The improved model-free proprioception demonstrated here—using only internal pressure and optical waveguide signals—could make manipulation more repeatable without relying on expensive external vision systems. Although the tested finger is isolated and runs at 25 Hz on CPU, the sensing approach and NARX-based estimator provide a template for robust low-level state feedback in future humanoid soft hands.
