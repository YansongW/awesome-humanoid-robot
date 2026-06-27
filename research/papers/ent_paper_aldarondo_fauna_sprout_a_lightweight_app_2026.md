---
$id: ent_paper_aldarondo_fauna_sprout_a_lightweight_app_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Fauna Sprout: A lightweight, approachable, developer-ready humanoid robot'
  zh: Fauna Sprout：一种轻量、易用、面向开发者的人形机器人
  ko: 'Fauna Sprout: 가벼운 접근성 높은 개발자용 휴머노이드 로봇'
summary:
  en: This paper introduces Sprout, a 1.07 m, 22.7 kg developer-ready humanoid robot
    platform from Fauna Robotics, designed for safe, expressive, long-term deployment
    in human environments through compliant hardware, a modular ROS 2 stack, VR teleoperation,
    dense SLAM, and expressive human-robot interaction.
  zh: 本文介绍了Fauna Robotics公司的Sprout人形机器人平台，身高1.07米、体重22.7千克，面向开发者设计，通过柔顺硬件、模块化ROS 2软件栈、VR遥操作、稠密SLAM以及富有表现力的人机交互，实现安全、富有表现力且可长期部署于人类环境的目标。
  ko: 본 논문은 Fauna Robotics의 개발자용 휴머노이드 로봇 플랫폼인 Sprout을 소개한다. 키 1.07m, 무게 22.7kg로,
    순응형 하드웨어, 모듈형 ROS 2 소프트웨어 스택, VR 텔레오퍼레이션, 밀집 SLAM, 표현력 높은 인간-로봇 상호작용을 통해 인간 환경에서
    안전하고 표현력 있으며 장기적인 배치를 목표로 한다.
domains:
- 06_design_engineering
- 05_mass_production
- 08_software_middleware
- 11_applications_markets
layers:
- intelligence
- midstream
- validation_markets
functional_roles:
- system
- knowledge
- intelligence
tags:
- humanoid_robot
- sprout
- fauna_robotics
- developer_platform
- whole_body_control
- vr_teleoperation
- dense_slam
- human_robot_interaction
- compliant_actuation
- ros_2
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the provided metadata and abstract; full-text verification
    not performed.
sources:
- id: src_001
  type: paper
  title: 'Fauna Sprout: A lightweight, approachable, developer-ready humanoid robot'
  url: https://arxiv.org/abs/2601.18963
  date: '2026'
  accessed_at: '2026-06-27'
theoretical_depth:
- system
---

## Overview

Sprout is a 1.07 m, 22.7 kg humanoid robot platform developed by Fauna Robotics as a lightweight, approachable, and developer-ready system for safe, long-term operation in human environments. The hardware emphasizes compliance and safety through limited joint torques, backdrivable motors, soft deformable exterior panels, and an independent embedded safety subsystem. Onboard sensing includes a ZED2i RGB-D stereo camera, VL53L8CX time-of-flight sensors, a 9-axis IMU, and a 4-channel MEMS microphone array, all centered around an NVIDIA Jetson AGX Orin 64GB compute stack and Molicel P50B Li-ion battery cells.

The software stack is modular and built on ROS 2, using containerized services with stable APIs for low-level control, whole-body reinforcement-learning controllers, and teleoperation/autonomy integration. The platform supports a Meta Quest VR teleoperation application with isomorphic retargeting and DAgger-style intervention data collection, a volumetric mapping SLAM pipeline based on TSDF maplets and GTSAM pose-graph optimization, and an expressive human-robot interaction subsystem using LEDs, eyebrows, head motion, and audio controlled via a hierarchical slot-based behavior graph.

## Key Contributions

- Lightweight humanoid hardware (1.07 m, 22.7 kg) with soft exterior, compliant actuation, limited joint torques, and an independent embedded safety subsystem for operation near people.
- Modular ROS 2 software stack using containerized services, with stable APIs for low-level control, whole-body RL-based controllers, and teleoperation/autonomy integration.
- Embody VR teleoperation application for Meta Quest with isomorphic retargeting, whole-body control, and DAgger-style intervention data collection.
- Volumetric Mapping SLAM pipeline based on TSDF maplets and GTSAM pose-graph optimization, designed for agile bipedal dynamics and low onboard compute.
- Expressive human-robot interaction subsystem using LEDs, eyebrows, head motion, and audio, controlled through a hierarchical slot-based behavior graph.

## Relevance to Humanoid Robotics

Sprout is directly relevant to humanoid robotics because it is designed as a mass-producible, developer-ready humanoid platform that explicitly targets safe, expressive, and long-term deployment in real human environments. By lowering physical and technical barriers to deployment, it provides a practical basis for developing embodied intelligence in home, lab, and public-space settings. Its integration of whole-body control, manipulation, navigation, teleoperation, and social interaction addresses multiple layers of the humanoid robot industry chain, from hardware design and manufacturing to software middleware and applications.
