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
  en: NimbRo-OP2X is a 135 cm, 19 kg open-source adult-sized humanoid robot built with 3D-printed parts and commercial off-the-shelf
    actuators, integrating GPU-accelerated onboard computing, a deep-learning vision system, and simulation-assisted gait
    optimization; it won all awards in the Humanoid AdultSize class at RoboCup 2018.
  zh: NimbRo-OP2X 是一款身高135厘米、重19公斤的开源成人尺寸人形机器人，采用3D打印部件和商用执行器，集成GPU加速的机载计算、深度学习视觉系统以及仿真辅助的步态优化，并在2018年机器人世界杯人形成人组比赛中获得所有奖项。
  ko: NimbRo-OP2X는 키 135cm, 무게 19kg의 오픈소스 성인 크기 휴머노이드 로봇으로, 3D 프린팅 부품과 상용 액추에이터를 사용하고 GPU 가속 온보드 컴퓨팅, 딥러닝 비전 시스템 및 시뮬레이션 보조
    보행 최적화를 통합했으며 2018년 로보컵 휴머노이드 성인부에서 모든 상을 수상했다.
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
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1810.08395v1.
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
## 概述
Humanoid robotics research depends on capable robot platforms, but recently developed advanced platforms are often not available to other research groups, expensive, dangerous to operate, or closed-source. The lack of available platforms forces researchers to work with smaller robots, which have less strict dynamic constraints or with simulations, which lack many real-world effects. We developed NimbRo-OP2X to address this need. At a height of 135 cm our robot is large enough to interact in a human environment. Its low weight of only 19 kg makes the operation of the robot safe and easy, as no special operational equipment is necessary. Our robot is equipped with a fast onboard computer and a GPU to accelerate parallel computations. We extend our already open-source software by a deep-learning based vision system and gait parameter optimisation. The NimbRo-OP2X was evaluated during RoboCup 2018 in Montréal, Canada, where it won all possible awards in the Humanoid AdultSize class.

## 核心内容
Humanoid robotics research depends on capable robot platforms, but recently developed advanced platforms are often not available to other research groups, expensive, dangerous to operate, or closed-source. The lack of available platforms forces researchers to work with smaller robots, which have less strict dynamic constraints or with simulations, which lack many real-world effects. We developed NimbRo-OP2X to address this need. At a height of 135 cm our robot is large enough to interact in a human environment. Its low weight of only 19 kg makes the operation of the robot safe and easy, as no special operational equipment is necessary. Our robot is equipped with a fast onboard computer and a GPU to accelerate parallel computations. We extend our already open-source software by a deep-learning based vision system and gait parameter optimisation. The NimbRo-OP2X was evaluated during RoboCup 2018 in Montréal, Canada, where it won all possible awards in the Humanoid AdultSize class.

## 参考
- http://arxiv.org/abs/1810.08395v1

## Overview
Humanoid robotics research depends on capable robot platforms, but recently developed advanced platforms are often not available to other research groups, expensive, dangerous to operate, or closed-source. The lack of available platforms forces researchers to work with smaller robots, which have less strict dynamic constraints or with simulations, which lack many real-world effects. We developed NimbRo-OP2X to address this need. At a height of 135 cm our robot is large enough to interact in a human environment. Its low weight of only 19 kg makes the operation of the robot safe and easy, as no special operational equipment is necessary. Our robot is equipped with a fast onboard computer and a GPU to accelerate parallel computations. We extend our already open-source software by a deep-learning based vision system and gait parameter optimisation. The NimbRo-OP2X was evaluated during RoboCup 2018 in Montréal, Canada, where it won all possible awards in the Humanoid AdultSize class.

## Content
Humanoid robotics research depends on capable robot platforms, but recently developed advanced platforms are often not available to other research groups, expensive, dangerous to operate, or closed-source. The lack of available platforms forces researchers to work with smaller robots, which have less strict dynamic constraints or with simulations, which lack many real-world effects. We developed NimbRo-OP2X to address this need. At a height of 135 cm our robot is large enough to interact in a human environment. Its low weight of only 19 kg makes the operation of the robot safe and easy, as no special operational equipment is necessary. Our robot is equipped with a fast onboard computer and a GPU to accelerate parallel computations. We extend our already open-source software by a deep-learning based vision system and gait parameter optimisation. The NimbRo-OP2X was evaluated during RoboCup 2018 in Montréal, Canada, where it won all possible awards in the Humanoid AdultSize class.

## 개요
휴머노이드 로봇 연구는 성능이 뛰어난 로봇 플랫폼에 의존하지만, 최근 개발된 고급 플랫폼은 종종 다른 연구 그룹이 이용할 수 없거나, 비싸고, 운영하기에 위험하거나, 폐쇄 소스인 경우가 많습니다. 이용 가능한 플랫폼의 부족으로 인해 연구자들은 동적 제약 조건이 덜 엄격한 소형 로봇이나 실제 세계의 많은 효과가 부족한 시뮬레이션을 사용해야 합니다. 우리는 이러한 필요를 해결하기 위해 NimbRo-OP2X를 개발했습니다. 높이 135cm로 우리 로봇은 인간 환경에서 상호작용하기에 충분히 큽니다. 무게가 19kg에 불과해 특별한 운영 장비 없이도 로봇을 안전하고 쉽게 조작할 수 있습니다. 우리 로봇에는 빠른 온보드 컴퓨터와 병렬 계산을 가속화하는 GPU가 장착되어 있습니다. 우리는 이미 오픈 소스인 소프트웨어를 딥러닝 기반 비전 시스템과 보행 매개변수 최적화로 확장했습니다. NimbRo-OP2X는 캐나다 몬트리올에서 열린 RoboCup 2018에서 평가되었으며, Humanoid AdultSize 클래스에서 가능한 모든 상을 수상했습니다.

## 핵심 내용
휴머노이드 로봇 연구는 성능이 뛰어난 로봇 플랫폼에 의존하지만, 최근 개발된 고급 플랫폼은 종종 다른 연구 그룹이 이용할 수 없거나, 비싸고, 운영하기에 위험하거나, 폐쇄 소스인 경우가 많습니다. 이용 가능한 플랫폼의 부족으로 인해 연구자들은 동적 제약 조건이 덜 엄격한 소형 로봇이나 실제 세계의 많은 효과가 부족한 시뮬레이션을 사용해야 합니다. 우리는 이러한 필요를 해결하기 위해 NimbRo-OP2X를 개발했습니다. 높이 135cm로 우리 로봇은 인간 환경에서 상호작용하기에 충분히 큽니다. 무게가 19kg에 불과해 특별한 운영 장비 없이도 로봇을 안전하고 쉽게 조작할 수 있습니다. 우리 로봇에는 빠른 온보드 컴퓨터와 병렬 계산을 가속화하는 GPU가 장착되어 있습니다. 우리는 이미 오픈 소스인 소프트웨어를 딥러닝 기반 비전 시스템과 보행 매개변수 최적화로 확장했습니다. NimbRo-OP2X는 캐나다 몬트리올에서 열린 RoboCup 2018에서 평가되었으며, Humanoid AdultSize 클래스에서 가능한 모든 상을 수상했습니다.
