---
$id: ent_paper_jafarzadeh_a_wearable_sensor_vest_for_soc_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A wearable sensor vest for social humanoid robots with GPGPU, IoT, and modular software architecture
  zh: 面向社交人形机器人的可穿戴传感器背心：集成GPGPU、物联网与模块化软件架构
  ko: GPGPU, IoT 및 모듈형 소프트웨어 아키텍처를 갖춘 사회적 휴머노이드 로봇용 웨어러블 센서 조끼
summary:
  en: This paper presents an affordable wearable sensor vest and a modular ROS-based open-source software architecture with
    IoT connectivity for social humanoid robots, supporting touch, temperature, gesture, distance, and vision sensing alongside
    local and remote human-robot interaction.
  zh: 本文提出了一种低成本的可穿戴传感器背心及模块化ROS开源软件架构，集成物联网连接，使社交人形机器人能够进行触觉、温度、手势、距离和视觉感知，并支持本地及远程人机交互。
  ko: 본 논문은 사회적 휴머노이드 로봇을 위한 저렴한 웨어러블 센서 조끼와 IoT 연결을 갖춘 모듈형 ROS 기반 오픈소스 소프트웨어 아키텍처를 제안하며, 촉각, 온도, 제스처, 거리 및 시각 센싱과 로컬 및 원격
    인간-로봇 상호작용을 지원한다.
domains:
- 08_software_middleware
- 02_components
layers:
- intelligence
- upstream
functional_roles:
- knowledge
- system
- intelligence
tags:
- wearable_sensor_vest
- social_humanoid_robot
- ros
- iot
- gpgpu
- modular_architecture
- i2c_spi_bus_manager
- embedded_vision
- human_robot_interaction
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2201.02192v1.
sources:
- id: src_001
  type: paper
  title: A wearable sensor vest for social humanoid robots with GPGPU, IoT, and modular software architecture
  url: https://arxiv.org/abs/2201.02192
  date: '2021'
  accessed_at: '2026-06-27'
  doi: 10.1016/j.robot.2020.103536
theoretical_depth:
- method
---
## 概述
Currently, most social robots interact with their surroundings and humans through sensors that are integral parts of the robots, which limits the usability of the sensors, human-robot interaction, and interchangeability. A wearable sensor garment that fits many robots is needed in many applications. This article presents an affordable wearable sensor vest, and an open-source software architecture with the Internet of Things (IoT) for social humanoid robots. The vest consists of touch, temperature, gesture, distance, vision sensors, and a wireless communication module. The IoT feature allows the robot to interact with humans locally and over the Internet. The designed architecture works for any social robot that has a general-purpose graphics processing unit (GPGPU), I2C/SPI buses, Internet connection, and the Robotics Operating System (ROS). The modular design of this architecture enables developers to easily add/remove/update complex behaviors. The proposed software architecture provides IoT technology, GPGPU nodes, I2C and SPI bus mangers, audio-visual interaction nodes (speech to text, text to speech, and image understanding), and isolation between behavior nodes and other nodes. The proposed IoT solution consists of related nodes in the robot, a RESTful web service, and user interfaces. We used the HTTP protocol as a means of two-way communication with the social robot over the Internet. Developers can easily edit or add nodes in C, C++, and Python programming languages. Our architecture can be used for designing more sophisticated behaviors for social humanoid robots.

## 核心内容
Currently, most social robots interact with their surroundings and humans through sensors that are integral parts of the robots, which limits the usability of the sensors, human-robot interaction, and interchangeability. A wearable sensor garment that fits many robots is needed in many applications. This article presents an affordable wearable sensor vest, and an open-source software architecture with the Internet of Things (IoT) for social humanoid robots. The vest consists of touch, temperature, gesture, distance, vision sensors, and a wireless communication module. The IoT feature allows the robot to interact with humans locally and over the Internet. The designed architecture works for any social robot that has a general-purpose graphics processing unit (GPGPU), I2C/SPI buses, Internet connection, and the Robotics Operating System (ROS). The modular design of this architecture enables developers to easily add/remove/update complex behaviors. The proposed software architecture provides IoT technology, GPGPU nodes, I2C and SPI bus mangers, audio-visual interaction nodes (speech to text, text to speech, and image understanding), and isolation between behavior nodes and other nodes. The proposed IoT solution consists of related nodes in the robot, a RESTful web service, and user interfaces. We used the HTTP protocol as a means of two-way communication with the social robot over the Internet. Developers can easily edit or add nodes in C, C++, and Python programming languages. Our architecture can be used for designing more sophisticated behaviors for social humanoid robots.

## 参考
- http://arxiv.org/abs/2201.02192v1

