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
  en: This paper introduces NimbRo-OP2, an affordable, fully open-source, 3D-printed adult-sized humanoid robot platform that
    stands approximately 135 cm tall and weighs 18 kg, and describes the mechanical design, electronics, and ROS-based software
    that enabled it to win the RoboCup 2017 Humanoid League AdultSize Soccer competition and Technical Challenge.
  zh: 本文介绍了NimbRo-OP2，一款经济实惠、完全开源、3D打印的成人尺寸人形机器人平台，高约135厘米、重18公斤，并描述了使其赢得2017年RoboCup人形组成人尺寸足球比赛和技术挑战的机械设计、电子系统及基于ROS的软件。
  ko: 본 논문은 약 135cm 키와 18kg 무게의 저렴하고 완전히 오픈소스인 3D 프린팅 성인 크기 휴머노이드 로봇 플랫폼인 NimbRo-OP2를 소개하고, RoboCup 2017 Humanoid League AdultSize
    축구 경기 및 기술 과제에서 우승하게 한 기계적 설계, 전자 시스템 및 ROS 기반 소프트웨어를 설명한다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1809.11144v1.
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
## 概述
The versatility of humanoid robots in locomotion, full-body motion, interaction with unmodified human environments, and intuitive human-robot interaction led to increased research interest. Multiple smaller platforms are available for research, but these require a miniaturized environment to interact with---and often the small scale of the robot diminishes the influence of factors which would have affected larger robots. Unfortunately, many research platforms in the larger size range are less affordable, more difficult to operate, maintain and modify, and very often closed-source. In this work, we introduce NimbRo-OP2X, an affordable, fully open-source platform in terms of both hardware and software. Being almost 135cm tall and only 18kg in weight, the robot is not only capable of interacting in an environment meant for humans, but also easy and safe to operate and does not require a gantry when doing so. The exoskeleton of the robot is 3D printed, which produces a lightweight and visually appealing design. We present all mechanical and electrical aspects of the robot, as well as some of the software features of our well-established open-source ROS software. The NimbRo-OP2X performed at RoboCup 2017 in Nagoya, Japan, where it won the Humanoid League AdultSize Soccer competition and Technical Challenge.

## 核心内容
The versatility of humanoid robots in locomotion, full-body motion, interaction with unmodified human environments, and intuitive human-robot interaction led to increased research interest. Multiple smaller platforms are available for research, but these require a miniaturized environment to interact with---and often the small scale of the robot diminishes the influence of factors which would have affected larger robots. Unfortunately, many research platforms in the larger size range are less affordable, more difficult to operate, maintain and modify, and very often closed-source. In this work, we introduce NimbRo-OP2X, an affordable, fully open-source platform in terms of both hardware and software. Being almost 135cm tall and only 18kg in weight, the robot is not only capable of interacting in an environment meant for humans, but also easy and safe to operate and does not require a gantry when doing so. The exoskeleton of the robot is 3D printed, which produces a lightweight and visually appealing design. We present all mechanical and electrical aspects of the robot, as well as some of the software features of our well-established open-source ROS software. The NimbRo-OP2X performed at RoboCup 2017 in Nagoya, Japan, where it won the Humanoid League AdultSize Soccer competition and Technical Challenge.

## 参考
- http://arxiv.org/abs/1809.11144v1

## Overview
The versatility of humanoid robots in locomotion, full-body motion, interaction with unmodified human environments, and intuitive human-robot interaction led to increased research interest. Multiple smaller platforms are available for research, but these require a miniaturized environment to interact with---and often the small scale of the robot diminishes the influence of factors which would have affected larger robots. Unfortunately, many research platforms in the larger size range are less affordable, more difficult to operate, maintain and modify, and very often closed-source. In this work, we introduce NimbRo-OP2X, an affordable, fully open-source platform in terms of both hardware and software. Being almost 135cm tall and only 18kg in weight, the robot is not only capable of interacting in an environment meant for humans, but also easy and safe to operate and does not require a gantry when doing so. The exoskeleton of the robot is 3D printed, which produces a lightweight and visually appealing design. We present all mechanical and electrical aspects of the robot, as well as some of the software features of our well-established open-source ROS software. The NimbRo-OP2X performed at RoboCup 2017 in Nagoya, Japan, where it won the Humanoid League AdultSize Soccer competition and Technical Challenge.

