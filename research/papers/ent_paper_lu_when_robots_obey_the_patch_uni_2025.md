---
$id: ent_paper_lu_when_robots_obey_the_patch_uni_2025
$schema: ../../data/schema/v1/entry_schema.json
$version: 1
type: paper
names:
  en: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models'
  zh: UPA-RFAS
  ko: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models'
summary:
  en: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (UPA-RFAS), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, DSO
    National Laboratories.'
  zh: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (UPA-RFAS), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, DSO
    National Laboratories.'
  ko: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (UPA-RFAS), is a
    2025 large vision-language-action model for robotic manipulation, introduced by Nanyang Technological University, DSO
    National Laboratories.'
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
- upa_rfas
- vision_language_action
- vla
theoretical_depth:
- system
verification:
  status: partially_verified
  reviewed_by: ai
  reviewed_at: '2026-07-14'
  confidence: medium
  notes: Abstract backfilled by scripts/backfill_paper_abstracts.py from http://arxiv.org/abs/2511.21192v3.
sources:
- id: src_001
  type: paper
  title: 'When Robots Obey the Patch: Universal Transferable Patch Attacks on Vision-Language-Action Models (arXiv)'
  url: https://arxiv.org/abs/2511.21192
  date: '2025'
  accessed_at: '2026-07-01'
- id: src_002
  type: website
  title: UPA-RFAS source
  url: https://doi.org/10.48550/arXiv.2511.21192
  date: '2025'
  accessed_at: '2026-07-01'
---
## 概述
Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

## 核心内容
Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

## 参考
- http://arxiv.org/abs/2511.21192v3

## Overview
Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

## Content
Vision-Language-Action (VLA) models are vulnerable to adversarial attacks, yet universal and transferable attacks remain underexplored, as most existing patches overfit to a single model and fail in black-box settings. To address this gap, we present a systematic study of universal, transferable adversarial patches against VLA-driven robots under unknown architectures, finetuned variants, and sim-to-real shifts. We introduce UPA-RFAS (Universal Patch Attack via Robust Feature, Attention, and Semantics), a unified framework that learns a single physical patch in a shared feature space while promoting cross-model transfer. UPA-RFAS combines (i) a feature-space objective with an $\ell_1$ deviation prior and repulsive InfoNCE loss to induce transferable representation shifts, (ii) a robustness-augmented two-phase min-max procedure where an inner loop learns invisible sample-wise perturbations and an outer loop optimizes the universal patch against this hardened neighborhood, and (iii) two VLA-specific losses: Patch Attention Dominance to hijack text$\to$vision attention and Patch Semantic Misalignment to induce image-text mismatch without labels. Experiments across diverse VLA models, manipulation suites, and physical executions show that UPA-RFAS consistently transfers across models, tasks, and viewpoints, exposing a practical patch-based attack surface and establishing a strong baseline for future defenses.

## 개요
Vision-Language-Action (VLA) 모델은 적대적 공격에 취약하지만, 대부분의 기존 패치가 단일 모델에 과적합되어 블랙박스 환경에서 실패하기 때문에 보편적이고 전이 가능한 공격은 아직 충분히 연구되지 않았습니다. 이러한 격차를 해소하기 위해, 우리는 알려지지 않은 아키텍처, 미세 조정 변형, 시뮬레이션-실제 전환 하에서 VLA 기반 로봇을 대상으로 하는 보편적이고 전이 가능한 적대적 패치에 대한 체계적인 연구를 제시합니다. 우리는 UPA-RFAS(Universal Patch Attack via Robust Feature, Attention, and Semantics)를 소개합니다. 이는 공유된 특징 공간에서 단일 물리적 패치를 학습하면서 교차 모델 전이를 촉진하는 통합 프레임워크입니다. UPA-RFAS는 (i) $\ell_1$ 편차 사전 및 반발 InfoNCE 손실을 포함한 특징 공간 목표를 결합하여 전이 가능한 표현 변화를 유도하고, (ii) 내부 루프가 보이지 않는 샘플별 섭동을 학습하고 외부 루프가 이 강화된 이웃에 대해 보편적 패치를 최적화하는 강건성 강화 2단계 최소-최대 절차, (iii) 두 가지 VLA 특화 손실, 즉 텍스트→비전 주의를 탈취하는 패치 주의 지배(Patch Attention Dominance)와 레이블 없이 이미지-텍스트 불일치를 유도하는 패치 의미 불일치(Patch Semantic Misalignment)를 결합합니다. 다양한 VLA 모델, 조작 스위트, 물리적 실행에 걸친 실험은 UPA-RFAS가 모델, 작업, 시점 간에 일관되게 전이되어 실용적인 패치 기반 공격 표면을 노출하고 향후 방어를 위한 강력한 기준선을 수립함을 보여줍니다.

## 핵심 내용
Vision-Language-Action (VLA) 모델은 적대적 공격에 취약하지만, 대부분의 기존 패치가 단일 모델에 과적합되어 블랙박스 환경에서 실패하기 때문에 보편적이고 전이 가능한 공격은 아직 충분히 연구되지 않았습니다. 이러한 격차를 해소하기 위해, 우리는 알려지지 않은 아키텍처, 미세 조정 변형, 시뮬레이션-실제 전환 하에서 VLA 기반 로봇을 대상으로 하는 보편적이고 전이 가능한 적대적 패치에 대한 체계적인 연구를 제시합니다. 우리는 UPA-RFAS(Universal Patch Attack via Robust Feature, Attention, and Semantics)를 소개합니다. 이는 공유된 특징 공간에서 단일 물리적 패치를 학습하면서 교차 모델 전이를 촉진하는 통합 프레임워크입니다. UPA-RFAS는 (i) $\ell_1$ 편차 사전 및 반발 InfoNCE 손실을 포함한 특징 공간 목표를 결합하여 전이 가능한 표현 변화를 유도하고, (ii) 내부 루프가 보이지 않는 샘플별 섭동을 학습하고 외부 루프가 이 강화된 이웃에 대해 보편적 패치를 최적화하는 강건성 강화 2단계 최소-최대 절차, (iii) 두 가지 VLA 특화 손실, 즉 텍스트→비전 주의를 탈취하는 패치 주의 지배(Patch Attention Dominance)와 레이블 없이 이미지-텍스트 불일치를 유도하는 패치 의미 불일치(Patch Semantic Misalignment)를 결합합니다. 다양한 VLA 모델, 조작 스위트, 물리적 실행에 걸친 실험은 UPA-RFAS가 모델, 작업, 시점 간에 일관되게 전이되어 실용적인 패치 기반 공격 표면을 노출하고 향후 방어를 위한 강력한 기준선을 수립함을 보여줍니다.
