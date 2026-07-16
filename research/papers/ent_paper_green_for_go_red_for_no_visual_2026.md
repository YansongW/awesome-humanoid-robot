---
$id: ent_paper_green_for_go_red_for_no_visual_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies'
  zh: 'Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies'
  ko: 'Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies'
summary:
  en: 'arXiv:2607.05122v1 Announce Type: cross Abstract: Vision-language-action (VLA) models enable robot navigation from
    natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations.
    This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time
    segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using
    SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA
    on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint,
    depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding
    provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory
    length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results
    indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model
    retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.'
  zh: 'arXiv:2607.05122v1 Announce Type: cross Abstract: Vision-language-action (VLA) models enable robot navigation from
    natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations.
    This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time
    segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using
    SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA
    on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint,
    depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding
    provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory
    length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results
    indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model
    retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.'
  ko: 'arXiv:2607.05122v1 Announce Type: cross Abstract: Vision-language-action (VLA) models enable robot navigation from
    natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations.
    This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time
    segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using
    SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA
    on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint,
    depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding
    provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory
    length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results
    indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model
    retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.'
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
- green_for_go_red_for_no
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.05122v1.
sources:
- id: src_001
  type: paper
  title: 'Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies (arXiv)'
  url: https://arxiv.org/abs/2607.05122
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.

## 核心内容
Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.

## 参考
- http://arxiv.org/abs/2607.05122v1

## Overview
Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.

## Content
Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.

## 개요
Vision-language-action (VLA) 모델은 자연어 및 시각적 목표를 통해 로봇 내비게이션을 가능하게 하지만, 지각적 방해 요소와 모호한 장면 해석에 취약한 상태를 유지합니다. 본 논문은 VLA 내비게이션 정책에 대한 시각적 근거의 첫 번째 실증적 평가를 제시합니다. 우리는 SegFormer를 사용하여 이동 가능 영역을 녹색, 이동 불가능 영역을 빨간색으로 강조하는 실시간 분할 기반 근거 방법을 제안합니다. 관찰 전용 분할과 관찰-목표 결합 증강의 두 가지 변형이 평가됩니다. Grand Tour 데이터셋에서 OmniVLA를 사용하여, 시각적 근거가 명령 길이에 따라 가장 먼 경유점에서 평균 경유점 오차를 27-44% 감소시킴을 보여줍니다. 이점은 짧은 명령보다 긴 명령에서 더 크며, 이미지 목표에 대해서는 근거가 거의 개선을 제공하지 않습니다. 정규화된 오차 분석은 근거가 주로 궤적 길이 정규화기 역할을 하여, 단위 거리당 추론 능력을 개선하지 않고 예측 경로 길이를 30% 감소시킴을 나타냅니다. 우리의 결과는 시각적 근거가 모델 재훈련 없이 VLA 내비게이션을 개선하는 간단하고 계산 비용이 적은 방법을 제공하지만, 분포 외 명령에서 누락된 훈련 신호를 보상할 수는 없음을 시사합니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 자연어 및 시각적 목표를 통해 로봇 내비게이션을 가능하게 하지만, 지각적 방해 요소와 모호한 장면 해석에 취약한 상태를 유지합니다. 본 논문은 VLA 내비게이션 정책에 대한 시각적 근거의 첫 번째 실증적 평가를 제시합니다. 우리는 SegFormer를 사용하여 이동 가능 영역을 녹색, 이동 불가능 영역을 빨간색으로 강조하는 실시간 분할 기반 근거 방법을 제안합니다. 관찰 전용 분할과 관찰-목표 결합 증강의 두 가지 변형이 평가됩니다. Grand Tour 데이터셋에서 OmniVLA를 사용하여, 시각적 근거가 명령 길이에 따라 가장 먼 경유점에서 평균 경유점 오차를 27-44% 감소시킴을 보여줍니다. 이점은 짧은 명령보다 긴 명령에서 더 크며, 이미지 목표에 대해서는 근거가 거의 개선을 제공하지 않습니다. 정규화된 오차 분석은 근거가 주로 궤적 길이 정규화기 역할을 하여, 단위 거리당 추론 능력을 개선하지 않고 예측 경로 길이를 30% 감소시킴을 나타냅니다. 우리의 결과는 시각적 근거가 모델 재훈련 없이 VLA 내비게이션을 개선하는 간단하고 계산 비용이 적은 방법을 제공하지만, 분포 외 명령에서 누락된 훈련 신호를 보상할 수는 없음을 시사합니다.
