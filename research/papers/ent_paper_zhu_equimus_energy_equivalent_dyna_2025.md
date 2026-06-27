---
$id: ent_paper_zhu_equimus_energy_equivalent_dyna_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EquiMus: Energy-Equivalent Dynamic Modeling and Simulation of Musculoskeletal
    Robots Driven by Linear Elastic Actuators'
  zh: EquiMus：线性弹性执行器驱动的肌肉骨骼机器人的能量等效动态建模与仿真
  ko: 'EquiMus: 선형 탄성 액추에이터로 구동되는 근골격 로봇의 에너지 등가 동적 모델링 및 시뮬레이션'
summary:
  en: This paper proposes EquiMus, an energy-equivalent dynamic modeling framework
    and MuJoCo-based simulator for musculoskeletal rigid-soft hybrid robots driven
    by linear elastic actuators, validated through simulations and real-world experiments
    on a pneumatic bionic robotic leg.
  zh: 该论文提出了 EquiMus，一种面向由线性弹性执行器驱动的肌肉骨骼刚柔混合机器人的能量等效动态建模与 MuJoCo 仿真框架，并通过气动仿生机器腿的仿真与真实实验验证其有效性。
  ko: 본 논문은 선형 탄성 액추에이터로 구동되는 근골격 강성-연성 하이브리드 로봇을 위한 에너지 등가 동적 모델링 및 MuJoCo 기반 시뮬레이션
    프레임워크인 EquiMus를 제안하고, 공압식 생체 모방 로봇 다리의 시뮬레이션 및 실제 실험을 통해 효과를 검증한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from arXiv abstract and supplied metadata; requires human review
    before full verification.
sources:
- id: src_001
  type: paper
  title: 'EquiMus: Energy-Equivalent Dynamic Modeling and Simulation of Musculoskeletal
    Robots Driven by Linear Elastic Actuators'
  url: https://arxiv.org/abs/2511.07887
  date: '2025'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---

## Overview

Dynamic modeling and control are critical for soft robots, but their complex constitutive behaviors and real-world operating conditions make accurate simulation difficult. Bio-inspired musculoskeletal robots that combine rigid skeletons with soft actuators offer high load capacity and flexibility, yet large-scale hybrid rigid-soft systems with continuously distributed mass, kinematic loops, and diverse motion modes remain hard to model efficiently. This paper introduces EquiMus, an energy-equivalent dynamic modeling framework together with a MuJoCo-based simulator for musculoskeletal rigid-soft hybrid robots driven by linear elastic actuators.

The core idea is to map the dynamics of elastic actuators to discrete rigid-body elements in an energy-equivalent way, preserving energies and matching the virtual work of damping and actuation. The implementation supports loop-closure constraints, smooth elastic actuator dynamics, and compatibility with reinforcement learning toolchains. The equivalence and effectiveness of the approach are examined through simulations and real-world experiments on a pneumatic bionic robotic leg. The authors further demonstrate downstream utility for tasks such as PID auto-tuning, model-based control, and reinforcement-learning-based control.

## Key Contributions

- Energy-equivalent lumped-mass formulation that maps elastic actuator dynamics to discrete rigid-body elements while preserving energies and matching the virtual work of damping and actuation.
- MuJoCo-based implementation supporting loop-closure constraints, smooth elastic actuator dynamics, and out-of-the-box reinforcement learning compatibility.
- Validation through simulations and real-world experiments on a pneumatic bionic robotic leg.
- Demonstration of downstream utility for PID auto-tuning, model-based control, and reinforcement learning-based control.

## Relevance to Humanoid Robotics

EquiMus directly addresses a key bottleneck for humanoid and bio-inspired articulated systems: accurate, real-time dynamic modeling of legs and other limbs that combine rigid links with compliant actuators. By enabling energy-equivalent simulation of linear elastic actuators within a standard physics engine, the framework supports controller design and sim-to-real transfer for musculoskeletal humanoid legs. Its reinforcement-learning compatibility also makes it relevant to learning-based locomotion and manipulation policies for humanoid robots.
