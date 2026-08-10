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
  zh: 本文是一篇关于移动机器人传感器的综述章节，系统介绍了传感器的分类体系、关键性能指标，并采用自底向上的方法详细阐述了触觉、接近觉、视觉及测距传感器的工作原理与应用。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2206.03223v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (565 chars, DeepSeek).'
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
传感器是将物理参数或环境特征（如温度、距离、速度等）转换为可数字测量与处理信号的装置。移动机器人依赖传感器感知环境，以实现安全导航、复杂感知与相应动作，以及与其他智能体的有效交互。本文按自底向上的结构，从基础原理与组件出发，逐步介绍实际传感器，涵盖触觉传感器（如保险杠）、接近觉传感器、视觉传感器（如结构光RGB-D相机）及测距传感器，并给出分类体系与关键规格说明。

## 核心内容
### 传感器定义与作用
传感器将物理参数或环境特征（如温度、距离、速度）转换为可数字测量与处理的信号。移动机器人利用传感器测量环境属性，从而支持安全导航、复杂感知与相应动作，以及与其他智能体的有效交互。

### 传感器类型与输出
- 移动机器人使用的传感器范围广泛，从简单的触觉传感器（如保险杠）到复杂的视觉传感器（如结构光RGB-D相机）。
- 所有传感器均提供数字输出（如字符串、数值集合、矩阵等），供机器人计算机处理。
- 数字输出通常通过传感器内置的模数转换器（ADC）对模拟电信号进行离散化获得。

### 章节内容与结构
- 本文介绍移动机器人中最常见的传感器，涵盖其分类体系、基本特性与规格。
- 采用自底向上的方法描述功能与应用：先介绍传感器所基于的基本原理与组件，再介绍通常集成多种技术与基础器件的实际传感器。

## Overview
A sensor is a device that converts a physical parameter or an environmental characteristic (e.g., temperature, distance, speed, etc.) into a signal that can be digitally measured and processed to perform specific tasks. Mobile robots need sensors to measure properties of their environment, thus allowing for safe navigation, complex perception and corresponding actions, and effective interactions with other agents that populate it. Sensors used by mobile robots range from simple tactile sensors, such as bumpers, to complex vision-based sensors such as structured light RGB-D cameras. All of them provide a digital output (e.g., a string, a set of values, a matrix, etc.) that can be processed by the robot's computer. Such output is typically obtained by discretizing one or more analog electrical signals by using an Analog to Digital Converter (ADC) included in the sensor. In this chapter we present the most common sensors used in mobile robotics, providing an introduction to their taxonomy, basic features, and specifications. The description of the functionalities and the types of applications follows a bottom-up approach: the basic principles and components on which the sensors are based are presented before describing real-world sensors, which are generally based on multiple technologies and basic devices.

## 参考
- http://arxiv.org/abs/2206.03223v3

## 개요
센서는 물리적 매개변수나 환경 특성(예: 온도, 거리, 속도 등)을 디지털 측정 및 처리 가능한 신호로 변환하는 장치입니다. 이동 로봇은 환경을 인식하기 위해 센서에 의존하며, 이를 통해 안전한 내비게이션, 복잡한 인식 및 이에 상응하는 동작, 그리고 다른 지능형 에이전트와의 효과적인 상호작용을 실현합니다. 본 문서는 하향식 구조를 따라 기본 원리와 구성 요소에서 출발하여 실제 센서를 단계적으로 소개하며, 촉각 센서(예: 범퍼), 근접 센서, 시각 센서(예: 구조광 RGB-D 카메라) 및 거리 측정 센서를 다루고, 분류 체계와 주요 사양을 제시합니다.

## 핵심 내용
### 센서 정의 및 역할
센서는 물리적 매개변수나 환경 특성(예: 온도, 거리, 속도)을 디지털 측정 및 처리 가능한 신호로 변환합니다. 이동 로봇은 센서를 사용하여 환경 속성을 측정하며, 이를 통해 안전한 내비게이션, 복잡한 인식 및 이에 상응하는 동작, 그리고 다른 지능형 에이전트와의 효과적인 상호작용을 지원합니다.

### 센서 유형 및 출력
- 이동 로봇에 사용되는 센서는 단순한 촉각 센서(예: 범퍼)부터 복잡한 시각 센서(예: 구조광 RGB-D 카메라)까지 광범위합니다.
- 모든 센서는 로봇 컴퓨터가 처리할 수 있도록 디지털 출력(예: 문자열, 숫자 집합, 행렬 등)을 제공합니다.
- 디지털 출력은 일반적으로 센서 내장 아날로그-디지털 변환기(ADC)를 통해 아날로그 전기 신호를 이산화하여 얻습니다.

### 챕터 내용 및 구조
- 본 문서는 이동 로봇에서 가장 흔한 센서를 소개하며, 분류 체계, 기본 특성 및 사양을 다룹니다.
- 기능과 응용을 설명하기 위해 하향식 방법을 사용합니다: 먼저 센서가 기반으로 하는 기본 원리와 구성 요소를 소개한 다음, 일반적으로 여러 기술과 기본 장치를 통합한 실제 센서를 소개합니다.
