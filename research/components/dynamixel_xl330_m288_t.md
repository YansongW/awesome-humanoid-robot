---
$id: ent_component_dynamixel_xl330_m288_t
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: ROBOTIS DYNAMIXEL XL330-M288-T
  zh: ROBOTIS DYNAMIXEL XL330-M288-T 舵机
  ko: ROBOTIS DYNAMIXEL XL330-M288-T
summary:
  en: A compact, low-cost smart servo actuator from ROBOTIS' X-series, featuring TTL communication,
    0.52 N·m stall torque, and a 288.4:1 gear ratio for small robotic joints and fingers.
  zh: ROBOTIS X 系列的小型低成本智能舵机执行器，具有 TTL 通信、0.52 N·m 堵转扭矩和 288.4:1 减速比，适用于小型机器人关节和手指。
  ko: ROBOTIS X 시리즈의 컴팩트한 저비용 스마트 서보 액추에이터로, TTL 통신, 0.52 N·m 정지 토크, 288.4:1 감속비를 갖추어 소형 로봇 관절 및 손가락에 적합함.
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
- xl330
- smart_servo
- actuator
- low_cost
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: Specifications sourced from ROBOTIS product documentation and reseller listings.
sources:
- id: src_001
  type: website
  title: DYNAMIXEL XL330-M288 Product Page
  url: https://emanual.robotis.com/docs/en/dxl/x/xl330-m288/
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

The DYNAMIXEL XL330-M288-T is a compact smart servo in ROBOTIS' entry-level X-series. It integrates a cored DC motor, engineering-plastic spur gear train with a 288.4:1 reduction ratio, a 12-bit contactless magnetic encoder, and a 32-bit ARM Cortex-M0+ controller in a 20 × 34 × 26 mm package weighing only 18 g. Communication is via half-duplex TTL serial bus, and it supports RC protocols without an additional converter.

Despite its small size, the XL330-M288-T provides 0.52 N·m stall torque at 5 V, making it suitable for lightweight robotic fingers and small joints. It supports current control, velocity control, position control, extended position control, current-based position control, and PWM control modes.

## Key Specifications

- Input voltage: 3.7–6.0 V (recommended 5 V)
- Stall torque: 0.52 N·m at 5 V
- Stall current: 1.5 A
- No-load speed: approximately 104 rpm at 5 V
- Gear ratio: 288.4:1
- Weight: 18 g
- Dimensions: 20 × 34 × 26 mm
- Resolution: 4096 steps per revolution (0.0879°)
- Communication: TTL half-duplex serial

## Relevance to Humanoid Robotics

The XL330-M288-T is widely used in low-cost dexterous hands such as the LEAP Hand and its derivatives because of its small size, low cost, and integrated control. It demonstrates how commodity miniature servos can be combined to achieve anthropomorphic hand kinematics on a research budget, providing a practical actuator option for humanoid end-effector design.
