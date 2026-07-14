---
$id: ent_paper_mahapatra_3d_printed_cable_driven_contin_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: '3D printed cable-driven continuum robots with generally routed cables: modeling and experiments'
  zh: 具有一般布线方式的3D打印缆索驱动连续体机器人：建模与实验
  ko: '일반적인 케이블 라우팅을 가진 3D 프린팅 케이블 구동 연속체 로봇: 모델링 및 실험'
summary:
  en: Compares a discrete optimization-based kinematic model with a Cosserat-rod static model for six general cable routings
    of a 3D-printed continuum robot, validates predictions within 2% of robot length, and demonstrates a three-fingered gripper.
  zh: 对3D打印连续体机器人的六种一般缆索布线方式，比较基于离散优化的运动学模型与Cosserat杆静力学模型，验证理论预测误差在机器人长度的2%以内，并展示了三指夹持器。
  ko: 3D 프린팅 연속체 로봇의 6가지 일반적인 케이블 라우팅에 대해 이산 최적화 기반 운동학 모델과 Cosserat 막대 정적 모델을 비교하고, 이론 예측이 로봇 길이의 2% 이내임을 검증하며, 3지 그리퍼를 시연한다.
domains:
- 02_components
- 06_design_engineering
- 03_manufacturing_processes
layers:
- midstream
functional_roles:
- knowledge
- component
- system
tags:
- continuum_robot
- cable_driven_robot
- soft_robotics
- 3d_printing
- gripper
- robotic_finger
- cosserat_rod
- kinematic_modeling
- abs
- additive_manufacturing
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2003.04593v1.
sources:
- id: src_001
  type: paper
  title: '3D printed cable-driven continuum robots with generally routed cables: modeling and experiments'
  url: https://arxiv.org/abs/2003.04593
  date: '2020'
  accessed_at: '2026-06-28'
theoretical_depth:
- method
- system
---
## 概述
Continuum robots are becoming increasingly popular for applications which require the robots to deform and change shape, while also being compliant. A cable-driven continuum robot is one of the most commonly used type. Typical cable driven continuum robots consist of a flexible backbone with spacer disks attached to the backbone and cables passing through the holes in the spacer disks from the fixed base to a free end. In most such robots, the routing of the cables are straight or a smooth helical curve. In this paper, we analyze the experimental and theoretical deformations of a 3D printed continuum robot, for 6 different kinds of cable routings. The results are compared for discrete optimization based kinematic modelling as well as static modelling using Cosserat rod theory. It is shown that the experimental results match the theoretical results with an error margin of 2%. It is also shown that the optimization based approach is faster than the one based on Cosserat rod theory. We also present a three-fingered gripper prototype where each of the fingers are 3D printed continuum robots with general cable routing. It is demonstrated that the prototype can be used for gripping objects and for its manipulation.

## 核心内容
Continuum robots are becoming increasingly popular for applications which require the robots to deform and change shape, while also being compliant. A cable-driven continuum robot is one of the most commonly used type. Typical cable driven continuum robots consist of a flexible backbone with spacer disks attached to the backbone and cables passing through the holes in the spacer disks from the fixed base to a free end. In most such robots, the routing of the cables are straight or a smooth helical curve. In this paper, we analyze the experimental and theoretical deformations of a 3D printed continuum robot, for 6 different kinds of cable routings. The results are compared for discrete optimization based kinematic modelling as well as static modelling using Cosserat rod theory. It is shown that the experimental results match the theoretical results with an error margin of 2%. It is also shown that the optimization based approach is faster than the one based on Cosserat rod theory. We also present a three-fingered gripper prototype where each of the fingers are 3D printed continuum robots with general cable routing. It is demonstrated that the prototype can be used for gripping objects and for its manipulation.

## 参考
- http://arxiv.org/abs/2003.04593v1

