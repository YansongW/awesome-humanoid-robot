---
$id: ent_paper_guided_motion_diffusion_for_co_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Guided Motion Diffusion for Controllable Human Motion Synthesis
  zh: Guided Motion Diffusion for Controllable Human Motion Synthesis
  ko: Guided Motion Diffusion for Controllable Human Motion Synthesis
summary:
  en: Guided Motion Diffusion for Controllable Human Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
  zh: Guided Motion Diffusion for Controllable Human Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
  ko: Guided Motion Diffusion for Controllable Human Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- guided_motion_diffusion_for_co
- humanoid
- motion_analysis
- motion_synthesis
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2305.12577v3.
sources:
- id: src_001
  type: paper
  title: Guided Motion Diffusion for Controllable Human Motion Synthesis (arXiv)
  url: https://arxiv.org/abs/2305.12577
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
Denoising diffusion models have shown great promise in human motion synthesis conditioned on natural language descriptions. However, integrating spatial constraints, such as pre-defined motion trajectories and obstacles, remains a challenge despite being essential for bridging the gap between isolated human motion and its surrounding environment. To address this issue, we propose Guided Motion Diffusion (GMD), a method that incorporates spatial constraints into the motion generation process. Specifically, we propose an effective feature projection scheme that manipulates motion representation to enhance the coherency between spatial information and local poses. Together with a new imputation formulation, the generated motion can reliably conform to spatial constraints such as global motion trajectories. Furthermore, given sparse spatial constraints (e.g. sparse keyframes), we introduce a new dense guidance approach to turn a sparse signal, which is susceptible to being ignored during the reverse steps, into denser signals to guide the generated motion to the given constraints. Our extensive experiments justify the development of GMD, which achieves a significant improvement over state-of-the-art methods in text-based motion generation while allowing control of the synthesized motions with spatial constraints.

## 核心内容
Denoising diffusion models have shown great promise in human motion synthesis conditioned on natural language descriptions. However, integrating spatial constraints, such as pre-defined motion trajectories and obstacles, remains a challenge despite being essential for bridging the gap between isolated human motion and its surrounding environment. To address this issue, we propose Guided Motion Diffusion (GMD), a method that incorporates spatial constraints into the motion generation process. Specifically, we propose an effective feature projection scheme that manipulates motion representation to enhance the coherency between spatial information and local poses. Together with a new imputation formulation, the generated motion can reliably conform to spatial constraints such as global motion trajectories. Furthermore, given sparse spatial constraints (e.g. sparse keyframes), we introduce a new dense guidance approach to turn a sparse signal, which is susceptible to being ignored during the reverse steps, into denser signals to guide the generated motion to the given constraints. Our extensive experiments justify the development of GMD, which achieves a significant improvement over state-of-the-art methods in text-based motion generation while allowing control of the synthesized motions with spatial constraints.

## 参考
- http://arxiv.org/abs/2305.12577v3

## Overview
Denoising diffusion models have shown great promise in human motion synthesis conditioned on natural language descriptions. However, integrating spatial constraints, such as pre-defined motion trajectories and obstacles, remains a challenge despite being essential for bridging the gap between isolated human motion and its surrounding environment. To address this issue, we propose Guided Motion Diffusion (GMD), a method that incorporates spatial constraints into the motion generation process. Specifically, we propose an effective feature projection scheme that manipulates motion representation to enhance the coherency between spatial information and local poses. Together with a new imputation formulation, the generated motion can reliably conform to spatial constraints such as global motion trajectories. Furthermore, given sparse spatial constraints (e.g. sparse keyframes), we introduce a new dense guidance approach to turn a sparse signal, which is susceptible to being ignored during the reverse steps, into denser signals to guide the generated motion to the given constraints. Our extensive experiments justify the development of GMD, which achieves a significant improvement over state-of-the-art methods in text-based motion generation while allowing control of the synthesized motions with spatial constraints.

