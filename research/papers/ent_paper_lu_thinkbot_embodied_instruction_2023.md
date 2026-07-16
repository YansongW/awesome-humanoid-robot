---
$id: ent_paper_lu_thinkbot_embodied_instruction_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning'
  zh: ThinkBot
  ko: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning'
summary:
  en: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning (ThinkBot), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tsinghua University, Carnegie
    Mellon University, Department of Automation, Tsinghua University, and published at ICLR 2023.'
  zh: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning (ThinkBot), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tsinghua University, Carnegie
    Mellon University, Department of Automation, Tsinghua University, and published at ICLR 2023.'
  ko: 'ThinkBot: Embodied Instruction Following with Thought Chain Reasoning (ThinkBot), is a 2023 large vision-language-action
    model for robotic manipulation, introduced by Tsinghua Shenzhen International Graduate School, Tsinghua University, Carnegie
    Mellon University, Department of Automation, Tsinghua University, and published at ICLR 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- robotic_manipulation
- thinkbot
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.07062v2.
sources:
- id: src_001
  type: paper
  title: ThinkBot source
  url: https://openreview.net/forum?id=tFDTHA3odg
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Embodied Instruction Following (EIF) requires agents to complete human instruction by interacting objects in complicated surrounding environments. Conventional methods directly consider the sparse human instruction to generate action plans for agents, which usually fail to achieve human goals because of the instruction incoherence in action descriptions. On the contrary, we propose ThinkBot that reasons the thought chain in human instruction to recover the missing action descriptions, so that the agent can successfully complete human goals by following the coherent instruction. Specifically, we first design an instruction completer based on large language models to recover the missing actions with interacted objects between consecutive human instruction, where the perceived surrounding environments and the completed sub-goals are considered for instruction completion. Based on the partially observed scene semantic maps, we present an object localizer to infer the position of interacted objects for agents to achieve complex human goals. Extensive experiments in the simulated environment show that our ThinkBot outperforms the state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## 核心内容
Embodied Instruction Following (EIF) requires agents to complete human instruction by interacting objects in complicated surrounding environments. Conventional methods directly consider the sparse human instruction to generate action plans for agents, which usually fail to achieve human goals because of the instruction incoherence in action descriptions. On the contrary, we propose ThinkBot that reasons the thought chain in human instruction to recover the missing action descriptions, so that the agent can successfully complete human goals by following the coherent instruction. Specifically, we first design an instruction completer based on large language models to recover the missing actions with interacted objects between consecutive human instruction, where the perceived surrounding environments and the completed sub-goals are considered for instruction completion. Based on the partially observed scene semantic maps, we present an object localizer to infer the position of interacted objects for agents to achieve complex human goals. Extensive experiments in the simulated environment show that our ThinkBot outperforms the state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## 参考
- http://arxiv.org/abs/2312.07062v2

## Overview
Embodied Instruction Following (EIF) requires agents to complete human instructions by interacting with objects in complex surrounding environments. Conventional methods directly consider sparse human instructions to generate action plans for agents, which usually fail to achieve human goals due to the incoherence of action descriptions in the instructions. In contrast, we propose ThinkBot, which reasons about the thought chain in human instructions to recover missing action descriptions, enabling the agent to successfully accomplish human goals by following coherent instructions. Specifically, we first design an instruction completer based on large language models to recover missing actions with interacted objects between consecutive human instructions, where the perceived surrounding environments and completed sub-goals are considered for instruction completion. Based on partially observed scene semantic maps, we present an object localizer to infer the positions of interacted objects for agents to achieve complex human goals. Extensive experiments in simulated environments show that our ThinkBot outperforms state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## Content
Embodied Instruction Following (EIF) requires agents to complete human instructions by interacting with objects in complex surrounding environments. Conventional methods directly consider sparse human instructions to generate action plans for agents, which usually fail to achieve human goals due to the incoherence of action descriptions in the instructions. In contrast, we propose ThinkBot, which reasons about the thought chain in human instructions to recover missing action descriptions, enabling the agent to successfully accomplish human goals by following coherent instructions. Specifically, we first design an instruction completer based on large language models to recover missing actions with interacted objects between consecutive human instructions, where the perceived surrounding environments and completed sub-goals are considered for instruction completion. Based on partially observed scene semantic maps, we present an object localizer to infer the positions of interacted objects for agents to achieve complex human goals. Extensive experiments in simulated environments show that our ThinkBot outperforms state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## 개요
Embodied Instruction Following (EIF)는 에이전트가 복잡한 주변 환경에서 객체와 상호작용하여 인간의 지시를 완료하도록 요구합니다. 기존 방법들은 일반적으로 희소한 인간 지시를 직접 고려하여 에이전트의 행동 계획을 생성하지만, 이는 행동 설명의 지시 불일치로 인해 인간의 목표를 달성하지 못하는 경우가 많습니다. 이와 달리, 우리는 ThinkBot을 제안하여 인간 지시의 사고 체인을 추론함으로써 누락된 행동 설명을 복원하고, 에이전트가 일관된 지시를 따라 인간의 목표를 성공적으로 완료할 수 있도록 합니다. 구체적으로, 먼저 대규모 언어 모델 기반의 지시 완성기를 설계하여 연속된 인간 지시 사이의 상호작용 객체와 함께 누락된 행동을 복원하며, 이때 인식된 주변 환경과 완료된 하위 목표를 지시 완성에 고려합니다. 부분적으로 관찰된 장면 의미 맵을 기반으로, 객체 위치 추정기를 제시하여 에이전트가 복잡한 인간 목표를 달성할 수 있도록 상호작용 객체의 위치를 추론합니다. 시뮬레이션 환경에서의 광범위한 실험 결과, ThinkBot은 성공률과 실행 효율성 모두에서 최신 EIF 방법들을 상당한 차이로 능가함을 보여줍니다.

## 핵심 내용
Embodied Instruction Following (EIF)는 에이전트가 복잡한 주변 환경에서 객체와 상호작용하여 인간의 지시를 완료하도록 요구합니다. 기존 방법들은 일반적으로 희소한 인간 지시를 직접 고려하여 에이전트의 행동 계획을 생성하지만, 이는 행동 설명의 지시 불일치로 인해 인간의 목표를 달성하지 못하는 경우가 많습니다. 이와 달리, 우리는 ThinkBot을 제안하여 인간 지시의 사고 체인을 추론함으로써 누락된 행동 설명을 복원하고, 에이전트가 일관된 지시를 따라 인간의 목표를 성공적으로 완료할 수 있도록 합니다. 구체적으로, 먼저 대규모 언어 모델 기반의 지시 완성기를 설계하여 연속된 인간 지시 사이의 상호작용 객체와 함께 누락된 행동을 복원하며, 이때 인식된 주변 환경과 완료된 하위 목표를 지시 완성에 고려합니다. 부분적으로 관찰된 장면 의미 맵을 기반으로, 객체 위치 추정기를 제시하여 에이전트가 복잡한 인간 목표를 달성할 수 있도록 상호작용 객체의 위치를 추론합니다. 시뮬레이션 환경에서의 광범위한 실험 결과, ThinkBot은 성공률과 실행 효율성 모두에서 최신 EIF 방법들을 상당한 차이로 능가함을 보여줍니다.
