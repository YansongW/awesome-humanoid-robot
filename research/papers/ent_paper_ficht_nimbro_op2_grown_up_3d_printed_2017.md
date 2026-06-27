---
$id: ent_paper_ficht_nimbro_op2_grown_up_3d_printed_2017
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research'
  zh: NimbRo-OP2：面向研究的3D打印开源成人尺寸人形机器人平台
  ko: 'NimbRo-OP2: 연구를 위한 3D 프린팅 오픈 성인 크기 휴머노이드 플랫폼'
summary:
  en: This paper introduces NimbRo-OP2, an affordable, fully open-source, 3D-printed
    adult-sized humanoid robot platform that stands approximately 135 cm tall and
    weighs 18 kg, and describes the mechanical design, electronics, and ROS-based
    software that enabled it to win the RoboCup 2017 Humanoid League AdultSize Soccer
    competition and Technical Challenge.
  zh: 本文介绍了NimbRo-OP2，一款经济实惠、完全开源、3D打印的成人尺寸人形机器人平台，高约135厘米、重18公斤，并描述了使其赢得2017年RoboCup人形组成人尺寸足球比赛和技术挑战的机械设计、电子系统及基于ROS的软件。
  ko: 본 논문은 약 135cm 키와 18kg 무게의 저렴하고 완전히 오픈소스인 3D 프린팅 성인 크기 휴머노이드 로봇 플랫폼인 NimbRo-OP2를
    소개하고, RoboCup 2017 Humanoid League AdultSize 축구 경기 및 기술 과제에서 우승하게 한 기계적 설계, 전자
    시스템 및 ROS 기반 소프트웨어를 설명한다.
domains:
- 06_design_engineering
- 03_manufacturing_processes
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- system
- process
tags:
- nimbro_op2
- humanoid_robot
- adult_size
- open_source_hardware
- open_source_software
- 3d_printing
- selective_laser_sintering
- polyamide_12
- parallel_kinematics
- ros
- dynamixel_mx_106r
- robocup
- lightweight_design
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; full paper text was not
    reviewed. Requires human verification before acceptance.
sources:
- id: src_001
  type: paper
  title: 'NimbRo-OP2: Grown-up 3D Printed Open Humanoid Platform for Research'
  url: https://arxiv.org/abs/1809.11144
  date: '2017'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---



## Overview

NimbRo-OP2 is presented as an affordable, adult-sized humanoid robot platform intended to address the limitations of existing research platforms. Many smaller humanoid platforms require miniaturized environments and do not capture the physical effects experienced by full-size robots, while larger platforms are often costly, closed-source, and difficult to maintain. NimbRo-OP2 aims to bridge this gap by offering a fully open-source design—both hardware and software—that is lightweight, safe to operate without a gantry, and sized for human environments at approximately 135 cm tall and 18 kg.

The mechanical design relies on selective laser sintering of Polyamide 12 (PA12) to produce a lightweight, visually integrated exoskeleton. The leg mechanism uses parallel kinematics driven by unified Robotis Dynamixel MX-106R actuators with external gearing to achieve sufficient torque while keeping the design simple and maintainable. Electronics include an Intel NUC NUC7I7BNH with a Core i7-7567U processor, a CM740 microcontroller board based on an STM32F103RE, an L3G4200D gyroscope, an LIS331DLH accelerometer, and a Logitech C905 camera with a wide-angle 150° lens. Power distribution and safety features include an igus PRT slewing ring bearing, igus axial thrust bearings, and a BTS555 smart high-side power switch.

The software stack is built on the Robot Operating System (ROS) and incorporates vision processing, orientation feedback, feed-forward control, and gait generation modules developed by the AIS Group. The authors report that NimbRo-OP2 competed at RoboCup 2017 in Nagoya, Japan, where it won the Humanoid League AdultSize Soccer competition and the Technical Challenge, demonstrating the integrated hardware-software design in a competitive real-world setting.

## Key Contributions

- An affordable, 3D-printed adult-sized humanoid robot platform with open hardware and open software, lowering barriers to research on full-size systems.
- A lightweight exoskeleton manufactured using selective laser sintering of Polyamide 12 (PA12), combining structural rigidity with reduced mass.
- A parallel kinematics leg design based on commercial off-the-shelf Robotis Dynamixel MX-106R actuators and external gearing to simplify maintenance and sourcing.
- An open-source ROS-based software framework integrating vision, inertial orientation feedback, feed-forward control, and gait generation.
- Demonstrated competitive performance by winning the RoboCup 2017 Humanoid League AdultSize Soccer competition and Technical Challenge.

## Relevance to Humanoid Robotics

NimbRo-OP2 is directly relevant to humanoid robotics because it provides a practical, reproducible pathway to building and experimenting with adult-sized humanoid systems. By releasing both hardware designs and software under an open-source model and using 3D-printed polymer structures, the work reduces cost and fabrication complexity, which are key obstacles to broader adoption and iterative development of humanoid robots.

The platform also illustrates how design engineering and manufacturing process choices—particularly selective laser sintering and the use of standardized COTS actuators—can influence the scalability, maintainability, and accessibility of humanoid hardware. Its application to RoboCup soccer further validates the design in a dynamic, human-scale task domain, making the paper relevant to researchers and engineers focused on affordable, open humanoid systems.
