---
$id: ent_paper_liu_hybridvla_collaborative_diffus_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model'
  zh: HybridVLA
  ko: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model'
summary:
  en: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (HybridVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Peking University, Beijing Academy of Artificial
    Intelligence (BAAI), CUHK.'
  zh: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (HybridVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Peking University, Beijing Academy of Artificial
    Intelligence (BAAI), CUHK.'
  ko: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (HybridVLA), is a 2025
    large vision-language-action model for robotic manipulation, introduced by Peking University, Beijing Academy of Artificial
    Intelligence (BAAI), CUHK.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- hybridvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2503.10631v3.
sources:
- id: src_001
  type: paper
  title: 'HybridVLA: Collaborative Diffusion and Autoregression in a Unified Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2503.10631
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: HybridVLA source
  url: https://doi.org/10.48550/arXiv.2503.10631
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
A fundamental objective of manipulation policy design is to endow robots to comprehend human instructions, reason about scene cues, and execute generalized actions in dynamic environments. Recent autoregressive vision-language-action (VLA) methods inherit common-sense reasoning capabilities from vision-language models (VLMs) for next action-token prediction. However, these methods quantize actions into discrete bins, which disrupts the continuity required for precise control. In contrast, existing diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions solely conditioned on feature representations extracted by the VLM, without fully leveraging the VLM's pretrained reasoning capabilities through token-level generation. To address these limitations, we introduce HybridVLA, a unified framework that absorbs the continuous nature of diffusion-based actions and the contextual reasoning of autoregression within a single large language model. To mitigate interference between the two generation paradigms, we propose a collaborative training recipe that seamlessly incorporates diffusion denoising into the next-token prediction process. With this recipe, we find these two action prediction methods not only reinforce each other but also exhibit varying strength across different tasks. Therefore, we design a collaborative action ensemble mechanism that adaptively fuses both predictions, leading to more robust control. HybridVLA outperforms previous state-of-the-art VLA methods by 14\% and 19\% in mean success rate on simulation and real-world tasks, respectively, while demonstrating stable manipulation in unseen configurations.

## 核心内容
A fundamental objective of manipulation policy design is to endow robots to comprehend human instructions, reason about scene cues, and execute generalized actions in dynamic environments. Recent autoregressive vision-language-action (VLA) methods inherit common-sense reasoning capabilities from vision-language models (VLMs) for next action-token prediction. However, these methods quantize actions into discrete bins, which disrupts the continuity required for precise control. In contrast, existing diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions solely conditioned on feature representations extracted by the VLM, without fully leveraging the VLM's pretrained reasoning capabilities through token-level generation. To address these limitations, we introduce HybridVLA, a unified framework that absorbs the continuous nature of diffusion-based actions and the contextual reasoning of autoregression within a single large language model. To mitigate interference between the two generation paradigms, we propose a collaborative training recipe that seamlessly incorporates diffusion denoising into the next-token prediction process. With this recipe, we find these two action prediction methods not only reinforce each other but also exhibit varying strength across different tasks. Therefore, we design a collaborative action ensemble mechanism that adaptively fuses both predictions, leading to more robust control. HybridVLA outperforms previous state-of-the-art VLA methods by 14\% and 19\% in mean success rate on simulation and real-world tasks, respectively, while demonstrating stable manipulation in unseen configurations.

## 参考
- http://arxiv.org/abs/2503.10631v3

## Overview
A fundamental objective of manipulation policy design is to endow robots to comprehend human instructions, reason about scene cues, and execute generalized actions in dynamic environments. Recent autoregressive vision-language-action (VLA) methods inherit common-sense reasoning capabilities from vision-language models (VLMs) for next action-token prediction. However, these methods quantize actions into discrete bins, which disrupts the continuity required for precise control. In contrast, existing diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions solely conditioned on feature representations extracted by the VLM, without fully leveraging the VLM's pretrained reasoning capabilities through token-level generation. To address these limitations, we introduce HybridVLA, a unified framework that absorbs the continuous nature of diffusion-based actions and the contextual reasoning of autoregression within a single large language model. To mitigate interference between the two generation paradigms, we propose a collaborative training recipe that seamlessly incorporates diffusion denoising into the next-token prediction process. With this recipe, we find these two action prediction methods not only reinforce each other but also exhibit varying strength across different tasks. Therefore, we design a collaborative action ensemble mechanism that adaptively fuses both predictions, leading to more robust control. HybridVLA outperforms previous state-of-the-art VLA methods by 14\% and 19\% in mean success rate on simulation and real-world tasks, respectively, while demonstrating stable manipulation in unseen configurations.

## Content
A fundamental objective of manipulation policy design is to endow robots to comprehend human instructions, reason about scene cues, and execute generalized actions in dynamic environments. Recent autoregressive vision-language-action (VLA) methods inherit common-sense reasoning capabilities from vision-language models (VLMs) for next action-token prediction. However, these methods quantize actions into discrete bins, which disrupts the continuity required for precise control. In contrast, existing diffusion-based VLA methods incorporate an additional diffusion head to predict continuous actions solely conditioned on feature representations extracted by the VLM, without fully leveraging the VLM's pretrained reasoning capabilities through token-level generation. To address these limitations, we introduce HybridVLA, a unified framework that absorbs the continuous nature of diffusion-based actions and the contextual reasoning of autoregression within a single large language model. To mitigate interference between the two generation paradigms, we propose a collaborative training recipe that seamlessly incorporates diffusion denoising into the next-token prediction process. With this recipe, we find these two action prediction methods not only reinforce each other but also exhibit varying strength across different tasks. Therefore, we design a collaborative action ensemble mechanism that adaptively fuses both predictions, leading to more robust control. HybridVLA outperforms previous state-of-the-art VLA methods by 14\% and 19\% in mean success rate on simulation and real-world tasks, respectively, while demonstrating stable manipulation in unseen configurations.

## 개요
조작 정책 설계의 근본적인 목표는 로봇이 인간의 명령을 이해하고, 장면 단서를 추론하며, 동적 환경에서 일반화된 동작을 실행할 수 있도록 하는 것입니다. 최근의 자기회귀형 시각-언어-행동(VLA) 방법은 시각-언어 모델(VLM)로부터 상식 추론 능력을 계승하여 다음 행동 토큰을 예측합니다. 그러나 이러한 방법은 행동을 이산적인 구간으로 양자화하여 정밀한 제어에 필요한 연속성을 방해합니다. 반면, 기존의 확산 기반 VLA 방법은 VLM이 추출한 특징 표현에만 조건화된 연속적인 행동을 예측하기 위해 추가적인 확산 헤드를 통합하며, 토큰 수준 생성을 통해 VLM의 사전 학습된 추론 능력을 완전히 활용하지 못합니다. 이러한 한계를 해결하기 위해, 우리는 단일 대규모 언어 모델 내에서 확산 기반 행동의 연속성과 자기회귀의 맥락적 추론을 통합하는 통합 프레임워크인 HybridVLA를 소개합니다. 두 생성 패러다임 간의 간섭을 완화하기 위해, 우리는 다음 토큰 예측 과정에 확산 잡음 제거를 원활하게 통합하는 협력적 훈련 방식을 제안합니다. 이 방식을 통해, 우리는 이 두 행동 예측 방법이 서로를 강화할 뿐만 아니라 다양한 작업에 따라 서로 다른 강점을 보인다는 것을 발견했습니다. 따라서, 우리는 두 예측을 적응적으로 융합하여 더 강력한 제어를 이끌어내는 협력적 행동 앙상블 메커니즘을 설계합니다. HybridVLA는 시뮬레이션 및 실제 세계 작업에서 평균 성공률이 각각 14%와 19% 향상되어 이전 최첨단 VLA 방법을 능가하며, 보이지 않는 구성에서도 안정적인 조작을 보여줍니다.

## 핵심 내용
조작 정책 설계의 근본적인 목표는 로봇이 인간의 명령을 이해하고, 장면 단서를 추론하며, 동적 환경에서 일반화된 동작을 실행할 수 있도록 하는 것입니다. 최근의 자기회귀형 시각-언어-행동(VLA) 방법은 시각-언어 모델(VLM)로부터 상식 추론 능력을 계승하여 다음 행동 토큰을 예측합니다. 그러나 이러한 방법은 행동을 이산적인 구간으로 양자화하여 정밀한 제어에 필요한 연속성을 방해합니다. 반면, 기존의 확산 기반 VLA 방법은 VLM이 추출한 특징 표현에만 조건화된 연속적인 행동을 예측하기 위해 추가적인 확산 헤드를 통합하며, 토큰 수준 생성을 통해 VLM의 사전 학습된 추론 능력을 완전히 활용하지 못합니다. 이러한 한계를 해결하기 위해, 우리는 단일 대규모 언어 모델 내에서 확산 기반 행동의 연속성과 자기회귀의 맥락적 추론을 통합하는 통합 프레임워크인 HybridVLA를 소개합니다. 두 생성 패러다임 간의 간섭을 완화하기 위해, 우리는 다음 토큰 예측 과정에 확산 잡음 제거를 원활하게 통합하는 협력적 훈련 방식을 제안합니다. 이 방식을 통해, 우리는 이 두 행동 예측 방법이 서로를 강화할 뿐만 아니라 다양한 작업에 따라 서로 다른 강점을 보인다는 것을 발견했습니다. 따라서, 우리는 두 예측을 적응적으로 융합하여 더 강력한 제어를 이끌어내는 협력적 행동 앙상블 메커니즘을 설계합니다. HybridVLA는 시뮬레이션 및 실제 세계 작업에서 평균 성공률이 각각 14%와 19% 향상되어 이전 최첨단 VLA 방법을 능가하며, 보이지 않는 구성에서도 안정적인 조작을 보여줍니다.
