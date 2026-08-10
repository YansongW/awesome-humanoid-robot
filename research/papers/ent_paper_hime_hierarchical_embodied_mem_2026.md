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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.03449v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (696 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2607.03449v1

## 개요
현재 VLA 모델은 로봇 조작에서 뛰어난 성능을 보이지만, 장기 기억과 추론이 필요한 비마르코프 과제에서는 즉각적인 관측에 의존하여 성능이 저조합니다. 기존 접근법은 '빈도-능력 역설'에 직면합니다: 강력한 추론 모델은 속도가 너무 느려 실시간 제어에 사용할 수 없고, 빠른 모델은 충분한 추론 능력을 갖추지 못합니다. HiMe 프레임워크는 임베디드 지능을 고주파 실행기, 작업 기억 센트리, 장기 전략 플래너로 분리하고, 교차 모달 의미 패턴 기반의 동적 지식 시스템을 도입하여 '추가, 업데이트, 삭제' 작업을 통해 기억 가소성을 유지함으로써 실시간 실행과 느린 추론 간의 충돌을 효과적으로 균형 있게 해결합니다.

## 핵심 내용
### 방법 아키텍처
HiMe 프레임워크는 임베디드 지능을 세 가지 계층으로 분리합니다:
- **고주파 실행기 (Executor)**: 실시간 제어와 동작 실행을 담당하여 고주파 응답을 보장합니다.
- **작업 기억 센트리 (Sentry)**: 단기 작업 기억을 유지하고 현재 작업과 관련된 컨텍스트 정보를 처리합니다.
- **장기 전략 플래너 (Planner)**: 장기 전략 수립과 추론을 담당하며 느린 사고가 필요한 복잡한 계획을 처리합니다.

### 동적 지식 시스템
- **교차 모달 의미 패턴** 기반으로 지식 표현을 구축하여 시각, 언어, 동작 정보의 융합을 지원합니다.
- 능동적 관리 메커니즘을 도입하여 '추가, 업데이트, 삭제' 작업을 통해 기억 가소성을 실현하며, 로봇이 인간의 선호도에 따라 내부 지식을 자기 수정할 수 있게 합니다.

### 실험 설정 및 주요 수치
- 실험은 장기 시간 도메인 작업에서 수행되었으며, **플랫 기억 베이스라인** 방법과 비교했습니다.
- HiMe는 성공률에서 베이스라인보다 현저히 우수하며, 인간 선호도에 기반한 내부 지식 자기 수정이라는 새로운 능력을 보여줍니다.
- 구체적인 수치는 초록에 제시되지 않았지만, 프레임워크는 실시간 실행과 느린 추론 간의 충돌을 효과적으로 해결합니다.

### 결론
HiMe는 계층적 기억 설계를 통해 VLA 모델의 장기 시간 도메인 작업에서의 기억 및 추론 병목을 성공적으로 극복하여, 로봇의 장기 자율 운영을 위한 새로운 패러다임을 제공합니다.
