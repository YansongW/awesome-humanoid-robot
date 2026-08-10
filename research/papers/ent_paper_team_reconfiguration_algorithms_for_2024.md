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
  zh: 本文提出了一种名为“松散滑动立方体”的单元立方体模块化机器人模型，该模型捕捉了机械对齐特征和由外部机器人处理的被动模块。研究证明了两个构造通用性结果：一个使用Θ(n)个辅助模块的平面扫描算法，以及一个针对外部特征尺寸至少为2的多立方体的单调构造方法。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2405.15724v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (810 chars, DeepSeek).'
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
本文介绍并分析了一种由单元立方体模块组成的自重构机器人模型。与以往模型相比，该模型旨在捕捉真实世界机器人的两个重要实际方面：模块通常不占据精确的单元立方体，而是具有凸起等特征，以便模块可以互锁；同时，模型捕捉了由单个机器人组装许多被动模块的实际场景，而不要求所有模块都能自行移动。研究证明了两个通用性结果：首先，通过提供辅助模块，任何连通的多立方体结构都可以通过精心对齐的平面扫描来构建；其次，在没有额外模块的情况下，可以构建任何外部特征尺寸至少为常数的结构，这一性质在很大程度上整合了先前可重构模块化机器人研究中使用的禁止模式属性。

## 核心内容
### 模型定义
- 提出“松散滑动立方体”模型，其中模块占据单元立方体空间，但具有机械对齐特征（如凸起），因此禁止模块挤入两个相距一个单位距离的模块之间。
- 模型支持被动模块，即由外部机器人处理而非自身移动的模块，这更贴近实际组装场景。

### 算法与构造
- **平面扫描算法**：使用Θ(n)个辅助模块，通过精心对齐的平面扫描，可以构建任何连通的多立方体结构。该算法确保模块在移动过程中不会违反机械约束。
- **单调构造方法**：针对外部特征尺寸至少为2的多立方体结构，无需额外辅助模块即可完成构造。外部特征尺寸定义为结构表面到内部的最小距离，该性质整合了先前工作中的禁止模式属性。

### 实验设置与关键数字
- 模型基于单元立方体模块，模块数量为n。
- 平面扫描算法使用Θ(n)个辅助模块，即辅助模块数量与结构模块数量成线性关系。
- 单调构造方法要求外部特征尺寸至少为2，这意味着结构表面不能有过于狭窄的凹陷或突出。

### 结论
本文提出的模型和算法为实际模块化机器人的自重构提供了理论基础，通过考虑机械对齐和被动模块，更贴近真实应用场景。两个通用性结果分别适用于有辅助模块和无辅助模块的情况，为未来机器人系统的设计提供了指导。

## Overview
We introduce and analyze a model for self-reconfigurable robots made up of unit-cube modules. Compared to past models, our model aims to newly capture two important practical aspects of real-world robots. First, modules often do not occupy an exact unit cube, but rather have features like bumps extending outside the allotted space so that modules can interlock. Thus, for example, our model forbids modules from squeezing in between two other modules that are one unit distance apart. Second, our model captures the practical scenario of many passive modules assembled by a single robot, instead of requiring all modules to be able to move on their own.   We prove two universality results. First, with a supply of auxiliary modules, we show that any connected polycube structure can be constructed by a carefully aligned plane sweep. Second, without additional modules, we show how to construct any structure for which a natural notion of external feature size is at least a constant; this property largely consolidates forbidden-pattern properties used in previous works on reconfigurable modular robots.

## Overview
We introduce and analyze a model for self-reconfigurable robots made up of unit-cube modules. Compared to past models, our model aims to newly capture two important practical aspects of real-world robots. First, modules often do not occupy an exact unit cube, but rather have features like bumps extending outside the allotted space so that modules can interlock. Thus, for example, our model forbids modules from squeezing in between two other modules that are one unit distance apart. Second, our model captures the practical scenario of many passive modules assembled by a single robot, instead of requiring all modules to be able to move on their own. We prove two universality results. First, with a supply of auxiliary modules, we show that any connected polycube structure can be constructed by a carefully aligned plane sweep. Second, without additional modules, we show how to construct any structure for which a natural notion of external feature size is at least a constant; this property largely consolidates forbidden-pattern properties used in previous works on reconfigurable modular robots.

