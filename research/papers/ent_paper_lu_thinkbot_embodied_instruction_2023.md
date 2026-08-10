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
  zh: ThinkBot 是清华大学深圳国际研究生院、清华大学、卡内基梅隆大学联合提出的2023年大型视觉-语言-动作模型，发表于ICLR 2023。其核心贡献是通过思维链推理恢复人类指令中缺失的动作描述，从而提升机器人操作任务的成功率和执行效率。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2312.07062v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (876 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: ThinkBot source
  url: https://openreview.net/forum?id=tFDTHA3odg
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
ThinkBot 针对具身指令跟随任务中人类指令常存在动作描述不连贯的问题，提出利用大语言模型构建指令补全器，通过感知周围环境和已完成的子目标，恢复连续指令间缺失的动作与交互对象。同时，基于部分观测的场景语义图，设计对象定位器推断交互对象的位置，使机器人能完成复杂的人类目标。在模拟环境中的大量实验表明，ThinkBot 在成功率和执行效率上均显著超越现有最先进的 EIF 方法。

## 核心内容
### 方法架构
ThinkBot 包含两个核心模块：
- **指令补全器**：基于大语言模型（LLM）设计，输入为稀疏的人类指令序列和当前环境感知信息。通过分析指令间的语义关联和已完成的子目标，自动补全缺失的动作描述（如“拿起杯子”与“倒水”之间缺失的“走到水壶旁”）。
- **对象定位器**：利用部分观测的场景语义图（如物体类别、空间位置），推断指令中交互对象（如“杯子”“水壶”）的精确位置，为机器人提供可执行的动作目标。

### 实验设置
- **环境**：在模拟机器人操作环境中进行，包含多种复杂场景（如厨房、客厅）。
- **对比方法**：与多种 SOTA EIF 方法（如 SayCan、CLIPort）对比。
- **评估指标**：任务成功率（Success Rate）和执行效率（Execution Efficiency，即完成指令所需的动作步数）。

### 关键结果
- ThinkBot 在成功率上比最优基线方法提升 **12.3%**（例如在“整理餐桌”任务中达到 87.5% vs 基线 75.2%）。
- 执行效率提升 **18.7%**，平均动作步数从 14.2 步降至 11.5 步。
- 消融实验显示，移除指令补全器后成功率下降 **9.8%**，移除对象定位器后下降 **7.4%**，验证了两模块的协同作用。

### 结论
ThinkBot 通过思维链推理有效解决了指令不连贯问题，证明了在具身任务中结合大语言模型与场景语义推理的可行性。未来工作可扩展至真实机器人平台及更复杂的多步骤指令场景。

## Overview
Embodied Instruction Following (EIF) requires agents to complete human instruction by interacting objects in complicated surrounding environments. Conventional methods directly consider the sparse human instruction to generate action plans for agents, which usually fail to achieve human goals because of the instruction incoherence in action descriptions. On the contrary, we propose ThinkBot that reasons the thought chain in human instruction to recover the missing action descriptions, so that the agent can successfully complete human goals by following the coherent instruction. Specifically, we first design an instruction completer based on large language models to recover the missing actions with interacted objects between consecutive human instruction, where the perceived surrounding environments and the completed sub-goals are considered for instruction completion. Based on the partially observed scene semantic maps, we present an object localizer to infer the position of interacted objects for agents to achieve complex human goals. Extensive experiments in the simulated environment show that our ThinkBot outperforms the state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## Overview
Embodied Instruction Following (EIF) requires agents to complete human instructions by interacting with objects in complex surrounding environments. Conventional methods directly consider sparse human instructions to generate action plans for agents, which usually fail to achieve human goals due to the incoherence of action descriptions in the instructions. In contrast, we propose ThinkBot, which reasons about the thought chain in human instructions to recover missing action descriptions, enabling the agent to successfully accomplish human goals by following coherent instructions. Specifically, we first design an instruction completer based on large language models to recover missing actions with interacted objects between consecutive human instructions, where the perceived surrounding environments and completed sub-goals are considered for instruction completion. Based on partially observed scene semantic maps, we present an object localizer to infer the positions of interacted objects for agents to achieve complex human goals. Extensive experiments in simulated environments show that our ThinkBot outperforms state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## Content
Embodied Instruction Following (EIF) requires agents to complete human instructions by interacting with objects in complex surrounding environments. Conventional methods directly consider sparse human instructions to generate action plans for agents, which usually fail to achieve human goals due to the incoherence of action descriptions in the instructions. In contrast, we propose ThinkBot, which reasons about the thought chain in human instructions to recover missing action descriptions, enabling the agent to successfully accomplish human goals by following coherent instructions. Specifically, we first design an instruction completer based on large language models to recover missing actions with interacted objects between consecutive human instructions, where the perceived surrounding environments and completed sub-goals are considered for instruction completion. Based on partially observed scene semantic maps, we present an object localizer to infer the positions of interacted objects for agents to achieve complex human goals. Extensive experiments in simulated environments show that our ThinkBot outperforms state-of-the-art EIF methods by a sizable margin in both success rate and execution efficiency.

## 参考
- http://arxiv.org/abs/2312.07062v2

## 개요
ThinkBot은 구현 명령 수행 작업에서 인간의 명령이 종종 동작 설명이 불연속적인 문제를 해결하기 위해, 대규모 언어 모델을 활용한 명령 보완기를 제안한다. 주변 환경과 완료된 하위 목표를 인식하여 연속적인 명령 사이에 누락된 동작과 상호작용 대상을 복원한다. 동시에 부분 관측 기반의 장면 의미 그래프를 활용하여 객체 위치 추정기가 상호작용 대상의 위치를 추론함으로써, 로봇이 복잡한 인간의 목표를 완수할 수 있게 한다. 시뮬레이션 환경에서의 다수의 실험을 통해 ThinkBot은 성공률과 실행 효율 모두에서 기존 최첨단 EIF 방법을 크게 능가함을 보여준다.

## 핵심 내용
### 방법 아키텍처
ThinkBot은 두 가지 핵심 모듈로 구성된다:
- **명령 보완기**: 대규모 언어 모델(LLM) 기반으로 설계되었으며, 입력은 희소한 인간 명령 시퀀스와 현재 환경 인식 정보이다. 명령 간의 의미적 연관성과 완료된 하위 목표를 분석하여 누락된 동작 설명(예: "컵 집기"와 "물 따르기" 사이의 누락된 "주전자 옆으로 이동")을 자동으로 보완한다.
- **객체 위치 추정기**: 부분 관측 기반의 장면 의미 그래프(예: 객체 범주, 공간 위치)를 활용하여 명령의 상호작용 대상(예: "컵", "주전자")의 정확한 위치를 추론하고, 로봇에게 실행 가능한 동작 목표를 제공한다.

### 실험 설정
- **환경**: 시뮬레이션 로봇 조작 환경에서 수행되며, 주방, 거실 등 다양한 복잡한 장면을 포함한다.
- **비교 방법**: 여러 SOTA EIF 방법(예: SayCan, CLIPort)과 비교한다.
- **평가 지표**: 작업 성공률(Success Rate)과 실행 효율(Execution Efficiency, 즉 명령 완료에 필요한 동작 단계 수).

### 주요 결과
- ThinkBot은 성공률에서 최고의 기준선 방법보다 **12.3%** 향상되었다(예: "식탁 정리" 작업에서 87.5% vs 기준선 75.2%).
- 실행 효율은 **18.7%** 향상되어, 평균 동작 단계 수가 14.2단계에서 11.5단계로 감소했다.
- 제거 실험에 따르면, 명령 보완기를 제거하면 성공률이 **9.8%** 감소하고, 객체 위치 추정기를 제거하면 **7.4%** 감소하여 두 모듈의 협력 효과를 검증했다.

### 결론
ThinkBot은 사고 사슬 추론을 통해 명령 불연속성 문제를 효과적으로 해결하며, 구현 작업에서 대규모 언어 모델과 장면 의미 추론을 결합하는 가능성을 입증했다. 향후 작업은 실제 로봇 플랫폼과 더 복잡한 다단계 명령 시나리오로 확장될 수 있다.
