---
$id: ent_paper_li_metavla_unified_meta_co_traini_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption'
  zh: MetaVLA
  ko: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption'
summary:
  en: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (MetaVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, Meta Reality Labs, USA.'
  zh: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (MetaVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, Meta Reality Labs, USA.'
  ko: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (MetaVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Carnegie Mellon University, Meta Reality Labs, USA.'
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
- metavla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.05580v3.
sources:
- id: src_001
  type: paper
  title: 'MetaVLA: Unified Meta Co-training For Efficient Embodied Adaption (arXiv)'
  url: https://arxiv.org/abs/2510.05580
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MetaVLA source
  url: https://doi.org/10.48550/arXiv.2510.05580
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists-they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism-derived from Attentive Neural Processes-to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by ~76%. These results show that scalable, low-resource post-training is achievable-paving the way toward general-purpose embodied agents. Code will be available.

## 核心内容
Vision-Language-Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists-they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism-derived from Attentive Neural Processes-to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by ~76%. These results show that scalable, low-resource post-training is achievable-paving the way toward general-purpose embodied agents. Code will be available.

## 参考
- http://arxiv.org/abs/2510.05580v3

## Overview
Vision-Language-Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists—they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism—derived from Attentive Neural Processes—to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by ~76%. These results show that scalable, low-resource post-training is achievable—paving the way toward general-purpose embodied agents. Code will be available.

## Content
Vision-Language-Action (VLA) models show promise in embodied reasoning, yet remain far from true generalists—they often require task-specific fine-tuning, incur high compute costs, and generalize poorly to unseen tasks. We propose MetaVLA, a unified, backbone-agnostic post-training framework for efficient and scalable alignment. MetaVLA introduces Context-Aware Meta Co-Training, which consolidates diverse target tasks into a single fine-tuning stage while leveraging structurally diverse auxiliary tasks to improve in-domain generalization. Unlike naive multi-task SFT, MetaVLA integrates a lightweight meta-learning mechanism—derived from Attentive Neural Processes—to enable rapid adaptation from diverse contexts with minimal architectural change or inference overhead. On the LIBERO benchmark, MetaVLA with six auxiliary tasks outperforms OpenVLA by up to 8.0% on long-horizon tasks, reduces training steps from 240K to 75K, and cuts GPU time by ~76%. These results show that scalable, low-resource post-training is achievable—paving the way toward general-purpose embodied agents. Code will be available.

## 개요
Vision-Language-Action (VLA) 모델은 구현된 추론에서 가능성을 보여주지만, 진정한 범용 모델과는 거리가 멀습니다. 종종 작업별 미세 조정이 필요하고, 높은 계산 비용이 발생하며, 보지 못한 작업에 대한 일반화 성능이 낮습니다. 본 논문에서는 효율적이고 확장 가능한 정렬을 위한 통합적이고 백본에 구애받지 않는 사후 훈련 프레임워크인 MetaVLA를 제안합니다. MetaVLA는 다양한 대상 작업을 단일 미세 조정 단계로 통합하면서 구조적으로 다양한 보조 작업을 활용하여 도메인 내 일반화를 개선하는 Context-Aware Meta Co-Training을 도입합니다. 단순한 멀티태스크 SFT와 달리, MetaVLA는 Attentive Neural Processes에서 파생된 경량 메타 학습 메커니즘을 통합하여 최소한의 아키텍처 변경이나 추론 오버헤드로 다양한 컨텍스트에서 빠른 적응을 가능하게 합니다. LIBERO 벤치마크에서 6개의 보조 작업을 사용한 MetaVLA는 장기 작업에서 OpenVLA보다 최대 8.0% 더 나은 성능을 보였으며, 훈련 단계를 240K에서 75K로 줄이고 GPU 시간을 약 76% 절감했습니다. 이러한 결과는 확장 가능하고 저자원 사후 훈련이 가능함을 보여주며, 범용 구현 에이전트를 향한 길을 열어줍니다. 코드는 공개될 예정입니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 구현된 추론에서 가능성을 보여주지만, 진정한 범용 모델과는 거리가 멉니다. 종종 작업별 미세 조정이 필요하고, 높은 계산 비용이 발생하며, 보지 못한 작업에 대한 일반화 성능이 낮습니다. 본 논문에서는 효율적이고 확장 가능한 정렬을 위한 통합적이고 백본에 구애받지 않는 사후 훈련 프레임워크인 MetaVLA를 제안합니다. MetaVLA는 다양한 대상 작업을 단일 미세 조정 단계로 통합하면서 구조적으로 다양한 보조 작업을 활용하여 도메인 내 일반화를 개선하는 Context-Aware Meta Co-Training을 도입합니다. 단순한 멀티태스크 SFT와 달리, MetaVLA는 Attentive Neural Processes에서 파생된 경량 메타 학습 메커니즘을 통합하여 최소한의 아키텍처 변경이나 추론 오버헤드로 다양한 컨텍스트에서 빠른 적응을 가능하게 합니다. LIBERO 벤치마크에서 6개의 보조 작업을 사용한 MetaVLA는 장기 작업에서 OpenVLA보다 최대 8.0% 더 나은 성능을 보였으며, 훈련 단계를 240K에서 75K로 줄이고 GPU 시간을 약 76% 절감했습니다. 이러한 결과는 확장 가능하고 저자원 사후 훈련이 가능함을 보여주며, 범용 구현 에이전트를 향한 길을 열어줍니다. 코드는 공개될 예정입니다.
