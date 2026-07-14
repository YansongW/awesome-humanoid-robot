---
$id: ent_component_allegro_hand
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: component
names:
  en: Allegro Hand
  zh: Allegro 灵巧手
  ko: Allegro Hand
summary:
  en: A commercial 16-DOF four-fingered dexterous robotic hand produced by Wonik Robotics,
    widely used in manipulation research for its torque-controlled joints and ROS
    compatibility.
  zh: 由 Wonik Robotics 生产的商用16自由度四指灵巧机器人手，因扭矩控制关节和 ROS 兼容性而广泛用于操作研究。
  ko: Wonik Robotics가 생산하는 상용 16자유도 4지 민첩한 로봇 손으로, 토크 제어 관절과 ROS 호환성 때문에 조작 연구에 널리
    사용됨.
domains:
- 02_components
- 06_design_engineering
- 11_applications_markets
layers:
- upstream
- midstream
functional_roles:
- component
- knowledge
tags:
- allegro_hand
- dexterous_hand
- wonik_robotics
- torque_control
- ros
- commercial
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: Specifications sourced from Wonik Robotics product information and reseller
    listings.
sources:
- id: src_001
  type: website
  title: Allegro Hand Official Website
  url: https://www.allegrohand.com/
  date: '2026'
  accessed_at: '2026-06-22'
- id: src_002
  type: paper
  title: 'RUKA: Rethinking the Design of Humanoid Hands with Learning'
  url: https://arxiv.org/abs/2504.13165
  date: '2025'
  accessed_at: '2026-06-22'
theoretical_depth:
- system
---

# Allegro Hand

## 抽象

> **生活实例**：它就像一位钢琴家的机械替身——每只手指都有独立的扭矩控制，能细腻地按键、捏取或旋转物体，并且能被常见的机器人软件直接调用。

> **自然语言逻辑**：Allegro Hand 是 Wonik Robotics 生产的商用四指灵巧手，拥有 16 个扭矩控制关节；它广泛用于机器人学习与遥操作研究，作为基准硬件帮助研究者比较不同算法和手设计的性能。

## Overview

The Allegro Hand is a commercially available dexterous robotic hand manufactured by Wonik Robotics (South Korea). It features four fingers with 16 independently torque-controlled joints (4 DoF per finger), enabling a wide range of grasp types and in-hand manipulation strategies. The hand is widely used in academic and industrial manipulation research because it is compact, lightweight, and well supported by ROS-based software.

The V4 version weighs approximately 1.1 kg and supports real-time CAN communication at high control frequencies. Optional tactile fingertip sensors are available through third-party add-ons. Newer variants such as the Allegro Hand V5 and V5 Sense introduce tactile sensing and alternative finger configurations.

## Key Characteristics

- 16 active degrees of freedom (4 per finger)
- Four-finger anthropomorphic design
- Torque-controlled DC motor joints
- Real-time CAN control interface
- ROS/ROS2 compatibility
- Weight: approximately 1.1 kg
- Optional tactile sensor add-ons

## Relevance to Humanoid Robotics

The Allegro Hand is one of the most common commercial dexterous hands in robot learning and teleoperation research. It serves as a benchmark for comparing new hand designs and control algorithms. Its commercial availability and software ecosystem make it a practical reference for humanoid end-effector selection.
