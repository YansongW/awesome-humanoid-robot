---
$id: ent_paper_physically_grounded_3d_generat_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  zh: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  ko: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
summary:
  en: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
  zh: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
  ko: 'arXiv:2604.09100v2 Announce Type: replace-cross Abstract: We propose a multimodal, physically grounded approach for
    metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware
    3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the
    posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded
    regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact
    latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining
    on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility
    masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and
    differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the
    reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure
    estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines
    geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves
    completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only
    baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different
    from those used during training.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- humanoid
- physically_grounded_3d_generat
- robotics
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2604.09100v2.
sources:
- id: src_001
  type: paper
  title: Physically Grounded 3D Generative Reconstruction under Hand Occlusion using Proprioception and Multi-Contact Touch
  url: https://arxiv.org/abs/2604.09100
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
We propose a multimodal, physically grounded approach for metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware 3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different from those used during training.

## 核心内容
We propose a multimodal, physically grounded approach for metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware 3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and differentiable decoder-guidance during finetuning and inference to reduce hand--object interpenetration and to align the reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different from those used during training.

## 参考
- http://arxiv.org/abs/2604.09100v2

## Overview
We propose a multimodal, physically grounded approach for metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware 3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and differentiable decoder-guidance during finetuning and inference to reduce hand–object interpenetration and to align the reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different from those used during training.

## Content
We propose a multimodal, physically grounded approach for metric-scale amodal object reconstruction and pose estimation under severe hand occlusion. Unlike prior occlusion-aware 3D generation methods that rely only on vision, we leverage physical interaction signals: proprioception provides the posed hand geometry, and multi-contact touch constrains where the object surface must lie, reducing ambiguity in occluded regions. We represent object structure as a pose-aware, camera-aligned signed distance field (SDF) and learn a compact latent space with a Structure-VAE. In this latent space, we train a conditional flow-matching diffusion model, pretraining on vision-only images and finetuning on occluded manipulation scenes while conditioning on visible RGB evidence, occluder/visibility masks, the hand latent representation, and tactile information. Crucially, we incorporate physics-based objectives and differentiable decoder-guidance during finetuning and inference to reduce hand–object interpenetration and to align the reconstructed surface with contact observations. Because our method produces a metric, physically consistent structure estimate, it integrates naturally into existing two-stage reconstruction pipelines, where a downstream module refines geometry and predicts appearance. Experiments in simulation show that adding proprioception and touch substantially improves completion under occlusion and yields physically plausible reconstructions at correct real-world scale compared to vision-only baselines; we further validate transfer by deploying the model on a real humanoid robot with an end-effector different from those used during training.

## 개요
본 연구는 심한 손 가림(hand occlusion) 상황에서 미터법 스케일의 아모달(amodal) 객체 재구성 및 자세 추정을 위한 다중 모달, 물리 기반 접근법을 제안합니다. 시각에만 의존하는 기존의 가림 인식 3D 생성 방법과 달리, 우리는 물리적 상호작용 신호를 활용합니다: 고유수용감각(proprioception)은 손의 자세 기하학을 제공하고, 다중 접촉 터치는 객체 표면이 위치해야 할 곳을 제약하여 가려진 영역의 모호성을 줄입니다. 객체 구조를 자세 인식, 카메라 정렬 부호 거리 필드(SDF)로 표현하고 Structure-VAE로 컴팩트한 잠재 공간을 학습합니다. 이 잠재 공간에서 조건부 흐름 매칭 확산 모델을 훈련하며, 시각 전용 이미지로 사전 훈련하고 가려진 조작 장면에서 미세 조정합니다. 이때 가시적인 RGB 증거, 가림/가시성 마스크, 손 잠재 표현, 촉각 정보를 조건으로 사용합니다. 핵심적으로, 미세 조정 및 추론 중 물리 기반 목표와 미분 가능 디코더 가이던스를 통합하여 손-객체 간 침투를 줄이고 재구성된 표면을 접촉 관측과 정렬합니다. 본 방법은 미터법, 물리적으로 일관된 구조 추정치를 생성하므로, 하위 모듈이 기하학을 정제하고 외관을 예측하는 기존의 2단계 재구성 파이프라인에 자연스럽게 통합됩니다. 시뮬레이션 실험에서 고유수용감각과 터치를 추가하면 가림 하에서 완성도가 크게 향상되고, 시각 전용 기준선과 비교하여 올바른 실제 세계 스케일에서 물리적으로 그럴듯한 재구성을 제공함을 보여줍니다. 또한, 훈련 중 사용된 것과 다른 엔드 이펙터를 가진 실제 인간형 로봇에 모델을 배포하여 전이 가능성을 검증합니다.

## 핵심 내용
본 연구는 심한 손 가림 상황에서 미터법 스케일의 아모달 객체 재구성 및 자세 추정을 위한 다중 모달, 물리 기반 접근법을 제안합니다. 시각에만 의존하는 기존의 가림 인식 3D 생성 방법과 달리, 우리는 물리적 상호작용 신호를 활용합니다: 고유수용감각은 손의 자세 기하학을 제공하고, 다중 접촉 터치는 객체 표면이 위치해야 할 곳을 제약하여 가려진 영역의 모호성을 줄입니다. 객체 구조를 자세 인식, 카메라 정렬 부호 거리 필드(SDF)로 표현하고 Structure-VAE로 컴팩트한 잠재 공간을 학습합니다. 이 잠재 공간에서 조건부 흐름 매칭 확산 모델을 훈련하며, 시각 전용 이미지로 사전 훈련하고 가려진 조작 장면에서 미세 조정합니다. 이때 가시적인 RGB 증거, 가림/가시성 마스크, 손 잠재 표현, 촉각 정보를 조건으로 사용합니다. 핵심적으로, 미세 조정 및 추론 중 물리 기반 목표와 미분 가능 디코더 가이던스를 통합하여 손-객체 간 침투를 줄이고 재구성된 표면을 접촉 관측과 정렬합니다. 본 방법은 미터법, 물리적으로 일관된 구조 추정치를 생성하므로, 하위 모듈이 기하학을 정제하고 외관을 예측하는 기존의 2단계 재구성 파이프라인에 자연스럽게 통합됩니다. 시뮬레이션 실험에서 고유수용감각과 터치를 추가하면 가림 하에서 완성도가 크게 향상되고, 시각 전용 기준선과 비교하여 올바른 실제 세계 스케일에서 물리적으로 그럴듯한 재구성을 제공함을 보여줍니다. 또한, 훈련 중 사용된 것과 다른 엔드 이펙터를 가진 실제 인간형 로봇에 모델을 배포하여 전이 가능성을 검증합니다.
