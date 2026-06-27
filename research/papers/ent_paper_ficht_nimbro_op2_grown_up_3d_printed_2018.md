---
$id: ent_paper_ficht_nimbro_op2_grown_up_3d_printed_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research'
  zh: NimbRo-OP2：面向研究的成人尺寸3D打印开源人形机器人平台
  ko: 'NimbRo-OP2: 연구를 위한 성인 크기 3D 프린팅 오픈 소스 휴머노이드 플랫폼'
summary:
  en: NimbRo-OP2 is an affordable, open-source adult-sized humanoid robot approximately
    135 cm tall and 18 kg in weight, featuring a 3D-printed PA12 exoskeleton and ROS-based
    software. The paper details its mechanical design, electronics, COTS actuator-based
    actuation with external gearing and parallel kinematics, and validation through
    victories at RoboCup 2017.
  zh: NimbRo-OP2是一款经济实惠、开源的成人尺寸人形机器人，高约135厘米、重约18千克，采用3D打印PA12外骨骼和基于ROS的软件。论文详细介绍了其机械设计、电子系统、基于商用执行器的外部齿轮传动与并联运动学，以及通过2017年RoboCup获胜进行的验证。
  ko: NimbRo-OP2는 약 135cm 높이와 18kg 무게의 저렴하고 오픈 소스인 성인 크기 휴머노이드 로봇으로, 3D 프린팅 PA12 외골격과
    ROS 기반 소프트웨어를 갖추고 있습니다. 본 논문은 기계적 설계, 전자 시스템, 상용 액추에이터 기반 외부 기어링과 병렬 운동학, 그리고
    2017 RoboCup에서의 승리를 통한 검증을 다룹니다.
domains:
- 06_design_engineering
- 03_manufacturing_processes
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- adult_size_humanoid
- 3d_printed_exoskeleton
- open_source_hardware
- open_source_software
- cots_actuators
- parallel_kinematics
- ros_software
- humanoid_soccer
- lightweight_design
- robocup
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    the full paper before verification.
sources:
- id: src_001
  type: paper
  title: 'NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research'
  url: https://arxiv.org/abs/1809.11144
  date: '2018'
  accessed_at: '2026-06-26'
---

## Overview

Humanoid robots offer unique advantages in locomotion, full-body motion, interaction with unmodified human environments, and intuitive human-robot interaction. However, many adult-sized research platforms are expensive, closed-source, difficult to maintain, and hard to modify, while smaller platforms do not fully capture the physical factors that affect larger robots. NimbRo-OP2 addresses this gap as an affordable, fully open-source (hardware and software) adult-sized humanoid robot. It stands approximately 135 cm tall and weighs only 18 kg, enabling operation in human-scale environments without a gantry.

The robot's exoskeleton is manufactured using selective laser sintering (SLS) of Polyamide 12 (PA12), producing a lightweight yet load-bearing structure with optimized wall thickness and ribs. Actuation relies on a single commercial-off-the-shelf (COTS) actuator type, the Robotis Dynamixel MX-106R, combined with external gearing and parallel kinematics to reduce cost, part count, and complexity. The onboard computation uses an Intel NUC NUC7I7BNH with an Intel Core i7-7567U processor, while a Robotis CM740 sub-controller (STM32F103RE) interfaces with the actuators. Power is supplied by a 4-cell LiPo battery (14.8 V, 6.6 Ah).

The paper also describes the open-source ROS-based software stack, which includes modular behavior control, vision processing using a Logitech C905 camera with a 150° wide-angle lens, gait generation, and parallel-kinematics adaptation. The authors validate the platform by reporting victories at the RoboCup 2017 Humanoid League AdultSize Soccer competition and Technical Challenge in Nagoya, Japan.

## Key Contributions

- Introduced NimbRo-OP2, an open-source, 3D-printed adult-sized humanoid robot (~135 cm, ~18 kg) at roughly an order of magnitude lower cost than comparable platforms.
- Developed a lightweight, load-bearing 3D-printed exoskeleton using SLS Polyamide 12 with optimized wall thickness and ribs.
- Used a single COTS actuator type (Robotis Dynamixel MX-106R) combined with external gearing and parallel kinematics to reduce cost and complexity.
- Released open-source ROS-based software with modular behavior control, vision, gait generation, and parallel-kinematics adaptation.
- Validated the platform by winning the RoboCup 2017 Humanoid League AdultSize soccer competition and Technical Challenge.

## Relevance to Humanoid Robotics

NimbRo-OP2 is directly relevant to humanoid-robot development because it demonstrates a practical pathway for producing affordable, adult-sized, open-source humanoid hardware. By leveraging 3D printing and COTS components, the design lowers financial and manufacturing barriers, making human-scale humanoid research accessible to a broader community. Its adult-scale form factor allows researchers to study locomotion, full-body motion, and human-robot interaction in environments intended for humans rather than miniaturized testbeds.

The work also provides a systems-level reference for integrating mechanical design, electronics, actuation, and open-source software in a single humanoid platform. The use of parallel kinematics and external gearing with standardized actuators offers a transferable strategy for simplifying humanoid leg and arm mechanisms, while the disclosed ROS software architecture supports reproducibility and further community development.
