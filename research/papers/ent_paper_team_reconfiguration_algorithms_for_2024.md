---
$id: ent_paper_team_reconfiguration_algorithms_for_2024
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Reconfiguration Algorithms for Cubic Modular Robots with Realistic Movement Constraints
  zh: 具有真实运动约束的立方体模块化机器人重构算法
  ko: 현실적인 이동 제약을 가진 입방체 모듈 로봇 재구성 알고리즘
summary:
  en: 'Introduces a realistic "loose sliding-cubes" model for unit-cube modular robots that captures mechanical alignment
    features and passive modules handled by external robots, and proves two constructive universality results: a plane-sweep
    algorithm using Θ(n) auxiliary modules and a monotone construction for polycubes with external feature size at least 2.'
  zh: 提出了一种针对单位立方体模块化机器人的现实化“松散滑动立方体”模型，考虑了机械对齐特征以及由外部机器人处理的被动模块，并证明了两种构造性通用性结果：使用 Θ(n) 个辅助模块的平面扫描算法，以及针对外部特征尺寸至少为 2 的多立方体的单调构造。
  ko: 기계적 정렬 특징과 외부 로봇이 처리하는 수동 모듈을 반영하는 단위 큐브 모듈 로봇을 위한 현실적인 '느슨한 슬라이딩 큐브' 모델을 제안하고, Θ(n) 개의 보조 모듈을 사용하는 평면 스위프트 알고리즘과 외부
    특징 크기가 최소 2 인 다중 큐브를 위한 단조 구성이라는 두 가지 구조적 보편성 결과를 증명합니다.
domains:
- 04_assembly_integration_testing
- 03_manufacturing_processes
- 06_design_engineering
- 05_mass_production
layers:
- midstream
- upstream
functional_roles:
- knowledge
- process
tags:
- modular_robots
- self_reconfigurable_robots
- cubic_modules
- passive_modules
- assembly_algorithms
- plane_sweep
- external_feature_size
- loose_sliding_cubes
- universal_reconfiguration
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.15724v1.
sources:
- id: src_001
  type: paper
  title: Reconfiguration Algorithms for Cubic Modular Robots with Realistic Movement Constraints
  url: https://arxiv.org/abs/2405.15724
  date: '2024'
  accessed_at: '2026-07-01'
theoretical_depth:
- method
---
## 概述
We introduce and analyze a model for self-reconfigurable robots made up of unit-cube modules. Compared to past models, our model aims to newly capture two important practical aspects of real-world robots. First, modules often do not occupy an exact unit cube, but rather have features like bumps extending outside the allotted space so that modules can interlock. Thus, for example, our model forbids modules from squeezing in between two other modules that are one unit distance apart. Second, our model captures the practical scenario of many passive modules assembled by a single robot, instead of requiring all modules to be able to move on their own.   We prove two universality results. First, with a supply of auxiliary modules, we show that any connected polycube structure can be constructed by a carefully aligned plane sweep. Second, without additional modules, we show how to construct any structure for which a natural notion of external feature size is at least a constant; this property largely consolidates forbidden-pattern properties used in previous works on reconfigurable modular robots.

## 核心内容
We introduce and analyze a model for self-reconfigurable robots made up of unit-cube modules. Compared to past models, our model aims to newly capture two important practical aspects of real-world robots. First, modules often do not occupy an exact unit cube, but rather have features like bumps extending outside the allotted space so that modules can interlock. Thus, for example, our model forbids modules from squeezing in between two other modules that are one unit distance apart. Second, our model captures the practical scenario of many passive modules assembled by a single robot, instead of requiring all modules to be able to move on their own.   We prove two universality results. First, with a supply of auxiliary modules, we show that any connected polycube structure can be constructed by a carefully aligned plane sweep. Second, without additional modules, we show how to construct any structure for which a natural notion of external feature size is at least a constant; this property largely consolidates forbidden-pattern properties used in previous works on reconfigurable modular robots.

## 参考
- http://arxiv.org/abs/2405.15724v1

