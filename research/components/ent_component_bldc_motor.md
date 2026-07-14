---
$id: ent_component_bldc_motor
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Brushless DC Motor
  zh: 无刷直流电机
  ko: 브러시리스 DC 모터
summary:
  en: An electric motor driven by electronic commutation rather than mechanical brushes,
    offering high efficiency, long lifetime, and high power density; widely used as
    the prime mover in robotic joints and humanoid actuators.
  zh: 一种通过电子换向而非机械电刷驱动的电动机，具有高效率、长寿命和高功率密度，广泛用作机器人关节和人形执行器的原动机。
  ko: 기계적 브러시가 아닌 전자적 정류로 구동되는 전동기로, 높은 효율, 긴 수명, 높은 전력 밀도를 제공하며 로봇 관절 및 휴머노이드 액추에이터의
    주 동력원으로 널리 사용됨.
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
functional_roles:
- component
- knowledge
tags:
- bldc
- brushless_motor
- actuator
- electric_motor
- joint_actuation
- power_density
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: General technology entry; specific model data should be added per application.
sources:
- id: src_001
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for
    the Unitree G1 Humanoid Arm
  url: https://arxiv.org/abs/2606.15915
  date: '2026'
  accessed_at: '2026-06-22'
theoretical_depth:
- system
---

# Brushless DC Motor

## 抽象

> **生活实例**：它就像无人机或电动滑板车里那颗高效、耐用的小电机——没有电刷磨损，能把电能持续不断地变成强劲旋转。

> **自然语言逻辑**：无刷直流电机（BLDC）利用电子换向替代机械电刷，具有高效率、长寿命和高功率密度；它是人形机器人关节中最主流的动力来源，与减速器、驱动器和编码器配合，构成紧凑而强劲的高扭矩关节模组。

## Overview

A brushless DC (BLDC) motor uses a permanent-magnet rotor and electronically switched stator windings instead of mechanical commutator brushes. Electronic commutation—typically via Hall-effect sensors or sensorless back-EMF estimation—allows precise control of torque, speed, and position. Compared with brushed DC motors, BLDC motors offer higher efficiency, higher torque-to-inertia ratios, longer service life, reduced electromagnetic interference, and better thermal performance.

In humanoid robotics, BLDC motors are the dominant motor technology inside joint actuators. They are paired with gear reducers (harmonic drives, planetary gears, or cycloidal drives), motor drives, and encoders to form compact, high-torque-density actuator modules. The motor's copper losses, iron losses, and friction characteristics are major contributors to the overall power consumption and thermal budget of a humanoid robot.

## Key Characteristics

- High efficiency (typically 85–95% in the designed operating range)
- High power density and torque-to-inertia ratio
- Long lifetime due to absence of brush wear
- Requires electronic motor controller/inverter
- Copper and iron losses dominate thermal behavior

## Relevance to Humanoid Robotics

BLDC motors are a foundational component for humanoid actuation. Their efficiency and power density directly affect battery life, cooling requirements, and the achievable torque density of joints. Physics-based power models for humanoid arms, such as those developed for the Unitree G1, explicitly model BLDC motor losses to predict electrical power consumption and enable energy-aware motion planning.
