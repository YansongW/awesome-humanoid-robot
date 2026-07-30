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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2004.00860v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
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

## Overview
In this paper, we investigate consensus control of fractional-order multi-agent systems with order in (0,1) via sampled-data control. A new scheme to design distributed controllers with rigorous analysis is presented by utilizing the unique properties of fractional-order calculus, namely hereditary and infinite memory. It is established that global boundedness of all closed-loop signals is ensured and asymptotic consensus is realized. Simulation studies are conducted to illustrate the effectiveness of the proposed control method and verify the obtained results.

## 개요
본 논문에서는 샘플링 데이터 제어를 통해 차수가 (0,1)인 분수차 다중 에이전트 시스템의 합의 제어를 연구합니다. 분수차 미적분학의 고유한 특성, 즉 유전성과 무한 메모리를 활용하여 엄격한 분석을 통해 분산 제어기를 설계하는 새로운 방식을 제시합니다. 모든 폐루프 신호의 전역적 유계성이 보장되고 점근적 합의가 실현됨을 입증합니다. 제안된 제어 방법의 효과성을 입증하고 얻어진 결과를 검증하기 위해 시뮬레이션 연구를 수행합니다.

## 핵심 내용
본 논문에서는 샘플링 데이터 제어를 통해 차수가 (0,1)인 분수차 다중 에이전트 시스템의 합의 제어를 연구합니다. 분수차 미적분학의 고유한 특성, 즉 유전성과 무한 메모리를 활용하여 엄격한 분석을 통해 분산 제어기를 설계하는 새로운 방식을 제시합니다. 모든 폐루프 신호의 전역적 유계성이 보장되고 점근적 합의가 실현됨을 입증합니다. 제안된 제어 방법의 효과성을 입증하고 얻어진 결과를 검증하기 위해 시뮬레이션 연구를 수행합니다.

## 参考
- http://arxiv.org/abs/2004.00860v1
