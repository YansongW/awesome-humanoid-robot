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
  en: This paper presents a proprioceptive soft actuator that uses conductive saline as both the actuation fluid and the sensing
    medium, enabling shape reconstruction via Electrical Impedance Tomography (EIT) with a custom Frequency Division Multiplexed
    (FDM) system.
  zh: Soft robotic systems offer benefits over traditional rigid systems through reduced contact trauma with soft tissues
    and by enabling access through tortuous paths in minimally invasive surgery. However, the inherent deformability of soft
    robots places both a greater onus on accurate modelling of their shape, and greater challenges in realising intraoperative
    shape sensing. Herein we present a proprioceptive (self-sensing) soft actuator, with an electrically conductive working
    fluid. Electrical impedance measurements from up to six electrodes enabled tomographic reconstructions using Electrical
  ko: 본 논문은 전도성 식염수를 구동 유체와 센싱 매질로 동시에 사용하는 본체감각형 소프트 액추에이터를 제안하며, 맞춤형 주파수 분할 다중화 전기 임피던스 단층촬영(FDM-EIT) 시스템을 통해 형상 재구성을 수행한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1904.02429v2.
sources:
- id: src_001
  type: paper
  title: Shape Sensing of Variable Stiffness Soft Robots using Electrical Impedance Tomography
  url: https://arxiv.org/abs/1904.02429
  date: '2019'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
---

## 概述
Soft robotic systems offer benefits over traditional rigid systems through reduced contact trauma with soft tissues and by enabling access through tortuous paths in minimally invasive surgery. However, the inherent deformability of soft robots places both a greater onus on accurate modelling of their shape, and greater challenges in realising intraoperative shape sensing. Herein we present a proprioceptive (self-sensing) soft actuator, with an electrically conductive working fluid. Electrical impedance measurements from up to six electrodes enabled tomographic reconstructions using Electrical Impedance Tomography (EIT). A new Frequency Division Multiplexed (FDM) EIT system was developed capable of measurements of 66 dB SNR with 20 ms temporal resolution. The concept was examined in two two-degree-of-freedom designs: a hydraulic hinged actuator and a pneumatic finger actuator with hydraulic beams. Both cases demonstrated that impedance measurements could be used to infer shape changes, and EIT images reconstructed during actuation showed distinct patterns with respect to each degree of freedom (DOF). Whilst there was some mechanical hysteresis observed, the repeatability of the measurements and resultant images was high. The results show the potential of FDM-EIT as a low-cost, low profile shape sensor in soft robots.

## 核心内容
Soft robotic systems offer benefits over traditional rigid systems through reduced contact trauma with soft tissues and by enabling access through tortuous paths in minimally invasive surgery. However, the inherent deformability of soft robots places both a greater onus on accurate modelling of their shape, and greater challenges in realising intraoperative shape sensing. Herein we present a proprioceptive (self-sensing) soft actuator, with an electrically conductive working fluid. Electrical impedance measurements from up to six electrodes enabled tomographic reconstructions using Electrical Impedance Tomography (EIT). A new Frequency Division Multiplexed (FDM) EIT system was developed capable of measurements of 66 dB SNR with 20 ms temporal resolution. The concept was examined in two two-degree-of-freedom designs: a hydraulic hinged actuator and a pneumatic finger actuator with hydraulic beams. Both cases demonstrated that impedance measurements could be used to infer shape changes, and EIT images reconstructed during actuation showed distinct patterns with respect to each degree of freedom (DOF). Whilst there was some mechanical hysteresis observed, the repeatability of the measurements and resultant images was high. The results show the potential of FDM-EIT as a low-cost, low profile shape sensor in soft robots.

## 参考
- http://arxiv.org/abs/1904.02429v2


