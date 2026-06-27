---
$id: ent_paper_stolzle_guiding_soft_robots_with_motor_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Guiding Soft Robots with Motor-Imagery Brain Signals and Impedance Control
  zh: 基于运动想象脑信号与阻抗控制的软体机器人导引
  ko: 운동 상상 뇌신호 및 임피던스 제어를 이용한 소프트 로봇 유도
summary:
  en: This paper presents a pipeline that uses a 3-channel wearable EEG motor-imagery
    brain-machine interface to steer a virtual Cartesian attractor for a planar Handed
    Shearing Auxetic soft robot, tracked by a novel Cartesian impedance controller;
    it reports preliminary quantitative setpoint-regulation results and a real-world
    activities-of-daily-living demonstration.
  zh: 本文提出了一种利用三通道可穿戴脑电图运动想象脑机接口，为平面手性剪切拉胀软体机器人驱动虚拟笛卡尔吸引子，并通过新型笛卡尔阻抗控制器进行跟踪的流程；报告了初步的定量设定点调节结果和一项日常生活活动演示。
  ko: 본 논문은 3채널 웨어러블 EEG 운동 상상 뇌-기계 인터페이스를 사용하여 평면 Handed Shearing Auxetic 소프트 로봇의
    가상 데카르트 어트랙터를 조향하고, 새로운 데카르트 임피던스 제어기로 추적하는 파이프라인을 제안하며, 예비적인 정량적 설정점 조절 결과와 실제
    일상생활 활동 시연을 보고한다.
domains:
- 08_software_middleware
- 07_ai_models_algorithms
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- brain_machine_interface
- motor_imagery
- eeg
- wearable_eeg
- soft_robotics
- handed_shearing_auxetic
- continuum_robot
- cartesian_impedance_control
- underactuated_control
- human_robot_interaction
- assistive_robotics
- setpoint_regulation
- activities_of_daily_living
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; full-text verification
    and exact source citations are pending human review.
sources:
- id: src_001
  type: paper
  title: Guiding Soft Robots with Motor-Imagery Brain Signals and Impedance Control
  url: https://arxiv.org/abs/2401.13441
  date: '2024'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

The paper addresses the safety risks of using error-prone, low-channel EEG motor-imagery classifiers to control rigid robots near humans. It proposes an alternative that combines wearable EEG with the intrinsic physical compliance of soft robots. The authors introduce an online pipeline in which motor-imagery and jaw-clench brain signals from a three-channel EEG device are decoded and used to move a virtual Cartesian attractor. A model-based Cartesian impedance controller then drives the end effector of a planar Handed Shearing Auxetic (HSA) soft robot toward that attractor, while compensating for the underactuation and non-affine control dynamics typical of continuum soft robots.

The control architecture is tailored specifically to planar HSA robots. It maps desired Cartesian forces to motor commands through a nonlinear least-squares actuation mapping, preserving compliant behavior rather than enforcing rigid trajectory tracking. The authors preliminarily evaluate the system on a setpoint-regulation task and further demonstrate its utility on a real-world activities-of-daily-living task: pressing a hairspray nozzle through brain-controlled soft-robot motion. The control code and the OpenVibe EEG processing pipeline are released as open-source software.

## Key Contributions

- A brain-machine-interface control strategy for continuum soft robots, demonstrated on planar HSA setpoint regulation.
- A Cartesian impedance controller tailored to planar HSA robots that handles underactuation and non-affinity in control while preserving compliance.
- Experimental validation on a real-world activities-of-daily-living task (pressing a hairspray nozzle) using EEG-based motor imagery.
- Open-source release of the control code and the OpenVibe EEG processing pipeline.

## Relevance to Humanoid Robotics

Although the work studies a continuum soft manipulator rather than a bipedal humanoid, it directly develops capabilities that are central to safe assistive humanoid deployment: compliant physical human-robot interaction and intuitive, non-invasive brain-controlled manipulation. The Cartesian impedance-control formulation and the integration of a wearable BCI with an impedance-regulated soft end effector are transferable to humanoid arms and hands, where safety around humans is equally critical. The paper therefore provides a methodological reference for impedance/admittance control and BCI interfacing in humanoid robotics.