## Content
Denoising diffusion models have shown great promise in human motion synthesis conditioned on natural language descriptions. However, integrating spatial constraints, such as pre-defined motion trajectories and obstacles, remains a challenge despite being essential for bridging the gap between isolated human motion and its surrounding environment. To address this issue, we propose Guided Motion Diffusion (GMD), a method that incorporates spatial constraints into the motion generation process. Specifically, we propose an effective feature projection scheme that manipulates motion representation to enhance the coherency between spatial information and local poses. Together with a new imputation formulation, the generated motion can reliably conform to spatial constraints such as global motion trajectories. Furthermore, given sparse spatial constraints (e.g. sparse keyframes), we introduce a new dense guidance approach to turn a sparse signal, which is susceptible to being ignored during the reverse steps, into denser signals to guide the generated motion to the given constraints. Our extensive experiments justify the development of GMD, which achieves a significant improvement over state-of-the-art methods in text-based motion generation while allowing control of the synthesized motions with spatial constraints.

## 개요
Denoising 확산 모델은 자연어 설명에 기반한 인간 동작 합성에서 큰 가능성을 보여주었습니다. 그러나 사전 정의된 동작 궤적 및 장애물과 같은 공간적 제약 조건을 통합하는 것은, 고립된 인간 동작과 주변 환경 간의 격차를 해소하는 데 필수적임에도 불구하고 여전히 어려운 과제로 남아 있습니다. 이 문제를 해결하기 위해, 우리는 공간적 제약 조건을 동작 생성 과정에 통합하는 방법인 Guided Motion Diffusion (GMD)을 제안합니다. 구체적으로, 우리는 공간 정보와 국소 포즈 간의 일관성을 향상시키기 위해 동작 표현을 조작하는 효과적인 특징 투영 기법을 제안합니다. 새로운 대체(imputation) 공식과 함께, 생성된 동작은 전역 동작 궤적과 같은 공간적 제약 조건을 신뢰성 있게 따를 수 있습니다. 또한, 희소한 공간적 제약 조건(예: 희소 키프레임)이 주어졌을 때, 역방향 단계에서 무시되기 쉬운 희소 신호를 더 조밀한 신호로 변환하여 생성된 동작을 주어진 제약 조건으로 안내하는 새로운 조밀 안내(dense guidance) 접근법을 도입합니다. 광범위한 실험을 통해 GMD의 개발이 정당화되었으며, 이는 텍스트 기반 동작 생성에서 최신 방법 대비 상당한 개선을 달성하면서도 공간적 제약 조건으로 합성된 동작을 제어할 수 있게 합니다.

## 핵심 내용
Denoising 확산 모델은 자연어 설명에 기반한 인간 동작 합성에서 큰 가능성을 보여주었습니다. 그러나 사전 정의된 동작 궤적 및 장애물과 같은 공간적 제약 조건을 통합하는 것은, 고립된 인간 동작과 주변 환경 간의 격차를 해소하는 데 필수적임에도 불구하고 여전히 어려운 과제로 남아 있습니다. 이 문제를 해결하기 위해, 우리는 공간적 제약 조건을 동작 생성 과정에 통합하는 방법인 Guided Motion Diffusion (GMD)을 제안합니다. 구체적으로, 우리는 공간 정보와 국소 포즈 간의 일관성을 향상시키기 위해 동작 표현을 조작하는 효과적인 특징 투영 기법을 제안합니다. 새로운 대체(imputation) 공식과 함께, 생성된 동작은 전역 동작 궤적과 같은 공간적 제약 조건을 신뢰성 있게 따를 수 있습니다. 또한, 희소한 공간적 제약 조건(예: 희소 키프레임)이 주어졌을 때, 역방향 단계에서 무시되기 쉬운 희소 신호를 더 조밀한 신호로 변환하여 생성된 동작을 주어진 제약 조건으로 안내하는 새로운 조밀 안내(dense guidance) 접근법을 도입합니다. 광범위한 실험을 통해 GMD의 개발이 정당화되었으며, 이는 텍스트 기반 동작 생성에서 최신 방법 대비 상당한 개선을 달성하면서도 공간적 제약 조건으로 합성된 동작을 제어할 수 있게 합니다.
