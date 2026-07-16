---
$id: ent_paper_fan_long_vla_unleashing_long_horiz_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation'
  zh: Long-VLA
  ko: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation'
summary:
  en: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (Long-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at
    CoRL25.'
  zh: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (Long-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at
    CoRL25.'
  ko: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (Long-VLA), is
    a 2025 large vision-language-action model for robotic manipulation, introduced by Zhejiang University, and published at
    CoRL25.'
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
- long_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19958v2.
sources:
- id: src_001
  type: paper
  title: 'Long-VLA: Unleashing Long-Horizon Capability of Vision Language Action Model for Robot Manipulation (arXiv)'
  url: https://arxiv.org/abs/2508.19958
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Long-VLA source
  url: https://doi.org/10.48550/arXiv.2508.19958
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control. However, existing VLA frameworks primarily address short-horizon tasks, and their effectiveness on long-horizon, multi-step robotic manipulation remains limited due to challenges in skill chaining and subtask dependencies. In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks. Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on phase-relevant sensory cues and enhancing subtask compatibility. This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models. We further propose the L-CALVIN benchmark to systematically evaluate long-horizon manipulation. Extensive experiments on both simulated and real-world tasks demonstrate that Long-VLA significantly outperforms prior state-of-the-art methods, establishing a new baseline for long-horizon robotic control.

## 核心内容
Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control. However, existing VLA frameworks primarily address short-horizon tasks, and their effectiveness on long-horizon, multi-step robotic manipulation remains limited due to challenges in skill chaining and subtask dependencies. In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks. Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on phase-relevant sensory cues and enhancing subtask compatibility. This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models. We further propose the L-CALVIN benchmark to systematically evaluate long-horizon manipulation. Extensive experiments on both simulated and real-world tasks demonstrate that Long-VLA significantly outperforms prior state-of-the-art methods, establishing a new baseline for long-horizon robotic control.

## 参考
- http://arxiv.org/abs/2508.19958v2

## Overview
Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control. However, existing VLA frameworks primarily address short-horizon tasks, and their effectiveness on long-horizon, multi-step robotic manipulation remains limited due to challenges in skill chaining and subtask dependencies. In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks. Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on phase-relevant sensory cues and enhancing subtask compatibility. This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models. We further propose the L-CALVIN benchmark to systematically evaluate long-horizon manipulation. Extensive experiments on both simulated and real-world tasks demonstrate that Long-VLA significantly outperforms prior state-of-the-art methods, establishing a new baseline for long-horizon robotic control.

## Content
Vision-Language-Action (VLA) models have become a cornerstone in robotic policy learning, leveraging large-scale multimodal data for robust and scalable control. However, existing VLA frameworks primarily address short-horizon tasks, and their effectiveness on long-horizon, multi-step robotic manipulation remains limited due to challenges in skill chaining and subtask dependencies. In this work, we introduce Long-VLA, the first end-to-end VLA model specifically designed for long-horizon robotic tasks. Our approach features a novel phase-aware input masking strategy that adaptively segments each subtask into moving and interaction phases, enabling the model to focus on phase-relevant sensory cues and enhancing subtask compatibility. This unified strategy preserves the scalability and data efficiency of VLA training, and our architecture-agnostic module can be seamlessly integrated into existing VLA models. We further propose the L-CALVIN benchmark to systematically evaluate long-horizon manipulation. Extensive experiments on both simulated and real-world tasks demonstrate that Long-VLA significantly outperforms prior state-of-the-art methods, establishing a new baseline for long-horizon robotic control.

## 개요
Vision-Language-Action (VLA) 모델은 대규모 멀티모달 데이터를 활용하여 강력하고 확장 가능한 제어를 가능하게 하는 로봇 정책 학습의 초석이 되었습니다. 그러나 기존 VLA 프레임워크는 주로 단기 작업을 다루며, 장기적이고 다단계 로봇 조작에서의 효과성은 기술 체이닝 및 하위 작업 의존성 문제로 인해 제한적입니다. 본 연구에서는 장기 로봇 작업을 위해 특별히 설계된 최초의 엔드투엔드 VLA 모델인 Long-VLA를 소개합니다. 우리의 접근 방식은 각 하위 작업을 이동 및 상호작용 단계로 적응적으로 분할하는 새로운 위상 인식 입력 마스킹 전략을 특징으로 하며, 모델이 위상 관련 감각 신호에 집중하고 하위 작업 호환성을 향상시킬 수 있도록 합니다. 이 통합 전략은 VLA 훈련의 확장성과 데이터 효율성을 유지하며, 아키텍처에 구애받지 않는 모듈은 기존 VLA 모델에 원활하게 통합될 수 있습니다. 또한 장기 조작을 체계적으로 평가하기 위해 L-CALVIN 벤치마크를 제안합니다. 시뮬레이션 및 실제 작업에 대한 광범위한 실험을 통해 Long-VLA가 이전 최첨단 방법을 크게 능가하며 장기 로봇 제어의 새로운 기준을 수립함을 입증합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 대규모 멀티모달 데이터를 활용하여 강력하고 확장 가능한 제어를 가능하게 하는 로봇 정책 학습의 초석이 되었습니다. 그러나 기존 VLA 프레임워크는 주로 단기 작업을 다루며, 장기적이고 다단계 로봇 조작에서의 효과성은 기술 체이닝 및 하위 작업 의존성 문제로 인해 제한적입니다. 본 연구에서는 장기 로봇 작업을 위해 특별히 설계된 최초의 엔드투엔드 VLA 모델인 Long-VLA를 소개합니다. 우리의 접근 방식은 각 하위 작업을 이동 및 상호작용 단계로 적응적으로 분할하는 새로운 위상 인식 입력 마스킹 전략을 특징으로 하며, 모델이 위상 관련 감각 신호에 집중하고 하위 작업 호환성을 향상시킬 수 있도록 합니다. 이 통합 전략은 VLA 훈련의 확장성과 데이터 효율성을 유지하며, 아키텍처에 구애받지 않는 모듈은 기존 VLA 모델에 원활하게 통합될 수 있습니다. 또한 장기 조작을 체계적으로 평가하기 위해 L-CALVIN 벤치마크를 제안합니다. 시뮬레이션 및 실제 작업에 대한 광범위한 실험을 통해 Long-VLA가 이전 최첨단 방법을 크게 능가하며 장기 로봇 제어의 새로운 기준을 수립함을 입증합니다.
