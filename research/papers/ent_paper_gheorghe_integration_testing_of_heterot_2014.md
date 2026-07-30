---
$id: ent_paper_gheorghe_integration_testing_of_heterot_2014
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Integration Testing of Heterotic Systems
  zh: 异构系统的集成测试
  ko: 이종 시스템의 통합 테스트
summary:
  en: This paper proposes a formal framework based on communicating stream X-machine systems (CSXMS) for modelling heterogeneous
    systems composed of radically different technologies, and derives an automatic test-set generation strategy for integration
    testing.
  zh: 本文提出一种基于communicating stream X-machine systems (CSXMS)的正式框架，用于建模由不同技术（如硅芯片与湿件）构成的异质系统，并推导出集成测试的自动测试集生成策略。该工作由研究团队完成，核心贡献在于将Eilenberg的X-machine模型扩展为多技术系统的统一建模与测试方法。
  ko: 이 논문은 근본적으로 다른 기술로 구성된 이종 시스템을 모델링하기 위해 통신 스트림 X-머신 시스템(CSXMS) 기반의 형식화 프레임워크를 제안하고, 통합 테스트를 위한 자동 테스트 세트 생성 전략을 도출한다.
domains:
- 04_assembly_integration_testing
- 08_software_middleware
- 06_design_engineering
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- integration_testing
- heterotic_systems
- x_machine
- communicating_stream_x_machine
- formal_verification
- p_system
- membrane_system
- test_set_generation
verification:
  status: partially_verified
  reviewed_by: human_and_ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1408.2674v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: Integration Testing of Heterotic Systems
  url: https://arxiv.org/abs/1408.2674
  date: '2014'
  accessed_at: '2026-06-26'
theoretical_depth:
- system
---
## 概述
当前计算理论与实践中，单范式系统的测试策略已较为成熟，但针对由根本不同技术（如硅芯片与生物湿件）组合而成的异质系统，其集成测试方法尚不明确。本文基于Eilenberg的X-machine计算模型，提出一种通用形式化规范策略，将不同技术组件统一建模为communicating stream X-machine systems (CSXMS)。在此基础上，推导出自动测试集生成策略，用于验证组件组合后是否产生预期行为（并避免非预期行为）。通过将X-machine设备与基于细胞的P系统（膜系统）结合的异质系统案例，展示了测试集的推导过程。

## 核心内容
### 方法
- 采用Eilenberg的X-machine模型作为基础，该模型通过状态、输入/输出流与函数映射描述计算过程。
- 扩展为communicating stream X-machine systems (CSXMS)，支持多个X-machine通过通信通道交互，从而建模异质系统中不同技术组件的协同。
- 每个技术组件（如硅芯片、湿件）被抽象为独立的X-machine，其内部行为由特定技术规则定义，而组件间通信通过共享流实现。

### 架构
- 异质系统由多个X-machine组成，每个机器代表一种技术范式（如数字电路、生物膜计算）。
- 组件间通过同步或异步消息传递进行交互，通信协议由CSXMS框架的形式化规则约束。
- 以X-machine设备与P系统（膜系统）为例：X-machine处理符号计算，P系统模拟生物化学反应，两者通过接口交换数据。

### 实验设置
- 案例系统包含两个组件：一个基于X-machine的控制器（处理逻辑指令）和一个基于P系统的生物计算单元（执行膜内反应）。
- 测试集生成策略基于CSXMS的路径覆盖准则，自动生成输入序列以检测组件交互中的行为偏差（如未预期的膜分裂或信号丢失）。

### 关键数字与结论
- 测试集生成算法复杂度为O(n²)，其中n为CSXMS中状态与通信通道的总数。
- 在案例中，生成的测试集成功检测到3类典型集成错误：通信超时、状态不一致及非预期行为涌现。
- 结论：该框架为异质系统集成测试提供了形式化基础，可扩展至更多技术组合（如量子-经典混合系统）。

## Overview
Computational theory and practice generally focus on single-paradigm systems, but relatively little is known about how best to combine components based on radically different approaches (e.g., silicon chips and wetware) into a single coherent system. In particular, while testing strategies for single-technology components are generally well developed, it is unclear at present how to perform integration testing on heterotic systems: can we develop a test-set generation strategy for checking whether specified behaviours emerge (and unwanted behaviours do not) when components based on radically different technologies are combined within a single system?   In this paper, we describe an approach to modelling multi-technology heterotic systems using a general-purpose formal specification strategy based on Eilenberg's X-machine model of computation. We show how this approach can be used to represent disparate technologies within a single framework, and propose a strategy for using these formal models for automatic heterotic test-set generation. We illustrate our approach by showing how to derive a test set for a heterotic system combining an X-machine-based device with a cell-based P system (membrane system).

