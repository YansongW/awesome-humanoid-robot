---
$id: ent_paper_wang_physiagent_an_embodied_agent_f_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PhysiAgent: An Embodied Agent Framework in Physical World'
  zh: PhysiAgent
  ko: 'PhysiAgent: An Embodied Agent Framework in Physical World'
summary:
  en: 'PhysiAgent: An Embodied Agent Framework in Physical World (PhysiAgent), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua University, Peking University,
    University of California, Berkeley.'
  zh: PhysiAgent 是由清华大学 AIR、北京大学及 UC Berkeley 联合提出的具身智能体框架，旨在解决 VLA 模型泛化性不足的问题。其核心贡献在于通过监控、记忆、自反思机制及轻量工具包，让 VLM 根据 VLA 的实时能力反馈自主组织组件，从而最大化
    VLA 的潜力。实验表明，该框架在复杂真实机器人任务中显著提升了任务解决性能。
  ko: 'PhysiAgent: An Embodied Agent Framework in Physical World (PhysiAgent), is a 2025 large vision-language-action model
    for robotic manipulation, introduced by Institute for AI Industry Research (AIR), Tsinghua University, Peking University,
    University of California, Berkeley.'
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
- physiagent
- robotic_manipulation
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.24524v1. [2026-07-29] zh
    content backfilled from English abstract via scripts/sinicize_english_cards.py
sources:
- id: src_001
  type: paper
  title: 'PhysiAgent: An Embodied Agent Framework in Physical World (arXiv)'
  url: https://arxiv.org/abs/2509.24524
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: PhysiAgent source
  url: https://doi.org/10.48550/arXiv.2509.24524
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
PhysiAgent 是一个面向物理世界的具身智能体框架，由清华大学 AIR、北京大学及 UC Berkeley 于 2025 年提出。该框架针对当前 VLM 与 VLA 模型在刚性顺序结构中协作低效的问题，引入了监控、记忆、自反思机制及轻量工具包。通过让 VLM 基于 VLA 的实时能力反馈自主组织组件，PhysiAgent 实现了有效的自我调节与工具协作。实验结果显示，该框架在复杂真实机器人任务中取得了显著性能提升，展现了自适应演化能力。

## 核心内容
### 方法
PhysiAgent 提出了一种自主脚手架框架，通过以下机制实现 VLM 与 VLA 的有效协作：
- **监控模块**：实时追踪 VLA 的执行状态与能力反馈。
- **记忆模块**：存储历史任务经验，支持长期学习。
- **自反思机制**：基于反馈动态调整 VLM 的组件组织策略。
- **轻量工具包**：集成现成工具，增强框架的灵活性与实用性。

### 架构
PhysiAgent 采用非刚性顺序结构，VLM 不再仅负责高层场景理解与任务规划，而是根据 VLA 的实时能力反馈自主调用不同组件。这种设计避免了传统方法中 VLM 与 VLA 协作低效的问题，提升了接地能力。

### 实验设置
- **任务**：复杂真实世界机器人操作任务。
- **评估指标**：任务完成率、协作效率及自适应演化能力。

### 关键结果
- 在复杂真实机器人任务中，PhysiAgent 显著提升了任务解决性能。
- 展示了 VLM 的有效自我调节能力，工具协作连贯且框架在执行过程中自适应演化。

### 结论
PhysiAgent 为将 VLM 与 VLA 集成到具身智能体框架中提供了实用且开创性的尝试，有效实现了在真实世界环境中的接地应用。

## Overview
Vision-Language-Action (VLA) models have achieved notable success but often struggle with limited generalizations. To address this, integrating generalized Vision-Language Models (VLMs) as assistants to VLAs has emerged as a popular solution. However, current approaches often combine these models in rigid, sequential structures: using VLMs primarily for high-level scene understanding and task planning, and VLAs merely as executors of lower-level actions, leading to ineffective collaboration and poor grounding challenges. In this paper, we propose an embodied agent framework, PhysiAgent, tailored to operate effectively in physical environments. By incorporating monitor, memory, self-reflection mechanisms, and lightweight off-the-shelf toolboxes, PhysiAgent offers an autonomous scaffolding framework to prompt VLMs to organize different components based on real-time proficiency feedback from VLAs to maximally exploit VLAs' capabilities. Experimental results demonstrate significant improvements in task-solving performance on complex real-world robotic tasks, showcasing effective self-regulation of VLMs, coherent tool collaboration, and adaptive evolution of the framework during execution. PhysiAgent makes practical and pioneering efforts to integrate VLMs and VLAs, effectively grounding embodied agent frameworks in real-world settings.

