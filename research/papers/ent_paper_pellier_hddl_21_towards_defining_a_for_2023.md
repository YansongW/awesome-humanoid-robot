---
$id: ent_paper_pellier_hddl_21_towards_defining_a_for_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HDDL 2.1: Towards Defining a Formalism and a Semantics for Temporal HTN Planning'
  zh: HDDL 2.1：面向时序HTN规划的形式化与语义定义
  ko: 'HDDL 2.1: 시간적 HTN 계획을 위한 형식화 및 의미 정의를 향하여'
summary:
  en: Proposes a lifted temporal HTN planning formalism and execution semantics that extends HDDL with durative actions, temporal
    task networks, and decomposition constraints inspired by PDDL 2.1 and ANML.
  zh: 提出一种 lifted 时序 HTN 规划形式化及执行语义，通过借鉴 PDDL 2.1 与 ANML，将 HDDL 扩展为支持持续动作、时序任务网络与分解约束。
  ko: PDDL 2.1과 ANML에서 영감을 받아 HDDL을 지속적 동작, 시간적 작업 네트워크 및 분해 제약으로 확장하는 lifted temporal HTN 계획 형식화 및 실행 의미를 제안한다.
domains:
- 07_ai_models_algorithms
- 04_assembly_integration_testing
- 05_mass_production
layers:
- intelligence
- midstream
functional_roles:
- knowledge
- intelligence
tags:
- temporal_htn_planning
- hierarchical_task_network
- durative_actions
- task_decomposition
- pddl
- pddl_2_1
- anml
- automated_planning
- robotics_planning
- planning_formalism
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.07353v1.
sources:
- id: src_001
  type: paper
  title: 'HDDL 2.1: Towards Defining a Formalism and a Semantics for Temporal HTN Planning'
  url: https://arxiv.org/abs/2306.07353
  date: '2023'
  accessed_at: '2026-06-27'
theoretical_depth:
- formalism
- method
---
## 概述
Real world applications as in industry and robotics need modelling rich and diverse automated planning problems. Their resolution usually requires coordinated and concurrent action execution. In several cases, these problems are naturally decomposed in a hierarchical way and expressed by a Hierarchical Task Network (HTN) formalism.   HDDL, a hierarchical extension of the Planning Domain Definition Language (PDDL), unlike PDDL 2.1 does not allow to represent planning problems with numerical and temporal constraints, which are essential for real world applications. We propose to fill the gap between HDDL and these operational needs and to extend HDDL by taking inspiration from PDDL 2.1 in order to express numerical and temporal expressions. This paper opens discussions on the semantics and the syntax needed for a future HDDL 2.1 extension.

## 核心内容
Real world applications as in industry and robotics need modelling rich and diverse automated planning problems. Their resolution usually requires coordinated and concurrent action execution. In several cases, these problems are naturally decomposed in a hierarchical way and expressed by a Hierarchical Task Network (HTN) formalism.   HDDL, a hierarchical extension of the Planning Domain Definition Language (PDDL), unlike PDDL 2.1 does not allow to represent planning problems with numerical and temporal constraints, which are essential for real world applications. We propose to fill the gap between HDDL and these operational needs and to extend HDDL by taking inspiration from PDDL 2.1 in order to express numerical and temporal expressions. This paper opens discussions on the semantics and the syntax needed for a future HDDL 2.1 extension.

## 参考
- http://arxiv.org/abs/2306.07353v1

## Overview
Real-world applications in industry and robotics require modeling rich and diverse automated planning problems. Their resolution typically demands coordinated and concurrent action execution. In many cases, these problems are naturally decomposed in a hierarchical manner and expressed using a Hierarchical Task Network (HTN) formalism. HDDL, a hierarchical extension of the Planning Domain Definition Language (PDDL), unlike PDDL 2.1, does not support representing planning problems with numerical and temporal constraints, which are essential for real-world applications. We propose to bridge the gap between HDDL and these operational needs by extending HDDL, drawing inspiration from PDDL 2.1 to express numerical and temporal expressions. This paper initiates discussions on the semantics and syntax required for a future HDDL 2.1 extension.

## Content
Real-world applications in industry and robotics require modeling rich and diverse automated planning problems. Their resolution typically demands coordinated and concurrent action execution. In many cases, these problems are naturally decomposed in a hierarchical manner and expressed using a Hierarchical Task Network (HTN) formalism. HDDL, a hierarchical extension of the Planning Domain Definition Language (PDDL), unlike PDDL 2.1, does not support representing planning problems with numerical and temporal constraints, which are essential for real-world applications. We propose to bridge the gap between HDDL and these operational needs by extending HDDL, drawing inspiration from PDDL 2.1 to express numerical and temporal expressions. This paper initiates discussions on the semantics and syntax required for a future HDDL 2.1 extension.

## 개요
산업 및 로보틱스와 같은 실제 애플리케이션에서는 풍부하고 다양한 자동화된 계획 문제를 모델링해야 합니다. 이러한 문제를 해결하려면 일반적으로 조정되고 동시적인 행동 실행이 필요합니다. 여러 경우에 이러한 문제는 계층적 방식으로 자연스럽게 분해되며, HTN(계층적 작업 네트워크) 형식으로 표현됩니다. HDDL은 PDDL(계획 도메인 정의 언어)의 계층적 확장이지만, PDDL 2.1과 달리 실제 애플리케이션에 필수적인 수치 및 시간적 제약 조건을 가진 계획 문제를 표현할 수 없습니다. 우리는 HDDL과 이러한 운영 요구 사이의 격차를 해소하고, PDDL 2.1에서 영감을 받아 수치 및 시간적 표현을 표현할 수 있도록 HDDL을 확장할 것을 제안합니다. 이 논문은 향후 HDDL 2.1 확장에 필요한 의미론과 구문에 대한 논의를 시작합니다.

## 핵심 내용
산업 및 로보틱스와 같은 실제 애플리케이션에서는 풍부하고 다양한 자동화된 계획 문제를 모델링해야 합니다. 이러한 문제를 해결하려면 일반적으로 조정되고 동시적인 행동 실행이 필요합니다. 여러 경우에 이러한 문제는 계층적 방식으로 자연스럽게 분해되며, HTN(계층적 작업 네트워크) 형식으로 표현됩니다. HDDL은 PDDL(계획 도메인 정의 언어)의 계층적 확장이지만, PDDL 2.1과 달리 실제 애플리케이션에 필수적인 수치 및 시간적 제약 조건을 가진 계획 문제를 표현할 수 없습니다. 우리는 HDDL과 이러한 운영 요구 사이의 격차를 해소하고, PDDL 2.1에서 영감을 받아 수치 및 시간적 표현을 표현할 수 있도록 HDDL을 확장할 것을 제안합니다. 이 논문은 향후 HDDL 2.1 확장에 필요한 의미론과 구문에 대한 논의를 시작합니다.
