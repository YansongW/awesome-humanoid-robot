---
$id: ent_paper_one_shot_humanoid_whole_body_m_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: One-shot Humanoid Whole-body Motion Learning
  zh: One-shot Humanoid Whole-body Motion Learning
  ko: One-shot Humanoid Whole-body Motion Learning
summary:
  en: One-shot Humanoid Whole-body Motion Learning is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.
  zh: One-shot Humanoid Whole-body Motion Learning is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.
  ko: One-shot Humanoid Whole-body Motion Learning is a 2025 work on loco-manipulation and whole-body-control for humanoid
    robots.
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
- loco_manipulation
- one_shot_humanoid_whole_body_m
- whole_body_control
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.25241v2.
sources:
- id: src_001
  type: paper
  title: One-shot Humanoid Whole-body Motion Learning (arXiv)
  url: https://arxiv.org/abs/2510.25241
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Whole-body humanoid motion represents a fundamental challenge in robotics, requiring balance, coordination, and adaptability to enable human-like behaviors. However, existing methods typically require multiple training samples per motion, rendering the collection of high-quality human motion datasets both labor-intensive and costly. To address this, we propose a data-efficient adaptation approach that learns a new humanoid motion from a single non-walking target sample together with auxiliary walking motions and a walking-trained base model. The core idea lies in leveraging order-preserving optimal transport to compute distances between walking and non-walking sequences, followed by interpolation along geodesics to generate new intermediate pose skeletons, which are then optimized for collision-free configurations and retargeted to the humanoid before integration into a simulated environment for policy adaptation via reinforcement learning. Experimental evaluations on the CMU MoCap dataset demonstrate that our method consistently outperforms baselines, achieving superior performance across metrics. Our code is available at: https://github.com/hhuang-code/One-shot-WBM.

## 核心内容
Whole-body humanoid motion represents a fundamental challenge in robotics, requiring balance, coordination, and adaptability to enable human-like behaviors. However, existing methods typically require multiple training samples per motion, rendering the collection of high-quality human motion datasets both labor-intensive and costly. To address this, we propose a data-efficient adaptation approach that learns a new humanoid motion from a single non-walking target sample together with auxiliary walking motions and a walking-trained base model. The core idea lies in leveraging order-preserving optimal transport to compute distances between walking and non-walking sequences, followed by interpolation along geodesics to generate new intermediate pose skeletons, which are then optimized for collision-free configurations and retargeted to the humanoid before integration into a simulated environment for policy adaptation via reinforcement learning. Experimental evaluations on the CMU MoCap dataset demonstrate that our method consistently outperforms baselines, achieving superior performance across metrics. Our code is available at: https://github.com/hhuang-code/One-shot-WBM.

## 参考
- http://arxiv.org/abs/2510.25241v2

## Overview
Whole-body humanoid motion represents a fundamental challenge in robotics, requiring balance, coordination, and adaptability to enable human-like behaviors. However, existing methods typically require multiple training samples per motion, rendering the collection of high-quality human motion datasets both labor-intensive and costly. To address this, we propose a data-efficient adaptation approach that learns a new humanoid motion from a single non-walking target sample together with auxiliary walking motions and a walking-trained base model. The core idea lies in leveraging order-preserving optimal transport to compute distances between walking and non-walking sequences, followed by interpolation along geodesics to generate new intermediate pose skeletons, which are then optimized for collision-free configurations and retargeted to the humanoid before integration into a simulated environment for policy adaptation via reinforcement learning. Experimental evaluations on the CMU MoCap dataset demonstrate that our method consistently outperforms baselines, achieving superior performance across metrics. Our code is available at: https://github.com/hhuang-code/One-shot-WBM.

## Content
Whole-body humanoid motion represents a fundamental challenge in robotics, requiring balance, coordination, and adaptability to enable human-like behaviors. However, existing methods typically require multiple training samples per motion, rendering the collection of high-quality human motion datasets both labor-intensive and costly. To address this, we propose a data-efficient adaptation approach that learns a new humanoid motion from a single non-walking target sample together with auxiliary walking motions and a walking-trained base model. The core idea lies in leveraging order-preserving optimal transport to compute distances between walking and non-walking sequences, followed by interpolation along geodesics to generate new intermediate pose skeletons, which are then optimized for collision-free configurations and retargeted to the humanoid before integration into a simulated environment for policy adaptation via reinforcement learning. Experimental evaluations on the CMU MoCap dataset demonstrate that our method consistently outperforms baselines, achieving superior performance across metrics. Our code is available at: https://github.com/hhuang-code/One-shot-WBM.

## 개요
전신 휴머노이드 동작은 로봇 공학에서 근본적인 도전 과제로, 인간과 같은 행동을 구현하기 위해 균형, 협응 및 적응성을 필요로 합니다. 그러나 기존 방법은 일반적으로 동작당 여러 개의 훈련 샘플을 필요로 하여, 고품질 인간 동작 데이터셋 수집이 노동 집약적이고 비용이 많이 드는 문제가 있습니다. 이를 해결하기 위해, 우리는 보조 걷기 동작 및 걷기 훈련된 기본 모델과 함께 단일 비걷기 대상 샘플로부터 새로운 휴머노이드 동작을 학습하는 데이터 효율적인 적응 접근법을 제안합니다. 핵심 아이디어는 순서 보존 최적 수송을 활용하여 걷기 및 비걷기 시퀀스 간의 거리를 계산한 후, 측지선을 따라 보간하여 새로운 중간 포즈 스켈레톤을 생성하는 데 있습니다. 그런 다음 충돌 없는 구성을 위해 최적화되고 휴머노이드에 리타겟팅된 후, 강화 학습을 통한 정책 적응을 위해 시뮬레이션 환경에 통합됩니다. CMU MoCap 데이터셋에 대한 실험 평가는 우리의 방법이 기준선을 일관되게 능가하며 모든 지표에서 우수한 성능을 달성함을 보여줍니다. 코드는 https://github.com/hhuang-code/One-shot-WBM에서 확인할 수 있습니다.

## 핵심 내용
전신 휴머노이드 동작은 로봇 공학에서 근본적인 도전 과제로, 인간과 같은 행동을 구현하기 위해 균형, 협응 및 적응성을 필요로 합니다. 그러나 기존 방법은 일반적으로 동작당 여러 개의 훈련 샘플을 필요로 하여, 고품질 인간 동작 데이터셋 수집이 노동 집약적이고 비용이 많이 드는 문제가 있습니다. 이를 해결하기 위해, 우리는 보조 걷기 동작 및 걷기 훈련된 기본 모델과 함께 단일 비걷기 대상 샘플로부터 새로운 휴머노이드 동작을 학습하는 데이터 효율적인 적응 접근법을 제안합니다. 핵심 아이디어는 순서 보존 최적 수송을 활용하여 걷기 및 비걷기 시퀀스 간의 거리를 계산한 후, 측지선을 따라 보간하여 새로운 중간 포즈 스켈레톤을 생성하는 데 있습니다. 그런 다음 충돌 없는 구성을 위해 최적화되고 휴머노이드에 리타겟팅된 후, 강화 학습을 통한 정책 적응을 위해 시뮬레이션 환경에 통합됩니다. CMU MoCap 데이터셋에 대한 실험 평가는 우리의 방법이 기준선을 일관되게 능가하며 모든 지표에서 우수한 성능을 달성함을 보여줍니다. 코드는 https://github.com/hhuang-code/One-shot-WBM에서 확인할 수 있습니다.
