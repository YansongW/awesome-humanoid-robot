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
  zh: 'arXiv:2509.15061v3 Announce Type: replace Abstract: Embodied agents are intelligent systems designed to perceive, reason,
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.15061v3.
sources:
- id: src_001
  type: paper
  title: 'Ask-to-Clarify: Resolving Instruction Ambiguity through Multi-turn Dialogue (arXiv)'
  url: https://arxiv.org/abs/2509.15061
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Embodied agents are intelligent systems designed to perceive, reason, and act within the physical world. While the robotics community has long strived to build such versatile agents, a fundamental limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act'' paradigm. These systems assume instructions are unambiguous and execute them in a passive fashion, preventing them from resolving uncertainty through dialogue. To address this, we propose Ask-to-Clarify, a unified end-to-end framework that seamlessly integrates multi-turn disambiguation dialogue with low-level visuomotor control, eliminating the reliance on high-level action primitives or external planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner with a Diffusion-based Motor Executor. To bridge the disparity between high-level disambiguation and low-level execution, we introduce a Semantic-Visual Alignment Adapter, which functions as a cross-modal interface to synthesize semantic intent with visual perceptual streams. Furthermore, we observe severe catastrophic forgetting: visuomotor fine-tuning completely erases dialogue capabilities. To overcome this, we propose a two-stage knowledge-insulation training strategy, effectively decoupling dialogue logic from physical manipulation. Extensive evaluations across 11 real-world tasks demonstrate that \framework{} significantly outperforms existing methods, offering a promising path toward building truly collaborative embodied agents.

## 核心内容
Embodied agents are intelligent systems designed to perceive, reason, and act within the physical world. While the robotics community has long strived to build such versatile agents, a fundamental limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act'' paradigm. These systems assume instructions are unambiguous and execute them in a passive fashion, preventing them from resolving uncertainty through dialogue. To address this, we propose Ask-to-Clarify, a unified end-to-end framework that seamlessly integrates multi-turn disambiguation dialogue with low-level visuomotor control, eliminating the reliance on high-level action primitives or external planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner with a Diffusion-based Motor Executor. To bridge the disparity between high-level disambiguation and low-level execution, we introduce a Semantic-Visual Alignment Adapter, which functions as a cross-modal interface to synthesize semantic intent with visual perceptual streams. Furthermore, we observe severe catastrophic forgetting: visuomotor fine-tuning completely erases dialogue capabilities. To overcome this, we propose a two-stage knowledge-insulation training strategy, effectively decoupling dialogue logic from physical manipulation. Extensive evaluations across 11 real-world tasks demonstrate that \framework{} significantly outperforms existing methods, offering a promising path toward building truly collaborative embodied agents.

## 参考
- http://arxiv.org/abs/2509.15061v3

## Overview
Embodied agents are intelligent systems designed to perceive, reason, and act within the physical world. While the robotics community has long strived to build such versatile agents, a fundamental limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act'' paradigm. These systems assume instructions are unambiguous and execute them in a passive fashion, preventing them from resolving uncertainty through dialogue. To address this, we propose Ask-to-Clarify, a unified end-to-end framework that seamlessly integrates multi-turn disambiguation dialogue with low-level visuomotor control, eliminating the reliance on high-level action primitives or external planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner with a Diffusion-based Motor Executor. To bridge the disparity between high-level disambiguation and low-level execution, we introduce a Semantic-Visual Alignment Adapter, which functions as a cross-modal interface to synthesize semantic intent with visual perceptual streams. Furthermore, we observe severe catastrophic forgetting: visuomotor fine-tuning completely erases dialogue capabilities. To overcome this, we propose a two-stage knowledge-insulation training strategy, effectively decoupling dialogue logic from physical manipulation. Extensive evaluations across 11 real-world tasks demonstrate that \framework{} significantly outperforms existing methods, offering a promising path toward building truly collaborative embodied agents.

## Content
Embodied agents are intelligent systems designed to perceive, reason, and act within the physical world. While the robotics community has long strived to build such versatile agents, a fundamental limitation persists: most current VLA-based models operate under a rigid ``Listen-and-Act'' paradigm. These systems assume instructions are unambiguous and execute them in a passive fashion, preventing them from resolving uncertainty through dialogue. To address this, we propose Ask-to-Clarify, a unified end-to-end framework that seamlessly integrates multi-turn disambiguation dialogue with low-level visuomotor control, eliminating the reliance on high-level action primitives or external planners. Specifically, Ask-to-Clarify synergizes a VLM-based Cognitive Planner with a Diffusion-based Motor Executor. To bridge the disparity between high-level disambiguation and low-level execution, we introduce a Semantic-Visual Alignment Adapter, which functions as a cross-modal interface to synthesize semantic intent with visual perceptual streams. Furthermore, we observe severe catastrophic forgetting: visuomotor fine-tuning completely erases dialogue capabilities. To overcome this, we propose a two-stage knowledge-insulation training strategy, effectively decoupling dialogue logic from physical manipulation. Extensive evaluations across 11 real-world tasks demonstrate that \framework{} significantly outperforms existing methods, offering a promising path toward building truly collaborative embodied agents.

