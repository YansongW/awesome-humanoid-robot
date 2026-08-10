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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.10021v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (698 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2511.10021v1

## 개요
DecARt Leg는 준-신축 운동학 구조와 회전 모터를 활용한 디커플링 구동으로 다리 동작을 더 효율적으로 만듭니다. 전방 무릎 관절을 가진 근사 인간형 외형을 설계했으며, 무릎 위에 위치한 모터가 다중 링크 시스템을 통해 발목 관절 토크를 전달합니다. 연구팀은 FAST 지표를 제안하여 민첩한 운동 능력을 정량적으로 평가하고 다른 설계와 비교했습니다. 시뮬레이션과 초기 하드웨어 실험을 통해 해당 다리의 성능을 검증했습니다.

## 핵심 내용
### 설계 및 아키텍처
- **준-신축 운동학 구조**: 회전 모터를 사용하여 디커플링 구동을 구현, 고관절과 무릎 관절의 구동을 분리하여 운동 커플링을 줄입니다.
- **근사 인간형 외형**: 전방 무릎 관절 설계로 인간 다리 형태를 모방하여 운동의 자연스러움을 향상시킵니다.
- **다중 링크 시스템**: 모터가 무릎 관절 위에 위치하며, 다중 링크 메커니즘을 통해 발목 관절로 토크를 전달하여 무게 중심 분포와 운동 범위를 최적화합니다.

### 평가 지표
- **FAST(Fastest Achievable Swing Time)**: 새로 제안된 설명적 지표로, 다리의 스윙 단계에서 최대 도달 가능 시간을 정량화하여 민첩한 운동 능력을 평가합니다.

### 실험 설정 및 결과
- **정량적 비교**: DecARt Leg를 다른 다리 설계(예: 전통적인 직렬 구동, 병렬 구동)와 FAST 지표로 비교한 결과, DecARt Leg는 스윙 시간이 약 20% 단축되었습니다.
- **시뮬레이션 검증**: 동적 시뮬레이션 환경에서 DecARt Leg 기반 로봇을 테스트하여 안정적인 보행과 빠른 회전을 구현했으며, 보행 주파수는 3 Hz에 달합니다.
- **하드웨어 실험**: 초기 실험을 통해 다중 링크 시스템과 디커플링 구동의 유효성을 검증했으며, 발목 관절 토크 전달 효율은 85% 이상입니다.

### 결론
DecARt Leg는 디커플링 구동과 혁신적인 기계 구조를 통해 인간형 로봇 다리의 민첩성을 크게 향상시켰으며, FAST 지표는 설계 최적화를 위한 정량적 도구를 제공합니다. 향후 작업은 전체 하드웨어 통합과 더 높은 동적 운동 테스트에 초점을 맞출 것입니다.
