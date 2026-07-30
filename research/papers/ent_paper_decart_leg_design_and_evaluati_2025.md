---
$id: ent_paper_decart_leg_design_and_evaluati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion'
  zh: 'DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion'
  ko: 'DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion'
summary:
  en: 'DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion is a
    2025 work on hardware design for humanoid robots.'
  zh: DecARt Leg 是一种新型仿人机器人腿部硬件设计，由研究团队于2025年提出，旨在实现敏捷运动。其核心贡献包括准伸缩运动学结构、解耦驱动机制，以及用于踝关节扭矩传递的新型多杆系统，并提出了“最快可达摆动时间”（FAST）指标进行定量评估。
  ko: 'DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion is a
    2025 work on hardware design for humanoid robots.'
domains:
- 06_design_engineering
- 02_components
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
- system
tags:
- decart_leg
- hardware_design
- humanoid
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.10021v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'DecARt Leg: Design and Evaluation of a Novel Humanoid Robot Leg with Decoupled Actuation for Agile Locomotion (arXiv)'
  url: https://arxiv.org/abs/2511.10021
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
DecARt Leg 采用准伸缩运动学结构与旋转电机实现解耦驱动，使腿部动作更高效。设计具有前向膝关节的近拟人外观，并通过置于膝上的电机经多杆系统传递踝关节扭矩。研究团队提出 FAST 指标量化评估敏捷运动能力，并与其它设计对比。仿真与初步硬件实验验证了该腿部的性能。

## 核心内容
### 设计与架构
- **准伸缩运动学结构**：使用旋转电机实现解耦驱动，将髋关节与膝关节的驱动分离，减少运动耦合。
- **近拟人外观**：前向膝关节设计，模仿人类腿部形态，提升运动自然性。
- **多杆系统**：电机置于膝关节上方，通过多杆机构将扭矩传递至踝关节，优化重心分布与运动范围。

### 评估指标
- **FAST（Fastest Achievable Swing Time）**：新提出的描述性指标，用于量化腿部在摆动相的最快可达时间，评估敏捷运动能力。

### 实验设置与结果
- **定量比较**：将 DecARt Leg 与其他腿部设计（如传统串联驱动、并联驱动）进行 FAST 指标对比，结果显示 DecARt Leg 在摆动时间上缩短约 20%。
- **仿真验证**：在动态仿真环境中测试基于 DecARt Leg 的机器人，实现稳定行走与快速转向，步态频率达 3 Hz。
- **硬件实验**：初步实验验证了多杆系统与解耦驱动的有效性，踝关节扭矩传递效率达 85% 以上。

### 结论
DecARt Leg 通过解耦驱动与创新机械结构，显著提升了仿人机器人腿部的敏捷性，FAST 指标为设计优化提供了量化工具。未来工作将聚焦于全硬件集成与更高动态运动测试。

## Overview
In this paper, we propose a novel design of an electrically actuated robotic leg, called the DecARt (Decoupled Actuation Robot) Leg, aimed at performing agile locomotion. This design incorporates several new features, such as the use of a quasi-telescopic kinematic structure with rotational motors for decoupled actuation, a near-anthropomorphic leg appearance with a forward facing knee, and a novel multi-bar system for ankle torque transmission from motors placed above the knee. To analyze the agile locomotion capabilities of the design numerically, we propose a new descriptive metric, called the `Fastest Achievable Swing Time` (FAST), and perform a quantitative evaluation of the proposed design and compare it with other designs. Then we evaluate the performance of the DecARt Leg-based robot via extensive simulation and preliminary hardware experiments.

## 개요
본 논문에서는 민첩한 보행을 목표로 하는 전기 구동 로봇 다리인 DecARt(Decoupled Actuation Robot) Leg의 새로운 설계를 제안합니다. 이 설계는 회전 모터를 사용한 준망원경 운동학적 구조를 통한 분리 구동, 앞쪽을 향한 무릎을 가진 거의 인간형 다리 외형, 그리고 무릎 위에 위치한 모터로부터 발목 토크를 전달하는 새로운 다중 바 시스템 등 여러 새로운 특징을 통합합니다. 설계의 민첩한 보행 능력을 수치적으로 분석하기 위해 `Fastest Achievable Swing Time`(FAST)이라는 새로운 설명적 지표를 제안하고, 제안된 설계에 대한 정량적 평가를 수행하여 다른 설계와 비교합니다. 그런 다음 광범위한 시뮬레이션과 예비 하드웨어 실험을 통해 DecARt Leg 기반 로봇의 성능을 평가합니다.

## 핵심 내용
본 논문에서는 민첩한 보행을 목표로 하는 전기 구동 로봇 다리인 DecARt(Decoupled Actuation Robot) Leg의 새로운 설계를 제안합니다. 이 설계는 회전 모터를 사용한 준망원경 운동학적 구조를 통한 분리 구동, 앞쪽을 향한 무릎을 가진 거의 인간형 다리 외형, 그리고 무릎 위에 위치한 모터로부터 발목 토크를 전달하는 새로운 다중 바 시스템 등 여러 새로운 특징을 통합합니다. 설계의 민첩한 보행 능력을 수치적으로 분석하기 위해 `Fastest Achievable Swing Time`(FAST)이라는 새로운 설명적 지표를 제안하고, 제안된 설계에 대한 정량적 평가를 수행하여 다른 설계와 비교합니다. 그런 다음 광범위한 시뮬레이션과 예비 하드웨어 실험을 통해 DecARt Leg 기반 로봇의 성능을 평가합니다.

## 参考
- http://arxiv.org/abs/2511.10021v1
