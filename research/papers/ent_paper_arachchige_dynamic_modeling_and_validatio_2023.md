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
  zh: Soft robotic snakes made of compliant materials can continuously deform their bodies and, therefore, mimic the biological
    snakes' flexible and agile locomotion gaits better than their rigid-bodied counterparts. Without wheel support, to date,
    soft robotic snakes are limited to emulating planar locomotion gaits, which are derived via kinematic modeling and tested
    on robotic prototypes. Given that the snake locomotion results from the reaction forces due to the distributed contact
    between their skin and the ground, it is essential to investigate the locomotion gaits through efficient dynamic mod
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

## Overview
Soft robotic snakes made of compliant materials can continuously deform their bodies and, therefore, mimic the biological snakes' flexible and agile locomotion gaits better than their rigid-bodied counterparts. Without wheel support, to date, soft robotic snakes are limited to emulating planar locomotion gaits, which are derived via kinematic modeling and tested on robotic prototypes. Given that the snake locomotion results from the reaction forces due to the distributed contact between their skin and the ground, it is essential to investigate the locomotion gaits through efficient dynamic models capable of accommodating distributed contact forces. We present a complete spatial dynamic model that utilizes a floating-base kinematic model with distributed contact dynamics for a pneumatically powered soft robotic snake. We numerically evaluate the feasibility of the planar and spatial rolling gaits utilizing the proposed model and experimentally validate the corresponding locomotion gait trajectories on a soft robotic snake prototype. We qualitatively and quantitatively compare the numerical and experimental results which confirm the validity of the proposed dynamic model.

## Content
Soft robotic snakes made of compliant materials can continuously deform their bodies and, therefore, mimic the biological snakes' flexible and agile locomotion gaits better than their rigid-bodied counterparts. Without wheel support, to date, soft robotic snakes are limited to emulating planar locomotion gaits, which are derived via kinematic modeling and tested on robotic prototypes. Given that the snake locomotion results from the reaction forces due to the distributed contact between their skin and the ground, it is essential to investigate the locomotion gaits through efficient dynamic models capable of accommodating distributed contact forces. We present a complete spatial dynamic model that utilizes a floating-base kinematic model with distributed contact dynamics for a pneumatically powered soft robotic snake. We numerically evaluate the feasibility of the planar and spatial rolling gaits utilizing the proposed model and experimentally validate the corresponding locomotion gait trajectories on a soft robotic snake prototype. We qualitatively and quantitatively compare the numerical and experimental results which confirm the validity of the proposed dynamic model.

## 개요
연성 재료로 만들어진 소프트 로봇 뱀은 몸체를 연속적으로 변형할 수 있어, 강체 기반의 로봇보다 생물학적 뱀의 유연하고 민첩한 이동 보행을 더 잘 모방할 수 있습니다. 바퀴 지지대 없이, 현재까지 소프트 로봇 뱀은 운동학적 모델링을 통해 도출되고 로봇 프로토타입에서 테스트된 평면 이동 보행을 모방하는 데 제한되어 있습니다. 뱀의 이동이 피부와 지면 사이의 분산 접촉으로 인한 반력에서 비롯된다는 점을 고려할 때, 분산 접촉력을 수용할 수 있는 효율적인 동적 모델을 통해 이동 보행을 연구하는 것이 필수적입니다. 우리는 공압으로 구동되는 소프트 로봇 뱀을 위해 분산 접촉 동역학을 갖춘 부동 기저 운동학 모델을 활용하는 완전한 공간 동적 모델을 제시합니다. 제안된 모델을 사용하여 평면 및 공간 롤링 보행의 실현 가능성을 수치적으로 평가하고, 소프트 로봇 뱀 프로토타입에서 해당 이동 보행 궤적을 실험적으로 검증합니다. 수치적 결과와 실험적 결과를 정성적 및 정량적으로 비교하여 제안된 동적 모델의 타당성을 확인합니다.

## 핵심 내용
연성 재료로 만들어진 소프트 로봇 뱀은 몸체를 연속적으로 변형할 수 있어, 강체 기반의 로봇보다 생물학적 뱀의 유연하고 민첩한 이동 보행을 더 잘 모방할 수 있습니다. 바퀴 지지대 없이, 현재까지 소프트 로봇 뱀은 운동학적 모델링을 통해 도출되고 로봇 프로토타입에서 테스트된 평면 이동 보행을 모방하는 데 제한되어 있습니다. 뱀의 이동이 피부와 지면 사이의 분산 접촉으로 인한 반력에서 비롯된다는 점을 고려할 때, 분산 접촉력을 수용할 수 있는 효율적인 동적 모델을 통해 이동 보행을 연구하는 것이 필수적입니다. 우리는 공압으로 구동되는 소프트 로봇 뱀을 위해 분산 접촉 동역학을 갖춘 부동 기저 운동학 모델을 활용하는 완전한 공간 동적 모델을 제시합니다. 제안된 모델을 사용하여 평면 및 공간 롤링 보행의 실현 가능성을 수치적으로 평가하고, 소프트 로봇 뱀 프로토타입에서 해당 이동 보행 궤적을 실험적으로 검증합니다. 수치적 결과와 실험적 결과를 정성적 및 정량적으로 비교하여 제안된 동적 모델의 타당성을 확인합니다.
