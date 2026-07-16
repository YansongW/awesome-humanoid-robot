---
$id: ent_paper_focchi_robot_impedance_control_and_pa_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robot Impedance Control and Passivity Analysis with Inner Torque and Velocity Feedback Loops
  zh: 基于内环力矩与速度反馈的机器人阻抗控制及无源性分析
  ko: 내부 토크 및 속도 피드백 루프를 갖춘 로봇 임피던스 제어 및 수동성 분석
summary:
  en: This paper analyzes how inner-loop torque bandwidth, velocity filtering, and sampling rate constrain the stable stiffness
    and damping range (Z-width) of impedance-controlled electric joints, and proposes a design method using positive velocity
    feedback to increase torque-loop bandwidth without increasing controller complexity.
  zh: 本文分析了内环力矩带宽、速度滤波和采样频率如何限制阻抗控制电动关节的稳定刚度与阻尼范围（Z-width），并提出一种利用正速度反馈扩大力矩环带宽而无需复杂控制器的设计方法。
  ko: 본 논문은 내륜 토크 대역폭, 속도 필터링 및 샘플링 주파수가 임피던스 제어 전기 관절의 안정적인 강성과 감쇠 범위(Z-width)를 제한하는 방식을 분석하고, 복잡한 제어기 없이 토크 루프 대역폭을 확대하기
    위한 양의 속도 피드백 설계 방법을 제안한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- impedance_control
- torque_control
- passivity_analysis
- velocity_feedback
- z_width
- joint_actuator
- discrete_time_stability
- hyq_robot
- electric_actuation
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1406.4047v2.
sources:
- id: src_001
  type: paper
  title: Robot Impedance Control and Passivity Analysis with Inner Torque and Velocity Feedback Loops
  url: https://arxiv.org/abs/1406.4047
  date: '2016'
  accessed_at: '2026-06-27'
  doi: 10.1007/s11768-016-5015-z
theoretical_depth:
- method
---
## 概述
Impedance control is a well-established technique to control interaction forces in robotics. However, real implementations of impedance control with an inner loop may suffer from several limitations. Although common practice in designing nested control systems is to maximize the bandwidth of the inner loop to improve tracking performance, it may not be the most suitable approach when a certain range of impedance parameters has to be rendered. In particular, it turns out that the viable range of stable stiffness and damping values can be strongly affected by the bandwidth of the inner control loops (e.g. a torque loop) as well as by the filtering and sampling frequency. This paper provides an extensive analysis on how these aspects influence the stability region of impedance parameters as well as the passivity of the system. This will be supported by both simulations and experimental data. Moreover, a methodology for designing joint impedance controllers based on an inner torque loop and a positive velocity feedback loop will be presented. The goal of the velocity feedback is to increase (given the constraints to preserve stability) the bandwidth of the torque loop without the need of a complex controller.

## 核心内容
Impedance control is a well-established technique to control interaction forces in robotics. However, real implementations of impedance control with an inner loop may suffer from several limitations. Although common practice in designing nested control systems is to maximize the bandwidth of the inner loop to improve tracking performance, it may not be the most suitable approach when a certain range of impedance parameters has to be rendered. In particular, it turns out that the viable range of stable stiffness and damping values can be strongly affected by the bandwidth of the inner control loops (e.g. a torque loop) as well as by the filtering and sampling frequency. This paper provides an extensive analysis on how these aspects influence the stability region of impedance parameters as well as the passivity of the system. This will be supported by both simulations and experimental data. Moreover, a methodology for designing joint impedance controllers based on an inner torque loop and a positive velocity feedback loop will be presented. The goal of the velocity feedback is to increase (given the constraints to preserve stability) the bandwidth of the torque loop without the need of a complex controller.

## 参考
- http://arxiv.org/abs/1406.4047v2

## Overview
Impedance control is a well-established technique to control interaction forces in robotics. However, real implementations of impedance control with an inner loop may suffer from several limitations. Although common practice in designing nested control systems is to maximize the bandwidth of the inner loop to improve tracking performance, it may not be the most suitable approach when a certain range of impedance parameters has to be rendered. In particular, it turns out that the viable range of stable stiffness and damping values can be strongly affected by the bandwidth of the inner control loops (e.g. a torque loop) as well as by the filtering and sampling frequency. This paper provides an extensive analysis on how these aspects influence the stability region of impedance parameters as well as the passivity of the system. This will be supported by both simulations and experimental data. Moreover, a methodology for designing joint impedance controllers based on an inner torque loop and a positive velocity feedback loop will be presented. The goal of the velocity feedback is to increase (given the constraints to preserve stability) the bandwidth of the torque loop without the need of a complex controller.

