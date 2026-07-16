---
$id: ent_paper_tedi_temporally_entangled_diff_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
  zh: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
  ko: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis'
summary:
  en: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.'
  zh: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.'
  ko: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis is a 2023 work on human motion analysis and synthesis
    for humanoid robots.'
domains:
- 07_ai_models_algorithms
- 09_data_datasets
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- motion_analysis
- motion_synthesis
- tedi
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2307.15042v2.
sources:
- id: src_001
  type: paper
  title: 'TEDi: Temporally-Entangled Diffusion for Long-Term Motion Synthesis (arXiv)'
  url: https://arxiv.org/abs/2307.15042
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
The gradual nature of a diffusion process that synthesizes samples in small increments constitutes a key ingredient of Denoising Diffusion Probabilistic Models (DDPM), which have presented unprecedented quality in image synthesis and been recently explored in the motion domain. In this work, we propose to adapt the gradual diffusion concept (operating along a diffusion time-axis) into the temporal-axis of the motion sequence. Our key idea is to extend the DDPM framework to support temporally varying denoising, thereby entangling the two axes. Using our special formulation, we iteratively denoise a motion buffer that contains a set of increasingly-noised poses, which auto-regressively produces an arbitrarily long stream of frames. With a stationary diffusion time-axis, in each diffusion step we increment only the temporal-axis of the motion such that the framework produces a new, clean frame which is removed from the beginning of the buffer, followed by a newly drawn noise vector that is appended to it. This new mechanism paves the way towards a new framework for long-term motion synthesis with applications to character animation and other domains.

## 核心内容
The gradual nature of a diffusion process that synthesizes samples in small increments constitutes a key ingredient of Denoising Diffusion Probabilistic Models (DDPM), which have presented unprecedented quality in image synthesis and been recently explored in the motion domain. In this work, we propose to adapt the gradual diffusion concept (operating along a diffusion time-axis) into the temporal-axis of the motion sequence. Our key idea is to extend the DDPM framework to support temporally varying denoising, thereby entangling the two axes. Using our special formulation, we iteratively denoise a motion buffer that contains a set of increasingly-noised poses, which auto-regressively produces an arbitrarily long stream of frames. With a stationary diffusion time-axis, in each diffusion step we increment only the temporal-axis of the motion such that the framework produces a new, clean frame which is removed from the beginning of the buffer, followed by a newly drawn noise vector that is appended to it. This new mechanism paves the way towards a new framework for long-term motion synthesis with applications to character animation and other domains.

## 参考
- http://arxiv.org/abs/2307.15042v2

## Overview
The gradual nature of a diffusion process that synthesizes samples in small increments constitutes a key ingredient of Denoising Diffusion Probabilistic Models (DDPM), which have presented unprecedented quality in image synthesis and been recently explored in the motion domain. In this work, we propose to adapt the gradual diffusion concept (operating along a diffusion time-axis) into the temporal-axis of the motion sequence. Our key idea is to extend the DDPM framework to support temporally varying denoising, thereby entangling the two axes. Using our special formulation, we iteratively denoise a motion buffer that contains a set of increasingly-noised poses, which auto-regressively produces an arbitrarily long stream of frames. With a stationary diffusion time-axis, in each diffusion step we increment only the temporal-axis of the motion such that the framework produces a new, clean frame which is removed from the beginning of the buffer, followed by a newly drawn noise vector that is appended to it. This new mechanism paves the way towards a new framework for long-term motion synthesis with applications to character animation and other domains.

## Content
The gradual nature of a diffusion process that synthesizes samples in small increments constitutes a key ingredient of Denoising Diffusion Probabilistic Models (DDPM), which have presented unprecedented quality in image synthesis and been recently explored in the motion domain. In this work, we propose to adapt the gradual diffusion concept (operating along a diffusion time-axis) into the temporal-axis of the motion sequence. Our key idea is to extend the DDPM framework to support temporally varying denoising, thereby entangling the two axes. Using our special formulation, we iteratively denoise a motion buffer that contains a set of increasingly-noised poses, which auto-regressively produces an arbitrarily long stream of frames. With a stationary diffusion time-axis, in each diffusion step we increment only the temporal-axis of the motion such that the framework produces a new, clean frame which is removed from the beginning of the buffer, followed by a newly drawn noise vector that is appended to it. This new mechanism paves the way towards a new framework for long-term motion synthesis with applications to character animation and other domains.

## 개요
확산 과정의 점진적 특성은 샘플을 작은 단위로 합성하는 방식으로, Denoising Diffusion Probabilistic Models (DDPM)의 핵심 요소를 구성합니다. DDPM은 이미지 합성에서 전례 없는 품질을 보여주었으며, 최근 모션 영역에서도 탐구되고 있습니다. 본 연구에서는 점진적 확산 개념(확산 시간 축을 따라 작동)을 모션 시퀀스의 시간 축에 적용하는 것을 제안합니다. 핵심 아이디어는 DDPM 프레임워크를 확장하여 시간에 따라 변하는 노이즈 제거를 지원함으로써 두 축을 결합하는 것입니다. 특수한 공식을 통해 점점 더 노이즈가 추가된 포즈 집합을 포함하는 모션 버퍼를 반복적으로 노이즈 제거하여, 임의로 긴 프레임 스트림을 자기회귀적으로 생성합니다. 고정된 확산 시간 축에서 각 확산 단계마다 모션의 시간 축만 증가시켜 프레임워크가 새로운 깨끗한 프레임을 생성하고, 이는 버퍼의 시작 부분에서 제거된 후 새로 추출된 노이즈 벡터가 버퍼에 추가됩니다. 이 새로운 메커니즘은 캐릭터 애니메이션 및 기타 도메인에 적용 가능한 장기 모션 합성을 위한 새로운 프레임워크의 길을 열어줍니다.

## 핵심 내용
확산 과정의 점진적 특성은 샘플을 작은 단위로 합성하는 방식으로, Denoising Diffusion Probabilistic Models (DDPM)의 핵심 요소를 구성합니다. DDPM은 이미지 합성에서 전례 없는 품질을 보여주었으며, 최근 모션 영역에서도 탐구되고 있습니다. 본 연구에서는 점진적 확산 개념(확산 시간 축을 따라 작동)을 모션 시퀀스의 시간 축에 적용하는 것을 제안합니다. 핵심 아이디어는 DDPM 프레임워크를 확장하여 시간에 따라 변하는 노이즈 제거를 지원함으로써 두 축을 결합하는 것입니다. 특수한 공식을 통해 점점 더 노이즈가 추가된 포즈 집합을 포함하는 모션 버퍼를 반복적으로 노이즈 제거하여, 임의로 긴 프레임 스트림을 자기회귀적으로 생성합니다. 고정된 확산 시간 축에서 각 확산 단계마다 모션의 시간 축만 증가시켜 프레임워크가 새로운 깨끗한 프레임을 생성하고, 이는 버퍼의 시작 부분에서 제거된 후 새로 추출된 노이즈 벡터가 버퍼에 추가됩니다. 이 새로운 메커니즘은 캐릭터 애니메이션 및 기타 도메인에 적용 가능한 장기 모션 합성을 위한 새로운 프레임워크의 길을 열어줍니다.
