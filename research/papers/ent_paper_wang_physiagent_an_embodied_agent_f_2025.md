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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.24524v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (768 chars, DeepSeek).'
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

## 参考
- http://arxiv.org/abs/2509.24524v1

## 개요
PhysiAgent는 물리 세계를 대상으로 하는 구현형 에이전트 프레임워크로, 칭화대학교 AIR, 베이징대학교 및 UC Berkeley가 2025년에 제안했습니다. 이 프레임워크는 현재 VLM과 VLA 모델이 경직된 순차 구조에서 협력 효율성이 낮은 문제를 해결하기 위해 모니터링, 메모리, 자기 반성 메커니즘 및 경량 도구 키트를 도입했습니다. VLM이 VLA의 실시간 능력 피드백을 기반으로 구성 요소를 자율적으로 조직하도록 함으로써, PhysiAgent는 효과적인 자기 조절과 도구 협력을 실현했습니다. 실험 결과, 이 프레임워크는 복잡한 실제 로봇 작업에서 현저한 성능 향상을 보여주며 적응형 진화 능력을 입증했습니다.

## 핵심 내용
### 방법
PhysiAgent는 자율 스캐폴딩 프레임워크를 제안하며, 다음 메커니즘을 통해 VLM과 VLA의 효과적인 협력을 실현합니다:
- **모니터링 모듈**: VLA의 실행 상태와 능력 피드백을 실시간으로 추적합니다.
- **메모리 모듈**: 과거 작업 경험을 저장하여 장기 학습을 지원합니다.
- **자기 반성 메커니즘**: 피드백을 기반으로 VLM의 구성 요소 조직 전략을 동적으로 조정합니다.
- **경량 도구 키트**: 기성 도구를 통합하여 프레임워크의 유연성과 실용성을 강화합니다.

### 아키텍처
PhysiAgent는 비경직적 순차 구조를 채택하며, VLM은 더 이상 고수준 장면 이해와 작업 계획만 담당하지 않고 VLA의 실시간 능력 피드백에 따라 다양한 구성 요소를 자율적으로 호출합니다. 이 설계는 전통적인 방법에서 VLM과 VLA의 협력 효율성이 낮은 문제를 피하고 접지 능력을 향상시킵니다.

### 실험 설정
- **작업**: 복잡한 실제 세계 로봇 조작 작업.
- **평가 지표**: 작업 완료율, 협력 효율성 및 적응형 진화 능력.

### 주요 결과
- 복잡한 실제 로봇 작업에서 PhysiAgent는 작업 해결 성능을 현저히 향상시켰습니다.
- VLM의 효과적인 자기 조절 능력을 입증했으며, 도구 협력이 일관되고 프레임워크가 실행 과정에서 적응형으로 진화했습니다.

### 결론
PhysiAgent는 VLM과 VLA를 구현형 에이전트 프레임워크에 통합하는 실용적이고 선구적인 시도를 제공하며, 실제 세계 환경에서의 접지 응용을 효과적으로 실현했습니다.
