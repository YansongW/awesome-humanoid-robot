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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2003.04593v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (626 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2003.04593v1

## 개요
연속체 로봇은 변형과 환경 적응 능력 덕분에 점점 더 인기를 얻고 있으며, 그중에서도 케이블 구동 방식이 가장 일반적입니다. 기존 로봇의 케이블 라우팅은 주로 직선 또는 부드러운 나선형 곡선이었지만, 본 논문에서는 여섯 가지 일반적인 라우팅 방식을 탐구합니다. 3D 프린팅 로봇을 이용한 실험을 통해 이산 최적화 운동학 모델과 Cosserat rod 정역학 모델의 이론적 예측을 비교했으며, 두 모델 모두 실험 결과와의 오차가 2% 미만임을 발견했고, 최적화 방법이 계산 속도가 더 빠른 것으로 나타났습니다. 또한, 이 설계를 기반으로 제작된 세 손가락 그리퍼 프로토타입이 물체를 성공적으로 잡고 조작하는 데 성공했습니다.

## 핵심 내용
### 방법 및 구조
- 로봇 구조: 유연한 골격을 사용하며, 간격을 두고 디스크가 부착되고, 케이블이 고정 베이스에서 디스크 구멍을 통과해 자유 끝단까지 도달합니다.
- 케이블 라우팅: 기존의 직선 또는 부드러운 나선형 곡선과는 다른 여섯 가지 일반적인 라우팅 방식을 연구했습니다.
- 모델링 방법:
  - **이산 최적화 운동학 모델**: 분할 상수 곡률 가정을 기반으로 최적화를 통해 변형을 해결합니다.
  - **Cosserat rod 정역학 모델**: 막대의 굽힘, 비틀림 및 전단을 고려하여 평형 방정식을 해결합니다.

### 실험 설정
- 3D 프린터로 연속체 로봇 프로토타입을 제작하고, 여섯 가지 케이블 라우팅에서의 변형을 테스트했습니다.
- 실험 변형을 측정하고 두 모델의 이론적 예측과 비교했습니다.

### 주요 결과
- 두 모델의 예측과 실험 결과의 오차는 모두 로봇 길이의 2% 이내였습니다.
- 이산 최적화 방법은 Cosserat rod 방법보다 계산 속도가 현저히 빨랐습니다.
- 세 손가락 그리퍼 프로토타입(각 손가락이 일반 라우팅을 사용하는 3D 프린팅 연속체 로봇)이 물체를 성공적으로 잡고 조작했습니다.

### 결론
본 논문은 3D 프린팅 연속체 로봇에서 일반적인 케이블 라우팅의 실현 가능성을 검증하고, 빠르고 정확한 모델링 방법을 제공하며, 그리퍼에서의 응용 가능성을 보여주었습니다.
