---
$id: ent_paper_allgeuer_child_sized_3d_printed_igus_hu_2015
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Child-sized 3D Printed igus Humanoid Open Platform
  zh: 儿童尺寸3D打印igus人形开放平台
  ko: 어린이 크기의 3D 프린팅 igus 휴머노이드 오픈 플랫폼
summary:
  en: Presents the igus Humanoid Open Platform, a 90 cm child-sized, low-cost, fully
    3D-printed humanoid robot with open-source ROS software, and reports its mechanical/electrical
    design and dynamic-motion demonstrations.
  zh: 介绍了igus人形开放平台，一种90厘米高、低成本、全3D打印的儿童尺寸人形机器人，配备开源ROS软件，并报告了其机电设计与动态运动演示。
  ko: 90cm 높이의 저비용 완전 3D 프린팅 어린이 크기 휴머노이드 로봇인 igus 휴머노이드 오픈 플랫폼을 소개하고, 오픈소스 ROS 소프트웨어와
    기계/전기 설계 및 동적 동작 시연을 보고한다.
domains:
- 06_design_engineering
- 03_manufacturing_processes
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
tags:
- igus_humanoid_open_platform
- 3d_printed_humanoid
- child_sized_robot
- open_source_hardware
- ros
- dynamixel
- fused_angles
- omnidirectional_walking
- robocup
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; full-text verification
    by a human reviewer is required before marking verified.
sources:
- id: src_001
  type: paper
  title: Child-sized 3D Printed igus Humanoid Open Platform
  url: https://arxiv.org/abs/1809.10701
  date: '2015'
  accessed_at: '2026-06-28'
theoretical_depth:
- system
- method
---

## Overview

The igus Humanoid Open Platform is introduced as a 90 cm child-sized humanoid robot intended to fill the gap between small, inexpensive platforms and large, costly research systems. Its structure is fully 3D-printed from Polyamide 12 (PA12), producing a lightweight exoskeleton that is both load-bearing and visually appealing. The mechanical and electrical designs are modular, relying on Robotis Dynamixel MX-64 and MX-106 servos, an igus axial-thrust-bearing hip yaw joint, a Gigabyte Brix onboard PC with an Intel Core i7-5500U CPU, a Logitech C905 camera, and an inertial/magnetic sensor suite. A 4-cell LiPo battery powers the system, although operating time is reported as only 15–30 minutes.

The corresponding software is built on the Robot Operating System (ROS) and includes a fused-angle-based state estimator, a keyframe motion editor, and an omnidirectional walking gait adapted for artificial grass. The paper reports demonstrations of dynamic behaviors such as getting up from the ground, kicking, and stable walking on artificial grass, performed at trade fairs and RoboCup competitions. All hardware CAD files and the software have been released open-source to lower the barrier for new research groups.

## Key Contributions

- A 90 cm child-sized open humanoid platform that bridges the gap between small affordable robots and large expensive research platforms.
- An entirely 3D-printed Polyamide 12 exoskeleton that is both load-bearing and aesthetic, enabling rapid customization and lightweight construction.
- Open-source release of print-ready 3D CAD hardware files and ROS software to lower barriers for research groups.
- Integration of compliant servo actuation, fused-angle-based state estimation, a keyframe motion editor, and a grass-adapted omnidirectional walking gait.
- Demonstration of dynamic motions including get-up, kicking, and stable walking on artificial grass at trade fairs and RoboCup competitions.

## Relevance to Humanoid Robotics

The paper is directly relevant to humanoid robot development because it presents a complete, affordable, and reproducible hardware/software reference platform in the child-sized range. By releasing open-source CAD files and ROS code, it reduces the cost and engineering effort required for new groups to enter humanoid robotics research. The platform's use of 3D-printed structural parts, commodity servos, and standard middleware also illustrates how scalable, maintainable humanoid systems can be built without custom metal machining or proprietary software. Its demonstrated dynamic locomotion and manipulation primitives on a human-scale environment make it a practical baseline for further work in balance control, perception, and human-robot interaction.
