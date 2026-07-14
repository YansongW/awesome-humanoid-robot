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
  zh: 提出了一种采用浮动基座运动学表皮表示与分布式接触动力学的气动软体机器蛇完整空间动力学模型，并通过数值仿真与实验验证了平面和空间滚动步态。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2303.02291v1.
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
Soft robotic snakes made of compliant materials can continuously deform their bodies and, therefore, mimic the biological snakes' flexible and agile locomotion gaits better than their rigid-bodied counterparts. Without wheel support, to date, soft robotic snakes are limited to emulating planar locomotion gaits, which are derived via kinematic modeling and tested on robotic prototypes. Given that the snake locomotion results from the reaction forces due to the distributed contact between their skin and the ground, it is essential to investigate the locomotion gaits through efficient dynamic models capable of accommodating distributed contact forces. We present a complete spatial dynamic model that utilizes a floating-base kinematic model with distributed contact dynamics for a pneumatically powered soft robotic snake. We numerically evaluate the feasibility of the planar and spatial rolling gaits utilizing the proposed model and experimentally validate the corresponding locomotion gait trajectories on a soft robotic snake prototype. We qualitatively and quantitatively compare the numerical and experimental results which confirm the validity of the proposed dynamic model.

## 核心内容
Soft robotic snakes made of compliant materials can continuously deform their bodies and, therefore, mimic the biological snakes' flexible and agile locomotion gaits better than their rigid-bodied counterparts. Without wheel support, to date, soft robotic snakes are limited to emulating planar locomotion gaits, which are derived via kinematic modeling and tested on robotic prototypes. Given that the snake locomotion results from the reaction forces due to the distributed contact between their skin and the ground, it is essential to investigate the locomotion gaits through efficient dynamic models capable of accommodating distributed contact forces. We present a complete spatial dynamic model that utilizes a floating-base kinematic model with distributed contact dynamics for a pneumatically powered soft robotic snake. We numerically evaluate the feasibility of the planar and spatial rolling gaits utilizing the proposed model and experimentally validate the corresponding locomotion gait trajectories on a soft robotic snake prototype. We qualitatively and quantitatively compare the numerical and experimental results which confirm the validity of the proposed dynamic model.

## 参考
- http://arxiv.org/abs/2303.02291v1

