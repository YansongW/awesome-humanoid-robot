---
$id: ent_paper_sartore_optimization_of_humanoid_robot_2022
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting
  zh: 面向人机工效协作负载提升的人形机器人设计优化
  ko: 인간-로봇 인체공학적 하중 리프팅을 위한 휴머노이드 로봇 설계 최적화
summary:
  en: Sartore, Rapetti, and Pucci formulate a nonlinear hardware-design optimization
    of humanoid link geometry and density to minimize agents' energy expenditure during
    collaborative payload lifting, then apply the method to evolve the iCub design
    into the ergoCub humanoid, extending the ergonomic payload height range and reducing
    robot energy expenditure by about 33%.
  zh: Sartore、Rapetti和Pucci将人形机器人连杆几何与密度作为设计变量，建立考虑人体模型的非线性优化问题以最小化协同搬运中的能量消耗，并将该方法应用于从iCub到ergoCub的设计，扩展了人机工效工作高度范围，同时使机器人能耗降低约33%。
  ko: Sartore, Rapetti, Pucci는 인간 모델을 포함한 비선형 하드웨어 설계 최적화 문제를 제안하여 협업 하중 리프팅에서 작업자들의
    에너지 소비를 최소화하고, 이를 iCub에서 ergoCub 휴머노이드 설계에 적용하여 인체공학적 작업 높이 범위를 확장하고 로봇 에너지 소비를
    약 33% 감소시켰다.
domains:
- 06_design_engineering
- 02_components
- 11_applications_markets
layers:
- midstream
- upstream
- validation_markets
functional_roles:
- knowledge
- intelligence
- system
tags:
- ergonomic_collaboration
- payload_lifting
- hardware_optimization
- humanoid_design
- energy_expenditure
- physical_human_robot_interaction
- ergocub
- icub
- link_geometry
- density_parameterization
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-06-25'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full paper not independently
    retrieved. Human review recommended before final verification.
sources:
- id: src_001
  type: paper
  title: Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload
    Lifting
  url: https://arxiv.org/abs/2211.13503
  date: '2022'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---



## Overview

This paper treats humanoid robot hardware parameters—specifically link geometry and density—as optimization variables for ergonomic physical human-robot collaboration. It develops a physically consistent parametrization of robot kinematics and dynamics and embeds it, together with a human model, into a coupled human-robot-payload dynamic model. A nonlinear optimization problem is then formulated to minimize the agents' energy expenditure, represented by joint torques, while respecting kinematic, dynamic, hardware, and human-geometric constraints. The work moves beyond prior control-only approaches by co-designing the robot's body with the collaboration task.

The authors apply the proposed framework to the design of the ergoCub humanoid, taking the existing iCub robot as the starting point. The optimized design is reported to extend the collaborative payload-lifting height range from 0.8–1.2 m (iCub) to 0.8–1.5 m (ergoCub), while reducing robot energy expenditure by approximately 33% and preserving human ergonomics. The study focuses on static equilibrium configurations rather than the full dynamic trajectory of lifting.

## Key Contributions

- Physically consistent hardware parametrization of humanoid robot kinematics and dynamics using link geometry and density variables.
- Coupled human-robot-payload dynamic model that explicitly includes robot hardware parameters and a human model.
- Nonlinear optimization formulation that minimizes agents' joint torques/energy expenditure subject to kinematic, dynamic, hardware, and human-geometric constraints.
- Application of the methodology to evolve the iCub robot design into the ergoCub humanoid for ergonomic interaction.
- Simulation validation reporting an extended payload height range (0.8–1.5 m) and roughly 33% reduction in robot energy expenditure while preserving human ergonomics.

## Relevance to Humanoid Robotics

The paper is directly relevant to humanoid robotics because it addresses the hardware-level design of humanoids intended to work alongside humans in industrial and healthcare settings. By optimizing link geometry and density for ergonomic payload lifting, it provides a principled approach to embodied intelligence for physical human-robot collaboration. The resulting ergoCub design illustrates how humanoid morphology can be co-optimized with collaborative tasks, a concern that becomes more important as humanoids are deployed in real-world applications requiring safe and efficient interaction with people.
