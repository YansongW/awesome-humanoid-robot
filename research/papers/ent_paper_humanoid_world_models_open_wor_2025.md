---
$id: ent_paper_humanoid_world_models_open_wor_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics'
  zh: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics'
  ko: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics'
summary:
  en: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics is a 2025 work on simulation benchmark for
    humanoid robots.'
  zh: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics is a 2025 work on simulation benchmark for
    humanoid robots.'
  ko: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics is a 2025 work on simulation benchmark for
    humanoid robots.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
- 10_evaluation_benchmarks
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- benchmark
- humanoid
- humanoid_world_models
- simulation
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2506.01182v2.
sources:
- id: src_001
  type: paper
  title: 'Humanoid World Models: Open World Foundation Models for Humanoid Robotics (arXiv)'
  url: https://arxiv.org/abs/2506.01182
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Humanoid robots, with their human-like form, are uniquely suited for interacting in environments built for people. However, enabling humanoids to reason, plan, and act in complex open-world settings remains a challenge. World models, models that predict the future outcome of a given action, can support these capabilities by serving as a dynamics model in long-horizon planning and generating synthetic data for policy learning. We introduce Humanoid World Models (HWM), a family of lightweight, open-source models that forecast future egocentric video conditioned on humanoid control tokens. We train two types of generative models, Masked Transformers and Flow-Matching, on 100 hours of humanoid demonstrations. Additionally, we explore architectural variants with different attention mechanisms and parameter-sharing strategies. Our parameter-sharing techniques reduce model size by 33-53% with minimal impact on performance or visual fidelity. HWMs are designed to be trained and deployed in practical academic and small-lab settings, such as 1-2 GPUs.

## 核心内容
Humanoid robots, with their human-like form, are uniquely suited for interacting in environments built for people. However, enabling humanoids to reason, plan, and act in complex open-world settings remains a challenge. World models, models that predict the future outcome of a given action, can support these capabilities by serving as a dynamics model in long-horizon planning and generating synthetic data for policy learning. We introduce Humanoid World Models (HWM), a family of lightweight, open-source models that forecast future egocentric video conditioned on humanoid control tokens. We train two types of generative models, Masked Transformers and Flow-Matching, on 100 hours of humanoid demonstrations. Additionally, we explore architectural variants with different attention mechanisms and parameter-sharing strategies. Our parameter-sharing techniques reduce model size by 33-53% with minimal impact on performance or visual fidelity. HWMs are designed to be trained and deployed in practical academic and small-lab settings, such as 1-2 GPUs.

## 参考
- http://arxiv.org/abs/2506.01182v2

## Overview
Humanoid robots, with their human-like form, are uniquely suited for interacting in environments built for people. However, enabling humanoids to reason, plan, and act in complex open-world settings remains a challenge. World models, models that predict the future outcome of a given action, can support these capabilities by serving as a dynamics model in long-horizon planning and generating synthetic data for policy learning. We introduce Humanoid World Models (HWM), a family of lightweight, open-source models that forecast future egocentric video conditioned on humanoid control tokens. We train two types of generative models, Masked Transformers and Flow-Matching, on 100 hours of humanoid demonstrations. Additionally, we explore architectural variants with different attention mechanisms and parameter-sharing strategies. Our parameter-sharing techniques reduce model size by 33-53% with minimal impact on performance or visual fidelity. HWMs are designed to be trained and deployed in practical academic and small-lab settings, such as 1-2 GPUs.

## Content
Humanoid robots, with their human-like form, are uniquely suited for interacting in environments built for people. However, enabling humanoids to reason, plan, and act in complex open-world settings remains a challenge. World models, models that predict the future outcome of a given action, can support these capabilities by serving as a dynamics model in long-horizon planning and generating synthetic data for policy learning. We introduce Humanoid World Models (HWM), a family of lightweight, open-source models that forecast future egocentric video conditioned on humanoid control tokens. We train two types of generative models, Masked Transformers and Flow-Matching, on 100 hours of humanoid demonstrations. Additionally, we explore architectural variants with different attention mechanisms and parameter-sharing strategies. Our parameter-sharing techniques reduce model size by 33-53% with minimal impact on performance or visual fidelity. HWMs are designed to be trained and deployed in practical academic and small-lab settings, such as 1-2 GPUs.

## 개요
휴머노이드 로봇은 인간과 유사한 형태를 갖추고 있어 인간을 위해 설계된 환경에서 상호작용하기에 특히 적합합니다. 그러나 휴머노이드가 복잡한 개방형 환경에서 추론, 계획 및 행동을 수행할 수 있도록 하는 것은 여전히 과제로 남아 있습니다. 월드 모델(World models)은 주어진 행동의 미래 결과를 예측하는 모델로, 장기 계획에서 동역학 모델 역할을 하며 정책 학습을 위한 합성 데이터를 생성함으로써 이러한 능력을 지원할 수 있습니다. 우리는 휴머노이드 제어 토큰에 조건화된 미래의 자아 중심 비디오를 예측하는 경량 오픈소스 모델군인 Humanoid World Models (HWM)을 소개합니다. 우리는 100시간의 휴머노이드 시연 데이터를 사용하여 Masked Transformers와 Flow-Matching이라는 두 가지 유형의 생성 모델을 학습시킵니다. 또한, 다양한 주의 메커니즘과 매개변수 공유 전략을 가진 아키텍처 변형을 탐구합니다. 우리의 매개변수 공유 기술은 성능이나 시각적 충실도에 미치는 영향을 최소화하면서 모델 크기를 33-53% 줄입니다. HWM은 1-2개의 GPU와 같은 실용적인 학술 및 소규모 연구실 환경에서 학습 및 배포될 수 있도록 설계되었습니다.

## 핵심 내용
휴머노이드 로봇은 인간과 유사한 형태를 갖추고 있어 인간을 위해 설계된 환경에서 상호작용하기에 특히 적합합니다. 그러나 휴머노이드가 복잡한 개방형 환경에서 추론, 계획 및 행동을 수행할 수 있도록 하는 것은 여전히 과제로 남아 있습니다. 월드 모델(World models)은 주어진 행동의 미래 결과를 예측하는 모델로, 장기 계획에서 동역학 모델 역할을 하며 정책 학습을 위한 합성 데이터를 생성함으로써 이러한 능력을 지원할 수 있습니다. 우리는 휴머노이드 제어 토큰에 조건화된 미래의 자아 중심 비디오를 예측하는 경량 오픈소스 모델군인 Humanoid World Models (HWM)을 소개합니다. 우리는 100시간의 휴머노이드 시연 데이터를 사용하여 Masked Transformers와 Flow-Matching이라는 두 가지 유형의 생성 모델을 학습시킵니다. 또한, 다양한 주의 메커니즘과 매개변수 공유 전략을 가진 아키텍처 변형을 탐구합니다. 우리의 매개변수 공유 기술은 성능이나 시각적 충실도에 미치는 영향을 최소화하면서 모델 크기를 33-53% 줄입니다. HWM은 1-2개의 GPU와 같은 실용적인 학술 및 소규모 연구실 환경에서 학습 및 배포될 수 있도록 설계되었습니다.