## 개요
Vision-Language-Action (VLA) 모델은 주목할 만한 성과를 거두었지만, 종종 제한된 일반화 능력으로 어려움을 겪습니다. 이를 해결하기 위해, 일반화된 Vision-Language Models (VLM)을 VLA의 보조자로 통합하는 것이 인기 있는 해결책으로 떠오르고 있습니다. 그러나 현재 접근 방식은 이러한 모델들을 경직된 순차적 구조로 결합하는 경우가 많습니다. 즉, VLM은 주로 고수준의 장면 이해와 작업 계획에 사용되고, VLA는 단순히 저수준 동작의 실행자 역할만 하여 비효율적인 협업과 취약한 근거(grounding) 문제를 초래합니다. 본 논문에서는 물리적 환경에서 효과적으로 작동하도록 설계된 임베디드 에이전트 프레임워크인 PhysiAgent를 제안합니다. 모니터, 메모리, 자기 성찰 메커니즘, 그리고 가벼운 기성 도구 상자를 통합함으로써, PhysiAgent는 VLA의 실시간 숙련도 피드백을 기반으로 VLM이 다양한 구성 요소를 조직하여 VLA의 능력을 최대한 활용하도록 유도하는 자율적 스캐폴딩 프레임워크를 제공합니다. 실험 결과는 복잡한 실제 로봇 작업에서 작업 해결 성능이 크게 향상되었음을 보여주며, VLM의 효과적인 자기 조절, 일관된 도구 협업, 그리고 실행 중 프레임워크의 적응적 진화를 입증합니다. PhysiAgent는 VLM과 VLA를 통합하고 임베디드 에이전트 프레임워크를 실제 환경에 효과적으로 근거시키는 실용적이고 선구적인 노력을 기울입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 주목할 만한 성과를 거두었지만, 종종 제한된 일반화 능력으로 어려움을 겪습니다. 이를 해결하기 위해, 일반화된 Vision-Language Models (VLM)을 VLA의 보조자로 통합하는 것이 인기 있는 해결책으로 떠오르고 있습니다. 그러나 현재 접근 방식은 이러한 모델들을 경직된 순차적 구조로 결합하는 경우가 많습니다. 즉, VLM은 주로 고수준의 장면 이해와 작업 계획에 사용되고, VLA는 단순히 저수준 동작의 실행자 역할만 하여 비효율적인 협업과 취약한 근거(grounding) 문제를 초래합니다. 본 논문에서는 물리적 환경에서 효과적으로 작동하도록 설계된 임베디드 에이전트 프레임워크인 PhysiAgent를 제안합니다. 모니터, 메모리, 자기 성찰 메커니즘, 그리고 가벼운 기성 도구 상자를 통합함으로써, PhysiAgent는 VLA의 실시간 숙련도 피드백을 기반으로 VLM이 다양한 구성 요소를 조직하여 VLA의 능력을 최대한 활용하도록 유도하는 자율적 스캐폴딩 프레임워크를 제공합니다. 실험 결과는 복잡한 실제 로봇 작업에서 작업 해결 성능이 크게 향상되었음을 보여주며, VLM의 효과적인 자기 조절, 일관된 도구 협업, 그리고 실행 중 프레임워크의 적응적 진화를 입증합니다. PhysiAgent는 VLM과 VLA를 통합하고 임베디드 에이전트 프레임워크를 실제 환경에 효과적으로 근거시키는 실용적이고 선구적인 노력을 기울입니다.

## 参考
- http://arxiv.org/abs/2509.24524v1
