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
  zh: 'MoIRA: Modular Instruction Routing Architecture for Multi-Task Robotics (MoIRA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Department of Multimedia Systems, National University of Kyiv-Mohyla Academy,
    Department of Mathematics, National University of Kyiv-Mohyla Academy.'
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2507.01843v2.
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
Mixture-of-Experts (MoE) approaches have recently gained traction in robotics applications due to their ability to dynamically allocate computational resources and specialize sub-networks for distinct tasks or environmental contexts, enabling more efficient decision-making. Such systems often comprise sparsely activated experts combined under a single monolithic architecture and require a well-configured internal routing mechanism, which does not allow for selective low-level expert and router customization and requires additional training. We propose MoIRA, an architecture-agnostic modular MoE framework designed to coordinate existing experts with an external text-based router. MoIRA incorporates two zero-shot routing options: embedding-based similarity and prompt-driven language model inference. In our experiments, we choose large Vision-Language-Action models, gr00t-N1 and $π_0$, as the underlying experts, and train low-rank adapters for low-overhead inference. We evaluate MoIRA on various GR1 Humanoid tasks and LIBERO Spatial and Goal benchmarks, where it consistently outperforms generalist models and competes with other MoE pipelines. Additionally, we analyse the robustness of the proposed approach to the variations of the instructions. While relying solely on textual descriptions of tasks and experts, MoIRA demonstrates the practical viability of modular deployment with precise, low-effort routing and provides an alternative, scalable foundation for future multi-expert robotic systems.

## 核心内容
Mixture-of-Experts (MoE) approaches have recently gained traction in robotics applications due to their ability to dynamically allocate computational resources and specialize sub-networks for distinct tasks or environmental contexts, enabling more efficient decision-making. Such systems often comprise sparsely activated experts combined under a single monolithic architecture and require a well-configured internal routing mechanism, which does not allow for selective low-level expert and router customization and requires additional training. We propose MoIRA, an architecture-agnostic modular MoE framework designed to coordinate existing experts with an external text-based router. MoIRA incorporates two zero-shot routing options: embedding-based similarity and prompt-driven language model inference. In our experiments, we choose large Vision-Language-Action models, gr00t-N1 and $π_0$, as the underlying experts, and train low-rank adapters for low-overhead inference. We evaluate MoIRA on various GR1 Humanoid tasks and LIBERO Spatial and Goal benchmarks, where it consistently outperforms generalist models and competes with other MoE pipelines. Additionally, we analyse the robustness of the proposed approach to the variations of the instructions. While relying solely on textual descriptions of tasks and experts, MoIRA demonstrates the practical viability of modular deployment with precise, low-effort routing and provides an alternative, scalable foundation for future multi-expert robotic systems.

## 参考
- http://arxiv.org/abs/2507.01843v2

## Overview
Mixture-of-Experts (MoE) approaches have recently gained traction in robotics applications due to their ability to dynamically allocate computational resources and specialize sub-networks for distinct tasks or environmental contexts, enabling more efficient decision-making. Such systems often comprise sparsely activated experts combined under a single monolithic architecture and require a well-configured internal routing mechanism, which does not allow for selective low-level expert and router customization and requires additional training. We propose MoIRA, an architecture-agnostic modular MoE framework designed to coordinate existing experts with an external text-based router. MoIRA incorporates two zero-shot routing options: embedding-based similarity and prompt-driven language model inference. In our experiments, we choose large Vision-Language-Action models, gr00t-N1 and $π_0$, as the underlying experts, and train low-rank adapters for low-overhead inference. We evaluate MoIRA on various GR1 Humanoid tasks and LIBERO Spatial and Goal benchmarks, where it consistently outperforms generalist models and competes with other MoE pipelines. Additionally, we analyse the robustness of the proposed approach to the variations of the instructions. While relying solely on textual descriptions of tasks and experts, MoIRA demonstrates the practical viability of modular deployment with precise, low-effort routing and provides an alternative, scalable foundation for future multi-expert robotic systems.

## Content
Mixture-of-Experts (MoE) approaches have recently gained traction in robotics applications due to their ability to dynamically allocate computational resources and specialize sub-networks for distinct tasks or environmental contexts, enabling more efficient decision-making. Such systems often comprise sparsely activated experts combined under a single monolithic architecture and require a well-configured internal routing mechanism, which does not allow for selective low-level expert and router customization and requires additional training. We propose MoIRA, an architecture-agnostic modular MoE framework designed to coordinate existing experts with an external text-based router. MoIRA incorporates two zero-shot routing options: embedding-based similarity and prompt-driven language model inference. In our experiments, we choose large Vision-Language-Action models, gr00t-N1 and $π_0$, as the underlying experts, and train low-rank adapters for low-overhead inference. We evaluate MoIRA on various GR1 Humanoid tasks and LIBERO Spatial and Goal benchmarks, where it consistently outperforms generalist models and competes with other MoE pipelines. Additionally, we analyse the robustness of the proposed approach to the variations of the instructions. While relying solely on textual descriptions of tasks and experts, MoIRA demonstrates the practical viability of modular deployment with precise, low-effort routing and provides an alternative, scalable foundation for future multi-expert robotic systems.

