---
$id: ent_paper_wang_monodream_monocular_vision_lan_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming'
  zh: MonoDream
  ko: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming'
summary:
  en: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming (MonoDream), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Renmin University of China, Innovation Center for Future Blockchain and
    Privacy Computing, Beijing, Horizon Robotics, National University of Singapore.'
  zh: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming (MonoDream), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Renmin University of China, Innovation Center for Future Blockchain and
    Privacy Computing, Beijing, Horizon Robotics, National University of Singapore.'
  ko: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming (MonoDream), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by Renmin University of China, Innovation Center for Future Blockchain and
    Privacy Computing, Beijing, Horizon Robotics, National University of Singapore.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- large_vla_model
- monodream
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2508.02549v4.
sources:
- id: src_001
  type: paper
  title: 'MonoDream: Monocular Vision-Language Navigation with Panoramic Dreaming (arXiv)'
  url: https://arxiv.org/abs/2508.02549
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: MonoDream source
  url: https://doi.org/10.48550/arXiv.2508.02549
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language Navigation (VLN) tasks often leverage panoramic RGB and depth inputs to provide rich spatial cues for action planning, but these sensors can be costly or less accessible in real-world deployments. Recent approaches based on Vision-Language Action (VLA) models achieve strong results with monocular input, yet they still lag behind methods using panoramic RGB-D information. We present MonoDream, a lightweight VLA framework that enables monocular agents to learn a Unified Navigation Representation (UNR). This shared feature representation jointly aligns navigation-relevant visual semantics (e.g., global layout, depth, and future cues) and language-grounded action intent, enabling more reliable action prediction. MonoDream further introduces Latent Panoramic Dreaming (LPD) tasks to supervise the UNR, which train the model to predict latent features of panoramic RGB and depth observations at both current and future steps based on only monocular input. Experiments on multiple VLN benchmarks show that MonoDream consistently improves monocular navigation performance and significantly narrows the gap with panoramic-based agents.

## 核心内容
Vision-Language Navigation (VLN) tasks often leverage panoramic RGB and depth inputs to provide rich spatial cues for action planning, but these sensors can be costly or less accessible in real-world deployments. Recent approaches based on Vision-Language Action (VLA) models achieve strong results with monocular input, yet they still lag behind methods using panoramic RGB-D information. We present MonoDream, a lightweight VLA framework that enables monocular agents to learn a Unified Navigation Representation (UNR). This shared feature representation jointly aligns navigation-relevant visual semantics (e.g., global layout, depth, and future cues) and language-grounded action intent, enabling more reliable action prediction. MonoDream further introduces Latent Panoramic Dreaming (LPD) tasks to supervise the UNR, which train the model to predict latent features of panoramic RGB and depth observations at both current and future steps based on only monocular input. Experiments on multiple VLN benchmarks show that MonoDream consistently improves monocular navigation performance and significantly narrows the gap with panoramic-based agents.

## 参考
- http://arxiv.org/abs/2508.02549v4

## Overview
Vision-Language Navigation (VLN) tasks often leverage panoramic RGB and depth inputs to provide rich spatial cues for action planning, but these sensors can be costly or less accessible in real-world deployments. Recent approaches based on Vision-Language Action (VLA) models achieve strong results with monocular input, yet they still lag behind methods using panoramic RGB-D information. We present MonoDream, a lightweight VLA framework that enables monocular agents to learn a Unified Navigation Representation (UNR). This shared feature representation jointly aligns navigation-relevant visual semantics (e.g., global layout, depth, and future cues) and language-grounded action intent, enabling more reliable action prediction. MonoDream further introduces Latent Panoramic Dreaming (LPD) tasks to supervise the UNR, which train the model to predict latent features of panoramic RGB and depth observations at both current and future steps based on only monocular input. Experiments on multiple VLN benchmarks show that MonoDream consistently improves monocular navigation performance and significantly narrows the gap with panoramic-based agents.

