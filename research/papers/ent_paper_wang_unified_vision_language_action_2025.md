---
$id: ent_paper_wang_unified_vision_language_action_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Unified Vision-Language-Action Model
  zh: UniVLA
  ko: Unified Vision-Language-Action Model
summary:
  en: Unified Vision-Language-Action Model (UniVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by CASIA, BAAI, THU, HKISI.
  zh: Unified Vision-Language-Action Model (UniVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by CASIA, BAAI, THU, HKISI.
  ko: Unified Vision-Language-Action Model (UniVLA), is a 2025 large vision-language-action model for robotic manipulation,
    introduced by CASIA, BAAI, THU, HKISI.
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
- univla
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.19850v1.
sources:
- id: src_001
  type: paper
  title: Unified Vision-Language-Action Model (arXiv)
  url: https://arxiv.org/abs/2506.19850
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UniVLA source
  url: https://dblp.org/rec/journals/corr/abs-2506-19850
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action models (VLAs) have garnered significant attention for their potential in advancing robotic manipulation. However, previous approaches predominantly rely on the general comprehension capabilities of vision-language models (VLMs) to generate action signals, often overlooking the rich temporal and causal structure embedded in visual observations. In this paper, we present UniVLA, a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences. This formulation enables flexible multimodal tasks learning, particularly from large-scale video data. By incorporating world modeling during post-training, UniVLA captures causal dynamics from videos, facilitating effective transfer to downstream policy learning--especially for long-horizon tasks. Our approach sets new state-of-the-art results across several widely used simulation benchmarks, including CALVIN, LIBERO, and Simplenv-Bridge, significantly surpassing previous methods. For example, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. We further demonstrate its broad applicability on real-world ALOHA manipulation and autonomous driving.

## 核心内容
Vision-language-action models (VLAs) have garnered significant attention for their potential in advancing robotic manipulation. However, previous approaches predominantly rely on the general comprehension capabilities of vision-language models (VLMs) to generate action signals, often overlooking the rich temporal and causal structure embedded in visual observations. In this paper, we present UniVLA, a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences. This formulation enables flexible multimodal tasks learning, particularly from large-scale video data. By incorporating world modeling during post-training, UniVLA captures causal dynamics from videos, facilitating effective transfer to downstream policy learning--especially for long-horizon tasks. Our approach sets new state-of-the-art results across several widely used simulation benchmarks, including CALVIN, LIBERO, and Simplenv-Bridge, significantly surpassing previous methods. For example, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. We further demonstrate its broad applicability on real-world ALOHA manipulation and autonomous driving.

## 参考
- http://arxiv.org/abs/2506.19850v1

## Overview
Vision-language-action models (VLAs) have garnered significant attention for their potential in advancing robotic manipulation. However, previous approaches predominantly rely on the general comprehension capabilities of vision-language models (VLMs) to generate action signals, often overlooking the rich temporal and causal structure embedded in visual observations. In this paper, we present UniVLA, a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences. This formulation enables flexible multimodal tasks learning, particularly from large-scale video data. By incorporating world modeling during post-training, UniVLA captures causal dynamics from videos, facilitating effective transfer to downstream policy learning--especially for long-horizon tasks. Our approach sets new state-of-the-art results across several widely used simulation benchmarks, including CALVIN, LIBERO, and Simplenv-Bridge, significantly surpassing previous methods. For example, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. We further demonstrate its broad applicability on real-world ALOHA manipulation and autonomous driving.

## Content
Vision-language-action models (VLAs) have garnered significant attention for their potential in advancing robotic manipulation. However, previous approaches predominantly rely on the general comprehension capabilities of vision-language models (VLMs) to generate action signals, often overlooking the rich temporal and causal structure embedded in visual observations. In this paper, we present UniVLA, a unified and native multimodal VLA model that autoregressively models vision, language, and action signals as discrete token sequences. This formulation enables flexible multimodal tasks learning, particularly from large-scale video data. By incorporating world modeling during post-training, UniVLA captures causal dynamics from videos, facilitating effective transfer to downstream policy learning--especially for long-horizon tasks. Our approach sets new state-of-the-art results across several widely used simulation benchmarks, including CALVIN, LIBERO, and Simplenv-Bridge, significantly surpassing previous methods. For example, UniVLA achieves 95.5% average success rate on LIBERO benchmark, surpassing pi0-FAST's 85.5%. We further demonstrate its broad applicability on real-world ALOHA manipulation and autonomous driving.

## 개요
Vision-language-action models (VLAs)는 로봇 조작 분야의 발전 가능성으로 인해 큰 주목을 받아왔습니다. 그러나 기존 접근법들은 주로 vision-language models (VLMs)의 일반적인 이해 능력에 의존하여 행동 신호를 생성하며, 시각적 관찰에 내재된 풍부한 시간적 및 인과적 구조를 간과하는 경우가 많았습니다. 본 논문에서는 UniVLA를 제안합니다. 이는 시각, 언어, 행동 신호를 이산 토큰 시퀀스로 자기회귀적으로 모델링하는 통합적이고 본질적인 멀티모달 VLA 모델입니다. 이러한 구성은 특히 대규모 비디오 데이터를 활용한 유연한 멀티모달 작업 학습을 가능하게 합니다. 사후 훈련 과정에서 세계 모델링을 통합함으로써, UniVLA는 비디오로부터 인과적 역학을 포착하여 다운스트림 정책 학습, 특히 장기적 작업에 효과적으로 전이할 수 있도록 합니다. 우리의 접근법은 CALVIN, LIBERO, Simplenv-Bridge를 포함한 여러 널리 사용되는 시뮬레이션 벤치마크에서 새로운 최첨단 결과를 달성하며, 이전 방법들을 크게 능가합니다. 예를 들어, UniVLA는 LIBERO 벤치마크에서 평균 95.5%의 성공률을 기록하여 pi0-FAST의 85.5%를 넘어섰습니다. 또한 실제 세계의 ALOHA 조작 및 자율 주행에서의 광범위한 적용 가능성을 입증합니다.

## 핵심 내용
Vision-language-action models (VLAs)는 로봇 조작 분야의 발전 가능성으로 인해 큰 주목을 받아왔습니다. 그러나 기존 접근법들은 주로 vision-language models (VLMs)의 일반적인 이해 능력에 의존하여 행동 신호를 생성하며, 시각적 관찰에 내재된 풍부한 시간적 및 인과적 구조를 간과하는 경우가 많았습니다. 본 논문에서는 UniVLA를 제안합니다. 이는 시각, 언어, 행동 신호를 이산 토큰 시퀀스로 자기회귀적으로 모델링하는 통합적이고 본질적인 멀티모달 VLA 모델입니다. 이러한 구성은 특히 대규모 비디오 데이터를 활용한 유연한 멀티모달 작업 학습을 가능하게 합니다. 사후 훈련 과정에서 세계 모델링을 통합함으로써, UniVLA는 비디오로부터 인과적 역학을 포착하여 다운스트림 정책 학습, 특히 장기적 작업에 효과적으로 전이할 수 있도록 합니다. 우리의 접근법은 CALVIN, LIBERO, Simplenv-Bridge를 포함한 여러 널리 사용되는 시뮬레이션 벤치마크에서 새로운 최첨단 결과를 달성하며, 이전 방법들을 크게 능가합니다. 예를 들어, UniVLA는 LIBERO 벤치마크에서 평균 95.5%의 성공률을 기록하여 pi0-FAST의 85.5%를 넘어섰습니다. 또한 실제 세계의 ALOHA 조작 및 자율 주행에서의 광범위한 적용 가능성을 입증합니다.
