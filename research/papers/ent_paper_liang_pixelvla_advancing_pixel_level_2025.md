---
$id: ent_paper_liang_pixelvla_advancing_pixel_level_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model'
  zh: PixelVLA
  ko: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model'
summary:
  en: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model (PixelVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Automation Science and Engineering, South China University of
    Technology, Shenyang Institute of Automation, Chinese Academy of Sciences, Mohamed bin Zayed University of Artificial
    Intelligence, Australian National University.'
  zh: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model (PixelVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Automation Science and Engineering, South China University of
    Technology, Shenyang Institute of Automation, Chinese Academy of Sciences, Mohamed bin Zayed University of Artificial
    Intelligence, Australian National University.'
  ko: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model (PixelVLA), is a 2025 large vision-language-action
    model for robotic manipulation, introduced by School of Automation Science and Engineering, South China University of
    Technology, Shenyang Institute of Automation, Chinese Academy of Sciences, Mohamed bin Zayed University of Artificial
    Intelligence, Australian National University.'
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
- pixelvla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.01571v2.
sources:
- id: src_001
  type: paper
  title: 'PixelVLA: Advancing Pixel-level Understanding in Vision-Language-Action Model (arXiv)'
  url: https://arxiv.org/abs/2511.01571
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: PixelVLA source
  url: https://doi.org/10.48550/arXiv.2511.01571
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action models (VLAs) are emerging as powerful tools for learning generalizable visuomotor control policies. However, current VLAs are mostly trained on large-scale image-text-action data and remain limited in two key ways: (i) they struggle with pixel-level scene understanding, and (ii) they rely heavily on textual prompts, which reduces their flexibility in real-world settings. To address these challenges, we introduce PixelVLA, the first VLA model designed to support both pixel-level reasoning and multimodal prompting with text and visual inputs. Our approach is built on a new visuomotor instruction tuning framework that integrates a multiscale pixel-aware encoder with a visual promptaware encoder. To train PixelVLA effectively, we further propose a two-stage automated annotation pipeline that generates Pixel-160K, a large-scale dataset with pixel-level annotations derived from existing robot data. Experiments on three standard VLA benchmarks and two VLA model variants show that PixelVLA improves manipulation success rates by 10.1%-28.7% over OpenVLA, while requiring only 1.5% of its pretraining cost. These results demonstrate that PixelVLA can be integrated into existing VLAs to enable more accurate, efficient, and versatile robot control in complex environments.

## 核心内容
Vision-Language-Action models (VLAs) are emerging as powerful tools for learning generalizable visuomotor control policies. However, current VLAs are mostly trained on large-scale image-text-action data and remain limited in two key ways: (i) they struggle with pixel-level scene understanding, and (ii) they rely heavily on textual prompts, which reduces their flexibility in real-world settings. To address these challenges, we introduce PixelVLA, the first VLA model designed to support both pixel-level reasoning and multimodal prompting with text and visual inputs. Our approach is built on a new visuomotor instruction tuning framework that integrates a multiscale pixel-aware encoder with a visual promptaware encoder. To train PixelVLA effectively, we further propose a two-stage automated annotation pipeline that generates Pixel-160K, a large-scale dataset with pixel-level annotations derived from existing robot data. Experiments on three standard VLA benchmarks and two VLA model variants show that PixelVLA improves manipulation success rates by 10.1%-28.7% over OpenVLA, while requiring only 1.5% of its pretraining cost. These results demonstrate that PixelVLA can be integrated into existing VLAs to enable more accurate, efficient, and versatile robot control in complex environments.

## 参考
- http://arxiv.org/abs/2511.01571v2

## Overview
Vision-Language-Action models (VLAs) are emerging as powerful tools for learning generalizable visuomotor control policies. However, current VLAs are mostly trained on large-scale image-text-action data and remain limited in two key ways: (i) they struggle with pixel-level scene understanding, and (ii) they rely heavily on textual prompts, which reduces their flexibility in real-world settings. To address these challenges, we introduce PixelVLA, the first VLA model designed to support both pixel-level reasoning and multimodal prompting with text and visual inputs. Our approach is built on a new visuomotor instruction tuning framework that integrates a multiscale pixel-aware encoder with a visual prompt-aware encoder. To train PixelVLA effectively, we further propose a two-stage automated annotation pipeline that generates Pixel-160K, a large-scale dataset with pixel-level annotations derived from existing robot data. Experiments on three standard VLA benchmarks and two VLA model variants show that PixelVLA improves manipulation success rates by 10.1%-28.7% over OpenVLA, while requiring only 1.5% of its pretraining cost. These results demonstrate that PixelVLA can be integrated into existing VLAs to enable more accurate, efficient, and versatile robot control in complex environments.

## Content
Vision-Language-Action models (VLAs) are emerging as powerful tools for learning generalizable visuomotor control policies. However, current VLAs are mostly trained on large-scale image-text-action data and remain limited in two key ways: (i) they struggle with pixel-level scene understanding, and (ii) they rely heavily on textual prompts, which reduces their flexibility in real-world settings. To address these challenges, we introduce PixelVLA, the first VLA model designed to support both pixel-level reasoning and multimodal prompting with text and visual inputs. Our approach is built on a new visuomotor instruction tuning framework that integrates a multiscale pixel-aware encoder with a visual prompt-aware encoder. To train PixelVLA effectively, we further propose a two-stage automated annotation pipeline that generates Pixel-160K, a large-scale dataset with pixel-level annotations derived from existing robot data. Experiments on three standard VLA benchmarks and two VLA model variants show that PixelVLA improves manipulation success rates by 10.1%-28.7% over OpenVLA, while requiring only 1.5% of its pretraining cost. These results demonstrate that PixelVLA can be integrated into existing VLAs to enable more accurate, efficient, and versatile robot control in complex environments.

## 개요
Vision-Language-Action 모델(VLA)은 일반화 가능한 시각-운동 제어 정책을 학습하기 위한 강력한 도구로 부상하고 있습니다. 그러나 현재의 VLA는 대부분 대규모 이미지-텍스트-행동 데이터로 훈련되며, 두 가지 주요 한계를 가지고 있습니다: (i) 픽셀 수준의 장면 이해에 어려움을 겪고, (ii) 텍스트 프롬프트에 크게 의존하여 실제 환경에서의 유연성이 떨어집니다. 이러한 문제를 해결하기 위해, 우리는 픽셀 수준 추론과 텍스트 및 시각 입력을 통한 다중 모드 프롬프트를 모두 지원하는 최초의 VLA 모델인 PixelVLA를 소개합니다. 우리의 접근 방식은 다중 스케일 픽셀 인식 인코더와 시각 프롬프트 인식 인코더를 통합하는 새로운 시각-운동 명령 튜닝 프레임워크를 기반으로 합니다. PixelVLA를 효과적으로 훈련하기 위해, 우리는 기존 로봇 데이터에서 파생된 픽셀 수준 주석이 포함된 대규모 데이터셋인 Pixel-160K를 생성하는 2단계 자동 주석 파이프라인을 추가로 제안합니다. 세 가지 표준 VLA 벤치마크와 두 가지 VLA 모델 변형에 대한 실험 결과, PixelVLA는 OpenVLA 대비 조작 성공률을 10.1%~28.7% 향상시키면서 사전 훈련 비용은 1.5%만 필요로 합니다. 이러한 결과는 PixelVLA가 기존 VLA에 통합되어 복잡한 환경에서 더 정확하고 효율적이며 다재다능한 로봇 제어를 가능하게 함을 보여줍니다.

## 핵심 내용
Vision-Language-Action 모델(VLA)은 일반화 가능한 시각-운동 제어 정책을 학습하기 위한 강력한 도구로 부상하고 있습니다. 그러나 현재의 VLA는 대부분 대규모 이미지-텍스트-행동 데이터로 훈련되며, 두 가지 주요 한계를 가지고 있습니다: (i) 픽셀 수준의 장면 이해에 어려움을 겪고, (ii) 텍스트 프롬프트에 크게 의존하여 실제 환경에서의 유연성이 떨어집니다. 이러한 문제를 해결하기 위해, 우리는 픽셀 수준 추론과 텍스트 및 시각 입력을 통한 다중 모드 프롬프트를 모두 지원하는 최초의 VLA 모델인 PixelVLA를 소개합니다. 우리의 접근 방식은 다중 스케일 픽셀 인식 인코더와 시각 프롬프트 인식 인코더를 통합하는 새로운 시각-운동 명령 튜닝 프레임워크를 기반으로 합니다. PixelVLA를 효과적으로 훈련하기 위해, 우리는 기존 로봇 데이터에서 파생된 픽셀 수준 주석이 포함된 대규모 데이터셋인 Pixel-160K를 생성하는 2단계 자동 주석 파이프라인을 추가로 제안합니다. 세 가지 표준 VLA 벤치마크와 두 가지 VLA 모델 변형에 대한 실험 결과, PixelVLA는 OpenVLA 대비 조작 성공률을 10.1%~28.7% 향상시키면서 사전 훈련 비용은 1.5%만 필요로 합니다. 이러한 결과는 PixelVLA가 기존 VLA에 통합되어 복잡한 환경에서 더 정확하고 효율적이며 다재다능한 로봇 제어를 가능하게 함을 보여줍니다.
