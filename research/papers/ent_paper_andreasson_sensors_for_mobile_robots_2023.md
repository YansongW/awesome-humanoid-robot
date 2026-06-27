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
  en: A survey chapter that presents a taxonomy, key specifications, and bottom-up
    survey of sensors used in mobile robots, covering tactile, proximity, vision-based,
    and ranging sensors.
  zh: 一篇综述章节，介绍移动机器人所用传感器的分类法、关键规格和自下而上的概述，涵盖触觉、接近、基于视觉和测距传感器。
  ko: 모바일 로봇에 사용되는 센서의 분류법, 주요 사양 및 하향식 개요를 제시하는 서베이 챕터로 촉각, 근접, 비전 기반 및 거리 측정 센서를
    다룬다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from the supplied metadata and abstract; full-text review is
    needed before verification.
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

## Overview

This chapter provides a broad survey of the sensors used in mobile robotics. It begins by explaining why mobile robots need diverse sensors to measure environmental and internal-state properties for safe navigation, perception, and interaction. The authors then introduce a taxonomy that classifies sensors according to their excitation source (passive or active), measurement domain (proprioceptive or exteroceptive), and measurement type. This organizational framework is used to structure the rest of the chapter.

Following the taxonomy, the paper characterizes key sensor specifications such as linearity, range, resolution, precision, accuracy, bandwidth, and response time. It then takes a bottom-up approach by describing basic transducer components—those based on force/deformation, light, electromagnetic, and magnetic principles—and the signal-conversion methods that turn physical measurements into usable data. Finally, the chapter surveys real-world sensor implementations, including encoders, GNSS/UWB positioning systems, IMUs, cameras, sonar, LiDAR, radar, Time-of-Flight cameras, stereo systems, structured-light cameras, and RGB-D cameras, and briefly discusses application scenarios and future trends.

The work is explicitly positioned as a survey and does not report new experimental results or quantitative benchmarks. Its value lies in providing a unified, accessible reference for sensor selection and integration in mobile robotics, including the supply-chain and design considerations relevant to humanoid mass production.

## Key Contributions

- A taxonomy of mobile-robot sensors based on passive/active excitation, proprioceptive/exteroceptive measurement domain, and measurement type.
- A characterization of key sensor specifications including linearity, range, resolution, precision, accuracy, bandwidth, and response time.
- A bottom-up presentation of basic transducer components (force/deformation, light, electromagnetic, magnetic) and signal-conversion methods.
- A comprehensive survey of real-world sensors: encoders, GNSS/UWB, IMUs, cameras, sonar, LiDAR, radar, ToF, stereo, structured light, and RGB-D cameras.
- Discussion of example application scenarios and emerging future directions such as solid-state LiDAR, event cameras, MIMO radar, and AI-enabled smart sensors.

## Relevance to Humanoid Robotics

Humanoid robots are a special class of mobile robots and depend on the same core sensor classes surveyed in this chapter—vision sensors, ranging sensors, IMUs, encoders, and proximity/contact sensors—to maintain balance, navigate, avoid obstacles, manipulate objects, and interact safely with humans. The taxonomy and specification framework therefore provide a direct foundation for humanoid sensor selection, system integration, and trade-off analysis.

Because the chapter also covers real-world implementations and commercial examples, it is relevant to the design-engineering, manufacturing-process, and mass-production domains of humanoid robotics. Engineers can use the survey to compare sensing technologies, understand supply-chain options, and anticipate emerging components such as solid-state LiDAR, event cameras, and AI-enabled smart sensors. However, the survey does not address humanoid-specific sensing needs such as whole-body tactile skins, joint-torque sensing, or expressive human-robot interaction sensors, which must be supplemented from other sources.
