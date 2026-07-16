---
$id: ent_paper_goyal_rvt_robotic_view_transformer_f_2023
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RVT: Robotic View Transformer for 3D Object Manipulation'
  zh: RVT
  ko: 'RVT: Robotic View Transformer for 3D Object Manipulation'
summary:
  en: 'RVT: Robotic View Transformer for 3D Object Manipulation (RVT), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, and published at CoRL 2023.'
  zh: 'RVT: Robotic View Transformer for 3D Object Manipulation (RVT), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, and published at CoRL 2023.'
  ko: 'RVT: Robotic View Transformer for 3D Object Manipulation (RVT), is a 2023 generalized vision-language-action model
    for robotic manipulation, introduced by NVIDIA, and published at CoRL 2023.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- generalist_policy
- robotic_manipulation
- rvt
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2306.14896v1.
sources:
- id: src_001
  type: paper
  title: RVT source
  url: https://proceedings.mlr.press/v229/goyal23a.html
  date: '2023'
  accessed_at: '2026-07-01'
---
## 概述
For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability. In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate. Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace. In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing state-of-the-art method (PerAct). It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct. Further, RVT can perform a variety of manipulation tasks in the real world with just a few ($\sim$10) demonstrations per task. Visual results, code, and trained model are provided at https://robotic-view-transformer.github.io/.

## 核心内容
For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability. In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate. Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace. In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing state-of-the-art method (PerAct). It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct. Further, RVT can perform a variety of manipulation tasks in the real world with just a few ($\sim$10) demonstrations per task. Visual results, code, and trained model are provided at https://robotic-view-transformer.github.io/.

## 参考
- http://arxiv.org/abs/2306.14896v1

## Overview
For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability. In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate. Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace. In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing state-of-the-art method (PerAct). It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct. Further, RVT can perform a variety of manipulation tasks in the real world with just a few ($\sim$10) demonstrations per task. Visual results, code, and trained model are provided at https://robotic-view-transformer.github.io/.

## Content
For 3D object manipulation, methods that build an explicit 3D representation perform better than those relying only on camera images. But using explicit 3D representations like voxels comes at large computing cost, adversely affecting scalability. In this work, we propose RVT, a multi-view transformer for 3D manipulation that is both scalable and accurate. Some key features of RVT are an attention mechanism to aggregate information across views and re-rendering of the camera input from virtual views around the robot workspace. In simulations, we find that a single RVT model works well across 18 RLBench tasks with 249 task variations, achieving 26% higher relative success than the existing state-of-the-art method (PerAct). It also trains 36X faster than PerAct for achieving the same performance and achieves 2.3X the inference speed of PerAct. Further, RVT can perform a variety of manipulation tasks in the real world with just a few ($\sim$10) demonstrations per task. Visual results, code, and trained model are provided at https://robotic-view-transformer.github.io/.

## 개요
3D 객체 조작을 위해 명시적 3D 표현을 구축하는 방법은 카메라 이미지만 사용하는 방법보다 더 나은 성능을 보입니다. 하지만 복셀과 같은 명시적 3D 표현을 사용하면 큰 계산 비용이 발생하여 확장성에 부정적인 영향을 미칩니다. 본 연구에서는 확장성과 정확성을 모두 갖춘 3D 조작용 멀티뷰 트랜스포머인 RVT를 제안합니다. RVT의 주요 특징으로는 뷰 간 정보를 통합하는 어텐션 메커니즘과 로봇 작업 공간 주변의 가상 뷰에서 카메라 입력을 재렌더링하는 기능이 있습니다. 시뮬레이션에서 단일 RVT 모델이 249개의 작업 변형을 포함한 18개의 RLBench 작업에서 잘 작동하며, 기존 최첨단 방법(PerAct)보다 상대적 성공률이 26% 더 높은 것을 확인했습니다. 또한 동일한 성능을 달성하는 데 PerAct보다 36배 빠르게 훈련되며, PerAct의 2.3배 추론 속도를 보입니다. 더 나아가 RVT는 실제 세계에서 작업당 몇 개(약 10개)의 시연만으로 다양한 조작 작업을 수행할 수 있습니다. 시각적 결과, 코드 및 훈련된 모델은 https://robotic-view-transformer.github.io/에서 제공됩니다.

## 핵심 내용
3D 객체 조작을 위해 명시적 3D 표현을 구축하는 방법은 카메라 이미지만 사용하는 방법보다 더 나은 성능을 보입니다. 하지만 복셀과 같은 명시적 3D 표현을 사용하면 큰 계산 비용이 발생하여 확장성에 부정적인 영향을 미칩니다. 본 연구에서는 확장성과 정확성을 모두 갖춘 3D 조작용 멀티뷰 트랜스포머인 RVT를 제안합니다. RVT의 주요 특징으로는 뷰 간 정보를 통합하는 어텐션 메커니즘과 로봇 작업 공간 주변의 가상 뷰에서 카메라 입력을 재렌더링하는 기능이 있습니다. 시뮬레이션에서 단일 RVT 모델이 249개의 작업 변형을 포함한 18개의 RLBench 작업에서 잘 작동하며, 기존 최첨단 방법(PerAct)보다 상대적 성공률이 26% 더 높은 것을 확인했습니다. 또한 동일한 성능을 달성하는 데 PerAct보다 36배 빠르게 훈련되며, PerAct의 2.3배 추론 속도를 보입니다. 더 나아가 RVT는 실제 세계에서 작업당 몇 개(약 10개)의 시연만으로 다양한 조작 작업을 수행할 수 있습니다. 시각적 결과, 코드 및 훈련된 모델은 https://robotic-view-transformer.github.io/에서 제공됩니다.
