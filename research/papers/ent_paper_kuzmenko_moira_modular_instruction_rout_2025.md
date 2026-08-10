---
$id: ent_paper_kuzmenko_moira_modular_instruction_rout_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics'
  zh: MoIRA
  ko: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics'
summary:
  en: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics (MoIRA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Department of Multimedia Systems, National University of Kyiv-Mohyla Academy,
    Department of Mathematics, National University of Kyiv-Mohyla Academy.'
  zh: MoIRA 是 2025 年由基辅莫希拉大学团队提出的模块化指令路由架构，用于多任务机器人操控。其核心贡献在于设计了一种与架构无关的 MoE 框架，通过外部文本路由器实现零样本专家选择，无需额外训练即可协调现有视觉-语言-动作模型。在
    GR1 Humanoid 和 LIBERO 基准上，MoIRA 持续优于通用模型，并与其他 MoE 管线性能相当。
  ko: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics (MoIRA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Department of Multimedia Systems, National University of Kyiv-Mohyla Academy,
    Department of Mathematics, National University of Kyiv-Mohyla Academy.'
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
- moira
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.01843v2. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (906 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics (arXiv)'
  url: https://arxiv.org/abs/2507.01843
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MoIRA source
  url: https://doi.org/10.48550/arXiv.2507.01843
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
MoIRA 针对现有混合专家（MoE）系统在机器人应用中路由机制僵化、无法灵活定制底层专家的问题，提出了一种架构无关的模块化框架。该框架通过外部文本路由器实现零样本路由，支持两种路由选项：基于嵌入的相似度匹配和基于提示的语言模型推理。实验选用 gr00t-N1 和 π₀ 作为底层专家，并训练低秩适配器以降低推理开销。在 GR1 Humanoid 任务和 LIBERO Spatial/Goal 基准上，MoIRA 不仅超越通用模型，还与其他 MoE 管线竞争，同时展现出对指令变化的鲁棒性。

## 核心内容
### 方法
- **架构无关的模块化 MoE 框架**：MoIRA 不依赖特定模型架构，通过外部文本路由器协调现有专家模型。
- **零样本路由机制**：
  - **嵌入相似度路由**：将任务指令与专家描述文本的嵌入向量进行相似度匹配。
  - **提示驱动路由**：利用语言模型根据任务提示直接推断最合适的专家。
- **低开销推理**：为底层专家（gr00t-N1 和 π₀）训练低秩适配器（LoRA），避免全模型微调。

### 实验设置
- **专家模型**：选用大型视觉-语言-动作模型 gr00t-N1 和 π₀ 作为底层专家。
- **基准测试**：
  - GR1 Humanoid 任务：评估人形机器人操控能力。
  - LIBERO Spatial 和 Goal 基准：测试空间推理与目标导向任务。
- **对比基线**：通用模型（如单专家模型）和其他 MoE 管线。

### 关键结果
- **性能优势**：MoIRA 在所有任务上持续优于通用模型，并与现有 MoE 管线性能持平或更优。
- **鲁棒性分析**：仅依赖任务和专家的文本描述，MoIRA 对指令变化（如措辞差异）表现出良好鲁棒性。
- **可扩展性**：框架为未来多专家机器人系统提供了可扩展的基础，无需重新训练即可集成新专家。

### 结论
MoIRA 通过外部文本路由实现了精确、低成本的模块化部署，验证了零样本路由在多任务机器人操控中的实际可行性，为构建可扩展的多专家系统提供了新范式。

## Overview
Mixture-of-Experts (MoE) approaches have recently gained traction in robotics applications due to their ability to dynamically allocate computational resources and specialize sub-networks for distinct tasks or environmental contexts, enabling more efficient decision-making. Such systems often comprise sparsely activated experts combined under a single monolithic architecture and require a well-configured internal routing mechanism, which does not allow for selective low-level expert and router customization and requires additional training. We propose MoIRA, an architecture-agnostic modular MoE framework designed to coordinate existing experts with an external text-based router. MoIRA incorporates two zero-shot routing options: embedding-based similarity and prompt-driven language model inference. In our experiments, we choose large Vision-Language-Action models, gr00t-N1 and $π_0$, as the underlying experts, and train low-rank adapters for low-overhead inference. We evaluate MoIRA on various GR1 Humanoid tasks and LIBERO Spatial and Goal benchmarks, where it consistently outperforms generalist models and competes with other MoE pipelines. Additionally, we analyse the robustness of the proposed approach to the variations of the instructions. While relying solely on textual descriptions of tasks and experts, MoIRA demonstrates the practical viability of modular deployment with precise, low-effort routing and provides an alternative, scalable foundation for future multi-expert robotic systems.

## 参考
- http://arxiv.org/abs/2507.01843v2

## 개요
MoIRA는 기존 혼합 전문가(MoE) 시스템이 로봇 애플리케이션에서 라우팅 메커니즘이 경직되고 하위 전문가를 유연하게 맞춤 설정할 수 없는 문제를 해결하기 위해, 아키텍처에 구애받지 않는 모듈식 프레임워크를 제안한다. 이 프레임워크는 외부 텍스트 라우터를 통해 제로샷 라우팅을 구현하며, 임베딩 기반 유사도 매칭과 프롬프트 기반 언어 모델 추론의 두 가지 라우팅 옵션을 지원한다. 실험에서는 gr00t-N1과 π₀를 하위 전문가로 선택하고, 추론 오버헤드를 줄이기 위해 저순위 어댑터를 훈련했다. GR1 Humanoid 작업과 LIBERO Spatial/Goal 벤치마크에서 MoIRA는 일반 모델을 능가할 뿐만 아니라 다른 MoE 파이프라인과도 경쟁하며, 명령 변화에 대한 견고성을 보여준다.

## 핵심 내용
### 방법
- **아키텍처에 구애받지 않는 모듈식 MoE 프레임워크**: MoIRA는 특정 모델 아키텍처에 의존하지 않으며, 외부 텍스트 라우터를 통해 기존 전문가 모델을 조정한다.
- **제로샷 라우팅 메커니즘**:
  - **임베딩 유사도 라우팅**: 작업 명령과 전문가 설명 텍스트의 임베딩 벡터 간 유사도를 매칭한다.
  - **프롬프트 기반 라우팅**: 언어 모델을 활용하여 작업 프롬프트에 따라 가장 적합한 전문가를 직접 추론한다.
- **저비용 추론**: 하위 전문가(gr00t-N1 및 π₀)를 위해 저순위 어댑터(LoRA)를 훈련하여 전체 모델 미세 조정을 피한다.

### 실험 설정
- **전문가 모델**: 대규모 비전-언어-행동 모델인 gr00t-N1과 π₀를 하위 전문가로 선택한다.
- **벤치마크 테스트**:
  - GR1 Humanoid 작업: 휴머노이드 로봇 조작 능력 평가.
  - LIBERO Spatial 및 Goal 벤치마크: 공간 추론 및 목표 지향 작업 테스트.
- **비교 기준선**: 일반 모델(예: 단일 전문가 모델) 및 다른 MoE 파이프라인.

### 주요 결과
- **성능 우위**: MoIRA는 모든 작업에서 일반 모델을 지속적으로 능가하며, 기존 MoE 파이프라인과 동등하거나 더 나은 성능을 보인다.
- **견고성 분석**: 작업 및 전문가의 텍스트 설명에만 의존하는 MoIRA는 명령 변화(예: 표현 차이)에 대해 우수한 견고성을 나타낸다.
- **확장성**: 이 프레임워크는 재훈련 없이 새 전문가를 통합할 수 있는 미래의 다중 전문가 로봇 시스템을 위한 확장 가능한 기반을 제공한다.

### 결론
MoIRA는 외부 텍스트 라우팅을 통해 정밀하고 저비용의 모듈식 배포를 구현하며, 다중 작업 로봇 조작에서 제로샷 라우팅의 실질적 실행 가능성을 검증하여 확장 가능한 다중 전문가 시스템 구축을 위한 새로운 패러다임을 제시한다.
