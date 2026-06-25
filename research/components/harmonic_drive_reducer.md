---
$id: ent_component_harmonic_drive_reducer
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Harmonic Drive Reducer
  zh: 谐波减速器
  ko: 하모닉 드라이브 감속기
summary:
  en: A high-ratio, zero-backlash gear reducer based on a flexible spline, circular spline,
    and wave generator, valued in humanoid joints for compact size, high torque capacity,
    and precise motion transmission.
  zh: 一种基于柔性轴承、刚轮和波发生器的高减速比、零背隙减速器，因其结构紧凑、扭矩容量大、运动传递精确而广泛用于人形机器人关节。
  ko: 플렉스플라인, 서큘러 스플라인, 웨이브 제너레이터를 기반으로 한 고감속비, 제로 백래시 기어 감속기로, 컴팩트한 크기와 높은 토크 용량, 정밀한 동력 전달 때문에 휴머노이드 관절에서 높이 평가됨.
domains:
- 02_components
- 06_design_engineering
layers:
- upstream
functional_roles:
- component
- knowledge
tags:
- harmonic_drive
- gear_reducer
- zero_backlash
- high_ratio
- joint_transmission
- precision_gearing
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: General technology entry; specific product variants can be added as separate entries.
sources:
- id: src_001
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for the
    Unitree G1 Humanoid Arm
  url: https://arxiv.org/abs/2606.15915
  date: '2026'
  accessed_at: '2026-06-22'
---

# Harmonic Drive Reducer

## 抽象

> **生活实例**：它就像自行车里那个小巧而强劲的变速器——让一只小脚踩出的快速旋转，变成车轮上足以爬坡的慢速大扭矩。

> **自然语言逻辑**：谐波减速器通过柔性齿轮、刚轮和波发生器实现高减速比，且几乎无背隙；它能把电机的高速低扭矩输出转换为人形机器人关节所需的低速高扭矩，保证动作精确、力量充足，是高性能人形关节的核心传动部件。

## Overview

A harmonic drive reducer consists of three main elements: a wave generator (input), a flexspline (flexible output ring), and a circular spline (fixed ring with internal teeth). The wave generator deforms the flexspline so that its teeth mesh with the circular spline at two opposite regions, producing a high reduction ratio in a very compact envelope. Typical reduction ratios range from 30:1 to 320:1.

Harmonic drives are widely used in precision robotics because they offer near-zero backlash, high torsional stiffness, and high torque capacity relative to their weight and volume. These properties make them attractive for humanoid robot joints that require accurate position and force control. However, they also introduce nonlinear friction, stiffness, and efficiency characteristics that affect dynamic performance and power consumption.

## Key Characteristics

- High single-stage reduction ratios (30:1 to 320:1)
- Near-zero backlash and high positioning accuracy
- High torque-to-weight ratio
- Nonlinear friction and stiffness behavior
- Sensitivity to shock loads and thermal expansion

## Relevance to Humanoid Robotics

Harmonic drive reducers are a core transmission technology in high-performance humanoid joints. Their compact form factor helps achieve human-like limb proportions while delivering the high torque needed for dynamic locomotion and manipulation. Understanding their asymmetric acceleration and braking behavior—as noted in power-consumption studies of the Unitree G1 arm—is important for accurate actuator modeling and control.
