---
$id: ent_paper_maur_roboa_construction_and_evaluat_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RoBoa: Construction and Evaluation of a Steerable Vine Robot for Search and
    Rescue Applications'
  zh: RoBoa：面向搜索救援应用的可转向藤蔓机器人的构建与评估
  ko: 'RoBoa: 탐색 및 구조 응용을 위한 조향 가능한 덩굴 로봇의 구축 및 평가'
summary:
  en: RoBoa is a 17-meter steerable vine robot for search and rescue that everts a
    soft fabric tube for locomotion and uses internal 3D-printed pneumatic actuators
    at the tip for steering, validated in a collapsed-building test site.
  zh: RoBoa是一种17米长的可转向藤蔓搜索救援机器人，通过外翻软质织物管实现移动，并利用尖端内部的3D打印气动执行器进行转向，已在倒塌建筑测试场地得到验证。
  ko: RoBoa는 17m 길이의 조향 가능한 덩굴 탐색 및 구조 로봇으로, 부드러운 직물 튜브를 에버팅하여 이동하고 끝단 내부의 3D 프린팅
    공압 액추에이터를 이용해 조향하며, 붕괴된 건물 시험 현장에서 검증되었다.
domains:
- 02_components
- 03_manufacturing_processes
- 05_mass_production
- 06_design_engineering
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- vine_robot
- soft_robot
- pneumatic_actuator
- search_and_rescue
- continuum_robot
- soft_actuator
- disaster_response
- eversion_locomotion
- tip_steering
- decentralized_control
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-28'
  confidence: medium
  notes: AI-extracted from abstract and provided metadata; full-text review is required
    before promotion to verified.; approved by autonomous review workflow.
sources:
- id: src_001
  type: paper
  title: 'RoBoa: Construction and Evaluation of a Steerable Vine Robot for Search
    and Rescue Applications'
  url: https://arxiv.org/abs/2203.15145
  date: '2022'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---

## Overview

RoBoa is a vine-like search-and-rescue robot designed to explore narrow, cluttered environments such as destroyed buildings. It locomotes by everting the tip of a soft fabric tube, so the body grows forward from the tip while the remainder stays stationary. A sensor head mounted outside at the tube tip provides camera, audio, and IMU feedback, and a supply box at the rear stores the rolled tube and provides pressurized air, power, computation, and a user interface. The system is fully functional and was demonstrated in a realistic collapsed-building scenario, repeatedly locating a trapped person after traveling about 10 m.

Inside the tube, 3D-printed pneumatic actuators enable lateral steering from the tip. A decentralized control scheme places valve terminals on the moving tip actuators, reducing cabling so that only one pressure tube is needed to the front. The prototype achieves a bending radius of 20 cm and a deployed length of 17 m, which the authors report as 70% longer than prior steerable vine robots.

The paper presents the design, characterization, and experimental evaluation of the system and its key components, including the tube material, actuators, electronics, supply box, and control architecture.

## Key Contributions

- Tip-steering concept for vine robots using internal pneumatic actuators that remain at the front, achieving a 20 cm bending radius.
- Demonstration of a 17 m steerable vine robot, reported as 70% longer than prior steerable vine robots.
- Decentralized pressure supply using valve terminals mounted on the moving tip actuators, requiring only one pressure tube to the front.
- Real-world validation in the debris of a destroyed building at a Swiss Rescue Troops training site.
- Interlocking head-to-tube mechanism that supports a wireless sensor head without obstructing eversion.

## Relevance to Humanoid Robotics

Although RoBoa is a search-and-rescue platform rather than a humanoid, its technology is directly transferable to humanoid robotics. The soft pneumatic actuators, decentralized valve-terminal control architecture, and fabric-tube manufacturing methods can inform the design of soft continuum joints and lightweight limbs for humanoid robots. The work also demonstrates how soft, deployable structures can be packaged compactly and extended on demand, a strategy relevant to lightweight, field-deployable humanoid systems and mass-production techniques for compliant mechanical components.
