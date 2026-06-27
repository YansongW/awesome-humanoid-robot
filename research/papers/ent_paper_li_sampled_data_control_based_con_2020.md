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
  en: This paper proposes a distributed sampled-data controller for fractional-order
    multi-agent systems that compensates for historical control inputs to account
    for the hereditary and infinite memory properties of fractional-order calculus,
    with proofs of global boundedness and asymptotic average consensus.
  zh: 本文提出了一种面向分数阶多智能体系统的分布式采样数据控制器，通过补偿历史控制输入来体现分数阶微积分的遗传性与无限记忆特性，并证明了闭环信号全局有界性与渐近平均一致性。
  ko: 본 논문은 분수 차수 미적분학의 유전적이고 무한한 기억 특성을 고려하기 위해 과거 제어 입력을 보상하는 분수 차수 다중 에이전트 시스템을
    위한 분산 샘플링 데이터 제어기를 제안하고, 전역 유계성과 점근적 평균 합의를 증명한다.
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
  reviewed_at: '2026-06-27'
  confidence: medium
  notes: AI-extracted from provided metadata and abstract; requires human review against
    the full arXiv text before verification.
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

## Overview

This paper investigates consensus control for fractional-order multi-agent systems with order in (0, 1) using sampled-data control. The authors highlight that fractional-order calculus exhibits hereditary and infinite memory properties, which existing sampled-data control approaches for integer-order systems do not adequately account for. To address this gap, they propose a novel distributed controller that includes a compensating term based on all previous control inputs, enabling the closed-loop error dynamics to be analyzed similarly to integer-order discrete-time consensus systems.

The proposed control law is applied to agents modeled as one-dimensional fractional-order single-integrators communicating over a strongly connected and balanced directed graph. The authors establish that all closed-loop signals remain globally bounded and that the agents achieve asymptotic average consensus. Simulation studies compare the proposed method against an existing sampled-data control approach, demonstrating improved asymptotic consensus accuracy.

## Key Contributions

- Novel distributed sampled-data control scheme for fractional-order multi-agent systems that explicitly incorporates the hereditary and infinite memory properties of fractional-order calculus.
- Rigorous proof of global boundedness of all closed-loop signals and asymptotic average consensus under strongly connected and balanced communication graphs.
- Controller compensation for historical control inputs rather than resetting initial values at each sampling interval, allowing integer-order-style discrete-time analysis.
- Simulation comparison showing that the proposed method achieves better asymptotic consensus accuracy than an existing sampled-data method.

## Relevance to Humanoid Robotics

Although the paper is theoretical and does not address humanoid hardware directly, its distributed consensus and sampled-data control principles are relevant to fleet-level coordination of multiple humanoid robots. Synchronization, formation control, and cooperative locomotion for groups of humanoids could potentially build on such multi-agent consensus methods. However, the current formulation assumes one-dimensional single-integrator dynamics and idealized communication, so significant extension would be needed for practical humanoid deployment.
