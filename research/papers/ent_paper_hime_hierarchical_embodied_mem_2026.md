---
$id: ent_paper_hime_hierarchical_embodied_mem_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control'
  zh: 'HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control'
  ko: 'HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control'
summary:
  en: 'arXiv:2607.03449v1 Announce Type: new Abstract: Current Vision-Language-Action (VLA) models excel at robotic manipulation
    but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate
    observations. Existing solutions face a ''''frequency-competence paradox,'''' where stronger reasoning models are too
    slow for real-time control, while faster models lack sufficient reasoning capabilities. To resolve this architectural
    misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency
    Executor for execution, a Sentry for working memory, and a Planner for long-term strategy. We also introduce a dynamic
    knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory
    plasticity through ''''Add, Update, and Delete'''' operations. This hierarchical design effectively balances the conflict
    between real-time execution and slow thinking planning, significantly improving success rates in long-horizon tasks. Experiments
    demonstrate that this approach not only outperforms flat memory baselines but also exhibits the novel ability to self-correct
    its internal knowledge based on human preferences.'
  zh: HiMe 是一个由研究者提出的分层具身记忆框架，旨在解决当前 Vision-Language-Action (VLA) 模型在长时域任务中因依赖即时观测而缺乏长期记忆与推理能力的问题。其核心贡献在于通过将具身智能解耦为高频执行器、工作记忆哨兵和长期策略规划器三个层次，并引入基于跨模态语义模式的动态知识系统，有效平衡了实时执行与慢速推理之间的冲突，显著提升了长时域任务的成功率。
  ko: 'arXiv:2607.03449v1 Announce Type: new Abstract: Current Vision-Language-Action (VLA) models excel at robotic manipulation
    but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate
    observations. Existing solutions face a ''''frequency-competence paradox,'''' where stronger reasoning models are too
    slow for real-time control, while faster models lack sufficient reasoning capabilities. To resolve this architectural
    misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency
    Executor for execution, a Sentry for working memory, and a Planner for long-term strategy. We also introduce a dynamic
    knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory
    plasticity through ''''Add, Update, and Delete'''' operations. This hierarchical design effectively balances the conflict
    between real-time execution and slow thinking planning, significantly improving success rates in long-horizon tasks. Experiments
    demonstrate that this approach not only outperforms flat memory baselines but also exhibits the novel ability to self-correct
    its internal knowledge based on human preferences.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- robotics
- hime
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03449v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'HiMe: Hierarchical Embodied Memory for Long-Horizon Vision-Language-Action Control (arXiv)'
  url: https://arxiv.org/abs/2607.03449
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
当前 VLA 模型在机器人操作中表现出色，但面对需要长期记忆和推理的非马尔可夫任务时，因依赖即时观测而表现不佳。现有方案面临“频率-能力悖论”：强推理模型速度过慢无法用于实时控制，而快速模型又缺乏足够的推理能力。HiMe 框架通过将具身智能解耦为高频执行器、工作记忆哨兵和长期策略规划器，并引入基于跨模态语义模式的动态知识系统，实现了“添加、更新、删除”操作以保持记忆可塑性，从而有效平衡实时执行与慢速推理之间的冲突。

## 核心内容
### 方法架构
HiMe 框架将具身智能解耦为三个层次：
- **高频执行器 (Executor)**：负责实时控制与动作执行，确保高频响应。
- **工作记忆哨兵 (Sentry)**：维护短期工作记忆，处理当前任务相关的上下文信息。
- **长期策略规划器 (Planner)**：负责长期策略制定与推理，处理需要慢速思考的复杂规划。

### 动态知识系统
- 基于**跨模态语义模式**构建知识表示，支持视觉、语言与动作信息的融合。
- 引入主动管理机制，通过“添加、更新、删除”操作实现记忆可塑性，使机器人能够根据人类偏好自我修正内部知识。

### 实验设置与关键数字
- 实验在长时域任务上进行，对比了**扁平记忆基线**方法。
- HiMe 在成功率上显著优于基线，并展现出基于人类偏好自我修正内部知识的新能力。
- 具体数字未在摘要中给出，但框架有效解决了实时执行与慢速推理之间的冲突。

### 结论
HiMe 通过分层记忆设计，成功克服了 VLA 模型在长时域任务中的记忆与推理瓶颈，为机器人长期自主操作提供了新范式。

## Overview
Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate observations. Existing solutions face a ''frequency-competence paradox,'' where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities. To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry for working memory, and a Planner for long-term strategy. We also introduce a dynamic knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory plasticity through ''Add, Update, and Delete'' operations. This hierarchical design effectively balances the conflict between real-time execution and slow thinking planning, significantly improving success rates in long-horizon tasks. Experiments demonstrate that this approach not only outperforms flat memory baselines but also exhibits the novel ability to self-correct its internal knowledge based on human preferences.

