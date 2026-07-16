---
$id: ent_paper_mitchell_soft_air_pocket_force_sensors_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Soft Air Pocket Force Sensors for Large Scale Flexible Robots
  zh: 用于大规模柔性机器人的软气囊力传感器
  ko: 대형 유연 로봇을 위한 소프트 공기 주머니 힘 센서
summary:
  en: This paper presents a soft, sealed air pocket force sensor fabricated from LDPE plastic tubing that converts applied
    force into a linear change in internal pressure, and demonstrates its integration on a vine robot for contact-guided growth
    and steering.
  zh: 本文提出了一种由低密度聚乙烯塑料管制成的软密封气囊力传感器，该传感器将施加的力转换为内部压力的线性变化，并展示了其在藤蔓机器人上的集成，用于接触引导的生长和转向。
  ko: 본 논문은 LDPE 플라스틱 튜브로 만든 부드럽고 밀폐된 공기 주머니 힘 센서를 제안하며, 이 센서는 가해진 힘을 내부 압력의 선형 변화로 변환하고 접촉에 따른 성장 및 조향을 위해 덩굴 로봇에 통합한 사례를
    보여준다.
domains:
- 02_components
- 03_manufacturing_processes
- 05_mass_production
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- component
- process
- knowledge
tags:
- soft_sensor
- force_sensor
- air_pocket_sensor
- tactile_sensing
- flexible_robot
- vine_robot
- large_scale_sensor
- low_density_polyethylene
- soft_robotics
- mass_production
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.14213v1.
sources:
- id: src_001
  type: paper
  title: Soft Air Pocket Force Sensors for Large Scale Flexible Robots
  url: https://arxiv.org/abs/2307.14213
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Flexible robots have advantages over rigid robots in their ability to conform physically to their environment and to form a wide variety of shapes. Sensing the force applied by or to flexible robots is useful for both navigation and manipulation tasks, but it is challenging due to the need for the sensors to withstand the robots' shape change without encumbering their functionality. Also, for robots with long or large bodies, the number of sensors required to cover the entire surface area of the robot body can be prohibitive due to high cost and complexity. We present a novel soft air pocket force sensor that is highly flexible, lightweight, relatively inexpensive, and easily scalable to various sizes. Our sensor produces a change in internal pressure that is linear with the applied force. We present results of experimental testing of how uncontrollable factors (contact location and contact area) and controllable factors (initial internal pressure, thickness, size, and number of interior seals) affect the sensitivity. We demonstrate our sensor applied to a vine robot-a soft inflatable robot that "grows" from the tip via eversion-and we show that the robot can successfully grow and steer towards an object with which it senses contact.

## 核心内容
Flexible robots have advantages over rigid robots in their ability to conform physically to their environment and to form a wide variety of shapes. Sensing the force applied by or to flexible robots is useful for both navigation and manipulation tasks, but it is challenging due to the need for the sensors to withstand the robots' shape change without encumbering their functionality. Also, for robots with long or large bodies, the number of sensors required to cover the entire surface area of the robot body can be prohibitive due to high cost and complexity. We present a novel soft air pocket force sensor that is highly flexible, lightweight, relatively inexpensive, and easily scalable to various sizes. Our sensor produces a change in internal pressure that is linear with the applied force. We present results of experimental testing of how uncontrollable factors (contact location and contact area) and controllable factors (initial internal pressure, thickness, size, and number of interior seals) affect the sensitivity. We demonstrate our sensor applied to a vine robot-a soft inflatable robot that "grows" from the tip via eversion-and we show that the robot can successfully grow and steer towards an object with which it senses contact.

## 参考
- http://arxiv.org/abs/2307.14213v1

## Overview
Flexible robots have advantages over rigid robots in their ability to conform physically to their environment and to form a wide variety of shapes. Sensing the force applied by or to flexible robots is useful for both navigation and manipulation tasks, but it is challenging due to the need for the sensors to withstand the robots' shape change without encumbering their functionality. Also, for robots with long or large bodies, the number of sensors required to cover the entire surface area of the robot body can be prohibitive due to high cost and complexity. We present a novel soft air pocket force sensor that is highly flexible, lightweight, relatively inexpensive, and easily scalable to various sizes. Our sensor produces a change in internal pressure that is linear with the applied force. We present results of experimental testing of how uncontrollable factors (contact location and contact area) and controllable factors (initial internal pressure, thickness, size, and number of interior seals) affect the sensitivity. We demonstrate our sensor applied to a vine robot—a soft inflatable robot that "grows" from the tip via eversion—and we show that the robot can successfully grow and steer towards an object with which it senses contact.

