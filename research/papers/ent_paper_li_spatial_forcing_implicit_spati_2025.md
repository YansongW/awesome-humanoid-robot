---
$id: ent_paper_li_spatial_forcing_implicit_spati_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model'
  zh: Spatial Forcing
  ko: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model'
summary:
  en: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (Spatial Forcing), is a
    2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and
    Technology (Guangzhou), Tsinghua University, Westlake University, Zhejiang University, South China University of Technology.'
  zh: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (Spatial Forcing), is a
    2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and
    Technology (Guangzhou), Tsinghua University, Westlake University, Zhejiang University, South China University of Technology.'
  ko: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (Spatial Forcing), is a
    2025 large vision-language-action model for robotic manipulation, introduced by The Hong Kong University of Science and
    Technology (Guangzhou), Tsinghua University, Westlake University, Zhejiang University, South China University of Technology.'
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
- robotic_manipulation
- spatial_forcing
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2510.12276v2.
sources:
- id: src_001
  type: paper
  title: 'Spatial Forcing: Implicit Spatial Representation Alignment for Vision-language-action Model (arXiv)'
  url: https://arxiv.org/abs/2510.12276
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: Spatial Forcing source
  url: https://doi.org/10.48550/arXiv.2510.12276
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions. However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in the 3D physical world. Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, hardware heterogeneity, and incomplete depth coverage in existing datasets. Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators. We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit 3D inputs or depth estimators. SF aligns intermediate visual embeddings of VLAs with geometric representations produced by pretrained 3D foundation models. By enforcing alignment at intermediate layers, SF guides VLAs to encode richer spatial representations that enhance action precision. Extensive experiments in simulation and real-world environments demonstrate that SF achieves state-of-the-art results, surpassing both 2D- and 3D-based VLAs. SF further accelerates training by up to 3.8x and improves data efficiency across diverse robotic tasks. Project page is at https://spatial-forcing.github.io/

## 核心内容
Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions. However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in the 3D physical world. Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, hardware heterogeneity, and incomplete depth coverage in existing datasets. Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators. We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit 3D inputs or depth estimators. SF aligns intermediate visual embeddings of VLAs with geometric representations produced by pretrained 3D foundation models. By enforcing alignment at intermediate layers, SF guides VLAs to encode richer spatial representations that enhance action precision. Extensive experiments in simulation and real-world environments demonstrate that SF achieves state-of-the-art results, surpassing both 2D- and 3D-based VLAs. SF further accelerates training by up to 3.8x and improves data efficiency across diverse robotic tasks. Project page is at https://spatial-forcing.github.io/

## 参考
- http://arxiv.org/abs/2510.12276v2

## Overview
Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions. However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in the 3D physical world. Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, hardware heterogeneity, and incomplete depth coverage in existing datasets. Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators. We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit 3D inputs or depth estimators. SF aligns intermediate visual embeddings of VLAs with geometric representations produced by pretrained 3D foundation models. By enforcing alignment at intermediate layers, SF guides VLAs to encode richer spatial representations that enhance action precision. Extensive experiments in simulation and real-world environments demonstrate that SF achieves state-of-the-art results, surpassing both 2D- and 3D-based VLAs. SF further accelerates training by up to 3.8x and improves data efficiency across diverse robotic tasks. Project page is at https://spatial-forcing.github.io/

## Content
Vision-language-action (VLA) models have recently shown strong potential in enabling robots to follow language instructions and execute precise actions. However, most VLAs are built upon vision-language models pretrained solely on 2D data, which lack accurate spatial awareness and hinder their ability to operate in the 3D physical world. Existing solutions attempt to incorporate explicit 3D sensor inputs such as depth maps or point clouds, but these approaches face challenges due to sensor noise, hardware heterogeneity, and incomplete depth coverage in existing datasets. Alternative methods that estimate 3D cues from 2D images also suffer from the limited performance of depth estimators. We propose Spatial Forcing (SF), a simple yet effective alignment strategy that implicitly forces VLA models to develop spatial comprehension capabilities without relying on explicit 3D inputs or depth estimators. SF aligns intermediate visual embeddings of VLAs with geometric representations produced by pretrained 3D foundation models. By enforcing alignment at intermediate layers, SF guides VLAs to encode richer spatial representations that enhance action precision. Extensive experiments in simulation and real-world environments demonstrate that SF achieves state-of-the-art results, surpassing both 2D- and 3D-based VLAs. SF further accelerates training by up to 3.8x and improves data efficiency across diverse robotic tasks. Project page is at https://spatial-forcing.github.io/