## Content
We introduce and analyze a model for self-reconfigurable robots made up of unit-cube modules. Compared to past models, our model aims to newly capture two important practical aspects of real-world robots. First, modules often do not occupy an exact unit cube, but rather have features like bumps extending outside the allotted space so that modules can interlock. Thus, for example, our model forbids modules from squeezing in between two other modules that are one unit distance apart. Second, our model captures the practical scenario of many passive modules assembled by a single robot, instead of requiring all modules to be able to move on their own. We prove two universality results. First, with a supply of auxiliary modules, we show that any connected polycube structure can be constructed by a carefully aligned plane sweep. Second, without additional modules, we show how to construct any structure for which a natural notion of external feature size is at least a constant; this property largely consolidates forbidden-pattern properties used in previous works on reconfigurable modular robots.

## 参考
- http://arxiv.org/abs/2405.15724v1

## 개요
본 논문은 단위 입방체 모듈로 구성된 자가 재구성 로봇 모델을 소개하고 분석한다. 기존 모델과 달리, 이 모델은 실제 세계 로봇의 두 가지 중요한 실제적 측면을 포착하는 것을 목표로 한다: 모듈은 일반적으로 정확한 단위 입방체를 차지하지 않으며, 모듈이 서로 맞물릴 수 있도록 돌출부와 같은 특징을 갖는다. 또한, 이 모델은 모든 모듈이 스스로 움직일 수 있어야 한다는 요구 없이, 단일 로봇이 많은 수동 모듈을 조립하는 실제 시나리오를 포착한다. 연구는 두 가지 일반성 결과를 증명한다: 첫째, 보조 모듈을 제공함으로써, 연결된 다중 입방체 구조는 정교하게 정렬된 평면 스캔을 통해 구성될 수 있다. 둘째, 추가 모듈 없이도 외부 특징 크기가 최소 상수인 구조를 구성할 수 있으며, 이 속성은 이전의 재구성 가능한 모듈식 로봇 연구에서 사용된 금지 패턴 속성을 크게 통합한다.

## 핵심 내용
### 모델 정의
- "느슨한 슬라이딩 입방체" 모델을 제안하며, 모듈은 단위 입방체 공간을 차지하지만 기계적 정렬 특징(예: 돌출부)을 가지므로, 모듈이 서로 한 단위 거리에 있는 두 모듈 사이로 밀려 들어가는 것이 금지된다.
- 모델은 수동 모듈, 즉 스스로 움직이지 않고 외부 로봇에 의해 처리되는 모듈을 지원하며, 이는 실제 조립 시나리오에 더 가깝다.

### 알고리즘 및 구성
- **평면 스캔 알고리즘**: Θ(n)개의 보조 모듈을 사용하여, 정교하게 정렬된 평면 스캔을 통해 연결된 다중 입방체 구조를 구성할 수 있다. 이 알고리즘은 모듈이 이동 중 기계적 제약을 위반하지 않도록 보장한다.
- **단조 구성 방법**: 외부 특징 크기가 최소 2인 다중 입방체 구조의 경우, 추가 보조 모듈 없이 구성을 완료할 수 있다. 외부 특징 크기는 구조 표면에서 내부까지의 최소 거리로 정의되며, 이 속성은 이전 연구의 금지 패턴 속성을 통합한다.

### 실험 설정 및 주요 수치
- 모델은 단위 입방체 모듈을 기반으로 하며, 모듈 수는 n이다.
- 평면 스캔 알고리즘은 Θ(n)개의 보조 모듈을 사용하며, 즉 보조 모듈 수는 구조 모듈 수와 선형 관계에 있다.
- 단조 구성 방법은 외부 특징 크기가 최소 2일 것을 요구하며, 이는 구조 표면에 너무 좁은 함몰이나 돌출이 없어야 함을 의미한다.

### 결론
본 논문에서 제안한 모델과 알고리즘은 실제 모듈식 로봇의 자가 재구성을 위한 이론적 기초를 제공하며, 기계적 정렬과 수동 모듈을 고려하여 실제 응용 시나리오에 더 가깝다. 두 가지 일반성 결과는 각각 보조 모듈이 있는 경우와 없는 경우에 적용되며, 미래 로봇 시스템 설계에 지침을 제공한다.