## Overview
Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate observations. Existing solutions face a "frequency-competence paradox," where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities. To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry for working memory, and a Planner for long-term strategy. We also introduce a dynamic knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory plasticity through "Add, Update, and Delete" operations. This hierarchical design effectively balances the conflict between real-time execution and slow thinking planning, significantly improving success rates in long-horizon tasks. Experiments demonstrate that this approach not only outperforms flat memory baselines but also exhibits the novel ability to self-correct its internal knowledge based on human preferences.

## Content
Current Vision-Language-Action (VLA) models excel at robotic manipulation but often struggle with non-Markovian tasks requiring long-term memory and reasoning due to their reliance on immediate observations. Existing solutions face a "frequency-competence paradox," where stronger reasoning models are too slow for real-time control, while faster models lack sufficient reasoning capabilities. To resolve this architectural misalignment, we propose HiMe, a Hierarchical Embodied Memory framework that decouples embodied intelligence into a high-frequency Executor for execution, a Sentry for working memory, and a Planner for long-term strategy. We also introduce a dynamic knowledge system based on cross-modal semantic schemas and active management mechanisms, allowing robots to maintain memory plasticity through "Add, Update, and Delete" operations. This hierarchical design effectively balances the conflict between real-time execution and slow thinking planning, significantly improving success rates in long-horizon tasks. Experiments demonstrate that this approach not only outperforms flat memory baselines but also exhibits the novel ability to self-correct its internal knowledge based on human preferences.

## 개요
현재의 Vision-Language-Action (VLA) 모델은 로봇 조작에 뛰어나지만, 즉각적인 관찰에 의존하기 때문에 장기 기억과 추론이 필요한 비마르코프 작업에서는 종종 어려움을 겪습니다. 기존 솔루션은 '빈도-능력 역설'에 직면해 있으며, 더 강력한 추론 모델은 실시간 제어에 너무 느리고, 더 빠른 모델은 충분한 추론 능력을 갖추지 못합니다. 이러한 구조적 부정합을 해결하기 위해, 우리는 HiMe(계층적 체화 기억 프레임워크)를 제안합니다. 이 프레임워크는 체화 지능을 실행을 위한 고빈도 실행기(Executor), 작업 기억을 위한 센트리(Sentry), 장기 전략을 위한 플래너(Planner)로 분리합니다. 또한, 교차 모달 의미 스키마와 능동 관리 메커니즘에 기반한 동적 지식 시스템을 도입하여, 로봇이 '추가, 업데이트, 삭제' 작업을 통해 기억 가소성을 유지할 수 있도록 합니다. 이 계층적 설계는 실시간 실행과 느린 사고 계획 간의 충돌을 효과적으로 균형 잡아, 장기 작업에서 성공률을 크게 향상시킵니다. 실험 결과, 이 접근 방식은 평면 기억 기준선을 능가할 뿐만 아니라, 인간의 선호도에 따라 내부 지식을 스스로 교정하는 새로운 능력을 보여줍니다.

## 핵심 내용
현재의 Vision-Language-Action (VLA) 모델은 로봇 조작에 뛰어나지만, 즉각적인 관찰에 의존하기 때문에 장기 기억과 추론이 필요한 비마르코프 작업에서는 종종 어려움을 겪습니다. 기존 솔루션은 '빈도-능력 역설'에 직면해 있으며, 더 강력한 추론 모델은 실시간 제어에 너무 느리고, 더 빠른 모델은 충분한 추론 능력을 갖추지 못합니다. 이러한 구조적 부정합을 해결하기 위해, 우리는 HiMe(계층적 체화 기억 프레임워크)를 제안합니다. 이 프레임워크는 체화 지능을 실행을 위한 고빈도 실행기(Executor), 작업 기억을 위한 센트리(Sentry), 장기 전략을 위한 플래너(Planner)로 분리합니다. 또한, 교차 모달 의미 스키마와 능동 관리 메커니즘에 기반한 동적 지식 시스템을 도입하여, 로봇이 '추가, 업데이트, 삭제' 작업을 통해 기억 가소성을 유지할 수 있도록 합니다. 이 계층적 설계는 실시간 실행과 느린 사고 계획 간의 충돌을 효과적으로 균형 잡아, 장기 작업에서 성공률을 크게 향상시킵니다. 실험 결과, 이 접근 방식은 평면 기억 기준선을 능가할 뿐만 아니라, 인간의 선호도에 따라 내부 지식을 스스로 교정하는 새로운 능력을 보여줍니다.

## 参考
- http://arxiv.org/abs/2607.03449v1
