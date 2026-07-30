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
  zh: 本文研究了一种3D打印线缆驱动连续体机器人，针对六种通用线缆路由方式，对比了基于离散优化的运动学模型与Cosserat rod静力学模型，实验验证误差在机器人长度的2%以内，并展示了三指夹持器原型。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2003.04593v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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
连续体机器人因能变形和顺应环境而日益流行，其中线缆驱动型最为常见。传统机器人的线缆路由多为直线或平滑螺旋曲线，而本文探索了六种通用路由方式。通过3D打印机器人进行实验，对比了离散优化运动学模型和Cosserat rod静力学模型的理论预测，发现两者与实验结果的误差均小于2%，且优化方法计算更快。此外，基于该设计制造的三指夹持器原型成功实现了抓取和操作物体。

## 核心内容
### 方法与架构
- 机器人结构：采用柔性骨架，间隔盘附着其上，线缆从固定基座穿过间隔盘孔到达自由端。
- 线缆路由：研究了六种通用路由方式，区别于传统的直线或平滑螺旋曲线。
- 建模方法：
  - **离散优化运动学模型**：基于分段常曲率假设，通过优化求解变形。
  - **Cosserat rod静力学模型**：考虑杆的弯曲、扭转和剪切，求解平衡方程。

### 实验设置
- 使用3D打印机制造连续体机器人原型，测试六种线缆路由下的变形。
- 测量实验变形并与两种模型的理论预测对比。

### 关键结果
- 两种模型的预测与实验结果的误差均在机器人长度的2%以内。
- 离散优化方法计算速度显著快于Cosserat rod方法。
- 三指夹持器原型（每指均为通用路由的3D打印连续体机器人）成功实现抓取和操作物体。

### 结论
本文验证了通用线缆路由在3D打印连续体机器人中的可行性，提供了快速且精确的建模方法，并展示了其在夹持器中的应用潜力。

## Overview
Continuum robots are becoming increasingly popular for applications which require the robots to deform and change shape, while also being compliant. A cable-driven continuum robot is one of the most commonly used type. Typical cable driven continuum robots consist of a flexible backbone with spacer disks attached to the backbone and cables passing through the holes in the spacer disks from the fixed base to a free end. In most such robots, the routing of the cables are straight or a smooth helical curve. In this paper, we analyze the experimental and theoretical deformations of a 3D printed continuum robot, for 6 different kinds of cable routings. The results are compared for discrete optimization based kinematic modelling as well as static modelling using Cosserat rod theory. It is shown that the experimental results match the theoretical results with an error margin of 2%. It is also shown that the optimization based approach is faster than the one based on Cosserat rod theory. We also present a three-fingered gripper prototype where each of the fingers are 3D printed continuum robots with general cable routing. It is demonstrated that the prototype can be used for gripping objects and for its manipulation.

## 개요
연속체 로봇은 변형과 형상 변화가 필요하면서도 유연성을 요구하는 응용 분야에서 점점 더 인기를 얻고 있습니다. 케이블 구동 연속체 로봇은 가장 일반적으로 사용되는 유형 중 하나입니다. 전형적인 케이블 구동 연속체 로봇은 유연한 백본(backbone)에 스페이서 디스크(spacer disk)가 부착되고, 고정된 베이스에서 자유 끝단까지 스페이서 디스크의 구멍을 통과하는 케이블로 구성됩니다. 대부분의 이러한 로봇에서 케이블의 경로는 직선이거나 부드러운 나선형 곡선입니다. 본 논문에서는 6가지 서로 다른 케이블 경로에 대해 3D 프린팅된 연속체 로봇의 실험적 및 이론적 변형을 분석합니다. 결과는 이산 최적화 기반 운동학적 모델링과 Cosserat rod 이론을 사용한 정적 모델링을 비교합니다. 실험 결과가 2%의 오차 범위 내에서 이론적 결과와 일치함을 보여줍니다. 또한 최적화 기반 접근 방식이 Cosserat rod 이론 기반 접근 방식보다 더 빠르다는 것을 보여줍니다. 또한 각 손가락이 일반적인 케이블 경로를 가진 3D 프린팅 연속체 로봇인 세 손가락 그리퍼 프로토타입을 제시합니다. 이 프로토타입이 물체를 잡고 조작하는 데 사용될 수 있음을 입증합니다.

## 핵심 내용
연속체 로봇은 변형과 형상 변화가 필요하면서도 유연성을 요구하는 응용 분야에서 점점 더 인기를 얻고 있습니다. 케이블 구동 연속체 로봇은 가장 일반적으로 사용되는 유형 중 하나입니다. 전형적인 케이블 구동 연속체 로봇은 유연한 백본(backbone)에 스페이서 디스크(spacer disk)가 부착되고, 고정된 베이스에서 자유 끝단까지 스페이서 디스크의 구멍을 통과하는 케이블로 구성됩니다. 대부분의 이러한 로봇에서 케이블의 경로는 직선이거나 부드러운 나선형 곡선입니다. 본 논문에서는 6가지 서로 다른 케이블 경로에 대해 3D 프린팅된 연속체 로봇의 실험적 및 이론적 변형을 분석합니다. 결과는 이산 최적화 기반 운동학적 모델링과 Cosserat rod 이론을 사용한 정적 모델링을 비교합니다. 실험 결과가 2%의 오차 범위 내에서 이론적 결과와 일치함을 보여줍니다. 또한 최적화 기반 접근 방식이 Cosserat rod 이론 기반 접근 방식보다 더 빠르다는 것을 보여줍니다. 또한 각 손가락이 일반적인 케이블 경로를 가진 3D 프린팅 연속체 로봇인 세 손가락 그리퍼 프로토타입을 제시합니다. 이 프로토타입이 물체를 잡고 조작하는 데 사용될 수 있음을 입증합니다.

## 参考
- http://arxiv.org/abs/2003.04593v1
