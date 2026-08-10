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
  zh: HDDL 2.1 提出了一种提升的时序 HTN 规划形式化方法与执行语义，旨在扩展 HDDL 以支持持续动作、时序任务网络及分解约束。该工作借鉴了 PDDL 2.1 与 ANML 的设计，填补了 HDDL 在数值与时间约束表达上的空白，为工业与机器人等实际应用场景提供了更丰富的建模能力。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.07353v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (949 chars, DeepSeek).'
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
工业与机器人等实际应用需要建模丰富多样的自动化规划问题，其解决通常涉及协调并发的动作执行。许多问题天然具有层次化分解结构，适合用 HTN 形式化表达。然而，HDDL 作为 PDDL 的层次化扩展，并未像 PDDL 2.1 那样支持数值与时间约束，这限制了其在真实场景中的应用。为此，本文提出 HDDL 2.1 扩展，借鉴 PDDL 2.1 与 ANML 的设计，引入持续动作、时序任务网络及分解约束，并讨论了未来扩展所需的语法与语义。

## 核心内容
### 动机与背景
- 现实世界规划问题（如工业与机器人领域）需要协调并发的动作执行，且常具有层次化分解结构，适合用 HTN 形式化表达。
- 现有 HDDL 作为 PDDL 的层次化扩展，缺乏对数值与时间约束的支持，而 PDDL 2.1 已具备这些能力。
- 本文旨在填补 HDDL 与这些操作需求之间的差距，借鉴 PDDL 2.1 与 ANML 的设计，提出 HDDL 2.1 扩展。

### 核心贡献
- **提升的时序 HTN 形式化方法**：定义了持续动作、时序任务网络及分解约束的语法与语义。
- **执行语义**：明确了时序 HTN 规划的执行模型，支持并发与时间约束。
- **与现有标准的兼容性**：扩展基于 HDDL 与 PDDL 2.1，确保与现有规划器及领域的兼容性。

### 关键设计
- **持续动作**：动作具有持续时间，可定义起始与结束条件，支持并发执行。
- **时序任务网络**：任务节点间可定义时序关系（如顺序、并行、重叠），并支持时间约束（如时间区间、延迟）。
- **分解约束**：借鉴 ANML 的分解机制，允许在任务分解时指定时间与资源约束。

### 实验与讨论
- 本文未提供具体实验，而是聚焦于形式化定义与语义讨论，为未来 HDDL 2.1 的标准化奠定基础。
- 讨论了与现有规划器（如 PANDA、SIADEX）的兼容性，以及如何将 HDDL 2.1 集成到现有规划流程中。

### 结论
HDDL 2.1 通过引入时序与数值约束，显著扩展了 HDDL 的表达能力，使其更适用于工业与机器人等实际应用。未来工作将包括完善语法定义、开发规划器支持，以及进行大规模实验验证。

## Overview
Real world applications as in industry and robotics need modelling rich and diverse automated planning problems. Their resolution usually requires coordinated and concurrent action execution. In several cases, these problems are naturally decomposed in a hierarchical way and expressed by a Hierarchical Task Network (HTN) formalism.   HDDL, a hierarchical extension of the Planning Domain Definition Language (PDDL), unlike PDDL 2.1 does not allow to represent planning problems with numerical and temporal constraints, which are essential for real world applications. We propose to fill the gap between HDDL and these operational needs and to extend HDDL by taking inspiration from PDDL 2.1 in order to express numerical and temporal expressions. This paper opens discussions on the semantics and the syntax needed for a future HDDL 2.1 extension.

## Overview
Real-world applications in industry and robotics require modeling rich and diverse automated planning problems. Their resolution typically demands coordinated and concurrent action execution. In many cases, these problems are naturally decomposed in a hierarchical manner and expressed using a Hierarchical Task Network (HTN) formalism. HDDL, a hierarchical extension of the Planning Domain Definition Language (PDDL), unlike PDDL 2.1, does not support representing planning problems with numerical and temporal constraints, which are essential for real-world applications. We propose to bridge the gap between HDDL and these operational needs by extending HDDL, drawing inspiration from PDDL 2.1 to express numerical and temporal expressions. This paper initiates discussions on the semantics and syntax required for a future HDDL 2.1 extension.

