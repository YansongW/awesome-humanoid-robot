---
$id: ent_paper_avery_shape_sensing_of_variable_stif_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Shape Sensing of Variable Stiffness Soft Robots using Electrical Impedance Tomography
  zh: 基于电阻抗断层扫描的变刚度软体机器人形状感知
  ko: 전기 임피던스 단층촬영법을 이용한 가변 강성 소프트 로봇의 형상 감지
summary:
  en: This paper presents a proprioceptive soft actuator that uses conductive saline
    as both the actuation fluid and the sensing medium, enabling shape reconstruction
    via Electrical Impedance Tomography (EIT) with a custom Frequency Division Multiplexed
    (FDM) system.
  zh: 该论文提出了一种本体感知软体执行器，使用导电盐水同时作为驱动流体和传感介质，通过定制的频分复用电阻抗断层扫描（FDM-EIT）系统实现形状重建。
  ko: 본 논문은 전도성 식염수를 구동 유체와 센싱 매질로 동시에 사용하는 본체감각형 소프트 액추에이터를 제안하며, 맞춤형 주파수 분할 다중화
    전기 임피던스 단층촬영(FDM-EIT) 시스템을 통해 형상 재구성을 수행한다.
domains:
- 02_components
- 03_manufacturing_processes
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- process
tags:
- soft_robotics
- shape_sensing
- electrical_impedance_tomography
- eit
- frequency_division_multiplexing
- fdm_eit
- conductive_fluid
- proprioception
- variable_stiffness
- soft_actuator
- laser_welding
- compliant_joints
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the arXiv full text and metadata; factual claims are sourced
    to the paper, but human review is required before full verification.
sources:
- id: src_001
  type: paper
  title: Shape Sensing of Variable Stiffness Soft Robots using Electrical Impedance
    Tomography
  url: https://arxiv.org/abs/1904.02429
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## Overview

Soft robotic systems offer benefits over traditional rigid systems through reduced contact trauma with soft tissues and by enabling access through tortuous paths in minimally invasive surgery. However, the inherent deformability of soft robots places both a greater onus on accurate modelling of their shape and greater challenges in realising intraoperative shape sensing. To address this, the authors present a proprioceptive soft actuator that contains an electrically conductive working fluid, allowing Electrical Impedance Tomography (EIT) to reconstruct shape changes from impedance measurements.

The paper develops a new Frequency Division Multiplexed (FDM) EIT system capable of measurements with 66 dB signal-to-noise ratio and 20 ms temporal resolution. The approach is demonstrated on two two-degree-of-freedom designs: a hydraulic hinged actuator and a pneumatic finger actuator with hydraulic beams. Both designs show that impedance measurements can infer shape changes, with EIT reconstructions producing distinct patterns for each degree of freedom. A robotically guided laser-welding process is used to rapidly integrate electrodes and fluidic channels into triple-laminate PE/PET/PE films, yielding a low-profile, adaptable manufacturing route for soft fluidic devices.

The reported measurements show high repeatability, although some mechanical hysteresis is observed during pressurisation cycles. The authors argue that FDM-EIT has potential as a low-cost, low-profile shape-sensing technique for soft robots.

## Key Contributions

- Developed a new FDM-EIT system achieving 66 dB SNR and 20 ms temporal resolution.
- Demonstrated proprioceptive soft actuators using conductive saline as both actuation fluid and sensing medium.
- Integrated EIT electrodes into laser-welded soft fluidic actuators via a rapid, adaptable manufacturing process guided by a UR5 robotic arm.
- Validated decoupled shape sensing in two 2-DOF designs: a hydraulic hinged actuator and a pneumatic finger actuator with hydraulic beams.
- Showed high repeatability and distinct EIT patterns corresponding to individual degrees of freedom.

## Relevance to Humanoid Robotics

Although the demonstrations focus on minimally invasive surgical soft robots, the underlying technologies are transferable to humanoid robotics. The proprioceptive conductive-fluid sensing approach can be adapted to soft actuators, compliant joints, and continuum manipulators where accurate, low-profile shape sensing is needed. The rapid laser-welded manufacturing process also provides a scalable route for embedding sensors and fluidic channels in soft structural components, which is relevant to humanoid designs that incorporate soft materials for safe human interaction.