## 개요
Mixture-of-Experts (MoE) 접근 방식은 최근 로봇공학 응용 분야에서 주목받고 있습니다. 이는 동적으로 컴퓨팅 자원을 할당하고, 서로 다른 작업이나 환경적 맥락에 맞춰 하위 네트워크를 특화시켜 더 효율적인 의사 결정을 가능하게 하기 때문입니다. 이러한 시스템은 종종 단일 모놀리식 아키텍처 아래 결합된 희소 활성화 전문가들로 구성되며, 잘 구성된 내부 라우팅 메커니즘이 필요합니다. 이는 선택적인 저수준 전문가 및 라우터 맞춤 설정을 허용하지 않으며 추가 학습을 요구합니다. 우리는 MoIRA를 제안합니다. 이는 아키텍처에 구애받지 않는 모듈형 MoE 프레임워크로, 기존 전문가들을 외부 텍스트 기반 라우터와 조정하도록 설계되었습니다. MoIRA는 두 가지 제로샷 라우팅 옵션을 통합합니다: 임베딩 기반 유사도와 프롬프트 기반 언어 모델 추론입니다. 실험에서 우리는 대규모 Vision-Language-Action 모델인 gr00t-N1과 $π_0$를 기본 전문가로 선택하고, 저오버헤드 추론을 위해 저순위 어댑터를 학습시킵니다. MoIRA를 다양한 GR1 휴머노이드 작업과 LIBERO 공간 및 목표 벤치마크에서 평가했으며, 이는 일반주의 모델을 일관되게 능가하고 다른 MoE 파이프라인과 경쟁합니다. 또한, 제안된 접근 방식의 지시 변동에 대한 강건성을 분석합니다. 작업과 전문가에 대한 텍스트 설명에만 의존하면서도 MoIRA는 정밀하고 노력이 적은 라우팅을 통한 모듈형 배포의 실질적 실행 가능성을 입증하며, 미래의 다중 전문가 로봇 시스템을 위한 대안적이고 확장 가능한 기반을 제공합니다.

## 핵심 내용
Mixture-of-Experts (MoE) 접근 방식은 최근 로봇공학 응용 분야에서 주목받고 있습니다. 이는 동적으로 컴퓨팅 자원을 할당하고, 서로 다른 작업이나 환경적 맥락에 맞춰 하위 네트워크를 특화시켜 더 효율적인 의사 결정을 가능하게 하기 때문입니다. 이러한 시스템은 종종 단일 모놀리식 아키텍처 아래 결합된 희소 활성화 전문가들로 구성되며, 잘 구성된 내부 라우팅 메커니즘이 필요합니다. 이는 선택적인 저수준 전문가 및 라우터 맞춤 설정을 허용하지 않으며 추가 학습을 요구합니다. 우리는 MoIRA를 제안합니다. 이는 아키텍처에 구애받지 않는 모듈형 MoE 프레임워크로, 기존 전문가들을 외부 텍스트 기반 라우터와 조정하도록 설계되었습니다. MoIRA는 두 가지 제로샷 라우팅 옵션을 통합합니다: 임베딩 기반 유사도와 프롬프트 기반 언어 모델 추론입니다. 실험에서 우리는 대규모 Vision-Language-Action 모델인 gr00t-N1과 $π_0$를 기본 전문가로 선택하고, 저오버헤드 추론을 위해 저순위 어댑터를 학습시킵니다. MoIRA를 다양한 GR1 휴머노이드 작업과 LIBERO 공간 및 목표 벤치마크에서 평가했으며, 이는 일반주의 모델을 일관되게 능가하고 다른 MoE 파이프라인과 경쟁합니다. 또한, 제안된 접근 방식의 지시 변동에 대한 강건성을 분석합니다. 작업과 전문가에 대한 텍스트 설명에만 의존하면서도 MoIRA는 정밀하고 노력이 적은 라우팅을 통한 모듈형 배포의 실질적 실행 가능성을 입증하며, 미래의 다중 전문가 로봇 시스템을 위한 대안적이고 확장 가능한 기반을 제공합니다.
