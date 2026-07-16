---
$id: ent_paper_ng_endovla_dual_phase_vision_lang_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy'
  zh: EndoVLA
  ko: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy'
summary:
  en: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy (EndoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Technical University of Munich, and
    published at CoRL25.'
  zh: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy (EndoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Technical University of Munich, and
    published at CoRL25.'
  ko: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy (EndoVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by The Chinese University of Hong Kong, Technical University of Munich, and
    published at CoRL25.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- endovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2505.15206v1.
sources:
- id: src_001
  type: paper
  title: 'EndoVLA: Dual-Phase Vision-Language-Action Model for Autonomous Tracking in Endoscopy (arXiv)'
  url: https://arxiv.org/abs/2505.15206
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: EndoVLA source
  url: https://doi.org/10.48550/arXiv.2505.15206
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
In endoscopic procedures, autonomous tracking of abnormal regions and following circumferential cutting markers can significantly reduce the cognitive burden on endoscopists. However, conventional model-based pipelines are fragile for each component (e.g., detection, motion planning) requires manual tuning and struggles to incorporate high-level endoscopic intent, leading to poor generalization across diverse scenes. Vision-Language-Action (VLA) models, which integrate visual perception, language grounding, and motion planning within an end-to-end framework, offer a promising alternative by semantically adapting to surgeon prompts without manual recalibration. Despite their potential, applying VLA models to robotic endoscopy presents unique challenges due to the complex and dynamic anatomical environments of the gastrointestinal (GI) tract. To address this, we introduce EndoVLA, designed specifically for continuum robots in GI interventions. Given endoscopic images and surgeon-issued tracking prompts, EndoVLA performs three core tasks: (1) polyp tracking, (2) delineation and following of abnormal mucosal regions, and (3) adherence to circular markers during circumferential cutting. To tackle data scarcity and domain shifts, we propose a dual-phase strategy comprising supervised fine-tuning on our EndoVLA-Motion dataset and reinforcement fine-tuning with task-aware rewards. Our approach significantly improves tracking performance in endoscopy and enables zero-shot generalization in diverse scenes and complex sequential tasks.

## 核心内容
In endoscopic procedures, autonomous tracking of abnormal regions and following circumferential cutting markers can significantly reduce the cognitive burden on endoscopists. However, conventional model-based pipelines are fragile for each component (e.g., detection, motion planning) requires manual tuning and struggles to incorporate high-level endoscopic intent, leading to poor generalization across diverse scenes. Vision-Language-Action (VLA) models, which integrate visual perception, language grounding, and motion planning within an end-to-end framework, offer a promising alternative by semantically adapting to surgeon prompts without manual recalibration. Despite their potential, applying VLA models to robotic endoscopy presents unique challenges due to the complex and dynamic anatomical environments of the gastrointestinal (GI) tract. To address this, we introduce EndoVLA, designed specifically for continuum robots in GI interventions. Given endoscopic images and surgeon-issued tracking prompts, EndoVLA performs three core tasks: (1) polyp tracking, (2) delineation and following of abnormal mucosal regions, and (3) adherence to circular markers during circumferential cutting. To tackle data scarcity and domain shifts, we propose a dual-phase strategy comprising supervised fine-tuning on our EndoVLA-Motion dataset and reinforcement fine-tuning with task-aware rewards. Our approach significantly improves tracking performance in endoscopy and enables zero-shot generalization in diverse scenes and complex sequential tasks.

## 参考
- http://arxiv.org/abs/2505.15206v1

## Overview
In endoscopic procedures, autonomous tracking of abnormal regions and following circumferential cutting markers can significantly reduce the cognitive burden on endoscopists. However, conventional model-based pipelines are fragile for each component (e.g., detection, motion planning) requires manual tuning and struggles to incorporate high-level endoscopic intent, leading to poor generalization across diverse scenes. Vision-Language-Action (VLA) models, which integrate visual perception, language grounding, and motion planning within an end-to-end framework, offer a promising alternative by semantically adapting to surgeon prompts without manual recalibration. Despite their potential, applying VLA models to robotic endoscopy presents unique challenges due to the complex and dynamic anatomical environments of the gastrointestinal (GI) tract. To address this, we introduce EndoVLA, designed specifically for continuum robots in GI interventions. Given endoscopic images and surgeon-issued tracking prompts, EndoVLA performs three core tasks: (1) polyp tracking, (2) delineation and following of abnormal mucosal regions, and (3) adherence to circular markers during circumferential cutting. To tackle data scarcity and domain shifts, we propose a dual-phase strategy comprising supervised fine-tuning on our EndoVLA-Motion dataset and reinforcement fine-tuning with task-aware rewards. Our approach significantly improves tracking performance in endoscopy and enables zero-shot generalization in diverse scenes and complex sequential tasks.

## Content
In endoscopic procedures, autonomous tracking of abnormal regions and following circumferential cutting markers can significantly reduce the cognitive burden on endoscopists. However, conventional model-based pipelines are fragile for each component (e.g., detection, motion planning) requires manual tuning and struggles to incorporate high-level endoscopic intent, leading to poor generalization across diverse scenes. Vision-Language-Action (VLA) models, which integrate visual perception, language grounding, and motion planning within an end-to-end framework, offer a promising alternative by semantically adapting to surgeon prompts without manual recalibration. Despite their potential, applying VLA models to robotic endoscopy presents unique challenges due to the complex and dynamic anatomical environments of the gastrointestinal (GI) tract. To address this, we introduce EndoVLA, designed specifically for continuum robots in GI interventions. Given endoscopic images and surgeon-issued tracking prompts, EndoVLA performs three core tasks: (1) polyp tracking, (2) delineation and following of abnormal mucosal regions, and (3) adherence to circular markers during circumferential cutting. To tackle data scarcity and domain shifts, we propose a dual-phase strategy comprising supervised fine-tuning on our EndoVLA-Motion dataset and reinforcement fine-tuning with task-aware rewards. Our approach significantly improves tracking performance in endoscopy and enables zero-shot generalization in diverse scenes and complex sequential tasks.

## 개요
내시경 시술에서 비정상 영역의 자율 추적 및 원형 절단 마커 추종은 내시경 의사의 인지 부담을 크게 줄일 수 있습니다. 그러나 기존의 모델 기반 파이프라인은 각 구성 요소(예: 탐지, 동작 계획)에 수동 조정이 필요하고 고수준의 내시경 의도를 통합하기 어려워 다양한 장면에서 일반화 성능이 낮습니다. 시각 인식, 언어 기반 추론, 동작 계획을 종단 간 프레임워크에 통합하는 Vision-Language-Action (VLA) 모델은 수동 재조정 없이 외과의 프롬프트에 의미적으로 적응할 수 있는 유망한 대안을 제공합니다. 그러나 VLA 모델을 로봇 내시경에 적용하는 것은 위장관(GI)의 복잡하고 동적인 해부학적 환경으로 인해 독특한 도전 과제를 제시합니다. 이를 해결하기 위해 우리는 GI 중재에서 연속체 로봇을 위해 특별히 설계된 EndoVLA를 소개합니다. 내시경 이미지와 외과의가 발행한 추적 프롬프트가 주어지면 EndoVLA는 세 가지 핵심 작업을 수행합니다: (1) 폴립 추적, (2) 비정상 점막 영역의 경계 설정 및 추종, (3) 원형 절단 중 원형 마커 준수. 데이터 부족 및 도메인 변화를 해결하기 위해 우리는 EndoVLA-Motion 데이터셋에서의 지도 미세 조정과 작업 인식 보상을 통한 강화 미세 조정으로 구성된 이중 단계 전략을 제안합니다. 우리의 접근 방식은 내시경에서 추적 성능을 크게 향상시키고 다양한 장면과 복잡한 순차 작업에서 제로샷 일반화를 가능하게 합니다.

## 핵심 내용
내시경 시술에서 비정상 영역의 자율 추적 및 원형 절단 마커 추종은 내시경 의사의 인지 부담을 크게 줄일 수 있습니다. 그러나 기존의 모델 기반 파이프라인은 각 구성 요소(예: 탐지, 동작 계획)에 수동 조정이 필요하고 고수준의 내시경 의도를 통합하기 어려워 다양한 장면에서 일반화 성능이 낮습니다. 시각 인식, 언어 기반 추론, 동작 계획을 종단 간 프레임워크에 통합하는 Vision-Language-Action (VLA) 모델은 수동 재조정 없이 외과의 프롬프트에 의미적으로 적응할 수 있는 유망한 대안을 제공합니다. 그러나 VLA 모델을 로봇 내시경에 적용하는 것은 위장관(GI)의 복잡하고 동적인 해부학적 환경으로 인해 독특한 도전 과제를 제시합니다. 이를 해결하기 위해 우리는 GI 중재에서 연속체 로봇을 위해 특별히 설계된 EndoVLA를 소개합니다. 내시경 이미지와 외과의가 발행한 추적 프롬프트가 주어지면 EndoVLA는 세 가지 핵심 작업을 수행합니다: (1) 폴립 추적, (2) 비정상 점막 영역의 경계 설정 및 추종, (3) 원형 절단 중 원형 마커 준수. 데이터 부족 및 도메인 변화를 해결하기 위해 우리는 EndoVLA-Motion 데이터셋에서의 지도 미세 조정과 작업 인식 보상을 통한 강화 미세 조정으로 구성된 이중 단계 전략을 제안합니다. 우리의 접근 방식은 내시경에서 추적 성능을 크게 향상시키고 다양한 장면과 복잡한 순차 작업에서 제로샷 일반화를 가능하게 합니다.
