---
$id: ent_paper_xiao_ava_vla_improving_vision_langu_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention'
  zh: AVA-VLA
  ko: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention'
summary:
  en: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention (AVA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by LiAuto Inc., School of Information Science and Technology, Beijing University
    of Technology, School of Data Science, The Chinese University of Hong Kong, Shenzhen.'
  zh: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention (AVA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by LiAuto Inc., School of Information Science and Technology, Beijing University
    of Technology, School of Data Science, The Chinese University of Hong Kong, Shenzhen.'
  ko: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention (AVA-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by LiAuto Inc., School of Information Science and Technology, Beijing University
    of Technology, School of Data Science, The Chinese University of Hong Kong, Shenzhen.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ava_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.18960v4.
sources:
- id: src_001
  type: paper
  title: 'AVA-VLA: Improving Vision-Language-Action models with Active Visual Attention (arXiv)'
  url: https://arxiv.org/abs/2511.18960
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: AVA-VLA source
  url: https://doi.org/10.48550/arXiv.2511.18960
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have shown remarkable progress in embodied tasks recently, but most methods process visual observations independently at each timestep. This history-agnostic design treats robot manipulation as a Markov Decision Process, even though real-world robotic control is inherently partially observable and requires reasoning over past interactions. To address this mismatch, we reformulate VLA policy learning from a Partially Observable Markov Decision Process perspective and propose AVA-VLA, a framework that conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history. Built on this recurrent state, we introduce Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history. Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks. These results demonstrate the effectiveness of temporally grounded active visual processing for improving VLA performance in robotic sequential decision-making. The project page is available at https://liauto-dsr.github.io/AVA-VLA-Page.

## 核心内容
Vision-Language-Action (VLA) models have shown remarkable progress in embodied tasks recently, but most methods process visual observations independently at each timestep. This history-agnostic design treats robot manipulation as a Markov Decision Process, even though real-world robotic control is inherently partially observable and requires reasoning over past interactions. To address this mismatch, we reformulate VLA policy learning from a Partially Observable Markov Decision Process perspective and propose AVA-VLA, a framework that conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history. Built on this recurrent state, we introduce Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history. Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks. These results demonstrate the effectiveness of temporally grounded active visual processing for improving VLA performance in robotic sequential decision-making. The project page is available at https://liauto-dsr.github.io/AVA-VLA-Page.

## 参考
- http://arxiv.org/abs/2511.18960v4

## Overview
Vision-Language-Action (VLA) models have shown remarkable progress in embodied tasks recently, but most methods process visual observations independently at each timestep. This history-agnostic design treats robot manipulation as a Markov Decision Process, even though real-world robotic control is inherently partially observable and requires reasoning over past interactions. To address this mismatch, we reformulate VLA policy learning from a Partially Observable Markov Decision Process perspective and propose AVA-VLA, a framework that conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history. Built on this recurrent state, we introduce Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history. Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks. These results demonstrate the effectiveness of temporally grounded active visual processing for improving VLA performance in robotic sequential decision-making. The project page is available at https://liauto-dsr.github.io/AVA-VLA-Page.

## Content
Vision-Language-Action (VLA) models have shown remarkable progress in embodied tasks recently, but most methods process visual observations independently at each timestep. This history-agnostic design treats robot manipulation as a Markov Decision Process, even though real-world robotic control is inherently partially observable and requires reasoning over past interactions. To address this mismatch, we reformulate VLA policy learning from a Partially Observable Markov Decision Process perspective and propose AVA-VLA, a framework that conditions action generation on a recurrent state that serves as a neural approximation to the agent's belief over task history. Built on this recurrent state, we introduce Active Visual Attention (AVA), which dynamically reweights visual tokens in the current observation to focus on regions most relevant given both the instruction and execution history. Extensive experiments show that AVA-VLA achieves state-of-the-art performance on standard robotic benchmarks, including LIBERO and CALVIN, and transfers effectively to real-world dual-arm manipulation tasks. These results demonstrate the effectiveness of temporally grounded active visual processing for improving VLA performance in robotic sequential decision-making. The project page is available at https://liauto-dsr.github.io/AVA-VLA-Page.

## 개요
Vision-Language-Action (VLA) 모델은 최근 임베디드 태스크에서 놀라운 진전을 보여주었지만, 대부분의 방법은 각 시간 단계에서 시각적 관찰을 독립적으로 처리합니다. 이러한 이력 무관 설계는 로봇 조작을 마르코프 결정 과정으로 취급하지만, 실제 로봇 제어는 본질적으로 부분 관찰 가능하며 과거 상호작용에 대한 추론이 필요합니다. 이러한 불일치를 해결하기 위해, 우리는 부분 관찰 가능 마르코프 결정 과정 관점에서 VLA 정책 학습을 재구성하고, 작업 이력에 대한 에이전트의 신념을 신경망적으로 근사하는 순환 상태에 기반하여 행동 생성을 조건화하는 프레임워크인 AVA-VLA를 제안합니다. 이 순환 상태를 기반으로, 우리는 명령과 실행 이력을 모두 고려하여 현재 관찰에서 가장 관련성 높은 영역에 초점을 맞추도록 시각적 토큰을 동적으로 재가중하는 Active Visual Attention (AVA)을 도입합니다. 광범위한 실험을 통해 AVA-VLA는 LIBERO 및 CALVIN을 포함한 표준 로봇 벤치마크에서 최첨단 성능을 달성하고, 실제 이중 팔 조작 작업으로 효과적으로 전이됨을 보여줍니다. 이러한 결과는 로봇 순차적 의사 결정에서 VLA 성능을 향상시키기 위한 시간 기반 능동 시각 처리의 효과성을 입증합니다. 프로젝트 페이지는 https://liauto-dsr.github.io/AVA-VLA-Page에서 확인할 수 있습니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 최근 임베디드 태스크에서 놀라운 진전을 보여주었지만, 대부분의 방법은 각 시간 단계에서 시각적 관찰을 독립적으로 처리합니다. 이러한 이력 무관 설계는 로봇 조작을 마르코프 결정 과정으로 취급하지만, 실제 로봇 제어는 본질적으로 부분 관찰 가능하며 과거 상호작용에 대한 추론이 필요합니다. 이러한 불일치를 해결하기 위해, 우리는 부분 관찰 가능 마르코프 결정 과정 관점에서 VLA 정책 학습을 재구성하고, 작업 이력에 대한 에이전트의 신념을 신경망적으로 근사하는 순환 상태에 기반하여 행동 생성을 조건화하는 프레임워크인 AVA-VLA를 제안합니다. 이 순환 상태를 기반으로, 우리는 명령과 실행 이력을 모두 고려하여 현재 관찰에서 가장 관련성 높은 영역에 초점을 맞추도록 시각적 토큰을 동적으로 재가중하는 Active Visual Attention (AVA)을 도입합니다. 광범위한 실험을 통해 AVA-VLA는 LIBERO 및 CALVIN을 포함한 표준 로봇 벤치마크에서 최첨단 성능을 달성하고, 실제 이중 팔 조작 작업으로 효과적으로 전이됨을 보여줍니다. 이러한 결과는 로봇 순차적 의사 결정에서 VLA 성능을 향상시키기 위한 시간 기반 능동 시각 처리의 효과성을 입증합니다. 프로젝트 페이지는 https://liauto-dsr.github.io/AVA-VLA-Page에서 확인할 수 있습니다.
