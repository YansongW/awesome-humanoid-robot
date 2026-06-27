---
$id: ent_paper_ficht_nimbro_op2x_adult_sized_open_s_2018
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'NimbRo-OP2X: Adult-sized Open-source 3D Printed Humanoid Robot'
  zh: NimbRo-OP2X：成人尺寸开源3D打印人形机器人
  ko: 'NimbRo-OP2X: 성인 크기 오픈소스 3D 프린팅 휴머노이드 로봇'
summary:
  en: NimbRo-OP2X is a 135 cm, 19 kg open-source adult-sized humanoid robot built
    with 3D-printed parts and commercial off-the-shelf actuators, integrating GPU-accelerated
    onboard computing, a deep-learning vision system, and simulation-assisted gait
    optimization; it won all awards in the Humanoid AdultSize class at RoboCup 2018.
  zh: NimbRo-OP2X 是一款身高135厘米、重19公斤的开源成人尺寸人形机器人，采用3D打印部件和商用执行器，集成GPU加速的机载计算、深度学习视觉系统以及仿真辅助的步态优化，并在2018年机器人世界杯人形成人组比赛中获得所有奖项。
  ko: NimbRo-OP2X는 키 135cm, 무게 19kg의 오픈소스 성인 크기 휴머노이드 로봇으로, 3D 프린팅 부품과 상용 액추에이터를 사용하고
    GPU 가속 온보드 컴퓨팅, 딥러닝 비전 시스템 및 시뮬레이션 보조 보행 최적화를 통합했으며 2018년 로보컵 휴머노이드 성인부에서 모든 상을
    수상했다.
domains:
- 02_components
- 06_design_engineering
- 07_ai_models_algorithms
layers:
- intelligence
- midstream
- upstream
functional_roles:
- knowledge
- system
tags:
- nimbro_op2x
- adult_size_humanoid
- open_source_hardware
- 3d_printed_robot
- humanoid_platform
- robocup
- dynamixel_xm540
- gazebo_simulation
- bayesian_optimization
- resnet_18
- robot_soccer_vision
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-06-26'
  confidence: medium
  notes: AI-extracted from supplied metadata and abstract; full-text verification
    is needed before promotion to verified.
sources:
- id: src_001
  type: paper
  title: 'NimbRo-OP2X: Adult-sized Open-source 3D Printed Humanoid Robot'
  url: https://arxiv.org/abs/1810.08395
  date: '2018'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---

## Overview

NimbRo-OP2X is an adult-sized humanoid robot developed to address the shortage of capable, affordable, and open humanoid platforms. Standing 135 cm tall and weighing only 19 kg, the robot is large enough to operate in human-scale environments while remaining light enough to be carried and operated without special equipment. Its mechanical structure relies heavily on 3D-printed parts and commercial off-the-shelf actuators, with the stated goals of low cost, rapid reproducibility, and safe operation.

The platform integrates an Intel Core i7-8700T CPU and an Nvidia GTX 1050 Ti GPU on a Z370 Chipset Mini-ITX mainboard, providing substantial onboard compute for vision and control. The paper reports a deep-learning based visual perception system built around a ResNet-18 encoder-decoder architecture for real-time object detection in robot soccer, and a sample-efficient Bayesian optimization procedure that combines Gazebo simulations with real-robot experiments to tune gait parameters. The hardware designs and software are released open source to support reproducibility and community extension.

During RoboCup 2018 in Montréal, Canada, the NimbRo-OP2X was reportedly evaluated in the Humanoid AdultSize soccer competition and technical challenges, where it won all possible awards in its class. The authors position the platform as a practical research vehicle for real-world humanoid robotics.

## Key Contributions

- Design and realization of a low-cost, adult-sized, lightweight, open-source 3D-printed humanoid robot.
- Integration of intelligent Robotis Dynamixel XM-540 actuators and GPU-enabled onboard computing (Intel Core i7-8700T and Nvidia GTX 1050 Ti).
- Deep-learning based visual perception system using a ResNet-18 encoder-decoder architecture for real-time object detection in robot soccer.
- Sample-efficient Bayesian optimization approach combining Gazebo simulations and real-robot experiments for gait parameter tuning.
- Open-source release of hardware designs and software to foster accelerated real-world humanoid robotics research.

## Relevance to Humanoid Robotics

NimbRo-OP2X is directly relevant to the humanoid-robot knowledge base because it provides a complete, adult-sized, open-source platform that lowers the barrier to developing and deploying human-scale robots. By combining lightweight 3D-printed construction with off-the-shelf actuators and onboard GPU acceleration, the paper illustrates how hardware-software co-design can yield a practical research platform for dynamic locomotion, perception, and behavior generation.

The reported methods—deep-learning vision, simulation-to-real gait optimization, and open hardware—are representative of the integrated stack required for real-world humanoids. Its competition success at RoboCup 2018 further demonstrates functional maturity in a standardized humanoid benchmark, making the work a useful reference for platform builders, component suppliers, and algorithm researchers in the humanoid ecosystem.
