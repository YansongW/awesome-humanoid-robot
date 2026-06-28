---
$id: ent_paper_shaker_developing_a_robotic_surgery_t_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Developing a Robotic Surgery Training System for Wide Accessibility and Research
  zh: 面向广泛可及性与研究的机器人手术训练系统开发
  ko: 넓은 접근성과 연구를 위한 로봇 수술 훈련 시스템 개발
summary:
  en: This paper presents RoboScope, a low-cost master-slave robotic laparoscopy training
    system that uses a redesigned end-effector, a RoboDK-based digital twin, and optimized
    velocity-control teleoperation with Remote Center of Motion constraints to broaden
    access to surgical training and research.
  zh: 本文提出了RoboScope，一种低成本的主从式机器人腹腔镜训练系统，该系统采用重新设计的末端执行器、基于RoboDK的数字孪生平台以及具有远程运动中心约束的优化速度控制遥操作，以扩大外科手术训练和研究的普及性。
  ko: 본 논문은 재설계된 엔드이펙터, RoboDK 기반 디지털 트윈, 그리고 원격 운동 중심(RCM) 제약이 있는 최적화된 속도 제어 원격 조작을
    사용하여 외과 수술 훈련 및 연구의 접근성을 확대하는 저렴한 마스터-슬레이브 로봇 복강경 훈련 시스템인 RoboScope를 제안한다.
domains:
- 06_design_engineering
- 02_components
- 03_manufacturing_processes
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- system
- tool_equipment
tags:
- teleoperation
- digital_twin
- master_slave_system
- remote_center_of_motion
- low_cost_design
- haptic_interface
- surgical_robotics
- collaborative_robot
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text review required
    before production verification.
sources:
- id: src_001
  type: paper
  title: Developing a Robotic Surgery Training System for Wide Accessibility and Research
  url: https://arxiv.org/abs/2505.20562
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

This paper develops RoboScope, a low-cost master-slave robotic laparoscopy training system intended to make robotic surgery training more accessible for on-site and remote users. The hardware centers on a redesigned low-cost robotic end-effector that mimics high-end laparoscopic instruments, actuated by Dynamixel servos and controlled through an Arduino processor, with force/torque sensing, Sony cameras, a fisheye lens camera, and an Oculus Rift S VR headset for visualization. A RoboDK-based digital twin is built to support simulation, testing, real-time monitoring, and remote operation. Teleoperation is implemented with Jacobian-based velocity control under a spherical-coordinate Remote Center of Motion (RCM) constraint, and the system includes safety checks for singularities, joint limits, and collisions together with continuous RCM-error monitoring.

Experimental evaluation reports an RCM RMSE of 5 µm (with a key-contribution note of 2 µm in one validation condition) and a teleoperation latency of 0.01 seconds. The system demonstrates smooth, continuous motion on standardized trajectories and foam-insertion tasks inside a laparoscopy training box. Usability testing with surgeons, enhanced visual feedback, and richer haptic feedback are left as future work, and the low 125 Hz control frequency of the UR3 CB3 arms is noted as a performance limit.

## Key Contributions

- Low-cost end-effector design mimicking high-end laparoscopic instruments using Design for Manufacturing and Assembly (DFM/DFA) principles.
- RoboDK-based digital twin for offline simulation, online testing, real-time monitoring, and remote operation of the training system.
- Optimized teleoperation control using a spherical-coordinate RCM constraint and Jacobian-based velocity control to maintain safe instrument insertion motion.
- Integration of safety features including singularity, joint-limit, and collision checking plus real-time RCM error monitoring.
- Experimental validation on standardized trajectories and foam-insertion tasks, reporting RCM RMSE in the micrometer range and teleoperation latency of 0.01 seconds.

## Relevance to Humanoid Robotics

Although the immediate application is surgical training, the paper addresses problems directly transferable to humanoid robotics: reducing end-effector cost through DFM/DFA, validating designs in a digital twin before physical integration, and enforcing real-time motion constraints during teleoperation. Humanoid prototyping can adopt the same workflow of low-cost custom end-effectors plus simulation-first validation. The RCM-constrained velocity-control formulation and the safety-monitoring architecture are also relevant to safe humanoid teleoperation and physical human-robot interaction, where joint limits, singularities, and remote-center-like constraints must be respected online.
