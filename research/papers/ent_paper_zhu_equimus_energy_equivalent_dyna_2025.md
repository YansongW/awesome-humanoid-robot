---
$id: ent_paper_zhu_equimus_energy_equivalent_dyna_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EquiMus: Energy-Equivalent Dynamic Modeling and Simulation of Musculoskeletal Robots Driven by Linear Elastic Actuators'
  zh: EquiMus：线性弹性执行器驱动的肌肉骨骼机器人的能量等效动态建模与仿真
  ko: 'EquiMus: 선형 탄성 액추에이터로 구동되는 근골격 로봇의 에너지 등가 동적 모델링 및 시뮬레이션'
summary:
  en: This paper proposes EquiMus, an energy-equivalent dynamic modeling framework and MuJoCo-based simulator for musculoskeletal
    rigid-soft hybrid robots driven by linear elastic actuators, validated through simulations and real-world experiments
    on a pneumatic bionic robotic leg.
  zh: 该论文提出了 EquiMus，一种面向由线性弹性执行器驱动的肌肉骨骼刚柔混合机器人的能量等效动态建模与 MuJoCo 仿真框架，并通过气动仿生机器腿的仿真与真实实验验证其有效性。
  ko: 본 논문은 선형 탄성 액추에이터로 구동되는 근골격 강성-연성 하이브리드 로봇을 위한 에너지 등가 동적 모델링 및 MuJoCo 기반 시뮬레이션 프레임워크인 EquiMus를 제안하고, 공압식 생체 모방 로봇 다리의
    시뮬레이션 및 실제 실험을 통해 효과를 검증한다.
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
- equimus
- energy_equivalent_modeling
- lumped_mass_formulation
- mujoco_simulation
- musculoskeletal_robot
- linear_elastic_actuator
- soft_robotics
- pneumatic_artificial_muscle
- sim_to_real
- reinforcement_learning
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.07887v1.
sources:
- id: src_001
  type: paper
  title: 'EquiMus: Energy-Equivalent Dynamic Modeling and Simulation of Musculoskeletal Robots Driven by Linear Elastic Actuators'
  url: https://arxiv.org/abs/2511.07887
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
Dynamic modeling and control are critical for unleashing soft robots' potential, yet remain challenging due to their complex constitutive behaviors and real-world operating conditions. Bio-inspired musculoskeletal robots, which integrate rigid skeletons with soft actuators, combine high load-bearing capacity with inherent flexibility. Although actuation dynamics have been studied through experimental methods and surrogate models, accurate and effective modeling and simulation remain a significant challenge, especially for large-scale hybrid rigid--soft robots with continuously distributed mass, kinematic loops, and diverse motion modes. To address these challenges, we propose EquiMus, an energy-equivalent dynamic modeling framework and MuJoCo-based simulation for musculoskeletal rigid--soft hybrid robots with linear elastic actuators. The equivalence and effectiveness of the proposed approach are validated and examined through both simulations and real-world experiments on a bionic robotic leg. EquiMus further demonstrates its utility for downstream tasks, including controller design and learning-based control strategies.

## 核心内容
Dynamic modeling and control are critical for unleashing soft robots' potential, yet remain challenging due to their complex constitutive behaviors and real-world operating conditions. Bio-inspired musculoskeletal robots, which integrate rigid skeletons with soft actuators, combine high load-bearing capacity with inherent flexibility. Although actuation dynamics have been studied through experimental methods and surrogate models, accurate and effective modeling and simulation remain a significant challenge, especially for large-scale hybrid rigid--soft robots with continuously distributed mass, kinematic loops, and diverse motion modes. To address these challenges, we propose EquiMus, an energy-equivalent dynamic modeling framework and MuJoCo-based simulation for musculoskeletal rigid--soft hybrid robots with linear elastic actuators. The equivalence and effectiveness of the proposed approach are validated and examined through both simulations and real-world experiments on a bionic robotic leg. EquiMus further demonstrates its utility for downstream tasks, including controller design and learning-based control strategies.

## 参考
- http://arxiv.org/abs/2511.07887v1

