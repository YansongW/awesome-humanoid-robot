---
$id: ent_paper_kumar_design_and_analysis_of_a_nonli_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Design and Analysis of a Nonlinear Parallel Mechanism Coupling for Dynamic Humanoid Legs
  zh: Design and Analysis of a Nonlinear Parallel Mechanism Coupling for Dynamic Humanoid Legs
  ko: Design and Analysis of a Nonlinear Parallel Mechanism Coupling for Dynamic Humanoid Legs
summary:
  en: Humanoids increasingly demand lightweight leg mechanisms for agile, dynamic, and energy-efficient locomotion. Reducing
    distal inertia through proximal actuation has thus become a common design goal. Yet, compact transmissions that preserve
    torque capability and efficient force transmission remain hard to achieve. This paper presents a novel series-parallel
    leg design combining a knee parallel ...
  zh: 本文提出一种用于动态人形机器人腿部的串联-并联机构设计，将膝关节并联机构、踝关节并联机构与非线性膝-踝耦合相结合，所有驱动器均靠近髋部布置。作者推导了耦合的非线性传动模型，并在仿真与硬件上完成验证。该设计使膝与踝可相互借用驱动能力，在6
    kg的腿部上实现足端0.37 kg的有效反射质量。
  ko: Humanoids increasingly demand lightweight leg mechanisms for agile, dynamic, and energy-efficient locomotion. Reducing
    distal inertia through proximal actuation has thus become a common design goal. Yet, compact transmissions that preserve
    torque capability and efficient force transmission remain hard to achieve. This paper presents a novel series-parallel
    leg design combining a knee parallel ...
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
theoretical_depth:
- system
tags:
- humanoid_leg_design
- parallel_mechanism
- knee_ankle_coupling
- proximal_actuation
- distal_inertia
- nonlinear_transmission
verification:
  status: unverified
  reviewed_by: ai
  reviewed_at: '2026-10-19'
  confidence: medium
  notes: Weekly auto-discovery by scripts/weekly_discovery.py (2026-10-19). Bibliographic metadata from arXiv API (2610.16604);
    zh content drafted by DeepSeek (deepseek-chat) from the abstract. Unverified until human review of the weekly discovery
    PR.
sources:
- id: src_001
  type: paper
  title: arXiv:2610.16604 Design and Analysis of a Nonlinear Parallel Mechanism Coupling for Dynamic Humanoid Legs
  url: https://arxiv.org/abs/2610.16604
  date: '2026-10-12'
  accessed_at: '2026-10-19'
---

## 概述

针对人形机器人对轻量化、高动态与高能效腿部的需求，本文通过近端驱动降低远端惯量，但紧凑传动下如何保持力矩能力与高效力传递仍是难点。作者提出一种串联-并联腿部构型，包含膝关节并联机构、踝关节并联机构以及非线性膝-踝耦合，全部驱动器布置在靠近髋部的位置。耦合的作用具有被动自适应特性：膝屈曲时辅助踝背屈以利于抬脚离地，膝伸展时辅助踝跖屈以利于蹬地推进，并通过膝部传动重新分配踝部负载。作者建立了该耦合的非线性传动模型，并在仿真和硬件上进行了验证。结果表明，共享传动使两个关节能够互相利用对方的驱动能力，降低膝部在负载下的峰值力矩需求以及踝部在快速运动中的峰值速度需求；配合近端驱动布置，6 kg的腿部在足端获得0.37 kg的有效反射质量。

## 核心内容

### 问题背景
人形机器人对敏捷、动态且高能效的运动需求日益增长，轻量化腿部机构成为关键设计目标。常见思路是将驱动器布置在近端以降低远端惯量，但在紧凑空间内同时保持力矩能力与高效力传递的传动方案仍然难以实现。

### 方法
- 提出一种新型串联-并联腿部设计，由三部分构成：膝关节并联机构、踝关节并联机构，以及连接两者的非线性膝-踝耦合。
- 所有驱动器均布置在靠近髋部的位置，以降低远端质量与惯量。
- 耦合具有被动辅助特性：膝关节屈曲时，耦合被动辅助踝关节背屈，有利于抬脚离地；膝关节伸展时，耦合辅助踝关节跖屈，有利于蹬地推进。
- 该共享传动通过膝部传动重新分配踝关节负载，使两个关节能够互相借用对方的驱动能力。
- 作者推导了耦合的非线性传动模型。

### 实验设置
- 通过仿真与硬件两种方式对非线性传动模型进行验证。

### 关键结果
- 共享传动降低了膝关节在负载下的峰值力矩需求。
- 共享传动降低了踝关节在快速运动中的峰值速度需求。
- 配合近端驱动布置，6 kg的腿部在足端实现0.37 kg的有效反射质量，表明远端腿部惯量很低。

### 结论
该设计说明，非线性膝-踝耦合与近端驱动相结合，可在保持力矩与速度能力的同时显著降低远端惯量，适用于动态人形机器人腿部。

## Overview

Humanoids increasingly demand lightweight leg mechanisms for agile, dynamic, and energy-efficient locomotion. Reducing distal inertia through proximal actuation has thus become a common design goal. Yet, compact transmissions that preserve torque capability and efficient force transmission remain hard to achieve. This paper presents a novel series-parallel leg design combining a knee parallel mechanism, an ankle parallel mechanism, and a nonlinear knee-ankle coupling where all actuators placed closer to the hip. As the knee flexes, the coupling passively assists ankle dorsiflexion for foot clearance and, as it extends it assists plantarflexion for push-off, redistributing ankle load through the knee transmission. We derive the coupling's nonlinear transmission models and validate them in simulation and on hardware. The design shows that the shared transmission lets both joints draw on each other's actuator capacity by easing the knee's peak torque demand under load and the ankle's peak speed demand during fast motion. %Together With the leg's proximal actuator placement, the leg achieves an effective reflected mass of 0.37kg at the foot for a 6kg leg, demonstrating very low distal leg inertia for dynamic humanoid robots.

## 参考
- https://arxiv.org/abs/2610.16604
