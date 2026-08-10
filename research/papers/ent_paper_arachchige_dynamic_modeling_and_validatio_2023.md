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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.02291v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (532 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2303.02291v1

## 개요
소프트 뱀 로봇은 유연한 재료로 제작되어 몸체를 연속적으로 변형할 수 있으며, 강체 로봇보다 생물학적 뱀의 유연한 보행을 더 사실적으로 모방합니다. 그러나 현재 소프트 뱀 로봇은 바퀴 지지대가 없어 평면 보행에 국한되어 있습니다. 뱀의 운동은 피부와 지면 사이의 분산 접촉에서 발생하는 반작용력에서 비롯되므로, 보행을 연구하기 위한 효율적인 동역학 모델이 필요합니다. 본 논문에서 제안하는 모델은 부동 베이스 운동학과 분산 접촉 동역학을 결합하여 공압 소프트 뱀 로봇에 적용하며, 수치 평가와 실험을 통해 평면 및 공간 구름 보행의 실현 가능성을 검증합니다.

## 핵심 내용
### 방법
- 부동 베이스 운동학 모델을 채택하여 소프트 뱀 로봇의 몸체를 연속적으로 변형 가능한 피부로 표현하고, 분산 접촉 동역학을 통합합니다.
- 모델은 공압 구동 소프트 뱀 로봇을 위해 설계되었으며, 몸체와 지면 사이의 접촉력 분포를 포착할 수 있습니다.

### 실험 설정
- 수치 평가: 제안된 모델을 사용하여 평면 및 공간 구름 보행을 시뮬레이션하고 그 실현 가능성을 분석합니다.
- 실험 검증: 소프트 뱀 로봇 프로토타입에서 해당 보행 궤적을 실행하고 수치 결과와 비교합니다.

### 주요 결과
- 수치 및 실험 결과의 정성적·정량적 비교를 통해 동역학 모델의 유효성을 확인했습니다.
- 모델은 평면 보행과 공간 구름 보행의 운동 궤적을 성공적으로 예측하여, 소프트 뱀 로봇의 보행 설계를 위한 신뢰할 수 있는 도구를 제공합니다.

### 결론
- 이 동역학 모델은 소프트 뱀 로봇의 공간 보행 연구의 공백을 메우며, 분산 접촉력 모델링을 통해 보행 시뮬레이션의 정확성을 향상시킵니다.
