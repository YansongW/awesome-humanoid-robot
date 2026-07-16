---
$id: ent_paper_andreasson_sensors_for_mobile_robots_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sensors for Mobile Robots
  zh: 移动机器人传感器
  ko: 모바일 로봇 센서
summary:
  en: A survey chapter that presents a taxonomy, key specifications, and bottom-up survey of sensors used in mobile robots,
    covering tactile, proximity, vision-based, and ranging sensors.
  zh: A sensor is a device that converts a physical parameter or an environmental characteristic (e.g., temperature, distance,
    speed, etc.) into a signal that can be digitally measured and processed to perform specific tasks. Mobile robots need
    sensors to measure properties of their environment, thus allowing for safe navigation, complex perception and corresponding
    actions, and effective interactions with other agents that populate it. Sensors used by mobile robots range from simple
    tactile sensors, such as bumpers, to complex vision-based sensors such as structured light RGB-D cameras. All of them
  ko: 모바일 로봇에 사용되는 센서의 분류법, 주요 사양 및 하향식 개요를 제시하는 서베이 챕터로 촉각, 근접, 비전 기반 및 거리 측정 센서를 다룬다.
domains:
- 02_components
- 06_design_engineering
- 03_manufacturing_processes
- 05_mass_production
layers:
- midstream
- upstream
functional_roles:
- knowledge
tags:
- sensor_survey
- sensor_taxonomy
- mobile_robotics
- exteroceptive_sensors
- proprioceptive_sensors
- lidar
- camera
- imu
- encoders
- rgb_d_cameras
- event_cameras
- sensor_specifications
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2206.03223v3.
sources:
- id: src_001
  type: paper
  title: Sensors for Mobile Robots
  url: https://arxiv.org/abs/2206.03223
  date: '2023'
  accessed_at: '2026-06-27'
  doi: 10.1007/978-3-642-41610-1_159-1
theoretical_depth:
- method
---

## 概述
A sensor is a device that converts a physical parameter or an environmental characteristic (e.g., temperature, distance, speed, etc.) into a signal that can be digitally measured and processed to perform specific tasks. Mobile robots need sensors to measure properties of their environment, thus allowing for safe navigation, complex perception and corresponding actions, and effective interactions with other agents that populate it. Sensors used by mobile robots range from simple tactile sensors, such as bumpers, to complex vision-based sensors such as structured light RGB-D cameras. All of them provide a digital output (e.g., a string, a set of values, a matrix, etc.) that can be processed by the robot's computer. Such output is typically obtained by discretizing one or more analog electrical signals by using an Analog to Digital Converter (ADC) included in the sensor. In this chapter we present the most common sensors used in mobile robotics, providing an introduction to their taxonomy, basic features, and specifications. The description of the functionalities and the types of applications follows a bottom-up approach: the basic principles and components on which the sensors are based are presented before describing real-world sensors, which are generally based on multiple technologies and basic devices.

## 核心内容
A sensor is a device that converts a physical parameter or an environmental characteristic (e.g., temperature, distance, speed, etc.) into a signal that can be digitally measured and processed to perform specific tasks. Mobile robots need sensors to measure properties of their environment, thus allowing for safe navigation, complex perception and corresponding actions, and effective interactions with other agents that populate it. Sensors used by mobile robots range from simple tactile sensors, such as bumpers, to complex vision-based sensors such as structured light RGB-D cameras. All of them provide a digital output (e.g., a string, a set of values, a matrix, etc.) that can be processed by the robot's computer. Such output is typically obtained by discretizing one or more analog electrical signals by using an Analog to Digital Converter (ADC) included in the sensor. In this chapter we present the most common sensors used in mobile robotics, providing an introduction to their taxonomy, basic features, and specifications. The description of the functionalities and the types of applications follows a bottom-up approach: the basic principles and components on which the sensors are based are presented before describing real-world sensors, which are generally based on multiple technologies and basic devices.

## 参考
- http://arxiv.org/abs/2206.03223v3

## Overview
A sensor is a device that converts a physical parameter or an environmental characteristic (e.g., temperature, distance, speed, etc.) into a signal that can be digitally measured and processed to perform specific tasks. Mobile robots need sensors to measure properties of their environment, thus allowing for safe navigation, complex perception and corresponding actions, and effective interactions with other agents that populate it. Sensors used by mobile robots range from simple tactile sensors, such as bumpers, to complex vision-based sensors such as structured light RGB-D cameras. All of them provide a digital output (e.g., a string, a set of values, a matrix, etc.) that can be processed by the robot's computer. Such output is typically obtained by discretizing one or more analog electrical signals by using an Analog to Digital Converter (ADC) included in the sensor. In this chapter we present the most common sensors used in mobile robotics, providing an introduction to their taxonomy, basic features, and specifications. The description of the functionalities and the types of applications follows a bottom-up approach: the basic principles and components on which the sensors are based are presented before describing real-world sensors, which are generally based on multiple technologies and basic devices.

