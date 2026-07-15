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