## Content
The versatility of humanoid robots in locomotion, full-body motion, interaction with unmodified human environments, and intuitive human-robot interaction led to increased research interest. Multiple smaller platforms are available for research, but these require a miniaturized environment to interact with---and often the small scale of the robot diminishes the influence of factors which would have affected larger robots. Unfortunately, many research platforms in the larger size range are less affordable, more difficult to operate, maintain and modify, and very often closed-source. In this work, we introduce NimbRo-OP2X, an affordable, fully open-source platform in terms of both hardware and software. Being almost 135cm tall and only 18kg in weight, the robot is not only capable of interacting in an environment meant for humans, but also easy and safe to operate and does not require a gantry when doing so. The exoskeleton of the robot is 3D printed, which produces a lightweight and visually appealing design. We present all mechanical and electrical aspects of the robot, as well as some of the software features of our well-established open-source ROS software. The NimbRo-OP2X performed at RoboCup 2017 in Nagoya, Japan, where it won the Humanoid League AdultSize Soccer competition and Technical Challenge.

## 개요
휴머노이드 로봇의 이동, 전신 동작, 개조되지 않은 인간 환경과의 상호작용, 직관적인 인간-로봇 상호작용에서의 다재다능함은 연구 관심을 증가시켰습니다. 연구를 위해 여러 소형 플랫폼이 제공되지만, 이들은 상호작용을 위해 소형화된 환경이 필요하며, 종종 로봇의 작은 크기로 인해 대형 로봇에 영향을 미칠 요소들의 영향이 감소합니다. 불행히도, 대형 크기 범위의 많은 연구 플랫폼은 가격이 비싸고, 운영, 유지보수 및 수정이 더 어려우며, 대부분 폐쇄 소스입니다. 본 연구에서는 하드웨어와 소프트웨어 모두에서 저렴하고 완전히 오픈소스인 플랫폼 NimbRo-OP2X를 소개합니다. 키가 약 135cm이고 무게가 18kg에 불과한 이 로봇은 인간을 위한 환경에서 상호작용할 수 있을 뿐만 아니라, 운영이 쉽고 안전하며, 이를 위해 갠트리가 필요하지 않습니다. 로봇의 외골격은 3D 프린팅되어 가볍고 시각적으로 매력적인 디자인을 제공합니다. 우리는 로봇의 모든 기계적 및 전기적 측면과 함께 잘 확립된 오픈소스 ROS 소프트웨어의 일부 기능을 제시합니다. NimbRo-OP2X는 일본 나고야에서 열린 RoboCup 2017에서 휴머노이드 리그 어덜트사이즈 축구 대회와 기술 챌린지에서 우승했습니다.

## 핵심 내용
휴머노이드 로봇의 이동, 전신 동작, 개조되지 않은 인간 환경과의 상호작용, 직관적인 인간-로봇 상호작용에서의 다재다능함은 연구 관심을 증가시켰습니다. 연구를 위해 여러 소형 플랫폼이 제공되지만, 이들은 상호작용을 위해 소형화된 환경이 필요하며, 종종 로봇의 작은 크기로 인해 대형 로봇에 영향을 미칠 요소들의 영향이 감소합니다. 불행히도, 대형 크기 범위의 많은 연구 플랫폼은 가격이 비싸고, 운영, 유지보수 및 수정이 더 어려우며, 대부분 폐쇄 소스입니다. 본 연구에서는 하드웨어와 소프트웨어 모두에서 저렴하고 완전히 오픈소스인 플랫폼 NimbRo-OP2X를 소개합니다. 키가 약 135cm이고 무게가 18kg에 불과한 이 로봇은 인간을 위한 환경에서 상호작용할 수 있을 뿐만 아니라, 운영이 쉽고 안전하며, 이를 위해 갠트리가 필요하지 않습니다. 로봇의 외골격은 3D 프린팅되어 가볍고 시각적으로 매력적인 디자인을 제공합니다. 우리는 로봇의 모든 기계적 및 전기적 측면과 함께 잘 확립된 오픈소스 ROS 소프트웨어의 일부 기능을 제시합니다. NimbRo-OP2X는 일본 나고야에서 열린 RoboCup 2017에서 휴머노이드 리그 어덜트사이즈 축구 대회와 기술 챌린지에서 우승했습니다.