## Content
A sensor is a device that converts a physical parameter or an environmental characteristic (e.g., temperature, distance, speed, etc.) into a signal that can be digitally measured and processed to perform specific tasks. Mobile robots need sensors to measure properties of their environment, thus allowing for safe navigation, complex perception and corresponding actions, and effective interactions with other agents that populate it. Sensors used by mobile robots range from simple tactile sensors, such as bumpers, to complex vision-based sensors such as structured light RGB-D cameras. All of them provide a digital output (e.g., a string, a set of values, a matrix, etc.) that can be processed by the robot's computer. Such output is typically obtained by discretizing one or more analog electrical signals by using an Analog to Digital Converter (ADC) included in the sensor. In this chapter we present the most common sensors used in mobile robotics, providing an introduction to their taxonomy, basic features, and specifications. The description of the functionalities and the types of applications follows a bottom-up approach: the basic principles and components on which the sensors are based are presented before describing real-world sensors, which are generally based on multiple technologies and basic devices.

## 개요
센서는 물리적 매개변수나 환경 특성(예: 온도, 거리, 속도 등)을 디지털로 측정 및 처리하여 특정 작업을 수행할 수 있는 신호로 변환하는 장치입니다. 이동 로봇은 환경의 속성을 측정하기 위해 센서가 필요하며, 이를 통해 안전한 주행, 복잡한 인식 및 이에 따른 동작, 그리고 환경 내 다른 에이전트와의 효과적인 상호작용이 가능해집니다. 이동 로봇이 사용하는 센서는 범퍼와 같은 단순한 촉각 센서부터 구조광 RGB-D 카메라와 같은 복잡한 비전 기반 센서까지 다양합니다. 이 모든 센서는 로봇의 컴퓨터에서 처리할 수 있는 디지털 출력(예: 문자열, 값 집합, 행렬 등)을 제공합니다. 이러한 출력은 일반적으로 센서에 포함된 아날로그-디지털 변환기(ADC)를 사용하여 하나 이상의 아날로그 전기 신호를 이산화함으로써 얻어집니다. 이 장에서는 이동 로봇 공학에서 가장 일반적으로 사용되는 센서를 소개하고, 그 분류, 기본 특징 및 사양에 대한 개요를 제공합니다. 기능 및 응용 유형에 대한 설명은 상향식 접근 방식을 따릅니다: 실제 센서를 설명하기 전에 센서의 기반이 되는 기본 원리와 구성 요소를 먼저 제시하며, 이러한 실제 센서는 일반적으로 여러 기술과 기본 장치를 기반으로 합니다.

## 핵심 내용
센서는 물리적 매개변수나 환경 특성(예: 온도, 거리, 속도 등)을 디지털로 측정 및 처리하여 특정 작업을 수행할 수 있는 신호로 변환하는 장치입니다. 이동 로봇은 환경의 속성을 측정하기 위해 센서가 필요하며, 이를 통해 안전한 주행, 복잡한 인식 및 이에 따른 동작, 그리고 환경 내 다른 에이전트와의 효과적인 상호작용이 가능해집니다. 이동 로봇이 사용하는 센서는 범퍼와 같은 단순한 촉각 센서부터 구조광 RGB-D 카메라와 같은 복잡한 비전 기반 센서까지 다양합니다. 이 모든 센서는 로봇의 컴퓨터에서 처리할 수 있는 디지털 출력(예: 문자열, 값 집합, 행렬 등)을 제공합니다. 이러한 출력은 일반적으로 센서에 포함된 아날로그-디지털 변환기(ADC)를 사용하여 하나 이상의 아날로그 전기 신호를 이산화함으로써 얻어집니다. 이 장에서는 이동 로봇 공학에서 가장 일반적으로 사용되는 센서를 소개하고, 그 분류, 기본 특징 및 사양에 대한 개요를 제공합니다. 기능 및 응용 유형에 대한 설명은 상향식 접근 방식을 따릅니다: 실제 센서를 설명하기 전에 센서의 기반이 되는 기본 원리와 구성 요소를 먼저 제시하며, 이러한 실제 센서는 일반적으로 여러 기술과 기본 장치를 기반으로 합니다.
