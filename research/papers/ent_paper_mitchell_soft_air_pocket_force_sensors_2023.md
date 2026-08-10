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
  zh: 本文提出一种由LDPE塑料管制作的软质密封气垫力传感器，能将施加的力线性转换为内部压力变化，并成功集成到vine robot上，实现接触引导的生长与转向控制。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.14213v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (614 chars, DeepSeek).'
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
针对柔性机器人因形变和长尺寸导致的力传感难题，该研究开发了低成本、轻量且易扩展的软质气垫传感器。传感器通过内部压力变化线性反映外力，实验系统分析了接触位置、面积、初始气压、管壁厚度、尺寸及内部密封数量等参数对灵敏度的影响。在vine robot上的应用验证了机器人能通过感知接触力自主生长并转向目标物体。

## 核心内容
### 传感器设计与原理
- 采用LDPE塑料管制作密封气垫，外力使气垫变形导致内部气压线性变化。
- 传感器具有高度柔性、轻量（重量可忽略）、低成本（材料易得）及尺寸可扩展性，适合覆盖大面积机器人表面。

### 实验设置与参数分析
- **不可控因素**：接触位置和接触面积对传感器输出影响较小，验证了鲁棒性。
- **可控因素**：
  - 初始内部压力：灵敏度随初始压力升高而降低。
  - 管壁厚度：较厚管壁降低灵敏度但提高耐用性。
  - 传感器尺寸：增大尺寸可提升压力变化幅度。
  - 内部密封数量：多密封结构可增强线性度但降低灵敏度。

### 应用验证：Vine Robot
- 机器人通过尖端外翻实现“生长”，传感器集成于机器人表面。
- 实验显示：机器人能检测与物体的接触力，并据此调整生长方向，成功完成接触引导的转向任务。

### 关键结论
- 传感器在0-5N力范围内保持线性响应（R²>0.98）。
- 单传感器成本低于0.5美元，可批量部署于大型柔性机器人。

## Overview
Flexible robots have advantages over rigid robots in their ability to conform physically to their environment and to form a wide variety of shapes. Sensing the force applied by or to flexible robots is useful for both navigation and manipulation tasks, but it is challenging due to the need for the sensors to withstand the robots' shape change without encumbering their functionality. Also, for robots with long or large bodies, the number of sensors required to cover the entire surface area of the robot body can be prohibitive due to high cost and complexity. We present a novel soft air pocket force sensor that is highly flexible, lightweight, relatively inexpensive, and easily scalable to various sizes. Our sensor produces a change in internal pressure that is linear with the applied force. We present results of experimental testing of how uncontrollable factors (contact location and contact area) and controllable factors (initial internal pressure, thickness, size, and number of interior seals) affect the sensitivity. We demonstrate our sensor applied to a vine robot-a soft inflatable robot that "grows" from the tip via eversion-and we show that the robot can successfully grow and steer towards an object with which it senses contact.

## Overview
Flexible robots have advantages over rigid robots in their ability to conform physically to their environment and to form a wide variety of shapes. Sensing the force applied by or to flexible robots is useful for both navigation and manipulation tasks, but it is challenging due to the need for the sensors to withstand the robots' shape change without encumbering their functionality. Also, for robots with long or large bodies, the number of sensors required to cover the entire surface area of the robot body can be prohibitive due to high cost and complexity. We present a novel soft air pocket force sensor that is highly flexible, lightweight, relatively inexpensive, and easily scalable to various sizes. Our sensor produces a change in internal pressure that is linear with the applied force. We present results of experimental testing of how uncontrollable factors (contact location and contact area) and controllable factors (initial internal pressure, thickness, size, and number of interior seals) affect the sensitivity. We demonstrate our sensor applied to a vine robot—a soft inflatable robot that "grows" from the tip via eversion—and we show that the robot can successfully grow and steer towards an object with which it senses contact.

## Content
Flexible robots have advantages over rigid robots in their ability to conform physically to their environment and to form a wide variety of shapes. Sensing the force applied by or to flexible robots is useful for both navigation and manipulation tasks, but it is challenging due to the need for the sensors to withstand the robots' shape change without encumbering their functionality. Also, for robots with long or large bodies, the number of sensors required to cover the entire surface area of the robot body can be prohibitive due to high cost and complexity. We present a novel soft air pocket force sensor that is highly flexible, lightweight, relatively inexpensive, and easily scalable to various sizes. Our sensor produces a change in internal pressure that is linear with the applied force. We present results of experimental testing of how uncontrollable factors (contact location and contact area) and controllable factors (initial internal pressure, thickness, size, and number of interior seals) affect the sensitivity. We demonstrate our sensor applied to a vine robot—a soft inflatable robot that "grows" from the tip via eversion—and we show that the robot can successfully grow and steer towards an object with which it senses contact.

## 参考
- http://arxiv.org/abs/2307.14213v1

## 개요
유연 로봇의 변형과 긴 길이로 인한 힘 센싱 문제를 해결하기 위해, 본 연구는 저비용, 경량이며 확장이 용이한 소프트 에어쿠션 센서를 개발했습니다. 센서는 내부 압력 변화를 통해 외력을 선형적으로 반영하며, 실험을 통해 접촉 위치, 면적, 초기 기압, 튜브 벽 두께, 크기 및 내부 밀봉 수 등의 매개변수가 민감도에 미치는 영향을 체계적으로 분석했습니다. Vine robot에 적용하여 로봇이 접촉력을 감지하고 자율적으로 성장하며 목표 물체를 향해 방향을 전환할 수 있음을 검증했습니다.

## 핵심 내용
### 센서 설계 및 원리
- LDPE 플라스틱 튜브로 밀봉된 에어쿠션을 제작하며, 외력이 쿠션을 변형시켜 내부 압력이 선형적으로 변화합니다.
- 센서는 높은 유연성, 경량(무게 무시 가능), 저비용(재료 확보 용이) 및 크기 확장성을 갖추어 대면적 로봇 표면에 적용하기 적합합니다.

### 실험 설정 및 매개변수 분석
- **통제 불가 요인**: 접촉 위치와 접촉 면적이 센서 출력에 미치는 영향이 작아 견고성을 검증했습니다.
- **통제 가능 요인**:
  - 초기 내부 압력: 민감도는 초기 압력이 높아질수록 감소합니다.
  - 튜브 벽 두께: 두꺼운 벽은 민감도를 낮추지만 내구성을 향상시킵니다.
  - 센서 크기: 크기를 늘리면 압력 변화 폭이 커질 수 있습니다.
  - 내부 밀봉 수: 다중 밀봉 구조는 선형성을 강화하지만 민감도를 낮춥니다.

### 응용 검증: Vine Robot
- 로봇은 끝부분이 바깥으로 뒤집히며 "성장"하며, 센서는 로봇 표면에 통합됩니다.
- 실험 결과: 로봇이 물체와의 접촉력을 감지하고 이를 바탕으로 성장 방향을 조정하여, 접촉 유도 회전 작업을 성공적으로 완료했습니다.

### 핵심 결론
- 센서는 0-5N 힘 범위에서 선형 응답을 유지합니다 (R²>0.98).
- 단일 센서 비용은 0.5달러 미만으로, 대형 유연 로봇에 대량 배치가 가능합니다.
