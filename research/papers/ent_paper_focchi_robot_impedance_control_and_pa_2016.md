---
$id: ent_paper_focchi_robot_impedance_control_and_pa_2016
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Robot Impedance Control and Passivity Analysis with Inner Torque and Velocity
    Feedback Loops
  zh: 基于内环力矩与速度反馈的机器人阻抗控制及无源性分析
  ko: 내부 토크 및 속도 피드백 루프를 갖춘 로봇 임피던스 제어 및 수동성 분석
summary:
  en: This paper analyzes how inner-loop torque bandwidth, velocity filtering, and
    sampling rate constrain the stable stiffness and damping range (Z-width) of impedance-controlled
    electric joints, and proposes a design method using positive velocity feedback
    to increase torque-loop bandwidth without increasing controller complexity.
  zh: 本文分析了内环力矩带宽、速度滤波和采样频率如何限制阻抗控制电动关节的稳定刚度与阻尼范围（Z-width），并提出一种利用正速度反馈扩大力矩环带宽而无需复杂控制器的设计方法。
  ko: 본 논문은 내륜 토크 대역폭, 속도 필터링 및 샘플링 주파수가 임피던스 제어 전기 관절의 안정적인 강성과 감쇠 범위(Z-width)를 제한하는
    방식을 분석하고, 복잡한 제어기 없이 토크 루프 대역폭을 확대하기 위한 양의 속도 피드백 설계 방법을 제안한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; full-text verification
    and human review are required before promotion to verified.
sources:
- id: src_001
  type: paper
  title: Robot Impedance Control and Passivity Analysis with Inner Torque and Velocity
    Feedback Loops
  url: https://arxiv.org/abs/1406.4047
  date: '2016'
  accessed_at: '2026-06-27'
  doi: 10.1007/s11768-016-5015-z
theoretical_depth:
- method
---

## Overview

Impedance control is widely used to regulate interaction forces in robots, but real implementations with nested inner loops face a limited range of stable stiffness and damping values—often called the Z-width. This limitation arises from the bandwidth of the inner torque loop, the velocity-filtering strategy, the sampling frequency, and the load inertia. The paper develops a discrete-time model of a gearbox-driven electric joint and applies eigenvalue stability analysis together with positive-real passivity analysis to map how each of these factors affects the stable and passive regions of impedance parameters.

The authors focus on an impedance controller built around an inner PI torque loop and a positive velocity-feedback loop. They show that simply maximizing the inner torque-loop bandwidth can actually shrink the region of impedance parameters that remain stable or passive. The proposed remedy is to use positive velocity feedback to increase the torque-loop bandwidth without resorting to a more complex controller structure. Simulations and experiments on the HyQ quadruped's electric HAA joint are used to validate the analysis across different controller gains, filter lengths, sampling times, and leg-inertia conditions.

The study therefore bridges actuator-level control design and contact stability: it gives concrete guidelines for selecting impedance parameters, torque-loop gains, velocity-feedback gains, and digital-filter settings in torque-controlled electric joints.

## Key Contributions

- Discrete-time stability and passivity analysis of nested impedance/torque/velocity-feedback control that explicitly accounts for actuator dynamics, sampling, filtering, and load variation.
- Demonstration that maximizing the inner torque-loop bandwidth can reduce, rather than enlarge, the region of stable and passive impedance parameters.
- A design methodology using positive velocity feedback to increase torque-loop bandwidth without requiring a complex controller.
- Simulation and experimental validation on the electric hip abduction-adduction (HAA) joint of the HyQ quadruped robot.
- Systematic mapping of stability regions versus torque gain, velocity-compensation gain, averaging-filter length, sampling time, and leg inertia.

## Relevance to Humanoid Robotics

Humanoid robots rely heavily on torque-controlled electric actuators to achieve compliant, predictable contact behavior during walking, manipulation, and physical human interaction. The impedance-control methodology and stability/passivity trade-offs analyzed in this paper apply directly to the design of these joint-level controllers. Understanding how inner-loop bandwidth, digital filtering, and sampling limit the usable stiffness and damping range is essential for building reliable, safe, and mass-producible humanoid hardware.
