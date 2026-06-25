---
$id: ent_component_dynamixel_xm430_w210_t
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: ROBOTIS DYNAMIXEL XM430-W210-T
  zh: ROBOTIS DYNAMIXEL XM430-W210-T 舵机
  ko: ROBOTIS DYNAMIXEL XM430-W210-T
summary:
  en: A medium-size smart servo actuator from ROBOTIS' X-series, featuring TTL communication,
    3.0 N·m stall torque, absolute encoder feedback, and multiple control modes for robotic
    joints.
  zh: ROBOTIS X 系列的中型智能舵机执行器，具有 TTL 通信、3.0 N·m 堵转扭矩、绝对编码器反馈和多种控制模式，适用于机器人关节。
  ko: ROBOTIS X 시리즈의 중형 스마트 서보 액추에이터로, TTL 통신, 3.0 N·m 정지 토크, 절대형 인코더 피드백 및 다양한 제어 모드를 갖추어 로봇 관절에 적합함.
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
functional_roles:
- component
- knowledge
tags:
- robotis
- dynamixel
- xm430
- smart_servo
- actuator
- ttl
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: Specifications sourced from ROBOTIS product documentation and reseller listings.
sources:
- id: src_001
  type: website
  title: DYNAMIXEL XM430-W210 Product Page
  url: https://emanual.robotis.com/docs/en/dxl/x/xm430-w210/
  date: '2026'
  accessed_at: '2026-06-22'
- id: src_002
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-22'
---

## Overview

The DYNAMIXEL XM430-W210-T is a smart servo actuator in ROBOTIS' X-series lineup. It integrates a coreless DC motor, precious-metal spur gear train with a 212.6:1 reduction ratio, a 12-bit contactless absolute encoder, and a 32-bit ARM Cortex-M3 controller into a compact 28.5 × 46.5 × 34 mm package weighing 82 g. Communication is via half-duplex TTL serial bus, allowing multiple servos to be daisy-chained on a single bus.

The actuator supports multiple operating modes including current control, velocity control, position control, extended position control (multi-turn), current-based position control, and PWM control. It provides feedback on position, velocity, current, temperature, voltage, and trajectory, making it suitable for precise robotic joint control.

## Key Specifications

- Input voltage: 10–14.8 V (recommended 12 V)
- Stall torque: 3.0 N·m at 12 V
- Stall current: 2.3 A
- No-load speed: 77 rpm at 12 V
- Gear ratio: 212.6:1
- Weight: 82 g
- Dimensions: 28.5 × 46.5 × 34 mm
- Resolution: 4096 steps per revolution (0.0879°)
- Communication: TTL half-duplex serial

## Relevance to Humanoid Robotics

The XM430-W210-T is a representative medium-torque smart servo used in research-grade robot hands and small humanoid joints. Its integrated controller and daisy-chain networking simplify wiring and control architecture, while its feedback capabilities support model-based and learning-based control. It is often compared with smaller XL-series servos when selecting actuators for dexterous end effectors.
