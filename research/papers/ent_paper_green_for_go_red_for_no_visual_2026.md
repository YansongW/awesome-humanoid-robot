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
  zh: 本文首次对视觉语言动作（VLA）导航策略中的视觉基础（visual grounding）进行了实证评估。作者提出一种基于SegFormer的实时分割方法，将可通行区域标记为绿色、不可通行区域标记为红色，在Grand Tour数据集上使用OmniVLA模型，使最远航点误差降低27-44%。该方法无需重新训练模型，主要作为轨迹长度正则化器，将预测路径长度缩短30%。
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
  notes: 'Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2607.05122v1. [2026-07-29]
    zh content backfilled from English abstract via scripts/sinicize_english_cards.py | WP4 trilingual backfill 2026-08-10:
    ko body retranslated from zh deep-read (650 chars, DeepSeek).'
sources:
- id: src_001
  type: paper
  title: 'Green for Go, Red for No: Visual Grounding via Semantic Segmentation for VLA Navigation Policies (arXiv)'
  url: https://arxiv.org/abs/2607.05122
  date: '2026'
  accessed_at: '2026-07-08'
---
## 概述
该研究针对VLA导航模型易受感知干扰和场景歧义影响的问题，提出一种轻量级的视觉基础方法。方法基于SegFormer语义分割，实时将可通行区域高亮为绿色、不可通行区域高亮为红色，并评估了仅观测分割与观测-目标联合增强两种变体。在Grand Tour数据集上使用OmniVLA的实验表明，该方法在最远航点处将平均航点误差降低27-44%，且对长指令的改善效果优于短指令，但对图像目标几乎无提升。归一化误差分析揭示，视觉基础主要通过缩短预测路径长度（减少30%）来提升性能，而非改善单位距离推理能力。

## 核心内容
### 方法
- 提出基于SegFormer的实时语义分割方法，将可通行区域着色为绿色、不可通行区域着色为红色。
- 评估两种变体：
  - **观测仅分割**：仅对当前观测图像进行分割。
  - **观测-目标联合增强**：同时对观测图像和目标图像进行分割。

### 实验设置
- 使用OmniVLA模型在Grand Tour数据集上进行评估。
- 关键指标：最远航点处的平均航点误差（mean waypoint error）。

### 关键结果
- 视觉基础使最远航点误差降低27-44%，具体幅度取决于指令长度。
- 长指令的改善效果显著优于短指令；对图像目标几乎无提升。
- 归一化误差分析表明，视觉基础主要作为轨迹长度正则化器，将预测路径长度缩短30%，但未改善单位距离推理能力。
- 该方法无需重新训练模型，计算开销低，但无法补偿分布外指令中缺失的训练信号。

## Overview
Vision-language-action (VLA) models enable robot navigation from natural language and visual goals, but remain susceptible to perceptual distractions and ambiguous scene interpretations. This paper presents the first empirical evaluation of visual grounding for VLA navigation policies. We propose a real-time segmentation-based grounding method that highlights traversable areas in green and non-traversable areas in red using SegFormer. Two variants are evaluated: observation-only segmentation and joint observation-goal augmentation. Using OmniVLA on the Grand Tour dataset, we show that visual grounding reduces the mean waypoint error by 27-44% at the farthest waypoint, depending on the instruction length. The benefits are greater for long instructions than for short instructions, and grounding provides little improvement for image goals. Normalized error analysis indicates that grounding primarily acts as a trajectory length regularizer, reducing the predicted path length by 30% without improving per-unit-distance reasoning. Our results indicate that visual grounding offers a simple, computationally inexpensive method to improve VLA navigation without model retraining, although it cannot compensate for missing training signals in out-of-distribution instructions.

## 参考
- http://arxiv.org/abs/2607.05122v1

## 개요
이 연구는 VLA 내비게이션 모델이 인식 간섭과 장면 모호성에 취약한 문제를 해결하기 위해, 경량화된 시각적 기반(visual grounding) 방법을 제안한다. 이 방법은 SegFormer 의미론적 분할을 기반으로, 실시간으로 주행 가능 영역을 녹색으로, 주행 불가 영역을 빨간색으로 강조하며, 관측만 분할하는 변형과 관측-목표 결합 강화의 두 가지 변형을 평가한다. Grand Tour 데이터셋에서 OmniVLA를 사용한 실험 결과, 이 방법은 가장 먼 웨이포인트에서 평균 웨이포인트 오차를 27-44% 감소시켰으며, 긴 명령에 대한 개선 효과가 짧은 명령보다 우수했지만 이미지 목표에 대해서는 거의 개선이 없었다. 정규화된 오차 분석은 시각적 기반이 주로 예측 경로 길이를 30% 단축시켜 성능을 향상시키며, 단위 거리 추론 능력은 개선하지 않음을 밝혀냈다.

## 핵심 내용
### 방법
- SegFormer 기반 실시간 의미론적 분할 방법을 제안하여, 주행 가능 영역을 녹색으로, 주행 불가 영역을 빨간색으로 색칠한다.
- 두 가지 변형을 평가:
  - **관측만 분할**: 현재 관측 이미지만 분할.
  - **관측-목표 결합 강화**: 관측 이미지와 목표 이미지를 동시에 분할.

### 실험 설정
- OmniVLA 모델을 Grand Tour 데이터셋에서 평가.
- 핵심 지표: 가장 먼 웨이포인트에서의 평균 웨이포인트 오차(mean waypoint error).

### 핵심 결과
- 시각적 기반은 가장 먼 웨이포인트 오차를 27-44% 감소시키며, 구체적인 감소 폭은 명령 길이에 따라 달라진다.
- 긴 명령에 대한 개선 효과가 짧은 명령보다 현저히 우수하며, 이미지 목표에 대해서는 거의 개선이 없다.
- 정규화된 오차 분석은 시각적 기반이 주로 궤적 길이 정규화기로 작용하여 예측 경로 길이를 30% 단축시키지만, 단위 거리 추론 능력은 개선하지 않음을 보여준다.
- 이 방법은 모델 재훈련이 필요 없고 계산 비용이 낮지만, 분포 외 명령에서 누락된 훈련 신호를 보완할 수는 없다.
