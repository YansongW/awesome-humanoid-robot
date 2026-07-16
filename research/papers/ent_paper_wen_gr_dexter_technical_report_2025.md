---
$id: ent_paper_wen_gr_dexter_technical_report_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: GR-Dexter Technical Report
  zh: GR-Dexter
  ko: GR-Dexter Technical Report
summary:
  en: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
  zh: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
  ko: GR-Dexter Technical Report (GR-Dexter), is a 2025 large vision-language-action model for robotic manipulation, introduced
    by ByteDance Seed.
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- gr_dexter
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.24210v2.
sources:
- id: src_001
  type: paper
  title: GR-Dexter Technical Report (arXiv)
  url: https://arxiv.org/abs/2512.24210
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: GR-Dexter source
  url: https://doi.org/10.48550/arXiv.2512.24210
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have enabled language-conditioned, long-horizon robot manipulation, but most existing systems are limited to grippers. Scaling VLA policies to bimanual robots with high degree-of-freedom (DoF) dexterous hands remains challenging due to the expanded action space, frequent hand-object occlusions, and the cost of collecting real-robot data. We present GR-Dexter, a holistic hardware-model-data framework for VLA-based generalist manipulation on a bimanual dexterous-hand robot. Our approach combines the design of a compact 21-DoF robotic hand, an intuitive bimanual teleoperation system for real-robot data collection, and a training recipe that leverages teleoperated robot trajectories together with large-scale vision-language and carefully curated cross-embodiment datasets. Across real-world evaluations spanning long-horizon everyday manipulation and generalizable pick-and-place, GR-Dexter achieves strong in-domain performance and improved robustness to unseen objects and unseen instructions. We hope GR-Dexter serves as a practical step toward generalist dexterous-hand robotic manipulation.

## 核心内容
Vision-language-action (VLA) models have enabled language-conditioned, long-horizon robot manipulation, but most existing systems are limited to grippers. Scaling VLA policies to bimanual robots with high degree-of-freedom (DoF) dexterous hands remains challenging due to the expanded action space, frequent hand-object occlusions, and the cost of collecting real-robot data. We present GR-Dexter, a holistic hardware-model-data framework for VLA-based generalist manipulation on a bimanual dexterous-hand robot. Our approach combines the design of a compact 21-DoF robotic hand, an intuitive bimanual teleoperation system for real-robot data collection, and a training recipe that leverages teleoperated robot trajectories together with large-scale vision-language and carefully curated cross-embodiment datasets. Across real-world evaluations spanning long-horizon everyday manipulation and generalizable pick-and-place, GR-Dexter achieves strong in-domain performance and improved robustness to unseen objects and unseen instructions. We hope GR-Dexter serves as a practical step toward generalist dexterous-hand robotic manipulation.

## 参考
- http://arxiv.org/abs/2512.24210v2

## Overview
Vision-language-action (VLA) models have enabled language-conditioned, long-horizon robot manipulation, but most existing systems are limited to grippers. Scaling VLA policies to bimanual robots with high degree-of-freedom (DoF) dexterous hands remains challenging due to the expanded action space, frequent hand-object occlusions, and the cost of collecting real-robot data. We present GR-Dexter, a holistic hardware-model-data framework for VLA-based generalist manipulation on a bimanual dexterous-hand robot. Our approach combines the design of a compact 21-DoF robotic hand, an intuitive bimanual teleoperation system for real-robot data collection, and a training recipe that leverages teleoperated robot trajectories together with large-scale vision-language and carefully curated cross-embodiment datasets. Across real-world evaluations spanning long-horizon everyday manipulation and generalizable pick-and-place, GR-Dexter achieves strong in-domain performance and improved robustness to unseen objects and unseen instructions. We hope GR-Dexter serves as a practical step toward generalist dexterous-hand robotic manipulation.

