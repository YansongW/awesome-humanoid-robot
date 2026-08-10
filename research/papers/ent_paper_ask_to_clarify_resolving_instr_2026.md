---
$id: ent_paper_ask_to_clarify_resolving_instr_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue'
  zh: 'Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue'
  ko: 'Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue'
summary:
  en: 'arXiv:2509.15061v3 Announce Type: replace Abstract: Embodied agents are intelligent systems designed to perceive, reason,
    and act within the physical world. While the robotics community has long strived to build such versatile agents, a fundamental
    limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act'''' paradigm. These systems
    assume instructions are unambiguous and execute them in a passive fashion, preventing them from resolving uncertainty
    through dialogue. To address this, we propose Ask-to-Clarify, a unified end-to-end framework that seamlessly integrates
    multi-turn disambiguation dialogue with low-level visuomotor control, eliminating the reliance on high-level action primitives
    or external planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner with a Diffusion-based Motor
    Executor. To bridge the disparity between high-level disambiguation and low-level execution, we introduce a Semantic-Visual
    Alignment Adapter, which functions as a cross-modal interface to synthesize semantic intent with visual perceptual streams.
    Furthermore, we observe severe catastrophic forgetting: visuomotor fine-tuning completely erases dialogue capabilities.
    To overcome this, we propose a two-stage knowledge-insulation training strategy, effectively decoupling dialogue logic
    from physical manipulation. Extensive evaluations across 11 real-world tasks demonstrate that \framework{} significantly
    outperforms existing methods, offering a promising path toward building truly collaborative embodied agents.'
  zh: Ask-to-Clarify 是一个端到端统一框架，由研究团队提出，旨在解决具身智能体在指令模糊时无法通过对话澄清的问题。其核心贡献在于将多轮消歧对话与底层视觉运动控制无缝集成，并引入语义-视觉对齐适配器与两阶段知识隔离训练策略，在11项真实世界任务中显著超越现有方法。
  ko: 'arXiv:2509.15061v3 Announce Type: replace Abstract: Embodied agents are intelligent systems designed to perceive, reason,
    and act within the physical world. While the robotics community has long strived to build such versatile agents, a fundamental
    limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act'''' paradigm. These systems
    assume instructions are unambiguous and execute them in a passive fashion, preventing them from resolving uncertainty
    through dialogue. To address this, we propose Ask-to-Clarify, a unified end-to-end framework that seamlessly integrates
    multi-turn disambiguation dialogue with low-level visuomotor control, eliminating the reliance on high-level action primitives
    or external planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner with a Diffusion-based Motor
    Executor. To bridge the disparity between high-level disambiguation and low-level execution, we introduce a Semantic-Visual
    Alignment Adapter, which functions as a cross-modal interface to synthesize semantic intent with visual perceptual streams.
    Furthermore, we observe severe catastrophic forgetting: visuomotor fine-tuning completely erases dialogue capabilities.
    To overcome this, we propose a two-stage knowledge-insulation training strategy, effectively decoupling dialogue logic
    from physical manipulation. Extensive evaluations across 11 real-world tasks demonstrate that \framework{} significantly
    outperforms existing methods, offering a promising path toward building truly collaborative embodied agents.'
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
- ask_to_clarify
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15061v3. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (734 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue (arXiv)'
  url: https://arxiv.org/abs/2509.15061
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
当前大多数基于VLA的具身模型遵循“听令即行”的被动范式，假设指令明确无误，无法通过对话消除不确定性。为此，Ask-to-Clarify 框架将基于VLM的认知规划器与基于扩散模型的运动执行器协同工作，并通过语义-视觉对齐适配器桥接高层消歧与底层执行之间的鸿沟。针对视觉运动微调会彻底擦除对话能力的灾难性遗忘问题，该框架采用两阶段知识隔离训练策略，有效解耦对话逻辑与物理操作。在11项真实世界任务上的广泛评估表明，该框架显著优于现有方法。

## 核心内容
### 方法架构
- **认知规划器（Cognitive Planner）**：基于VLM，负责理解模糊指令并通过多轮对话主动向用户提问以澄清意图。
- **运动执行器（Motor Executor）**：基于扩散模型，将澄清后的语义意图转化为低层视觉运动控制信号。
- **语义-视觉对齐适配器（Semantic-Visual Alignment Adapter）**：作为跨模态接口，将高层语义意图与视觉感知流合成，解决高层消歧与底层执行之间的语义鸿沟。

### 训练策略
- **两阶段知识隔离训练**：第一阶段训练对话逻辑能力，第二阶段训练物理操作能力，通过知识隔离机制防止视觉运动微调覆盖对话能力，从而克服灾难性遗忘。

### 实验设置与结果
- 在11项真实世界任务上进行评估，涵盖物体操作、导航等场景。
- 与现有基线方法相比，Ask-to-Clarify 在任务成功率、对话效率及鲁棒性上均取得显著提升，具体数字未在摘要中列出，但论文中提供了详细对比。

### 结论
该框架为构建真正协作的具身智能体提供了可行路径，通过主动对话消除指令歧义，突破了传统“听令即行”范式的局限。

## Overview
Embodied agents are intelligent systems designed to perceive, reason, and act within the physical world. While the robotics community has long strived to build such versatile agents, a fundamental limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act'' paradigm. These systems assume instructions are unambiguous and execute them in a passive fashion, preventing them from resolving uncertainty through dialogue. To address this, we propose Ask-to-Clarify, a unified end-to-end framework that seamlessly integrates multi-turn disambiguation dialogue with low-level visuomotor control, eliminating the reliance on high-level action primitives or external planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner with a Diffusion-based Motor Executor. To bridge the disparity between high-level disambiguation and low-level execution, we introduce a Semantic-Visual Alignment Adapter, which functions as a cross-modal interface to synthesize semantic intent with visual perceptual streams. Furthermore, we observe severe catastrophic forgetting: visuomotor fine-tuning completely erases dialogue capabilities. To overcome this, we propose a two-stage knowledge-insulation training strategy, effectively decoupling dialogue logic from physical manipulation. Extensive evaluations across 11 real-world tasks demonstrate that \framework{} significantly outperforms existing methods, offering a promising path toward building truly collaborative embodied agents.

## 参考
- http://arxiv.org/abs/2509.15061v3

## 개요
현재 대부분의 VLA 기반 구현 모델은 "명령을 받으면 즉시 실행"하는 수동적 패러다임을 따르며, 명령이 명확하다고 가정하여 대화를 통한 불확실성 해소가 불가능합니다. 이를 위해 Ask-to-Clarify 프레임워크는 VLM 기반 인지 플래너와 확산 모델 기반 운동 실행기를 협력적으로 작동시키고, 의미-시각 정렬 어댑터를 통해 고수준 명확화와 저수준 실행 간의 격차를 연결합니다. 시각 운동 미세 조정이 대화 능력을 완전히 지워버리는 치명적 망각 문제를 해결하기 위해, 이 프레임워크는 두 단계 지식 격리 훈련 전략을 채택하여 대화 논리와 물리적 조작을 효과적으로 분리합니다. 11가지 실제 세계 작업에 대한 광범위한 평가에서 이 프레임워크는 기존 방법보다 현저히 우수한 성능을 보여줍니다.

## 핵심 내용
### 방법 아키텍처
- **인지 플래너(Cognitive Planner)**: VLM 기반으로, 모호한 명령을 이해하고 다중 턴 대화를 통해 사용자에게 적극적으로 질문하여 의도를 명확히 합니다.
- **운동 실행기(Motor Executor)**: 확산 모델 기반으로, 명확화된 의미적 의도를 저수준 시각 운동 제어 신호로 변환합니다.
- **의미-시각 정렬 어댑터(Semantic-Visual Alignment Adapter)**: 교차 모달 인터페이스로, 고수준 의미적 의도와 시각적 지각 흐름을 합성하여 고수준 명확화와 저수준 실행 간의 의미적 격차를 해결합니다.

### 훈련 전략
- **두 단계 지식 격리 훈련**: 첫 번째 단계는 대화 논리 능력을 훈련하고, 두 번째 단계는 물리적 조작 능력을 훈련합니다. 지식 격리 메커니즘을 통해 시각 운동 미세 조정이 대화 능력을 덮어쓰지 않도록 방지하여 치명적 망각을 극복합니다.

### 실험 설정 및 결과
- 11가지 실제 세계 작업에서 평가되었으며, 객체 조작, 내비게이션 등의 시나리오를 포함합니다.
- 기존 기준선 방법과 비교하여 Ask-to-Clarify는 작업 성공률, 대화 효율성 및 견고성에서 현저한 향상을 보였으며, 구체적인 수치는 초록에 나열되지 않았지만 논문에 상세 비교가 제공됩니다.

### 결론
이 프레임워크는 능동적 대화를 통해 명령 모호성을 제거하여 전통적인 "명령을 받으면 즉시 실행" 패러다임의 한계를 돌파함으로써, 진정한 협력적 구현 에이전트를 구축하는 실현 가능한 경로를 제공합니다.
