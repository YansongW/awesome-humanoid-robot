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

