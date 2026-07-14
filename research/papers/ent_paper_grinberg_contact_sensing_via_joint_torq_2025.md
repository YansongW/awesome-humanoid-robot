---
$id: ent_paper_grinberg_contact_sensing_via_joint_torq_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Contact Sensing via Joint Torque Sensors and a Force/Torque Sensor for Legged Robots
  zh: 基于关节力矩传感器和力/力矩传感器的腿式机器人接触感知
  ko: 관절 토크 센서 및 힘/토크 센서를 활용한 다리 로봇 접촉 감지
summary:
  en: This paper presents a generalized momentum-based observer framework that fuses low-cost strain-gauge joint torque sensors
    with a single hip-mounted force/torque sensor to detect, localize, and estimate contact forces along robot legs, achieving
    sub-centimeter localization accuracy and force errors below 0.2 N in hardware experiments.
  zh: 本文提出了一种广义动量观测器框架，融合低成本应变片关节力矩传感器和单个髋部安装的力/力矩传感器，以检测、定位并估计机器人腿部沿线的接触力，硬件实验实现了亚厘米级定位精度和低于0.2 N的力误差。
  ko: 본 논문은 저렴한 변형 게이지 관절 토크 센서와 하나의 고관절 장착 힘/토크 센서를 융합하여 로봇 다리의 접촉을 감지하고 위치를 추정하며 접촉력을 추정하는 일반화된 운동량 기반 관측기 프레임워크를 제안하며,
    하드웨어 실험에서 센티미터 미만의 접촉 위치 정확도와 0.2 N 이하의 힘 오차를 달성했다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.10843v1.
sources:
- id: src_001
  type: paper
  title: Contact Sensing via Joint Torque Sensors and a Force/Torque Sensor for Legged Robots
  url: https://arxiv.org/abs/2510.10843
  date: '2025'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
This paper presents a method for detecting and localizing contact along robot legs using distributed joint torque sensors and a single hip-mounted force-torque (FT) sensor using a generalized momentum-based observer framework. We designed a low-cost strain-gauge-based joint torque sensor that can be installed on every joint to provide direct torque measurements, eliminating the need for complex friction models and providing more accurate torque readings than estimation based on motor current. Simulation studies on a floating-based 2-DoF robot leg verified that the proposed framework accurately recovers contact force and location along the thigh and shin links. Through a calibration procedure, our torque sensor achieved an average 96.4% accuracy relative to ground truth measurements. Building upon the torque sensor, we performed hardware experiments on a 2-DoF manipulator, which showed sub-centimeter contact localization accuracy and force errors below 0.2 N.

## 核心内容
This paper presents a method for detecting and localizing contact along robot legs using distributed joint torque sensors and a single hip-mounted force-torque (FT) sensor using a generalized momentum-based observer framework. We designed a low-cost strain-gauge-based joint torque sensor that can be installed on every joint to provide direct torque measurements, eliminating the need for complex friction models and providing more accurate torque readings than estimation based on motor current. Simulation studies on a floating-based 2-DoF robot leg verified that the proposed framework accurately recovers contact force and location along the thigh and shin links. Through a calibration procedure, our torque sensor achieved an average 96.4% accuracy relative to ground truth measurements. Building upon the torque sensor, we performed hardware experiments on a 2-DoF manipulator, which showed sub-centimeter contact localization accuracy and force errors below 0.2 N.

## 参考
- http://arxiv.org/abs/2510.10843v1

