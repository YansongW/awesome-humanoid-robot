---
$id: ent_paper_farm_frame_accelerated_augment_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control'
  zh: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control'
  ko: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control'
summary:
  en: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control
    is a 2025 work on physics-based character animation for humanoid robots.'
  zh: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control
    is a 2025 work on physics-based character animation for humanoid robots.'
  ko: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control
    is a 2025 work on physics-based character animation for humanoid robots.'
domains:
- 07_ai_models_algorithms
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- character_animation
- farm
- humanoid
- physics_based
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.19926v1.
sources:
- id: src_001
  type: paper
  title: 'FARM: Frame-Accelerated Augmentation and Residual Mixture-of-Experts for Physics-Based High-Dynamic Humanoid Control
    (arXiv)'
  url: https://arxiv.org/abs/2508.19926
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Unified physics-based humanoid controllers are pivotal for robotics and character animation, yet models that excel on gentle, everyday motions still stumble on explosive actions, hampering real-world deployment. We bridge this gap with FARM (Frame-Accelerated Augmentation and Residual Mixture-of-Experts), an end-to-end framework composed of frame-accelerated augmentation, a robust base controller, and a residual mixture-of-experts (MoE). Frame-accelerated augmentation exposes the model to high-velocity pose changes by widening inter-frame gaps. The base controller reliably tracks everyday low-dynamic motions, while the residual MoE adaptively allocates additional network capacity to handle challenging high-dynamic actions, significantly enhancing tracking accuracy. In the absence of a public benchmark, we curate the High-Dynamic Humanoid Motion (HDHM) dataset, comprising 3593 physically plausible clips. On HDHM, FARM reduces the tracking failure rate by 42.8\% and lowers global mean per-joint position error by 14.6\% relative to the baseline, while preserving near-perfect accuracy on low-dynamic motions. These results establish FARM as a new baseline for high-dynamic humanoid control and introduce the first open benchmark dedicated to this challenge. The code and dataset will be released at https://github.com/Colin-Jing/FARM.

## 核心内容
Unified physics-based humanoid controllers are pivotal for robotics and character animation, yet models that excel on gentle, everyday motions still stumble on explosive actions, hampering real-world deployment. We bridge this gap with FARM (Frame-Accelerated Augmentation and Residual Mixture-of-Experts), an end-to-end framework composed of frame-accelerated augmentation, a robust base controller, and a residual mixture-of-experts (MoE). Frame-accelerated augmentation exposes the model to high-velocity pose changes by widening inter-frame gaps. The base controller reliably tracks everyday low-dynamic motions, while the residual MoE adaptively allocates additional network capacity to handle challenging high-dynamic actions, significantly enhancing tracking accuracy. In the absence of a public benchmark, we curate the High-Dynamic Humanoid Motion (HDHM) dataset, comprising 3593 physically plausible clips. On HDHM, FARM reduces the tracking failure rate by 42.8\% and lowers global mean per-joint position error by 14.6\% relative to the baseline, while preserving near-perfect accuracy on low-dynamic motions. These results establish FARM as a new baseline for high-dynamic humanoid control and introduce the first open benchmark dedicated to this challenge. The code and dataset will be released at https://github.com/Colin-Jing/FARM.

## 参考
- http://arxiv.org/abs/2508.19926v1

## Overview
Unified physics-based humanoid controllers are pivotal for robotics and character animation, yet models that excel on gentle, everyday motions still stumble on explosive actions, hampering real-world deployment. We bridge this gap with FARM (Frame-Accelerated Augmentation and Residual Mixture-of-Experts), an end-to-end framework composed of frame-accelerated augmentation, a robust base controller, and a residual mixture-of-experts (MoE). Frame-accelerated augmentation exposes the model to high-velocity pose changes by widening inter-frame gaps. The base controller reliably tracks everyday low-dynamic motions, while the residual MoE adaptively allocates additional network capacity to handle challenging high-dynamic actions, significantly enhancing tracking accuracy. In the absence of a public benchmark, we curate the High-Dynamic Humanoid Motion (HDHM) dataset, comprising 3593 physically plausible clips. On HDHM, FARM reduces the tracking failure rate by 42.8\% and lowers global mean per-joint position error by 14.6\% relative to the baseline, while preserving near-perfect accuracy on low-dynamic motions. These results establish FARM as a new baseline for high-dynamic humanoid control and introduce the first open benchmark dedicated to this challenge. The code and dataset will be released at https://github.com/Colin-Jing/FARM.

