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
  zh: NimbRo-OP2X 是一款身高 135 cm、重 19 kg 的开源成人尺寸人形机器人，采用 3D 打印部件与商用现成执行器构建，集成了 GPU 加速板载计算、深度学习视觉系统与仿真辅助步态优化。该机器人在 2018 年 RoboCup
    成人尺寸组中赢得了所有奖项。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1810.08395v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (790 chars, DeepSeek).'
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
NimbRo-OP2X 旨在解决当前人形机器人研究中平台可用性不足的问题，许多先进平台要么昂贵、危险，要么闭源，迫使研究者只能使用小型机器人或仿真环境。该机器人身高 135 cm，足以在人类环境中交互，而仅 19 kg 的重量使其操作安全简便，无需特殊设备。它配备了快速板载计算机与 GPU 以加速并行计算，并扩展了开源软件，加入了基于深度学习的视觉系统与步态参数优化。在 2018 年加拿大蒙特利尔举办的 RoboCup 中，NimbRo-OP2X 在成人尺寸组中赢得了所有奖项。

## 核心内容
### 背景与动机
人形机器人研究依赖于高性能平台，但近年来开发的先进平台往往难以被其他研究团队获取，存在成本高、操作危险或闭源等问题。这迫使研究者只能使用动态约束较宽松的小型机器人，或缺乏真实世界效应的仿真环境。NimbRo-OP2X 的开发正是为了填补这一空白。

### 硬件设计
- **尺寸与重量**：身高 135 cm，重 19 kg，足够大以在人类环境中交互，同时轻量化设计确保操作安全，无需特殊设备。
- **执行器**：采用商用现成执行器，降低开发门槛。
- **计算平台**：配备快速板载计算机与 GPU，用于加速并行计算任务，如深度学习推理。

### 软件与算法
- **开源软件**：在已有开源软件基础上扩展，新增基于深度学习的视觉系统，用于目标检测与场景理解。
- **步态优化**：通过仿真辅助的步态参数优化，提升行走稳定性与效率。

### 实验与评估
- **竞赛表现**：在 2018 年加拿大蒙特利尔举办的 RoboCup 中，NimbRo-OP2X 在 Humanoid AdultSize 类中赢得了所有奖项，验证了其综合性能。
- **关键优势**：开源设计、低成本、安全易操作，且具备实时深度学习能力，适合作为研究平台。

## Overview
Humanoid robotics research depends on capable robot platforms, but recently developed advanced platforms are often not available to other research groups, expensive, dangerous to operate, or closed-source. The lack of available platforms forces researchers to work with smaller robots, which have less strict dynamic constraints or with simulations, which lack many real-world effects. We developed NimbRo-OP2X to address this need. At a height of 135 cm our robot is large enough to interact in a human environment. Its low weight of only 19 kg makes the operation of the robot safe and easy, as no special operational equipment is necessary. Our robot is equipped with a fast onboard computer and a GPU to accelerate parallel computations. We extend our already open-source software by a deep-learning based vision system and gait parameter optimisation. The NimbRo-OP2X was evaluated during RoboCup 2018 in Montréal, Canada, where it won all possible awards in the Humanoid AdultSize class.

## 参考
- http://arxiv.org/abs/1810.08395v1

## 개요
NimbRo-OP2X는 현재 휴머노이드 로봇 연구에서 플랫폼 가용성이 부족한 문제를 해결하기 위해 설계되었습니다. 많은 첨단 플랫폼은 비싸거나, 위험하거나, 폐쇄 소스여서 연구자들이 소형 로봇이나 시뮬레이션 환경만 사용할 수밖에 없는 상황입니다. 이 로봇은 키 135cm로 인간 환경에서 상호작용하기에 충분하며, 무게가 19kg에 불과해 특별한 장비 없이도 안전하고 쉽게 조작할 수 있습니다. 고속 온보드 컴퓨터와 GPU를 탑재하여 병렬 계산을 가속화하고, 오픈 소스 소프트웨어를 확장하여 딥러닝 기반 비전 시스템과 보행 파라미터 최적화를 추가했습니다. 2018년 캐나다 몬트리올에서 열린 RoboCup에서 NimbRo-OP2X는 성인 크기 부문에서 모든 상을 수상했습니다.

## 핵심 내용
### 배경 및 동기
휴머노이드 로봇 연구는 고성능 플랫폼에 의존하지만, 최근 개발된 첨단 플랫폼은 다른 연구팀이 접근하기 어려운 경우가 많으며, 비용이 높거나, 조작이 위험하거나, 폐쇄 소스인 문제가 있습니다. 이로 인해 연구자들은 동적 제약이 덜 엄격한 소형 로봇이나 실제 세계 효과가 부족한 시뮬레이션 환경을 사용할 수밖에 없습니다. NimbRo-OP2X의 개발은 바로 이러한 공백을 메우기 위한 것입니다.

### 하드웨어 설계
- **크기 및 무게**: 키 135cm, 무게 19kg으로 인간 환경에서 상호작용하기에 충분히 크면서도, 경량 설계로 특별한 장비 없이 안전한 조작을 보장합니다.
- **액추에이터**: 상용 기성 액추에이터를 사용하여 개발 장벽을 낮췄습니다.
- **계산 플랫폼**: 고속 온보드 컴퓨터와 GPU를 탑재하여 딥러닝 추론과 같은 병렬 계산 작업을 가속화합니다.

### 소프트웨어 및 알고리즘
- **오픈 소스 소프트웨어**: 기존 오픈 소스 소프트웨어를 확장하여 객체 감지와 장면 이해를 위한 딥러닝 기반 비전 시스템을 새로 추가했습니다.
- **보행 최적화**: 시뮬레이션 지원 보행 파라미터 최적화를 통해 보행 안정성과 효율성을 향상시킵니다.

### 실험 및 평가
- **대회 성과**: 2018년 캐나다 몬트리올에서 열린 RoboCup에서 NimbRo-OP2X는 Humanoid AdultSize 부문에서 모든 상을 수상하며 종합 성능을 입증했습니다.
- **주요 장점**: 오픈 소스 설계, 저비용, 안전하고 쉬운 조작, 그리고 실시간 딥러닝 기능을 갖추어 연구 플랫폼으로 적합합니다.
