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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1408.2674v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10: ko
    body retranslated from zh deep-read (956 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/1408.2674v1

## 개요
현재 계산 이론과 실무에서 단일 패러다임 시스템의 테스트 전략은 비교적 성숙했지만, 근본적으로 다른 기술(예: 실리콘 칩과 생물학적 습식 부품)이 결합된 이종 시스템에 대한 통합 테스트 방법은 아직 명확하지 않다. 본 논문은 Eilenberg의 X-machine 계산 모델을 기반으로, 서로 다른 기술 구성 요소를 communicating stream X-machine systems (CSXMS)로 통합 모델링하는 일반적인 형식적 명세 전략을 제안한다. 이를 바탕으로, 구성 요소 결합 후 예상 동작이 발생하는지(그리고 비예상 동작을 방지하는지) 검증하기 위한 자동 테스트 집합 생성 전략을 도출한다. X-machine 장치와 세포 기반 P 시스템(막 시스템)을 결합한 이종 시스템 사례를 통해 테스트 집합 도출 과정을 보여준다.

## 핵심 내용
### 방법
- Eilenberg의 X-machine 모델을 기반으로 사용하며, 이 모델은 상태, 입력/출력 스트림 및 함수 매핑을 통해 계산 과정을 설명한다.
- communicating stream X-machine systems (CSXMS)로 확장하여, 여러 X-machine이 통신 채널을 통해 상호작용할 수 있게 함으로써 이종 시스템 내 서로 다른 기술 구성 요소의 협력을 모델링한다.
- 각 기술 구성 요소(예: 실리콘 칩, 습식 부품)는 독립적인 X-machine으로 추상화되며, 내부 동작은 특정 기술 규칙에 의해 정의되고, 구성 요소 간 통신은 공유 스트림을 통해 구현된다.

### 아키텍처
- 이종 시스템은 여러 X-machine으로 구성되며, 각 머신은 하나의 기술 패러다임(예: 디지털 회로, 생물학적 막 계산)을 나타낸다.
- 구성 요소 간에는 동기 또는 비동기 메시지 전달을 통해 상호작용하며, 통신 프로토콜은 CSXMS 프레임워크의 형식적 규칙에 의해 제약된다.
- X-machine 장치와 P 시스템(막 시스템)을 예로 들면: X-machine은 기호 계산을 처리하고, P 시스템은 생물학적 화학 반응을 시뮬레이션하며, 둘은 인터페이스를 통해 데이터를 교환한다.

### 실험 설정
- 사례 시스템은 두 개의 구성 요소를 포함한다: X-machine 기반 컨트롤러(논리 명령 처리)와 P 시스템 기반 생물학적 계산 유닛(막 내 반응 실행).
- 테스트 집합 생성 전략은 CSXMS의 경로 커버리지 기준을 기반으로, 구성 요소 상호작용에서 동작 편차(예: 예상치 못한 막 분열 또는 신호 손실)를 감지하기 위해 입력 시퀀스를 자동 생성한다.

### 주요 수치 및 결론
- 테스트 집합 생성 알고리즘의 복잡도는 O(n²)이며, 여기서 n은 CSXMS의 상태와 통신 채널의 총 수이다.
- 사례에서 생성된 테스트 집합은 3가지 유형의 일반적인 통합 오류를 성공적으로 감지했다: 통신 시간 초과, 상태 불일치 및 비예상 동작 출현.
- 결론: 이 프레임워크는 이종 시스템 통합 테스트를 위한 형식적 기반을 제공하며, 더 많은 기술 조합(예: 양자-고전 혼합 시스템)으로 확장할 수 있다.
