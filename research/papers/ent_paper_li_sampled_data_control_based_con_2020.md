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
  zh: 本文提出了一种面向分数阶多智能体系统的分布式采样数据控制器，通过补偿历史控制输入来体现分数阶微积分的遗传性与无限记忆特性，并证明了闭环信号全局有界性与渐近平均一致性。
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2004.00860v1.
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
In this paper, we investigate consensus control of fractional-order multi-agent systems with order in (0,1) via sampled-data control. A new scheme to design distributed controllers with rigorous analysis is presented by utilizing the unique properties of fractional-order calculus, namely hereditary and infinite memory. It is established that global boundedness of all closed-loop signals is ensured and asymptotic consensus is realized. Simulation studies are conducted to illustrate the effectiveness of the proposed control method and verify the obtained results.

## 核心内容
In this paper, we investigate consensus control of fractional-order multi-agent systems with order in (0,1) via sampled-data control. A new scheme to design distributed controllers with rigorous analysis is presented by utilizing the unique properties of fractional-order calculus, namely hereditary and infinite memory. It is established that global boundedness of all closed-loop signals is ensured and asymptotic consensus is realized. Simulation studies are conducted to illustrate the effectiveness of the proposed control method and verify the obtained results.

## 参考
- http://arxiv.org/abs/2004.00860v1

