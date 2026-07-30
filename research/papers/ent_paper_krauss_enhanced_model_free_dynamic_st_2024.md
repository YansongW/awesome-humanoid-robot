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
  zh: Krauss 与 Takemura（2024）将一种半分割芯可拉伸光学波导传感器集成到双腔 PneuNet 软手指中，并训练 NARX 神经网络直接从压力和传感器信号估计指尖位置。相比仅使用压力输入，该方法将末端执行器平均估计误差降低了
    51%。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2406.03708v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
该研究将一种先进的可拉伸光学波导传感器嵌入多方向 PneuNet 软致动器中，利用 NARX 神经网络提升动态状态估计性能。传感器采用半分割芯设计，对多种应变模式敏感，被集成到模拟人类手指运动的双腔软手指中。研究首先表征了软手指的工作空间和传感器响应，随后开发了三种不同传感器融合程度的 NARX 动态状态估计器。在测试路径上的评估表明，完整传感器响应使末端位置估计的平均误差从 5.70 mm 降至 2.80 mm，降幅达 51%，而仅使用单芯波导设计的估计器仅将误差降至 4.53 mm（改善 21%）。

## 核心内容
### 方法
- 传感器采用半分割芯可拉伸光学波导设计，对拉伸、弯曲等多种应变模式敏感，嵌入双腔 PneuNet 软手指中。
- 软手指由两个压力腔室驱动，通过电机线性级控制气动执行，模拟人类手指运动，适用于软体夹爪或手部应用。

### 架构
- 使用 NARX（非线性自回归外生输入）神经网络架构，构建三种动态状态估计器，区别在于光学波导传感器信号的融合程度：
  - 仅压力输入
  - 部分传感器响应（模拟单芯波导设计）
  - 完整传感器响应（半分割芯设计）

### 实验设置
- 首先表征软手指的工作空间及传感器在不同运动模式下的响应特性。
- 在测试路径上评估各估计器的指尖位置估计精度。

### 关键数字
- 完整传感器响应估计器：平均误差从 5.70 mm 降至 2.80 mm，改善 51%。
- 单芯波导模拟估计器：平均误差降至 4.53 mm，仅改善 21%。
- 压力仅输入估计器：平均误差为 5.70 mm。

### 结论
- 完整传感器响应显著提升了模型无关的状态估计精度，适用于软体机器人的开环模型预测控制。
- 未来工作建议聚焦于先进结构化软（光学）传感器，以进一步推动软体机器人的模型无关状态估计与控制。

## Overview
In this letter, an advanced stretchable optical waveguide sensor is implemented into a multidirectional PneuNet soft actuator to enhance dynamic state estimation through a NARX neural network. The stretchable waveguide featuring a semidivided core design from previous work is sensitive to multiple strain modes. It is integrated into a soft finger actuator with two pressure chambers that replicates human finger motions. The soft finger, designed for applications in soft robotic grippers or hands, is viewed in isolation under pneumatic actuation controlled by motorized linear stages. The research first characterizes the soft finger's workspace and sensor response. Subsequently, three dynamic state estimators are developed using NARX architecture, differing in the degree of incorporating the optical waveguide sensor response. Evaluation on a testing path reveals that the full sensor response significantly improves end effector position estimation, reducing mean error by 51\% from 5.70 mm to 2.80 mm, compared to only 21\% improvement to 4.53 mm using the estimator representing a single core waveguide design. The letter concludes by discussing the application of these estimators for (open-loop) model-predictive control and recommends future focus on advanced, structured soft (optical) sensors for model-free state estimation and control of soft robots.

## 개요
본 논문에서는 고급 신축성 광 도파관 센서를 다방향 PneuNet 소프트 액추에이터에 통합하여 NARX 신경망을 통한 동적 상태 추정을 향상시킵니다. 이전 연구에서 개발된 반분할 코어 설계를 특징으로 하는 신축성 도파관은 여러 변형 모드에 민감합니다. 이 센서는 인간 손가락 움직임을 모방하는 두 개의 압력 챔버를 가진 소프트 핑거 액추에이터에 통합됩니다. 소프트 로봇 그리퍼나 핸드에 적용하기 위해 설계된 이 소프트 핑거는 모터 구동 선형 스테이지로 제어되는 공압 작동 하에 단독으로 분석됩니다. 연구는 먼저 소프트 핑거의 작업 공간과 센서 응답을 특성화합니다. 이후, NARX 아키텍처를 사용하여 광 도파관 센서 응답의 통합 정도가 다른 세 가지 동적 상태 추정기를 개발합니다. 테스트 경로에 대한 평가 결과, 전체 센서 응답이 엔드 이펙터 위치 추정을 크게 개선하여 평균 오차를 5.70mm에서 2.80mm로 51% 감소시킨 반면, 단일 코어 도파관 설계를 대표하는 추정기를 사용한 경우 21% 개선(4.53mm)에 그쳤습니다. 논문은 이러한 추정기를 (개루프) 모델 예측 제어에 적용하는 방법을 논의하며, 소프트 로봇의 모델 없는 상태 추정 및 제어를 위한 고급 구조화된 소프트 (광) 센서에 대한 향후 연구를 권장합니다.

## 핵심 내용
본 논문에서는 고급 신축성 광 도파관 센서를 다방향 PneuNet 소프트 액추에이터에 통합하여 NARX 신경망을 통한 동적 상태 추정을 향상시킵니다. 이전 연구에서 개발된 반분할 코어 설계를 특징으로 하는 신축성 도파관은 여러 변형 모드에 민감합니다. 이 센서는 인간 손가락 움직임을 모방하는 두 개의 압력 챔버를 가진 소프트 핑거 액추에이터에 통합됩니다. 소프트 로봇 그리퍼나 핸드에 적용하기 위해 설계된 이 소프트 핑거는 모터 구동 선형 스테이지로 제어되는 공압 작동 하에 단독으로 분석됩니다. 연구는 먼저 소프트 핑거의 작업 공간과 센서 응답을 특성화합니다. 이후, NARX 아키텍처를 사용하여 광 도파관 센서 응답의 통합 정도가 다른 세 가지 동적 상태 추정기를 개발합니다. 테스트 경로에 대한 평가 결과, 전체 센서 응답이 엔드 이펙터 위치 추정을 크게 개선하여 평균 오차를 5.70mm에서 2.80mm로 51% 감소시킨 반면, 단일 코어 도파관 설계를 대표하는 추정기를 사용한 경우 21% 개선(4.53mm)에 그쳤습니다. 논문은 이러한 추정기를 (개루프) 모델 예측 제어에 적용하는 방법을 논의하며, 소프트 로봇의 모델 없는 상태 추정 및 제어를 위한 고급 구조화된 소프트 (광) 센서에 대한 향후 연구를 권장합니다.

## 参考
- http://arxiv.org/abs/2406.03708v1
