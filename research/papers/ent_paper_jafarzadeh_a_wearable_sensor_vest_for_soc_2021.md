---
$id: ent_paper_jafarzadeh_a_wearable_sensor_vest_for_soc_2021
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: A wearable sensor vest for social humanoid robots with GPGPU, IoT, and modular
    software architecture
  zh: 面向社交人形机器人的可穿戴传感器背心：集成GPGPU、物联网与模块化软件架构
  ko: GPGPU, IoT 및 모듈형 소프트웨어 아키텍처를 갖춘 사회적 휴머노이드 로봇용 웨어러블 센서 조끼
summary:
  en: This paper presents an affordable wearable sensor vest and a modular ROS-based
    open-source software architecture with IoT connectivity for social humanoid robots,
    supporting touch, temperature, gesture, distance, and vision sensing alongside
    local and remote human-robot interaction.
  zh: 本文提出了一种低成本的可穿戴传感器背心及模块化ROS开源软件架构，集成物联网连接，使社交人形机器人能够进行触觉、温度、手势、距离和视觉感知，并支持本地及远程人机交互。
  ko: 본 논문은 사회적 휴머노이드 로봇을 위한 저렴한 웨어러블 센서 조끼와 IoT 연결을 갖춘 모듈형 ROS 기반 오픈소스 소프트웨어 아키텍처를
    제안하며, 촉각, 온도, 제스처, 거리 및 시각 센싱과 로컬 및 원격 인간-로봇 상호작용을 지원한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; specific section-level
    citations and full-text claims require human review before verification.
sources:
- id: src_001
  type: paper
  title: A wearable sensor vest for social humanoid robots with GPGPU, IoT, and modular
    software architecture
  url: https://arxiv.org/abs/2201.02192
  date: '2021'
  accessed_at: '2026-06-27'
  doi: 10.1016/j.robot.2020.103536
theoretical_depth:
- method
---

## Overview

This article introduces a low-cost wearable sensor vest designed for social humanoid robots, together with an open-source, modular software architecture that integrates embedded GPGPU computing, Internet of Things (IoT) connectivity, and I2C/SPI bus management. The vest hosts multiple sensor modalities—touch, temperature, gesture, distance, and vision—together with a wireless communication module, allowing the robot to sense and interact with humans both locally and over the Internet. The accompanying architecture is intended to be robot-agnostic, requiring only a GPGPU, I2C/SPI buses, an Internet connection, and ROS. By isolating behavior nodes from hardware and service nodes, the design aims to make complex behaviors easier to add, remove, or update without disturbing low-level sensing and actuation.

The hardware prototype is built around embedded NVIDIA platforms (Jetson TX2 and AGX Xavier), a Logitech C922x Pro webcam, force and capacitive touch sensors, time-of-flight and ultrasonic range finders, a gesture sensor, a temperature sensor, ADC and PWM peripherals, servo controllers, RGB LEDs, MOSFETs, and audio I/O. The software side is organized as a set of ROS nodes: behavior nodes implement high-level interaction logic, while dedicated bus-manager nodes regulate access to shared I2C/SPI resources, and service nodes handle GPGPU-accelerated perception and IoT communication. A RESTful web service and remote user interface let operators monitor and control the robot over the Internet.

## Key Contributions

- A wearable sensor vest integrating touch, temperature, gesture, distance, and vision sensors for social humanoid robots.
- A modular ROS-based open-source software architecture that separates behavior nodes from hardware and service nodes.
- Embedded GPGPU integration enabling local deep-learning-based image understanding and audio-visual interaction.
- An IoT framework with a RESTful API and remote user interface for monitoring and controlling robots over the Internet.
- I2C/SPI bus manager nodes that coordinate orderly access to multiple sensors and actuators.

## Relevance to Humanoid Robotics

The work is directly relevant to humanoid robotics because it provides an interchangeable, low-cost sensing and compute framework that can be fitted to different social humanoid robots rather than being tied to a single platform. This modularity supports rapid prototyping and could lower barriers to mass-producing interactive humanoids by standardizing how sensors, embedded AI, and remote services are integrated. The emphasis on wearable, externally mounted sensing also expands the sensing envelope of humanoid bodies without requiring custom internal sensor integration, which is valuable for social humanoids that must perceive and respond to physical contact, proximity, gestures, and faces during human-robot interaction.