## 개요
Embodied agents는 물리적 세계에서 인지, 추론 및 행동을 수행하도록 설계된 지능형 시스템입니다. 로봇 공학 커뮤니티는 오랫동안 이러한 다재다능한 에이전트를 구축하기 위해 노력해 왔지만, 근본적인 한계가 지속되고 있습니다. 대부분의 현재 VLA 기반 모델은 엄격한 "듣고-행동하기(Listen-and-Act)" 패러다임 하에서 작동합니다. 이러한 시스템은 명령이 명확하다고 가정하고 수동적으로 실행하여 대화를 통해 불확실성을 해결하지 못합니다. 이를 해결하기 위해, 우리는 다중 턴 명확화 대화를 저수준 시각-운동 제어와 원활하게 통합하고, 고수준 행동 프리미티브나 외부 플래너에 대한 의존성을 제거하는 통합 종단 간 프레임워크인 Ask-to-Clarify를 제안합니다. 구체적으로, Ask-to-Clarify는 VLM 기반 인지 플래너(Cognitive Planner)와 확산 기반 운동 실행기(Diffusion-based Motor Executor)를 시너지 효과를 내도록 결합합니다. 고수준 명확화와 저수준 실행 간의 차이를 연결하기 위해, 우리는 의미적 의도와 시각적 지각 스트림을 합성하는 교차 모달 인터페이스 역할을 하는 의미-시각 정렬 어댑터(Semantic-Visual Alignment Adapter)를 도입합니다. 또한, 심각한 파괴적 망각(catastrophic forgetting) 현상을 관찰했습니다. 시각-운동 미세 조정이 대화 능력을 완전히 지워버리는 것입니다. 이를 극복하기 위해, 우리는 2단계 지식 절연 훈련 전략(two-stage knowledge-insulation training strategy)을 제안하여 대화 논리와 물리적 조작을 효과적으로 분리합니다. 11가지 실제 작업에 대한 광범위한 평가는 \framework{}가 기존 방법보다 현저히 뛰어난 성능을 보여주며, 진정한 협력적 임베디드 에이전트를 구축하기 위한 유망한 경로를 제시합니다.

## 핵심 내용
Embodied agents는 물리적 세계에서 인지, 추론 및 행동을 수행하도록 설계된 지능형 시스템입니다. 로봇 공학 커뮤니티는 오랫동안 이러한 다재다능한 에이전트를 구축하기 위해 노력해 왔지만, 근본적인 한계가 지속되고 있습니다. 대부분의 현재 VLA 기반 모델은 엄격한 "듣고-행동하기(Listen-and-Act)" 패러다임 하에서 작동합니다. 이러한 시스템은 명령이 명확하다고 가정하고 수동적으로 실행하여 대화를 통해 불확실성을 해결하지 못합니다. 이를 해결하기 위해, 우리는 다중 턴 명확화 대화를 저수준 시각-운동 제어와 원활하게 통합하고, 고수준 행동 프리미티브나 외부 플래너에 대한 의존성을 제거하는 통합 종단 간 프레임워크인 Ask-to-Clarify를 제안합니다. 구체적으로, Ask-to-Clarify는 VLM 기반 인지 플래너(Cognitive Planner)와 확산 기반 운동 실행기(Diffusion-based Motor Executor)를 시너지 효과를 내도록 결합합니다. 고수준 명확화와 저수준 실행 간의 차이를 연결하기 위해, 우리는 의미적 의도와 시각적 지각 스트림을 합성하는 교차 모달 인터페이스 역할을 하는 의미-시각 정렬 어댑터(Semantic-Visual Alignment Adapter)를 도입합니다. 또한, 심각한 파괴적 망각(catastrophic forgetting) 현상을 관찰했습니다. 시각-운동 미세 조정이 대화 능력을 완전히 지워버리는 것입니다. 이를 극복하기 위해, 우리는 2단계 지식 절연 훈련 전략(two-stage knowledge-insulation training strategy)을 제안하여 대화 논리와 물리적 조작을 효과적으로 분리합니다. 11가지 실제 작업에 대한 광범위한 평가는 \framework{}가 기존 방법보다 현저히 뛰어난 성능을 보여주며, 진정한 협력적 임베디드 에이전트를 구축하기 위한 유망한 경로를 제시합니다.
