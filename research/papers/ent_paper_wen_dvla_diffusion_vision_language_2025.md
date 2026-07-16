---
$id: ent_paper_wen_dvla_diffusion_vision_language_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought'
  zh: dVLA
  ko: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought'
summary:
  en: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (dVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Shanghai Jiaotong University.'
  zh: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (dVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Shanghai Jiaotong University.'
  ko: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (dVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Peking University, Shanghai Jiaotong University.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- dvla
- large_vla_model
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.25681v1.
sources:
- id: src_001
  type: paper
  title: 'dVLA: Diffusion Vision-Language-Action Model with Multimodal Chain-of-Thought (arXiv)'
  url: https://arxiv.org/abs/2509.25681
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: dVLA source
  url: https://doi.org/10.48550/arXiv.2509.25681
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models are emerging as a next-generation paradigm for robotics. We introduce dVLA, a diffusion-based VLA that leverages a multimodal chain-of-thought to unify visual perception, language reasoning, and robotic control in a single system. dVLA jointly optimizes perception, language understanding, and action under a single diffusion objective, enabling stronger cross-modal reasoning and better generalization to novel instructions and objects. For practical deployment, we mitigate inference latency by incorporating two acceleration strategies, a prefix attention mask and KV caching, yielding up to around times speedup at test-time inference. We evaluate dVLA in both simulation and the real world: on the LIBERO benchmark, it achieves state-of-the-art performance with a 96.4% average success rate, consistently surpassing both discrete and continuous action policies; on a real Franka robot, it succeeds across a diverse task suite, including a challenging bin-picking task that requires multi-step planning, demonstrating robust real-world performance. Together, these results underscore the promise of unified diffusion frameworks for practical, high-performance VLA robotics.

## 核心内容
Vision-Language-Action (VLA) models are emerging as a next-generation paradigm for robotics. We introduce dVLA, a diffusion-based VLA that leverages a multimodal chain-of-thought to unify visual perception, language reasoning, and robotic control in a single system. dVLA jointly optimizes perception, language understanding, and action under a single diffusion objective, enabling stronger cross-modal reasoning and better generalization to novel instructions and objects. For practical deployment, we mitigate inference latency by incorporating two acceleration strategies, a prefix attention mask and KV caching, yielding up to around times speedup at test-time inference. We evaluate dVLA in both simulation and the real world: on the LIBERO benchmark, it achieves state-of-the-art performance with a 96.4% average success rate, consistently surpassing both discrete and continuous action policies; on a real Franka robot, it succeeds across a diverse task suite, including a challenging bin-picking task that requires multi-step planning, demonstrating robust real-world performance. Together, these results underscore the promise of unified diffusion frameworks for practical, high-performance VLA robotics.

## 参考
- http://arxiv.org/abs/2509.25681v1

## Overview
Vision-Language-Action (VLA) models are emerging as a next-generation paradigm for robotics. We introduce dVLA, a diffusion-based VLA that leverages a multimodal chain-of-thought to unify visual perception, language reasoning, and robotic control in a single system. dVLA jointly optimizes perception, language understanding, and action under a single diffusion objective, enabling stronger cross-modal reasoning and better generalization to novel instructions and objects. For practical deployment, we mitigate inference latency by incorporating two acceleration strategies, a prefix attention mask and KV caching, yielding up to around times speedup at test-time inference. We evaluate dVLA in both simulation and the real world: on the LIBERO benchmark, it achieves state-of-the-art performance with a 96.4% average success rate, consistently surpassing both discrete and continuous action policies; on a real Franka robot, it succeeds across a diverse task suite, including a challenging bin-picking task that requires multi-step planning, demonstrating robust real-world performance. Together, these results underscore the promise of unified diffusion frameworks for practical, high-performance VLA robotics.

## Content
Vision-Language-Action (VLA) models are emerging as a next-generation paradigm for robotics. We introduce dVLA, a diffusion-based VLA that leverages a multimodal chain-of-thought to unify visual perception, language reasoning, and robotic control in a single system. dVLA jointly optimizes perception, language understanding, and action under a single diffusion objective, enabling stronger cross-modal reasoning and better generalization to novel instructions and objects. For practical deployment, we mitigate inference latency by incorporating two acceleration strategies, a prefix attention mask and KV caching, yielding up to around times speedup at test-time inference. We evaluate dVLA in both simulation and the real world: on the LIBERO benchmark, it achieves state-of-the-art performance with a 96.4% average success rate, consistently surpassing both discrete and continuous action policies; on a real Franka robot, it succeeds across a diverse task suite, including a challenging bin-picking task that requires multi-step planning, demonstrating robust real-world performance. Together, these results underscore the promise of unified diffusion frameworks for practical, high-performance VLA robotics.

## 개요
Vision-Language-Action (VLA) 모델은 로봇 공학의 차세대 패러다임으로 부상하고 있습니다. 우리는 멀티모달 체인 오브 소트(multimodal chain-of-thought)를 활용하여 시각적 인식, 언어 추론 및 로봇 제어를 단일 시스템으로 통합하는 확산 기반 VLA인 dVLA를 소개합니다. dVLA는 단일 확산 목표 하에 인식, 언어 이해 및 행동을 공동으로 최적화하여 더 강력한 교차 모달 추론과 새로운 명령 및 객체에 대한 더 나은 일반화를 가능하게 합니다. 실제 배포를 위해 접두사 주의 마스크(prefix attention mask)와 KV 캐싱(KV caching)이라는 두 가지 가속 전략을 통합하여 추론 지연 시간을 완화하며, 테스트 시 추론에서 최대 약 몇 배의 속도 향상을 제공합니다. 우리는 dVLA를 시뮬레이션과 실제 환경 모두에서 평가했습니다: LIBERO 벤치마크에서 96.4%의 평균 성공률로 최첨단 성능을 달성하여 이산 및 연속 행동 정책을 모두 일관되게 능가했습니다; 실제 Franka 로봇에서는 다단계 계획이 필요한 까다로운 빈 피킹(bin-picking) 작업을 포함한 다양한 작업 세트에서 성공하여 강력한 실제 성능을 입증했습니다. 이러한 결과는 실용적이고 고성능의 VLA 로봇 공학을 위한 통합 확산 프레임워크의 가능성을 강조합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 로봇 공학의 차세대 패러다임으로 부상하고 있습니다. 우리는 멀티모달 체인 오브 소트(multimodal chain-of-thought)를 활용하여 시각적 인식, 언어 추론 및 로봇 제어를 단일 시스템으로 통합하는 확산 기반 VLA인 dVLA를 소개합니다. dVLA는 단일 확산 목표 하에 인식, 언어 이해 및 행동을 공동으로 최적화하여 더 강력한 교차 모달 추론과 새로운 명령 및 객체에 대한 더 나은 일반화를 가능하게 합니다. 실제 배포를 위해 접두사 주의 마스크(prefix attention mask)와 KV 캐싱(KV caching)이라는 두 가지 가속 전략을 통합하여 추론 지연 시간을 완화하며, 테스트 시 추론에서 최대 약 몇 배의 속도 향상을 제공합니다. 우리는 dVLA를 시뮬레이션과 실제 환경 모두에서 평가했습니다: LIBERO 벤치마크에서 96.4%의 평균 성공률로 최첨단 성능을 달성하여 이산 및 연속 행동 정책을 모두 일관되게 능가했습니다; 실제 Franka 로봇에서는 다단계 계획이 필요한 까다로운 빈 피킹(bin-picking) 작업을 포함한 다양한 작업 세트에서 성공하여 강력한 실제 성능을 입증했습니다. 이러한 결과는 실용적이고 고성능의 VLA 로봇 공학을 위한 통합 확산 프레임워크의 가능성을 강조합니다.