## Content
Vision-language-action (VLA) models have enabled language-conditioned, long-horizon robot manipulation, but most existing systems are limited to grippers. Scaling VLA policies to bimanual robots with high degree-of-freedom (DoF) dexterous hands remains challenging due to the expanded action space, frequent hand-object occlusions, and the cost of collecting real-robot data. We present GR-Dexter, a holistic hardware-model-data framework for VLA-based generalist manipulation on a bimanual dexterous-hand robot. Our approach combines the design of a compact 21-DoF robotic hand, an intuitive bimanual teleoperation system for real-robot data collection, and a training recipe that leverages teleoperated robot trajectories together with large-scale vision-language and carefully curated cross-embodiment datasets. Across real-world evaluations spanning long-horizon everyday manipulation and generalizable pick-and-place, GR-Dexter achieves strong in-domain performance and improved robustness to unseen objects and unseen instructions. We hope GR-Dexter serves as a practical step toward generalist dexterous-hand robotic manipulation.

## 개요
Vision-language-action (VLA) 모델은 언어 조건에 기반한 장기 로봇 조작을 가능하게 했지만, 대부분의 기존 시스템은 그리퍼(gripper)에 국한되어 있습니다. VLA 정책을 높은 자유도(DoF)를 가진 양손(dexterous hand) 로봇으로 확장하는 것은 확장된 행동 공간, 빈번한 손-물체 가림 현상, 그리고 실제 로봇 데이터 수집 비용으로 인해 여전히 어려운 과제입니다. 우리는 양손(dexterous-hand) 로봇을 위한 VLA 기반 범용 조작을 위한 통합 하드웨어-모델-데이터 프레임워크인 GR-Dexter를 제시합니다. 우리의 접근 방식은 21-DoF의 소형 로봇 손 설계, 실제 로봇 데이터 수집을 위한 직관적인 양손 원격 조작 시스템, 그리고 원격 조작 로봇 궤적과 대규모 시각-언어 데이터 및 신중하게 선별된 교차-체현(cross-embodiment) 데이터셋을 활용하는 훈련 레시피를 결합합니다. 장기 일상 조작과 일반화 가능한 집기-놓기(pick-and-place)를 포괄하는 실제 환경 평가에서 GR-Dexter는 강력한 도메인 내 성능과 보이지 않는 물체 및 지시에 대한 향상된 강건성을 달성했습니다. GR-Dexter가 범용(dexterous-hand) 로봇 조작을 위한 실용적인 단계가 되기를 바랍니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 언어 조건에 기반한 장기 로봇 조작을 가능하게 했지만, 대부분의 기존 시스템은 그리퍼(gripper)에 국한되어 있습니다. VLA 정책을 높은 자유도(DoF)를 가진 양손(dexterous hand) 로봇으로 확장하는 것은 확장된 행동 공간, 빈번한 손-물체 가림 현상, 그리고 실제 로봇 데이터 수집 비용으로 인해 여전히 어려운 과제입니다. 우리는 양손(dexterous-hand) 로봇을 위한 VLA 기반 범용 조작을 위한 통합 하드웨어-모델-데이터 프레임워크인 GR-Dexter를 제시합니다. 우리의 접근 방식은 21-DoF의 소형 로봇 손 설계, 실제 로봇 데이터 수집을 위한 직관적인 양손 원격 조작 시스템, 그리고 원격 조작 로봇 궤적과 대규모 시각-언어 데이터 및 신중하게 선별된 교차-체현(cross-embodiment) 데이터셋을 활용하는 훈련 레시피를 결합합니다. 장기 일상 조작과 일반화 가능한 집기-놓기(pick-and-place)를 포괄하는 실제 환경 평가에서 GR-Dexter는 강력한 도메인 내 성능과 보이지 않는 물체 및 지시에 대한 향상된 강건성을 달성했습니다. GR-Dexter가 범용(dexterous-hand) 로봇 조작을 위한 실용적인 단계가 되기를 바랍니다.
