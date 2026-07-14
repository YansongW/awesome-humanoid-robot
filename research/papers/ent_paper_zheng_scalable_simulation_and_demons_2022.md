---
$id: ent_paper_zheng_scalable_simulation_and_demons_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Scalable Simulation and Demonstration of Jumping Piezoelectric 2-D Soft Robots
  zh: 可扩展的跳跃式压电二维软体机器人仿真与演示
  ko: 확장 가능한 점핑 압전 2차원 소프트 로봇의 시뮬레이션 및 실증
summary:
  en: This paper presents a five-actuator piezoelectric soft robot and a scalable PyBullet-based simulation framework that
    models actuators as discrete rigid-link elements connected by motors, validated against static and dynamic experiments
    including inchworm crawling and jumping.
  zh: 本文提出了一种五执行器压电软体机器人，并开发了一个基于 PyBullet 的可扩展仿真框架，该框架将执行器建模为通过电机连接的离散刚性连杆，并通过包括 inchworm 爬行和跳跃在内的静态与动态实验进行了验证。
  ko: 본 논문은 5개의 구동기를 갖춘 압전 소프트 로봇을 제시하고, 모터로 연결된 이산 강성 링크 요소로 구동부를 모델링하는 확장 가능한 PyBullet 기반 시뮬레이션 프레임워크를 개발하며, inchworm 기어가기
    및 점핑을 포함한 정적·동적 실험으로 검증하였다.
domains:
- 02_components
- 06_design_engineering
- 08_software_middleware
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- intelligence
tags:
- soft_robot
- piezoelectric_actuator
- pybullet_simulation
- pseudo_rigid_body_model
- soft_actuator
- jumping_robot
- inchworm_motion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2202.13521v1.
sources:
- id: src_001
  type: paper
  title: Scalable Simulation and Demonstration of Jumping Piezoelectric 2-D Soft Robots
  url: https://arxiv.org/abs/2202.13521
  date: '2022'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Soft robots have drawn great interest due to their ability to take on a rich range of shapes and motions, compared to traditional rigid robots. However, the motions, and underlying statics and dynamics, pose significant challenges to forming well-generalized and robust models necessary for robot design and control. In this work, we demonstrate a five-actuator soft robot capable of complex motions and develop a scalable simulation framework that reliably predicts robot motions. The simulation framework is validated by comparing its predictions to experimental results, based on a robot constructed from piezoelectric layers bonded to a steel-foil substrate. The simulation framework exploits the physics engine PyBullet, and employs discrete rigid-link elements connected by motors to model the actuators. We perform static and AC analyses to validate a single-unit actuator cantilever setup and observe close agreement between simulation and experiments for both the cases. The analyses are extended to the five-actuator robot, where simulations accurately predict the static and AC robot motions, including shapes for applied DC voltage inputs, nearly-static "inchworm" motion, and jumping (in vertical as well as vertical and horizontal directions). These motions exhibit complex non-linear behavior, with forward robot motion reaching ~1 cm/s. Our open-source code can be found at: https://github.com/zhiwuz/sfers.

## 核心内容
Soft robots have drawn great interest due to their ability to take on a rich range of shapes and motions, compared to traditional rigid robots. However, the motions, and underlying statics and dynamics, pose significant challenges to forming well-generalized and robust models necessary for robot design and control. In this work, we demonstrate a five-actuator soft robot capable of complex motions and develop a scalable simulation framework that reliably predicts robot motions. The simulation framework is validated by comparing its predictions to experimental results, based on a robot constructed from piezoelectric layers bonded to a steel-foil substrate. The simulation framework exploits the physics engine PyBullet, and employs discrete rigid-link elements connected by motors to model the actuators. We perform static and AC analyses to validate a single-unit actuator cantilever setup and observe close agreement between simulation and experiments for both the cases. The analyses are extended to the five-actuator robot, where simulations accurately predict the static and AC robot motions, including shapes for applied DC voltage inputs, nearly-static "inchworm" motion, and jumping (in vertical as well as vertical and horizontal directions). These motions exhibit complex non-linear behavior, with forward robot motion reaching ~1 cm/s. Our open-source code can be found at: https://github.com/zhiwuz/sfers.

## 参考
- http://arxiv.org/abs/2202.13521v1

