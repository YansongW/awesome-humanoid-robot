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
  zh: 'Computational theory and practice generally focus on single-paradigm systems, but relatively little is known about
    how best to combine components based on radically different approaches (e.g., silicon chips and wetware) into a single
    coherent system. In particular, while testing strategies for single-technology components are generally well developed,
    it is unclear at present how to perform integration testing on heterotic systems: can we develop a test-set generation
    strategy for checking whether specified behaviours emerge (and unwanted behaviours do not) when components based on radically
    d'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/1408.2674v1.
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
Computational theory and practice generally focus on single-paradigm systems, but relatively little is known about how best to combine components based on radically different approaches (e.g., silicon chips and wetware) into a single coherent system. In particular, while testing strategies for single-technology components are generally well developed, it is unclear at present how to perform integration testing on heterotic systems: can we develop a test-set generation strategy for checking whether specified behaviours emerge (and unwanted behaviours do not) when components based on radically different technologies are combined within a single system?   In this paper, we describe an approach to modelling multi-technology heterotic systems using a general-purpose formal specification strategy based on Eilenberg's X-machine model of computation. We show how this approach can be used to represent disparate technologies within a single framework, and propose a strategy for using these formal models for automatic heterotic test-set generation. We illustrate our approach by showing how to derive a test set for a heterotic system combining an X-machine-based device with a cell-based P system (membrane system).

## 核心内容
Computational theory and practice generally focus on single-paradigm systems, but relatively little is known about how best to combine components based on radically different approaches (e.g., silicon chips and wetware) into a single coherent system. In particular, while testing strategies for single-technology components are generally well developed, it is unclear at present how to perform integration testing on heterotic systems: can we develop a test-set generation strategy for checking whether specified behaviours emerge (and unwanted behaviours do not) when components based on radically different technologies are combined within a single system?   In this paper, we describe an approach to modelling multi-technology heterotic systems using a general-purpose formal specification strategy based on Eilenberg's X-machine model of computation. We show how this approach can be used to represent disparate technologies within a single framework, and propose a strategy for using these formal models for automatic heterotic test-set generation. We illustrate our approach by showing how to derive a test set for a heterotic system combining an X-machine-based device with a cell-based P system (membrane system).

## 参考
- http://arxiv.org/abs/1408.2674v1

## Overview
Computational theory and practice generally focus on single-paradigm systems, but relatively little is known about how best to combine components based on radically different approaches (e.g., silicon chips and wetware) into a single coherent system. In particular, while testing strategies for single-technology components are generally well developed, it is unclear at present how to perform integration testing on heterotic systems: can we develop a test-set generation strategy for checking whether specified behaviours emerge (and unwanted behaviours do not) when components based on radically different technologies are combined within a single system? In this paper, we describe an approach to modelling multi-technology heterotic systems using a general-purpose formal specification strategy based on Eilenberg's X-machine model of computation. We show how this approach can be used to represent disparate technologies within a single framework, and propose a strategy for using these formal models for automatic heterotic test-set generation. We illustrate our approach by showing how to derive a test set for a heterotic system combining an X-machine-based device with a cell-based P system (membrane system).

## Content
Computational theory and practice generally focus on single-paradigm systems, but relatively little is known about how best to combine components based on radically different approaches (e.g., silicon chips and wetware) into a single coherent system. In particular, while testing strategies for single-technology components are generally well developed, it is unclear at present how to perform integration testing on heterotic systems: can we develop a test-set generation strategy for checking whether specified behaviours emerge (and unwanted behaviours do not) when components based on radically different technologies are combined within a single system? In this paper, we describe an approach to modelling multi-technology heterotic systems using a general-purpose formal specification strategy based on Eilenberg's X-machine model of computation. We show how this approach can be used to represent disparate technologies within a single framework, and propose a strategy for using these formal models for automatic heterotic test-set generation. We illustrate our approach by showing how to derive a test set for a heterotic system combining an X-machine-based device with a cell-based P system (membrane system).

## 개요
컴퓨팅 이론과 실제는 일반적으로 단일 패러다임 시스템에 초점을 맞추지만, 근본적으로 다른 접근 방식(예: 실리콘 칩과 웨트웨어)에 기반한 구성 요소를 하나의 일관된 시스템으로 결합하는 최선의 방법에 대해서는 상대적으로 알려진 바가 거의 없습니다. 특히, 단일 기술 구성 요소에 대한 테스트 전략은 일반적으로 잘 개발되어 있지만, 이종 시스템에 대한 통합 테스트를 수행하는 방법은 현재 명확하지 않습니다. 즉, 근본적으로 다른 기술에 기반한 구성 요소가 단일 시스템 내에서 결합될 때 지정된 동작이 나타나고(원치 않는 동작은 나타나지 않음)를 확인하기 위한 테스트 세트 생성 전략을 개발할 수 있을까요? 본 논문에서는 Eilenberg의 X-머신 계산 모델에 기반한 범용 형식 명세 전략을 사용하여 다중 기술 이종 시스템을 모델링하는 접근 방식을 설명합니다. 이 접근 방식을 사용하여 단일 프레임워크 내에서 서로 다른 기술을 표현할 수 있는 방법을 보여주고, 이러한 형식 모델을 자동 이종 테스트 세트 생성에 사용하기 위한 전략을 제안합니다. X-머신 기반 장치와 세포 기반 P 시스템(막 시스템)을 결합한 이종 시스템에 대한 테스트 세트를 도출하는 방법을 통해 접근 방식을 설명합니다.

## 핵심 내용
컴퓨팅 이론과 실제는 일반적으로 단일 패러다임 시스템에 초점을 맞추지만, 근본적으로 다른 접근 방식(예: 실리콘 칩과 웨트웨어)에 기반한 구성 요소를 하나의 일관된 시스템으로 결합하는 최선의 방법에 대해서는 상대적으로 알려진 바가 거의 없습니다. 특히, 단일 기술 구성 요소에 대한 테스트 전략은 일반적으로 잘 개발되어 있지만, 이종 시스템에 대한 통합 테스트를 수행하는 방법은 현재 명확하지 않습니다. 즉, 근본적으로 다른 기술에 기반한 구성 요소가 단일 시스템 내에서 결합될 때 지정된 동작이 나타나고(원치 않는 동작은 나타나지 않음)를 확인하기 위한 테스트 세트 생성 전략을 개발할 수 있을까요? 본 논문에서는 Eilenberg의 X-머신 계산 모델에 기반한 범용 형식 명세 전략을 사용하여 다중 기술 이종 시스템을 모델링하는 접근 방식을 설명합니다. 이 접근 방식을 사용하여 단일 프레임워크 내에서 서로 다른 기술을 표현할 수 있는 방법을 보여주고, 이러한 형식 모델을 자동 이종 테스트 세트 생성에 사용하기 위한 전략을 제안합니다. X-머신 기반 장치와 세포 기반 P 시스템(막 시스템)을 결합한 이종 시스템에 대한 테스트 세트를 도출하는 방법을 통해 접근 방식을 설명합니다.
