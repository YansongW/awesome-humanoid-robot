---
$id: ent_paper_abouzeid_geoaware_vla_implicit_geometry_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model'
  zh: GeoAware-VLA
  ko: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model'
summary:
  en: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (GeoAware-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mohamed bin Zayed University of Artificial Intelligence.'
  zh: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (GeoAware-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mohamed bin Zayed University of Artificial Intelligence.'
  ko: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (GeoAware-VLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Mohamed bin Zayed University of Artificial Intelligence.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- geoaware_vla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.14117v4.
sources:
- id: src_001
  type: paper
  title: 'GeoAware-VLA: Implicit Geometry Aware Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2509.14117
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GeoAware-VLA source
  url: https://doi.org/10.48550/arXiv.2509.14117
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models often fail to generalize to unseen camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images. We introduce GeoAware-VLA, a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone. Instead of training a visual encoder or relying on explicit 3D data, we leverage a frozen, pretrained geometric vision model as a feature extractor. A lightweight, trainable projection layer then adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch. Through extensive evaluations on the LIBERO and CALVIN benchmarks, we show that GeoAware-VLA preserves and even improves in-distribution performance while achieving substantial gains in zero-shot generalization to unseen camera poses, improving unseen-view success rates by an average of 35 percentage points on LIBERO and over 11 percentage points on CALVIN compared to their respective baselines. Crucially, these gains transfer to the physical world, where our model shows significant improvement on a real robotic platform. Our approach proves effective across both continuous and discrete action spaces, highlighting that robust geometric grounding is a key ingredient for building more generalizable robotic agents.

## 核心内容
Vision-Language-Action (VLA) models often fail to generalize to unseen camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images. We introduce GeoAware-VLA, a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone. Instead of training a visual encoder or relying on explicit 3D data, we leverage a frozen, pretrained geometric vision model as a feature extractor. A lightweight, trainable projection layer then adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch. Through extensive evaluations on the LIBERO and CALVIN benchmarks, we show that GeoAware-VLA preserves and even improves in-distribution performance while achieving substantial gains in zero-shot generalization to unseen camera poses, improving unseen-view success rates by an average of 35 percentage points on LIBERO and over 11 percentage points on CALVIN compared to their respective baselines. Crucially, these gains transfer to the physical world, where our model shows significant improvement on a real robotic platform. Our approach proves effective across both continuous and discrete action spaces, highlighting that robust geometric grounding is a key ingredient for building more generalizable robotic agents.

## 参考
- http://arxiv.org/abs/2509.14117v4

## Overview
Vision-Language-Action (VLA) models often fail to generalize to unseen camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images. We introduce GeoAware-VLA, a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone. Instead of training a visual encoder or relying on explicit 3D data, we leverage a frozen, pretrained geometric vision model as a feature extractor. A lightweight, trainable projection layer then adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch. Through extensive evaluations on the LIBERO and CALVIN benchmarks, we show that GeoAware-VLA preserves and even improves in-distribution performance while achieving substantial gains in zero-shot generalization to unseen camera poses, improving unseen-view success rates by an average of 35 percentage points on LIBERO and over 11 percentage points on CALVIN compared to their respective baselines. Crucially, these gains transfer to the physical world, where our model shows significant improvement on a real robotic platform. Our approach proves effective across both continuous and discrete action spaces, highlighting that robust geometric grounding is a key ingredient for building more generalizable robotic agents.

## Content
Vision-Language-Action (VLA) models often fail to generalize to unseen camera viewpoints, a limitation stemming from their difficulty in inferring robust 3D geometry from 2D images. We introduce GeoAware-VLA, a simple yet effective approach that enhances viewpoint invariance by integrating strong geometric priors into the vision backbone. Instead of training a visual encoder or relying on explicit 3D data, we leverage a frozen, pretrained geometric vision model as a feature extractor. A lightweight, trainable projection layer then adapts these geometrically-rich features for the policy decoder, relieving it of the burden of learning 3D consistency from scratch. Through extensive evaluations on the LIBERO and CALVIN benchmarks, we show that GeoAware-VLA preserves and even improves in-distribution performance while achieving substantial gains in zero-shot generalization to unseen camera poses, improving unseen-view success rates by an average of 35 percentage points on LIBERO and over 11 percentage points on CALVIN compared to their respective baselines. Crucially, these gains transfer to the physical world, where our model shows significant improvement on a real robotic platform. Our approach proves effective across both continuous and discrete action spaces, highlighting that robust geometric grounding is a key ingredient for building more generalizable robotic agents.

## 개요
Vision-Language-Action (VLA) 모델은 종종 보지 못한 카메라 시점으로의 일반화에 실패하는데, 이는 2D 이미지로부터 강건한 3D 기하학을 추론하는 데 어려움을 겪기 때문입니다. 우리는 강력한 기하학적 사전 지식을 비전 백본에 통합하여 시점 불변성을 향상시키는 간단하면서도 효과적인 접근법인 GeoAware-VLA를 소개합니다. 시각 인코더를 훈련시키거나 명시적인 3D 데이터에 의존하는 대신, 우리는 동결된 사전 훈련된 기하학적 비전 모델을 특징 추출기로 활용합니다. 그런 다음 가볍고 훈련 가능한 투영 레이어가 이러한 기하학적 특징을 정책 디코더에 맞게 조정하여, 처음부터 3D 일관성을 학습해야 하는 부담을 덜어줍니다. LIBERO 및 CALVIN 벤치마크에 대한 광범위한 평가를 통해, GeoAware-VLA가 분포 내 성능을 유지하고 심지어 향상시키면서, 보지 못한 카메라 포즈에 대한 제로샷 일반화에서 상당한 이득을 얻는다는 것을 보여줍니다. 각각의 기준선과 비교하여 LIBERO에서 평균 35% 포인트, CALVIN에서 11% 포인트 이상의 보지 못한 시점 성공률 향상을 달성했습니다. 결정적으로, 이러한 이득은 실제 세계로 전이되어, 실제 로봇 플랫폼에서 모델이 상당한 개선을 보여줍니다. 우리의 접근법은 연속 및 이산 행동 공간 모두에서 효과적임을 입증하며, 강건한 기하학적 기반이 더 일반화 가능한 로봇 에이전트를 구축하는 핵심 요소임을 강조합니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 종종 보지 못한 카메라 시점으로의 일반화에 실패하는데, 이는 2D 이미지로부터 강건한 3D 기하학을 추론하는 데 어려움을 겪기 때문입니다. 우리는 강력한 기하학적 사전 지식을 비전 백본에 통합하여 시점 불변성을 향상시키는 간단하면서도 효과적인 접근법인 GeoAware-VLA를 소개합니다. 시각 인코더를 훈련시키거나 명시적인 3D 데이터에 의존하는 대신, 우리는 동결된 사전 훈련된 기하학적 비전 모델을 특징 추출기로 활용합니다. 그런 다음 가볍고 훈련 가능한 투영 레이어가 이러한 기하학적 특징을 정책 디코더에 맞게 조정하여, 처음부터 3D 일관성을 학습해야 하는 부담을 덜어줍니다. LIBERO 및 CALVIN 벤치마크에 대한 광범위한 평가를 통해, GeoAware-VLA가 분포 내 성능을 유지하고 심지어 향상시키면서, 보지 못한 카메라 포즈에 대한 제로샷 일반화에서 상당한 이득을 얻는다는 것을 보여줍니다. 각각의 기준선과 비교하여 LIBERO에서 평균 35% 포인트, CALVIN에서 11% 포인트 이상의 보지 못한 시점 성공률 향상을 달성했습니다. 결정적으로, 이러한 이득은 실제 세계로 전이되어, 실제 로봇 플랫폼에서 모델이 상당한 개선을 보여줍니다. 우리의 접근법은 연속 및 이산 행동 공간 모두에서 효과적임을 입증하며, 강건한 기하학적 기반이 더 일반화 가능한 로봇 에이전트를 구축하는 핵심 요소임을 강조합니다.