## Content
Impedance control is a well-established technique to control interaction forces in robotics. However, real implementations of impedance control with an inner loop may suffer from several limitations. Although common practice in designing nested control systems is to maximize the bandwidth of the inner loop to improve tracking performance, it may not be the most suitable approach when a certain range of impedance parameters has to be rendered. In particular, it turns out that the viable range of stable stiffness and damping values can be strongly affected by the bandwidth of the inner control loops (e.g. a torque loop) as well as by the filtering and sampling frequency. This paper provides an extensive analysis on how these aspects influence the stability region of impedance parameters as well as the passivity of the system. This will be supported by both simulations and experimental data. Moreover, a methodology for designing joint impedance controllers based on an inner torque loop and a positive velocity feedback loop will be presented. The goal of the velocity feedback is to increase (given the constraints to preserve stability) the bandwidth of the torque loop without the need of a complex controller.

## 개요
임피던스 제어는 로봇 공학에서 상호작용 힘을 제어하기 위해 잘 정립된 기술입니다. 그러나 내부 루프를 사용하는 임피던스 제어의 실제 구현은 여러 한계를 겪을 수 있습니다. 중첩 제어 시스템을 설계할 때 일반적인 관행은 내부 루프의 대역폭을 최대화하여 추적 성능을 향상시키는 것이지만, 특정 범위의 임피던스 파라미터를 구현해야 하는 경우에는 가장 적합한 접근 방식이 아닐 수 있습니다. 특히, 안정적인 강성 및 감쇠 값의 실현 가능한 범위는 내부 제어 루프(예: 토크 루프)의 대역폭뿐만 아니라 필터링 및 샘플링 주파수에 의해 크게 영향을 받을 수 있습니다. 본 논문은 이러한 측면이 임피던스 파라미터의 안정성 영역과 시스템의 수동성에 어떻게 영향을 미치는지에 대한 광범위한 분석을 제공합니다. 이는 시뮬레이션과 실험 데이터 모두를 통해 뒷받침됩니다. 또한, 내부 토크 루프와 양의 속도 피드백 루프를 기반으로 한 관절 임피던스 제어기 설계 방법론이 제시됩니다. 속도 피드백의 목표는 복잡한 제어기 없이도 (안정성을 유지하기 위한 제약 조건 하에서) 토크 루프의 대역폭을 증가시키는 것입니다.

## 핵심 내용
임피던스 제어는 로봇 공학에서 상호작용 힘을 제어하기 위해 잘 정립된 기술입니다. 그러나 내부 루프를 사용하는 임피던스 제어의 실제 구현은 여러 한계를 겪을 수 있습니다. 중첩 제어 시스템을 설계할 때 일반적인 관행은 내부 루프의 대역폭을 최대화하여 추적 성능을 향상시키는 것이지만, 특정 범위의 임피던스 파라미터를 구현해야 하는 경우에는 가장 적합한 접근 방식이 아닐 수 있습니다. 특히, 안정적인 강성 및 감쇠 값의 실현 가능한 범위는 내부 제어 루프(예: 토크 루프)의 대역폭뿐만 아니라 필터링 및 샘플링 주파수에 의해 크게 영향을 받을 수 있습니다. 본 논문은 이러한 측면이 임피던스 파라미터의 안정성 영역과 시스템의 수동성에 어떻게 영향을 미치는지에 대한 광범위한 분석을 제공합니다. 이는 시뮬레이션과 실험 데이터 모두를 통해 뒷받침됩니다. 또한, 내부 토크 루프와 양의 속도 피드백 루프를 기반으로 한 관절 임피던스 제어기 설계 방법론이 제시됩니다. 속도 피드백의 목표는 복잡한 제어기 없이도 (안정성을 유지하기 위한 제약 조건 하에서) 토크 루프의 대역폭을 증가시키는 것입니다.