## Overview
Dynamic modeling and control are critical for unleashing soft robots' potential, yet remain challenging due to their complex constitutive behaviors and real-world operating conditions. Bio-inspired musculoskeletal robots, which integrate rigid skeletons with soft actuators, combine high load-bearing capacity with inherent flexibility. Although actuation dynamics have been studied through experimental methods and surrogate models, accurate and effective modeling and simulation remain a significant challenge, especially for large-scale hybrid rigid--soft robots with continuously distributed mass, kinematic loops, and diverse motion modes. To address these challenges, we propose EquiMus, an energy-equivalent dynamic modeling framework and MuJoCo-based simulation for musculoskeletal rigid--soft hybrid robots with linear elastic actuators. The equivalence and effectiveness of the proposed approach are validated and examined through both simulations and real-world experiments on a bionic robotic leg. EquiMus further demonstrates its utility for downstream tasks, including controller design and learning-based control strategies.

## Content
Dynamic modeling and control are critical for unleashing soft robots' potential, yet remain challenging due to their complex constitutive behaviors and real-world operating conditions. Bio-inspired musculoskeletal robots, which integrate rigid skeletons with soft actuators, combine high load-bearing capacity with inherent flexibility. Although actuation dynamics have been studied through experimental methods and surrogate models, accurate and effective modeling and simulation remain a significant challenge, especially for large-scale hybrid rigid--soft robots with continuously distributed mass, kinematic loops, and diverse motion modes. To address these challenges, we propose EquiMus, an energy-equivalent dynamic modeling framework and MuJoCo-based simulation for musculoskeletal rigid--soft hybrid robots with linear elastic actuators. The equivalence and effectiveness of the proposed approach are validated and examined through both simulations and real-world experiments on a bionic robotic leg. EquiMus further demonstrates its utility for downstream tasks, including controller design and learning-based control strategies.

## 개요
동적 모델링 및 제어는 소프트 로봇의 잠재력을 발휘하는 데 중요하지만, 복잡한 구성적 거동과 실제 작동 조건으로 인해 여전히 어려운 과제로 남아 있습니다. 생체 모방 근골격 로봇은 강성 골격과 소프트 액추에이터를 통합하여 높은 하중 지지 능력과 고유한 유연성을 결합합니다. 실험적 방법과 대리 모델을 통해 작동 동역학이 연구되었지만, 특히 연속적으로 분포된 질량, 운동학적 폐쇄 루프 및 다양한 운동 모드를 가진 대규모 하이브리드 강성-소프트 로봇의 경우 정확하고 효과적인 모델링 및 시뮬레이션은 여전히 중요한 도전 과제입니다. 이러한 문제를 해결하기 위해 우리는 선형 탄성 액추에이터를 갖춘 근골격 강성-소프트 하이브리드 로봇을 위한 에너지 등가 동적 모델링 프레임워크이자 MuJoCo 기반 시뮬레이션인 EquiMus를 제안합니다. 제안된 접근 방식의 등가성과 효과성은 생체 모방 로봇 다리에 대한 시뮬레이션과 실제 실험을 통해 검증 및 조사되었습니다. EquiMus는 제어기 설계 및 학습 기반 제어 전략을 포함한 하위 작업에서도 그 유용성을 입증합니다.

## 핵심 내용
동적 모델링 및 제어는 소프트 로봇의 잠재력을 발휘하는 데 중요하지만, 복잡한 구성적 거동과 실제 작동 조건으로 인해 여전히 어려운 과제로 남아 있습니다. 생체 모방 근골격 로봇은 강성 골격과 소프트 액추에이터를 통합하여 높은 하중 지지 능력과 고유한 유연성을 결합합니다. 실험적 방법과 대리 모델을 통해 작동 동역학이 연구되었지만, 특히 연속적으로 분포된 질량, 운동학적 폐쇄 루프 및 다양한 운동 모드를 가진 대규모 하이브리드 강성-소프트 로봇의 경우 정확하고 효과적인 모델링 및 시뮬레이션은 여전히 중요한 도전 과제입니다. 이러한 문제를 해결하기 위해 우리는 선형 탄성 액추에이터를 갖춘 근골격 강성-소프트 하이브리드 로봇을 위한 에너지 등가 동적 모델링 프레임워크이자 MuJoCo 기반 시뮬레이션인 EquiMus를 제안합니다. 제안된 접근 방식의 등가성과 효과성은 생체 모방 로봇 다리에 대한 시뮬레이션과 실제 실험을 통해 검증 및 조사되었습니다. EquiMus는 제어기 설계 및 학습 기반 제어 전략을 포함한 하위 작업에서도 그 유용성을 입증합니다.
