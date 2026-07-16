---
$id: ent_paper_iterative_closed_loop_motion_s_2026
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
  zh: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
  ko: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control
summary:
  en: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control is a 2026 work on physics-based
    character animation for humanoid robots.
  zh: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control is a 2026 work on physics-based
    character animation for humanoid robots.
  ko: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control is a 2026 work on physics-based
    character animation for humanoid robots.
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- humanoid
- iterative_closed_loop_motion_s
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2602.21599v2.
sources:
- id: src_001
  type: paper
  title: Iterative Closed-Loop Motion Synthesis for Scaling the Capabilities of Humanoid Control (arXiv)
  url: https://arxiv.org/abs/2602.21599
  date: '2026'
  accessed_at: '2026-07-01'
---
## 概述
Physics-based humanoid control relies on training with motion datasets that have diverse data distributions. However, the fixed difficulty distribution of datasets limits the performance ceiling of the trained control policies. Additionally, the method of acquiring high-quality data through professional motion capture systems is constrained by costs, making it difficult to achieve large-scale scalability. To address these issues, we propose a closed-loop automated motion data generation and iterative framework. It can generate high-quality motion data with rich action semantics, including martial arts, dance, combat, sports, gymnastics, and more. Furthermore, our framework enables difficulty iteration of policies and data through physical metrics and objective evaluations, allowing the trained tracker to break through its original difficulty limits. On the PHC single-primitive tracker, using only approximately 1/10 of the AMASS dataset size, the average failure rate on the test set (2201 clips) is reduced by 45% compared to the baseline. Finally, we conduct comprehensive ablation and comparative experiments to highlight the rationality and advantages of our framework.

## 核心内容
Physics-based humanoid control relies on training with motion datasets that have diverse data distributions. However, the fixed difficulty distribution of datasets limits the performance ceiling of the trained control policies. Additionally, the method of acquiring high-quality data through professional motion capture systems is constrained by costs, making it difficult to achieve large-scale scalability. To address these issues, we propose a closed-loop automated motion data generation and iterative framework. It can generate high-quality motion data with rich action semantics, including martial arts, dance, combat, sports, gymnastics, and more. Furthermore, our framework enables difficulty iteration of policies and data through physical metrics and objective evaluations, allowing the trained tracker to break through its original difficulty limits. On the PHC single-primitive tracker, using only approximately 1/10 of the AMASS dataset size, the average failure rate on the test set (2201 clips) is reduced by 45% compared to the baseline. Finally, we conduct comprehensive ablation and comparative experiments to highlight the rationality and advantages of our framework.

## 参考
- http://arxiv.org/abs/2602.21599v2

## Overview
Physics-based humanoid control relies on training with motion datasets that have diverse data distributions. However, the fixed difficulty distribution of datasets limits the performance ceiling of the trained control policies. Additionally, the method of acquiring high-quality data through professional motion capture systems is constrained by costs, making it difficult to achieve large-scale scalability. To address these issues, we propose a closed-loop automated motion data generation and iterative framework. It can generate high-quality motion data with rich action semantics, including martial arts, dance, combat, sports, gymnastics, and more. Furthermore, our framework enables difficulty iteration of policies and data through physical metrics and objective evaluations, allowing the trained tracker to break through its original difficulty limits. On the PHC single-primitive tracker, using only approximately 1/10 of the AMASS dataset size, the average failure rate on the test set (2201 clips) is reduced by 45% compared to the baseline. Finally, we conduct comprehensive ablation and comparative experiments to highlight the rationality and advantages of our framework.

## Content
Physics-based humanoid control relies on training with motion datasets that have diverse data distributions. However, the fixed difficulty distribution of datasets limits the performance ceiling of the trained control policies. Additionally, the method of acquiring high-quality data through professional motion capture systems is constrained by costs, making it difficult to achieve large-scale scalability. To address these issues, we propose a closed-loop automated motion data generation and iterative framework. It can generate high-quality motion data with rich action semantics, including martial arts, dance, combat, sports, gymnastics, and more. Furthermore, our framework enables difficulty iteration of policies and data through physical metrics and objective evaluations, allowing the trained tracker to break through its original difficulty limits. On the PHC single-primitive tracker, using only approximately 1/10 of the AMASS dataset size, the average failure rate on the test set (2201 clips) is reduced by 45% compared to the baseline. Finally, we conduct comprehensive ablation and comparative experiments to highlight the rationality and advantages of our framework.

## 개요
물리 기반 휴머노이드 제어는 다양한 데이터 분포를 가진 모션 데이터셋을 활용한 훈련에 의존합니다. 그러나 데이터셋의 고정된 난이도 분포는 훈련된 제어 정책의 성능 상한을 제한합니다. 또한 전문 모션 캡처 시스템을 통해 고품질 데이터를 획득하는 방법은 비용 제약으로 인해 대규모 확장이 어렵습니다. 이러한 문제를 해결하기 위해, 우리는 폐루프 자동 모션 데이터 생성 및 반복 프레임워크를 제안합니다. 이 프레임워크는 무술, 춤, 격투, 스포츠, 체조 등 풍부한 동작 의미를 가진 고품질 모션 데이터를 생성할 수 있습니다. 또한 물리적 지표와 객관적 평가를 통해 정책과 데이터의 난이도 반복을 가능하게 하여, 훈련된 트래커가 원래의 난이도 한계를 돌파할 수 있도록 합니다. PHC 단일 프리미티브 트래커에서 AMASS 데이터셋 크기의 약 1/10만 사용하여, 테스트 세트(2201 클립)에서 평균 실패율이 기준선 대비 45% 감소했습니다. 마지막으로, 포괄적인 절제 및 비교 실험을 통해 프레임워크의 합리성과 장점을 강조합니다.

## 핵심 내용
물리 기반 휴머노이드 제어는 다양한 데이터 분포를 가진 모션 데이터셋을 활용한 훈련에 의존합니다. 그러나 데이터셋의 고정된 난이도 분포는 훈련된 제어 정책의 성능 상한을 제한합니다. 또한 전문 모션 캡처 시스템을 통해 고품질 데이터를 획득하는 방법은 비용 제약으로 인해 대규모 확장이 어렵습니다. 이러한 문제를 해결하기 위해, 우리는 폐루프 자동 모션 데이터 생성 및 반복 프레임워크를 제안합니다. 이 프레임워크는 무술, 춤, 격투, 스포츠, 체조 등 풍부한 동작 의미를 가진 고품질 모션 데이터를 생성할 수 있습니다. 또한 물리적 지표와 객관적 평가를 통해 정책과 데이터의 난이도 반복을 가능하게 하여, 훈련된 트래커가 원래의 난이도 한계를 돌파할 수 있도록 합니다. PHC 단일 프리미티브 트래커에서 AMASS 데이터셋 크기의 약 1/10만 사용하여, 테스트 세트(2201 클립)에서 평균 실패율이 기준선 대비 45% 감소했습니다. 마지막으로, 포괄적인 절제 및 비교 실험을 통해 프레임워크의 합리성과 장점을 강조합니다.
