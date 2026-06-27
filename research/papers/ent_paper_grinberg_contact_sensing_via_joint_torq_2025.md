---
$id: ent_paper_grinberg_contact_sensing_via_joint_torq_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contact Sensing via Joint Torque Sensors and a Force/Torque Sensor for Legged
    Robots
  zh: 基于关节力矩传感器和力/力矩传感器的腿式机器人接触感知
  ko: 관절 토크 센서 및 힘/토크 센서를 활용한 다리 로봇 접촉 감지
summary:
  en: This paper presents a generalized momentum-based observer framework that fuses
    low-cost strain-gauge joint torque sensors with a single hip-mounted force/torque
    sensor to detect, localize, and estimate contact forces along robot legs, achieving
    sub-centimeter localization accuracy and force errors below 0.2 N in hardware
    experiments.
  zh: 本文提出了一种广义动量观测器框架，融合低成本应变片关节力矩传感器和单个髋部安装的力/力矩传感器，以检测、定位并估计机器人腿部沿线的接触力，硬件实验实现了亚厘米级定位精度和低于0.2
    N的力误差。
  ko: 본 논문은 저렴한 변형 게이지 관절 토크 센서와 하나의 고관절 장착 힘/토크 센서를 융합하여 로봇 다리의 접촉을 감지하고 위치를 추정하며
    접촉력을 추정하는 일반화된 운동량 기반 관측기 프레임워크를 제안하며, 하드웨어 실험에서 센티미터 미만의 접촉 위치 정확도와 0.2 N 이하의
    힘 오차를 달성했다.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- component
- intelligence
tags:
- contact_sensing
- joint_torque_sensor
- force_torque_sensor
- legged_robots
- collision_detection
- momentum_observer
- strain_gauge_sensor
- tactile_sensing
- contact_localization
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full paper text was not
    provided for cross-checking.
sources:
- id: src_001
  type: paper
  title: Contact Sensing via Joint Torque Sensors and a Force/Torque Sensor for Legged
    Robots
  url: https://arxiv.org/abs/2510.10843
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---


## Overview

Legged robots operating in cluttered environments require reliable contact sensing to ensure safe navigation and robust locomotion. Existing approaches based on motor-current estimation suffer from drivetrain friction, backlash, and nonlinearities, while tactile skins can be fragile and update slowly. This paper proposes a contact-sensing method that combines direct strain-gauge-based joint torque measurements at every joint with a single six-axis force/torque sensor mounted at the hip, all integrated within a generalized momentum-based observer framework.

The framework detects collisions, identifies the contacted link, and estimates both the contact force and its location along the thigh and shin links. The authors designed a low-cost strain-gauge joint torque sensor with a 6061 aluminum body and calibrated it to an average accuracy of 96.4% relative to ground truth. Validation includes simulation studies on fixed-base and floating-base 2-DoF robot legs, as well as hardware experiments on a fixed-base 2-DoF planar manipulator.

The proposed approach aims to eliminate the need for complex friction models by using direct torque measurements, while a single hip-mounted force/torque sensor provides additional information for resolving contact location. The momentum observer formulation leverages the robot's dynamics to recover external contact wrenches from sensor data.

## Key Contributions

- Low-cost custom strain-gauge-based joint torque sensor with 96.4% accuracy relative to ground truth measurements.
- Generalized momentum-based observer framework that fuses joint torque sensor data and a hip-mounted force/torque sensor for multi-link contact detection, contact localization, and contact force estimation.
- Hardware experimental validation on a 2-DoF planar manipulator demonstrating sub-centimeter contact localization accuracy and force errors below 0.2 N.
- Simulation validation on both fixed-base and floating-base 2-DoF robot legs recovering contact force and location along the thigh and shin links.

## Relevance to Humanoid Robotics

Reliable, low-cost, and high-bandwidth contact sensing along robot legs is critical for deploying humanoid robots in cluttered real-world environments. It enables safe obstacle clearance, disturbance rejection, and collision recovery, all of which are essential for robust locomotion outside controlled laboratories. The strain-gauge torque sensor design and the momentum-observer framework are particularly relevant for humanoid hardware because they can be installed on every joint without requiring complex friction modeling.

By providing sub-centimeter localization accuracy and sub-newton force errors, the proposed sensing pipeline supports the reactive behaviors needed for autonomous humanoid navigation. Although the hardware validation is limited to a 2-DoF planar manipulator, the component-level contributions and observer methodology are directly transferable to full-scale legged and humanoid systems.
