---
$id: ent_paper_li_vla_models_are_more_generaliza_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling'
  zh: FTM, FLA
  ko: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling'
summary:
  en: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (FTM, FLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab.'
  zh: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (FTM, FLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab.'
  ko: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (FTM, FLA), is a 2025 large
    vision-language-action model for robotic manipulation, introduced by Sun Yat-sen University, Guangdong Key Laboratory
    of Big Data Analysis and Processing, X-Era AI Lab.'
domains:
- 07_ai_models_algorithms
- 08_software_middleware
layers:
- intelligence
functional_roles:
- knowledge
- intelligence
tags:
- ftm_fla
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
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2512.02902v2.
sources:
- id: src_001
  type: paper
  title: 'VLA Models Are More Generalizable Than You Think: Revisiting Physical and Spatial Modeling (arXiv)'
  url: https://arxiv.org/abs/2512.02902
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: FTM, FLA source
  url: https://doi.org/10.48550/arXiv.2512.02902
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations. We show that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling. To address this, we propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Our first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Building on this, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters -- matching LoRA-scale finetuning at far lower cost. Together, these results reveal substantial untapped robustness in pretrained VLA models and demonstrate that targeted, minimal visual adaptation is sufficient to restore viewpoint generalization.

## 核心内容
Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations. We show that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling. To address this, we propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Our first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Building on this, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters -- matching LoRA-scale finetuning at far lower cost. Together, these results reveal substantial untapped robustness in pretrained VLA models and demonstrate that targeted, minimal visual adaptation is sufficient to restore viewpoint generalization.

## 参考
- http://arxiv.org/abs/2512.02902v2

## Overview
Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations. We show that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling. To address this, we propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Our first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Building on this, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters -- matching LoRA-scale finetuning at far lower cost. Together, these results reveal substantial untapped robustness in pretrained VLA models and demonstrate that targeted, minimal visual adaptation is sufficient to restore viewpoint generalization.

## Content
Vision-language-action (VLA) models achieve strong in-distribution performance but degrade sharply under novel camera viewpoints and visual perturbations. We show that this brittleness primarily arises from misalignment in Spatial Modeling, rather than Physical Modeling. To address this, we propose a one-shot adaptation framework that recalibrates visual representations through lightweight, learnable updates. Our first method, Feature Token Modulation (FTM), applies a global affine transformation to visual tokens and improves Libero viewpoint accuracy from 48.5% to 87.1% with only 4K parameters. Building on this, Feature Linear Adaptation (FLA) introduces low-rank updates to the ViT encoder, achieving 90.8% success with 4.7M parameters -- matching LoRA-scale finetuning at far lower cost. Together, these results reveal substantial untapped robustness in pretrained VLA models and demonstrate that targeted, minimal visual adaptation is sufficient to restore viewpoint generalization.

## 개요
Vision-language-action (VLA) 모델은 분포 내 성능이 뛰어나지만, 새로운 카메라 시점과 시각적 교란 하에서 성능이 급격히 저하됩니다. 본 연구는 이러한 취약성이 주로 물리적 모델링(Physical Modeling)이 아닌 공간 모델링(Spatial Modeling)의 정렬 불일치에서 비롯됨을 보여줍니다. 이를 해결하기 위해, 가볍고 학습 가능한 업데이트를 통해 시각적 표현을 재조정하는 원샷 적응 프레임워크를 제안합니다. 첫 번째 방법인 Feature Token Modulation (FTM)은 시각적 토큰에 전역 아핀 변환을 적용하여 단 4K 파라미터만으로 Libero 시점 정확도를 48.5%에서 87.1%로 향상시킵니다. 이를 기반으로 한 Feature Linear Adaptation (FLA)은 ViT 인코더에 저랭크 업데이트를 도입하여 4.7M 파라미터로 90.8%의 성공률을 달성하며, 훨씬 낮은 비용으로 LoRA 규모의 미세 조정과 동등한 성능을 보여줍니다. 이러한 결과들은 사전 학습된 VLA 모델에 상당한 미활용 강건성이 존재함을 밝히며, 표적화된 최소한의 시각적 적응만으로도 시점 일반화를 복원하기에 충분함을 입증합니다.

## 핵심 내용
Vision-language-action (VLA) 모델은 분포 내 성능이 뛰어나지만, 새로운 카메라 시점과 시각적 교란 하에서 성능이 급격히 저하됩니다. 본 연구는 이러한 취약성이 주로 물리적 모델링(Physical Modeling)이 아닌 공간 모델링(Spatial Modeling)의 정렬 불일치에서 비롯됨을 보여줍니다. 이를 해결하기 위해, 가볍고 학습 가능한 업데이트를 통해 시각적 표현을 재조정하는 원샷 적응 프레임워크를 제안합니다. 첫 번째 방법인 Feature Token Modulation (FTM)은 시각적 토큰에 전역 아핀 변환을 적용하여 단 4K 파라미터만으로 Libero 시점 정확도를 48.5%에서 87.1%로 향상시킵니다. 이를 기반으로 한 Feature Linear Adaptation (FLA)은 ViT 인코더에 저랭크 업데이트를 도입하여 4.7M 파라미터로 90.8%의 성공률을 달성하며, 훨씬 낮은 비용으로 LoRA 규모의 미세 조정과 동등한 성능을 보여줍니다. 이러한 결과들은 사전 학습된 VLA 모델에 상당한 미활용 강건성이 존재함을 밝히며, 표적화된 최소한의 시각적 적응만으로도 시점 일반화를 복원하기에 충분함을 입증합니다.
