---
$id: ent_paper_tactx_learning_shared_tactile_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
  zh: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
  ko: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
summary:
  en: 'arXiv:2606.31236v1 Announce Type: new Abstract: Tactile sensors provide critical information for contact-rich manipulation,
    yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across
    robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across
    sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps
    heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact
    data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained
    across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns
    tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity
    prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation
    tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one
    sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success
    rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.'
  zh: 'arXiv:2606.31236v1 Announce Type: new Abstract: Tactile sensors provide critical information for contact-rich manipulation,
    yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across
    robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across
    sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps
    heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact
    data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained
    across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns
    tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity
    prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation
    tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one
    sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success
    rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.'
  ko: 'arXiv:2606.31236v1 Announce Type: new Abstract: Tactile sensors provide critical information for contact-rich manipulation,
    yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across
    robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across
    sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps
    heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact
    data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained
    across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns
    tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity
    prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation
    tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one
    sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success
    rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.'
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
- robotics
- tactx
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2606.31236v1.
sources:
- id: src_001
  type: paper
  title: 'TactX: Learning Shared Tactile Representations Across Diverse Sensors'
  url: https://arxiv.org/abs/2606.31236
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Tactile sensors provide critical information for contact-rich manipulation, yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.

## 核心内容
Tactile sensors provide critical information for contact-rich manipulation, yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.

## 参考
- http://arxiv.org/abs/2606.31236v1

## Overview
Tactile sensors provide critical information for contact-rich manipulation, yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.

## Content
Tactile sensors provide critical information for contact-rich manipulation, yet tactile representations and policies remain tightly coupled to each specific sensor, limiting transferability across robots and hardware platforms. We propose TactX, a framework for learning a transferable tactile representation across sensors spanning three fundamentally different transduction modalities: resistive, magnetic, and vision-based. TactX maps heterogeneous tactile observations into a shared latent space through modality-specific encoders trained on paired contact data. Such paired interactions provide a natural alignment signal across modalities, and the encoders are jointly trained across all sensor pairs, inducing a consistent latent space for all sensor types. Our experiments show that TactX aligns tactile representations across sensors while preserving object-level contact information, as evidenced by sensor-identity prediction and object classification in the learned latent space. We evaluate TactX on four contact-rich manipulation tasks: pick-and-place, plug insertion, board wiping, and object reorientation, and show that policies trained with one sensor transfer zero-shot to physically distinct sensors through the shared latent. This improves the average success rate from 27.5% for vision-only policy to 45.9%, providing a step toward sensor-agnostic tactile manipulation.

## 개요
촉각 센서는 접촉이 많은 조작 작업에 중요한 정보를 제공하지만, 촉각 표현과 정책은 각 특정 센서에 밀접하게 결합되어 있어 로봇 및 하드웨어 플랫폼 간의 전이 가능성을 제한합니다. 우리는 저항성, 자기 기반, 시각 기반이라는 세 가지 근본적으로 다른 변환 방식을 아우르는 센서 간 전이 가능한 촉각 표현을 학습하기 위한 프레임워크인 TactX를 제안합니다. TactX는 쌍을 이루는 접촉 데이터로 훈련된 방식별 인코더를 통해 이질적인 촉각 관측값을 공유 잠재 공간으로 매핑합니다. 이러한 쌍을 이루는 상호작용은 방식 간 자연스러운 정렬 신호를 제공하며, 인코더는 모든 센서 쌍에 걸쳐 공동으로 훈련되어 모든 센서 유형에 대해 일관된 잠재 공간을 유도합니다. 실험 결과, TactX는 학습된 잠재 공간에서 센서 식별 예측 및 객체 분류를 통해 입증된 바와 같이 객체 수준의 접촉 정보를 보존하면서 센서 간 촉각 표현을 정렬함을 보여줍니다. 우리는 TactX를 집어 옮기기, 플러그 삽입, 보드 닦기, 객체 재배향이라는 네 가지 접촉이 많은 조작 작업에서 평가했으며, 하나의 센서로 훈련된 정책이 공유 잠재 공간을 통해 물리적으로 다른 센서로 제로샷 전이됨을 보여줍니다. 이는 시각 전용 정책의 평균 성공률을 27.5%에서 45.9%로 향상시켜, 센서에 구애받지 않는 촉각 조작을 위한 한 걸음을 제공합니다.

## 핵심 내용
촉각 센서는 접촉이 많은 조작 작업에 중요한 정보를 제공하지만, 촉각 표현과 정책은 각 특정 센서에 밀접하게 결합되어 있어 로봇 및 하드웨어 플랫폼 간의 전이 가능성을 제한합니다. 우리는 저항성, 자기 기반, 시각 기반이라는 세 가지 근본적으로 다른 변환 방식을 아우르는 센서 간 전이 가능한 촉각 표현을 학습하기 위한 프레임워크인 TactX를 제안합니다. TactX는 쌍을 이루는 접촉 데이터로 훈련된 방식별 인코더를 통해 이질적인 촉각 관측값을 공유 잠재 공간으로 매핑합니다. 이러한 쌍을 이루는 상호작용은 방식 간 자연스러운 정렬 신호를 제공하며, 인코더는 모든 센서 쌍에 걸쳐 공동으로 훈련되어 모든 센서 유형에 대해 일관된 잠재 공간을 유도합니다. 실험 결과, TactX는 학습된 잠재 공간에서 센서 식별 예측 및 객체 분류를 통해 입증된 바와 같이 객체 수준의 접촉 정보를 보존하면서 센서 간 촉각 표현을 정렬함을 보여줍니다. 우리는 TactX를 집어 옮기기, 플러그 삽입, 보드 닦기, 객체 재배향이라는 네 가지 접촉이 많은 조작 작업에서 평가했으며, 하나의 센서로 훈련된 정책이 공유 잠재 공간을 통해 물리적으로 다른 센서로 제로샷 전이됨을 보여줍니다. 이는 시각 전용 정책의 평균 성공률을 27.5%에서 45.9%로 향상시켜, 센서에 구애받지 않는 촉각 조작을 위한 한 걸음을 제공합니다.
