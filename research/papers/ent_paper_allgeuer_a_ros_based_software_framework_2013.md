---
$id: ent_paper_allgeuer_a_ros_based_software_framework_2013
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform
  zh: 基于ROS的NimbRo-OP人形开放平台软件框架
  ko: NimbRo-OP 휴머노이드 개방형 플랫폼을 위한 ROS 기반 소프트웨어 프레임워크
summary:
  en: This paper presents a modular ROS-based software framework for the NimbRo-OP humanoid robot, providing hardware abstraction,
    visual perception, motion control, and behavior generation for soccer skills demonstrated at RoboCup 2013.
  zh: 本文介绍了面向NimbRo-OP人形机器人的模块化ROS软件框架，提供硬件抽象、视觉感知、运动控制和行为生成功能，并用于实现2013年RoboCup中展示的基本足球技能。
  ko: 본 논문은 NimbRo-OP 휴머노이드 로봇을 위한 모듈화된 ROS 기반 소프트웨어 프레임워크를 제시하며, 2013년 RoboCup에서 시연된 축구 기술을 구현하기 위한 하드웨어 추상화, 시각 인지, 동작 제어
    및 행위 생성 기능을 제공한다.
domains:
- 08_software_middleware
- 04_assembly_integration_testing
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- system
- tool_equipment
- knowledge
- intelligence
tags:
- ros
- nimbro-op
- humanoid_platform
- software_framework
- hardware_abstraction
- visual_perception
- motion_control
- behavior_generation
- robocup
- soccer_robots
- dynamixel
- rviz
- rqt
- rbdl
- real_time_control
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.11051v1.
sources:
- id: src_001
  type: paper
  title: A ROS-based Software Framework for the NimbRo-OP Humanoid Open Platform
  url: https://arxiv.org/abs/1809.11051
  date: '2013'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
Over the past few years, a number of successful humanoid platforms have been developed, including the Nao and the DARwIn-OP, both of which are used by many research groups for the investigation of bipedal walking, full-body motions, and human-robot interaction. The NimbRo-OP is an open humanoid platform under development by team NimbRo of the University of Bonn. Significantly larger than the two aforementioned humanoids, this platform has the potential to interact with a more human-scale environment. This paper describes a software framework for the NimbRo-OP that is based on the Robot Operating System (ROS) middleware. The software provides functionality for hardware abstraction, visual perception, and behavior generation, and has been used to implement basic soccer skills. These were demonstrated at RoboCup 2013, as part of the winning team of the Humanoid League competition.

## 核心内容
Over the past few years, a number of successful humanoid platforms have been developed, including the Nao and the DARwIn-OP, both of which are used by many research groups for the investigation of bipedal walking, full-body motions, and human-robot interaction. The NimbRo-OP is an open humanoid platform under development by team NimbRo of the University of Bonn. Significantly larger than the two aforementioned humanoids, this platform has the potential to interact with a more human-scale environment. This paper describes a software framework for the NimbRo-OP that is based on the Robot Operating System (ROS) middleware. The software provides functionality for hardware abstraction, visual perception, and behavior generation, and has been used to implement basic soccer skills. These were demonstrated at RoboCup 2013, as part of the winning team of the Humanoid League competition.

## 参考
- http://arxiv.org/abs/1809.11051v1

## Overview
Over the past few years, a number of successful humanoid platforms have been developed, including the Nao and the DARwIn-OP, both of which are used by many research groups for the investigation of bipedal walking, full-body motions, and human-robot interaction. The NimbRo-OP is an open humanoid platform under development by team NimbRo of the University of Bonn. Significantly larger than the two aforementioned humanoids, this platform has the potential to interact with a more human-scale environment. This paper describes a software framework for the NimbRo-OP that is based on the Robot Operating System (ROS) middleware. The software provides functionality for hardware abstraction, visual perception, and behavior generation, and has been used to implement basic soccer skills. These were demonstrated at RoboCup 2013, as part of the winning team of the Humanoid League competition.

## Content
Over the past few years, a number of successful humanoid platforms have been developed, including the Nao and the DARwIn-OP, both of which are used by many research groups for the investigation of bipedal walking, full-body motions, and human-robot interaction. The NimbRo-OP is an open humanoid platform under development by team NimbRo of the University of Bonn. Significantly larger than the two aforementioned humanoids, this platform has the potential to interact with a more human-scale environment. This paper describes a software framework for the NimbRo-OP that is based on the Robot Operating System (ROS) middleware. The software provides functionality for hardware abstraction, visual perception, and behavior generation, and has been used to implement basic soccer skills. These were demonstrated at RoboCup 2013, as part of the winning team of the Humanoid League competition.

## 개요
지난 몇 년 동안 Nao와 DARwIn-OP를 포함한 여러 성공적인 휴머노이드 플랫폼이 개발되었으며, 이 두 플랫폼은 많은 연구 그룹에서 이족 보행, 전신 동작 및 인간-로봇 상호작용 연구에 사용되고 있습니다. NimbRo-OP는 본 대학의 NimbRo 팀이 개발 중인 오픈 휴머노이드 플랫폼입니다. 앞서 언급한 두 휴머노이드보다 훨씬 큰 이 플랫폼은 보다 인간적인 규모의 환경과 상호작용할 수 있는 잠재력을 가지고 있습니다. 본 논문은 Robot Operating System (ROS) 미들웨어를 기반으로 한 NimbRo-OP용 소프트웨어 프레임워크를 설명합니다. 이 소프트웨어는 하드웨어 추상화, 시각적 인식 및 행동 생성을 위한 기능을 제공하며, 기본적인 축구 기술을 구현하는 데 사용되었습니다. 이러한 기술은 RoboCup 2013에서 휴머노이드 리그 우승 팀의 일환으로 시연되었습니다.

## 핵심 내용
지난 몇 년 동안 Nao와 DARwIn-OP를 포함한 여러 성공적인 휴머노이드 플랫폼이 개발되었으며, 이 두 플랫폼은 많은 연구 그룹에서 이족 보행, 전신 동작 및 인간-로봇 상호작용 연구에 사용되고 있습니다. NimbRo-OP는 본 대학의 NimbRo 팀이 개발 중인 오픈 휴머노이드 플랫폼입니다. 앞서 언급한 두 휴머노이드보다 훨씬 큰 이 플랫폼은 보다 인간적인 규모의 환경과 상호작용할 수 있는 잠재력을 가지고 있습니다. 본 논문은 Robot Operating System (ROS) 미들웨어를 기반으로 한 NimbRo-OP용 소프트웨어 프레임워크를 설명합니다. 이 소프트웨어는 하드웨어 추상화, 시각적 인식 및 행동 생성을 위한 기능을 제공하며, 기본적인 축구 기술을 구현하는 데 사용되었습니다. 이러한 기술은 RoboCup 2013에서 휴머노이드 리그 우승 팀의 일환으로 시연되었습니다.
