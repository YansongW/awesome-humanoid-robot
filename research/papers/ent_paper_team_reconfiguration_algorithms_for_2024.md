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

## Overview
We introduce and analyze a model for self-reconfigurable robots made up of unit-cube modules. Compared to past models, our model aims to newly capture two important practical aspects of real-world robots. First, modules often do not occupy an exact unit cube, but rather have features like bumps extending outside the allotted space so that modules can interlock. Thus, for example, our model forbids modules from squeezing in between two other modules that are one unit distance apart. Second, our model captures the practical scenario of many passive modules assembled by a single robot, instead of requiring all modules to be able to move on their own. We prove two universality results. First, with a supply of auxiliary modules, we show that any connected polycube structure can be constructed by a carefully aligned plane sweep. Second, without additional modules, we show how to construct any structure for which a natural notion of external feature size is at least a constant; this property largely consolidates forbidden-pattern properties used in previous works on reconfigurable modular robots.

## Content
We introduce and analyze a model for self-reconfigurable robots made up of unit-cube modules. Compared to past models, our model aims to newly capture two important practical aspects of real-world robots. First, modules often do not occupy an exact unit cube, but rather have features like bumps extending outside the allotted space so that modules can interlock. Thus, for example, our model forbids modules from squeezing in between two other modules that are one unit distance apart. Second, our model captures the practical scenario of many passive modules assembled by a single robot, instead of requiring all modules to be able to move on their own. We prove two universality results. First, with a supply of auxiliary modules, we show that any connected polycube structure can be constructed by a carefully aligned plane sweep. Second, without additional modules, we show how to construct any structure for which a natural notion of external feature size is at least a constant; this property largely consolidates forbidden-pattern properties used in previous works on reconfigurable modular robots.

## 개요
우리는 단위 정육면체 모듈로 구성된 자가 재구성 로봇을 위한 모델을 소개하고 분석합니다. 기존 모델과 비교하여, 우리의 모델은 실제 로봇의 두 가지 중요한 실용적 측면을 새롭게 포착하는 것을 목표로 합니다. 첫째, 모듈은 종종 정확한 단위 정육면체를 차지하지 않고, 모듈이 서로 맞물릴 수 있도록 할당된 공간 밖으로 돌출된 돌기와 같은 특징을 가집니다. 따라서 예를 들어, 우리의 모델은 모듈이 한 단위 거리만큼 떨어진 두 개의 다른 모듈 사이에 끼어드는 것을 금지합니다. 둘째, 우리의 모델은 모든 모듈이 스스로 움직일 수 있어야 하는 대신, 단일 로봇에 의해 조립되는 많은 수동 모듈의 실제 시나리오를 포착합니다. 우리는 두 가지 보편성 결과를 증명합니다. 첫째, 보조 모듈이 공급될 때, 신중하게 정렬된 평면 스윕을 통해 모든 연결된 폴리큐브 구조를 구성할 수 있음을 보여줍니다. 둘째, 추가 모듈 없이도 외부 특징 크기의 자연스러운 개념이 적어도 상수인 모든 구조를 구성하는 방법을 보여줍니다. 이 속성은 재구성 가능한 모듈형 로봇에 대한 이전 연구에서 사용된 금지 패턴 속성을 대부분 통합합니다.

## 핵심 내용
우리는 단위 정육면체 모듈로 구성된 자가 재구성 로봇을 위한 모델을 소개하고 분석합니다. 기존 모델과 비교하여, 우리의 모델은 실제 로봇의 두 가지 중요한 실용적 측면을 새롭게 포착하는 것을 목표로 합니다. 첫째, 모듈은 종종 정확한 단위 정육면체를 차지하지 않고, 모듈이 서로 맞물릴 수 있도록 할당된 공간 밖으로 돌출된 돌기와 같은 특징을 가집니다. 따라서 예를 들어, 우리의 모델은 모듈이 한 단위 거리만큼 떨어진 두 개의 다른 모듈 사이에 끼어드는 것을 금지합니다. 둘째, 우리의 모델은 모든 모듈이 스스로 움직일 수 있어야 하는 대신, 단일 로봇에 의해 조립되는 많은 수동 모듈의 실제 시나리오를 포착합니다. 우리는 두 가지 보편성 결과를 증명합니다. 첫째, 보조 모듈이 공급될 때, 신중하게 정렬된 평면 스윕을 통해 모든 연결된 폴리큐브 구조를 구성할 수 있음을 보여줍니다. 둘째, 추가 모듈 없이도 외부 특징 크기의 자연스러운 개념이 적어도 상수인 모든 구조를 구성하는 방법을 보여줍니다. 이 속성은 재구성 가능한 모듈형 로봇에 대한 이전 연구에서 사용된 금지 패턴 속성을 대부분 통합합니다.