## 개요
Vision-language-action (VLA) 모델은 최근 로봇이 언어 명령을 따르고 정밀한 동작을 실행할 수 있도록 하는 데 강력한 잠재력을 보여주고 있습니다. 그러나 대부분의 VLA는 2D 데이터만으로 사전 학습된 vision-language 모델을 기반으로 구축되어 정확한 공간 인식이 부족하며, 3D 물리적 세계에서 작동하는 능력을 저해합니다. 기존 해결책은 깊이 맵이나 포인트 클라우드와 같은 명시적 3D 센서 입력을 통합하려고 시도하지만, 이러한 접근 방식은 센서 노이즈, 하드웨어 이질성, 기존 데이터셋의 불완전한 깊이 범위로 인해 어려움에 직면합니다. 2D 이미지에서 3D 단서를 추정하는 대체 방법 역시 깊이 추정기의 제한된 성능으로 인해 어려움을 겪습니다. 우리는 명시적 3D 입력이나 깊이 추정기에 의존하지 않고 VLA 모델이 암시적으로 공간 이해 능력을 개발하도록 강제하는 간단하면서도 효과적인 정렬 전략인 Spatial Forcing (SF)을 제안합니다. SF는 VLA의 중간 시각적 임베딩을 사전 학습된 3D 기반 모델이 생성한 기하학적 표현과 정렬합니다. 중간 계층에서 정렬을 강제함으로써 SF는 VLA가 동작 정밀도를 향상시키는 더 풍부한 공간 표현을 인코딩하도록 유도합니다. 시뮬레이션 및 실제 환경에서의 광범위한 실험을 통해 SF가 최첨단 결과를 달성하며, 2D 기반 및 3D 기반 VLA를 모두 능가함을 입증했습니다. SF는 또한 훈련 속도를 최대 3.8배 가속화하고 다양한 로봇 작업에서 데이터 효율성을 향상시킵니다. 프로젝트 페이지는 https://spatial-forcing.github.io/ 에 있습니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 최근 로봇이 언어 명령을 따르고 정밀한 동작을 실행할 수 있도록 하는 데 강력한 잠재력을 보여주고 있습니다. 그러나 대부분의 VLA는 2D 데이터만으로 사전 학습된 vision-language 모델을 기반으로 구축되어 정확한 공간 인식이 부족하며, 3D 물리적 세계에서 작동하는 능력을 저해합니다. 기존 해결책은 깊이 맵이나 포인트 클라우드와 같은 명시적 3D 센서 입력을 통합하려고 시도하지만, 이러한 접근 방식은 센서 노이즈, 하드웨어 이질성, 기존 데이터셋의 불완전한 깊이 범위로 인해 어려움에 직면합니다. 2D 이미지에서 3D 단서를 추정하는 대체 방법 역시 깊이 추정기의 제한된 성능으로 인해 어려움을 겪습니다. 우리는 명시적 3D 입력이나 깊이 추정기에 의존하지 않고 VLA 모델이 암시적으로 공간 이해 능력을 개발하도록 강제하는 간단하면서도 효과적인 정렬 전략인 Spatial Forcing (SF)을 제안합니다. SF는 VLA의 중간 시각적 임베딩을 사전 학습된 3D 기반 모델이 생성한 기하학적 표현과 정렬합니다. 중간 계층에서 정렬을 강제함으로써 SF는 VLA가 동작 정밀도를 향상시키는 더 풍부한 공간 표현을 인코딩하도록 유도합니다. 시뮬레이션 및 실제 환경에서의 광범위한 실험을 통해 SF가 최첨단 결과를 달성하며, 2D 기반 및 3D 기반 VLA를 모두 능가함을 입증했습니다. SF는 또한 훈련 속도를 최대 3.8배 가속화하고 다양한 로봇 작업에서 데이터 효율성을 향상시킵니다. 프로젝트 페이지는 https://spatial-forcing.github.io/ 에 있습니다.
