---
$id: ent_paper_yu_quasi_direct_drive_actuation_f_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Quasi-Direct Drive Actuation for a Lightweight Hip Exoskeleton with High Backdrivability
    and High Bandwidth
  zh: 用于高反驱性和高带宽轻量化髋关节外骨骼的准直驱驱动
  ko: 높은 역구동성 및 높은 대역폭을 가진 경량 고관절 외골격용 준직구동 구동
summary:
  en: This paper presents a custom quasi-direct-drive actuator and a 3.4 kg bilateral
    hip exoskeleton that achieves 17.5 Nm nominal torque, 0.4 Nm backdrive torque,
    62.4 Hz bandwidth, and a simple controller validated during walking and squatting.
  zh: 本文介绍了一种定制准直驱执行器和一个3.4公斤的双侧髋关节外骨骼，实现了17.5牛·米额定扭矩、0.4牛·米反驱扭矩、62.4赫兹带宽，并在行走和蹲起中验证了简单的控制器。
  ko: 본 논문은 맞춤형 준직구동 구동기와 17.5 Nm 정격 토크, 0.4 Nm 역구동 토크, 62.4 Hz 대역폭을 달성하고 보행 및 스쿼팅에서
    간단한 제어기를 검증한 3.4 kg 양측 고관절 외골격을 제시한다.
domains:
- 02_components
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- component
tags:
- quasi_direct_drive
- qdd
- hip_exoskeleton
- wearable_robot
- actuator
- backdrivability
- high_bandwidth
- bldc_motor
- planetary_gearbox
- design_for_control
- lower_limb_assist
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
sources:
- id: src_001
  type: paper
  title: Quasi-Direct Drive Actuation for a Lightweight Hip Exoskeleton with High
    Backdrivability and High Bandwidth
  url: https://arxiv.org/abs/2004.00467
  date: '2020'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## Overview

The paper proposes a custom quasi-direct-drive (QDD) actuator for a lightweight bilateral hip exoskeleton. The actuator combines a high-torque-density exterior-rotor brushless direct-current (BLDC) motor with an 8:1 planetary gearbox, a 14-bit magnetic encoder, and an integrated motor driver/controller, weighing 777 g overall. The authors derive a unified human-robot interaction model to compare conventional actuation, series elastic actuation (SEA), and QDD in terms of torque capability, control bandwidth, backdrivability, and force-tracking accuracy. The resulting exoskeleton has a total mass of 3.4 kg and one active sagittal-plane degree of freedom per hip.

Experiments characterize the actuator under continuous stall conditions and validate torque tracking during able-bodied walking at speeds from 0.8 to 1.4 m/s and during squatting at a 2 s cadence. The reported performance metrics include a nominal torque of 17.5 Nm, a backdrive torque of 0.4 Nm, a control bandwidth of 62.4 Hz, and a root-mean-square torque-tracking error of 1.09 Nm (5.4 % of the desired peak torque). A simple hierarchical controller is shown to be sufficient, supporting the paper's "design for control" argument that careful mechanical design can reduce control complexity while maintaining high performance.

The work situates itself against lower-limb wearable robots that rely on conventional high-ratio geared actuators or series elastic actuators. The authors note that conventional actuation meets torque, speed, and bandwidth requirements but introduces high mechanical impedance, whereas SEAs improve compliance at the cost of bandwidth. The QDD approach is presented as a way to achieve simultaneously high bandwidth, high backdrivability, and compact mass.

## Key Contributions

- Design of a 777 g custom quasi-direct-drive actuator using an exterior-rotor BLDC motor, an 8:1 planetary gearbox, a 14-bit magnetic encoder, and an integrated driver/controller.
- Design and fabrication of a 3.4 kg bilateral hip exoskeleton with one active sagittal-plane degree of freedom per hip.
- Unified human-robot interaction model comparing conventional actuation, series elastic actuation, and quasi-direct drive in terms of backdrivability, bandwidth, and torque capability.
- Model-based benchmark of representative actuators in torque, bandwidth, backdrivability, and force-tracking accuracy.
- Experimental validation of torque tracking during walking (0.8-1.4 m/s) and squatting (2 s cadence) using a simple hierarchical controller.

## Relevance to Humanoid Robotics

The actuator architecture described in this paper is directly transferable to the hip and leg joints of humanoid robots. Its combination of high torque density, low mechanical impedance, high backdrivability, and high control bandwidth addresses the requirements for safe and dynamic physical interaction in mass-produced humanoids. The compact, low-ratio drivetrain can reduce control complexity and improve force fidelity, which is important for balancing, walking, and contact-rich tasks. The design-for-control philosophy also aligns with the need to simplify software stacks in commercial humanoid platforms.