## Content
Flexible robots have advantages over rigid robots in their ability to conform physically to their environment and to form a wide variety of shapes. Sensing the force applied by or to flexible robots is useful for both navigation and manipulation tasks, but it is challenging due to the need for the sensors to withstand the robots' shape change without encumbering their functionality. Also, for robots with long or large bodies, the number of sensors required to cover the entire surface area of the robot body can be prohibitive due to high cost and complexity. We present a novel soft air pocket force sensor that is highly flexible, lightweight, relatively inexpensive, and easily scalable to various sizes. Our sensor produces a change in internal pressure that is linear with the applied force. We present results of experimental testing of how uncontrollable factors (contact location and contact area) and controllable factors (initial internal pressure, thickness, size, and number of interior seals) affect the sensitivity. We demonstrate our sensor applied to a vine robot—a soft inflatable robot that "grows" from the tip via eversion—and we show that the robot can successfully grow and steer towards an object with which it senses contact.

## 개요
유연 로봇은 환경에 물리적으로 적응하고 다양한 형태를 형성할 수 있는 능력에서 강체 로봇보다 장점을 가집니다. 유연 로봇이 가하거나 받는 힘을 감지하는 것은 탐색 및 조작 작업 모두에 유용하지만, 센서가 로봇의 기능을 방해하지 않으면서 형상 변화를 견뎌야 하기 때문에 어렵습니다. 또한, 길거나 큰 몸체를 가진 로봇의 경우, 로봇 몸체 전체 표면을 덮는 데 필요한 센서 수가 높은 비용과 복잡성으로 인해 실용적이지 않을 수 있습니다. 본 연구에서는 매우 유연하고 가벼우며 비교적 저렴하고 다양한 크기로 쉽게 확장 가능한 새로운 소프트 에어 포켓 힘 센서를 제시합니다. 이 센서는 가해진 힘에 선형적으로 비례하는 내부 압력 변화를 생성합니다. 제어 불가능한 요인(접촉 위치 및 접촉 면적)과 제어 가능한 요인(초기 내부 압력, 두께, 크기, 내부 밀봉 개수)이 감도에 미치는 영향을 실험적으로 테스트한 결과를 제시합니다. 또한, 이 센서를 덩굴 로봇(끝에서 외전을 통해 '성장'하는 소프트 팽창식 로봇)에 적용하여, 로봇이 접촉을 감지한 물체를 향해 성공적으로 성장하고 방향을 조정할 수 있음을 보여줍니다.

## 핵심 내용
유연 로봇은 환경에 물리적으로 적응하고 다양한 형태를 형성할 수 있는 능력에서 강체 로봇보다 장점을 가집니다. 유연 로봇이 가하거나 받는 힘을 감지하는 것은 탐색 및 조작 작업 모두에 유용하지만, 센서가 로봇의 기능을 방해하지 않으면서 형상 변화를 견뎌야 하기 때문에 어렵습니다. 또한, 길거나 큰 몸체를 가진 로봇의 경우, 로봇 몸체 전체 표면을 덮는 데 필요한 센서 수가 높은 비용과 복잡성으로 인해 실용적이지 않을 수 있습니다. 본 연구에서는 매우 유연하고 가벼우며 비교적 저렴하고 다양한 크기로 쉽게 확장 가능한 새로운 소프트 에어 포켓 힘 센서를 제시합니다. 이 센서는 가해진 힘에 선형적으로 비례하는 내부 압력 변화를 생성합니다. 제어 불가능한 요인(접촉 위치 및 접촉 면적)과 제어 가능한 요인(초기 내부 압력, 두께, 크기, 내부 밀봉 개수)이 감도에 미치는 영향을 실험적으로 테스트한 결과를 제시합니다. 또한, 이 센서를 덩굴 로봇(끝에서 외전을 통해 '성장'하는 소프트 팽창식 로봇)에 적용하여, 로봇이 접촉을 감지한 물체를 향해 성공적으로 성장하고 방향을 조정할 수 있음을 보여줍니다.
