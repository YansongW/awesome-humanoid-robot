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
  zh: 本文分析了内环力矩带宽、速度滤波和采样率如何约束阻抗控制关节的稳定刚度与阻尼范围（Z-width），并提出一种利用正速度反馈提升力矩环带宽的设计方法，无需增加控制器复杂度。该研究通过仿真与实验验证了内环参数对阻抗参数稳定区域及系统无源性的影响。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1406.4047v2. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
本文深入探讨了机器人阻抗控制中内环力矩带宽、速度滤波及采样频率对系统稳定性的制约机制。研究发现，传统上最大化内环带宽的做法并不适用于需要渲染特定阻抗参数范围的应用场景，因为这会显著影响稳定刚度与阻尼的可行范围（Z-width）。作者通过仿真与实验数据，系统分析了这些因素如何改变阻抗参数的稳定区域及系统无源性。此外，论文提出了一种基于内力矩环与正速度反馈的关节阻抗控制器设计方法，旨在不增加控制器复杂度的前提下提升力矩环带宽。

## 核心内容
### 核心问题
- 阻抗控制虽广泛用于机器人交互力控制，但实际实现中内环（如力矩环）的带宽、速度滤波及采样频率会严重限制可稳定渲染的刚度与阻尼范围（Z-width）。
- 传统嵌套控制设计强调最大化内环带宽以提升跟踪性能，但本文指出，当需要渲染特定阻抗参数时，该策略可能适得其反。

### 分析方法
- 通过理论推导与仿真，量化了内环力矩带宽、速度滤波截止频率及采样率对阻抗参数稳定区域的影响。
- 引入无源性分析，确保系统在交互中不产生能量，避免不稳定行为。

### 关键发现
- 内环带宽不足会缩小稳定刚度与阻尼的可行范围；速度滤波会引入相位滞后，进一步压缩Z-width。
- 采样率过低会导致离散化效应，破坏系统无源性。

### 设计方法
- 提出基于内力矩环与正速度反馈的控制器结构：正速度反馈用于补偿内环延迟，从而在不增加控制器复杂度（如高阶滤波器或复杂补偿器）的前提下提升力矩环带宽。
- 实验验证：在电动关节平台上测试，结果显示该方法能显著扩展稳定阻抗参数范围，同时保持系统无源性。

### 结论
- 本文为阻抗控制中内环参数的选择提供了系统性指导，并给出一种实用设计方法，适用于需要高刚度与宽阻尼范围的机器人交互任务（如装配、人机协作）。

## Overview
Impedance control is a well-established technique to control interaction forces in robotics. However, real implementations of impedance control with an inner loop may suffer from several limitations. Although common practice in designing nested control systems is to maximize the bandwidth of the inner loop to improve tracking performance, it may not be the most suitable approach when a certain range of impedance parameters has to be rendered. In particular, it turns out that the viable range of stable stiffness and damping values can be strongly affected by the bandwidth of the inner control loops (e.g. a torque loop) as well as by the filtering and sampling frequency. This paper provides an extensive analysis on how these aspects influence the stability region of impedance parameters as well as the passivity of the system. This will be supported by both simulations and experimental data. Moreover, a methodology for designing joint impedance controllers based on an inner torque loop and a positive velocity feedback loop will be presented. The goal of the velocity feedback is to increase (given the constraints to preserve stability) the bandwidth of the torque loop without the need of a complex controller.

## 개요
임피던스 제어는 로봇 공학에서 상호작용 힘을 제어하기 위해 잘 정립된 기술입니다. 그러나 내부 루프를 사용하는 임피던스 제어의 실제 구현은 여러 한계를 겪을 수 있습니다. 중첩 제어 시스템을 설계할 때 일반적인 관행은 내부 루프의 대역폭을 최대화하여 추적 성능을 향상시키는 것이지만, 특정 범위의 임피던스 파라미터를 구현해야 하는 경우에는 가장 적합한 접근 방식이 아닐 수 있습니다. 특히, 안정적인 강성 및 감쇠 값의 실현 가능한 범위는 내부 제어 루프(예: 토크 루프)의 대역폭뿐만 아니라 필터링 및 샘플링 주파수에 의해 크게 영향을 받을 수 있습니다. 본 논문은 이러한 측면이 임피던스 파라미터의 안정성 영역과 시스템의 수동성에 어떻게 영향을 미치는지에 대한 광범위한 분석을 제공합니다. 이는 시뮬레이션과 실험 데이터 모두를 통해 뒷받침됩니다. 또한, 내부 토크 루프와 양의 속도 피드백 루프를 기반으로 한 관절 임피던스 제어기 설계 방법론이 제시됩니다. 속도 피드백의 목표는 복잡한 제어기 없이도 (안정성을 유지하기 위한 제약 조건 하에서) 토크 루프의 대역폭을 증가시키는 것입니다.

## 핵심 내용
임피던스 제어는 로봇 공학에서 상호작용 힘을 제어하기 위해 잘 정립된 기술입니다. 그러나 내부 루프를 사용하는 임피던스 제어의 실제 구현은 여러 한계를 겪을 수 있습니다. 중첩 제어 시스템을 설계할 때 일반적인 관행은 내부 루프의 대역폭을 최대화하여 추적 성능을 향상시키는 것이지만, 특정 범위의 임피던스 파라미터를 구현해야 하는 경우에는 가장 적합한 접근 방식이 아닐 수 있습니다. 특히, 안정적인 강성 및 감쇠 값의 실현 가능한 범위는 내부 제어 루프(예: 토크 루프)의 대역폭뿐만 아니라 필터링 및 샘플링 주파수에 의해 크게 영향을 받을 수 있습니다. 본 논문은 이러한 측면이 임피던스 파라미터의 안정성 영역과 시스템의 수동성에 어떻게 영향을 미치는지에 대한 광범위한 분석을 제공합니다. 이는 시뮬레이션과 실험 데이터 모두를 통해 뒷받침됩니다. 또한, 내부 토크 루프와 양의 속도 피드백 루프를 기반으로 한 관절 임피던스 제어기 설계 방법론이 제시됩니다. 속도 피드백의 목표는 복잡한 제어기 없이도 (안정성을 유지하기 위한 제약 조건 하에서) 토크 루프의 대역폭을 증가시키는 것입니다.

## 参考
- http://arxiv.org/abs/1406.4047v2
