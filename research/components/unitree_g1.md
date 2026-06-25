---
$id: ent_robot_system_unitree_g1
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: robot_system
names:
  en: Unitree G1 Humanoid Robot
  zh: Unitree G1 人形机器人
  ko: Unitree G1 휴머노이드 로봇
summary:
  en: A compact, mass-produced humanoid robot developed by Unitree Robotics, featuring 23–43
    degrees of freedom, a 35 kg body, 2 m/s walking speed, and options for dexterous hands,
    designed for research, education, and light industrial tasks.
  zh: 由宇树科技开发的紧凑型量产人形机器人，具有23–43自由度、35公斤体重、2米/秒步行速度，可选配灵巧手，面向研究、教育和轻工业任务。
  ko: Unitree Robotics가 개발한 컴팩트한 양산형 휴머노이드 로봇으로, 23~43자유도, 35kg 몸체, 2m/s 보행 속도를 갖추며 연구, 교육 및 경량 산업 작업을 위해 설계됨.
domains:
- 02_components
- 06_design_engineering
- 05_mass_production
- 11_applications_markets
layers:
- upstream
- midstream
- validation_markets
functional_roles:
- system
- knowledge
tags:
- unitree
- humanoid_robot
- g1
- low_cost_humanoid
- research_platform
- dexterous_hand
- mass_production
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-22'
  confidence: medium
  notes: Specifications compiled from official Unitree documentation and reseller pages;
    exact configuration depends on G1/G1-EDU variant.
sources:
- id: src_001
  type: website
  title: Unitree G1 Developer Specifications
  url: https://support.unitree.com/home/en/G1_developer
  date: '2026'
  accessed_at: '2026-06-22'
- id: src_002
  type: paper
  title: Identification of a Physics-Based Electrical Power Consumption Model for the
    Unitree G1 Humanoid Arm
  url: https://arxiv.org/abs/2606.15915
  date: '2026'
  accessed_at: '2026-06-22'
---

# Unitree G1 Humanoid Robot

## 生活实例 + 自然语言阐述逻辑

> **生活实例**：它就像人形机器人界的“树莓派”——价格相对亲民、可以批量买到，让研究者和开发者能快速拿到一具完整的人体形态硬件来验证算法。

> **自然语言逻辑**：Unitree G1 是宇树科技推出的一款紧凑型量产人形机器人，基础版 23 自由度、EDU 版可扩展至 43 自由度；它将永磁同步电机、减速器、传感器和可选的 Jetson 计算单元集成在一起，成为 embodied AI 和机器人量产研究的重要参考平台。

## Overview

The Unitree G1 is a commercially available humanoid robot platform developed by Unitree Robotics. It is positioned as an affordable, compact research and development platform for embodied AI, locomotion, and manipulation research. The base G1 model offers 23 degrees of freedom, while the G1-EDU variant can be expanded to 43 DoF with additional wrist and waist joints and optional Dex3-1 three-finger dexterous hands.

Key hardware features include low-inertia internal-rotor PMSM joint motors, industrial-grade crossed-roller bearings, dual encoders on each joint, full hollow electrical routing, and a 9000 mAh quick-release battery providing approximately two hours of operation. The sensing suite combines a depth camera and a 3D LiDAR with an 8-core CPU for onboard computation; EDU variants can integrate an NVIDIA Jetson Orin module.

## Key Specifications

- Height (standing): approximately 1.27–1.32 m
- Weight (with battery): about 35 kg
- Degrees of freedom: 23 (G1) / up to 43 (G1-EDU)
- Walking speed: up to 2 m/s
- Knee joint maximum torque: 90 N·m (G1) / 120 N·m (G1-EDU)
- Arm payload: approximately 2 kg (G1) / 3 kg (G1-EDU)
- Battery: 9000 mAh, approximately 2 h runtime
- Onboard compute: 8-core CPU; optional NVIDIA Jetson Orin on EDU

## Relevance to Humanoid Robotics

The Unitree G1 is significant for the 0-to-1 mass-production roadmap because it represents one of the first low-cost, commercially scalable full-size humanoid robot platforms. Its use in power-modeling research, teleoperation datasets, and learning-based control makes it a common reference system for translating algorithms to real hardware. Understanding its actuator, power, and sensor architecture also informs component-selection and supply-chain decisions for similar humanoid products.