## Content
Unified physics-based humanoid controllers are pivotal for robotics and character animation, yet models that excel on gentle, everyday motions still stumble on explosive actions, hampering real-world deployment. We bridge this gap with FARM (Frame-Accelerated Augmentation and Residual Mixture-of-Experts), an end-to-end framework composed of frame-accelerated augmentation, a robust base controller, and a residual mixture-of-experts (MoE). Frame-accelerated augmentation exposes the model to high-velocity pose changes by widening inter-frame gaps. The base controller reliably tracks everyday low-dynamic motions, while the residual MoE adaptively allocates additional network capacity to handle challenging high-dynamic actions, significantly enhancing tracking accuracy. In the absence of a public benchmark, we curate the High-Dynamic Humanoid Motion (HDHM) dataset, comprising 3593 physically plausible clips. On HDHM, FARM reduces the tracking failure rate by 42.8\% and lowers global mean per-joint position error by 14.6\% relative to the baseline, while preserving near-perfect accuracy on low-dynamic motions. These results establish FARM as a new baseline for high-dynamic humanoid control and introduce the first open benchmark dedicated to this challenge. The code and dataset will be released at https://github.com/Colin-Jing/FARM.

## 개요
통합 물리 기반 휴머노이드 제어기는 로봇공학과 캐릭터 애니메이션에서 핵심적이지만, 부드러운 일상 동작에 뛰어난 모델도 폭발적인 동작에서는 여전히 어려움을 겪어 실제 배치를 저해합니다. 우리는 프레임 가속 증강(Frame-Accelerated Augmentation), 강력한 기본 제어기(Base Controller), 그리고 잔차 전문가 혼합(Residual Mixture-of-Experts, MoE)으로 구성된 종단 간 프레임워크인 FARM(Frame-Accelerated Augmentation and Residual Mixture-of-Experts)으로 이 격차를 해소합니다. 프레임 가속 증강은 프레임 간 간격을 넓혀 모델을 고속 자세 변화에 노출시킵니다. 기본 제어기는 일상적인 저동적 동작을 안정적으로 추적하는 반면, 잔차 MoE는 적응적으로 추가 네트워크 용량을 할당하여 까다로운 고동적 동작을 처리함으로써 추적 정확도를 크게 향상시킵니다. 공개 벤치마크가 없는 상황에서 우리는 3593개의 물리적으로 타당한 클립으로 구성된 HDHM(High-Dynamic Humanoid Motion) 데이터셋을 구축했습니다. HDHM에서 FARM은 기준선 대비 추적 실패율을 42.8% 감소시키고 전역 평균 관절당 위치 오차를 14.6% 낮추면서 저동적 동작에서는 거의 완벽한 정확도를 유지합니다. 이러한 결과는 FARM을 고동적 휴머노이드 제어를 위한 새로운 기준선으로 확립하고, 이 과제에 전념하는 최초의 공개 벤치마크를 소개합니다. 코드와 데이터셋은 https://github.com/Colin-Jing/FARM에서 공개될 예정입니다.

## 핵심 내용
통합 물리 기반 휴머노이드 제어기는 로봇공학과 캐릭터 애니메이션에서 핵심적이지만, 부드러운 일상 동작에 뛰어난 모델도 폭발적인 동작에서는 여전히 어려움을 겪어 실제 배치를 저해합니다. 우리는 프레임 가속 증강(Frame-Accelerated Augmentation), 강력한 기본 제어기(Base Controller), 그리고 잔차 전문가 혼합(Residual Mixture-of-Experts, MoE)으로 구성된 종단 간 프레임워크인 FARM(Frame-Accelerated Augmentation and Residual Mixture-of-Experts)으로 이 격차를 해소합니다. 프레임 가속 증강은 프레임 간 간격을 넓혀 모델을 고속 자세 변화에 노출시킵니다. 기본 제어기는 일상적인 저동적 동작을 안정적으로 추적하는 반면, 잔차 MoE는 적응적으로 추가 네트워크 용량을 할당하여 까다로운 고동적 동작을 처리함으로써 추적 정확도를 크게 향상시킵니다. 공개 벤치마크가 없는 상황에서 우리는 3593개의 물리적으로 타당한 클립으로 구성된 HDHM(High-Dynamic Humanoid Motion) 데이터셋을 구축했습니다. HDHM에서 FARM은 기준선 대비 추적 실패율을 42.8% 감소시키고 전역 평균 관절당 위치 오차를 14.6% 낮추면서 저동적 동작에서는 거의 완벽한 정확도를 유지합니다. 이러한 결과는 FARM을 고동적 휴머노이드 제어를 위한 새로운 기준선으로 확립하고, 이 과제에 전념하는 최초의 공개 벤치마크를 소개합니다. 코드와 데이터셋은 https://github.com/Colin-Jing/FARM에서 공개될 예정입니다.
