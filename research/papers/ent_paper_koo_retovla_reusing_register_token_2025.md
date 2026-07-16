---
$id: ent_paper_koo_retovla_reusing_register_token_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models'
  zh: RetoVLA
  ko: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models'
summary:
  en: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (RetoVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by School of Computing, Gachon University.'
  zh: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (RetoVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by School of Computing, Gachon University.'
  ko: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (RetoVLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by School of Computing, Gachon University.'
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
- retovla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2509.21243v2.
sources:
- id: src_001
  type: paper
  title: 'RetoVLA: Reusing Register Tokens for Spatial Reasoning in Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2509.21243
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: RetoVLA source
  url: https://doi.org/10.48550/arXiv.2509.21243
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models have demonstrated robust performance across diverse robotic tasks. However, their high memory and computational demands often limit real-time deployment. While existing model compression techniques reduce the parameter footprint, they often drop in 3D spatial reasoning and scene layout understanding. This work introduces RetoVLA, an architecture designed to maintain spatial awareness in lightweight models by repurposing Register Tokens-learnable parameters originally introduced to mitigate attention artifacts in Vision Transformers. While these tokens are generally discarded once used, we repurpose them for their dense representation of global spatial context. RetoVLA integrates these recycled tokens directly into the action-planning module through a dedicated spatial context injection path. Our proposed design enables the recovery of global context without increasing the total parameter count. Real-world experiments using a 7-DOF manipulator show a 17.1%p improvement in average success rates over the baseline. Our results demonstrate that leveraging internal register tokens provides a highly effective mechanism for developing efficient, spatially-aware robotic agents. A video demonstration is available at: https://youtu.be/2CseBR-snZg

## 核心内容
Vision-Language-Action (VLA) models have demonstrated robust performance across diverse robotic tasks. However, their high memory and computational demands often limit real-time deployment. While existing model compression techniques reduce the parameter footprint, they often drop in 3D spatial reasoning and scene layout understanding. This work introduces RetoVLA, an architecture designed to maintain spatial awareness in lightweight models by repurposing Register Tokens-learnable parameters originally introduced to mitigate attention artifacts in Vision Transformers. While these tokens are generally discarded once used, we repurpose them for their dense representation of global spatial context. RetoVLA integrates these recycled tokens directly into the action-planning module through a dedicated spatial context injection path. Our proposed design enables the recovery of global context without increasing the total parameter count. Real-world experiments using a 7-DOF manipulator show a 17.1%p improvement in average success rates over the baseline. Our results demonstrate that leveraging internal register tokens provides a highly effective mechanism for developing efficient, spatially-aware robotic agents. A video demonstration is available at: https://youtu.be/2CseBR-snZg

## 参考
- http://arxiv.org/abs/2509.21243v2

## 개요
Vision-Language-Action (VLA) 모델은 다양한 로봇 작업에서 강력한 성능을 입증했습니다. 그러나 높은 메모리 및 계산 요구로 인해 실시간 배포가 제한되는 경우가 많습니다. 기존 모델 압축 기술은 파라미터 크기를 줄이지만, 3D 공간 추론 및 장면 레이아웃 이해에서 성능 저하가 자주 발생합니다. 본 연구는 Register Tokens(비전 트랜스포머에서 주의 아티팩트를 완화하기 위해 도입된 학습 가능한 파라미터)을 재활용하여 경량 모델에서 공간 인식을 유지하도록 설계된 아키텍처인 RetoVLA를 소개합니다. 이러한 토큰은 일반적으로 사용 후 폐기되지만, 우리는 이를 전역 공간 컨텍스트의 밀집 표현을 위해 재활용합니다. RetoVLA는 전용 공간 컨텍스트 주입 경로를 통해 이러한 재활용 토큰을 행동 계획 모듈에 직접 통합합니다. 제안된 설계는 총 파라미터 수를 증가시키지 않으면서 전역 컨텍스트를 복구할 수 있게 합니다. 7-DOF 매니퓰레이터를 사용한 실제 실험에서 기준선 대비 평균 성공률이 17.1%p 향상되었습니다. 본 결과는 내부 레지스터 토큰을 활용하는 것이 효율적이고 공간 인식이 가능한 로봇 에이전트를 개발하는 데 매우 효과적인 메커니즘을 제공함을 보여줍니다. 비디오 데모는 다음에서 확인할 수 있습니다: https://youtu.be/2CseBR-snZg

## 핵심 내용
Vision-Language-Action (VLA) 모델은 다양한 로봇 작업에서 강력한 성능을 입증했습니다. 그러나 높은 메모리 및 계산 요구로 인해 실시간 배포가 제한되는 경우가 많습니다. 기존 모델 압축 기술은 파라미터 크기를 줄이지만, 3D 공간 추론 및 장면 레이아웃 이해에서 성능 저하가 자주 발생합니다. 본 연구는 Register Tokens(비전 트랜스포머에서 주의 아티팩트를 완화하기 위해 도입된 학습 가능한 파라미터)을 재활용하여 경량 모델에서 공간 인식을 유지하도록 설계된 아키텍처인 RetoVLA를 소개합니다. 이러한 토큰은 일반적으로 사용 후 폐기되지만, 우리는 이를 전역 공간 컨텍스트의 밀집 표현을 위해 재활용합니다. RetoVLA는 전용 공간 컨텍스트 주입 경로를 통해 이러한 재활용 토큰을 행동 계획 모듈에 직접 통합합니다. 제안된 설계는 총 파라미터 수를 증가시키지 않으면서 전역 컨텍스트를 복구할 수 있게 합니다. 7-DOF 매니퓰레이터를 사용한 실제 실험에서 기준선 대비 평균 성공률이 17.1%p 향상되었습니다. 본 결과는 내부 레지스터 토큰을 활용하는 것이 효율적이고 공간 인식이 가능한 로봇 에이전트를 개발하는 데 매우 효과적인 메커니즘을 제공함을 보여줍니다. 비디오 데모는 다음에서 확인할 수 있습니다: https://youtu.be/2CseBR-snZg

## Overview
Vision-Language-Action (VLA) models have demonstrated robust performance across diverse robotic tasks. However, their high memory and computational demands often limit real-time deployment. While existing model compression techniques reduce the parameter footprint, they often drop in 3D spatial reasoning and scene layout understanding. This work introduces RetoVLA, an architecture designed to maintain spatial awareness in lightweight models by repurposing Register Tokens—learnable parameters originally introduced to mitigate attention artifacts in Vision Transformers. While these tokens are generally discarded once used, we repurpose them for their dense representation of global spatial context. RetoVLA integrates these recycled tokens directly into the action-planning module through a dedicated spatial context injection path. Our proposed design enables the recovery of global context without increasing the total parameter count. Real-world experiments using a 7-DOF manipulator show a 17.1%p improvement in average success rates over the baseline. Our results demonstrate that leveraging internal register tokens provides a highly effective mechanism for developing efficient, spatially-aware robotic agents. A video demonstration is available at: https://youtu.be/2CseBR-snZg

## Content
Vision-Language-Action (VLA) models have demonstrated robust performance across diverse robotic tasks. However, their high memory and computational demands often limit real-time deployment. While existing model compression techniques reduce the parameter footprint, they often drop in 3D spatial reasoning and scene layout understanding. This work introduces RetoVLA, an architecture designed to maintain spatial awareness in lightweight models by repurposing Register Tokens—learnable parameters originally introduced to mitigate attention artifacts in Vision Transformers. While these tokens are generally discarded once used, we repurpose them for their dense representation of global spatial context. RetoVLA integrates these recycled tokens directly into the action-planning module through a dedicated spatial context injection path. Our proposed design enables the recovery of global context without increasing the total parameter count. Real-world experiments using a 7-DOF manipulator show a 17.1%p improvement in average success rates over the baseline. Our results demonstrate that leveraging internal register tokens provides a highly effective mechanism for developing efficient, spatially-aware robotic agents. A video demonstration is available at: https://youtu.be/2CseBR-snZg
