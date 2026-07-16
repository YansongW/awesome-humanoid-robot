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

## Overview
Soft robots have drawn great interest due to their ability to take on a rich range of shapes and motions, compared to traditional rigid robots. However, the motions, and underlying statics and dynamics, pose significant challenges to forming well-generalized and robust models necessary for robot design and control. In this work, we demonstrate a five-actuator soft robot capable of complex motions and develop a scalable simulation framework that reliably predicts robot motions. The simulation framework is validated by comparing its predictions to experimental results, based on a robot constructed from piezoelectric layers bonded to a steel-foil substrate. The simulation framework exploits the physics engine PyBullet, and employs discrete rigid-link elements connected by motors to model the actuators. We perform static and AC analyses to validate a single-unit actuator cantilever setup and observe close agreement between simulation and experiments for both the cases. The analyses are extended to the five-actuator robot, where simulations accurately predict the static and AC robot motions, including shapes for applied DC voltage inputs, nearly-static "inchworm" motion, and jumping (in vertical as well as vertical and horizontal directions). These motions exhibit complex non-linear behavior, with forward robot motion reaching ~1 cm/s. Our open-source code can be found at: https://github.com/zhiwuz/sfers.

## Content
Soft robots have drawn great interest due to their ability to take on a rich range of shapes and motions, compared to traditional rigid robots. However, the motions, and underlying statics and dynamics, pose significant challenges to forming well-generalized and robust models necessary for robot design and control. In this work, we demonstrate a five-actuator soft robot capable of complex motions and develop a scalable simulation framework that reliably predicts robot motions. The simulation framework is validated by comparing its predictions to experimental results, based on a robot constructed from piezoelectric layers bonded to a steel-foil substrate. The simulation framework exploits the physics engine PyBullet, and employs discrete rigid-link elements connected by motors to model the actuators. We perform static and AC analyses to validate a single-unit actuator cantilever setup and observe close agreement between simulation and experiments for both the cases. The analyses are extended to the five-actuator robot, where simulations accurately predict the static and AC robot motions, including shapes for applied DC voltage inputs, nearly-static "inchworm" motion, and jumping (in vertical as well as vertical and horizontal directions). These motions exhibit complex non-linear behavior, with forward robot motion reaching ~1 cm/s. Our open-source code can be found at: https://github.com/zhiwuz/sfers.

## 개요
소프트 로봇은 기존의 강체 로봇에 비해 풍부한 형상과 움직임을 구현할 수 있는 능력으로 인해 큰 관심을 받아왔습니다. 그러나 이러한 움직임과 그 기저의 정역학 및 동역학은 로봇 설계와 제어에 필요한 잘 일반화되고 강건한 모델을 형성하는 데 상당한 도전 과제를 제기합니다. 본 연구에서는 복잡한 움직임이 가능한 5-액추에이터 소프트 로봇을 시연하고, 로봇 움직임을 신뢰성 있게 예측하는 확장 가능한 시뮬레이션 프레임워크를 개발합니다. 이 시뮬레이션 프레임워크는 강철 호일 기판에 접합된 압전 층으로 구성된 로봇을 기반으로, 예측 결과를 실험 결과와 비교하여 검증됩니다. 시뮬레이션 프레임워크는 물리 엔진 PyBullet을 활용하며, 액추에이터를 모델링하기 위해 모터로 연결된 이산 강체 링크 요소를 사용합니다. 우리는 정적 및 AC 분석을 수행하여 단일 유닛 액추에이터 캔틸레버 설정을 검증하고, 두 경우 모두에서 시뮬레이션과 실험 간의 밀접한 일치를 관찰합니다. 분석은 5-액추에이터 로봇으로 확장되며, 시뮬레이션은 정적 및 AC 로봇 움직임, 즉 인가된 DC 전압 입력에 대한 형상, 준정적 "인치웜" 움직임, 점프(수직 방향 및 수직/수평 방향 모두)를 정확하게 예측합니다. 이러한 움직임은 복잡한 비선형 거동을 나타내며, 전진 로봇 움직임은 약 1 cm/s에 도달합니다. 오픈소스 코드는 다음에서 확인할 수 있습니다: https://github.com/zhiwuz/sfers.

## 핵심 내용
소프트 로봇은 기존의 강체 로봇에 비해 풍부한 형상과 움직임을 구현할 수 있는 능력으로 인해 큰 관심을 받아왔습니다. 그러나 이러한 움직임과 그 기저의 정역학 및 동역학은 로봇 설계와 제어에 필요한 잘 일반화되고 강건한 모델을 형성하는 데 상당한 도전 과제를 제기합니다. 본 연구에서는 복잡한 움직임이 가능한 5-액추에이터 소프트 로봇을 시연하고, 로봇 움직임을 신뢰성 있게 예측하는 확장 가능한 시뮬레이션 프레임워크를 개발합니다. 이 시뮬레이션 프레임워크는 강철 호일 기판에 접합된 압전 층으로 구성된 로봇을 기반으로, 예측 결과를 실험 결과와 비교하여 검증됩니다. 시뮬레이션 프레임워크는 물리 엔진 PyBullet을 활용하며, 액추에이터를 모델링하기 위해 모터로 연결된 이산 강체 링크 요소를 사용합니다. 우리는 정적 및 AC 분석을 수행하여 단일 유닛 액추에이터 캔틸레버 설정을 검증하고, 두 경우 모두에서 시뮬레이션과 실험 간의 밀접한 일치를 관찰합니다. 분석은 5-액추에이터 로봇으로 확장되며, 시뮬레이션은 정적 및 AC 로봇 움직임, 즉 인가된 DC 전압 입력에 대한 형상, 준정적 "인치웜" 움직임, 점프(수직 방향 및 수직/수평 방향 모두)를 정확하게 예측합니다. 이러한 움직임은 복잡한 비선형 거동을 나타내며, 전진 로봇 움직임은 약 1 cm/s에 도달합니다. 오픈소스 코드는 다음에서 확인할 수 있습니다: https://github.com/zhiwuz/sfers.
