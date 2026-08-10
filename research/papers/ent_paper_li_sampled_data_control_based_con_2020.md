---
$id: ent_paper_li_sampled_data_control_based_con_2020
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Sampled-Data Control Based Consensus of Fractional-Order Multi-Agent Systems
  zh: 基于采样数据控制的分数阶多智能体系统一致性研究
  ko: 샘플링 데이터 제어 기반 분수 차수 다중 에이전트 시스템의 합의
summary:
  en: This paper proposes a distributed sampled-data controller for fractional-order multi-agent systems that compensates
    for historical control inputs to account for the hereditary and infinite memory properties of fractional-order calculus,
    with proofs of global boundedness and asymptotic average consensus.
  zh: 本文针对分数阶多智能体系统提出一种分布式采样数据控制器，通过补偿历史控制输入来应对分数阶微积分的遗传性与无限记忆特性，并证明了全局有界性与渐近平均一致性。
  ko: 본 논문은 분수 차수 미적분학의 유전적이고 무한한 기억 특성을 고려하기 위해 과거 제어 입력을 보상하는 분수 차수 다중 에이전트 시스템을 위한 분산 샘플링 데이터 제어기를 제안하고, 전역 유계성과 점근적 평균
    합의를 증명한다.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- multi_agent_systems
- sampled_data_control
- fractional_order_control
- distributed_consensus
- fleet_coordination
- control_theory
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2004.00860v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    en/ko body retranslated from zh deep-read (468 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: Sampled-Data Control Based Consensus of Fractional-Order Multi-Agent Systems
  url: https://arxiv.org/abs/2004.00860
  date: '2020'
  accessed_at: '2026-06-27'
theoretical_depth:
- method
---
## 概述
该研究聚焦于阶数在(0,1)范围内的分数阶多智能体系统，利用采样数据控制实现一致性。作者设计了一种新型分布式控制器，其核心创新在于利用分数阶微积分的独特性质（遗传性与无限记忆）对历史控制输入进行补偿。理论分析严格证明了闭环信号全局有界且系统能实现渐近一致性，仿真实验验证了方法的有效性。

## 核心内容
### 方法
- 针对分数阶多智能体系统（阶数α∈(0,1)），提出基于采样数据的分布式控制器设计框架。
- 控制器通过补偿历史控制输入，显式处理分数阶微积分的遗传性与无限记忆特性。

### 理论分析
- 严格证明闭环系统所有信号全局有界。
- 建立渐近平均一致性条件，确保智能体状态最终收敛至共同值。

### 实验设置
- 仿真采用多智能体网络拓扑，验证控制器在不同阶数α下的性能。
- 对比传统整数阶控制器，突出分数阶补偿机制的优势。

### 关键结果
- 全局有界性：所有状态量在有限时间内不发散。
- 渐近一致性：智能体状态误差随时间趋于零。
- 仿真结果与理论分析一致，证实控制器对分数阶系统的有效性。

## 参考
- http://arxiv.org/abs/2004.00860v1

## Overview
This study focuses on fractional-order multi-agent systems with orders in the range (0,1), achieving consensus using sampled-data control. The authors design a novel distributed controller, whose core innovation lies in compensating for historical control inputs by leveraging the unique properties of fractional calculus (heredity and infinite memory). Theoretical analysis rigorously proves that closed-loop signals are globally bounded and the system can achieve asymptotic consensus, with simulation experiments validating the effectiveness of the method.

## Content
### Method
- Proposes a distributed controller design framework based on sampled data for fractional-order multi-agent systems (order α∈(0,1)).
- The controller explicitly handles the heredity and infinite memory characteristics of fractional calculus by compensating for historical control inputs.

### Theoretical Analysis
- Rigorously proves that all signals in the closed-loop system are globally bounded.
- Establishes conditions for asymptotic average consensus, ensuring that agent states ultimately converge to a common value.

### Experimental Setup
- Simulations employ a multi-agent network topology to verify controller performance under different orders α.
- Comparisons with traditional integer-order controllers highlight the advantages of the fractional-order compensation mechanism.

### Key Results
- Global boundedness: All state variables do not diverge within finite time.
- Asymptotic consensus: Agent state errors tend to zero over time.
- Simulation results align with theoretical analysis, confirming the controller's effectiveness for fractional-order systems.

## 개요
이 연구는 차수가 (0,1) 범위에 있는 분수차 다중 에이전트 시스템에 초점을 맞추며, 샘플링 데이터 제어를 통해 일치성을 구현합니다. 저자는 새로운 유형의 분산 제어기를 설계했으며, 핵심 혁신은 분수차 미적분의 독특한 성질(유전성과 무한 기억)을 활용하여 과거 제어 입력을 보상하는 데 있습니다. 이론 분석은 폐루프 신호가 전역적으로 유계이며 시스템이 점근적 일치성을 달성할 수 있음을 엄밀히 증명했으며, 시뮬레이션 실험은 방법의 유효성을 검증했습니다.

## 핵심 내용
### 방법
- 분수차 다중 에이전트 시스템(차수 α∈(0,1))을 대상으로 샘플링 데이터 기반 분산 제어기 설계 프레임워크를 제안합니다.
- 제어기는 과거 제어 입력을 보상하여 분수차 미적분의 유전성과 무한 기억 특성을 명시적으로 처리합니다.

### 이론 분석
- 폐루프 시스템의 모든 신호가 전역적으로 유계임을 엄밀히 증명합니다.
- 점근적 평균 일치성 조건을 확립하여 에이전트 상태가 최종적으로 공통 값에 수렴하도록 보장합니다.

### 실험 설정
- 시뮬레이션은 다중 에이전트 네트워크 토폴로지를 사용하여 서로 다른 차수 α에서 제어기의 성능을 검증합니다.
- 전통적인 정수차 제어기와 비교하여 분수차 보상 메커니즘의 장점을 부각합니다.

### 주요 결과
- 전역 유계성: 모든 상태량이 유한 시간 내에 발산하지 않습니다.
- 점근적 일치성: 에이전트 상태 오차가 시간에 따라 0으로 수렴합니다.
- 시뮬레이션 결과는 이론 분석과 일치하며, 분수차 시스템에 대한 제어기의 유효성을 확인합니다.
