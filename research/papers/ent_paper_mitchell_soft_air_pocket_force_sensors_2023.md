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
  en: This paper presents a soft, sealed air pocket force sensor fabricated from LDPE
    plastic tubing that converts applied force into a linear change in internal pressure,
    and demonstrates its integration on a vine robot for contact-guided growth and
    steering.
  zh: 本文提出了一种由低密度聚乙烯塑料管制成的软密封气囊力传感器，该传感器将施加的力转换为内部压力的线性变化，并展示了其在藤蔓机器人上的集成，用于接触引导的生长和转向。
  ko: 본 논문은 LDPE 플라스틱 튜브로 만든 부드럽고 밀폐된 공기 주머니 힘 센서를 제안하며, 이 센서는 가해진 힘을 내부 압력의 선형 변화로
    변환하고 접촉에 따른 성장 및 조향을 위해 덩굴 로봇에 통합한 사례를 보여준다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from full text; requires human review before verification.
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

## Overview

Flexible robots can conform to their environment and form diverse shapes, but sensing forces across their large, deformable bodies is difficult because sensors must tolerate shape change while remaining lightweight, inexpensive, and scalable. This paper proposes a soft air pocket force sensor made from sealed low-density polyethylene (LDPE) tubing and an embedded MPRLS air pressure sensor. When an external force compresses the pocket, the internal pressure changes approximately linearly with the applied force, enabling simple, low-cost force measurement over large surface areas.

The authors fabricate the sensor using an impulse heat sealer to create sealed LDPE pockets of varying size, thickness, and internal structure. They experimentally characterize how sensitivity is affected by uncontrollable contact factors (radial contact location and contact area) and controllable design factors (initial internal pressure, membrane thickness, pocket size, and number of interior seals). The results provide empirical design guidance for tuning sensor response. The paper also demonstrates the sensor integrated onto a vine robot—a soft inflatable robot that extends by eversion—showing that contact with an object can be detected and used to guide the robot's growth and steering.

## Key Contributions

- Novel soft air pocket force sensor design that is flexible, lightweight, low-cost, and scalable for large flexible robots.
- Experimental characterization of how contact location, contact area, initial internal pressure, membrane thickness, pocket size, and number of interior seals affect sensor sensitivity.
- Demonstration of sensor integration on a vine robot, enabling contact-based growth and steering control.

## Relevance to Humanoid Robotics

Although demonstrated on a vine robot, the sensor design directly addresses requirements that are central to humanoid robotics: large-area, compliant tactile sensing for safe physical interaction. Humanoid robots intended for unstructured environments and close human contact need tactile skins that can cover curved, deformable surfaces without adding significant mass, cost, or wiring complexity. The LDPE air pocket approach can be scaled to cover large areas and fabricated with simple heat sealing, making it compatible with mass production of soft robot coverings. The use of standard pressure sensors and microcontrollers also fits the cost and integration constraints of commercial humanoid platforms.
