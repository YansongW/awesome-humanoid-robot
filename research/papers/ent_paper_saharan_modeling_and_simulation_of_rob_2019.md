---
$id: ent_paper_saharan_modeling_and_simulation_of_rob_2019
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Modeling and Simulation of Robotic Finger Powered by Nylon Artificial Muscles
    — Equations with Simulink Model
  zh: 尼龙人造肌肉驱动的机器人手指建模与仿真——含Simulink模型的方程
  ko: 나일론 인공근육으로 구동되는 로봇 손가락의 모델링 및 시뮬레이션 — Simulink 모델과 함께하는 방정식
summary:
  en: Presents a detailed Euler-Lagrangian dynamic model and a MATLAB/Simulink simulation
    of a three-link robotic finger actuated by twisted-and-coiled polymer (TCP) artificial
    muscles.
  zh: 提出了由扭转卷曲聚合物（TCP）人工肌肉驱动的三连杆机器人手指的详细欧拉-拉格朗日动力学模型及MATLAB/Simulink仿真。
  ko: 꼬임 및 코일형 폴리머(TCP) 인공근육으로 구동되는 3링크 로봇 손가락에 대한 상세한 오일러-라그랑주 동역학 모델과 MATLAB/Simulink
    시뮬레이션을 제시한다.
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
- tcp_muscle
- twisted_coiled_polymer
- artificial_muscle
- robotic_finger
- humanoid_hand
- simulink_model
- euler_lagrangian_dynamics
- dynamic_modeling
- 3d_printed_hand
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-01'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review of
    the full text before verification.
sources:
- id: src_001
  type: paper
  title: Modeling and Simulation of Robotic Finger Powered by Nylon Artificial Muscles-
    Equations with Simulink model
  url: https://arxiv.org/abs/1901.09486
  date: '2019'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---

## Overview

This paper develops a detailed dynamic model of a three-link robotic finger driven by twisted-and-coiled polymer (TCP) artificial muscles and implements the model in MATLAB/Simulink for numerical study. The prototype hand is a 3D-printed, lightweight and compact design actuated by silver-coated nylon TCP muscles, which are thermal actuators that contract when heated. The authors derive the finger dynamics using an Euler-Lagrangian formulation with velocity Jacobians, simplify the coupled equations by neglecting small Coriolis and off-diagonal inertia terms, and add velocity-proportional joint damping to improve numerical tractability.

The actuator force from a TCP muscle is distributed as joint torques across the metacarpophalangeal (MCP), proximal interphalangeal (PIP) and distal interphalangeal (DIP) joints through a tendon/cable transmission. The resulting Simulink block model allows simulation of finger joint motion for given input force and temperature profiles of the TCP actuator. The work is intended as a reusable modeling and simulation framework to support the design and control of low-cost, 3D-printed humanoid hands.

## Key Contributions

- Three-link robotic finger dynamic model based on Euler-Lagrangian equations.
- Simplified coupled equations by neglecting negligible Coriolis/off-diagonal inertia terms and adding joint damping.
- Torque distribution formulation linking TCP muscle force to MCP, PIP and DIP joint torques.
- MATLAB/Simulink block model for simulating finger joint motion driven by TCP actuators.

## Relevance to Humanoid Robotics

The paper directly supports scalable design and control of humanoid robot hands by providing a reusable dynamic modeling and simulation framework for low-cost, 3D-printed fingers actuated by artificial muscles. TCP muscles offer a lightweight and inexpensive alternative to conventional motors and pneumatic actuators, making them attractive for compact humanoid manipulation hardware. The Simulink implementation enables rapid numerical exploration of design parameters and control strategies before physical prototyping.

## References

- [Modeling and Simulation of Robotic Finger Powered by Nylon Artificial Muscles- Equations with Simulink model](https://arxiv.org/abs/1901.09486) (accessed 2026-07-01)