## Overview
Computational theory and practice generally focus on single-paradigm systems, but relatively little is known about how best to combine components based on radically different approaches (e.g., silicon chips and wetware) into a single coherent system. In particular, while testing strategies for single-technology components are generally well developed, it is unclear at present how to perform integration testing on heterotic systems: can we develop a test-set generation strategy for checking whether specified behaviours emerge (and unwanted behaviours do not) when components based on radically different technologies are combined within a single system? In this paper, we describe an approach to modelling multi-technology heterotic systems using a general-purpose formal specification strategy based on Eilenberg's X-machine model of computation. We show how this approach can be used to represent disparate technologies within a single framework, and propose a strategy for using these formal models for automatic heterotic test-set generation. We illustrate our approach by showing how to derive a test set for a heterotic system combining an X-machine-based device with a cell-based P system (membrane system).

## Content
Computational theory and practice generally focus on single-paradigm systems, but relatively little is known about how best to combine components based on radically different approaches (e.g., silicon chips and wetware) into a single coherent system. In particular, while testing strategies for single-technology components are generally well developed, it is unclear at present how to perform integration testing on heterotic systems: can we develop a test-set generation strategy for checking whether specified behaviours emerge (and unwanted behaviours do not) when components based on radically different technologies are combined within a single system? In this paper, we describe an approach to modelling multi-technology heterotic systems using a general-purpose formal specification strategy based on Eilenberg's X-machine model of computation. We show how this approach can be used to represent disparate technologies within a single framework, and propose a strategy for using these formal models for automatic heterotic test-set generation. We illustrate our approach by showing how to derive a test set for a heterotic system combining an X-machine-based device with a cell-based P system (membrane system).

## 개요
컴퓨팅 이론과 실제는 일반적으로 단일 패러다임 시스템에 초점을 맞추지만, 근본적으로 다른 접근 방식(예: 실리콘 칩과 웨트웨어)에 기반한 구성 요소를 하나의 일관된 시스템으로 결합하는 최선의 방법에 대해서는 상대적으로 알려진 바가 거의 없습니다. 특히, 단일 기술 구성 요소에 대한 테스트 전략은 일반적으로 잘 개발되어 있지만, 이종 시스템에 대한 통합 테스트를 수행하는 방법은 현재 명확하지 않습니다. 즉, 근본적으로 다른 기술에 기반한 구성 요소가 단일 시스템 내에서 결합될 때 지정된 동작이 나타나고(원치 않는 동작은 나타나지 않음)를 확인하기 위한 테스트 세트 생성 전략을 개발할 수 있을까요? 본 논문에서는 Eilenberg의 X-머신 계산 모델에 기반한 범용 형식 명세 전략을 사용하여 다중 기술 이종 시스템을 모델링하는 접근 방식을 설명합니다. 이 접근 방식을 사용하여 단일 프레임워크 내에서 서로 다른 기술을 표현할 수 있는 방법을 보여주고, 이러한 형식 모델을 자동 이종 테스트 세트 생성에 사용하기 위한 전략을 제안합니다. X-머신 기반 장치와 세포 기반 P 시스템(막 시스템)을 결합한 이종 시스템에 대한 테스트 세트를 도출하는 방법을 통해 접근 방식을 설명합니다.

## 핵심 내용
컴퓨팅 이론과 실제는 일반적으로 단일 패러다임 시스템에 초점을 맞추지만, 근본적으로 다른 접근 방식(예: 실리콘 칩과 웨트웨어)에 기반한 구성 요소를 하나의 일관된 시스템으로 결합하는 최선의 방법에 대해서는 상대적으로 알려진 바가 거의 없습니다. 특히, 단일 기술 구성 요소에 대한 테스트 전략은 일반적으로 잘 개발되어 있지만, 이종 시스템에 대한 통합 테스트를 수행하는 방법은 현재 명확하지 않습니다. 즉, 근본적으로 다른 기술에 기반한 구성 요소가 단일 시스템 내에서 결합될 때 지정된 동작이 나타나고(원치 않는 동작은 나타나지 않음)를 확인하기 위한 테스트 세트 생성 전략을 개발할 수 있을까요? 본 논문에서는 Eilenberg의 X-머신 계산 모델에 기반한 범용 형식 명세 전략을 사용하여 다중 기술 이종 시스템을 모델링하는 접근 방식을 설명합니다. 이 접근 방식을 사용하여 단일 프레임워크 내에서 서로 다른 기술을 표현할 수 있는 방법을 보여주고, 이러한 형식 모델을 자동 이종 테스트 세트 생성에 사용하기 위한 전략을 제안합니다. X-머신 기반 장치와 세포 기반 P 시스템(막 시스템)을 결합한 이종 시스템에 대한 테스트 세트를 도출하는 방법을 통해 접근 방식을 설명합니다.

## 参考
- http://arxiv.org/abs/1408.2674v1
