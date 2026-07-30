---
$id: ent_paper_arachchige_dynamic_modeling_and_validatio_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Dynamic Modeling and Validation of Soft Robotic Snake Locomotion
  zh: 软体机器蛇运动的动态建模与验证
  ko: 소프트 로봇 뱀 보행의 동적 모델링 및 검증
summary:
  en: Presents a complete spatial dynamic model of a pneumatic soft robotic snake using a floating-base kinematic skin representation
    and distributed contact dynamics, and validates planar and spatial rolling gaits numerically and experimentally.
  zh: 本文提出了一种用于气动软体蛇形机器人的完整空间动力学模型，该模型采用浮动基座运动学皮肤表示和分布式接触动力学，并通过数值模拟和实验验证了平面与空间滚动步态的有效性。
  ko: 부유 기반 운동학적 피부 표현과 분산 접촉 역학을 활용한 공압식 소프트 로봇 뱀의 완전한 공간 동적 모델을 제시하고, 평면 및 공간 롤링 보행을 수치적으로 그리고 실험적으로 검증한다.
domains:
- 06_design_engineering
- 02_components
layers:
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- soft_robotics
- snake_robot
- continuum_robotics
- pneumatic_artificial_muscles
- mckibben_muscles
- dynamic_modeling
- distributed_contact_dynamics
- floating_base
- recursive_lagrangian
- rolling_gait
- locomotion
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.02291v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Dynamic Modeling and Validation of Soft Robotic Snake Locomotion
  url: https://arxiv.org/abs/2303.02291
  date: '2023'
  accessed_at: '2026-06-28'
theoretical_depth:
- formalism
- method
---
## 概述
软体蛇形机器人由柔性材料制成，能连续变形身体，比刚性机器人更逼真地模仿生物蛇的灵活步态。然而，目前软体蛇形机器人缺乏轮式支撑，仅限于平面步态。由于蛇的 locomotion 源于皮肤与地面分布式接触产生的反作用力，因此需要高效的动力学模型来研究步态。本文提出的模型结合了浮动基座运动学与分布式接触动力学，用于气动软体蛇形机器人，并通过数值评估和实验验证了平面与空间滚动步态的可行性。

## 核心内容
### 方法
- 采用浮动基座运动学模型，将软体蛇形机器人的身体表示为连续可变形皮肤，并集成分布式接触动力学。
- 模型针对气动驱动软体蛇形机器人设计，能够捕捉身体与地面之间的接触力分布。

### 实验设置
- 数值评估：使用所提模型模拟平面和空间滚动步态，分析其可行性。
- 实验验证：在软体蛇形机器人原型上执行对应的步态轨迹，并与数值结果进行对比。

### 关键结果
- 数值与实验结果的定性和定量比较证实了动力学模型的有效性。
- 模型成功预测了平面步态和空间滚动步态的运动轨迹，为软体蛇形机器人的步态设计提供了可靠工具。

### 结论
- 该动力学模型填补了软体蛇形机器人空间步态研究的空白，通过分布式接触力建模提升了步态模拟的准确性。

## Overview
Soft robotic snakes made of compliant materials can continuously deform their bodies and, therefore, mimic the biological snakes' flexible and agile locomotion gaits better than their rigid-bodied counterparts. Without wheel support, to date, soft robotic snakes are limited to emulating planar locomotion gaits, which are derived via kinematic modeling and tested on robotic prototypes. Given that the snake locomotion results from the reaction forces due to the distributed contact between their skin and the ground, it is essential to investigate the locomotion gaits through efficient dynamic models capable of accommodating distributed contact forces. We present a complete spatial dynamic model that utilizes a floating-base kinematic model with distributed contact dynamics for a pneumatically powered soft robotic snake. We numerically evaluate the feasibility of the planar and spatial rolling gaits utilizing the proposed model and experimentally validate the corresponding locomotion gait trajectories on a soft robotic snake prototype. We qualitatively and quantitatively compare the numerical and experimental results which confirm the validity of the proposed dynamic model.

## 개요
연성 재료로 만들어진 소프트 로봇 뱀은 몸체를 연속적으로 변형할 수 있어, 강체 기반의 로봇보다 생물학적 뱀의 유연하고 민첩한 이동 보행을 더 잘 모방할 수 있습니다. 바퀴 지지대 없이, 현재까지 소프트 로봇 뱀은 운동학적 모델링을 통해 도출되고 로봇 프로토타입에서 테스트된 평면 이동 보행을 모방하는 데 제한되어 있습니다. 뱀의 이동이 피부와 지면 사이의 분산 접촉으로 인한 반력에서 비롯된다는 점을 고려할 때, 분산 접촉력을 수용할 수 있는 효율적인 동적 모델을 통해 이동 보행을 연구하는 것이 필수적입니다. 우리는 공압으로 구동되는 소프트 로봇 뱀을 위해 분산 접촉 동역학을 갖춘 부동 기저 운동학 모델을 활용하는 완전한 공간 동적 모델을 제시합니다. 제안된 모델을 사용하여 평면 및 공간 롤링 보행의 실현 가능성을 수치적으로 평가하고, 소프트 로봇 뱀 프로토타입에서 해당 이동 보행 궤적을 실험적으로 검증합니다. 수치적 결과와 실험적 결과를 정성적 및 정량적으로 비교하여 제안된 동적 모델의 타당성을 확인합니다.

## 핵심 내용
연성 재료로 만들어진 소프트 로봇 뱀은 몸체를 연속적으로 변형할 수 있어, 강체 기반의 로봇보다 생물학적 뱀의 유연하고 민첩한 이동 보행을 더 잘 모방할 수 있습니다. 바퀴 지지대 없이, 현재까지 소프트 로봇 뱀은 운동학적 모델링을 통해 도출되고 로봇 프로토타입에서 테스트된 평면 이동 보행을 모방하는 데 제한되어 있습니다. 뱀의 이동이 피부와 지면 사이의 분산 접촉으로 인한 반력에서 비롯된다는 점을 고려할 때, 분산 접촉력을 수용할 수 있는 효율적인 동적 모델을 통해 이동 보행을 연구하는 것이 필수적입니다. 우리는 공압으로 구동되는 소프트 로봇 뱀을 위해 분산 접촉 동역학을 갖춘 부동 기저 운동학 모델을 활용하는 완전한 공간 동적 모델을 제시합니다. 제안된 모델을 사용하여 평면 및 공간 롤링 보행의 실현 가능성을 수치적으로 평가하고, 소프트 로봇 뱀 프로토타입에서 해당 이동 보행 궤적을 실험적으로 검증합니다. 수치적 결과와 실험적 결과를 정성적 및 정량적으로 비교하여 제안된 동적 모델의 타당성을 확인합니다.

## 参考
- http://arxiv.org/abs/2303.02291v1
