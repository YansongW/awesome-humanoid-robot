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
  en: Sartore, Rapetti, and Pucci formulate a nonlinear hardware-design optimization of humanoid link geometry and density
    to minimize agents' energy expenditure during collaborative payload lifting, then apply the method to evolve the iCub
    design into the ergoCub humanoid, extending the ergonomic payload height range and reducing robot energy expenditure by
    about 33%.
  zh: Sartore、Rapetti和Pucci将人形机器人连杆几何与密度作为设计变量，建立考虑人体模型的非线性优化问题以最小化协同搬运中的能量消耗，并将该方法应用于从iCub到ergoCub的设计，扩展了人机工效工作高度范围，同时使机器人能耗降低约33%。
  ko: Sartore, Rapetti, Pucci는 인간 모델을 포함한 비선형 하드웨어 설계 최적화 문제를 제안하여 협업 하중 리프팅에서 작업자들의 에너지 소비를 최소화하고, 이를 iCub에서 ergoCub 휴머노이드
    설계에 적용하여 인체공학적 작업 높이 범위를 확장하고 로봇 에너지 소비를 약 33% 감소시켰다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2211.13503v1.
sources:
- id: src_001
  type: paper
  title: Optimization of Humanoid Robot Designs for Human-Robot Ergonomic Payload Lifting
  url: https://arxiv.org/abs/2211.13503
  date: '2022'
  accessed_at: '2026-06-25'
theoretical_depth:
- system
---
## 概述
When a human and a humanoid robot collaborate physically, ergonomics is a key factor to consider. Assuming a given humanoid robot, several control architectures exist nowadays to address ergonomic physical human-robot collaboration. This paper takes one step further by considering robot hardware parameters as optimization variables in the problem of collaborative payload lifting. The variables that parametrize robot's kinematics and dynamics ensure their physical consistency, and the human model is considered in the optimization problem. By leveraging the proposed modelling framework, the ergonomy of the interaction is maximized, here given by the agents' energy expenditure. Robot kinematic, dynamics, hardware constraints and human geometries are considered when solving the associated optimization problem. The proposed methodology is used to identify optimum hardware parameters for the design of the ergoCub robot, a humanoid possessing a degree of embodied intelligence for ergonomic interaction with humans. For the optimization problem, the starting point is the iCub humanoid robot. The obtained robot design reaches loads at heights in the range of 0.8-1.5 m with respect to the iCub robot whose range is limited to 0.8-1.2 m. The robot energy expenditure is decreased by about 33%, meanwhile, the human ergonomy is preserved, leading overall to an improved interaction.

## 核心内容
When a human and a humanoid robot collaborate physically, ergonomics is a key factor to consider. Assuming a given humanoid robot, several control architectures exist nowadays to address ergonomic physical human-robot collaboration. This paper takes one step further by considering robot hardware parameters as optimization variables in the problem of collaborative payload lifting. The variables that parametrize robot's kinematics and dynamics ensure their physical consistency, and the human model is considered in the optimization problem. By leveraging the proposed modelling framework, the ergonomy of the interaction is maximized, here given by the agents' energy expenditure. Robot kinematic, dynamics, hardware constraints and human geometries are considered when solving the associated optimization problem. The proposed methodology is used to identify optimum hardware parameters for the design of the ergoCub robot, a humanoid possessing a degree of embodied intelligence for ergonomic interaction with humans. For the optimization problem, the starting point is the iCub humanoid robot. The obtained robot design reaches loads at heights in the range of 0.8-1.5 m with respect to the iCub robot whose range is limited to 0.8-1.2 m. The robot energy expenditure is decreased by about 33%, meanwhile, the human ergonomy is preserved, leading overall to an improved interaction.

## 参考
- http://arxiv.org/abs/2211.13503v1

