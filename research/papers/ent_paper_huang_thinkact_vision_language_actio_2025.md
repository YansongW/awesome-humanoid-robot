---
$id: ent_paper_huang_thinkact_vision_language_actio_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning'
  zh: ThinkAct
  ko: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning'
summary:
  en: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (ThinkAct), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, National Taiwan University.'
  zh: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (ThinkAct), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, National Taiwan University.'
  ko: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (ThinkAct), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by NVIDIA, National Taiwan University.'
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
- thinkact
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.16815v2.
sources:
- id: src_001
  type: paper
  title: 'ThinkAct: Vision-Language-Action Reasoning via Reinforced Visual Latent Planning (arXiv)'
  url: https://arxiv.org/abs/2507.16815
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: ThinkAct source
  url: https://doi.org/10.48550/arXiv.2507.16815
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## 核心内容
Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## 参考
- http://arxiv.org/abs/2507.16815v2

## Overview
Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## Content
Vision-language-action (VLA) reasoning tasks require agents to interpret multimodal instructions, perform long-horizon planning, and act adaptively in dynamic environments. Existing approaches typically train VLA models in an end-to-end fashion, directly mapping inputs to actions without explicit reasoning, which hinders their ability to plan over multiple steps or adapt to complex task variations. In this paper, we propose ThinkAct, a dual-system framework that bridges high-level reasoning with low-level action execution via reinforced visual latent planning. ThinkAct trains a multimodal LLM to generate embodied reasoning plans guided by reinforcing action-aligned visual rewards based on goal completion and trajectory consistency. These reasoning plans are compressed into a visual plan latent that conditions a downstream action model for robust action execution on target environments. Extensive experiments on embodied reasoning and robot manipulation benchmarks demonstrate that ThinkAct enables few-shot adaptation, long-horizon planning, and self-correction behaviors in complex embodied AI tasks.

## 개요
Vision-language-action (VLA) 추론 작업은 에이전트가 멀티모달 명령을 해석하고, 장기 계획을 수행하며, 동적 환경에서 적응적으로 행동할 것을 요구합니다. 기존 접근 방식은 일반적으로 VLA 모델을 종단간 방식으로 훈련하여 명시적 추론 없이 입력을 행동에 직접 매핑하므로, 여러 단계에 걸친 계획이나 복잡한 작업 변형에 적응하는 능력이 저해됩니다. 본 논문에서는 강화된 시각적 잠재 계획을 통해 고수준 추론과 저수준 행동 실행을 연결하는 이중 시스템 프레임워크인 ThinkAct를 제안합니다. ThinkAct는 목표 완료 및 궤적 일관성에 기반한 행동 정렬 시각적 보상을 강화하여 안내되는 체화된 추론 계획을 생성하도록 멀티모달 LLM을 훈련합니다. 이러한 추론 계획은 시각적 계획 잠재 변수로 압축되어 하류 행동 모델이 대상 환경에서 강건한 행동 실행을 수행하도록 조건화합니다. 체화된 추론 및 로봇 조작 벤치마크에 대한 광범위한 실험을 통해 ThinkAct가 복잡한 체화된 AI 작업에서 소수 샷 적응, 장기 계획 및 자기 수정 행동을 가능하게 함을 입증합니다.

## 핵심 내용
Vision-language-action (VLA) 추론 작업은 에이전트가 멀티모달 명령을 해석하고, 장기 계획을 수행하며, 동적 환경에서 적응적으로 행동할 것을 요구합니다. 기존 접근 방식은 일반적으로 VLA 모델을 종단간 방식으로 훈련하여 명시적 추론 없이 입력을 행동에 직접 매핑하므로, 여러 단계에 걸친 계획이나 복잡한 작업 변형에 적응하는 능력이 저해됩니다. 본 논문에서는 강화된 시각적 잠재 계획을 통해 고수준 추론과 저수준 행동 실행을 연결하는 이중 시스템 프레임워크인 ThinkAct를 제안합니다. ThinkAct는 목표 완료 및 궤적 일관성에 기반한 행동 정렬 시각적 보상을 강화하여 안내되는 체화된 추론 계획을 생성하도록 멀티모달 LLM을 훈련합니다. 이러한 추론 계획은 시각적 계획 잠재 변수로 압축되어 하류 행동 모델이 대상 환경에서 강건한 행동 실행을 수행하도록 조건화합니다. 체화된 추론 및 로봇 조작 벤치마크에 대한 광범위한 실험을 통해 ThinkAct가 복잡한 체화된 AI 작업에서 소수 샷 적응, 장기 계획 및 자기 수정 행동을 가능하게 함을 입증합니다.
