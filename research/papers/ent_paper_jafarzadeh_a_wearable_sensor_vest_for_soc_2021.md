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

## Overview
Currently, most social robots interact with their surroundings and humans through sensors that are integral parts of the robots, which limits the usability of the sensors, human-robot interaction, and interchangeability. A wearable sensor garment that fits many robots is needed in many applications. This article presents an affordable wearable sensor vest, and an open-source software architecture with the Internet of Things (IoT) for social humanoid robots. The vest consists of touch, temperature, gesture, distance, vision sensors, and a wireless communication module. The IoT feature allows the robot to interact with humans locally and over the Internet. The designed architecture works for any social robot that has a general-purpose graphics processing unit (GPGPU), I2C/SPI buses, Internet connection, and the Robotics Operating System (ROS). The modular design of this architecture enables developers to easily add/remove/update complex behaviors. The proposed software architecture provides IoT technology, GPGPU nodes, I2C and SPI bus managers, audio-visual interaction nodes (speech to text, text to speech, and image understanding), and isolation between behavior nodes and other nodes. The proposed IoT solution consists of related nodes in the robot, a RESTful web service, and user interfaces. We used the HTTP protocol as a means of two-way communication with the social robot over the Internet. Developers can easily edit or add nodes in C, C++, and Python programming languages. Our architecture can be used for designing more sophisticated behaviors for social humanoid robots.

## Content
Currently, most social robots interact with their surroundings and humans through sensors that are integral parts of the robots, which limits the usability of the sensors, human-robot interaction, and interchangeability. A wearable sensor garment that fits many robots is needed in many applications. This article presents an affordable wearable sensor vest, and an open-source software architecture with the Internet of Things (IoT) for social humanoid robots. The vest consists of touch, temperature, gesture, distance, vision sensors, and a wireless communication module. The IoT feature allows the robot to interact with humans locally and over the Internet. The designed architecture works for any social robot that has a general-purpose graphics processing unit (GPGPU), I2C/SPI buses, Internet connection, and the Robotics Operating System (ROS). The modular design of this architecture enables developers to easily add/remove/update complex behaviors. The proposed software architecture provides IoT technology, GPGPU nodes, I2C and SPI bus managers, audio-visual interaction nodes (speech to text, text to speech, and image understanding), and isolation between behavior nodes and other nodes. The proposed IoT solution consists of related nodes in the robot, a RESTful web service, and user interfaces. We used the HTTP protocol as a means of two-way communication with the social robot over the Internet. Developers can easily edit or add nodes in C, C++, and Python programming languages. Our architecture can be used for designing more sophisticated behaviors for social humanoid robots.

## 개요
현재 대부분의 소셜 로봇은 로봇의 일부인 센서를 통해 주변 환경 및 인간과 상호작용하며, 이는 센서의 활용성, 인간-로봇 상호작용 및 호환성을 제한합니다. 다양한 로봇에 적용 가능한 웨어러블 센서 의류가 많은 응용 분야에서 필요합니다. 본 논문은 저렴한 웨어러블 센서 조끼와 사물인터넷(IoT)을 활용한 오픈소스 소프트웨어 아키텍처를 소셜 휴머노이드 로봇용으로 제시합니다. 조끼는 터치, 온도, 제스처, 거리, 비전 센서 및 무선 통신 모듈로 구성됩니다. IoT 기능을 통해 로봇은 로컬 및 인터넷을 통해 인간과 상호작용할 수 있습니다. 설계된 아키텍처는 GPGPU(범용 그래픽 처리 장치), I2C/SPI 버스, 인터넷 연결 및 ROS(로봇 운영 체제)를 갖춘 모든 소셜 로봇에서 작동합니다. 이 아키텍처의 모듈식 설계는 개발자가 복잡한 동작을 쉽게 추가/제거/업데이트할 수 있도록 합니다. 제안된 소프트웨어 아키텍처는 IoT 기술, GPGPU 노드, I2C 및 SPI 버스 관리자, 시청각 상호작용 노드(음성-텍스트, 텍스트-음성, 이미지 이해), 그리고 동작 노드와 다른 노드 간의 격리를 제공합니다. 제안된 IoT 솔루션은 로봇 내 관련 노드, RESTful 웹 서비스 및 사용자 인터페이스로 구성됩니다. 우리는 HTTP 프로토콜을 인터넷을 통한 소셜 로봇과의 양방향 통신 수단으로 사용했습니다. 개발자는 C, C++ 및 Python 프로그래밍 언어로 노드를 쉽게 편집하거나 추가할 수 있습니다. 우리의 아키텍처는 소셜 휴머노이드 로봇을 위한 더 정교한 동작 설계에 사용될 수 있습니다.

## 핵심 내용
현재 대부분의 소셜 로봇은 로봇의 일부인 센서를 통해 주변 환경 및 인간과 상호작용하며, 이는 센서의 활용성, 인간-로봇 상호작용 및 호환성을 제한합니다. 다양한 로봇에 적용 가능한 웨어러블 센서 의류가 많은 응용 분야에서 필요합니다. 본 논문은 저렴한 웨어러블 센서 조끼와 사물인터넷(IoT)을 활용한 오픈소스 소프트웨어 아키텍처를 소셜 휴머노이드 로봇용으로 제시합니다. 조끼는 터치, 온도, 제스처, 거리, 비전 센서 및 무선 통신 모듈로 구성됩니다. IoT 기능을 통해 로봇은 로컬 및 인터넷을 통해 인간과 상호작용할 수 있습니다. 설계된 아키텍처는 GPGPU(범용 그래픽 처리 장치), I2C/SPI 버스, 인터넷 연결 및 ROS(로봇 운영 체제)를 갖춘 모든 소셜 로봇에서 작동합니다. 이 아키텍처의 모듈식 설계는 개발자가 복잡한 동작을 쉽게 추가/제거/업데이트할 수 있도록 합니다. 제안된 소프트웨어 아키텍처는 IoT 기술, GPGPU 노드, I2C 및 SPI 버스 관리자, 시청각 상호작용 노드(음성-텍스트, 텍스트-음성, 이미지 이해), 그리고 동작 노드와 다른 노드 간의 격리를 제공합니다. 제안된 IoT 솔루션은 로봇 내 관련 노드, RESTful 웹 서비스 및 사용자 인터페이스로 구성됩니다. 우리는 HTTP 프로토콜을 인터넷을 통한 소셜 로봇과의 양방향 통신 수단으로 사용했습니다. 개발자는 C, C++ 및 Python 프로그래밍 언어로 노드를 쉽게 편집하거나 추가할 수 있습니다. 우리의 아키텍처는 소셜 휴머노이드 로봇을 위한 더 정교한 동작 설계에 사용될 수 있습니다.