## Content
Vision-Language Navigation (VLN) tasks often leverage panoramic RGB and depth inputs to provide rich spatial cues for action planning, but these sensors can be costly or less accessible in real-world deployments. Recent approaches based on Vision-Language Action (VLA) models achieve strong results with monocular input, yet they still lag behind methods using panoramic RGB-D information. We present MonoDream, a lightweight VLA framework that enables monocular agents to learn a Unified Navigation Representation (UNR). This shared feature representation jointly aligns navigation-relevant visual semantics (e.g., global layout, depth, and future cues) and language-grounded action intent, enabling more reliable action prediction. MonoDream further introduces Latent Panoramic Dreaming (LPD) tasks to supervise the UNR, which train the model to predict latent features of panoramic RGB and depth observations at both current and future steps based on only monocular input. Experiments on multiple VLN benchmarks show that MonoDream consistently improves monocular navigation performance and significantly narrows the gap with panoramic-based agents.

## 개요
Vision-Language Navigation (VLN) 작업은 종종 파노라마 RGB 및 깊이 입력을 활용하여 행동 계획에 풍부한 공간적 단서를 제공하지만, 이러한 센서는 실제 배포에서 비용이 많이 들거나 접근성이 낮을 수 있습니다. 최근 Vision-Language Action (VLA) 모델 기반 접근 방식은 단안 입력으로 강력한 결과를 달성하지만, 여전히 파노라마 RGB-D 정보를 사용하는 방법에 비해 뒤처져 있습니다. 우리는 단안 에이전트가 통합 내비게이션 표현(UNR)을 학습할 수 있게 하는 경량 VLA 프레임워크인 MonoDream을 제시합니다. 이 공유 특징 표현은 내비게이션 관련 시각적 의미(예: 전역 레이아웃, 깊이 및 미래 단서)와 언어 기반 행동 의도를 공동으로 정렬하여 더 신뢰할 수 있는 행동 예측을 가능하게 합니다. MonoDream은 또한 UNR을 감독하기 위해 잠재 파노라마 꿈꾸기(LPD) 작업을 도입하며, 이는 단안 입력만을 기반으로 현재 및 미래 단계에서 파노라마 RGB 및 깊이 관찰의 잠재 특징을 예측하도록 모델을 훈련합니다. 여러 VLN 벤치마크에 대한 실험은 MonoDream이 단안 내비게이션 성능을 지속적으로 개선하고 파노라마 기반 에이전트와의 격차를 크게 좁힌다는 것을 보여줍니다.

## 핵심 내용
Vision-Language Navigation (VLN) 작업은 종종 파노라마 RGB 및 깊이 입력을 활용하여 행동 계획에 풍부한 공간적 단서를 제공하지만, 이러한 센서는 실제 배포에서 비용이 많이 들거나 접근성이 낮을 수 있습니다. 최근 Vision-Language Action (VLA) 모델 기반 접근 방식은 단안 입력으로 강력한 결과를 달성하지만, 여전히 파노라마 RGB-D 정보를 사용하는 방법에 비해 뒤처져 있습니다. 우리는 단안 에이전트가 통합 내비게이션 표현(UNR)을 학습할 수 있게 하는 경량 VLA 프레임워크인 MonoDream을 제시합니다. 이 공유 특징 표현은 내비게이션 관련 시각적 의미(예: 전역 레이아웃, 깊이 및 미래 단서)와 언어 기반 행동 의도를 공동으로 정렬하여 더 신뢰할 수 있는 행동 예측을 가능하게 합니다. MonoDream은 또한 UNR을 감독하기 위해 잠재 파노라마 꿈꾸기(LPD) 작업을 도입하며, 이는 단안 입력만을 기반으로 현재 및 미래 단계에서 파노라마 RGB 및 깊이 관찰의 잠재 특징을 예측하도록 모델을 훈련합니다. 여러 VLN 벤치마크에 대한 실험은 MonoDream이 단안 내비게이션 성능을 지속적으로 개선하고 파노라마 기반 에이전트와의 격차를 크게 좁힌다는 것을 보여줍니다.