## Content
Real-world applications in industry and robotics require modeling rich and diverse automated planning problems. Their resolution typically demands coordinated and concurrent action execution. In many cases, these problems are naturally decomposed in a hierarchical manner and expressed using a Hierarchical Task Network (HTN) formalism. HDDL, a hierarchical extension of the Planning Domain Definition Language (PDDL), unlike PDDL 2.1, does not support representing planning problems with numerical and temporal constraints, which are essential for real-world applications. We propose to bridge the gap between HDDL and these operational needs by extending HDDL, drawing inspiration from PDDL 2.1 to express numerical and temporal expressions. This paper initiates discussions on the semantics and syntax required for a future HDDL 2.1 extension.

## 参考
- http://arxiv.org/abs/2306.07353v1

## 개요
산업 및 로봇 분야와 같은 실제 응용 분야에서는 다양하고 풍부한 자동화 계획 문제를 모델링해야 하며, 이를 해결하려면 일반적으로 동시적 동작 실행의 조정이 필요합니다. 많은 문제는 자연스럽게 계층적 분해 구조를 가지며, HTN으로 형식화하기에 적합합니다. 그러나 PDDL의 계층적 확장인 HDDL은 PDDL 2.1과 달리 수치 및 시간 제약을 지원하지 않아 실제 시나리오에서의 적용에 제한이 있습니다. 이를 위해 본 논문은 PDDL 2.1과 ANML의 설계를 참고하여 지속적 동작, 시간적 태스크 네트워크 및 분해 제약을 도입하는 HDDL 2.1 확장을 제안하며, 향후 확장에 필요한 구문과 의미론을 논의합니다.

## 핵심 내용
### 동기 및 배경
- 실제 세계의 계획 문제(예: 산업 및 로봇 분야)는 동시적 동작 실행의 조정이 필요하며, 종종 계층적 분해 구조를 가지므로 HTN으로 형식화하기에 적합합니다.
- 기존 HDDL은 PDDL의 계층적 확장으로서 수치 및 시간 제약에 대한 지원이 부족한 반면, PDDL 2.1은 이미 이러한 기능을 갖추고 있습니다.
- 본 논문은 HDDL과 이러한 운영 요구 사이의 격차를 메우는 것을 목표로 하며, PDDL 2.1과 ANML의 설계를 참고하여 HDDL 2.1 확장을 제안합니다.

### 핵심 기여
- **향상된 시간적 HTN 형식화 방법**: 지속적 동작, 시간적 태스크 네트워크 및 분해 제약의 구문과 의미론을 정의합니다.
- **실행 의미론**: 동시성 및 시간 제약을 지원하는 시간적 HTN 계획의 실행 모델을 명확히 합니다.
- **기존 표준과의 호환성**: 확장은 HDDL 및 PDDL 2.1을 기반으로 하여 기존 플래너 및 도메인과의 호환성을 보장합니다.

### 핵심 설계
- **지속적 동작**: 동작은 지속 시간을 가지며, 시작 및 종료 조건을 정의할 수 있고 동시 실행을 지원합니다.
- **시간적 태스크 네트워크**: 태스크 노드 간에 시간적 관계(예: 순차, 병렬, 중첩)를 정의할 수 있으며, 시간 제약(예: 시간 구간, 지연)을 지원합니다.
- **분해 제약**: ANML의 분해 메커니즘을 참고하여 태스크 분해 시 시간 및 자원 제약을 지정할 수 있게 합니다.

### 실험 및 논의
- 본 논문은 구체적인 실험을 제공하지 않으며, 대신 형식적 정의와 의미론 논의에 초점을 맞추어 향후 HDDL 2.1 표준화의 기반을 마련합니다.
- 기존 플래너(예: PANDA, SIADEX)와의 호환성 및 HDDL 2.1을 기존 계획 프로세스에 통합하는 방법에 대해 논의합니다.

### 결론
HDDL 2.1은 시간적 및 수치적 제약을 도입함으로써 HDDL의 표현 능력을 크게 확장하여 산업 및 로봇과 같은 실제 응용 분야에 더 적합하게 만듭니다. 향후 작업에는 구문 정의 완성, 플래너 지원 개발 및 대규모 실험 검증이 포함될 것입니다.
